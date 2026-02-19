# WPF DocumentViewer/FlowDocumentReader and Rich Reading Surfaces to Avalonia

## Table of Contents
1. Scope and APIs
2. Rich Document Surface Mapping
3. Conversion Example
4. Avalonia C# Equivalent
5. Troubleshooting

## Scope and APIs

Primary WPF APIs:

- `DocumentViewer`
- `FlowDocumentReader`
- `FlowDocument` reading surfaces

Primary Avalonia patterns:

- structured content rendering with `ScrollViewer` + templated sections
- markdown/html/document components from dedicated libraries
- export/preview document workflows for print-like experiences

## Rich Document Surface Mapping

| WPF | Avalonia |
|---|---|
| `DocumentViewer` fixed document surface | custom document view + virtualization/paging patterns |
| `FlowDocumentReader` reading modes | template-driven reading UI and optional package integration |
| document command bars | command-based shell around content host |

Avalonia core does not include direct `DocumentViewer`/`FlowDocumentReader` equivalents.

## Conversion Example

WPF XAML:

```xaml
<FlowDocumentReader>
  <FlowDocument>
    <Paragraph FontWeight="Bold">Quarterly Report</Paragraph>
    <Paragraph>Revenue increased by 12%.</Paragraph>
  </FlowDocument>
</FlowDocumentReader>
```

Avalonia XAML:

```xaml
<UserControl xmlns="https://github.com/avaloniaui"
             xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
             xmlns:vm="using:MyApp.ViewModels"
             x:DataType="vm:ReportReaderViewModel">
  <DockPanel>
    <StackPanel DockPanel.Dock="Top" Orientation="Horizontal" Spacing="8" Margin="0,0,0,8">
      <Button Content="Export" Command="{CompiledBinding ExportCommand}" />
      <Button Content="Open External" Command="{CompiledBinding OpenExternalCommand}" />
    </StackPanel>

    <ScrollViewer>
      <StackPanel Spacing="8">
        <TextBlock FontSize="18" FontWeight="Bold" Text="{CompiledBinding Title}" />
        <ItemsControl ItemsSource="{CompiledBinding Paragraphs}">
          <ItemsControl.ItemTemplate>
            <DataTemplate x:DataType="vm:ParagraphViewModel">
              <TextBlock TextWrapping="Wrap" Text="{CompiledBinding Text}" />
            </DataTemplate>
          </ItemsControl.ItemTemplate>
        </ItemsControl>
      </StackPanel>
    </ScrollViewer>
  </DockPanel>
</UserControl>
```

## Avalonia C# Equivalent

```csharp
using System.Linq;
using Avalonia.Controls;

var bodyText = string.Join("\n\n", viewModel.Paragraphs.Select(p => p.Text));

var reader = new ScrollViewer
{
    Content = new StackPanel
    {
        Spacing = 8,
        Children =
        {
            new TextBlock { Text = viewModel.Title, FontSize = 18, FontWeight = Avalonia.Media.FontWeight.Bold },
            new TextBlock { Text = bodyText, TextWrapping = Avalonia.Media.TextWrapping.Wrap }
        }
    }
};
```

## Troubleshooting

1. Expecting full `FlowDocument` feature parity.
- define required document capabilities and choose a focused rendering strategy/library.

2. Large documents become slow.
- page or virtualize content and avoid building huge visual trees at once.

3. Reading and export paths diverge.
- keep one canonical document model shared by reader and export services.
