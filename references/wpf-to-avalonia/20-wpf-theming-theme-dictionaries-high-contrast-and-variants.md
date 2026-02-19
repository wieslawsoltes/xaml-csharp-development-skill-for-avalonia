# WPF Theming, Theme Dictionaries, High Contrast, and Variants to Avalonia

## Table of Contents
1. Scope and APIs
2. Theme Mapping
3. Conversion Example
4. Avalonia C# Equivalent
5. Troubleshooting

## Scope and APIs

Primary WPF APIs:

- themed resource dictionaries
- high-contrast/system theme reactions

Primary Avalonia APIs:

- `ThemeVariant` (`Light`, `Dark`, `Default`)
- `Application.RequestedThemeVariant`
- `ThemeVariantScope`
- `ResourceDictionary.ThemeDictionaries`

## Theme Mapping

| WPF | Avalonia |
|---|---|
| theme-specific dictionaries | `ThemeDictionaries` keyed by `ThemeVariant` |
| app-level theme changes | `Application.RequestedThemeVariant` |
| subtree theme overrides | `ThemeVariantScope` |

## Conversion Example

WPF XAML concept:

```xaml
<!-- Theme dictionaries chosen by current system theme -->
```

Avalonia XAML:

```xaml
<Application xmlns="https://github.com/avaloniaui"
             xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml">
  <Application.Resources>
    <ResourceDictionary>
      <ResourceDictionary.ThemeDictionaries>
        <ResourceDictionary x:Key="Light">
          <SolidColorBrush x:Key="ShellBackground" Color="#F8F9FB" />
        </ResourceDictionary>
        <ResourceDictionary x:Key="Dark">
          <SolidColorBrush x:Key="ShellBackground" Color="#1F2430" />
        </ResourceDictionary>
      </ResourceDictionary.ThemeDictionaries>
    </ResourceDictionary>
  </Application.Resources>
</Application>

<Border Background="{DynamicResource ShellBackground}" />
```

## Avalonia C# Equivalent

```csharp
using Avalonia;
using Avalonia.Styling;

Application.Current!.RequestedThemeVariant = ThemeVariant.Dark;
```

Subtree override:

```xaml
<ThemeVariantScope RequestedThemeVariant="Light">
  <ContentPresenter />
</ThemeVariantScope>
```

## Troubleshooting

1. theme change does not propagate.
- use `DynamicResource` for theme-dependent values.

2. mixed theme surfaces conflict.
- isolate subtree overrides with `ThemeVariantScope`.

3. high-contrast behavior is inconsistent.
- verify resource keys and automation/accessibility contrast usage.
