# Storage Provider and File Picker Workflows

## Table of Contents
1. Scope and APIs
2. Capability and Lifecycle Model
3. Open/Save/Folder Picker Patterns
4. Bookmarks and Path Strategies
5. XAML-First and Code-Only Usage
6. Best Practices
7. Troubleshooting

## Scope and APIs

Primary APIs:
- `TopLevel.GetTopLevel(...)`
- `TopLevel.StorageProvider`
- `IStorageProvider`
- `IStorageFile`, `IStorageFolder`, `IStorageItem`
- `FilePickerOpenOptions`, `FilePickerSaveOptions`, `FolderPickerOpenOptions`
- `FilePickerFileType`
- `StorageProviderExtensions.TryGetFileFromPathAsync(...)`
- `StorageProviderExtensions.TryGetFolderFromPathAsync(...)`
- `StorageProviderExtensions.TryGetLocalPath(...)`
- `WellKnownFolder`

Important members:
- `IStorageProvider.CanOpen`, `CanSave`, `CanPickFolder`
- `OpenFilePickerAsync(...)`
- `SaveFilePickerAsync(...)`, `SaveFilePickerWithResultAsync(...)`
- `OpenFolderPickerAsync(...)`
- `TryGetFileFromPathAsync(...)`, `TryGetFolderFromPathAsync(...)`
- `TryGetWellKnownFolderAsync(...)`
- `IStorageFile.OpenReadAsync()`, `OpenWriteAsync()`
- `IStorageItem.SaveBookmarkAsync()`, `DeleteAsync()`, `MoveAsync(...)`

Reference source files:
- `src/Avalonia.Controls/TopLevel.cs`
- `src/Avalonia.Base/Platform/Storage/IStorageProvider.cs`
- `src/Avalonia.Base/Platform/Storage/IStorageItem.cs`
- `src/Avalonia.Base/Platform/Storage/IStorageFile.cs`
- `src/Avalonia.Base/Platform/Storage/IStorageFolder.cs`
- `src/Avalonia.Base/Platform/Storage/FilePickerOpenOptions.cs`
- `src/Avalonia.Base/Platform/Storage/FilePickerSaveOptions.cs`
- `src/Avalonia.Base/Platform/Storage/StorageProviderExtensions.cs`
- `src/Avalonia.Base/Platform/Storage/WellKnownFolder.cs`

## Capability and Lifecycle Model

Provider model:
1. Resolve `TopLevel` from a visual at interaction time.
2. Use `TopLevel.StorageProvider`.
3. Guard with capability flags before invoking dialogs.
4. Dispose storage items when not needed.

Notes:
- Unsupported platforms may expose a fallback/no-op provider.
- Path semantics vary by platform (`file:` vs `content:` or isolated browser paths).

## Open/Save/Folder Picker Patterns

```csharp
using System;
using System.Collections.Generic;
using System.Threading.Tasks;
using Avalonia.Controls;
using Avalonia.Platform.Storage;

public static class StorageWorkflows
{
    public static async Task<IReadOnlyList<IStorageFile>> OpenJsonFilesAsync(Control anchor)
    {
        TopLevel? top = TopLevel.GetTopLevel(anchor);
        if (top is null || !top.StorageProvider.CanOpen)
            return Array.Empty<IStorageFile>();

        IStorageFolder? start = await top.StorageProvider.TryGetWellKnownFolderAsync(WellKnownFolder.Documents);

        FilePickerFileType json = new("JSON")
        {
            Patterns = new[] { "*.json" },
            MimeTypes = new[] { "application/json" }
        };

        return await top.StorageProvider.OpenFilePickerAsync(new FilePickerOpenOptions
        {
            Title = "Open JSON",
            AllowMultiple = true,
            SuggestedStartLocation = start,
            FileTypeFilter = new[] { json },
            SuggestedFileType = json
        });
    }

    public static async Task<IStorageFile?> SaveTextFileAsync(Control anchor, string suggestedName)
    {
        TopLevel? top = TopLevel.GetTopLevel(anchor);
        if (top is null || !top.StorageProvider.CanSave)
            return null;

        FilePickerFileType text = new("Text")
        {
            Patterns = new[] { "*.txt" },
            MimeTypes = new[] { "text/plain" }
        };

        return await top.StorageProvider.SaveFilePickerAsync(new FilePickerSaveOptions
        {
            Title = "Save As",
            SuggestedFileName = suggestedName,
            DefaultExtension = "txt",
            FileTypeChoices = new[] { text },
            SuggestedFileType = text,
            ShowOverwritePrompt = true
        });
    }
}
```

## Bookmarks and Path Strategies

Bookmark strategy:
- If `IStorageItem.CanBookmark` is true, persist bookmark IDs instead of raw paths.
- Rehydrate with `OpenFileBookmarkAsync(...)` / `OpenFolderBookmarkAsync(...)`.

Path strategy:
- Use `TryGetLocalPath()` only when truly needed.
- Prefer `IStorageFile.OpenReadAsync()` and `OpenWriteAsync()` over path-based IO.

## XAML-First and Code-Only Usage

Default mode:
- Trigger storage workflows from XAML-bound commands.
- Keep picker logic in viewmodel/service code.
- Use code-only UI construction only when explicitly requested.

XAML-first complete example:

```xml
<UserControl xmlns="https://github.com/avaloniaui"
             xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
             xmlns:vm="using:MyApp.ViewModels"
             x:DataType="vm:StorageToolsViewModel">
  <StackPanel Margin="12" Spacing="8">
    <Button Content="Open JSON" Command="{CompiledBinding OpenJsonCommand}" />
    <Button Content="Save Report" Command="{CompiledBinding SaveReportCommand}" />
    <TextBlock Text="{CompiledBinding LastPath}" />
  </StackPanel>
</UserControl>
```

Code-only alternative (on request):

```csharp
using System.IO;
using System.Text;
using System.Threading.Tasks;
using Avalonia.Controls;
using Avalonia.Platform.Storage;

public static class CodeOnlyStorageSample
{
    public static async Task SaveSampleAsync(Control anchor)
    {
        IStorageFile? file = await StorageWorkflows.SaveTextFileAsync(anchor, "report.txt");
        if (file is null)
            return;

        await using Stream stream = await file.OpenWriteAsync();
        await using StreamWriter writer = new(stream, Encoding.UTF8, leaveOpen: false);
        await writer.WriteLineAsync("Generated by Avalonia storage workflow.");
    }
}
```

## Best Practices

- Use capability flags before picker calls.
- Keep picker option objects explicit and deterministic.
- Prefer stream-based access to avoid platform path assumptions.
- Dispose `IStorageItem` instances once done.
- Keep all picker logic async and cancellation-aware at app level.

## Troubleshooting

1. Empty picker result:
- User canceled dialog.
- Capability flag is false on current platform.

2. Path-dependent code breaks on mobile/browser:
- `Path` may be URI-like and not a local file path.
- Use storage item streams and bookmarks.

3. Save file returns null:
- User canceled.
- Platform save operation unsupported.

4. Folder picker unavailable:
- `CanPickFolder` false for current runtime/backend.
