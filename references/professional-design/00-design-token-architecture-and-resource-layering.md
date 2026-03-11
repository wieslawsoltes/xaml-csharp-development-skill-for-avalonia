# Design Token Architecture and Resource Layering in Avalonia

## Table of Contents
1. Scope and Primary APIs
2. Token Model
3. Resource Composition
4. Practical Rules
5. AOT and Performance Notes
6. Do and Don't Guidance
7. Troubleshooting
8. Official Resources

## Scope and Primary APIs

Use this reference to build the token backbone for a professional Avalonia app.

Primary APIs:
- `Application.Resources`, `Application.Styles`
- `ResourceDictionary`, `MergedDictionaries`, `ThemeDictionaries`
- `ThemeVariant`, `ThemeVariantScope`
- `DynamicResourceExtension`, `ResourceInclude`, `StyleInclude`
- `Style`, `ControlTheme`, `StyledElement.Theme`

## Token Model

Use three layers:

1. Primitive tokens
- raw numbers and colors such as spacing steps, radii, font sizes, and shadow values.

2. Semantic tokens
- intent-based names such as `Brush.Text.Primary` or `Brush.Surface.Card`.

3. Component tokens
- values scoped to one UI family such as `Button.Primary.Padding` or `Shell.Nav.RailWidth`.

Recommended structure:

```text
Design/
  Tokens/
    Primitives.axaml
    Semantic.LightDark.axaml
    Component.Buttons.axaml
    Component.Shell.axaml
```

## Resource Composition

```xml
<Application xmlns="https://github.com/avaloniaui"
             xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
             RequestedThemeVariant="Default">
  <Application.Resources>
    <ResourceDictionary>
      <ResourceDictionary.MergedDictionaries>
        <ResourceInclude Source="avares://MyApp/Design/Tokens/Primitives.axaml" />
        <ResourceInclude Source="avares://MyApp/Design/Tokens/Semantic.LightDark.axaml" />
        <ResourceInclude Source="avares://MyApp/Design/Tokens/Component.Buttons.axaml" />
        <ResourceInclude Source="avares://MyApp/Design/Tokens/Component.Shell.axaml" />
      </ResourceDictionary.MergedDictionaries>
    </ResourceDictionary>
  </Application.Resources>
</Application>
```

Primitive and semantic example:

```xml
<ResourceDictionary xmlns="https://github.com/avaloniaui"
                    xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml">
  <x:Double x:Key="Space.100">4</x:Double>
  <x:Double x:Key="Space.200">8</x:Double>
  <x:Double x:Key="Space.400">16</x:Double>
  <CornerRadius x:Key="Radius.100">8</CornerRadius>
  <Thickness x:Key="Inset.Control">14,10</Thickness>

  <ResourceDictionary.ThemeDictionaries>
    <ResourceDictionary x:Key="Light">
      <Color x:Key="Color.Surface.Card">#FFFFFFFF</Color>
      <Color x:Key="Color.Text.Primary">#FF16181D</Color>
    </ResourceDictionary>
    <ResourceDictionary x:Key="Dark">
      <Color x:Key="Color.Surface.Card">#FF171A20</Color>
      <Color x:Key="Color.Text.Primary">#FFF7F9FC</Color>
    </ResourceDictionary>
  </ResourceDictionary.ThemeDictionaries>

  <SolidColorBrush x:Key="Brush.Surface.Card" Color="{DynamicResource Color.Surface.Card}" />
  <SolidColorBrush x:Key="Brush.Text.Primary" Color="{DynamicResource Color.Text.Primary}" />
</ResourceDictionary>
```

## Practical Rules

- Keep primitive tokens dull and reusable.
- Put light/dark decisions in `ThemeDictionaries`, not code-behind branches.
- Reference semantic tokens from component themes, not raw values.
- Use `ControlTheme` for reusable families and plain `Style` for small selector-based adjustments.

## AOT and Performance Notes

- Keep resource dictionaries compiled and split by topic.
- Avoid runtime XAML parsing for token packs unless plugin loading is required.
- Use `DynamicResource` only for values expected to change.

## Do and Don't Guidance

Do:
- stabilize semantic names early,
- split tokens by ownership,
- let component themes depend on semantic resources.

Do not:
- hardcode hex values across many files,
- mix primitive and semantic naming in one layer,
- rebuild full token dictionaries at runtime for small changes.

## Troubleshooting

1. Theme switching updates only some surfaces.
- The missed surfaces are usually using `StaticResource` instead of `DynamicResource`.

2. Styling ownership becomes unclear.
- Split dictionaries by token layer or feature boundary and keep filenames explicit.

3. Component themes drift visually.
- Replace raw setter values with semantic keys and centralize the tokens.

## Official Resources

- Avalonia resources: [docs.avaloniaui.net/docs/guides/styles-and-resources/resources](https://docs.avaloniaui.net/docs/guides/styles-and-resources/resources)
- Avalonia themes: [docs.avaloniaui.net/docs/basics/user-interface/styling/themes](https://docs.avaloniaui.net/docs/basics/user-interface/styling/themes/)
- Fluent 2 design tokens: [fluent2.microsoft.design/design-tokens](https://fluent2.microsoft.design/design-tokens)
