# WinForms Splitter, ScrollableControl, AutoScroll to Avalonia Resizable Regions

## Table of Contents
1. Scope and APIs
2. Layout and Scrolling Mapping
3. Conversion Example
4. C# Equivalent
5. Troubleshooting

## Scope and APIs

Primary WinForms APIs:

- `Splitter`
- `ScrollableControl` / `Panel.AutoScroll`
- `HScrollBar`, `VScrollBar`

Primary Avalonia APIs:

- `Grid` + `GridSplitter`
- `ScrollViewer` (`HorizontalScrollBarVisibility`, `VerticalScrollBarVisibility`)
- `ScrollBar`

## Layout and Scrolling Mapping

| WinForms | Avalonia |
|---|---|
| `Splitter` with docked panels | `GridSplitter` between `Grid` columns/rows |
| `Panel.AutoScroll = true` | `ScrollViewer` around overflowing content |
| explicit `HScrollBar`/`VScrollBar` controls | `ScrollViewer` scrollbars, or explicit `ScrollBar` only for custom scenarios |
| `AutoScrollPosition` management | `Control.BringIntoView()` and view-model driven focus/selection |

## Conversion Example

WinForms C#:

```csharp
var navigation = new Panel
{
    Dock = DockStyle.Left,
    Width = 280,
    AutoScroll = true
};

var splitter = new Splitter
{
    Dock = DockStyle.Left,
    Width = 6
};

var editor = new Panel
{
    Dock = DockStyle.Fill,
    AutoScroll = true
};

navigation.Controls.Add(BuildNavigation());
editor.Controls.Add(BuildEditor());

Controls.Add(editor);
Controls.Add(splitter);
Controls.Add(navigation);
```

Avalonia XAML:

```xaml
<UserControl xmlns="https://github.com/avaloniaui"
             xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
             xmlns:vm="using:MyApp.ViewModels"
             x:DataType="vm:ShellViewModel">
  <Grid ColumnDefinitions="280,6,*">
    <ScrollViewer Grid.Column="0"
                  HorizontalScrollBarVisibility="Auto"
                  VerticalScrollBarVisibility="Auto">
      <ItemsControl ItemsSource="{CompiledBinding NavigationItems}" />
    </ScrollViewer>

    <GridSplitter Grid.Column="1"
                  ResizeDirection="Columns"
                  ShowsPreview="True"
                  Width="6"
                  Background="#33000000" />

    <ScrollViewer Grid.Column="2"
                  HorizontalScrollBarVisibility="Auto"
                  VerticalScrollBarVisibility="Auto">
      <StackPanel Spacing="8">
        <TextBlock FontWeight="Bold"
                   Text="{CompiledBinding SelectedTitle}" />
        <ItemsControl ItemsSource="{CompiledBinding EditorSections}" />
      </StackPanel>
    </ScrollViewer>
  </Grid>
</UserControl>
```

## C# Equivalent

```csharp
using Avalonia;
using Avalonia.Controls;

var root = new Grid
{
    ColumnDefinitions = ColumnDefinitions.Parse("280,6,*")
};

var navigation = new ScrollViewer
{
    HorizontalScrollBarVisibility = ScrollBarVisibility.Auto,
    VerticalScrollBarVisibility = ScrollBarVisibility.Auto,
    Content = new ItemsControl
    {
        ItemsSource = viewModel.NavigationItems
    }
};

var splitter = new GridSplitter
{
    ResizeDirection = GridResizeDirection.Columns,
    ShowsPreview = true,
    Width = 6
};

var editor = new ScrollViewer
{
    HorizontalScrollBarVisibility = ScrollBarVisibility.Auto,
    VerticalScrollBarVisibility = ScrollBarVisibility.Auto,
    Content = new ItemsControl
    {
        ItemsSource = viewModel.EditorSections
    }
};

Grid.SetColumn(navigation, 0);
Grid.SetColumn(splitter, 1);
Grid.SetColumn(editor, 2);

root.Children.Add(navigation);
root.Children.Add(splitter);
root.Children.Add(editor);
```

## Troubleshooting

1. Splitter drag does not resize expected columns/rows.
- ensure `GridSplitter` sits in its own thin column/row and `ResizeDirection` matches orientation.

2. Scrolling feels inconsistent after migration.
- wrap only the region that should scroll and avoid nested `ScrollViewer` controls for the same axis.

3. Programmatic focus/selection is off-screen.
- call `BringIntoView()` on target controls after selection changes.
