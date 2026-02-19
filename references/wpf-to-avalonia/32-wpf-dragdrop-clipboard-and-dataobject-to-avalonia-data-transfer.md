# WPF DragDrop/Clipboard/DataObject to Avalonia DataTransfer

## Table of Contents
1. Scope and APIs
2. Data Transfer Mapping
3. Conversion Example
4. Avalonia C# Equivalent
5. Troubleshooting

## Scope and APIs

Primary WPF APIs:

- `DragDrop.DoDragDrop(...)`
- `DataObject`
- drag events (`DragEnter`, `DragOver`, `Drop`)
- `Clipboard`

Primary Avalonia APIs:

- `DragDrop.DoDragDropAsync(...)`
- `DataTransfer` and `DataTransferItem`
- `DragDrop.AllowDrop` + routed drag/drop events
- `TopLevel.Clipboard` + clipboard extensions

## Data Transfer Mapping

| WPF | Avalonia |
|---|---|
| `DataObject.SetData(...)` | `DataTransfer` + `DataTransferItem` |
| `DoDragDrop` sync call | `DoDragDropAsync` async call |
| `e.Data.GetData(...)` | `e.DataTransfer.TryGet...` helpers |
| `Clipboard.SetText/GetText` | `SetTextAsync`/`TryGetTextAsync` |

## Conversion Example

WPF C#:

```csharp
var data = new DataObject(DataFormats.Text, selectedText);
DragDrop.DoDragDrop(sourceList, data, DragDropEffects.Copy);

var dropped = e.Data.GetData(DataFormats.Text) as string;
```

Avalonia XAML:

```xaml
<UserControl xmlns="https://github.com/avaloniaui"
             xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
             xmlns:vm="using:MyApp.ViewModels"
             x:DataType="vm:TransferViewModel">
  <Grid ColumnDefinitions="*,*" RowDefinitions="*,Auto" ColumnSpacing="12" RowSpacing="8">
    <ListBox x:Name="SourceList"
             Grid.Column="0"
             ItemsSource="{CompiledBinding SourceItems}"
             SelectedItem="{CompiledBinding SelectedSourceItem, Mode=TwoWay}" />

    <ListBox x:Name="TargetList"
             Grid.Column="1"
             DragDrop.AllowDrop="True"
             ItemsSource="{CompiledBinding TargetItems}" />

    <Button Grid.Row="1"
            Grid.ColumnSpan="2"
            Content="Copy Target Items"
            Command="{CompiledBinding CopyItemsCommand}" />
  </Grid>
</UserControl>
```

## Avalonia C# Equivalent

```csharp
using System;
using System.Threading.Tasks;
using Avalonia.Controls;
using Avalonia.Input;
using Avalonia.Input.Platform;

SourceList.PointerPressed += async (_, e) =>
{
    if (viewModel.SelectedSourceItem is not string text)
        return;

    var transfer = new DataTransfer();
    transfer.Add(DataTransferItem.CreateText(text));

    await DragDrop.DoDragDropAsync(e, transfer, DragDropEffects.Copy);
};

TargetList.AddHandler(DragDrop.DragOverEvent, (_, e) => e.DragEffects = DragDropEffects.Copy);
TargetList.AddHandler(DragDrop.DropEvent, (_, e) =>
{
    var text = e.DataTransfer.TryGetText();
    if (!string.IsNullOrWhiteSpace(text))
        viewModel.TargetItems.Add(text);
});

var top = TopLevel.GetTopLevel(TargetList);
if (top?.Clipboard is { } clipboard)
    await clipboard.SetTextAsync(string.Join(Environment.NewLine, viewModel.TargetItems));
```

## Troubleshooting

1. Drop handlers never run.
- set `DragDrop.AllowDrop="True"` on the target control.

2. Drag succeeds but payload is empty.
- ensure `DataTransfer` contains a matching text/file format item.

3. Clipboard operations fail in some hosts.
- guard for `TopLevel` and clipboard availability before calling APIs.
