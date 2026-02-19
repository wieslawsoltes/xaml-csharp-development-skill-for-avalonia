# WPF UserControl, CustomControl, and TemplatedControl to Avalonia

## Table of Contents
1. Scope and APIs
2. Authoring Model Mapping
3. Conversion Example
4. Avalonia C# Equivalent
5. Troubleshooting

## Scope and APIs

Primary WPF APIs:

- `UserControl`
- `Control` subclasses with `DefaultStyleKey` metadata override
- template parts and custom dependency properties

Primary Avalonia APIs:

- `UserControl`
- `TemplatedControl`
- `ControlTheme`, template parts, styled/direct properties

## Authoring Model Mapping

| WPF | Avalonia |
|---|---|
| `UserControl` | `UserControl` |
| custom control with `DefaultStyleKey` override | `TemplatedControl` + `ControlTheme` |
| dependency properties | Avalonia styled/direct properties |

## Conversion Example

WPF C#:

```csharp
public class BadgeControl : Control
{
    static BadgeControl()
    {
        DefaultStyleKeyProperty.OverrideMetadata(typeof(BadgeControl),
            new FrameworkPropertyMetadata(typeof(BadgeControl)));
    }
}
```

Avalonia XAML (`Styles.axaml`):

```xaml
<ControlTheme xmlns="https://github.com/avaloniaui"
              xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
              xmlns:local="using:MyApp.Controls"
              x:Key="BadgeControlTheme"
              TargetType="local:BadgeControl">
  <Setter Property="Template">
    <ControlTemplate>
      <Border Background="{TemplateBinding Background}" CornerRadius="10" Padding="8,2">
        <ContentPresenter Content="{TemplateBinding Content}" />
      </Border>
    </ControlTemplate>
  </Setter>
</ControlTheme>
```

Usage:

```xaml
<local:BadgeControl xmlns="https://github.com/avaloniaui"
                    xmlns:local="using:MyApp.Controls"
                    Theme="{StaticResource BadgeControlTheme}"
                    Content="New" />
```

## Avalonia C# Equivalent

```csharp
using Avalonia;
using Avalonia.Controls.Primitives;

public class BadgeControl : TemplatedControl
{
    public static readonly StyledProperty<object?> ContentProperty =
        AvaloniaProperty.Register<BadgeControl, object?>(nameof(Content));

    public object? Content
    {
        get => GetValue(ContentProperty);
        set => SetValue(ContentProperty, value);
    }
}
```

## Troubleshooting

1. custom control renders as empty box.
- ensure a `ControlTheme` exists and is loaded into app styles.

2. properties not styleable.
- use `StyledProperty` for values intended to be set by styles.

3. template part code fails at runtime.
- verify expected part names/types in `OnApplyTemplate`.
