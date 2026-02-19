# WPF Resources, StaticResource, DynamicResource, and Merged Dictionaries to Avalonia

## Table of Contents
1. Scope and APIs
2. Resource Mapping
3. Conversion Example
4. Avalonia C# Equivalent
5. Troubleshooting

## Scope and APIs

Primary WPF APIs:

- `ResourceDictionary`
- `StaticResource`, `DynamicResource`
- `MergedDictionaries`

Primary Avalonia APIs:

- `ResourceDictionary`
- `StaticResource` and `DynamicResource` markup
- merged dictionaries and theme dictionaries

## Resource Mapping

| WPF | Avalonia |
|---|---|
| `StaticResource` | `StaticResource` |
| `DynamicResource` | `DynamicResource` |
| `Application.Resources` and merged dictionaries | same concept |
| theme dictionary lookups | `ThemeDictionaries` and theme-variant resources |

## Conversion Example

WPF XAML:

```xaml
<Application.Resources>
  <ResourceDictionary>
    <ResourceDictionary.MergedDictionaries>
      <ResourceDictionary Source="Themes/Colors.xaml" />
    </ResourceDictionary.MergedDictionaries>

    <SolidColorBrush x:Key="AccentBrush" Color="#0E639C" />
  </ResourceDictionary>
</Application.Resources>
```

Avalonia XAML:

```xaml
<Application xmlns="https://github.com/avaloniaui"
             xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml">
  <Application.Resources>
    <ResourceDictionary>
      <ResourceDictionary.MergedDictionaries>
        <ResourceInclude Source="avares://MyApp/Styles/Colors.axaml" />
      </ResourceDictionary.MergedDictionaries>

      <SolidColorBrush x:Key="AccentBrush" Color="#0E639C" />
    </ResourceDictionary>
  </Application.Resources>
</Application>

<Button Background="{StaticResource AccentBrush}" />
<Border Background="{DynamicResource AccentBrush}" />
```

## Avalonia C# Equivalent

```csharp
using Avalonia;
using Avalonia.Controls;
using Avalonia.Markup.Xaml.Styling;
using Avalonia.Media;

var app = Application.Current!;
var dict = new ResourceDictionary
{
    ["AccentBrush"] = new SolidColorBrush(Color.Parse("#0E639C"))
};

dict.MergedDictionaries.Add(new ResourceInclude
{
    Source = new Uri("avares://MyApp/Styles/Colors.axaml")
});

app.Resources.MergedDictionaries.Add(dict);
```

## Troubleshooting

1. Resource not found at runtime.
- verify asset URI and dictionary inclusion in app resources.

2. Theme switch does not update color.
- use `DynamicResource` for theme-dependent values.

3. Duplicate resource keys produce surprising overrides.
- centralize key ownership and document override order.
