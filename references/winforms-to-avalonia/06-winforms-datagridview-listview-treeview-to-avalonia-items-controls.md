# WinForms DataGridView, ListView, TreeView to Avalonia Items Controls

## Table of Contents
1. Scope and APIs
2. Control Mapping Matrix
3. Grid/List/Tree Conversion Example
4. C# Equivalent
5. Troubleshooting

## Scope and APIs

Primary WinForms APIs:

- `DataGridView`
- `ListView`
- `TreeView`

Primary Avalonia APIs:

- `ListBox`, `ItemsControl`, `TreeView`, `TabControl`
- `DataTemplate`, `TreeDataTemplate`
- optional `DataGrid` from `Avalonia.Controls.DataGrid` package for grid-native features

## Control Mapping Matrix

| WinForms | Avalonia |
|---|---|
| `DataGridView` | `DataGrid` package (sorting/resizing/editing) or `Grid` + virtualized list templates |
| `ListView` details mode | `ListBox` with `Grid` row template or `DataGrid` package |
| `TreeView` | `TreeView` + `TreeDataTemplate` |

## Grid/List/Tree Conversion Example

WinForms C#:

```csharp
usersGrid.DataSource = users;
usersGrid.AutoGenerateColumns = false;
usersGrid.Columns.Add(new DataGridViewTextBoxColumn { HeaderText = "Name", DataPropertyName = "Name" });

filesList.View = View.Details;
filesList.Columns.Add("File", 240);
filesTree.Nodes.Add("Root");
```

Avalonia XAML:

```xaml
<Grid xmlns="https://github.com/avaloniaui"
      xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
      xmlns:vm="using:MyApp.ViewModels"
      x:DataType="vm:ExplorerViewModel"
      RowDefinitions="Auto,*,*"
      RowSpacing="8">
  <!-- Optional: replace with DataGrid from Avalonia.Controls.DataGrid when full grid behavior is required. -->
  <ListBox Grid.Row="0" ItemsSource="{CompiledBinding Users}">
    <ListBox.ItemTemplate>
      <DataTemplate x:DataType="vm:UserRowViewModel">
        <Grid ColumnDefinitions="2*,*" ColumnSpacing="12">
          <TextBlock Grid.Column="0" Text="{CompiledBinding Name}" />
          <TextBlock Grid.Column="1" Text="{CompiledBinding Role}" />
        </Grid>
      </DataTemplate>
    </ListBox.ItemTemplate>
  </ListBox>

  <ListBox Grid.Row="1" ItemsSource="{CompiledBinding Files}" />

  <TreeView Grid.Row="2" ItemsSource="{CompiledBinding TreeItems}">
    <TreeView.ItemTemplate>
      <TreeDataTemplate x:DataType="vm:TreeItemViewModel"
                        ItemsSource="{CompiledBinding Children}">
        <TextBlock Text="{CompiledBinding Name}" />
      </TreeDataTemplate>
    </TreeView.ItemTemplate>
  </TreeView>
</Grid>
```

Avalonia C#:

```csharp
using Avalonia.Controls;

var usersList = new ListBox { ItemsSource = viewModel.Users };
var filesList = new ListBox { ItemsSource = viewModel.Files };
var tree = new TreeView { ItemsSource = viewModel.TreeItems };

var root = new Grid
{
    RowDefinitions = RowDefinitions.Parse("Auto,*,*"),
    RowSpacing = 8
};

Grid.SetRow(usersList, 0);
Grid.SetRow(filesList, 1);
Grid.SetRow(tree, 2);

root.Children.Add(usersList);
root.Children.Add(filesList);
root.Children.Add(tree);
```

## Troubleshooting

1. Data grid feature parity is insufficient.
- use `Avalonia.Controls.DataGrid` package for built-in column/selection/editing behaviors.

2. Large list performance regresses.
- simplify item templates and validate virtualization strategy.

3. Tree expansion state resets.
- keep stable node identity and expansion state in the view model.
