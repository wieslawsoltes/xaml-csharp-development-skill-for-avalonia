# Color, Surfaces, Elevation, and Material Depth in Avalonia

## Table of Contents
1. Scope and Primary APIs
2. Surface Strategy
3. Elevation Rules
4. Material Guidance
5. AOT and Performance Notes
6. Do and Don't Guidance
7. Troubleshooting
8. Official Resources

## Scope and Primary APIs

Use this reference for polished surface treatment and depth decisions.

Primary APIs:
- `Color`, `SolidColorBrush`, gradient brushes
- `Border.Background`, `Border.BorderBrush`, `Border.BorderThickness`
- `Border.CornerRadius`, `Border.BoxShadow`
- `BoxShadows`
- `ExperimentalAcrylicBorder`, `ExperimentalAcrylicMaterial`

## Surface Strategy

Use semantic roles:
- app background,
- card surface,
- subtle surface,
- border,
- emphasis or accent,
- danger and success semantics.

Card example:

```xml
<Border xmlns="https://github.com/avaloniaui"
        xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
        Classes="metric-card"
        Padding="16">
  <StackPanel Spacing="8">
    <TextBlock Classes="eyebrow" Text="Revenue" />
    <TextBlock Classes="title" Text="$420,000" />
  </StackPanel>
</Border>
```

```xml
<Style Selector="Border.metric-card">
  <Setter Property="Background" Value="{DynamicResource Brush.Surface.Card}" />
  <Setter Property="BorderBrush" Value="{DynamicResource Brush.Border.Subtle}" />
  <Setter Property="BorderThickness" Value="1" />
  <Setter Property="CornerRadius" Value="12" />
  <Setter Property="BoxShadow" Value="0 8 24 0 #18000000" />
</Style>
```

## Elevation Rules

- Use more border contrast and less shadow in dense productivity UI.
- Increase shadow only for floating or transient surfaces.
- Keep one elevation scale across cards, flyouts, dialogs, and teaching surfaces.

## Material Guidance

Use acrylic sparingly and only where a translucent surface adds context.

```xml
<ExperimentalAcrylicBorder xmlns="https://github.com/avaloniaui"
                           xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
                           CornerRadius="12">
  <ExperimentalAcrylicBorder.Material>
    <ExperimentalAcrylicMaterial TintColor="#FF20242B"
                                 TintOpacity="0.8"
                                 MaterialOpacity="0.45"
                                 FallbackColor="#CC20242B" />
  </ExperimentalAcrylicBorder.Material>
  <Border Padding="16">
    <TextBlock Text="Use acrylic for accent surfaces, not every surface." />
  </Border>
</ExperimentalAcrylicBorder>
```

## AOT and Performance Notes

- Prefer static brush resources over building many brushes in code-behind.
- Limit acrylic and complex gradients on large, frequently changing surfaces.
- Avoid high-shadow counts in virtualized lists.

## Do and Don't Guidance

Do:
- use semantic brush names,
- keep the surface palette calm,
- let borders help define layers.

Do not:
- stack heavy shadows on every card,
- depend on transparency for readability,
- mix many unrelated corner-radius systems.

## Troubleshooting

1. Surfaces feel noisy.
- Reduce shadow depth, simplify border colors, and narrow the accent palette.

2. Dark theme feels muddy.
- Increase edge contrast and reduce translucent layering.

3. Acrylic becomes unreadable.
- Strengthen fallback color and keep text on stable inner surfaces.

## Official Resources

- Fluent 2 color: [fluent2.microsoft.design/styles/color](https://fluent2.microsoft.design/styles/color/)
- Fluent 2 elevation: [fluent2.microsoft.design/elevation](https://fluent2.microsoft.design/elevation)
- Fluent 2 material: [fluent2.microsoft.design/material](https://fluent2.microsoft.design/material)
