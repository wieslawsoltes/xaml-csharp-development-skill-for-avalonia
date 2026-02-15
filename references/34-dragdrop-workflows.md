# DragDrop Workflows

## Table of Contents
1. Scope and APIs
2. DragDrop Event Model
3. Drop Target Patterns
4. Drag Source Patterns
5. XAML-First and Code-Only Usage
6. Best Practices
7. Troubleshooting

## Scope and APIs

Primary APIs:
- `DragDrop`
- `DragEventArgs`
- `DragDropEffects`
- `IDataTransfer`, `IAsyncDataTransfer`
- `DataTransfer`, `DataTransferItem`

Important members:
- `DragDrop.AllowDropProperty`
- `DragDrop.DragEnterEvent`, `DragLeaveEvent`, `DragOverEvent`, `DropEvent`
- `DragDrop.SetAllowDrop(...)`
- `DragDrop.AddDragOverHandler(...)`, `AddDropHandler(...)`
- `DragDrop.DoDragDropAsync(...)`
- `DragEventArgs.DataTransfer`, `DragEffects`, `GetPosition(...)`
- `DataTransferItem.CreateText(...)`, `CreateFile(...)`, `Set(...)`
- `DataTransferExtensions.TryGetText()`, `TryGetFiles()`

Reference source files:
- `src/Avalonia.Base/Input/DragDrop.cs`
- `src/Avalonia.Base/Input/DragEventArgs.cs`
- `src/Avalonia.Base/Input/IDataTransfer.cs`
- `src/Avalonia.Base/Input/DataTransfer.cs`
- `src/Avalonia.Base/Input/DataTransferItem.cs`
- `src/Avalonia.Base/Input/DataTransferExtensions.cs`

## DragDrop Event Model

Target route model:
1. Enable drop with `DragDrop.AllowDrop`.
2. Handle `DragOver` and assign `e.DragEffects`.
3. Handle `Drop` and consume `e.DataTransfer` payload.

Source model:
1. Build a `DataTransfer` payload.
2. Call `DragDrop.DoDragDropAsync(triggerEvent, payload, allowedEffects)`.
3. Use returned effect to confirm operation outcome.

## Drop Target Patterns

```csharp
using System;
using Avalonia.Controls;
using Avalonia.Input;
using Avalonia.Platform.Storage;

public sealed class FileDropBehavior
{
    public static void Attach(Control target, Action<IStorageItem[]> onFilesDropped)
    {
        DragDrop.SetAllowDrop(target, true);

        target.AddHandler(DragDrop.DragOverEvent, (_, e) =>
        {
            IStorageItem[]? files = e.DataTransfer.TryGetFiles();
            e.DragEffects = files is { Length: > 0 } ? DragDropEffects.Copy : DragDropEffects.None;
            e.Handled = true;
        });

        target.AddHandler(DragDrop.DropEvent, (_, e) =>
        {
            IStorageItem[]? files = e.DataTransfer.TryGetFiles();
            if (files is { Length: > 0 })
                onFilesDropped(files);

            e.Handled = true;
        });
    }
}
```

## Drag Source Patterns

```csharp
using System.Threading.Tasks;
using Avalonia.Input;

public static class DragSourceWorkflows
{
    public static Task<DragDropEffects> StartTextDragAsync(PointerEventArgs trigger, string text)
    {
        DataTransfer payload = new();
        payload.Add(DataTransferItem.CreateText(text));

        return DragDrop.DoDragDropAsync(trigger, payload, DragDropEffects.Copy | DragDropEffects.Move);
    }
}
```

## XAML-First and Code-Only Usage

Default mode:
- Declare drop targets in XAML first.
- Wire drag/drop behavior via reusable behavior/service classes.
- Use code-only UI trees only when requested.

XAML-first complete example:

```xml
<UserControl xmlns="https://github.com/avaloniaui"
             xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
             xmlns:vm="using:MyApp.ViewModels"
             x:DataType="vm:DragDropViewModel">
  <Border Margin="12"
          Padding="12"
          BorderBrush="Gray"
          BorderThickness="1"
          DragDrop.AllowDrop="True">
    <TextBlock Text="{CompiledBinding DropHint}" />
  </Border>
</UserControl>
```

Code-only alternative (on request):

```csharp
using System;
using Avalonia;
using Avalonia.Controls;
using Avalonia.Media;
using Avalonia.Input;

public static class CodeOnlyDragDropSample
{
    public static Control BuildDropSurface(Action<string> onText)
    {
        Border surface = new()
        {
            Padding = new Thickness(12),
            BorderBrush = Brushes.Gray,
            BorderThickness = new Thickness(1),
            Child = new TextBlock { Text = "Drop text or files here" }
        };

        DragDrop.SetAllowDrop(surface, true);
        surface.AddHandler(DragDrop.DropEvent, (_, e) =>
        {
            string? text = e.DataTransfer.TryGetText();
            if (!string.IsNullOrEmpty(text))
                onText(text);

            e.Handled = true;
        });

        return surface;
    }
}
```

## Best Practices

- Set `DragEffects` in `DragOver` for deterministic UX feedback.
- Keep drop handlers lightweight; dispatch heavy work off UI thread.
- Prefer typed data extraction (`TryGetText`, `TryGetFiles`) over raw format parsing.
- Keep drag source payload minimal and explicit.

## Troubleshooting

1. Drop handlers never run:
- `DragDrop.AllowDrop` was not enabled.
- Another control intercepts input before target.

2. Drop cursor always disabled:
- `DragOver` did not set `e.DragEffects` to a non-`None` value.

3. Source drag returns `None` effect:
- Target rejected data or operation was canceled.

4. Testing drag/drop is flaky:
- Prefer headless drag-drop helpers over manual args construction.
