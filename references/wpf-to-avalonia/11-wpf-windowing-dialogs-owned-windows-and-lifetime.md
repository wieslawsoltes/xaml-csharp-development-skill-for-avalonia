# WPF Windowing, Dialogs, Owned Windows, and Lifetime to Avalonia

## Table of Contents
1. Scope and APIs
2. Lifetime Mapping
3. Dialog/Ownership Mapping
4. Conversion Example
5. Avalonia C# Equivalent
6. Troubleshooting

## Scope and APIs

Primary WPF APIs:

- `Application`, `Window`
- `StartupUri`
- `Show()`, `ShowDialog()`, owned windows

Primary Avalonia APIs:

- `AppBuilder.StartWithClassicDesktopLifetime(args)`
- `IClassicDesktopStyleApplicationLifetime`
- `Window.Show()`, `Window.ShowDialog(owner)`

## Lifetime Mapping

| WPF | Avalonia |
|---|---|
| `App.xaml` + `StartupUri` | assign `MainWindow` in `OnFrameworkInitializationCompleted()` |
| `Application.Current.Windows` | lifetime window tracking and explicit references |
| `ShutdownMode` assumptions | explicit close behavior via lifetime and window logic |

## Dialog/Ownership Mapping

| WPF | Avalonia |
|---|---|
| `child.Owner = this; child.Show();` | `child.Show(owner)` |
| `ShowDialog()` blocking | async `await ShowDialog(owner)` |

## Conversion Example

WPF C#:

```csharp
var settings = new SettingsWindow { Owner = this };
settings.ShowDialog();
```

Avalonia XAML:

```xaml
<Button xmlns="https://github.com/avaloniaui"
        xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
        xmlns:vm="using:MyApp.ViewModels"
        x:DataType="vm:MainWindowViewModel"
        Content="Settings"
        Command="{CompiledBinding OpenSettingsCommand}" />
```

## Avalonia C# Equivalent

```csharp
using System.Threading.Tasks;
using Avalonia.Controls;

public static async Task OpenSettingsAsync(Window owner)
{
    var settings = new Window
    {
        Width = 480,
        Height = 320,
        Title = "Settings"
    };

    await settings.ShowDialog(owner);
}
```

## Troubleshooting

1. Modal flows still coded as blocking chains.
- migrate to async command paths end-to-end.

2. ownerless dialogs appear behind main window.
- pass explicit owner when opening dialogs.

3. app does not exit as expected.
- verify main window lifetime and explicit shutdown conditions.
