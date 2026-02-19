# WinForms Drag/Drop, Clipboard, and Data Transfer to Avalonia

## Table of Contents
1. Scope and APIs
2. Data Transfer Mapping
3. Conversion Example
4. C# Equivalent
5. Troubleshooting

## Scope and APIs

Primary WinForms APIs:

- `Control.DoDragDrop(...)`
- drag events (`DragEnter`, `DragOver`, `DragDrop`)
- `Clipboard` helpers

Primary Avalonia APIs:

- `DragDrop` (`DoDragDropAsync`, `AllowDrop`, drag/drop routed events)
- `DataTransfer` and `DataTransferItem`
- `TopLevel.Clipboard` + clipboard extension helpers

## Data Transfer Mapping

| WinForms | Avalonia |
|---|---|
| `DoDragDrop(data, effects)` | `await DragDrop.DoDragDropAsync(...)` |
| `DragDropEffects` | `DragDropEffects` |
| `e.Data.GetData(...)` | `e.DataTransfer.TryGet...` helpers |
| `Clipboard.SetText/GetText` | `IClipboard` (`SetTextAsync`, `TryGetTextAsync`) |

## Conversion Example

WinForms C#:

```csharp
private void Source_MouseDown(object sender, MouseEventArgs e)
{
    if (sourceList.SelectedItem is string text)
        sourceList.DoDragDrop(text, DragDropEffects.Copy);
}

private void Target_DragDrop(object sender, DragEventArgs e)
{
    var text = e.Data?.GetData(DataFormats.Text)?.ToString();
    if (!string.IsNullOrWhiteSpace(text))
        targetList.Items.Add(text);
}
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
            Content="Copy Target Items to Clipboard"
            Command="{CompiledBinding CopyToClipboardCommand}" />
  </Grid>
</UserControl>
```

## C# Equivalent

```csharp
using System;
using System.Linq;
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

    await DragDrop.DoDragDropAsync(e, transfer, DragDropEffects.Copy | DragDropEffects.Move);
};

TargetList.AddHandler(DragDrop.DragOverEvent, (_, e) =>
{
    e.DragEffects = DragDropEffects.Copy;
});

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

1. Drop handlers never fire.
- set `DragDrop.AllowDrop="True"` on the drop target.

2. Drag starts but data is empty.
- ensure `DataTransfer` contains at least one `DataTransferItem` with the expected format.

3. Clipboard APIs fail on headless/service contexts.
- guard for `TopLevel` and clipboard availability before invoking clipboard operations.
