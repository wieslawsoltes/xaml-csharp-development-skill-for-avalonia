# Media Colors, Brushes, and FormattedText Practical Usage

## Table of Contents
1. Scope and APIs
2. `Colors` vs `Brushes`
3. XAML Color/Brush Patterns
4. `FormattedText` Construction and Metrics
5. Range-Level Formatting APIs
6. Drawing and Geometry Usage
7. Best Practices
8. Troubleshooting

## Scope and APIs

Primary APIs:
- `Avalonia.Media.Colors`
- `Avalonia.Media.Brushes`
- `Color`
- `IBrush` / `IImmutableSolidColorBrush`
- `FormattedText`
- `DrawingContext.DrawText(FormattedText, Point)`

Important `FormattedText` members:
- constructor: `FormattedText(string, CultureInfo, FlowDirection, Typeface, double, IBrush?)`
- paragraph settings: `FlowDirection`, `TextAlignment`, `LineHeight`
- layout limits: `MaxTextWidth`, `SetMaxTextWidths(double[])`, `MaxTextHeight`, `MaxLineCount`, `Trimming`
- metrics: `Width`, `WidthIncludingTrailingWhitespace`, `Height`, `Extent`, `Baseline`, `OverhangLeading`, `OverhangTrailing`, `OverhangAfter`
- styling mutators:
  - `SetForegroundBrush(...)`
  - `SetFontFamily(...)`
  - `SetFontSize(...)`
  - `SetFontWeight(...)`
  - `SetFontStyle(...)`
  - `SetFontTypeface(...)`
  - `SetTextDecorations(...)`
  - `SetCulture(...)`
  - `SetFontFeatures(...)`
- geometry output:
  - `BuildGeometry(Point)`
  - `BuildHighlightGeometry(Point)`
  - `BuildHighlightGeometry(Point, int, int)`

Reference source files:
- `src/Avalonia.Base/Media/Colors.cs`
- `src/Avalonia.Base/Media/Brushes.cs`
- `src/Avalonia.Base/Media/FormattedText.cs`
- `src/Avalonia.Base/Media/DrawingContext.cs`

## `Colors` vs `Brushes`

- `Colors` gives static `Color` values.
- `Brushes` gives reusable immutable solid brushes (`IImmutableSolidColorBrush`).

Use `Colors` when you need color math/conversion and `Brushes` when you need draw/fill/stroke instances.

```csharp
using Avalonia.Media;

Color accent = Colors.CornflowerBlue;
IBrush textBrush = Brushes.White;
```

## XAML Color/Brush Patterns

```xml
<Border xmlns="https://github.com/avaloniaui"
        xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
        Background="{DynamicResource AccentBrush}"
        BorderBrush="{StaticResource CardBorderBrush}"
        BorderThickness="1"
        Padding="12">
  <Border.Resources>
    <SolidColorBrush x:Key="AccentBrush" Color="CornflowerBlue" />
    <SolidColorBrush x:Key="CardBorderBrush" Color="#335A6A7A" />
  </Border.Resources>

  <TextBlock Foreground="White" Text="Brush resource usage" />
</Border>
```

Use resource keys for theme substitution instead of hardcoding many literal colors in controls.

## `FormattedText` Construction and Metrics

```csharp
using System.Globalization;
using Avalonia;
using Avalonia.Media;

FormattedText BuildTitle(string text)
{
    var ft = new FormattedText(
        text,
        CultureInfo.CurrentUICulture,
        FlowDirection.LeftToRight,
        new Typeface("Inter"),
        18,
        Brushes.White);

    ft.TextAlignment = TextAlignment.Left;
    ft.MaxTextWidth = 420;
    ft.Trimming = TextTrimming.CharacterEllipsis;

    return ft;
}
```

Use metrics (`Width`, `Height`, `Baseline`) to align custom drawing with surrounding primitives.

## Range-Level Formatting APIs

`FormattedText` supports per-range updates without rebuilding the object.

```csharp
using Avalonia.Media;

void EmphasizePrefix(FormattedText ft)
{
    ft.SetFontWeight(FontWeight.Bold, 0, 4);
    ft.SetForegroundBrush(Brushes.Gold, 0, 4);
    ft.SetTextDecorations(TextDecorations.Underline, 0, 4);
}
```

This is useful for compact custom-rendered labels where full text controls are unnecessary.

## Drawing and Geometry Usage

In custom controls:

```csharp
using System.Globalization;
using Avalonia;
using Avalonia.Controls;
using Avalonia.Media;

public class BadgeControl : Control
{
    public override void Render(DrawingContext context)
    {
        base.Render(context);

        var ft = new FormattedText(
            "LIVE",
            CultureInfo.CurrentUICulture,
            FlowDirection.LeftToRight,
            new Typeface("Inter"),
            12,
            Brushes.White)
        {
            MaxTextWidth = Bounds.Width,
            TextAlignment = TextAlignment.Center
        };

        context.DrawRectangle(Brushes.Crimson, null, Bounds);
        context.DrawText(ft, new Point(0, (Bounds.Height - ft.Height) / 2));
    }
}
```

Geometry extraction pattern:

```csharp
using Avalonia;
using Avalonia.Media;

Geometry? BuildTextOutline(FormattedText ft)
{
    return ft.BuildGeometry(new Point(0, 0));
}
```

`BuildHighlightGeometry` is useful for custom text-selection visualization.

## Best Practices

- Use `Brushes.*` for shared immutable solid brushes in code paths.
- Avoid constructing many transient `FormattedText` instances in tight frame loops.
- Set `MaxTextWidth`/`MaxTextHeight` before measuring when trimming behavior matters.
- Keep font family availability platform-aware; provide fallback families.
- Prefer resource-driven brush authoring in XAML for themeability.

## Troubleshooting

1. Text clips unexpectedly.
- Check `MaxTextWidth`, `MaxTextHeight`, and `MaxLineCount` interactions.

2. Trimming does not appear.
- Ensure width/height constraints are actually limiting layout and `Trimming` is not `None`.

3. Geometry from text is empty.
- Confirm text length is non-zero and rendering metrics were initialized.

4. Performance degrades in custom render loop.
- Cache `FormattedText` and rebuild only when text/style inputs change.

5. Color values appear correct but fill is wrong.
- Verify brush assignment and alpha channel values (`#AARRGGBB` semantics).
