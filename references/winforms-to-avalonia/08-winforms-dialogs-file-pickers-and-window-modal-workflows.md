# WinForms Dialogs, File Pickers, and Modal Workflows to Avalonia

## Table of Contents
1. Scope and APIs
2. Dialog Mapping Matrix
3. Conversion Example
4. C# Equivalent
5. Troubleshooting

## Scope and APIs

Primary WinForms APIs:

- `OpenFileDialog`, `SaveFileDialog`, `FolderBrowserDialog`
- `ColorDialog`, `FontDialog`
- `Form.ShowDialog()`

Primary Avalonia APIs:

- `TopLevel.GetTopLevel(...)`
- `IStorageProvider` (`OpenFilePickerAsync`, `SaveFilePickerAsync`, `OpenFolderPickerAsync`)
- `Window.ShowDialog(owner)`
- control-based color/font pickers in custom dialog windows

## Dialog Mapping Matrix

| WinForms | Avalonia |
|---|---|
| `OpenFileDialog` | `StorageProvider.OpenFilePickerAsync` |
| `SaveFileDialog` | `StorageProvider.SaveFilePickerAsync` |
| `FolderBrowserDialog` | `StorageProvider.OpenFolderPickerAsync` |
| `ShowDialog()` | `await window.ShowDialog(owner)` |
| `ColorDialog` / `FontDialog` | custom dialog with `ColorPicker`/font chooser UI |

## Conversion Example

WinForms C#:

```csharp
using var open = new OpenFileDialog { Filter = "Images|*.png;*.jpg" };
if (open.ShowDialog(this) == DialogResult.OK)
{
    LoadImage(open.FileName);
}
```

Avalonia XAML:

```xaml
<UserControl xmlns="https://github.com/avaloniaui"
             xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
             xmlns:vm="using:MyApp.ViewModels"
             x:DataType="vm:FilesViewModel">
  <StackPanel Spacing="8">
    <Button Content="Open Image" Command="{CompiledBinding OpenImageCommand}" />
    <TextBlock Text="{CompiledBinding SelectedPath}" />
  </StackPanel>
</UserControl>
```

## C# Equivalent

```csharp
using Avalonia.Controls;
using Avalonia.Platform.Storage;

public async Task OpenImageAsync(Control anchor)
{
    var top = TopLevel.GetTopLevel(anchor);
    if (top is null || !top.StorageProvider.CanOpen)
        return;

    var files = await top.StorageProvider.OpenFilePickerAsync(new FilePickerOpenOptions
    {
        Title = "Open Image",
        AllowMultiple = false,
        FileTypeFilter = new[]
        {
            new FilePickerFileType("Images") { Patterns = new[] { "*.png", "*.jpg", "*.jpeg" } }
        }
    });

    var selected = files.Count > 0 ? files[0] : null;
    if (selected is not null)
        viewModel.SelectedPath = selected.Path.ToString();
}
```

Modal dialog example:

```csharp
var dialog = new Window { Width = 360, Height = 220, Title = "Confirm" };
if (TopLevel.GetTopLevel(anchor) is Window owner)
    await dialog.ShowDialog(owner);
```

## Troubleshooting

1. Dialog API seems different from WinForms blocking pattern.
- use async command flows around `await` rather than blocking UI thread.

2. Path handling fails on non-desktop targets.
- use storage streams/bookmarks and avoid assuming local filesystem paths.

3. Color/font dialogs are missing.
- build custom modal UI around Avalonia picker controls.
