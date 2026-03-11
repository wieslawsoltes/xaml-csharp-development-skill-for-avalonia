# Component Themes, Variants, and Shell Surfaces in Avalonia

## Table of Contents
1. Scope and Primary APIs
2. Button and Card Variants
3. Lists, Navigation, and Flyouts
4. Shell Guidance
5. AOT and Performance Notes
6. Do and Don't Guidance
7. Troubleshooting
8. Official Resources

## Scope and Primary APIs

Use this reference to make reusable component families instead of one-off styles.

Primary APIs:
- `ControlTheme`, `StyledElement.Theme`
- `Style`, nested selectors, `TemplateBinding`
- `ItemsControl.ItemContainerTheme`
- `Flyout.FlyoutPresenterTheme`, `MenuFlyout.ItemContainerTheme`

High-value theme members:
- `StyledElement.ThemeProperty`
- `StyledElement.Theme`
- `ItemsControl.ItemContainerThemeProperty`
- `ItemsControl.ItemContainerTheme`
- `Flyout.FlyoutPresenterThemeProperty`
- `Flyout.FlyoutPresenterTheme`
- `MenuFlyout.ItemContainerThemeProperty`
- `MenuFlyout.FlyoutPresenterThemeProperty`
- `TemplateBinding`

## Button and Card Variants

```xml
<ResourceDictionary xmlns="https://github.com/avaloniaui"
                    xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml">
  <ControlTheme x:Key="PrimaryButtonTheme"
                TargetType="Button"
                BasedOn="{StaticResource {x:Type Button}}">
    <Setter Property="Padding" Value="{DynamicResource Inset.Control}" />
    <Setter Property="CornerRadius" Value="{DynamicResource Radius.100}" />
    <Setter Property="Background" Value="{DynamicResource Brush.Action.Primary}" />
    <Setter Property="Foreground" Value="White" />
    <Setter Property="BorderBrush" Value="{DynamicResource Brush.Action.Primary}" />

    <Style Selector="^:pointerover">
      <Setter Property="Background" Value="{DynamicResource Brush.Action.Primary.Hover}" />
    </Style>
  </ControlTheme>

  <ControlTheme x:Key="CardSurfaceTheme"
                TargetType="Border">
    <Setter Property="Background" Value="{DynamicResource Brush.Surface.Card}" />
    <Setter Property="BorderBrush" Value="{DynamicResource Brush.Border.Subtle}" />
    <Setter Property="BorderThickness" Value="1" />
    <Setter Property="CornerRadius" Value="{DynamicResource Radius.200}" />
    <Setter Property="Padding" Value="{DynamicResource Inset.Card}" />
  </ControlTheme>
</ResourceDictionary>
```

## Lists, Navigation, and Flyouts

```xml
<ResourceDictionary xmlns="https://github.com/avaloniaui"
                    xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml">
  <ControlTheme x:Key="NavItemTheme"
                TargetType="ListBoxItem"
                BasedOn="{StaticResource {x:Type ListBoxItem}}">
    <Setter Property="Padding" Value="12,10" />
    <Setter Property="Margin" Value="0,0,0,4" />
    <Setter Property="CornerRadius" Value="{DynamicResource Radius.100}" />
  </ControlTheme>

  <ControlTheme x:Key="OverlayPresenterTheme"
                TargetType="FlyoutPresenter"
                BasedOn="{StaticResource {x:Type FlyoutPresenter}}">
    <Setter Property="Background" Value="{DynamicResource Brush.Surface.Card}" />
    <Setter Property="BorderBrush" Value="{DynamicResource Brush.Border.Subtle}" />
    <Setter Property="BorderThickness" Value="1" />
    <Setter Property="CornerRadius" Value="{DynamicResource Radius.200}" />
    <Setter Property="Padding" Value="6" />
  </ControlTheme>
</ResourceDictionary>
```

```xml
<ListBox ItemContainerTheme="{StaticResource NavItemTheme}" />
<MenuFlyout FlyoutPresenterTheme="{StaticResource OverlayPresenterTheme}" />
```

## Shell Guidance

- Treat nav rails, sidebars, cards, dialogs, and flyouts as one design system.
- Reuse radius, border, spacing, and shadow ramps across surfaces.
- Keep shell chrome quieter than content emphasis surfaces.

## AOT and Performance Notes

- Prefer `ControlTheme` resources over runtime template creation.
- Keep nested template selectors stable and tied to explicit part contracts.

## Do and Don't Guidance

Do:
- use `BasedOn` to preserve control defaults,
- theme item containers and overlay presenters explicitly,
- share variant names across views.

Do not:
- rebuild the same visual language with separate local styles in every view,
- overuse deep descendant selectors,
- couple visual hierarchy to code-behind state.

## Troubleshooting

1. Reusable components still look inconsistent.
- Move remaining local styles into shared `ControlTheme` or semantic resources.

2. Flyouts look disconnected from the app.
- Apply the same surface, radius, border, and shadow tokens used by cards and dialogs.

3. List items ignore spacing or selected-state expectations.
- Set `ItemContainerTheme` explicitly instead of styling only the content template.

## Official Resources

- Avalonia control themes: [docs.avaloniaui.net/docs/basics/user-interface/styling/control-themes](https://docs.avaloniaui.net/docs/basics/user-interface/styling/control-themes)
- Avalonia style classes: [docs.avaloniaui.net/docs/basics/user-interface/styling/style-classes](https://docs.avaloniaui.net/docs/basics/user-interface/styling/style-classes)
