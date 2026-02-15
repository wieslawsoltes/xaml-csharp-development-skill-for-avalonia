# Screens and Display Awareness

## Table of Contents
1. Scope and APIs
2. Screen Model
3. Monitor-Aware Patterns
4. Change Tracking Patterns
5. XAML-First and Code-Only Usage
6. Best Practices
7. Troubleshooting

## Scope and APIs

Primary APIs:
- `TopLevel.GetTopLevel(...)`
- `TopLevel.Screens`
- `Screens`
- `Screen`

Important members:
- `Screens.ScreenCount`
- `Screens.All`, `Screens.Primary`
- `Screens.ScreenFromBounds(...)`
- `Screens.ScreenFromPoint(...)`
- `Screens.ScreenFromTopLevel(...)`
- `Screens.ScreenFromVisual(...)`
- `Screens.RequestScreenDetails()`
- `Screens.Changed` event
- `Screen.Bounds`, `WorkingArea`, `Scaling`, `DisplayName`, `IsPrimary`, `CurrentOrientation`

Reference source files:
- `src/Avalonia.Controls/TopLevel.cs`
- `src/Avalonia.Controls/Screens.cs`
- `src/Avalonia.Controls/Platform/Screen.cs`

## Screen Model

Use `TopLevel.Screens` as read model for connected displays.

Model notes:
- `All` is platform-provided and can change over runtime.
- `WorkingArea` may differ from `Bounds` due to taskbars/notches.
- `Scaling` is per-display and relevant for pixel calculations.
- Some methods return null on mobile-like platforms for unsupported queries.

## Monitor-Aware Patterns

```csharp
using Avalonia;
using Avalonia.Controls;
using Avalonia.Platform;

public static class ScreenWorkflows
{
    public static Screen? GetCurrentScreen(Control anchor)
    {
        TopLevel? top = TopLevel.GetTopLevel(anchor);
        return top?.Screens?.ScreenFromVisual(anchor);
    }

    public static PixelRect? GetPrimaryWorkingArea(Control anchor)
    {
        TopLevel? top = TopLevel.GetTopLevel(anchor);
        return top?.Screens?.Primary?.WorkingArea;
    }
}
```

## Change Tracking Patterns

```csharp
using System;
using Avalonia.Controls;

public sealed class ScreenChangeTracker : IDisposable
{
    private readonly Screens? _screens;
    private readonly EventHandler _handler;

    public ScreenChangeTracker(TopLevel topLevel, Action onChanged)
    {
        _handler = (_, _) => onChanged();
        _screens = topLevel.Screens;
        if (_screens is not null)
            _screens.Changed += _handler;
    }

    public void Dispose()
    {
        if (_screens is not null)
            _screens.Changed -= _handler;
    }
}
```

## XAML-First and Code-Only Usage

Default mode:
- Surface display info through viewmodel properties bound in XAML.
- Keep screen query logic in services/viewmodels.
- Use code-only UI trees only when requested.

XAML-first complete example:

```xml
<UserControl xmlns="https://github.com/avaloniaui"
             xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
             xmlns:vm="using:MyApp.ViewModels"
             x:DataType="vm:DisplayViewModel">
  <StackPanel Margin="12" Spacing="8">
    <Button Content="Refresh Displays" Command="{CompiledBinding RefreshScreensCommand}" />
    <TextBlock Text="{CompiledBinding PrimaryDisplayName}" />
    <TextBlock Text="{CompiledBinding PrimaryWorkingAreaText}" />
  </StackPanel>
</UserControl>
```

Code-only alternative (on request):

```csharp
using Avalonia.Controls;

public static class CodeOnlyScreenSample
{
    public static string DescribePrimary(Control anchor)
    {
        TopLevel? top = TopLevel.GetTopLevel(anchor);
        Screen? primary = top?.Screens?.Primary;

        if (primary is null)
            return "No screen information available.";

        return $"{primary.DisplayName} {primary.WorkingArea} scale={primary.Scaling:0.##}";
    }
}
```

## Best Practices

- Re-query screens on `Screens.Changed` for dynamic environments.
- Use `WorkingArea` for window placement, not raw `Bounds`.
- Keep pixel vs logical coordinate conversions explicit.

## Troubleshooting

1. Screen query returns null:
- Visual is not attached to a `TopLevel`.
- Platform does not expose that query path.

2. Window placement looks wrong on multi-monitor setup:
- Used `Bounds` where `WorkingArea` should be used.
- Ignored per-display scaling.

3. Display names/details missing:
- Platform may require explicit `RequestScreenDetails()` and permission.
