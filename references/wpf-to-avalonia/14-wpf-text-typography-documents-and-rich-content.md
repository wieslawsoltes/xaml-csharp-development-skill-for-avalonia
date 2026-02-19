# WPF Text, Typography, Documents, and Rich Content to Avalonia

## Table of Contents
1. Scope and APIs
2. Text and Rich Content Mapping
3. Conversion Example
4. Avalonia C# Equivalent
5. Troubleshooting

## Scope and APIs

Primary WPF APIs:

- `TextBlock`, `TextBox`, typography properties
- `FlowDocument`/`RichTextBox`
- formatted text and inline elements

Primary Avalonia APIs:

- `TextBlock`, `TextBox`
- inline text runs in `TextBlock`
- `FormattedText`/`TextLayout` for advanced text rendering

## Text and Rich Content Mapping

| WPF | Avalonia |
|---|---|
| `TextBlock` + inline runs | same concept |
| `TextBox` editing behaviors | same concept with Avalonia input options |
| `FlowDocument`/`RichTextBox` | no direct core equivalent; use custom/third-party solutions |

## Conversion Example

WPF XAML:

```xaml
<TextBlock>
  <Run Text="Total: " />
  <Run Text="$420" FontWeight="Bold" />
</TextBlock>
```

Avalonia XAML:

```xaml
<TextBlock xmlns="https://github.com/avaloniaui"
           xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml">
  <Run Text="Total: " />
  <Run Text="$420" FontWeight="Bold" />
</TextBlock>
```

## Avalonia C# Equivalent

```csharp
using Avalonia.Controls;
using Avalonia.Documents;
using Avalonia.Media;

var text = new TextBlock();
text.Inlines.Add(new Run("Total: "));
text.Inlines.Add(new Run("$420") { FontWeight = FontWeight.Bold });
```

## Troubleshooting

1. expecting direct `FlowDocument` parity.
- move to template-driven rich views or integrate a specialized document component.

2. typography differs after port.
- align font family/weight/line-height and text rendering settings explicitly.

3. rich text editor functionality missing.
- plan a dedicated editor integration instead of forcing `TextBox` parity.
