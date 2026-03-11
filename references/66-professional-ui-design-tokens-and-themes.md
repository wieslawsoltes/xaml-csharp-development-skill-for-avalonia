# Professional UI/UX Design Tokens and Themes in Avalonia

## Table of Contents
1. Scope and Coverage Contract
2. Design Workflow
3. Granular Reference Set
4. Full API Coverage Pointers
5. First Example
6. AOT and Runtime Notes
7. Official Design Resources

## Scope and Coverage Contract

This reference lane covers how to design professional-looking Avalonia applications with:

- coherent design-token architecture,
- typography and content hierarchy,
- color, surface, elevation, and material decisions,
- reusable control themes and shell patterns,
- responsive layout and density strategies,
- motion, focus, accessibility, loading, empty, and error UX polish,
- design-system governance, command language, and release-review rules,
- transition, page-transition, and composition-animation architecture,
- information architecture, navigation selection, progressive disclosure, and dense-product workflows.

Coverage intent for this lane:

- guidance stays app-development-focused and aligned to Avalonia `11.3.12`,
- examples stay XAML-first with compiled-binding-friendly patterns,
- detailed topics are split into smaller files so they can be loaded selectively.

Use this lane together with:
- [`04-styles-themes-resources.md`](04-styles-themes-resources)
- [`10-templated-controls-and-control-themes.md`](10-templated-controls-and-control-themes)
- [`16-property-system-attached-properties-behaviors-and-style-properties.md`](16-property-system-attached-properties-behaviors-and-style-properties)
- [`17-resources-assets-theme-variants-and-xmlns.md`](17-resources-assets-theme-variants-and-xmlns)
- [`28-custom-themes-xaml-and-code-only.md`](28-custom-themes-xaml-and-code-only)

## Design Workflow

1. Define the product tone, layout density, and content hierarchy first.
2. Establish primitive, semantic, and component token layers.
3. Build typography, iconography, and surface treatments from those tokens.
4. Create reusable `ControlTheme` and `ItemContainerTheme` variants.
5. Define command language, state matrices, and design review gates.
6. Add responsive shell behavior with `ContainerQuery`, class state, and density choices.
7. Finish with motion, composition, focus, accessibility, loading/empty/error states, and UX review.

## Granular Reference Set

All detailed professional-design references now live under [`professional-design/README.md`](professional-design/README):

- [`00-design-token-architecture-and-resource-layering.md`](professional-design/00-design-token-architecture-and-resource-layering)
- [`01-typography-iconography-and-content-hierarchy.md`](professional-design/01-typography-iconography-and-content-hierarchy)
- [`02-color-surfaces-elevation-and-material-depth.md`](professional-design/02-color-surfaces-elevation-and-material-depth)
- [`03-component-themes-variants-and-shell-surfaces.md`](professional-design/03-component-themes-variants-and-shell-surfaces)
- [`04-responsive-layout-density-and-stateful-feedback.md`](professional-design/04-responsive-layout-density-and-stateful-feedback)
- [`05-motion-focus-accessibility-and-design-review.md`](professional-design/05-motion-focus-accessibility-and-design-review)
- [`06-design-system-governance-language-and-quality-gates.md`](professional-design/06-design-system-governance-language-and-quality-gates)
- [`07-animations-composition-and-motion-architecture.md`](professional-design/07-animations-composition-and-motion-architecture)
- [`08-information-architecture-navigation-and-progressive-disclosure.md`](professional-design/08-information-architecture-navigation-and-progressive-disclosure)
- [`09-forms-decision-heavy-ux-and-data-dense-surfaces.md`](professional-design/09-forms-decision-heavy-ux-and-data-dense-surfaces)
- [`10-advanced-composition-implicit-expression-and-animation-group-patterns.md`](professional-design/10-advanced-composition-implicit-expression-and-animation-group-patterns)
- [`11-globalization-localization-bidi-and-inclusive-design.md`](professional-design/11-globalization-localization-bidi-and-inclusive-design)
- [`12-touch-gesture-postures-and-kinetic-feedback.md`](professional-design/12-touch-gesture-postures-and-kinetic-feedback)

## Full API Coverage Pointers

For exhaustive lookup beyond these design-specific docs:

- styles/themes/resources: [`04-styles-themes-resources.md`](04-styles-themes-resources), [`17-resources-assets-theme-variants-and-xmlns.md`](17-resources-assets-theme-variants-and-xmlns)
- control authoring/themes: [`10-templated-controls-and-control-themes.md`](10-templated-controls-and-control-themes)
- layout and adaptive behavior: [`16-property-system-attached-properties-behaviors-and-style-properties.md`](16-property-system-attached-properties-behaviors-and-style-properties), [`30-layout-measure-arrange-and-custom-layout-controls.md`](30-layout-measure-arrange-and-custom-layout-controls)
- text, color, and vector assets: [`35-path-icons-and-vector-geometry-assets.md`](35-path-icons-and-vector-geometry-assets), [`59-media-colors-brushes-and-formatted-text-practical-usage.md`](59-media-colors-brushes-and-formatted-text-practical-usage)
- overlays and shell surfaces: [`25-popups-flyouts-tooltips-and-overlays.md`](25-popups-flyouts-tooltips-and-overlays), [`53-menu-controls-contextmenu-and-menuflyout-patterns.md`](53-menu-controls-contextmenu-and-menuflyout-patterns)
- signatures: [`api-index-generated.md`](api-index-generated)

## First Example

Token-first surface example:

```xml
<Border xmlns="https://github.com/avaloniaui"
        xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
        Classes="app-card"
        Padding="{DynamicResource Inset.Card}">
  <StackPanel Spacing="{DynamicResource Space.200}">
    <TextBlock Classes="eyebrow" Text="Performance" />
    <TextBlock Classes="title" Text="Release readiness" />
    <TextBlock Classes="body"
               Text="Professional-looking UI starts with consistent spacing, hierarchy, and reusable component rules." />
  </StackPanel>
</Border>
```

```xml
<Style Selector="Border.app-card">
  <Setter Property="Background" Value="{DynamicResource Brush.Surface.Card}" />
  <Setter Property="BorderBrush" Value="{DynamicResource Brush.Border.Subtle}" />
  <Setter Property="BorderThickness" Value="1" />
  <Setter Property="CornerRadius" Value="{DynamicResource Radius.200}" />
  <Setter Property="BoxShadow" Value="{DynamicResource Shadow.Card.Rest}" />
</Style>
```

## AOT and Runtime Notes

- Keep tokens, styles, and themes in compiled XAML by default.
- Use `DynamicResource` only for values that must react to theme or runtime changes.
- Keep runtime class or density updates explicit and on `Dispatcher.UIThread`.
- Prefer stable semantic keys over ad hoc code-generated style values.

## Official Design Resources

- Avalonia styles: [docs.avaloniaui.net/docs/basics/user-interface/styling/styles](https://docs.avaloniaui.net/docs/basics/user-interface/styling/styles)
- Avalonia style classes: [docs.avaloniaui.net/docs/basics/user-interface/styling/style-classes](https://docs.avaloniaui.net/docs/basics/user-interface/styling/style-classes)
- Avalonia control themes: [docs.avaloniaui.net/docs/basics/user-interface/styling/control-themes](https://docs.avaloniaui.net/docs/basics/user-interface/styling/control-themes)
- Avalonia resources: [docs.avaloniaui.net/docs/guides/styles-and-resources/resources](https://docs.avaloniaui.net/docs/guides/styles-and-resources/resources)
- Avalonia container queries: [docs.avaloniaui.net/docs/basics/user-interface/styling/container-queries](https://docs.avaloniaui.net/docs/basics/user-interface/styling/container-queries)
- Avalonia transitions: [docs.avaloniaui.net/docs/guides/graphics-and-animation/transitions](https://docs.avaloniaui.net/docs/guides/graphics-and-animation/transitions)
- Avalonia `Compositor` API: [api-docs.avaloniaui.net/docs/T_Avalonia_Rendering_Composition_Compositor](https://api-docs.avaloniaui.net/docs/T_Avalonia_Rendering_Composition_Compositor)
- Fluent 2 design principles: [fluent2.microsoft.design/design-principles](https://fluent2.microsoft.design/design-principles)
- Fluent 2 content design: [fluent2.microsoft.design/content-design](https://fluent2.microsoft.design/content-design)
- Fluent 2 layout: [fluent2.microsoft.design/layout](https://fluent2.microsoft.design/layout)
- Fluent 2 accessibility: [fluent2.microsoft.design/accessibility](https://fluent2.microsoft.design/accessibility)
