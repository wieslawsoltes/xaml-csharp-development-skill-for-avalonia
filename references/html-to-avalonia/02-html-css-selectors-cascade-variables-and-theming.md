# HTML/CSS Selectors, Cascade, Variables, and Theming in Avalonia

## Table of Contents
1. Scope and APIs
2. Selector Mapping
3. Selector Conversion Examples
4. Cascade/Precedence Differences
5. CSS Custom Properties to Avalonia Resources
6. Component Variants and State Styling
7. Conversion Example: Button System
8. C# Equivalent: Button System
9. AOT/Trimming Notes
10. Troubleshooting

## Scope and APIs

Primary APIs:

- `Style`, `Styles`, `Setter`, `ControlTheme`
- `Selectors` (`Is`, `OfType`, `Class`, `Name`, `Child`, `Descendant`, `Not`, `NthChild`, `PropertyEquals`)
- `ThemeVariant`, `ThemeVariantScope`
- `ResourceDictionary` (`ThemeDictionaries`, `MergedDictionaries`, `TryGetResource`)
- `DynamicResourceExtension`, `StyleInclude`, `ResourceInclude`

Reference docs:

- [`04-styles-themes-resources.md`](../04-styles-themes-resources)
- [`10-templated-controls-and-control-themes.md`](../10-templated-controls-and-control-themes)
- [`17-resources-assets-theme-variants-and-xmlns.md`](../17-resources-assets-theme-variants-and-xmlns)
- [`28-custom-themes-xaml-and-code-only.md`](../28-custom-themes-xaml-and-code-only)

## Selector Mapping

| CSS selector idiom | Avalonia selector idiom |
|---|---|
| `.card` | `Border.card` or `*.card`-style targeting by type/class |
| `button.primary` | `Button.primary` |
| `#header` | `#Header` via `Name` selector |
| `.list > .item` | parent/child composition in selector chain |
| `.grid .cell` | descendant selector chain |
| `:hover` | `:pointerover` |
| `:focus` | `:focus` / `:focus-visible`-style patterns via pseudo-class support |
| `:disabled` | `:disabled` |
| `:nth-child(2n+1)` | `NthChild(step: 2, offset: 1)` in typed selector APIs |

For complex runtime style construction, prefer typed selectors in C#:

```csharp
using Avalonia.Controls;
using Avalonia.Styling;

var style = new Style(x => x.OfType<Button>().Class("primary").Not(y => y.Class("danger")));
style.Setters.Add(new Setter(
    Avalonia.Controls.Primitives.TemplatedControl.FontWeightProperty,
    Avalonia.Media.FontWeight.SemiBold));
```

## Selector Conversion Examples

HTML/CSS:

```css
.sidebar > .item:hover { background: #1b2638; }
.sidebar .item.active { border-left: 3px solid var(--accent); }
.panel :is(button, a).danger { color: #d13f4a; }
```

Avalonia:

```xaml
<Style Selector="StackPanel.sidebar > Border.item:pointerover">
  <Setter Property="Background" Value="#1B2638" />
</Style>
<Style Selector="StackPanel.sidebar Border.item.active">
  <Setter Property="BorderBrush" Value="{DynamicResource AccentBrush}" />
  <Setter Property="BorderThickness" Value="3,0,0,0" />
</Style>
<Style Selector="Border.panel Button.danger">
  <Setter Property="Foreground" Value="#D13F4A" />
</Style>
<Style Selector="Border.panel HyperlinkButton.danger">
  <Setter Property="Foreground" Value="#D13F4A" />
</Style>
```

Typed C# selector equivalent for `Sidebar > Item` (state-specific pseudo-classes are usually clearer in XAML selector strings):

```csharp
var itemStyle = new Style(x => x
    .OfType<StackPanel>().Class("sidebar")
    .Child()
    .OfType<Border>().Class("item"));
```

## Cascade/Precedence Differences

Important differences from browser CSS:

1. Avalonia property value precedence is integrated with the property system (local values, styles, bindings, animations).
2. Style ordering in `Styles` still matters when selectors overlap.
3. Local values (`SetValue`, inline XAML property assignment) usually override style-set values.

Practical rule: use explicit classes and small style scopes instead of very deep selector chains.

## CSS Custom Properties to Avalonia Resources

CSS:

```css
:root {
  --accent: #2f6fed;
  --surface: #10151e;
}
.card { background: var(--surface); border-color: var(--accent); }
```

Avalonia:

```xaml
<Application.Resources>
  <Color x:Key="AccentColor">#2F6FED</Color>
  <SolidColorBrush x:Key="AccentBrush" Color="{DynamicResource AccentColor}" />
  <SolidColorBrush x:Key="SurfaceBrush" Color="#10151E" />
</Application.Resources>

<Style Selector="Border.card">
  <Setter Property="Background" Value="{DynamicResource SurfaceBrush}" />
  <Setter Property="BorderBrush" Value="{DynamicResource AccentBrush}" />
</Style>
```

Theme-aware token split:

```xaml
<ResourceDictionary.ThemeDictionaries>
  <ResourceDictionary x:Key="Light">
    <SolidColorBrush x:Key="SurfaceBrush" Color="#F8FAFD" />
  </ResourceDictionary>
  <ResourceDictionary x:Key="Dark">
    <SolidColorBrush x:Key="SurfaceBrush" Color="#10151E" />
  </ResourceDictionary>
</ResourceDictionary.ThemeDictionaries>
```

## Component Variants and State Styling

Map utility/variant classes from CSS frameworks to Avalonia classes:

- `Button.primary`
- `Button.secondary`
- `Button.destructive`
- `Button:disabled`
- `Button:pointerover`

```xaml
<Style Selector="Button.primary">
  <Setter Property="Background" Value="{DynamicResource AccentBrush}" />
  <Setter Property="Foreground" Value="White" />
</Style>
<Style Selector="Button.primary:pointerover">
  <Setter Property="Opacity" Value="0.92" />
</Style>
<Style Selector="Button.primary:disabled">
  <Setter Property="Opacity" Value="0.45" />
</Style>
```

Use `ControlTheme` when variant changes include template structure (not only colors/metrics).

## Conversion Example: Button System

HTML/CSS:

```html
<button class="btn btn-primary">Save</button>
<button class="btn btn-danger">Delete</button>
```

```css
.btn { padding:.6rem 1rem; border-radius:.6rem; }
.btn-primary { background:#2f6fed; color:white; }
.btn-danger { background:#d13f4a; color:white; }
```

Avalonia:

```xaml
<StackPanel Orientation="Horizontal" Spacing="8">
  <Button Classes="btn primary" Content="Save" />
  <Button Classes="btn danger" Content="Delete" />
</StackPanel>

<Style Selector="Button.btn">
  <Setter Property="Padding" Value="14,9" />
  <Setter Property="CornerRadius" Value="10" />
</Style>
<Style Selector="Button.btn.primary">
  <Setter Property="Background" Value="#2F6FED" />
  <Setter Property="Foreground" Value="White" />
</Style>
<Style Selector="Button.btn.danger">
  <Setter Property="Background" Value="#D13F4A" />
  <Setter Property="Foreground" Value="White" />
</Style>
```

## C# Equivalent: Button System

```csharp
using Avalonia;
using Avalonia.Controls;
using Avalonia.Media;

var buttonRow = new StackPanel
{
    Orientation = Avalonia.Layout.Orientation.Horizontal,
    Spacing = 8,
    Children =
    {
        new Button
        {
            Content = "Save",
            Padding = new Thickness(14, 9),
            CornerRadius = new CornerRadius(10),
            Background = new SolidColorBrush(Color.Parse("#2F6FED")),
            Foreground = Brushes.White
        },
        new Button
        {
            Content = "Delete",
            Padding = new Thickness(14, 9),
            CornerRadius = new CornerRadius(10),
            Background = new SolidColorBrush(Color.Parse("#D13F4A")),
            Foreground = Brushes.White
        }
    }
};
```

## AOT/Trimming Notes

- Keep style/token definitions in compiled XAML for predictable AOT behavior.
- Use typed selectors in C# where runtime-generated selector strings are avoidable.

## Troubleshooting

1. Styles appear ignored.
- Check class names, control type in selector, and style load order.

2. Theme swap updates only some controls.
- Ensure brushes are consumed through `DynamicResource`, not literal values.

3. Variant-specific templates fail.
- Move template-level differences to `ControlTheme` instead of only setter-based styles.
