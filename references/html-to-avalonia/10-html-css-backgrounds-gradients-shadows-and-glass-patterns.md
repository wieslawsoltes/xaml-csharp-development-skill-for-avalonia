# HTML/CSS Backgrounds, Gradients, Shadows, and Glass Patterns in Avalonia

## Table of Contents
1. Scope and APIs
2. Background and Gradient Mapping
3. Border Radius and Shadow Mapping
4. Glassmorphism-Like Surface Mapping
5. Layered Background Composition
6. Conversion Example: Glass Card
7. C# Equivalent: Glass Card
8. AOT/Performance Notes
9. Troubleshooting

## Scope and APIs

Primary APIs:

- `Border`, `Panel`, `Image`
- `SolidColorBrush`, `LinearGradientBrush`, `RadialGradientBrush`
- `BoxShadow`/`BoxShadows`
- `ExperimentalAcrylicBorder` for acrylic-like surfaces

Reference docs:

- [`59-media-colors-brushes-and-formatted-text-practical-usage.md`](../59-media-colors-brushes-and-formatted-text-practical-usage)
- [`28-custom-themes-xaml-and-code-only.md`](../28-custom-themes-xaml-and-code-only)

## Background and Gradient Mapping

| HTML/CSS | Avalonia |
|---|---|
| `background-color` | `Background` with `SolidColorBrush` |
| `background: linear-gradient(...)` | `LinearGradientBrush` |
| `background: radial-gradient(...)` | `RadialGradientBrush` |
| layered `background` values | stacked visuals/overlays with multiple borders/panels |

HTML/CSS:

```html
<section class="hero"></section>
```

```css
.hero {
  background: linear-gradient(120deg, #0f172a 0%, #1d4ed8 55%, #0ea5e9 100%);
}
```

Avalonia:

```xaml
<Border>
  <Border.Background>
    <LinearGradientBrush StartPoint="0,0" EndPoint="1,1">
      <GradientStop Offset="0" Color="#0F172A" />
      <GradientStop Offset="0.55" Color="#1D4ED8" />
      <GradientStop Offset="1" Color="#0EA5E9" />
    </LinearGradientBrush>
  </Border.Background>
</Border>
```

## Border Radius and Shadow Mapping

| HTML/CSS | Avalonia |
|---|---|
| `border-radius: 12px` | `CornerRadius="12"` |
| `box-shadow: 0 12px 24px rgba(...)` | `BoxShadow` |
| `border: 1px solid ...` | `BorderBrush` + `BorderThickness` |

HTML/CSS:

```html
<article class="card">...</article>
```

```css
.card {
  border-radius: 14px;
  border: 1px solid rgba(255,255,255,.12);
  box-shadow: 0 14px 36px rgba(0,0,0,.28);
}
```

Avalonia:

```xaml
<Border CornerRadius="14"
        BorderThickness="1"
        BorderBrush="#1FFFFFFF"
        BoxShadow="0 14 36 0 #47000000" />
```

## Glassmorphism-Like Surface Mapping

HTML/CSS:

```html
<section class="glass">...</section>
```

```css
.glass {
  background: rgba(255,255,255,.10);
  backdrop-filter: blur(18px);
  border: 1px solid rgba(255,255,255,.22);
}
```

Avalonia patterns:

1. translucent border + layered gradient (portable baseline),
2. `ExperimentalAcrylicBorder` where platform rendering supports desired effect.

```xaml
<experimental:ExperimentalAcrylicBorder
    xmlns:experimental="clr-namespace:Avalonia.Controls;assembly=Avalonia.Controls"
    xmlns:media="clr-namespace:Avalonia.Media;assembly=Avalonia.Base"
    CornerRadius="16"
    BorderBrush="#30FFFFFF"
    BorderThickness="1">
  <experimental:ExperimentalAcrylicBorder.Material>
    <media:ExperimentalAcrylicMaterial
        TintColor="#CC1E293B"
        TintOpacity="0.65"
        MaterialOpacity="0.35" />
  </experimental:ExperimentalAcrylicBorder.Material>
</experimental:ExperimentalAcrylicBorder>
```

## Layered Background Composition

HTML/CSS layered pattern:

```html
<section class="panel"></section>
```

```css
.panel {
  background:
    radial-gradient(circle at 20% 10%, rgba(56,189,248,.22), transparent 48%),
    linear-gradient(180deg, #111827, #0b1220);
}
```

Avalonia pattern:

```xaml
<Grid>
  <Border Background="#0B1220" />
  <Border>
    <Border.Background>
      <RadialGradientBrush Center="0.2,0.1" GradientOrigin="0.2,0.1" Radius="0.7">
        <GradientStop Offset="0" Color="#3838BDF8" />
        <GradientStop Offset="1" Color="#0038BDF8" />
      </RadialGradientBrush>
    </Border.Background>
  </Border>
</Grid>
```

## Conversion Example: Glass Card

```xaml
<Border Classes="glass-card" Padding="18" CornerRadius="16">
  <StackPanel Spacing="6">
    <TextBlock Text="Workspace" FontSize="14" Opacity="0.8" />
    <TextBlock Text="84 active users" FontSize="26" FontWeight="Bold" />
  </StackPanel>
</Border>

<Style Selector="Border.glass-card">
  <Setter Property="Background" Value="#1AFFFFFF" />
  <Setter Property="BorderBrush" Value="#30FFFFFF" />
  <Setter Property="BorderThickness" Value="1" />
  <Setter Property="BoxShadow" Value="0 16 40 0 #40000000" />
</Style>
```

## C# Equivalent: Glass Card

```csharp
using Avalonia;
using Avalonia.Controls;
using Avalonia.Media;

var glassCard = new Border
{
    CornerRadius = new CornerRadius(16),
    Padding = new Thickness(18),
    Background = new SolidColorBrush(Color.Parse("#1AFFFFFF")),
    BorderBrush = new SolidColorBrush(Color.Parse("#30FFFFFF")),
    BorderThickness = new Thickness(1),
    BoxShadow = BoxShadows.Parse("0 16 40 0 #40000000"),
    Child = new StackPanel
    {
        Spacing = 6,
        Children =
        {
            new TextBlock { Text = "Workspace", FontSize = 14, Opacity = 0.8 },
            new TextBlock { Text = "84 active users", FontSize = 26, FontWeight = FontWeight.Bold }
        }
    }
};

var acrylic = new ExperimentalAcrylicBorder
{
    CornerRadius = new CornerRadius(16),
    BorderBrush = new SolidColorBrush(Color.Parse("#30FFFFFF")),
    BorderThickness = new Thickness(1),
    Material = new ExperimentalAcrylicMaterial
    {
        TintColor = Color.Parse("#CC1E293B"),
        TintOpacity = 0.65,
        MaterialOpacity = 0.35
    }
};
```

## AOT/Performance Notes

- Prefer static brush resources for repeated surfaces.
- Reduce expensive blur/acrylic usage in large scrolling lists.

## Troubleshooting

1. Glass effect looks different across platforms.
- Use a fallback solid/gradient surface for non-acrylic environments.

2. Shadows look too heavy on low-DPI displays.
- Tune blur radius/opacity per theme density.

3. Gradient banding appears.
- Introduce subtle overlays/noise and avoid abrupt color stop jumps.
