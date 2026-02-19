# WPF Menus, ToolBars, ContextMenus, Status, and Tray to Avalonia

## Table of Contents
1. Scope and APIs
2. Command Surface Mapping
3. Conversion Example
4. Avalonia C# Equivalent
5. Troubleshooting

## Scope and APIs

Primary WPF APIs:

- `Menu`, `MenuItem`, `ContextMenu`
- `ToolBar`/`ToolBarTray`
- `StatusBar`

Primary Avalonia APIs:

- `Menu`, `MenuItem`, `ContextMenu`, `MenuFlyout`
- custom toolbar/status layouts using core panels
- `TrayIcon` and `NativeMenu`

## Command Surface Mapping

| WPF | Avalonia |
|---|---|
| `Menu`/`ContextMenu` | same controls |
| `ToolBar`/`ToolBarTray` | custom command row (`Grid`/`StackPanel`) |
| `StatusBar` | bottom bar using `Border`/`Grid` |
| tray integrations | `TrayIcon` attached to `Application` |

## Conversion Example

WPF XAML:

```xaml
<DockPanel>
  <Menu DockPanel.Dock="Top" />
  <ToolBarTray DockPanel.Dock="Top">
    <ToolBar>
      <Button Content="Refresh" Command="{Binding RefreshCommand}" />
    </ToolBar>
  </ToolBarTray>
  <StatusBar DockPanel.Dock="Bottom" />
</DockPanel>
```

Avalonia XAML:

```xaml
<DockPanel xmlns="https://github.com/avaloniaui"
           xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
           xmlns:vm="using:MyApp.ViewModels"
           x:DataType="vm:MainWindowViewModel">
  <Menu DockPanel.Dock="Top">
    <MenuItem Header="_File">
      <MenuItem Header="_Refresh" Command="{CompiledBinding RefreshCommand}" />
    </MenuItem>
  </Menu>

  <Border DockPanel.Dock="Top" Padding="8" Classes="toolbar-row">
    <StackPanel Orientation="Horizontal" Spacing="8">
      <Button Content="Refresh" Command="{CompiledBinding RefreshCommand}" />
    </StackPanel>
  </Border>

  <Border DockPanel.Dock="Bottom" Padding="6" Classes="status-row">
    <TextBlock Text="{CompiledBinding StatusText}" />
  </Border>
</DockPanel>
```

## Avalonia C# Equivalent

```csharp
using System;
using Avalonia;
using Avalonia.Controls;
using Avalonia.Platform;

using var iconStream = AssetLoader.Open(new Uri("avares://MyApp/Assets/app.ico"));
var trayIcon = new WindowIcon(iconStream);

TrayIcon.SetIcons(Application.Current!, new TrayIcons
{
    new TrayIcon
    {
        Icon = trayIcon,
        ToolTipText = "MyApp",
        Menu = new NativeMenu
        {
            new NativeMenuItem("Open") { Command = viewModel.OpenCommand },
            new NativeMenuItem("Exit") { Command = viewModel.ExitCommand }
        }
    }
});
```

## Troubleshooting

1. searching for direct `ToolBar`/`StatusBar` controls in core.
- build reusable bars with standard layout primitives.

2. menu shortcuts not firing.
- add `KeyBindings`/`HotKey` wiring in addition to gesture text.

3. tray menu does not show.
- ensure `TrayIcon.Icons` is set on `Application` and icon resource is valid.
