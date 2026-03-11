# Motion, Focus, Accessibility, and Design Review in Avalonia

## Scope and Primary APIs

Use this reference to finish interaction polish without harming usability.

Primary APIs:
- `Transitions`
- `BrushTransition`, `DoubleTransition`, `BoxShadowsTransition`, `TransformOperationsTransition`
- pseudo-classes such as `:pointerover`, `:focus-visible`, `:disabled`
- `AutomationProperties`

High-value state helpers:
- `Classes`
- `Classes.Contains(...)`
- `PseudoClassesExtensions.Set(...)`
- `Animatable.Transitions`

## Motion Pattern

```xml
<Border xmlns="https://github.com/avaloniaui"
        xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
        Classes="interactive-card"
        RenderTransform="translateY(0px)">
  <Border.Transitions>
    <Transitions>
      <TransformOperationsTransition Property="RenderTransform" Duration="0:0:0.16" />
      <BoxShadowsTransition Property="BoxShadow" Duration="0:0:0.16" />
    </Transitions>
  </Border.Transitions>
</Border>
```

```xml
<Style Selector="Border.interactive-card:pointerover">
  <Setter Property="RenderTransform" Value="translateY(-2px)" />
</Style>
<Style Selector="Border.interactive-card:focus-visible">
  <Setter Property="BorderBrush" Value="{DynamicResource Brush.Focus}" />
  <Setter Property="BorderThickness" Value="2" />
</Style>
```

## Accessibility Rules

- Keep focus states stronger than hover states.
- Preserve contrast in both light and dark themes.
- Use `AutomationProperties.Name` and labels for icon-only commands.
- Offer reduced-motion paths or minimal-motion variants for repetitive surfaces.

## Design Review Checklist

- Is the most important item obvious within two seconds?
- Are spacing and radius rules consistent across pages and overlays?
- Do loading, empty, and error states feel like part of the same product?
- Can keyboard users see focus clearly everywhere?
- Does the UI still read well in light, dark, and compact modes?

## AOT and Performance Notes

- Prefer transitions over heavy custom animation for simple state changes.
- Do not animate large data regions or layout churn without clear benefit.

## Do and Don't Guidance

Do:
- keep durations short,
- constrain motion to the element in focus,
- use automation metadata for critical surfaces.

Do not:
- animate every state change,
- let focus visuals disappear under hover styling,
- communicate status only by motion or color.

## Troubleshooting

1. Motion feels distracting.
- Reduce distance, duration, and the number of moving properties.

2. Focus is hard to see.
- Increase border or outline contrast and ensure `:focus-visible` wins precedence.

3. Screen-reader behavior is unclear on compact UIs.
- Audit labels, names, and action text rather than relying on iconography alone.

## Official Resources

- Avalonia transitions: [docs.avaloniaui.net/docs/guides/graphics-and-animation/transitions](https://docs.avaloniaui.net/docs/guides/graphics-and-animation/transitions)
- Avalonia pseudoclasses: [docs.avaloniaui.net/docs/reference/styles/pseudo-classes](https://docs.avaloniaui.net/docs/reference/styles/pseudo-classes)
- Fluent 2 motion: [fluent2.microsoft.design/styles/motion](https://fluent2.microsoft.design/styles/motion/)
- Fluent 2 accessibility: [fluent2.microsoft.design/accessibility](https://fluent2.microsoft.design/accessibility)
