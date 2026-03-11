# Typography, Iconography, and Content Hierarchy in Avalonia

## Table of Contents
1. Scope and Primary APIs
2. Type Roles
3. Font Strategy
4. Icon Strategy
5. Content Hierarchy Rules
6. AOT and Performance Notes
7. Do and Don't Guidance
8. Troubleshooting
9. Official Resources

## Scope and Primary APIs

Use this reference to establish readable hierarchy and polished content rhythm.

Primary APIs:
- `TextBlock`, `SelectableTextBlock`
- `TextElement.FontFamily`, `FontWeight`, `FontStyle`
- `TextBlock.TextWrapping`, `TextBlock.TextTrimming`, `TextBlock.TextAlignment`
- `AppBuilder.ConfigureFonts(...)`, `WithInterFont()`
- `PathIcon`
- `AutomationProperties.Name`

## Type Roles

Use a small role system:
- eyebrow or caption,
- title,
- body,
- muted or metadata,
- numeric or KPI emphasis when needed.

Example:

```xml
<Styles xmlns="https://github.com/avaloniaui"
        xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml">
  <Style Selector="TextBlock.eyebrow">
    <Setter Property="FontSize" Value="12" />
    <Setter Property="FontWeight" Value="SemiBold" />
    <Setter Property="Foreground" Value="{DynamicResource Brush.Text.Secondary}" />
  </Style>
  <Style Selector="TextBlock.title">
    <Setter Property="FontSize" Value="22" />
    <Setter Property="FontWeight" Value="SemiBold" />
    <Setter Property="Foreground" Value="{DynamicResource Brush.Text.Primary}" />
  </Style>
  <Style Selector="TextBlock.body">
    <Setter Property="FontSize" Value="14" />
    <Setter Property="TextWrapping" Value="Wrap" />
    <Setter Property="Foreground" Value="{DynamicResource Brush.Text.Primary}" />
  </Style>
  <Style Selector="TextBlock.meta">
    <Setter Property="FontSize" Value="12" />
    <Setter Property="TextTrimming" Value="CharacterEllipsis" />
    <Setter Property="Foreground" Value="{DynamicResource Brush.Text.Secondary}" />
  </Style>
</Styles>
```

## Font Strategy

Cross-platform defaults:
- use native platform fonts when platform familiarity matters,
- use `WithInterFont()` or custom font setup when a product-wide consistent tone matters,
- keep the font stack small.

```csharp
public static AppBuilder BuildAvaloniaApp() =>
    AppBuilder.Configure<App>()
        .UsePlatformDetect()
        .WithInterFont();
```

## Icon Strategy

Use `PathIcon` for vector icons that should inherit text color and scale predictably.

```xml
<StackPanel xmlns="https://github.com/avaloniaui"
            xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
            Orientation="Horizontal"
            Spacing="8">
  <PathIcon Data="{StaticResource Icon.Search}" />
  <TextBlock Classes="body" Text="Search incidents" />
</StackPanel>
```

Guidance:
- keep system icons single-color in most app UI,
- do not use tiny icons as primary interaction targets,
- pair icons with labels for critical actions.

## Content Hierarchy Rules

- use sentence case for most UI copy,
- keep support copy short and direct,
- let spacing create groups before adding separators,
- reserve stronger color or weight for one focal item per region.

## AOT and Performance Notes

- Prefer compiled XAML styles and icon geometry resources.
- Keep icon geometry dictionaries shared rather than duplicated per view.

## Do and Don't Guidance

Do:
- keep the type ramp small,
- ensure large text and metadata both have defined roles,
- use icons semantically.

Do not:
- use all caps for hierarchy,
- mix many unrelated font weights or families,
- rely on color alone to distinguish critical text.

## Troubleshooting

1. Text hierarchy feels muddy.
- Reduce the number of roles and increase spacing contrast between groups.

2. Secondary text dominates.
- Lower contrast or weight for metadata instead of shrinking everything.

3. Icons feel inconsistent.
- Standardize geometry source, icon size, and foreground treatment.

## Official Resources

- Avalonia fonts: [docs.avaloniaui.net/docs/guides/styles-and-resources/how-to-use-fonts](https://docs.avaloniaui.net/docs/guides/styles-and-resources/how-to-use-fonts)
- Avalonia PathIcon: [docs.avaloniaui.net/docs/reference/controls/path-icon](https://docs.avaloniaui.net/docs/reference/controls/path-icon)
- Fluent 2 typography: [fluent2.microsoft.design/typography](https://fluent2.microsoft.design/typography)
- Fluent 2 iconography: [fluent2.microsoft.design/iconography](https://fluent2.microsoft.design/iconography)
