# HTML/CSS Typography, Fonts, Text Flow, and Truncation in Avalonia

## Table of Contents
1. Scope and APIs
2. Typography Property Mapping
3. Text Flow and Wrapping Mapping
4. Truncation and Clamping Patterns
5. Rich Text Styling Comparison
6. Conversion Example: Marketing Hero Copy
7. C# Equivalent: Marketing Hero Copy
8. AOT/Performance Notes
9. Troubleshooting

## Scope and APIs

Primary APIs:

- `TextBlock`, `SelectableTextBlock`, `Run`, `Span`
- typography properties (`FontSize`, `FontWeight`, `FontStyle`, `LineHeight`, `LetterSpacing`)
- wrapping/trim (`TextWrapping`, `TextTrimming`, `MaxLines`)
- custom text rendering (`FormattedText`)

Reference docs:

- [`59-media-colors-brushes-and-formatted-text-practical-usage.md`](../59-media-colors-brushes-and-formatted-text-practical-usage)
- [`58-textbox-editing-clipboard-undo-and-input-options.md`](../58-textbox-editing-clipboard-undo-and-input-options)

## Typography Property Mapping

| HTML/CSS | Avalonia |
|---|---|
| `font-family` | `FontFamily` |
| `font-size` | `FontSize` |
| `font-weight` | `FontWeight` |
| `font-style` | `FontStyle` |
| `line-height` | `LineHeight` |
| `letter-spacing` | `LetterSpacing` |
| `text-align` | `TextAlignment` |

HTML/CSS:

```html
<h1 class="headline">Ship Faster UI</h1>
```

```css
.headline {
  font-family: "Inter", sans-serif;
  font-size: clamp(2rem, 4vw, 3.25rem);
  font-weight: 800;
  letter-spacing: -0.02em;
  line-height: 1.1;
}
```

Avalonia:

```xaml
<TextBlock Classes="headline" Text="Ship Faster UI" />

<Style Selector="TextBlock.headline">
  <Setter Property="FontFamily" Value="Inter" />
  <Setter Property="FontSize" Value="48" />
  <Setter Property="FontWeight" Value="ExtraBold" />
  <Setter Property="LetterSpacing" Value="-0.6" />
  <Setter Property="LineHeight" Value="52" />
</Style>
```

## Text Flow and Wrapping Mapping

| HTML/CSS | Avalonia |
|---|---|
| `white-space: normal` | `TextWrapping="Wrap"` |
| `white-space: nowrap` | `TextWrapping="NoWrap"` |
| `word-break`/`overflow-wrap` | `TextWrapping` strategy + width constraints |
| `text-align: center/right` | `TextAlignment` |

HTML/CSS:

```css
.summary {
  max-width: 56ch;
  white-space: normal;
}
```

Avalonia:

```xaml
<TextBlock Classes="summary"
           MaxWidth="640"
           TextWrapping="Wrap"
           Text="{CompiledBinding Summary}" />
```

## Truncation and Clamping Patterns

HTML/CSS single-line ellipsis:

```css
.title {
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
```

Avalonia:

```xaml
<TextBlock Text="{CompiledBinding Title}"
           TextWrapping="NoWrap"
           TextTrimming="CharacterEllipsis" />
```

HTML/CSS multiline clamp:

```css
.excerpt {
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
```

Avalonia:

```xaml
<TextBlock Text="{CompiledBinding Excerpt}"
           TextWrapping="Wrap"
           MaxLines="3"
           TextTrimming="CharacterEllipsis" />
```

## Rich Text Styling Comparison

HTML:

```html
<p>Deploy to <strong>production</strong> with <em>confidence</em>.</p>
```

Avalonia:

```xaml
<TextBlock>
  <Run Text="Deploy to " />
  <Run Text="production" FontWeight="Bold" />
  <Run Text=" with " />
  <Run Text="confidence" FontStyle="Italic" />
  <Run Text="." />
</TextBlock>
```

## Conversion Example: Marketing Hero Copy

HTML/CSS:

```html
<section class="hero-copy">
  <h1>Design and ship native UI</h1>
  <p>Use one codebase for desktop, mobile, and web targets.</p>
</section>
```

```css
.hero-copy h1 { font-size: 3rem; margin-bottom: .5rem; }
.hero-copy p { font-size: 1.125rem; color: #9aa6bd; max-width: 52ch; }
```

Avalonia:

```xaml
<StackPanel Classes="hero-copy" Spacing="8">
  <TextBlock Classes="hero-title" Text="Design and ship native UI" />
  <TextBlock Classes="hero-subtitle"
             Text="Use one codebase for desktop, mobile, and web targets."
             TextWrapping="Wrap"
             MaxWidth="700" />
</StackPanel>
```

## C# Equivalent: Marketing Hero Copy

```csharp
using Avalonia.Controls;
using Avalonia.Media;

var hero = new StackPanel { Spacing = 8 };

hero.Children.Add(new TextBlock
{
    Text = "Design and ship native UI",
    FontSize = 48,
    FontWeight = FontWeight.ExtraBold,
    LineHeight = 52
});

hero.Children.Add(new TextBlock
{
    Text = "Use one codebase for desktop, mobile, and web targets.",
    TextWrapping = TextWrapping.Wrap,
    MaxWidth = 700,
    Foreground = new SolidColorBrush(Color.Parse("#9AA6BD"))
});
```

## AOT/Performance Notes

- Prefer declarative text styles in XAML resources.
- For high-frequency custom drawing, cache `FormattedText` objects.

## Troubleshooting

1. Text metrics differ from browser screenshots.
- Validate installed fonts and fallback families on each target OS.

2. Ellipsis does not appear.
- Ensure width/max lines constraints are actually limiting layout.

3. Wrapped text overflows container.
- Check parent width constraints and `HorizontalAlignment` settings.
