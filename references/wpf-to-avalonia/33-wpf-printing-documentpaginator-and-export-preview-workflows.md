# WPF Printing, DocumentPaginator, and Export/Preview Workflows to Avalonia

## Table of Contents
1. Scope and APIs
2. Printing Mapping
3. Conversion Example
4. Avalonia C# Equivalent
5. Troubleshooting

## Scope and APIs

Primary WPF APIs:

- `PrintDialog`
- `DocumentPaginator`
- `FlowDocument`/`FixedDocument` print flows

Primary Avalonia patterns:

- export-first report/document workflows
- in-app preview windows for exported content
- launcher integration to open exported outputs
- optional external printing packages for direct printer support

## Printing Mapping

| WPF | Avalonia |
|---|---|
| `PrintDialog.PrintDocument(...)` | explicit export service + preview/launch flow |
| `DocumentPaginator` print paging | report pagination in app services/view-models |
| sync print flow | async export and user-driven open/print steps |

Avalonia core does not provide direct equivalents for WPF printing APIs.

## Conversion Example

WPF C#:

```csharp
var dialog = new PrintDialog();
if (dialog.ShowDialog() == true)
    dialog.PrintDocument(((IDocumentPaginatorSource)document).DocumentPaginator, "Report");
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

## Avalonia C# Equivalent

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

1. Expecting direct WPF print API parity.
- treat printing as an explicit subsystem (export + preview + optional package integration).

2. Report generation blocks UI.
- run heavy generation off the UI thread and marshal only UI updates.

3. Export open/print behavior varies by OS.
- validate launcher/file-association behavior per target platform.
