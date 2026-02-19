# WinForms MenuStrip, ToolStrip, ContextMenuStrip, Status, and Tray to Avalonia

## Table of Contents
1. Scope and APIs
2. Menu and Command Surface Mapping
3. Conversion Example
4. C# Equivalent
5. Troubleshooting

## Scope and APIs

Primary WinForms APIs:

- `MenuStrip`, `ToolStrip`, `ContextMenuStrip`, `StatusStrip`
- `NotifyIcon`

Primary Avalonia APIs:

- `Menu`, `MenuItem`, `ContextMenu`, `MenuFlyout`
- `NativeMenu`, `NativeMenuBar`
- `TrayIcon` / `TrayIcons`
- custom top/bottom bars with `Grid`/`Border` (no direct `ToolStrip`/`StatusStrip` control in core)

## Menu and Command Surface Mapping

| WinForms | Avalonia |
|---|---|
| `MenuStrip` | `Menu` / `NativeMenuBar` |
| `ContextMenuStrip` | `ContextMenu` |
| `ToolStrip` | custom horizontal command row (`StackPanel`/`Grid`) |
| `StatusStrip` | bottom-aligned `Border`/`Grid` status region |
| `NotifyIcon` | `TrayIcon` attached to `Application` |

## Conversion Example

WinForms C#:

```csharp
var menu = new MenuStrip();
menu.Items.Add(new ToolStripMenuItem("File"));

var tool = new ToolStrip();
tool.Items.Add(new ToolStripButton("Refresh", null, (_, _) => RefreshData()));

var status = new StatusStrip();
status.Items.Add(new ToolStripStatusLabel("Ready"));

var tray = new NotifyIcon { Text = "MyApp", Visible = true, Icon = SystemIcons.Application };
```

Avalonia XAML (`MainWindow.axaml`):

```xaml
<DockPanel xmlns="https://github.com/avaloniaui"
           xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
           xmlns:vm="using:MyApp.ViewModels"
           x:DataType="vm:MainWindowViewModel">
  <Menu DockPanel.Dock="Top">
    <MenuItem Header="_File">
      <MenuItem Header="_Refresh" Command="{CompiledBinding RefreshCommand}" InputGesture="Ctrl+R" />
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

  <ContentPresenter />
</DockPanel>
```

Avalonia XAML (`App.axaml`, tray):

```xaml
<Application xmlns="https://github.com/avaloniaui"
             xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
             x:Class="MyApp.App">
  <TrayIcon.Icons>
    <TrayIcons>
      <TrayIcon Icon="avares://MyApp/Assets/app.ico" ToolTipText="MyApp">
        <TrayIcon.Menu>
          <NativeMenu>
            <NativeMenuItem Header="Open" />
            <NativeMenuItem Header="Exit" />
          </NativeMenu>
        </TrayIcon.Menu>
      </TrayIcon>
    </TrayIcons>
  </TrayIcon.Icons>
</Application>
```

Assign menu item commands in application startup code when the app command surface is initialized.

## C# Equivalent

```csharp
using System;
using Avalonia;
using Avalonia.Controls;
using Avalonia.Platform;

var menu = new Menu
{
    Items =
    {
        new MenuItem
        {
            Header = "_File",
            Items = { new MenuItem { Header = "_Refresh", Command = viewModel.RefreshCommand } }
        }
    }
};

using var iconStream = AssetLoader.Open(new Uri("avares://MyApp/Assets/app.ico"));
var trayWindowIcon = new WindowIcon(iconStream);

TrayIcon.SetIcons(Application.Current!, new TrayIcons
{
    new TrayIcon
    {
        Icon = trayWindowIcon,
        ToolTipText = "MyApp",
        Menu = new NativeMenu
        {
            new NativeMenuItem("Open") { Command = viewModel.OpenMainWindowCommand },
            new NativeMenuItem("Exit") { Command = viewModel.ExitCommand }
        }
    }
});
```

## Troubleshooting

1. Looking for direct `ToolStrip` or `StatusStrip` in Avalonia core.
- build reusable command/status bars with standard layout controls.

2. Tray menu does not appear.
- ensure tray icons are registered on `Application` via `TrayIcon.Icons`.

3. Shortcut hint shown but action not triggered.
- pair menu `InputGesture` with `HotKey` or root `KeyBindings`.
