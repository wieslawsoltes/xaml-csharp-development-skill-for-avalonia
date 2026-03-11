# Globalization, Localization, BiDi, and Inclusive Design in Avalonia

## Table of Contents
1. Scope and Primary APIs
2. Localization-Safe Design Rules
3. BiDi and `FlowDirection` Patterns
4. Inclusive Design Rules
5. AOT and Runtime Notes
6. Do and Don't Guidance
7. Troubleshooting
8. Official Resources

## Scope and Primary APIs

Use this reference to keep a polished design system usable across languages, cultures, and reading directions.

Primary APIs:
- `FlowDirection`
- `Visual.FlowDirection`
- `TextBlock`, `SelectableTextBlock`
- `Grid`, `StackPanel`, `DockPanel`
- `PathIcon`
- `FormattedText`, `TextLayout`
- `AutomationProperties`

This file covers:
- localization-safe copy and layout,
- right-to-left and bidirectional UI,
- icon mirroring and directional language,
- inclusive design rules for broad user needs.

## Localization-Safe Design Rules

Localization-safe UI starts with content and layout discipline:

- do not assume English-length labels,
- avoid hardcoding width around short words,
- let labels wrap where possible,
- prefer `Start` / `End` semantics over `Left` / `Right` in UX language,
- keep parallel labels structurally similar so translation stays consistent.

```xml
<Grid xmlns="https://github.com/avaloniaui"
      xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
      ColumnDefinitions="*,Auto"
      ColumnSpacing="12">
  <TextBlock TextWrapping="Wrap"
             Text="Review the deployment summary and confirm the next action." />
  <Button Grid.Column="1"
          MinWidth="140"
          Content="Deploy now" />
</Grid>
```

Guidance:
- use minimum sizes more often than fixed sizes,
- keep commands short enough to remain tappable when translated,
- avoid embedding meaning only in icon direction or physical position,
- test with long strings and mirrored layouts early.

## BiDi and `FlowDirection` Patterns

Avalonia exposes inherited `FlowDirection` on `Visual`, which makes RTL support a layout concern rather than an afterthought.

```xml
<StackPanel xmlns="https://github.com/avaloniaui"
            xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
            FlowDirection="RightToLeft"
            Spacing="8">
  <TextBlock Classes="title" Text="مركز الإصدارات" />
  <TextBlock Classes="body"
             TextWrapping="Wrap"
             Text="راجع الإعدادات ثم اختر الإجراء التالي." />
</StackPanel>
```

For custom text or drawing paths, pass the intended flow direction explicitly when text layout is built in code.

```csharp
using Avalonia.Media;

var text = new FormattedText(
    "Release summary",
    CultureInfo.CurrentCulture,
    FlowDirection.LeftToRight,
    new Typeface("Inter"),
    14,
    Brushes.White);
```

Rules:
- mirror layout where the product language expects it,
- review iconography that implies direction,
- avoid mixed-direction strings without explicit testing,
- do not assume a left rail is always culturally correct.

## Inclusive Design Rules

Inclusive design means the UI works for broader abilities, contexts, and experience levels.

Rules:
- keep primary workflows understandable without specialist jargon,
- do not rely on color alone,
- preserve readable type and clear focus states,
- provide enough time and control around risky or timed tasks,
- write helper text that reduces uncertainty rather than scolding the user.

Inclusive polish overlaps with accessibility, but the design review should also ask:
- would a first-time user understand this state,
- would a low-vision or high-zoom user keep the same hierarchy,
- would a translated UI still preserve the same decision flow.

## AOT and Runtime Notes

- `FlowDirection` is a normal visual property and fits well into compiled XAML examples.
- Keep localization behavior in shared styles and layouts rather than page-specific hacks.
- Review custom text rendering code paths for explicit culture and flow-direction handling.

## Do and Don't Guidance

Do:
- design for string growth and mirrored layouts,
- keep directional language semantic rather than physical,
- include localization and inclusive review in the same design gate as spacing and contrast.

Do not:
- hardcode tiny widths around English labels,
- assume icons or layout direction explain meaning by themselves,
- leave RTL support until after visual polish is finished.

## Troubleshooting

1. A localized page feels cramped.
- Fixed widths and over-compressed action bars are usually the cause.

2. RTL works technically but feels awkward.
- Revisit shell assumptions, icon direction, and local navigation placement.

3. Inclusive review still finds confusing workflows.
- The issue is likely language and hierarchy, not only accessibility metadata.

## Official Resources

- Design for bidirectional text: [learn.microsoft.com/en-us/windows/apps/design/globalizing/design-for-bidi-text](https://learn.microsoft.com/en-us/windows/apps/design/globalizing/design-for-bidi-text)
- Adjust layout and fonts and support RTL: [learn.microsoft.com/en-us/windows/apps/design/globalizing/adjust-layout-and-fonts--and-support-rtl](https://learn.microsoft.com/en-us/windows/apps/design/globalizing/adjust-layout-and-fonts--and-support-rtl)
- Prepare your app for localization: [learn.microsoft.com/en-us/windows/apps/design/globalizing/prepare-your-app-for-localization](https://learn.microsoft.com/en-us/windows/apps/design/globalizing/prepare-your-app-for-localization)
- Designing inclusive software: [learn.microsoft.com/en-us/windows/apps/design/accessibility/designing-inclusive-software](https://learn.microsoft.com/en-us/windows/apps/design/accessibility/designing-inclusive-software)
- Fluent 2 accessibility: [fluent2.microsoft.design/accessibility](https://fluent2.microsoft.design/accessibility)
