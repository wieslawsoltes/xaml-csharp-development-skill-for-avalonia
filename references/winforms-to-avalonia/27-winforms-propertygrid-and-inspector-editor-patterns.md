# WinForms PropertyGrid and Inspector Editor Patterns to Avalonia

## Table of Contents
1. Scope and APIs
2. Inspector Mapping
3. Conversion Example
4. C# Equivalent
5. Troubleshooting

## Scope and APIs

Primary WinForms APIs:

- `PropertyGrid`
- `SelectedObject` / `SelectedObjects`
- type-descriptor driven property editing

Primary Avalonia patterns:

- `ItemsControl`/`TreeView`/optional `DataGrid`-style inspectors
- explicit `PropertyEntryViewModel` rows
- editor controls composed by templates

## Inspector Mapping

| WinForms | Avalonia |
|---|---|
| automatic `PropertyGrid` reflection view | explicit inspector row view-models |
| property tabs/categories | grouped collections + templates |
| built-in editor hosts | explicit editor `Control` content or template selection |

Avalonia core does not include a direct `PropertyGrid` control.

## Conversion Example

WinForms C#:

```csharp
propertyGrid1.SelectedObject = selectedCustomer;
```

Avalonia XAML:

```xaml
<UserControl xmlns="https://github.com/avaloniaui"
             xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
             xmlns:vm="using:MyApp.ViewModels"
             x:DataType="vm:InspectorViewModel">
  <ItemsControl ItemsSource="{CompiledBinding Properties}">
    <ItemsControl.ItemTemplate>
      <DataTemplate x:DataType="vm:PropertyEntryViewModel">
        <Grid ColumnDefinitions="180,*" ColumnSpacing="8" Margin="0,2">
          <TextBlock Grid.Column="0"
                     VerticalAlignment="Center"
                     Text="{CompiledBinding DisplayName}" />
          <ContentControl Grid.Column="1"
                          Content="{CompiledBinding Editor}" />
        </Grid>
      </DataTemplate>
    </ItemsControl.ItemTemplate>
  </ItemsControl>
</UserControl>
```

## C# Equivalent

```csharp
using System.Collections.ObjectModel;
using Avalonia.Controls;

public sealed class PropertyEntryViewModel
{
    public string DisplayName { get; init; } = string.Empty;
    public Control Editor { get; init; } = new TextBlock();
}

public sealed class InspectorViewModel
{
    public ObservableCollection<PropertyEntryViewModel> Properties { get; } = new();
}
```

## Troubleshooting

1. Inspector generation is too dynamic and brittle.
- use explicit row descriptors for high-value editing workflows.

2. Editing controls lose focus/state while refreshing.
- keep stable row identity and update values in-place.

3. Category/grouping UX is missing.
- add grouped view-model sections and render with nested templates.
