# HTML/CSS Data Table, List, and Master-Detail Patterns in Avalonia

## Table of Contents
1. Scope and APIs
2. Data Presentation Pattern Matrix
3. Table-Like Layout Conversion
4. Shared-Size Column Layout (Advanced Grid Pattern)
5. Optional `DataGrid` Pattern
6. Responsive List-to-Detail Conversion
7. Master-Detail Split Pattern
8. Sorting/Filtering UX Mapping
9. C# Equivalent: Master-Detail Split
10. Troubleshooting

## Scope and APIs

Primary APIs:

- `ItemsControl`, `ListBox`, `TreeView`, `ScrollViewer`
- layout for rows/columns (`Grid`, `ColumnDefinitions`)
- shared column sizing (`Grid.IsSharedSizeScope`, `SharedSizeGroup`)
- split compositions (`GridSplitter`, `SplitView`)
- data template patterns (`DataTemplate`, `TreeDataTemplate`)

Reference docs:

- [`06-html-rich-content-lists-cards-tables-and-virtualization.md`](06-html-rich-content-lists-cards-tables-and-virtualization)
- [`20-itemscontrol-virtualization-and-recycling.md`](../20-itemscontrol-virtualization-and-recycling)

## Data Presentation Pattern Matrix

| Web pattern | Avalonia pattern |
|---|---|
| `<table>` with sticky headers | `Grid` header row + virtualized item list |
| responsive table collapsing to cards | class-driven template switch |
| master-detail side panel | `Grid` + `GridSplitter` or `SplitView` |
| nested folder/file browser | `TreeView` |

## Table-Like Layout Conversion

HTML/CSS:

```html
<table class="users">
  <thead><tr><th>Name</th><th>Role</th><th>Status</th></tr></thead>
  <tbody>...</tbody>
</table>
```

```css
.users th, .users td { padding: 10px 12px; border-bottom: 1px solid #2a3348; }
```

Avalonia:

```xaml
<StackPanel>
  <Grid ColumnDefinitions="2*,*,*" Classes="users-header">
    <TextBlock Grid.Column="0" Text="Name" />
    <TextBlock Grid.Column="1" Text="Role" />
    <TextBlock Grid.Column="2" Text="Status" />
  </Grid>

  <ListBox ItemsSource="{CompiledBinding Users}">
    <ListBox.ItemTemplate>
      <DataTemplate x:DataType="vm:UserRowViewModel">
        <Grid ColumnDefinitions="2*,*,*" Classes="users-row">
          <TextBlock Grid.Column="0" Text="{CompiledBinding Name}" />
          <TextBlock Grid.Column="1" Text="{CompiledBinding Role}" />
          <TextBlock Grid.Column="2" Text="{CompiledBinding Status}" />
        </Grid>
      </DataTemplate>
    </ListBox.ItemTemplate>
  </ListBox>
</StackPanel>
```

## Shared-Size Column Layout (Advanced Grid Pattern)

For HTML-table-like column alignment across header and body templates, use shared-size groups:

```xaml
<Grid Grid.IsSharedSizeScope="True" RowDefinitions="Auto,*">
  <Grid Grid.Row="0" Classes="users-header">
    <Grid.ColumnDefinitions>
      <ColumnDefinition SharedSizeGroup="NameCol" />
      <ColumnDefinition SharedSizeGroup="RoleCol" />
      <ColumnDefinition SharedSizeGroup="StatusCol" />
    </Grid.ColumnDefinitions>
    <TextBlock Grid.Column="0" Text="Name" />
    <TextBlock Grid.Column="1" Text="Role" />
    <TextBlock Grid.Column="2" Text="Status" />
  </Grid>

  <ListBox Grid.Row="1" ItemsSource="{CompiledBinding Users}">
    <ListBox.ItemTemplate>
      <DataTemplate x:DataType="vm:UserRowViewModel">
        <Grid Classes="users-row">
          <Grid.ColumnDefinitions>
            <ColumnDefinition SharedSizeGroup="NameCol" />
            <ColumnDefinition SharedSizeGroup="RoleCol" />
            <ColumnDefinition SharedSizeGroup="StatusCol" />
          </Grid.ColumnDefinitions>
          <TextBlock Grid.Column="0" Text="{CompiledBinding Name}" />
          <TextBlock Grid.Column="1" Text="{CompiledBinding Role}" />
          <TextBlock Grid.Column="2" Text="{CompiledBinding Status}" />
        </Grid>
      </DataTemplate>
    </ListBox.ItemTemplate>
  </ListBox>
</Grid>
```

This pattern is the closest equivalent to HTML table column synchronization while staying fully template-driven.

## Optional `DataGrid` Pattern

When the UX requirement is grid-native behavior (sorting, selection, resizable columns, in-place editing), prefer `DataGrid` over handcrafted rows.

```xaml
<!-- Requires Avalonia.Controls.DataGrid package -->
<DataGrid ItemsSource="{CompiledBinding Users}"
          AutoGenerateColumns="False"
          CanUserSortColumns="True"
          CanUserResizeColumns="True"
          CanUserReorderColumns="True"
          GridLinesVisibility="Horizontal"
          IsReadOnly="False">
  <DataGrid.Columns>
    <DataGridTextColumn Header="Name" Binding="{Binding Name}" Width="2*" />
    <DataGridTextColumn Header="Role" Binding="{Binding Role}" Width="*" />
    <DataGridTextColumn Header="Status" Binding="{Binding Status}" Width="*" />
  </DataGrid.Columns>
</DataGrid>
```

## Responsive List-to-Detail Conversion

HTML/CSS pattern: table on desktop, stacked cards on mobile.

Avalonia pattern:

- toggle root classes (`mobile`/`desktop`),
- provide two templates and switch through style/class-driven visibility.

## Master-Detail Split Pattern

```xaml
<Grid ColumnDefinitions="320,6,*">
  <ListBox Grid.Column="0" ItemsSource="{CompiledBinding Items}" SelectedItem="{CompiledBinding SelectedItem}" />
  <GridSplitter Grid.Column="1" Width="6" />
  <ContentControl Grid.Column="2" Content="{CompiledBinding SelectedItem}" />
</Grid>
```

## C# Equivalent: Master-Detail Split

```csharp
using Avalonia.Controls;

var layout = new Grid
{
    ColumnDefinitions = ColumnDefinitions.Parse("320,6,*")
};

var list = new ListBox();
Grid.SetColumn(list, 0);

var splitter = new GridSplitter { Width = 6 };
Grid.SetColumn(splitter, 1);

var detail = new ContentControl();
Grid.SetColumn(detail, 2);

layout.Children.Add(list);
layout.Children.Add(splitter);
layout.Children.Add(detail);
```

## Sorting/Filtering UX Mapping

HTML table pattern usually has clickable headers and filter chips.

Avalonia mapping:

- command-bound header buttons for sorting,
- filter chips as toggle buttons/classes,
- stable sort/filter state in view model.

## Troubleshooting

1. Table-like rows misalign with headers.
- Keep identical `ColumnDefinitions` between header and row templates, or use shared-size groups.

2. Large datasets consume too much memory.
- Verify virtualization and avoid large nested controls per row.

3. Master-detail detail pane doesn't refresh.
- Ensure selected item raises property-change notifications.

4. Table interaction complexity grows too much.
- Escalate to `DataGrid` instead of reimplementing sorting/editing/selection behavior.
