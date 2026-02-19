# WinForms ListView (Details, Groups, Virtual Mode) to Avalonia

## Table of Contents
1. Scope and APIs
2. ListView Mapping
3. Conversion Example
4. C# Equivalent
5. Troubleshooting

## Scope and APIs

Primary WinForms APIs:

- `ListView` (`View.Details`, columns, `FullRowSelect`)
- `ListViewGroup`
- `VirtualMode` (`RetrieveVirtualItem`)

Primary Avalonia APIs/patterns:

- `ListBox` + `DataTemplate` (details-style rows)
- grouped collections rendered with `ItemsControl` + nested `ListBox`
- optional `DataGrid` package when built-in column behaviors are required

## ListView Mapping

| WinForms | Avalonia |
|---|---|
| `View.Details` with columns | `ListBox` row template with a `Grid` of cells |
| `ListViewGroup` headers | grouped view-model collections rendered by `ItemsControl` |
| `VirtualMode` callbacks | virtualized items controls + incremental loading in view model |
| `SmallImageList`/`LargeImageList` | `Image`/`PathIcon` inside item templates |

## Conversion Example

WinForms C#:

```csharp
filesList.View = View.Details;
filesList.FullRowSelect = true;
filesList.Columns.Add("Name", 280);
filesList.Columns.Add("Modified", 170);
filesList.Columns.Add("Size", 120);

filesList.Groups.Add(new ListViewGroup("Recent"));
filesList.VirtualMode = true;
filesList.VirtualListSize = repository.Count;
filesList.RetrieveVirtualItem += OnRetrieveVirtualItem;
```

Avalonia XAML:

```xaml
<UserControl xmlns="https://github.com/avaloniaui"
             xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
             xmlns:vm="using:MyApp.ViewModels"
             x:DataType="vm:FilesViewModel">
  <ItemsControl ItemsSource="{CompiledBinding Groups}">
    <ItemsControl.ItemTemplate>
      <DataTemplate x:DataType="vm:FileGroupViewModel">
        <StackPanel Margin="0,0,0,12" Spacing="6">
          <TextBlock FontWeight="SemiBold"
                     Text="{CompiledBinding Name}" />

          <ListBox ItemsSource="{CompiledBinding Items}"
                   SelectedItem="{CompiledBinding SelectedItem, Mode=TwoWay}">
            <ListBox.ItemTemplate>
              <DataTemplate x:DataType="vm:FileItemViewModel">
                <Grid ColumnDefinitions="Auto,2*,*,Auto" ColumnSpacing="10">
                  <PathIcon Grid.Column="0"
                            Width="16"
                            Height="16"
                            Data="{CompiledBinding KindIcon}" />
                  <TextBlock Grid.Column="1" Text="{CompiledBinding Name}" />
                  <TextBlock Grid.Column="2" Text="{CompiledBinding ModifiedLabel}" />
                  <TextBlock Grid.Column="3"
                             HorizontalAlignment="Right"
                             Text="{CompiledBinding SizeLabel}" />
                </Grid>
              </DataTemplate>
            </ListBox.ItemTemplate>
          </ListBox>
        </StackPanel>
      </DataTemplate>
    </ItemsControl.ItemTemplate>
  </ItemsControl>
</UserControl>
```

## C# Equivalent

```csharp
using Avalonia.Controls;

var groupsHost = new StackPanel
{
    Spacing = 12
};

foreach (var group in viewModel.Groups)
{
    groupsHost.Children.Add(new TextBlock
    {
        Text = group.Name
    });

    groupsHost.Children.Add(new ListBox
    {
        ItemsSource = group.Items
    });
}
```

## Troubleshooting

1. Large lists regress in performance.
- keep item templates lean and move filtering/sorting to view-model pipelines.

2. Details rows are hard to align.
- use shared column definitions per row template and avoid pixel offsets from WinForms layouts.

3. Column-resize/sort/edit parity is required.
- use `Avalonia.Controls.DataGrid` for full grid-style behavior instead of forcing it into `ListBox`.
