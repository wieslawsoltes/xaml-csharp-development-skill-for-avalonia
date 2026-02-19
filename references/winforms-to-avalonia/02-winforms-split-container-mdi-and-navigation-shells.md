# WinForms SplitContainer, MDI, and Navigation Shells to Avalonia

## Table of Contents
1. Scope and APIs
2. Split Layout Mapping
3. MDI Mapping Strategy
4. Split and MDI Conversion Example
5. C# Equivalent
6. Troubleshooting

## Scope and APIs

Primary WinForms APIs:

- `SplitContainer` (`Orientation`, `SplitterDistance`, `Panel1MinSize`, `Panel2MinSize`)
- MDI (`IsMdiContainer`, `MdiParent`, `MdiChildren`)

Primary Avalonia APIs:

- `Grid` + `GridSplitter`
- `SplitView`
- `TabControl` for document-like shells
- multiple `Window` top-levels when needed

## Split Layout Mapping

| WinForms `SplitContainer` | Avalonia |
|---|---|
| `Orientation = Vertical` | `Grid ColumnDefinitions="*,Auto,*"` + vertical `GridSplitter` |
| `Orientation = Horizontal` | `Grid RowDefinitions="*,Auto,*"` + horizontal `GridSplitter` |
| `Panel1MinSize`/`Panel2MinSize` | `MinWidth`/`MinHeight` on hosted panels |
| `SplitterDistance` | initial star/absolute column or row sizing |

## MDI Mapping Strategy

Avalonia has no built-in MDI container equivalent. Preferred replacements:

- tabbed document shell: `TabControl` + document view-model collection,
- docked workspace shell: `Dock` library integration when advanced docking is required,
- true multi-window: create additional `Window` instances.

## Split and MDI Conversion Example

WinForms C#:

```csharp
var split = new SplitContainer
{
    Dock = DockStyle.Fill,
    Orientation = Orientation.Vertical,
    SplitterDistance = 320,
    Panel1MinSize = 220,
    Panel2MinSize = 300
};

split.Panel1.Controls.Add(new TreeView { Dock = DockStyle.Fill });
split.Panel2.Controls.Add(new TabControl { Dock = DockStyle.Fill });
Controls.Add(split);
```

Avalonia XAML:

```xaml
<Grid xmlns="https://github.com/avaloniaui"
      xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
      xmlns:vm="using:MyApp.ViewModels"
      x:DataType="vm:WorkspaceShellViewModel"
      ColumnDefinitions="320,6,*">
  <TreeView Grid.Column="0"
            MinWidth="220"
            ItemsSource="{CompiledBinding NavigationItems}" />

  <GridSplitter Grid.Column="1"
                Width="6"
                ResizeDirection="Columns"
                ResizeBehavior="PreviousAndNext" />

  <TabControl Grid.Column="2"
              MinWidth="300"
              ItemsSource="{CompiledBinding Documents}"
              SelectedItem="{CompiledBinding SelectedDocument}" />
</Grid>
```

## C# Equivalent

```csharp
using Avalonia.Controls;

var shell = new Grid
{
    ColumnDefinitions = ColumnDefinitions.Parse("320,6,*")
};

var nav = new TreeView { MinWidth = 220, ItemsSource = viewModel.NavigationItems };
Grid.SetColumn(nav, 0);

var splitter = new GridSplitter
{
    Width = 6,
    ResizeDirection = GridResizeDirection.Columns,
    ResizeBehavior = GridResizeBehavior.PreviousAndNext
};
Grid.SetColumn(splitter, 1);

var docs = new TabControl { MinWidth = 300, ItemsSource = viewModel.Documents };
Grid.SetColumn(docs, 2);

shell.Children.Add(nav);
shell.Children.Add(splitter);
shell.Children.Add(docs);
```

## Troubleshooting

1. Splitter does not move expected pane.
- set `ResizeBehavior="PreviousAndNext"` and ensure adjacent definitions exist.

2. MDI migration becomes brittle.
- switch to tabbed or docked document patterns instead of trying to emulate MDI internals.

3. Tab content is recreated too often.
- use stable view-model identities and data templates.
