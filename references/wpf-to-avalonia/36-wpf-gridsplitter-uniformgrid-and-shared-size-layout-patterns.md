# WPF GridSplitter, UniformGrid, and Shared-Size Layout Patterns to Avalonia

## Table of Contents
1. Scope and APIs
2. Layout Mapping
3. Conversion Example
4. Avalonia C# Equivalent
5. Troubleshooting

## Scope and APIs

Primary WPF APIs:

- `GridSplitter`
- `UniformGrid`
- `Grid.IsSharedSizeScope` + `SharedSizeGroup`

Primary Avalonia APIs:

- `GridSplitter` (`ResizeDirection`, `ResizeBehavior`, `ShowsPreview`)
- `Avalonia.Controls.Primitives.UniformGrid`
- `Grid.IsSharedSizeScope` + `SharedSizeGroup`

## Layout Mapping

| WPF | Avalonia |
|---|---|
| `GridSplitter` drag resize between columns/rows | `GridSplitter` (same concept; explicit resize options available) |
| `UniformGrid` equal cell matrix | `Avalonia.Controls.Primitives.UniformGrid` |
| `Grid.IsSharedSizeScope="True"` | `Grid.IsSharedSizeScope="True"` |
| `ColumnDefinition SharedSizeGroup="Label"` | `ColumnDefinition SharedSizeGroup="Label"` |

## Conversion Example

WPF XAML:

```xaml
<Grid Grid.IsSharedSizeScope="True">
  <Grid.RowDefinitions>
    <RowDefinition Height="Auto" />
    <RowDefinition Height="*" />
  </Grid.RowDefinitions>

  <Grid Grid.Row="0">
    <Grid.ColumnDefinitions>
      <ColumnDefinition Width="Auto" SharedSizeGroup="Label" />
      <ColumnDefinition Width="*" />
    </Grid.ColumnDefinitions>
    <TextBlock Grid.Column="0" Text="Name" Margin="0,0,8,0" />
    <TextBox Grid.Column="1" />
  </Grid>

  <Grid Grid.Row="1">
    <Grid.ColumnDefinitions>
      <ColumnDefinition Width="2*" />
      <ColumnDefinition Width="Auto" />
      <ColumnDefinition Width="3*" />
    </Grid.ColumnDefinitions>
    <ListBox Grid.Column="0" />
    <GridSplitter Grid.Column="1" Width="6" HorizontalAlignment="Stretch" />
    <Border Grid.Column="2" />
  </Grid>
</Grid>
```

Avalonia XAML:

```xaml
<UserControl xmlns="https://github.com/avaloniaui"
             xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
             xmlns:vm="using:MyApp.ViewModels"
             xmlns:primitives="clr-namespace:Avalonia.Controls.Primitives;assembly=Avalonia.Controls"
             x:DataType="vm:WorkspaceLayoutViewModel">
  <Grid Grid.IsSharedSizeScope="True" RowDefinitions="Auto,Auto,*" RowSpacing="8">
    <Grid Grid.Row="0" ColumnSpacing="8">
      <Grid.ColumnDefinitions>
        <ColumnDefinition Width="Auto" SharedSizeGroup="Label" />
        <ColumnDefinition Width="*" />
      </Grid.ColumnDefinitions>
      <TextBlock Grid.Column="0" Text="Name" />
      <TextBox Grid.Column="1" Text="{CompiledBinding Name, Mode=TwoWay}" />
    </Grid>

    <Grid Grid.Row="1" ColumnSpacing="8">
      <Grid.ColumnDefinitions>
        <ColumnDefinition Width="Auto" SharedSizeGroup="Label" />
        <ColumnDefinition Width="*" />
      </Grid.ColumnDefinitions>
      <TextBlock Grid.Column="0" Text="Role" />
      <ComboBox Grid.Column="1"
                ItemsSource="{CompiledBinding Roles}"
                SelectedItem="{CompiledBinding SelectedRole, Mode=TwoWay}" />
    </Grid>

    <Grid Grid.Row="2" ColumnDefinitions="2*,Auto,3*" ColumnSpacing="0">
      <Border Grid.Column="0" Padding="8">
        <primitives:UniformGrid Columns="3" RowSpacing="8" ColumnSpacing="8">
          <Button Content="A" />
          <Button Content="B" />
          <Button Content="C" />
          <Button Content="D" />
          <Button Content="E" />
          <Button Content="F" />
        </primitives:UniformGrid>
      </Border>

      <GridSplitter Grid.Column="1"
                    Width="6"
                    HorizontalAlignment="Stretch"
                    ResizeDirection="Columns"
                    ResizeBehavior="PreviousAndNext"
                    ShowsPreview="True" />

      <Border Grid.Column="2" Padding="8">
        <TextBlock Text="{CompiledBinding PreviewText}" TextWrapping="Wrap" />
      </Border>
    </Grid>
  </Grid>
</UserControl>
```

## Avalonia C# Equivalent

```csharp
using Avalonia;
using Avalonia.Controls;
using Avalonia.Controls.Primitives;

var root = new Grid
{
    RowDefinitions = new RowDefinitions("Auto,Auto,*"),
    RowSpacing = 8
};
Grid.SetIsSharedSizeScope(root, true);

var nameRow = new Grid
{
    ColumnDefinitions =
    {
        new ColumnDefinition(GridLength.Auto) { SharedSizeGroup = "Label" },
        new ColumnDefinition(GridLength.Star)
    },
    ColumnSpacing = 8
};
var nameLabel = new TextBlock { Text = "Name" };
var nameBox = new TextBox { Text = viewModel.Name };
Grid.SetColumn(nameBox, 1);
nameRow.Children.Add(nameLabel);
nameRow.Children.Add(nameBox);

var roleRow = new Grid
{
    ColumnDefinitions =
    {
        new ColumnDefinition(GridLength.Auto) { SharedSizeGroup = "Label" },
        new ColumnDefinition(GridLength.Star)
    },
    ColumnSpacing = 8
};
var roleLabel = new TextBlock { Text = "Role" };
var roleBox = new ComboBox
{
    ItemsSource = viewModel.Roles,
    SelectedItem = viewModel.SelectedRole
};
Grid.SetColumn(roleBox, 1);
roleRow.Children.Add(roleLabel);
roleRow.Children.Add(roleBox);

var body = new Grid
{
    ColumnDefinitions = new ColumnDefinitions("2*,Auto,3*")
};

var matrix = new UniformGrid
{
    Columns = 3,
    RowSpacing = 8,
    ColumnSpacing = 8
};
matrix.Children.Add(new Button { Content = "A" });
matrix.Children.Add(new Button { Content = "B" });
matrix.Children.Add(new Button { Content = "C" });
matrix.Children.Add(new Button { Content = "D" });
matrix.Children.Add(new Button { Content = "E" });
matrix.Children.Add(new Button { Content = "F" });

var left = new Border { Padding = new Thickness(8), Child = matrix };
var preview = new Border
{
    Padding = new Thickness(8),
    Child = new TextBlock
    {
        Text = viewModel.PreviewText,
        TextWrapping = Avalonia.Media.TextWrapping.Wrap
    }
};

Grid.SetColumn(left, 0);
Grid.SetColumn(preview, 2);
body.Children.Add(left);
body.Children.Add(preview);

var splitter = new GridSplitter
{
    Width = 6,
    HorizontalAlignment = Avalonia.Layout.HorizontalAlignment.Stretch,
    ResizeDirection = GridResizeDirection.Columns,
    ResizeBehavior = GridResizeBehavior.PreviousAndNext,
    ShowsPreview = true
};
Grid.SetColumn(splitter, 1);
body.Children.Add(splitter);

Grid.SetRow(nameRow, 0);
Grid.SetRow(roleRow, 1);
Grid.SetRow(body, 2);
root.Children.Add(nameRow);
root.Children.Add(roleRow);
root.Children.Add(body);
```

## Troubleshooting

1. Shared label columns are not aligned.
- Ensure both participating grids are under the same `Grid.IsSharedSizeScope="True"` ancestor.

2. Splitter does not resize expected columns.
- Set `ResizeDirection` and `ResizeBehavior` explicitly in migrated layouts.

3. Uniform grid wraps unexpectedly.
- Verify `Rows`/`Columns` and `FirstColumn` values after porting from WPF defaults.
