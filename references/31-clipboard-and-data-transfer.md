# Clipboard and DataTransfer Workflows

## Table of Contents
1. Scope and APIs
2. Clipboard Access Model
3. Typed Clipboard Patterns
4. DataTransfer Payload Authoring
5. XAML-First and Code-Only Usage
6. Best Practices
7. Troubleshooting

## Scope and APIs

Primary APIs:
- `TopLevel.GetTopLevel(...)`
- `TopLevel.Clipboard`
- `IClipboard`
- `ClipboardExtensions`
- `IDataTransfer`, `IAsyncDataTransfer`
- `DataTransfer`, `DataTransferItem`
- `DataFormat`

Important members:
- `IClipboard.ClearAsync()`, `SetDataAsync(...)`, `TryGetDataAsync()`
- `IClipboard.FlushAsync()`
- `ClipboardExtensions.SetTextAsync(...)`, `TryGetTextAsync()`
- `ClipboardExtensions.SetFileAsync(...)`, `TryGetFileAsync()`, `TryGetFilesAsync()`
- `ClipboardExtensions.SetBitmapAsync(...)`, `TryGetBitmapAsync()`
- `DataTransfer.Add(...)`
- `DataTransferItem.CreateText(...)`, `CreateFile(...)`, `Set(...)`, `SetText(...)`, `SetFile(...)`

Reference source files:
- `src/Avalonia.Controls/TopLevel.cs`
- `src/Avalonia.Base/Input/Platform/IClipboard.cs`
- `src/Avalonia.Base/Input/Platform/ClipboardExtensions.cs`
- `src/Avalonia.Base/Input/IDataTransfer.cs`
- `src/Avalonia.Base/Input/IAsyncDataTransfer.cs`
- `src/Avalonia.Base/Input/DataTransfer.cs`
- `src/Avalonia.Base/Input/DataTransferItem.cs`

## Clipboard Access Model

Access pattern:
1. Resolve `TopLevel` from active visual.
2. Check `topLevel.Clipboard` for null.
3. Use typed helper extensions for most operations.
4. Dispose data transfer objects returned by `TryGetDataAsync()` when required.

## Typed Clipboard Patterns

```csharp
using System.Threading.Tasks;
using Avalonia.Controls;
using Avalonia.Input.Platform;

public static class ClipboardWorkflows
{
    public static async Task CopyTextAsync(Control anchor, string text)
    {
        TopLevel? top = TopLevel.GetTopLevel(anchor);
        if (top?.Clipboard is { } clipboard)
            await clipboard.SetTextAsync(text);
    }

    public static async Task<string?> PasteTextAsync(Control anchor)
    {
        TopLevel? top = TopLevel.GetTopLevel(anchor);
        if (top?.Clipboard is not { } clipboard)
            return null;

        return await clipboard.TryGetTextAsync();
    }
}
```

## DataTransfer Payload Authoring

Use `DataTransfer` for multi-format payloads:

```csharp
using Avalonia.Input;
using Avalonia.Platform.Storage;

public static class DataTransferFactory
{
    public static DataTransfer CreateTextAndFilePayload(string text, IStorageItem file)
    {
        DataTransfer transfer = new();

        DataTransferItem item = DataTransferItem.CreateText(text);
        item.SetFile(file);

        transfer.Add(item);
        return transfer;
    }
}
```

## XAML-First and Code-Only Usage

Default mode:
- Bind copy/paste actions through commands in XAML.
- Keep clipboard logic in service/viewmodel layer.
- Use code-only UI construction only when requested.

XAML-first complete example:

```xml
<UserControl xmlns="https://github.com/avaloniaui"
             xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
             xmlns:vm="using:MyApp.ViewModels"
             x:DataType="vm:ClipboardViewModel">
  <StackPanel Margin="12" Spacing="8">
    <TextBox Text="{CompiledBinding InputText, Mode=TwoWay}" />
    <StackPanel Orientation="Horizontal" Spacing="8">
      <Button Content="Copy" Command="{CompiledBinding CopyCommand}" />
      <Button Content="Paste" Command="{CompiledBinding PasteCommand}" />
    </StackPanel>
    <TextBlock Text="{CompiledBinding LastPaste}" />
  </StackPanel>
</UserControl>
```

Code-only alternative (on request):

```csharp
using System.Threading.Tasks;
using Avalonia.Controls;
using Avalonia.Input.Platform;

public static class CodeOnlyClipboardSample
{
    public static async Task RoundTripAsync(Control anchor)
    {
        TopLevel? top = TopLevel.GetTopLevel(anchor);
        if (top?.Clipboard is not { } clipboard)
            return;

        await clipboard.SetTextAsync("clipboard sample");
        string? value = await clipboard.TryGetTextAsync();

        // Use value in viewmodel/service flow.
        _ = value;
    }
}
```

## Best Practices

- Prefer typed `ClipboardExtensions` over raw format probing.
- Keep clipboard operations short-lived and user-triggered.
- Avoid storing large clipboard payloads in long-lived objects.
- Respect platform differences (some operations are best-effort).

## Troubleshooting

1. Clipboard is null:
- Platform backend does not expose clipboard feature.

2. `TryGetTextAsync()` returns null:
- Clipboard does not currently contain text format.

3. In-process clipboard behavior differs across platforms:
- `TryGetInProcessDataAsync()` has platform-specific support.

4. Data transfer lifecycle bugs:
- Ensure objects returned by `TryGetDataAsync()` are disposed promptly.
