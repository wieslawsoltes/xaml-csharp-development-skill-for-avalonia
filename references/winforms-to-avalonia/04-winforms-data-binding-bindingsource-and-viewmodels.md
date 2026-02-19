# WinForms Data Binding, BindingSource, and ViewModels to Avalonia

## Table of Contents
1. Scope and APIs
2. Binding Model Mapping
3. BindingSource Conversion Strategy
4. Conversion Example
5. C# Equivalent
6. AOT Notes
7. Troubleshooting

## Scope and APIs

Primary WinForms APIs:

- `BindingSource`
- `Control.DataBindings`
- `DataGridView.DataSource`

Primary Avalonia APIs:

- compiled bindings (`{CompiledBinding ...}`)
- `DataContext`
- `INotifyPropertyChanged` and collection bindings
- item controls (`ListBox`, `ItemsControl`, optional `DataGrid` package)

## Binding Model Mapping

| WinForms | Avalonia |
|---|---|
| `BindingSource.DataSource` | `DataContext` + strongly typed view model |
| `Control.DataBindings.Add(...)` | XAML binding expressions |
| `BindingSource.Current` | `SelectedItem` / explicit current item property |
| `BindingSource.Filter/Sort` | view-model query/projection state |

## BindingSource Conversion Strategy

- replace `BindingSource` as implicit UI state holder with explicit view-model properties.
- expose `ObservableCollection<T>` and `SelectedItem` on the view model.
- keep filtering/sorting logic in the view-model or service layer.

## Conversion Example

WinForms C#:

```csharp
var source = new BindingSource();
source.DataSource = customers;

nameTextBox.DataBindings.Add("Text", source, "Name", true, DataSourceUpdateMode.OnPropertyChanged);
customersGrid.DataSource = source;
```

Avalonia XAML:

```xaml
<UserControl xmlns="https://github.com/avaloniaui"
             xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
             xmlns:vm="using:MyApp.ViewModels"
             x:DataType="vm:CustomersViewModel">
  <Grid RowDefinitions="Auto,*" RowSpacing="8">
    <TextBox Grid.Row="0" Text="{CompiledBinding SelectedCustomer.Name}" />

    <ListBox Grid.Row="1"
             ItemsSource="{CompiledBinding Customers}"
             SelectedItem="{CompiledBinding SelectedCustomer}">
      <ListBox.ItemTemplate>
        <DataTemplate x:DataType="vm:CustomerViewModel">
          <TextBlock Text="{CompiledBinding Name}" />
        </DataTemplate>
      </ListBox.ItemTemplate>
    </ListBox>
  </Grid>
</UserControl>
```

## C# Equivalent

```csharp
using Avalonia.Controls;

var list = new ListBox
{
    ItemsSource = viewModel.Customers,
    SelectedItem = viewModel.SelectedCustomer
};

var nameBox = new TextBox
{
    Text = viewModel.SelectedCustomer?.Name
};
```

## AOT Notes

- use `x:DataType` with compiled bindings to avoid reflection-heavy binding paths.
- keep model/view-model members public and strongly typed.

## Troubleshooting

1. UI no longer updates after edits.
- ensure view-model properties raise `PropertyChanged`.

2. Selected item and details panel desynchronize.
- bind both `SelectedItem` and detail controls to the same selected object.

3. Filtered data feels stateful and fragile.
- avoid hidden `BindingSource` state; use explicit filter/sort properties in the view model.
