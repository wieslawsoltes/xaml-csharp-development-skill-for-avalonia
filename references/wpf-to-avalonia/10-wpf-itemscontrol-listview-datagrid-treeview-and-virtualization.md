# WPF ItemsControl, ListView, DataGrid, TreeView, and Virtualization to Avalonia

## Table of Contents
1. Scope and APIs
2. Control Mapping Matrix
3. Conversion Example
4. Avalonia C# Equivalent
5. Troubleshooting

## Scope and APIs

Primary WPF APIs:

- `ItemsControl`, `ListView`, `DataGrid`, `TreeView`
- `VirtualizingStackPanel`

Primary Avalonia APIs:

- `ItemsControl`, `ListBox`, `TreeView`
- virtualization support in item controls and `VirtualizingStackPanel`
- optional `Avalonia.Controls.DataGrid` package for grid-specific UX

## Control Mapping Matrix

| WPF | Avalonia |
|---|---|
| `ItemsControl` | `ItemsControl` |
| `ListView` + `GridView` | `ListBox`/`ItemsControl` + templated row grid |
| `DataGrid` | optional `Avalonia.Controls.DataGrid` package |
| `TreeView` | `TreeView` + `TreeDataTemplate` |

## Conversion Example

WPF XAML:

```xaml
<ListView ItemsSource="{Binding Users}">
  <ListView.View>
    <GridView>
      <GridViewColumn Header="Name" DisplayMemberBinding="{Binding Name}" />
      <GridViewColumn Header="Role" DisplayMemberBinding="{Binding Role}" />
    </GridView>
  </ListView.View>
</ListView>
```

Avalonia XAML:

```xaml
<ListBox xmlns="https://github.com/avaloniaui"
         xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
         xmlns:vm="using:MyApp.ViewModels"
         x:DataType="vm:UsersPageViewModel"
         ItemsSource="{CompiledBinding Users}">
  <ListBox.ItemTemplate>
    <DataTemplate x:DataType="vm:UserRowViewModel">
      <Grid ColumnDefinitions="2*,*" ColumnSpacing="12">
        <TextBlock Grid.Column="0" Text="{CompiledBinding Name}" />
        <TextBlock Grid.Column="1" Text="{CompiledBinding Role}" />
      </Grid>
    </DataTemplate>
  </ListBox.ItemTemplate>
</ListBox>
```

Optional DataGrid pattern:

```xaml
<!-- Requires Avalonia.Controls.DataGrid package -->
<DataGrid xmlns="https://github.com/avaloniaui"
          xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
          xmlns:vm="using:MyApp.ViewModels"
          x:DataType="vm:UsersPageViewModel"
          ItemsSource="{CompiledBinding Users}"
          AutoGenerateColumns="False" />
```

## Avalonia C# Equivalent

```csharp
using Avalonia.Controls;

var users = new ListBox { ItemsSource = viewModel.Users };
var tree = new TreeView { ItemsSource = viewModel.Nodes };
```

## Troubleshooting

1. large data sets become slow after template port.
- simplify templates and verify virtualization behavior.

2. missing WPF `GridView` convenience columns.
- model row layout explicitly with `Grid` templates or use `DataGrid` package.

3. tree expansion state is unstable.
- keep node identity and expansion state in the view model.
