# HTML/CSS Logical Properties to Avalonia Flow-Aware Spacing and Alignment

## Table of Contents
1. Scope and APIs
2. Logical Property Support Model
3. Mapping Table (Inline/Block to Avalonia)
4. Flow-Aware Thickness and Corner Helpers
5. Conversion Example: Logical Card Spacing
6. C# Equivalent: Logical Card Spacing
7. Practical Do/Don't Guidance
8. Troubleshooting

## Scope and APIs

Primary APIs:

- `FlowDirection` (`LeftToRight`, `RightToLeft`)
- spacing/sizing properties: `Margin`, `Padding`, `BorderThickness`, `CornerRadius`, `Width`, `Height`, `MinWidth`, `MinHeight`
- positioning properties: `Canvas.Left`, `Canvas.Right`, `Canvas.Top`, `Canvas.Bottom`
- text alignment baseline: `TextBlock.TextAlignment`

Reference docs:

- [`00-html-css-layout-box-model-and-positioning.md`](00-html-css-layout-box-model-and-positioning)
- [`01-html-css-flexbox-grid-and-responsive-layout-recipes.md`](01-html-css-flexbox-grid-and-responsive-layout-recipes)
- [`16-html-css-accessibility-semantics-and-motion-preference-mapping.md`](16-html-css-accessibility-semantics-and-motion-preference-mapping)

## Logical Property Support Model

CSS logical properties (`margin-inline-start`, `padding-block-end`, `inset-inline-start`, `inline-size`, etc.) are direction-aware by design.

Avalonia does not expose separate built-in logical thickness properties. The practical mapping is:

1. keep one `FlowDirection` source of truth (`LeftToRight` or `RightToLeft`),
2. compute physical `Thickness`/position values from logical inputs,
3. bind computed values into XAML properties.

For application UI migration, this is the most predictable equivalent of web logical spacing.

## Mapping Table (Inline/Block to Avalonia)

| CSS logical idiom | Avalonia mapping |
|---|---|
| `margin-inline-start` / `margin-inline-end` | map to `Margin.Left`/`Margin.Right` based on `FlowDirection` |
| `margin-block-start` / `margin-block-end` | map to `Margin.Top`/`Margin.Bottom` |
| `padding-inline-*` / `padding-block-*` | map to `Padding` `Thickness` values |
| `border-inline-start-width` / `border-inline-end-width` | map to `BorderThickness.Left`/`BorderThickness.Right` by flow |
| `inset-inline-start` / `inset-inline-end` | map to `Canvas.Left`/`Canvas.Right` by flow |
| `inset-block-start` / `inset-block-end` | map to `Canvas.Top`/`Canvas.Bottom` |
| `inline-size` / `min-inline-size` | `Width` / `MinWidth` (horizontal writing mode apps) |
| `block-size` / `min-block-size` | `Height` / `MinHeight` (horizontal writing mode apps) |
| `text-align: start` | `TextAlignment="Start"` with appropriate `FlowDirection` |

Notes:

- `writing-mode`-driven vertical inline/block axes are not a direct 1:1 Avalonia layout feature.
- for app UIs, horizontal writing mode plus `FlowDirection` is the practical migration target.

## Flow-Aware Thickness and Corner Helpers

```csharp
using Avalonia;
using Avalonia.Media;

public static class LogicalLayout
{
    public static Thickness Thickness(
        double inlineStart,
        double blockStart,
        double inlineEnd,
        double blockEnd,
        FlowDirection flowDirection)
    {
        return flowDirection == FlowDirection.RightToLeft
            ? new Thickness(inlineEnd, blockStart, inlineStart, blockEnd)
            : new Thickness(inlineStart, blockStart, inlineEnd, blockEnd);
    }

    public static CornerRadius Corner(
        double startStart,
        double startEnd,
        double endEnd,
        double endStart,
        FlowDirection flowDirection)
    {
        // Avalonia corner order: TopLeft, TopRight, BottomRight, BottomLeft
        return flowDirection == FlowDirection.RightToLeft
            ? new CornerRadius(startEnd, startStart, endStart, endEnd)
            : new CornerRadius(startStart, startEnd, endEnd, endStart);
    }
}
```

## Conversion Example: Logical Card Spacing

HTML/CSS:

```html
<article class="card">
  <h3 class="title">Revenue</h3>
</article>
```

```css
.card {
  margin-inline: 24px 12px;
  padding-inline: 20px 28px;
  padding-block: 12px 16px;
  border-inline-start-width: 6px;
  border-inline-end-width: 2px;
}
```

Avalonia pattern (computed once per direction and bound):

```xaml
<Border Classes="metric-card"
        Margin="{CompiledBinding CardMargin}"
        Padding="{CompiledBinding CardPadding}"
        BorderThickness="{CompiledBinding CardBorderThickness}"
        CornerRadius="{CompiledBinding CardCornerRadius}">
  <TextBlock Text="{CompiledBinding Title}" TextAlignment="Start" />
</Border>
```

## C# Equivalent: Logical Card Spacing

```csharp
using Avalonia;
using Avalonia.Media;

public FlowDirection CurrentFlowDirection { get; set; } = FlowDirection.LeftToRight;

public Thickness CardMargin =>
    LogicalLayout.Thickness(inlineStart: 24, blockStart: 0, inlineEnd: 12, blockEnd: 0, CurrentFlowDirection);

public Thickness CardPadding =>
    LogicalLayout.Thickness(inlineStart: 20, blockStart: 12, inlineEnd: 28, blockEnd: 16, CurrentFlowDirection);

public Thickness CardBorderThickness =>
    LogicalLayout.Thickness(inlineStart: 6, blockStart: 1, inlineEnd: 2, blockEnd: 1, CurrentFlowDirection);

public CornerRadius CardCornerRadius =>
    LogicalLayout.Corner(startStart: 14, startEnd: 6, endEnd: 14, endStart: 6, CurrentFlowDirection);
```

## Practical Do/Don't Guidance

- Do keep logical values in one place (view model/service) and derive `Thickness`/`CornerRadius`.
- Do apply `FlowDirection` at root or feature-scope containers, not ad-hoc per control.
- Do prefer grid/stack layouts over absolute positioning for flow-sensitive UIs.
- Don't hardcode both LTR and RTL physical margins throughout XAML.
- Don't assume inline/block axis rotation for vertical writing-mode migration; validate target UX explicitly.

## Troubleshooting

1. RTL UI still shows LTR spacing.
- Confirm the active container `FlowDirection` and recompute bound logical thickness properties.

2. Borders/radii mirror incorrectly on RTL.
- Centralize mapping helpers and verify corner order (`TopLeft`, `TopRight`, `BottomRight`, `BottomLeft`).

3. Inline start/end positioned elements overlap.
- For absolute layouts, map logical inset to `Canvas.Left`/`Canvas.Right` using one direction-aware function.
