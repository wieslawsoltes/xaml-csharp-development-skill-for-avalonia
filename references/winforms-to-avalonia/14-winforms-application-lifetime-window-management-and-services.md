# WinForms Application Lifetime, Window Management, and Services to Avalonia

## Table of Contents
1. Scope and APIs
2. Lifetime Mapping
3. Window and Service Mapping
4. Conversion Example
5. C# Equivalent
6. Troubleshooting

## Scope and APIs

Primary WinForms APIs:

- `Application.Run(...)`
- `ApplicationContext`
- `Form.Show()`, `Form.ShowDialog()`

Primary Avalonia APIs:

- `AppBuilder.StartWithClassicDesktopLifetime(args)`
- `IClassicDesktopStyleApplicationLifetime`
- `Window.Show()`, `Window.ShowDialog(owner)`
- `TopLevel` service access (`StorageProvider`, `Clipboard`, `Launcher`)

## Lifetime Mapping

| WinForms | Avalonia |
|---|---|
| `Application.Run(new MainForm())` | configure lifetime and assign `MainWindow` in `App.OnFrameworkInitializationCompleted()` |
| `ApplicationContext` multi-window orchestration | lifetime-managed window creation and event wiring |
| blocking modal call chain | async dialog flows with `await ShowDialog(...)` |

## Window and Service Mapping

- use `IClassicDesktopStyleApplicationLifetime` as primary desktop lifetime.
- resolve runtime services from `TopLevel` instead of static global helpers.

## Conversion Example

WinForms C#:

```csharp
[STAThread]
static void Main()
{
    ApplicationConfiguration.Initialize();
    Application.Run(new MainForm());
}
```

Avalonia XAML (`App.axaml`):

```xaml
<Application xmlns="https://github.com/avaloniaui"
             xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
             x:Class="MyApp.App">
  <Application.Styles>
    <FluentTheme />
  </Application.Styles>
</Application>
```

## C# Equivalent

```csharp
using Avalonia;
using Avalonia.Controls.ApplicationLifetimes;

internal static class Program
{
    [STAThread]
    public static void Main(string[] args) => BuildAvaloniaApp().StartWithClassicDesktopLifetime(args);

    public static AppBuilder BuildAvaloniaApp()
        => AppBuilder.Configure<App>().UsePlatformDetect().LogToTrace();
}

public partial class App : Application
{
    public override void OnFrameworkInitializationCompleted()
    {
        if (ApplicationLifetime is IClassicDesktopStyleApplicationLifetime desktop)
            desktop.MainWindow = new MainWindow();

        base.OnFrameworkInitializationCompleted();
    }
}
```

## Troubleshooting

1. Main window never appears.
- ensure desktop lifetime is active and `MainWindow` is assigned.

2. Legacy global service calls fail.
- migrate to `TopLevel`-scoped services.

3. Modal dialogs block app shutdown unexpectedly.
- use async dialog workflows and explicit cancellation/close paths.
