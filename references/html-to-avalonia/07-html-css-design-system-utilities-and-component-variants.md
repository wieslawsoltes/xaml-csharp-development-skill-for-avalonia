# HTML/CSS Design System Utilities and Component Variants in Avalonia

## Table of Contents
1. Scope and APIs
2. Utility-Class Migration Strategy
3. BEM/Component-Class Migration Strategy
4. Token System Migration
5. Variant + State Architecture
6. HTML Utility CSS Comparison
7. Example: Utility-to-Theme Refactor
8. C# Equivalent: Utility-to-Theme Refactor
9. AOT/Packaging Notes
10. Troubleshooting

## Scope and APIs

Primary APIs:

- style system: `Styles`, `Style`, `ControlTheme`, `Setter`
- selectors: `Selectors.*`
- resources/tokens: `ResourceDictionary`, `ThemeDictionaries`, `DynamicResource`
- library packaging: `StyleInclude`, `ResourceInclude`, merged dictionaries

Reference docs:

- [`04-styles-themes-resources.md`](../04-styles-themes-resources)
- [`28-custom-themes-xaml-and-code-only.md`](../28-custom-themes-xaml-and-code-only)
- [`43-xaml-in-libraries-and-resource-packaging.md`](../43-xaml-in-libraries-and-resource-packaging)
- [`49-adaptive-markup-and-dynamic-resource-patterns.md`](../49-adaptive-markup-and-dynamic-resource-patterns)

## Utility-Class Migration Strategy

Web utility-first systems usually become Avalonia class packs:

- spacing: `u-p-2`, `u-p-4`, `u-gap-2`
- typography: `u-text-sm`, `u-text-lg`, `u-font-semibold`
- surfaces: `u-bg-surface`, `u-border-muted`

```xaml
<Style Selector="*.u-p-4">
  <Setter Property="Padding" Value="16" />
</Style>
<Style Selector="StackPanel.u-gap-2">
  <Setter Property="Spacing" Value="8" />
</Style>
```

Use utility classes sparingly for layout glue; prefer component classes/themes for durable UI systems.

## BEM/Component-Class Migration Strategy

| Web BEM idiom | Avalonia idiom |
|---|---|
| `.card`, `.card__title`, `.card--warning` | control classes (`card`, `card-title`, `warning`) + local styles |
| variant modifiers | separate class selectors or `ControlTheme` based variants |

## Token System Migration

Create explicit tokens and keep controls consuming tokens, not literals:

- color tokens: `Color` + `SolidColorBrush`
- spacing tokens: numeric resources
- radius/shadow tokens: style resources
- typography tokens: font size/weight resources

```xaml
<Application.Resources>
  <x:Double x:Key="Space.3">12</x:Double>
  <x:Double x:Key="Radius.M">10</x:Double>
  <SolidColorBrush x:Key="Brush.Surface" Color="#10151E" />
</Application.Resources>
```

## Variant + State Architecture

Recommended layering:

1. base control theme
2. semantic variants (`primary`, `danger`, `success`)
3. interaction states (`:pointerover`, `:pressed`, `:disabled`)
4. responsive/state classes at root scope

## HTML Utility CSS Comparison

HTML/CSS utility-heavy markup:

```html
<button class="px-4 py-2 rounded-md bg-blue-600 text-white" disabled>
  Save
</button>
```

```css
.px-4 { padding-inline: 1rem; }
.py-2 { padding-block: .5rem; }
.rounded-md { border-radius: .375rem; }
.bg-blue-600 { background: #2563eb; }
.text-white { color: #fff; }
.bg-blue-600:hover { background: #3b82f6; }
button:disabled { opacity: .5; }
```

Equivalent Avalonia class strategy:

```xaml
<Button Classes="u-px-4 u-py-2 u-rounded-m u-bg-primary u-fg-on-primary"
        Content="Save" />

<Style Selector="Button.u-bg-primary:pointerover">
  <Setter Property="Background" Value="{DynamicResource Brush.PrimaryHover}" />
</Style>
<Style Selector="Button.u-bg-primary:disabled">
  <Setter Property="Opacity" Value="0.5" />
</Style>
```

Migration recommendation:

1. keep utilities for spacing/layout primitives,
2. move semantic states and tokens into component classes/themes,
3. avoid very long class strings for reusable controls.

## Example: Utility-to-Theme Refactor

Start (utility-heavy):

```xaml
<Button Classes="u-p-3 u-rounded-m u-bg-primary u-text-on-primary" Content="Save" />
```

Refactor target (theme-centric):

```xaml
<Button Classes="btn primary" Content="Save" />
```

```xaml
<Style Selector="Button.btn">
  <Setter Property="Padding" Value="14,9" />
  <Setter Property="CornerRadius" Value="{StaticResource Radius.M}" />
</Style>
<Style Selector="Button.btn.primary">
  <Setter Property="Background" Value="{DynamicResource Brush.Primary}" />
  <Setter Property="Foreground" Value="{DynamicResource Brush.OnPrimary}" />
</Style>
```

## C# Equivalent: Utility-to-Theme Refactor

```csharp
using Avalonia;
using Avalonia.Controls;
using Avalonia.Media;
using Avalonia.Styling;

application.Resources["Radius.M"] = new CornerRadius(10);
application.Resources["Brush.Primary"] = new SolidColorBrush(Color.Parse("#2F6FED"));
application.Resources["Brush.OnPrimary"] = Brushes.White;

var baseButton = new Style(x => x.OfType<Button>().Class("btn"))
{
    Setters =
    {
        new Setter(TemplatedControl.PaddingProperty, new Thickness(14, 9)),
        new Setter(TemplatedControl.CornerRadiusProperty, application.Resources["Radius.M"])
    }
};

var primaryButton = new Style(x => x.OfType<Button>().Class("btn").Class("primary"))
{
    Setters =
    {
        new Setter(TemplatedControl.BackgroundProperty, application.Resources["Brush.Primary"]),
        new Setter(TemplatedControl.ForegroundProperty, application.Resources["Brush.OnPrimary"])
    }
};

application.Styles.Add(baseButton);
application.Styles.Add(primaryButton);
```

## AOT/Packaging Notes

- Keep token/style dictionaries in compiled XAML assets.
- For reusable design systems, package styles in library resources and include via `StyleInclude`/`ResourceInclude`.
- Avoid runtime string-based style generation for stable shared components.

## Troubleshooting

1. Utility classes become unmaintainable.
- Consolidate repeated class bundles into component classes/themes.

2. Variant rules conflict.
- Define clear style ordering and keep selector depth low.

3. Theme package works in one app but not another.
- Verify merged dictionary order and resource-key consistency.
