# Data Templates and IDataTemplate Selector Patterns

## Table of Contents
1. Scope and APIs
2. Template Resolution Order
3. WPF TemplateSelector Equivalent in Avalonia
4. Typed Templates and DataType Rules
5. ItemTemplate, DisplayMemberBinding, and Recycling
6. TreeDataTemplate Patterns
7. Function Tree Templates and Template Utility APIs
8. Best Practices
9. Troubleshooting

## Scope and APIs

Primary APIs:
- `IDataTemplate`
- `IDataTemplate.Match(...)`
- `DataTemplates`
- `DataTemplateExtensions.FindDataTemplate(...)`
- `DataTemplate`
- `FuncDataTemplate`
- `IRecyclingDataTemplate`
- `ITypedDataTemplate`
- `ITreeDataTemplate`
- `FuncTreeDataTemplate`
- `FuncTreeDataTemplate<T>`
- `TemplateContent`
- `ItemsControl.ItemTemplate`
- `ContentPresenter.ContentTemplate`

Reference source files:
- `src/Avalonia.Controls/Templates/IDataTemplate.cs`
- `src/Avalonia.Controls/Templates/DataTemplates.cs`
- `src/Avalonia.Controls/Templates/DataTemplateExtensions.cs`
- `src/Avalonia.Controls/Templates/FuncDataTemplate.cs`
- `src/Avalonia.Controls/Templates/IRecyclingDataTemplate.cs`
- `src/Avalonia.Controls/Templates/ITypedDataTemplate.cs`
- `src/Avalonia.Controls/Templates/ITreeDataTemplate.cs`
- `src/Avalonia.Controls/Templates/FuncTreeDataTemplate.cs`
- `src/Avalonia.Controls/Templates/FuncTreeDataTemplate\`1.cs`
- `src/Avalonia.Controls/Templates/FuncTemplate\`1.cs`
- `src/Avalonia.Controls/Templates/FuncTemplate\`2.cs`
- `src/Avalonia.Controls/Templates/ITemplate\`1.cs`
- `src/Avalonia.Controls/Templates/ITemplate\`2.cs`
- `src/Avalonia.Controls/Templates/FuncTemplateNameScopeExtensions.cs`
- `src/Markup/Avalonia.Markup.Xaml/Templates/DataTemplate.cs`
- `src/Markup/Avalonia.Markup.Xaml/Templates/TreeDataTemplate.cs`
- `src/Markup/Avalonia.Markup.Xaml/Templates/TemplateContent.cs`
- `src/Avalonia.Controls/Presenters/ContentPresenter.cs`
- `src/Avalonia.Controls/ItemsControl.cs`

## Template Resolution Order

`DataTemplateExtensions.FindDataTemplate(...)` resolves in this order:
1. Primary template (for example `ContentTemplate`/`ItemTemplate`) if `Match` succeeds.
2. Nearest logical-tree `IDataTemplateHost.DataTemplates` moving up ancestors.
3. Global app templates (`Application.DataTemplates` via `IGlobalDataTemplates`).

`ContentPresenter` then falls back to default templates when needed:
- `FuncDataTemplate.Default`
- `FuncDataTemplate.Access` when access-key rendering is enabled.

This precedence is critical when multiple templates can match the same data.

## WPF TemplateSelector Equivalent in Avalonia

Avalonia does not use WPF `DataTemplateSelector`; use `IDataTemplate` instead.

Selector-style implementation:

```csharp
using Avalonia.Controls;
using Avalonia.Controls.Templates;

public sealed class MessageTemplateSelector : IDataTemplate
{
    public bool Match(object? data) => data is MessageViewModel;

    public Control? Build(object? data)
    {
        return data switch
        {
            ErrorMessageViewModel vm => new ErrorMessageView { DataContext = vm },
            WarningMessageViewModel vm => new WarningMessageView { DataContext = vm },
            InfoMessageViewModel vm => new InfoMessageView { DataContext = vm },
            MessageViewModel vm => new DefaultMessageView { DataContext = vm },
            _ => null
        };
    }
}
```

Register in templates:

```xml
<Application.DataTemplates>
  <local:MessageTemplateSelector />
</Application.DataTemplates>
```

Alternative selector pattern with `FuncDataTemplate` ordering:

```csharp
var templates = new DataTemplates
{
    new FuncDataTemplate<ErrorMessageViewModel>((vm, _) => new ErrorMessageView { DataContext = vm }),
    new FuncDataTemplate<MessageViewModel>((vm, _) => new DefaultMessageView { DataContext = vm })
};
```

## Typed Templates and DataType Rules

Important rule from `DataTemplates`:
- Any `ITypedDataTemplate` in a `DataTemplates` collection must have `DataType` set.

Example:

```xml
<Application.DataTemplates>
  <DataTemplate x:DataType="vm:DashboardViewModel">
    <views:DashboardView />
  </DataTemplate>
</Application.DataTemplates>
```

Untyped custom `IDataTemplate` implementations can still participate without `DataType`.

## ItemTemplate, DisplayMemberBinding, and Recycling

`ItemsControl` behavior highlights:
- `ItemTemplate` and `DisplayMemberBinding` are mutually exclusive.
- `DisplayMemberBinding` internally creates a `FuncDataTemplate` with a `TextBlock`.

Recycling:
- Use `IRecyclingDataTemplate.Build(data, existing)` for recyclable scenarios.
- `FuncDataTemplate(..., supportsRecycling: true)` opts in to reusing controls.

Example:

```csharp
listBox.ItemTemplate = new FuncDataTemplate<RowViewModel>(
    (row, _) => new RowView { DataContext = row },
    supportsRecycling: true);
```

## TreeDataTemplate Patterns

For hierarchical data, use `TreeDataTemplate`/`ITreeDataTemplate`.

```xml
<TreeDataTemplate xmlns="https://github.com/avaloniaui"
                  xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
                  xmlns:vm="using:MyApp.ViewModels"
                  x:DataType="vm:NodeViewModel"
                  ItemsSource="{CompiledBinding Children}">
  <TextBlock Text="{CompiledBinding Title}" />
</TreeDataTemplate>
```

In `11.3.12`, `TreeDataTemplate.ItemsSource` supports:
- `Binding`
- `CompiledBindingExtension`

## Function Tree Templates and Template Utility APIs

Function-based tree templates:
- `FuncTreeDataTemplate`
- `FuncTreeDataTemplate<T>`
- `FuncTreeDataTemplate(Type type, Func<object?, INameScope, Control> build, Func<object?, IEnumerable> itemsSelector)`
- `FuncTreeDataTemplate(Func<object?, bool> match, Func<object?, INameScope, Control?> build, Func<object?, IEnumerable> itemsSelector)`
- `FuncTreeDataTemplate(Func<T, INameScope, Control> build, Func<T, IEnumerable> itemsSelector)`
- `FuncTreeDataTemplate(Func<T, bool> match, Func<T, INameScope, Control> build, Func<T, IEnumerable> itemsSelector)`

Template utility contracts often used with this space:
- `ITemplate<TControl>`
- `ITemplate<TParam, TControl>`
- `FuncTemplate<TControl>`
- `FuncTemplate<TParam, TControl>`
- `FuncTemplateNameScopeExtensions.RegisterInNameScope<T>(...)`
- `TemplateContent.Load(...)`

API-index compatibility note:
- [`references/api-index-generated.md`](api-index-generated) includes `FuncTreeDataTemplate.ItemsSelector(object item)` and `TreeDataTemplate.ItemsSelector(object item)` signatures.
- In app authoring, use `FuncTreeDataTemplate` selector delegates and `TreeDataTemplate.ItemsSource` as primary configuration paths.

For end-to-end advanced coverage of these APIs, see:
- [`51-template-content-and-func-template-patterns.md`](51-template-content-and-func-template-patterns)

## Best Practices

- Treat `IDataTemplate.Match` as fast and deterministic.
- Prefer typed templates (`x:DataType`) for clarity and compiled-binding alignment.
- Keep template ordering intentional; first match wins.
- Use selector templates for branching logic, not viewmodels.
- Use recycling templates only when the control can be safely reset/rebound.

## Troubleshooting

1. Wrong template applied:
- A broader template matched earlier in order.
- Local template host shadows global app templates.

2. Exception adding template to `DataTemplates`:
- Typed template missing `DataType`.

3. Item template appears ignored:
- `DisplayMemberBinding` is also set (not allowed with `ItemTemplate`).

4. Recycled item shows stale state:
- Template opted into recycling but control state is not reset correctly.

5. Tree template children not showing:
- `ItemsSource` binding is invalid or not one-way observable for children.
