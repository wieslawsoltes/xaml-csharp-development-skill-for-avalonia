# HTML Rich Content Patterns (Lists, Cards, Tables, Dashboards) to Avalonia

## Table of Contents
1. Scope and APIs
2. Pattern Mapping Matrix
3. Recipe: Card Grid Dashboard
4. Recipe: Virtualized Feed/List
5. Recipe: Tree/Hierarchy Explorer
6. Recipe: Table-Like Data View
7. Recipe: Shared-Column Table Rows
8. Recipe: `DataGrid` Escalation Path
9. Recipe: Inline Editing Surface
10. C# Equivalent: Table and DataGrid
11. Performance and AOT Notes
12. Troubleshooting

## Scope and APIs

Primary APIs:

- `ItemsControl`, `ListBox`, `TreeView`, `Carousel`, `TabControl`
- virtualization: `VirtualizingPanel`, `VirtualizingStackPanel`
- presentation: `ContentPresenter`, `ItemsPresenter`, `DataTemplate`, `FuncDataTemplate`
- scroll and anchoring: `ScrollViewer`

Reference docs:

- [`20-itemscontrol-virtualization-and-recycling.md`](../20-itemscontrol-virtualization-and-recycling)
- [`38-data-templates-and-idatatemplate-selector-patterns.md`](../38-data-templates-and-idatatemplate-selector-patterns)
- [`57-scrollviewer-offset-anchoring-and-snap-points.md`](../57-scrollviewer-offset-anchoring-and-snap-points)
- [`52-controls-reference-catalog.md`](../52-controls-reference-catalog)

## Pattern Mapping Matrix

| Modern web UI pattern | Avalonia pattern |
|---|---|
| card masonry/grid dashboard | `ItemsControl` + custom items panel (`UniformGrid`, `WrapPanel`, custom panel) |
| feed/timeline | `ListBox`/`ItemsControl` + `ScrollViewer` + virtualization |
| tree explorer | `TreeView` + `TreeDataTemplate` |
| tabbed workspace | `TabControl` |
| carousel/hero rotator | `Carousel` / `TransitioningContentControl` |

## Recipe: Card Grid Dashboard

HTML/CSS intent: responsive cards with reusable component styles.

Avalonia recipe:

```xaml
<ItemsControl ItemsSource="{CompiledBinding Cards}">
  <ItemsControl.ItemsPanel>
    <ItemsPanelTemplate>
      <WrapPanel ItemWidth="320" ItemHeight="180" />
    </ItemsPanelTemplate>
  </ItemsControl.ItemsPanel>

  <ItemsControl.ItemTemplate>
    <DataTemplate x:DataType="vm:CardViewModel">
      <Border Classes="dashboard-card" Padding="14" Margin="6">
        <StackPanel Spacing="6">
          <TextBlock Text="{CompiledBinding Title}" Classes="card-title" />
          <TextBlock Text="{CompiledBinding Value}" Classes="card-value" />
        </StackPanel>
      </Border>
    </DataTemplate>
  </ItemsControl.ItemTemplate>
</ItemsControl>
```

## Recipe: Virtualized Feed/List

Use `ListBox` with virtualization-friendly item templates and avoid heavy nested visual trees.

```xaml
<ListBox ItemsSource="{CompiledBinding Events}"
         ScrollViewer.VerticalScrollBarVisibility="Auto">
  <ListBox.ItemTemplate>
    <DataTemplate x:DataType="vm:EventItemViewModel">
      <Grid ColumnDefinitions="Auto,*" Margin="8">
        <Border Width="10" Height="10" CornerRadius="5" Background="{CompiledBinding DotBrush}" />
        <StackPanel Grid.Column="1" Margin="10,0,0,0">
          <TextBlock Text="{CompiledBinding Title}" />
          <TextBlock Text="{CompiledBinding TimestampText}" Classes="muted" />
        </StackPanel>
      </Grid>
    </DataTemplate>
  </ListBox.ItemTemplate>
</ListBox>
```

## Recipe: Tree/Hierarchy Explorer

```xaml
<TreeView ItemsSource="{CompiledBinding Nodes}">
  <TreeView.ItemTemplate>
    <TreeDataTemplate x:DataType="vm:NodeViewModel" ItemsSource="{CompiledBinding Children}">
      <TextBlock Text="{CompiledBinding Name}" />
    </TreeDataTemplate>
  </TreeView.ItemTemplate>
</TreeView>
```

## Recipe: Table-Like Data View

HTML/CSS:

```html
<table class="orders">
  <thead>
    <tr><th>ID</th><th>Status</th><th>Total</th></tr>
  </thead>
  <tbody>
    <tr><td>#1042</td><td>Paid</td><td>$128.00</td></tr>
  </tbody>
</table>
```

```css
.orders { width: 100%; border-collapse: collapse; }
.orders th, .orders td { padding: 10px 12px; border-bottom: 1px solid #2a3348; }
.orders th { text-align: left; font-weight: 600; }
```

Avalonia (table-like layout with `ItemsControl`):

```xaml
<StackPanel>
  <Grid ColumnDefinitions="120,160,*" Classes="orders-header">
    <TextBlock Grid.Column="0" Text="ID" />
    <TextBlock Grid.Column="1" Text="Status" />
    <TextBlock Grid.Column="2" Text="Total" />
  </Grid>

  <ItemsControl ItemsSource="{CompiledBinding Orders}">
    <ItemsControl.ItemTemplate>
      <DataTemplate x:DataType="vm:OrderRowViewModel">
        <Grid ColumnDefinitions="120,160,*" Classes="orders-row">
          <TextBlock Grid.Column="0" Text="{CompiledBinding Id}" />
          <TextBlock Grid.Column="1" Text="{CompiledBinding Status}" />
          <TextBlock Grid.Column="2" Text="{CompiledBinding TotalText}" />
        </Grid>
      </DataTemplate>
    </ItemsControl.ItemTemplate>
  </ItemsControl>
</StackPanel>
```

## Recipe: Shared-Column Table Rows

When column widths should stay aligned between header and every row (similar to HTML table column sizing), use `Grid.IsSharedSizeScope` + `SharedSizeGroup`.

```xaml
<Grid Grid.IsSharedSizeScope="True" RowDefinitions="Auto,*">
  <Grid Grid.Row="0" Classes="orders-header">
    <Grid.ColumnDefinitions>
      <ColumnDefinition SharedSizeGroup="ColId" />
      <ColumnDefinition SharedSizeGroup="ColStatus" />
      <ColumnDefinition SharedSizeGroup="ColTotal" />
    </Grid.ColumnDefinitions>

    <TextBlock Grid.Column="0" Text="ID" />
    <TextBlock Grid.Column="1" Text="Status" />
    <TextBlock Grid.Column="2" Text="Total" />
  </Grid>

  <ItemsControl Grid.Row="1" ItemsSource="{CompiledBinding Orders}">
    <ItemsControl.ItemTemplate>
      <DataTemplate x:DataType="vm:OrderRowViewModel">
        <Grid Classes="orders-row">
          <Grid.ColumnDefinitions>
            <ColumnDefinition SharedSizeGroup="ColId" />
            <ColumnDefinition SharedSizeGroup="ColStatus" />
            <ColumnDefinition SharedSizeGroup="ColTotal" />
          </Grid.ColumnDefinitions>

          <TextBlock Grid.Column="0" Text="{CompiledBinding Id}" />
          <TextBlock Grid.Column="1" Text="{CompiledBinding Status}" />
          <TextBlock Grid.Column="2" Text="{CompiledBinding TotalText}" />
        </Grid>
      </DataTemplate>
    </ItemsControl.ItemTemplate>
  </ItemsControl>
</Grid>
```

## Recipe: `DataGrid` Escalation Path

If the web table requires built-in sorting, column resize/reorder, selection, and editing semantics, move from handcrafted `Grid` rows to `DataGrid` (package-based).

Use `Grid + ItemsControl` when:

- table is mostly read-only and custom-styled,
- row visuals are highly bespoke cards/rows.

Use `DataGrid` when:

- users need spreadsheet-like interaction,
- headers/columns are interactive and standardized.

```xaml
<!-- Requires Avalonia.Controls.DataGrid package -->
<DataGrid ItemsSource="{CompiledBinding Orders}"
          AutoGenerateColumns="False"
          CanUserSortColumns="True"
          CanUserResizeColumns="True"
          GridLinesVisibility="Horizontal">
  <DataGrid.Columns>
    <DataGridTextColumn Header="ID" Binding="{Binding Id}" Width="SizeToHeader" />
    <DataGridTextColumn Header="Status" Binding="{Binding Status}" Width="*" />
    <DataGridTextColumn Header="Total" Binding="{Binding TotalText}" Width="*" />
  </DataGrid.Columns>
</DataGrid>
```

## Recipe: Inline Editing Surface

Web inline-edit idiom maps to templated list item states:

- read mode: text + action buttons,
- edit mode: `TextBox` + commit/cancel commands,
- style states via item classes.

## C# Equivalent: Table and DataGrid

```csharp
using Avalonia.Controls;
using Avalonia.Controls.Templates;

var table = new StackPanel();

var header = new Grid
{
    ColumnDefinitions = ColumnDefinitions.Parse("120,160,*"),
};
var idHeader = new TextBlock { Text = "ID" };
var statusHeader = new TextBlock { Text = "Status" };
var totalHeader = new TextBlock { Text = "Total" };
Grid.SetColumn(statusHeader, 1);
Grid.SetColumn(totalHeader, 2);
header.Children.Add(idHeader);
header.Children.Add(statusHeader);
header.Children.Add(totalHeader);
table.Children.Add(header);

var rows = new ItemsControl
{
    ItemTemplate = new FuncDataTemplate<OrderRowViewModel>((item, _) =>
    {
        var row = new Grid { ColumnDefinitions = ColumnDefinitions.Parse("120,160,*") };
        row.Children.Add(new TextBlock { Text = item.Id });
        row.Children.Add(new TextBlock { Text = item.Status });
        row.Children.Add(new TextBlock { Text = item.TotalText });
        Grid.SetColumn(row.Children[1], 1);
        Grid.SetColumn(row.Children[2], 2);
        return row;
    })
};
table.Children.Add(rows);

// Optional package-based grid when spreadsheet-like interaction is required.
var dataGrid = new DataGrid
{
    AutoGenerateColumns = false,
    CanUserSortColumns = true,
    CanUserResizeColumns = true,
    GridLinesVisibility = DataGridGridLinesVisibility.Horizontal
};
dataGrid.Columns.Add(new DataGridTextColumn { Header = "ID", Binding = new Avalonia.Data.Binding("Id") });
dataGrid.Columns.Add(new DataGridTextColumn { Header = "Status", Binding = new Avalonia.Data.Binding("Status") });
dataGrid.Columns.Add(new DataGridTextColumn { Header = "Total", Binding = new Avalonia.Data.Binding("TotalText") });
```

## Performance and AOT Notes

- Keep item templates typed (`x:DataType`) and simple.
- Use virtualization for large collections.
- Avoid reflection-heavy runtime template generation in hot paths.

## Troubleshooting

1. Scrolling stutters on long lists.
- Reduce visual tree depth and verify virtualization path.

2. Item state updates redraw too much.
- Split template regions and avoid global style invalidations.

3. Template mismatch at runtime.
- Ensure `DataType` alignment with actual item model types.

4. Header and row columns drift out of alignment.
- Use `Grid.IsSharedSizeScope` and shared column groups.
