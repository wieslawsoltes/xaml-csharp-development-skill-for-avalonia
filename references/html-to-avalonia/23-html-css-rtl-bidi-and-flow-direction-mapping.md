# HTML/CSS RTL, BiDi, and `FlowDirection` Mapping to Avalonia

## Table of Contents
1. Scope and APIs
2. Direction and BiDi Mapping Table
3. Web Baseline (HTML/CSS)
4. Root and Subtree Direction Patterns
5. Layout Mirroring Patterns
6. Mixed RTL/LTR Content Patterns
7. Custom Text Rendering with Direction
8. C# Equivalent: RTL-Aware Shell
9. Troubleshooting

## Scope and APIs

Primary APIs:

- `FlowDirection` on `Visual` (`LeftToRight`, `RightToLeft`)
- `TextBlock.TextAlignment` (use logical alignment where possible)
- layout placement APIs (`Grid.SetColumn`, `Grid.SetRow`, spans) for explicit mirroring
- text rendering APIs: `TextLayout` and `FormattedText` flow-direction parameters

Reference docs:

- [`16-html-css-accessibility-semantics-and-motion-preference-mapping.md`](16-html-css-accessibility-semantics-and-motion-preference-mapping)
- [`19-focus-and-keyboard-navigation.md`](../19-focus-and-keyboard-navigation)
- [`59-media-colors-brushes-and-formatted-text-practical-usage.md`](../59-media-colors-brushes-and-formatted-text-practical-usage)

## Direction and BiDi Mapping Table

| Web idiom | Avalonia mapping |
|---|---|
| `<html dir="rtl">` or `direction: rtl` on app root | set root `FlowDirection="RightToLeft"` |
| `direction: ltr` on subtree | set subtree `FlowDirection="LeftToRight"` |
| `text-align: start` | `TextAlignment="Start"` |
| per-component `:dir(rtl)` styling | direction class (`rtl`/`ltr`) plus style selectors |
| custom canvas/text drawing with RTL | pass `FlowDirection.RightToLeft` to `TextLayout`/`FormattedText` |

## Web Baseline (HTML/CSS)

```html
<html dir="rtl">
  <body>
    <div class="shell">
      <aside class="nav">...</aside>
      <main class="content">
        <h1 class="start-aligned">طلبات اليوم</h1>
        <p dir="ltr" class="code">Order #A-1042</p>
      </main>
    </div>
  </body>
</html>
```

```css
:root[dir="rtl"] .shell {
  direction: rtl;
}

.start-aligned {
  text-align: start;
}

.rtl-only:dir(rtl) {
  padding-inline-start: 16px;
}
```

## Root and Subtree Direction Patterns

XAML root pattern:

```xaml
<Grid FlowDirection="{CompiledBinding AppFlowDirection}">
  <StackPanel Spacing="8">
    <TextBlock Text="{CompiledBinding PageTitle}" TextAlignment="Start" />
    <TextBlock Text="{CompiledBinding Subtitle}" TextAlignment="Start" />

    <!-- Force LTR for product codes/emails even in RTL pages -->
    <Border FlowDirection="LeftToRight" Padding="8">
      <TextBlock Text="{CompiledBinding ProductCode}" TextAlignment="Start" />
    </Border>
  </StackPanel>
</Grid>
```

C# direction source:

```csharp
using Avalonia.Media;

public FlowDirection AppFlowDirection { get; set; } = FlowDirection.RightToLeft;
```

## Layout Mirroring Patterns

For critical chrome regions (navigation rail, utility pane, primary content), mirror placement explicitly so behavior is deterministic across controls.

```csharp
using Avalonia.Controls;
using Avalonia.Media;

static void ApplyShellDirection(Grid shell, Control navRail, Control mainContent, FlowDirection flowDirection)
{
    shell.FlowDirection = flowDirection;

    var rtl = flowDirection == FlowDirection.RightToLeft;
    Grid.SetColumn(navRail, rtl ? 1 : 0);
    Grid.SetColumn(mainContent, rtl ? 0 : 1);
}
```

This is a practical equivalent of swapping CSS grid areas/tracks between LTR and RTL variants.

## Mixed RTL/LTR Content Patterns

Mixed scripts (Arabic/Hebrew + codes, SKUs, numbers) are usually best modeled as separate text runs/controls with local direction overrides.

```xaml
<StackPanel FlowDirection="RightToLeft" Spacing="4">
  <TextBlock Text="طلبات اليوم" TextAlignment="Start" />
  <TextBlock FlowDirection="LeftToRight"
             Text="Order #A-1042"
             TextAlignment="Start" />
</StackPanel>
```

## Custom Text Rendering with Direction

For custom drawing paths, always pass explicit direction to text layout objects.

```csharp
using Avalonia.Media;

var textLayout = new TextLayout(
    text: "طلبات اليوم",
    typeface: new Typeface("Segoe UI"),
    fontSize: 14,
    foreground: Brushes.Black,
    textAlignment: TextAlignment.Start,
    flowDirection: FlowDirection.RightToLeft,
    maxWidth: 360);
```

`FormattedText` supports the same explicit flow-direction input for lower-level draw scenarios.

## C# Equivalent: RTL-Aware Shell

```csharp
using Avalonia.Controls;
using Avalonia.Media;

var shell = new Grid
{
    ColumnDefinitions = ColumnDefinitions.Parse("220,*"),
    FlowDirection = FlowDirection.RightToLeft
};

var navRail = new Border
{
    Child = new TextBlock { Text = "Navigation" }
};

var mainContent = new StackPanel
{
    Spacing = 8,
    Children =
    {
        new TextBlock { Text = "طلبات اليوم", TextAlignment = TextAlignment.Start },
        new Border
        {
            FlowDirection = FlowDirection.LeftToRight,
            Child = new TextBlock { Text = "Order #A-1042", TextAlignment = TextAlignment.Start }
        }
    }
};

Grid.SetColumn(navRail, 1);
Grid.SetColumn(mainContent, 0);

shell.Children.Add(navRail);
shell.Children.Add(mainContent);
```

## Troubleshooting

1. Left/right keyboard focus behavior feels inverted.
- This is expected in RTL flows; validate directional navigation paths (`XYFocus`) in critical layouts.

2. Numbers or codes render in unexpected order inside RTL text.
- Isolate mixed-direction tokens into nested controls (or explicit text runs) with local `FlowDirection`.

3. Shell chrome mirrors partially.
- Mirror core region placement explicitly (for example with `Grid.SetColumn`) instead of relying on incidental defaults.
