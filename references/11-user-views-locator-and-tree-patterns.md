# User Views, View Locator, and Tree Patterns

## Table of Contents
1. Scope and APIs
2. View Locator Patterns
3. Reflection-Free Locator Pattern
4. Logical vs Visual Tree
5. Best Practices
6. Troubleshooting

## Scope and APIs

Primary APIs:
- `IDataTemplate`
- `DataTemplate`
- `DataTemplates`
- `FuncDataTemplate`
- `ITypedDataTemplate`
- `LogicalExtensions`
- `VisualExtensions`

Reference source files:
- `src/Avalonia.Controls/Templates/IDataTemplate.cs`
- `src/Avalonia.Controls/Templates/DataTemplates.cs`
- `src/Avalonia.Controls/Templates/FuncDataTemplate.cs`
- `src/Avalonia.Base/LogicalTree/LogicalExtensions.cs`
- `src/Avalonia.Base/VisualTree/VisualExtensions.cs`
- `samples/SafeAreaDemo/ViewLocator.cs`

## View Locator Patterns

Avalonia resolves view content via data templates. For view-model-driven composition:
- Place templates under `Application.DataTemplates` or local `DataTemplates`.
- Match on VM type and build the corresponding view.

Important detail from `DataTemplates` API:
- Templates inside a `DataTemplates` collection must have `DataType` when typed.

Example usage in app resources:

```xml
<Application.DataTemplates>
  <local:ViewLocator />
</Application.DataTemplates>
```

## Reflection-Free Locator Pattern

The sample `ViewLocator` uses `Type.GetType` and `Activator.CreateInstance`, which is simple but not trim/AOT friendly.

Prefer explicit registration:

```csharp
using Avalonia.Controls;
using Avalonia.Data;
using Avalonia.Controls.Templates;

public sealed class ViewLocator : IDataTemplate
{
    private readonly Dictionary<Type, Func<Control>> _map = new()
    {
        [typeof(MainViewModel)] = static () => new MainView(),
        [typeof(SettingsViewModel)] = static () => new SettingsView(),
    };

    public Control? Build(object? data)
    {
        if (data is null)
            return null;

        return _map.TryGetValue(data.GetType(), out var factory)
            ? factory()
            : new TextBlock { Text = $"No view for {data.GetType().Name}" };
    }

    public bool Match(object? data) => data is ViewModelBase;
}
```

Why this pattern is preferred:
- No runtime type-name string lookup.
- No `Activator` reflection path.
- Better compatibility with trimming and NativeAOT.

## Logical vs Visual Tree

Use the right tree for the job.

Logical tree APIs (`ILogical`, `LogicalExtensions`):
- `GetLogicalAncestors()`
- `FindLogicalAncestorOfType<T>()`
- `GetLogicalDescendants()`

Visual tree APIs (`VisualExtensions`):
- `GetVisualAncestors()`
- `FindAncestorOfType<T>()`
- `FindDescendantOfType<T>()`
- `GetVisualAt(point)`

Guidance:
- Resource lookup and data-context scope are mainly logical-tree concerns.
- Hit testing, transforms, and rendered structure are visual-tree concerns.
- For deep visual-tree diagnostics, see [`39-visual-tree-inspection-and-traversal.md`](39-visual-tree-inspection-and-traversal).
- For deep logical-tree diagnostics, see [`40-logical-tree-inspection-and-traversal.md`](40-logical-tree-inspection-and-traversal).

## Best Practices

- Resolve view content through templates, not manual `switch` in UI containers.
- Use typed templates and explicit `DataType` whenever possible.
- Keep view models independent from concrete views.
- Use logical-tree traversal for ownership/lifetime checks.
- Use visual-tree traversal for geometry/input/render behavior.

## Troubleshooting

1. Data template not chosen:
- `Match` returns false.
- For typed templates in `DataTemplates`, missing `DataType` can invalidate setup.

2. Wrong ancestor found:
- You used visual-tree APIs when logical parent chain was needed, or vice versa.

3. Locator fails after trimming:
- Reflection-based locator (`Type.GetType` + `Activator`) got trimmed.
- Replace with explicit dictionary/factory mapping.

4. Recycled item controls showing stale state:
- If using `IRecyclingDataTemplate`, ensure control state is fully rebound/reset.

## XAML-First and Code-Only Usage

Default mode:
- Register view locator/data templates in XAML first.
- Use code-only host composition only when requested.

XAML-first complete example:

```xml
<Application xmlns="https://github.com/avaloniaui"
             xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
             xmlns:local="using:MyApp"
             x:Class="MyApp.App">
  <Application.DataTemplates>
    <local:ViewLocator />
  </Application.DataTemplates>
</Application>
```

```xml
<ContentControl xmlns="https://github.com/avaloniaui"
                xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
                Content="{Binding CurrentViewModel}" />
```

Code-only alternative (on request):

```csharp
using Avalonia.Controls;

var host = new ContentControl
{
    DataContext = shellViewModel
};
host.Bind(ContentControl.ContentProperty, new Binding(nameof(ShellViewModel.CurrentViewModel)));

// Locator still maps VM -> View via IDataTemplate.
```
