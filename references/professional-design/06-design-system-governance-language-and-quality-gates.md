# Design System Governance, Language, and Quality Gates in Avalonia

## Table of Contents
1. Scope and Primary APIs
2. Design-System Contracts
3. Command and Content Language
4. Component State Matrix
5. Review and Release Gates
6. AOT and Runtime Notes
7. Do and Don't Guidance
8. Troubleshooting
9. Official Resources

## Scope and Primary APIs

Use this reference to keep a design system coherent after tokens and themes exist.

Primary APIs:
- `Style`, `ControlTheme`, `ResourceDictionary`
- `Classes`, pseudo-classes, `ThemeVariantScope`
- `Button`, `ToggleButton`, `MenuFlyout`, `Expander`, `TabControl`
- `TextBlock`, `SelectableTextBlock`, `ToolTip`
- `AutomationProperties`

This file covers the missing design-system rules that usually separate "styled" UI from a product-quality UI:
- consistent naming and ownership,
- command hierarchy and content language,
- shared state definitions across components,
- design review and release gates.

## Design-System Contracts

Treat the system as four contracts:

1. Foundation contract
- spacing, typography, radius, border, elevation, motion, and color tokens.

2. Semantic contract
- names that describe intent, such as `Brush.Surface.Card`, `Brush.Text.Secondary`, or `Motion.Duration.Fast`.

3. Component contract
- per-component slots and states, such as `Button.Primary.Background.Rest` or `Shell.NavItem.Padding.Compact`.

4. Usage contract
- where primary, secondary, quiet, destructive, disclosure, and status patterns are allowed.

Recommended ownership split:

```text
Design/
  Tokens/
  Themes/
  Patterns/
  Reviews/
```

Practical rules:
- do not let views invent new token names casually,
- keep one command hierarchy across the whole app,
- publish density and state rules once and reuse them,
- treat dialogs, flyouts, notifications, and pages as one system.

## Command and Content Language

Command labels should reflect product intent, not generic framework verbs.

```xml
<StackPanel xmlns="https://github.com/avaloniaui"
            xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
            Spacing="8">
  <TextBlock Classes="section-title" Text="Deployment" />
  <TextBlock Classes="body"
             Foreground="{DynamicResource Brush.Text.Secondary}"
             Text="Review the release details and choose the next action." />

  <StackPanel Orientation="Horizontal" Spacing="8">
    <Button Classes="primary" Content="Deploy now" />
    <Button Classes="secondary" Content="Save draft" />
    <Button Classes="quiet" Content="View history" />
  </StackPanel>

  <Button Classes="danger"
          Content="Delete environment"
          AutomationProperties.Name="Delete environment" />
</StackPanel>
```

Guidance:
- use one clear primary action per region,
- prefer verb-first labels such as `Deploy now`, `Add member`, `Open report`,
- make destructive actions explicit,
- keep helper text calm and specific,
- use sentence case for headings, labels, and most supporting copy.

Avoid:
- generic labels such as `Submit`, `Continue`, or `OK` when the action can be named,
- marketing tone in productivity flows,
- mixing instructional tone and status tone in the same region.

## Component State Matrix

Every reusable family should define the same state vocabulary where relevant:

- rest
- pointer over
- pressed
- focused or focus-visible
- disabled
- selected
- loading
- success
- warning
- error
- empty

Token naming pattern:

```text
Button.Primary.Background.Rest
Button.Primary.Background.PointerOver
Button.Primary.Border.FocusVisible
Button.Primary.Foreground.Disabled
Shell.NavItem.Background.Selected
Dialog.Surface.Error
```

Do not ship component variants without documenting:
- which states they support,
- what changes in each state,
- which state wins when two states overlap,
- whether motion is allowed for that state.

## Review and Release Gates

Use a repeatable review gate before promoting a new theme or component family:

1. Visual consistency
- spacing, radius, border, and shadow ramps are reused rather than reinvented.

2. Hierarchy
- the most important action and message are obvious within two seconds.

3. Accessibility
- focus is visible, contrast holds in light and dark, automation names exist for icon-only actions.

4. Localization
- labels still work when text expands, truncates, or wraps.

5. Density
- default and compact treatments remain readable and clickable.

6. Feedback
- loading, empty, warning, success, and error states all feel like the same product.

7. Input
- keyboard, touch, and pointer affordances are all clear.

## AOT and Runtime Notes

- Keep design-system rules expressed through compiled XAML styles and themes.
- Prefer class toggles and stable resource keys over runtime-generated styling logic.
- Keep review checklists and state matrices in docs, not only in designer memory.

## Do and Don't Guidance

Do:
- define command hierarchy globally,
- keep state names parallel across components,
- review content and visuals together.

Do not:
- let every page invent its own button taxonomy,
- change tone between dialogs, flyouts, and full pages,
- treat accessibility or localization as final-pass cleanup only.

## Troubleshooting

1. The product looks consistent on one page but not across the app.
- The design language is probably local-style driven instead of theme-driven.

2. Teams disagree about labels and action priority.
- Publish command hierarchy rules and examples for primary, secondary, quiet, and danger actions.

3. New components regress quality late.
- Add a design gate that checks states, accessibility, localization, and density before merge.

## Official Resources

- Fluent 2 design principles: [fluent2.microsoft.design/design-principles](https://fluent2.microsoft.design/design-principles)
- Fluent 2 content design: [fluent2.microsoft.design/content-design](https://fluent2.microsoft.design/content-design)
- Content design basics for Windows apps: [learn.microsoft.com/en-us/windows/apps/design/basics/content-basics](https://learn.microsoft.com/en-us/windows/apps/design/basics/content-basics)
- Buttons for Windows apps: [learn.microsoft.com/en-us/windows/apps/design/controls/buttons](https://learn.microsoft.com/en-us/windows/apps/design/controls/buttons)
- Microsoft Style Guide welcome: [learn.microsoft.com/en-us/style-guide/welcome](https://learn.microsoft.com/en-us/style-guide/welcome/)
- Microsoft Style Guide capitalization: [learn.microsoft.com/en-us/style-guide/capitalization](https://learn.microsoft.com/en-us/style-guide/capitalization)
