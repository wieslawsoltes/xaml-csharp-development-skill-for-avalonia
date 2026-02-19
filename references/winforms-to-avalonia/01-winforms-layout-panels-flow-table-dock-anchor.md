# WinForms Layout Panels, Flow/Table, Dock/Anchor to Avalonia

## Table of Contents
1. Scope and APIs
2. Panel and Container Mapping
3. Anchor/Dock Conversion Rules
4. Flow and Table Recipes
5. End-to-End Example
6. Troubleshooting

## Scope and APIs

Primary WinForms APIs:

- `Panel`, `FlowLayoutPanel`, `TableLayoutPanel`
- `Control.Dock`, `Control.Anchor`

Primary Avalonia APIs:

- `Grid`, `StackPanel`, `WrapPanel`, `DockPanel`, `RelativePanel`
- `Grid.RowDefinitions`, `Grid.ColumnDefinitions`
- `Grid.IsSharedSizeScope`, `SharedSizeGroup`

## Panel and Container Mapping

| WinForms | Avalonia |
|---|---|
| `Panel` | `Border` + `Grid` or `StackPanel` |
| `FlowLayoutPanel` | `WrapPanel` (wrapping) or `StackPanel` (single axis) |
| `TableLayoutPanel` | `Grid` with explicit rows/columns |
| `AutoScroll` container | `ScrollViewer` |

## Anchor/Dock Conversion Rules

| WinForms idiom | Avalonia idiom |
|---|---|
| `DockStyle.Top` | `DockPanel.Dock="Top"` |
| `DockStyle.Fill` | star-sized `Grid` cell or last child of `DockPanel` |
| `AnchorStyles.Right` | `HorizontalAlignment="Right"` |
| `AnchorStyles.Bottom | Right` | place in bottom row + `HorizontalAlignment="Right"` |

## Flow and Table Recipes

WinForms C# (`TableLayoutPanel` + `FlowLayoutPanel`):

```csharp
var table = new TableLayoutPanel
{
    Dock = DockStyle.Fill,
    ColumnCount = 2,
    RowCount = 2
};

table.ColumnStyles.Add(new ColumnStyle(SizeType.Absolute, 180));
table.ColumnStyles.Add(new ColumnStyle(SizeType.Percent, 100));

var flow = new FlowLayoutPanel { Dock = DockStyle.Fill, FlowDirection = FlowDirection.LeftToRight };
flow.Controls.Add(new Button { Text = "Save" });
flow.Controls.Add(new Button { Text = "Cancel" });

table.Controls.Add(new Label { Text = "Name" }, 0, 0);
table.Controls.Add(new TextBox(), 1, 0);
table.Controls.Add(flow, 1, 1);
```

Avalonia XAML:

```xaml
<Grid xmlns="https://github.com/avaloniaui"
      xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
      xmlns:vm="using:MyApp.ViewModels"
      x:DataType="vm:FormLayoutViewModel"
      RowDefinitions="Auto,Auto"
      ColumnDefinitions="180,*"
      RowSpacing="8"
      ColumnSpacing="12">
  <TextBlock Grid.Row="0" Grid.Column="0" VerticalAlignment="Center" Text="Name" />
  <TextBox Grid.Row="0" Grid.Column="1" />

  <WrapPanel Grid.Row="1" Grid.Column="1" Spacing="8" Orientation="Horizontal">
    <Button Content="Save" Command="{CompiledBinding SaveCommand}" />
    <Button Content="Cancel" Command="{CompiledBinding CancelCommand}" />
  </WrapPanel>
</Grid>
```

Avalonia C#:

```csharp
using Avalonia.Controls;

var grid = new Grid
{
    RowDefinitions = RowDefinitions.Parse("Auto,Auto"),
    ColumnDefinitions = ColumnDefinitions.Parse("180,*"),
    RowSpacing = 8,
    ColumnSpacing = 12
};

grid.Children.Add(new TextBlock { Text = "Name", VerticalAlignment = Avalonia.Layout.VerticalAlignment.Center });

var nameBox = new TextBox();
Grid.SetColumn(nameBox, 1);
grid.Children.Add(nameBox);

var actions = new WrapPanel { Spacing = 8, Orientation = Avalonia.Layout.Orientation.Horizontal };
actions.Children.Add(new Button { Content = "Save", Command = viewModel.SaveCommand });
actions.Children.Add(new Button { Content = "Cancel", Command = viewModel.CancelCommand });
Grid.SetRow(actions, 1);
Grid.SetColumn(actions, 1);
grid.Children.Add(actions);
```

## End-to-End Example

For table-like forms with aligned header/body columns, use shared-size groups:

```xaml
<Grid Grid.IsSharedSizeScope="True">
  <Grid.ColumnDefinitions>
    <ColumnDefinition SharedSizeGroup="LabelCol" />
    <ColumnDefinition SharedSizeGroup="ValueCol" />
  </Grid.ColumnDefinitions>
</Grid>
```

This pattern is the closest replacement for complex designer-driven `TableLayoutPanel` setups.

## Troubleshooting

1. Anchored controls drift on resize.
- replace offset math with row/column-based placement.

2. Converted flow layout does not wrap.
- use `WrapPanel` instead of `StackPanel`.

3. Table columns do not line up across sections.
- enable `Grid.IsSharedSizeScope` and matching `SharedSizeGroup` names.
