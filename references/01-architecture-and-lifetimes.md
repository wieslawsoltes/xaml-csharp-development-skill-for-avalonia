# Architecture and Lifetime Patterns

## Goals

- Keep startup deterministic.
- Keep app lifetime logic explicit and testable.
- Keep platform-specific behavior in one place.

## Recommended Project Shape

- `Program.cs`: platform startup (`BuildAvaloniaApp`, `StartWithClassicDesktopLifetime`, browser start, etc).
- `App.axaml` + `App.axaml.cs`: global resources, theme, and lifetime-based root assignment.
- `Views/`: `Window`, `UserControl`, template resources.
- `ViewModels/`: state, commands, async workflows, observables.
- `Services/`: I/O, persistence, HTTP, domain logic.

## Startup Baseline

```csharp
using System;
using Avalonia;

internal static class Program
{
    [STAThread]
    public static int Main(string[] args)
        => BuildAvaloniaApp().StartWithClassicDesktopLifetime(args);

    public static AppBuilder BuildAvaloniaApp()
        => AppBuilder.Configure<App>()
            .UsePlatformDetect();
}
```

## App Baseline (Desktop + SingleView + Activation Feature)

```csharp
using Avalonia;
using Avalonia.Controls;
using Avalonia.Controls.ApplicationLifetimes;
using Avalonia.Markup.Xaml;
using Avalonia.Platform;

public class App : Application
{
    public override void Initialize()
        => AvaloniaXamlLoader.Load(this);

    public override void OnFrameworkInitializationCompleted()
    {
        if (ApplicationLifetime is IClassicDesktopStyleApplicationLifetime desktop)
        {
            desktop.MainWindow = new MainWindow
            {
                DataContext = new MainWindowViewModel()
            };
        }
        else if (ApplicationLifetime is ISingleViewApplicationLifetime singleView)
        {
            singleView.MainView = new MainView
            {
                DataContext = new MainViewModel()
            };
        }

        if (Application.Current?.TryGetFeature<IActivatableLifetime>() is { } activatable)
        {
            activatable.Activated += (_, _) => { };
            activatable.Deactivated += (_, _) => { };
        }

        base.OnFrameworkInitializationCompleted();
    }
}
```

## Lifetime Selection Rules

- Choose `IClassicDesktopStyleApplicationLifetime` when multiple windows/dialogs/system menu integration are required.
- Choose `ISingleViewApplicationLifetime` when the host presents one root view (browser/mobile shell).
- Use `IActivatableLifetime` feature hooks when you need activation/deactivation events from the host platform.

## Shutdown Behavior

Desktop controls:
- `ShutdownMode`:
  - `OnLastWindowClose` for consumer desktop apps.
  - `OnMainWindowClose` for strict primary-window behavior.
  - `OnExplicitShutdown` for background/tray-style apps.
- `ShutdownRequested` to inspect/cancel shutdown requests.

Use:
- Keep shutdown policy in one place (e.g., startup/lifetime config).
- Avoid hidden calls to `Shutdown()` from deeply nested UI components.

## `AppBuilder.With<TOptions>` Pattern

Use options binding instead of scattered globals:

```csharp
public static AppBuilder BuildAvaloniaApp()
    => AppBuilder.Configure<App>()
        .UsePlatformDetect()
        .With(new Win32PlatformOptions
        {
            RenderingMode = new[]
            {
                Win32RenderingMode.AngleEgl,
                Win32RenderingMode.Software
            }
        })
        .With(new X11PlatformOptions
        {
            RenderingMode = new[]
            {
                X11RenderingMode.Glx,
                X11RenderingMode.Software
            }
        });
```

## Service Registration Strategy

`Application.RegisterServices()` is the framework-level default service registration hook.

Guidance:
- Keep app-specific service wiring explicit and centralized.
- Avoid service location from random controls; inject through constructors/factories where possible.
- If using external DI container, bridge it once during startup.

## Common Architecture Mistakes

1. Mixing startup, navigation, and business logic in `Program.cs`.
- Fix: keep `Program.cs` minimal; perform app-level branching in `App`.

2. Assigning `MainWindow`/`MainView` before lifetime is set.
- Fix: assign roots inside `OnFrameworkInitializationCompleted()`.

3. Duplicating platform setup in multiple entry points.
- Fix: one shared `BuildAvaloniaApp()` plus thin platform launchers.

4. Hiding shutdown side-effects in viewmodels.
- Fix: route shutdown through a dedicated application service/lifetime adapter.

## XAML-First and Code-Only Usage

Default mode:
- Use XAML for root view composition and compiled bindings.
- Use code-only root/view setup only when requested.

XAML-first references:
- `App.axaml`, `MainWindow.axaml`, `x:DataType`, compiled bindings

XAML-first usage example:

```xml
<Application xmlns="https://github.com/avaloniaui"
             xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
             x:Class="MyApp.App">
  <Application.Styles>
    <FluentTheme />
  </Application.Styles>
</Application>
```

```xml
<Window xmlns="https://github.com/avaloniaui"
        xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
        xmlns:vm="using:MyApp.ViewModels"
        x:Class="MyApp.MainWindow"
        x:DataType="vm:MainWindowViewModel">
  <TextBlock Text="{CompiledBinding Title}" />
</Window>
```

Code-only alternative (on request):

```csharp
desktop.MainWindow = new Window
{
    DataContext = new MainWindowViewModel(),
    Content = new StackPanel
    {
        Children =
        {
            new TextBlock { [!TextBlock.TextProperty] = new Binding("Title") }
        }
    }
};
```
