# WinForms ToolStrip DropDown and SplitButton Patterns to Avalonia

## Table of Contents
1. Scope and APIs
2. Command Surface Mapping
3. Conversion Example
4. C# Equivalent
5. Troubleshooting

## Scope and APIs

Primary WinForms APIs:

- `ToolStripDropDownButton`
- `ToolStripSplitButton`
- `ToolStripMenuItem`

Primary Avalonia APIs:

- `DropDownButton`
- `SplitButton`
- `MenuFlyout`, `MenuItem`, `Separator`

## Command Surface Mapping

| WinForms | Avalonia |
|---|---|
| `ToolStripDropDownButton` + menu items | `DropDownButton` + `MenuFlyout` |
| `ToolStripSplitButton` primary + dropdown actions | `SplitButton` primary command + `Flyout` |
| `ToolStripMenuItem.Click` handlers | `ICommand` on `MenuItem`/button controls |
| ad-hoc toolbar event wiring | command-first toolbar view-model patterns |

## Conversion Example

WinForms C#:

```csharp
var run = new ToolStripSplitButton("Run");
run.ButtonClick += (_, _) => RunNow();
run.DropDownItems.Add("Run Full", null, (_, _) => RunFull());
run.DropDownItems.Add("Run Selected", null, (_, _) => RunSelected());

var export = new ToolStripDropDownButton("Export");
export.DropDownItems.Add("CSV", null, (_, _) => ExportCsv());
export.DropDownItems.Add("JSON", null, (_, _) => ExportJson());
toolStrip1.Items.Add(run);
toolStrip1.Items.Add(export);
```

Avalonia XAML:

```xaml
<UserControl xmlns="https://github.com/avaloniaui"
             xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
             xmlns:vm="using:MyApp.ViewModels"
             x:DataType="vm:CommandBarViewModel">
  <StackPanel Orientation="Horizontal" Spacing="8">
    <SplitButton Content="Run"
                 Command="{CompiledBinding RunNowCommand}">
      <SplitButton.Flyout>
        <MenuFlyout>
          <MenuItem Header="Run Full"
                    Command="{CompiledBinding RunFullCommand}" />
          <MenuItem Header="Run Selected"
                    Command="{CompiledBinding RunSelectedCommand}" />
        </MenuFlyout>
      </SplitButton.Flyout>
    </SplitButton>

    <DropDownButton Content="Export">
      <DropDownButton.Flyout>
        <MenuFlyout>
          <MenuItem Header="CSV"
                    Command="{CompiledBinding ExportCsvCommand}" />
          <MenuItem Header="JSON"
                    Command="{CompiledBinding ExportJsonCommand}" />
          <Separator />
          <MenuItem Header="Open Export Folder"
                    Command="{CompiledBinding OpenExportFolderCommand}" />
        </MenuFlyout>
      </DropDownButton.Flyout>
    </DropDownButton>
  </StackPanel>
</UserControl>
```

## C# Equivalent

```csharp
using Avalonia.Controls;

var runFlyout = new MenuFlyout
{
    Items =
    {
        new MenuItem { Header = "Run Full", Command = viewModel.RunFullCommand },
        new MenuItem { Header = "Run Selected", Command = viewModel.RunSelectedCommand }
    }
};

var runButton = new SplitButton
{
    Content = "Run",
    Command = viewModel.RunNowCommand,
    Flyout = runFlyout
};

var exportFlyout = new MenuFlyout
{
    Items =
    {
        new MenuItem { Header = "CSV", Command = viewModel.ExportCsvCommand },
        new MenuItem { Header = "JSON", Command = viewModel.ExportJsonCommand },
        new Separator(),
        new MenuItem { Header = "Open Export Folder", Command = viewModel.OpenExportFolderCommand }
    }
};

var exportButton = new DropDownButton
{
    Content = "Export",
    Flyout = exportFlyout
};
```

## Troubleshooting

1. Flyout commands execute in the wrong view-model scope.
- ensure flyout `DataContext` resolves to the toolbar view-model that owns commands.

2. Split button does not perform primary action.
- set `Command` on `SplitButton` itself, not only on flyout menu items.

3. Shortcut handling becomes inconsistent.
- centralize gestures with `KeyBinding` at `Window` level and keep menu/toolbar commands shared.
