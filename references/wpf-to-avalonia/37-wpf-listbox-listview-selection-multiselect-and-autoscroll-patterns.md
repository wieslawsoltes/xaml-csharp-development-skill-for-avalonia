# WPF ListBox/ListView Selection, Multi-Select, and Auto-Scroll Patterns to Avalonia

## Table of Contents
1. Scope and APIs
2. Selection Mapping
3. Conversion Example
4. Avalonia C# Equivalent
5. Troubleshooting

## Scope and APIs

Primary WPF APIs:

- `ListBox`, `ListView`
- `SelectionMode` (`Single`, `Multiple`, `Extended`)
- `SelectedItem`, `SelectedItems`, `ScrollIntoView(...)`

Primary Avalonia APIs:

- `ListBox` and `SelectingItemsControl` selection model
- `SelectionMode` flags (`Single`, `Multiple`, `Toggle`, `AlwaysSelected`)
- `SelectedItem`, `SelectedItems`, `Selection` (`ISelectionModel`)
- `AutoScrollToSelectedItem`

## Selection Mapping

| WPF | Avalonia |
|---|---|
| `ListView` + `GridView` selection | `ListBox` + row template selection |
| `SelectionMode="Extended"` | `SelectionMode="Multiple"` (optional `Toggle`) |
| `SelectedItems` sync patterns | `SelectedItems`/`Selection` (`ISelectionModel`) |
| `ListBox.ScrollIntoView(item)` | `AutoScrollToSelectedItem` + item `BringIntoView()` |

## Conversion Example

WPF XAML:

```xaml
<ListView ItemsSource="{Binding Users}"
          SelectionMode="Extended"
          SelectedItem="{Binding SelectedUser, Mode=TwoWay}">
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
         x:DataType="vm:UsersViewModel"
         ItemsSource="{CompiledBinding Users}"
         SelectedItem="{CompiledBinding SelectedUser, Mode=TwoWay}"
         SelectionMode="Multiple"
         AutoScrollToSelectedItem="True">
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

## Avalonia C# Equivalent

```csharp
using Avalonia.Controls;

var list = new ListBox
{
    ItemsSource = viewModel.Users,
    SelectionMode = SelectionMode.Multiple | SelectionMode.Toggle,
    AutoScrollToSelectedItem = true
};

list.Selection.Select(0);
list.Selection.Select(2);
list.Selection.Deselect(0);
list.Selection.SelectedIndex = 3;
```

## Troubleshooting

1. Multi-select behavior feels different from WPF `Extended`.
- Use `SelectionMode="Multiple"` and optionally add `Toggle` for click-to-toggle semantics.

2. Selected item is set but not visible.
- Enable `AutoScrollToSelectedItem`; for custom containers call `BringIntoView()` when needed.

3. Selection resets after source refresh.
- Keep stable item identity and avoid replacing collections unnecessarily.
