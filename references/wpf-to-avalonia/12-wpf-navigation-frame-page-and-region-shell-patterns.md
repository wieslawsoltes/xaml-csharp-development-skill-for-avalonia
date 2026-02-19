# WPF Navigation Frame/Page and Region Shell Patterns to Avalonia

## Table of Contents
1. Scope and APIs
2. Navigation Mapping
3. Conversion Example
4. Avalonia C# Equivalent
5. Troubleshooting

## Scope and APIs

Primary WPF APIs:

- `NavigationWindow`
- `Frame` and `Page`
- region/content navigation patterns

Primary Avalonia patterns:

- `ContentControl` or `TransitioningContentControl` with view-model-based routing
- `TabControl`/`SplitView` shells for multi-surface navigation
- explicit navigation service abstractions

## Navigation Mapping

| WPF | Avalonia |
|---|---|
| `Frame.Navigate(page)` | update current route/view-model and swap content |
| `Page` classes | `UserControl` views + view-model route models |
| journal/history | explicit navigation stack service |

Avalonia core does not include a direct `Frame`/`Page` replacement control.

## Conversion Example

WPF XAML:

```xaml
<Frame x:Name="MainFrame" NavigationUIVisibility="Hidden" />
```

Avalonia XAML:

```xaml
<TransitioningContentControl xmlns="https://github.com/avaloniaui"
                             xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
                             xmlns:vm="using:MyApp.ViewModels"
                             x:DataType="vm:ShellViewModel"
                             Content="{CompiledBinding CurrentViewModel}" />
```

## Avalonia C# Equivalent

```csharp
using System.Collections.Generic;

public interface INavigationService
{
    void Navigate(object routeViewModel);
    bool CanGoBack { get; }
    void GoBack();
}

public sealed class NavigationService : INavigationService
{
    private readonly Stack<object> _history = new();
    private object? _current;

    public bool CanGoBack => _history.Count > 0;

    public void Navigate(object routeViewModel)
    {
        if (_current is not null)
            _history.Push(_current);

        _current = routeViewModel;
    }

    public void GoBack()
    {
        if (_history.Count > 0)
            _current = _history.Pop();
    }
}
```

## Troubleshooting

1. direct page class port creates tight coupling.
- separate route state from view implementation.

2. back stack behavior is inconsistent.
- centralize navigation history in one service.

3. complex shells become monolithic.
- split navigation into regions (`main`, `sidebar`, `dialog`) with independent state.
