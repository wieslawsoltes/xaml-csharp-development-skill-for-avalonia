# Template Content and Func Template Patterns

## Table of Contents
1. Scope and APIs
2. Generic Template Contracts (`ITemplate`)
3. Function Templates (`FuncTemplate`)
4. Name-Scope Registration Helpers
5. Control Templates and `IControlTemplate`
6. Recycling Data Templates (`IRecyclingDataTemplate`)
7. Tree Templates (`FuncTreeDataTemplate` and `TreeDataTemplate`)
8. Runtime Template Content Loading (`TemplateContent`)
9. Inspecting Applied Template Children (`TemplateExtensions`)
10. Best Practices
11. Troubleshooting

## Scope and APIs

Primary APIs:

- `ITemplate<TControl>`
- `ITemplate<TParam, TControl>`
- `FuncTemplate<TControl>`
- `FuncTemplate<TParam, TControl>`
- `FuncTemplateNameScopeExtensions`
- `RegisterInNameScope<T>(...)`
- `IControlTemplate`
- `IRecyclingDataTemplate`
- `FuncTreeDataTemplate`
- `FuncTreeDataTemplate<T>`
- `TreeDataTemplate`
- `TemplateContent`
- `TemplateExtensions`
- `TemplateExtensions.GetTemplateChildren(...)`

Frequently referenced signatures:

- `FuncTemplate(Func<TControl> func)`
- `FuncTemplate(Func<TParam, INameScope, TControl> func)`
- `FuncTreeDataTemplate(Type type, Func<object?, INameScope, Control> build, Func<object?, IEnumerable> itemsSelector)`
- `FuncTreeDataTemplate(Func<object?, bool> match, Func<object?, INameScope, Control?> build, Func<object?, IEnumerable> itemsSelector)`
- `FuncTreeDataTemplate(Func<T, INameScope, Control> build, Func<T, IEnumerable> itemsSelector)`
- `FuncTreeDataTemplate(Func<T, bool> match, Func<T, INameScope, Control> build, Func<T, IEnumerable> itemsSelector)`
- `FuncTreeDataTemplate.ItemsSelector(object item)`
- `TreeDataTemplate.ItemsSelector(object item)`
- `TemplateContent.Load(object? templateContent)`
- `TemplateContent.Load<T>(object? templateContent)`

Reference source files:

- `src/Avalonia.Controls/Templates/ITemplate\`1.cs`
- `src/Avalonia.Controls/Templates/ITemplate\`2.cs`
- `src/Avalonia.Controls/Templates/FuncTemplate\`1.cs`
- `src/Avalonia.Controls/Templates/FuncTemplate\`2.cs`
- `src/Avalonia.Controls/Templates/FuncTemplateNameScopeExtensions.cs`
- `src/Avalonia.Controls/Templates/IControlTemplate.cs`
- `src/Avalonia.Controls/Templates/IRecyclingDataTemplate.cs`
- `src/Avalonia.Controls/Templates/FuncTreeDataTemplate.cs`
- `src/Avalonia.Controls/Templates/FuncTreeDataTemplate\`1.cs`
- `src/Avalonia.Controls/Templates/TemplateExtensions.cs`
- `src/Markup/Avalonia.Markup.Xaml/Templates/TemplateContent.cs`
- `src/Markup/Avalonia.Markup.Xaml/Templates/TreeDataTemplate.cs`

## Generic Template Contracts (`ITemplate`)

Core contracts:

- `ITemplate<TControl>` builds a control with no explicit input parameter.
- `ITemplate<TParam, TControl>` builds a control from an explicit parameter.

These generic interfaces are the shared base for control templates, data-template helpers, and function-based builders.

Use:

- `ITemplate<TControl>` for template instances with implicit context.
- `ITemplate<TParam, TControl>` when the caller passes explicit state/input.

## Function Templates (`FuncTemplate`)

`FuncTemplate` wrappers let you build templates from strongly typed delegates.

Types:

- `FuncTemplate<TControl> : ITemplate<TControl>`
- `FuncTemplate<TParam, TControl> : ITemplate<TParam, TControl>`

Constructors:

- `FuncTemplate(Func<TControl> func)`
- `FuncTemplate(Func<TParam, INameScope, TControl> func)`

Example:

```csharp
using Avalonia.Controls;
using Avalonia.Controls.Templates;

var noArg = new FuncTemplate<TextBlock>(() => new TextBlock { Text = "Hello" });
TextBlock built = noArg.Build();

var withParam = new FuncTemplate<string, TextBlock>((value, scope) =>
{
    var text = new TextBlock { Name = "PART_Label", Text = value };
    return text.RegisterInNameScope(scope);
});

TextBlock builtWithParam = withParam.Build("Template value");
```

## Name-Scope Registration Helpers

`FuncTemplateNameScopeExtensions` provides helper registration for function-template output.

API:

- `FuncTemplateNameScopeExtensions`
- `RegisterInNameScope<T>(this T control, INameScope scope) where T : StyledElement`

Use this when function templates create named elements that must be discoverable from template name scope.

## Control Templates and `IControlTemplate`

`IControlTemplate` is the typed contract for `TemplatedControl` template building.

API:

- `IControlTemplate : ITemplate<TemplatedControl, TemplateResult<Control>?>`

Practical guidance:

- use `ControlTemplate` in XAML for normal app authoring,
- use function-backed control templates in C# only when dynamic template composition is required.

## Recycling Data Templates (`IRecyclingDataTemplate`)

`IRecyclingDataTemplate` extends `IDataTemplate` with recycle-aware build:

- `Control? Build(object? data, Control? existing)`

Use when item controls are frequently re-bound and you can reliably reset reused state.

If recycling is enabled, ensure state cleanup is deterministic:

- clear transient visual state,
- re-bind all data-dependent properties,
- avoid stale event handlers on reused controls.

## Tree Templates (`FuncTreeDataTemplate` and `TreeDataTemplate`)

Tree-template APIs:

- `FuncTreeDataTemplate`
- `FuncTreeDataTemplate<T>`
- `TreeDataTemplate`

Function-based hierarchical templates:

- `FuncTreeDataTemplate(Type type, Func<object?, INameScope, Control> build, Func<object?, IEnumerable> itemsSelector)`
- `FuncTreeDataTemplate(Func<object?, bool> match, Func<object?, INameScope, Control?> build, Func<object?, IEnumerable> itemsSelector)`
- `FuncTreeDataTemplate(Func<T, INameScope, Control> build, Func<T, IEnumerable> itemsSelector)`
- `FuncTreeDataTemplate(Func<T, bool> match, Func<T, INameScope, Control> build, Func<T, IEnumerable> itemsSelector)`

Example:

```csharp
using Avalonia.Controls;
using Avalonia.Controls.Templates;

var treeTemplate = new FuncTreeDataTemplate<MyNode>(
    build: (node, scope) => new TextBlock { Name = "PART_Title", Text = node.Title }.RegisterInNameScope(scope),
    itemsSelector: node => node.Children);
```

XAML tree template path:

```xml
<TreeDataTemplate xmlns="https://github.com/avaloniaui"
                  xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
                  xmlns:vm="using:MyApp.ViewModels"
                  x:DataType="vm:NodeViewModel"
                  ItemsSource="{CompiledBinding Children}">
  <TextBlock Text="{CompiledBinding Title}" />
</TreeDataTemplate>
```

API-index compatibility note:

- [`references/api-index-generated.md`](api-index-generated) includes `FuncTreeDataTemplate.ItemsSelector(object item)` and `TreeDataTemplate.ItemsSelector(object item)` signatures.
- In practical `11.3.12` usage, author against `FuncTreeDataTemplate` constructor selector functions and `TreeDataTemplate.ItemsSource`.

## Runtime Template Content Loading (`TemplateContent`)

`TemplateContent` is the loader utility used by markup template wrappers.

APIs:

- `TemplateContent`
- `TemplateContent.Load(object? templateContent)`
- `TemplateContent.Load<T>(object? templateContent)`

Use this when handling deferred template content in infrastructure code; app-level code normally consumes higher-level `ControlTemplate`, `DataTemplate`, and `TreeDataTemplate`.

## Inspecting Applied Template Children (`TemplateExtensions`)

`TemplateExtensions.GetTemplateChildren(this TemplatedControl control)` traverses controls created from the control's applied template.

Use cases:

- diagnostics in `OnApplyTemplate`,
- validating template part presence,
- custom visual policy checks that operate on applied template subtree.

Example:

```csharp
using Avalonia.Controls.Primitives;
using Avalonia.Controls.Templates;

protected override void OnApplyTemplate(TemplateAppliedEventArgs e)
{
    base.OnApplyTemplate(e);

    foreach (var child in this.GetTemplateChildren())
    {
        // Inspect template-built controls tied to this templated parent.
    }
}
```

## Best Practices

1. Prefer XAML templates first.
- Use `FuncTemplate`/function-template APIs for dynamic or infrastructure scenarios.

2. Keep `IRecyclingDataTemplate` opt-in and explicit.
- Recycle only when control reset behavior is proven safe.

3. Keep name-scope behavior deterministic.
- Register named function-template controls via `RegisterInNameScope(...)`.

4. Separate authoring and diagnostics concerns.
- Use `TemplateExtensions.GetTemplateChildren(...)` for diagnostics and verification, not routine business logic.

5. Keep tree-template child selection simple.
- Prefer stable child enumerable selection functions and avoid side effects in selectors.

## Troubleshooting

1. Template-built parts cannot be found by name.
- Ensure named controls are registered in the template `INameScope` (`RegisterInNameScope(...)` in function templates).

2. Recycled items show stale data.
- `IRecyclingDataTemplate.Build(data, existing)` must fully reset view state before reuse.

3. Tree nodes render but children do not expand.
- Verify child selector (`FuncTreeDataTemplate` selector or `TreeDataTemplate.ItemsSource`) returns expected enumerable.

4. Template traversal returns unexpected controls.
- `GetTemplateChildren(...)` is scoped to templated-parent ownership, not all visual descendants.

5. Template content fails to load.
- Validate that deferred content shape matches what `TemplateContent.Load(...)` expects.
