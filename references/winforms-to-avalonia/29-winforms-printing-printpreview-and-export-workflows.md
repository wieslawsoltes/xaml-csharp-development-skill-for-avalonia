# WinForms Printing, PrintPreview, and Export Workflows to Avalonia

## Table of Contents
1. Scope and APIs
2. Printing and Export Mapping
3. Conversion Example
4. C# Equivalent
5. Troubleshooting

## Scope and APIs

Primary WinForms APIs:

- `PrintDocument`
- `PrintPreviewDialog`
- printer-specific drawing workflows

Primary Avalonia patterns:

- file export (PDF/CSV/HTML or app-specific formats)
- preview in-app via document/image views
- launch exported files through platform launcher
- external printing integration packages for direct printer pipelines

## Printing and Export Mapping

| WinForms | Avalonia |
|---|---|
| `PrintDocument.PrintPage` | render/export document content in app services |
| `PrintPreviewDialog` | in-app preview control/window over exported model |
| `PrintDialog` direct OS print flow | external package/platform-specific integration |
| synchronous print flows | async save/export + launch workflows |

Avalonia core does not provide a direct built-in `PrintDocument`/`PrintPreviewDialog` equivalent.

## Conversion Example

WinForms C#:

```csharp
var doc = new PrintDocument();
doc.PrintPage += (_, e) => e.Graphics.DrawString(reportText, Font, Brushes.Black, 20, 20);

using var preview = new PrintPreviewDialog { Document = doc };
preview.ShowDialog(this);
```

Avalonia XAML:

```xaml
<UserControl xmlns="https://github.com/avaloniaui"
             xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
             xmlns:vm="using:MyApp.ViewModels"
             x:DataType="vm:ReportViewModel">
  <StackPanel Spacing="8">
    <Button Content="Preview Report"
            Command="{CompiledBinding PreviewReportCommand}" />
    <Button Content="Export Report"
            Command="{CompiledBinding ExportReportCommand}" />
  </StackPanel>
</UserControl>
```

## C# Equivalent

```csharp
using System.IO;
using System.Threading.Tasks;
using Avalonia.Controls;
using Avalonia.Platform.Storage;

public static async Task ExportReportAsync(TopLevel topLevel, string reportText)
{
    var file = await topLevel.StorageProvider.SaveFilePickerAsync(new FilePickerSaveOptions
    {
        Title = "Export Report",
        SuggestedFileName = "report.txt",
        FileTypeChoices = new[]
        {
            new FilePickerFileType("Text") { Patterns = new[] { "*.txt" } }
        }
    });

    if (file is null)
        return;

    await using var stream = await file.OpenWriteAsync();
    await using var writer = new StreamWriter(stream);
    await writer.WriteAsync(reportText);

    await topLevel.Launcher.LaunchFileAsync(file);
}
```

## Troubleshooting

1. Expecting full WinForms print APIs in core Avalonia.
- plan explicit export/preview architecture or integrate a dedicated printing package.

2. Large reports freeze UI.
- generate export content off the UI thread and marshal only UI state updates.

3. Exported files open inconsistently.
- verify file type associations and launcher support on each target platform.
