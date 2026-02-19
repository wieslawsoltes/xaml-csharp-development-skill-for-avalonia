# HTML/CSS Color Input and Spectrum UX to Avalonia `ColorPicker` and `ColorView`

## Table of Contents
1. Scope and APIs
2. Mapping Table
3. Basic Color Input Pattern
4. Advanced Spectrum and Alpha Pattern
5. Conversion Example: Theme Accent Editor
6. C# Equivalent: Theme Accent Editor
7. AOT/Threading Notes
8. Troubleshooting

## Scope and APIs

Primary APIs:

- `ColorPicker` (`Color`, `ColorChanged`, content alignment/template support)
- `ColorView` (`Color`, `ColorChanged`, `IsAlphaEnabled`, `IsColorSpectrumVisible`, `IsColorPaletteVisible`)
- `ColorView` advanced display options:
  - `ColorModel`, `ColorSpectrumComponents`, `ColorSpectrumShape`
  - `IsColorPreviewVisible`, `IsColorComponentsVisible`, `IsColorModelVisible`

Reference docs:

- [`02-html-css-selectors-cascade-variables-and-theming.md`](02-html-css-selectors-cascade-variables-and-theming)
- [`07-html-css-design-system-utilities-and-component-variants.md`](07-html-css-design-system-utilities-and-component-variants)
- [`controls/color-picker.md`](../controls/color-picker)
- [`controls/color-view.md`](../controls/color-view)

## Mapping Table

| HTML/CSS idiom | Avalonia mapping |
|---|---|
| `<input type="color">` | `ColorPicker` |
| custom hue/saturation/alpha panel | `ColorView` |
| CSS custom property `--accent` | bind Avalonia resource/VM color property |
| preview swatch `<div style="background: var(--accent)">` | `Border Background="{Binding AccentBrush}"` |

## Basic Color Input Pattern

HTML/CSS:

```html
<label for="accent">Accent</label>
<input id="accent" type="color" value="#2f6fed" />
```

```css
.preview {
  inline-size: 40px;
  block-size: 40px;
  border-radius: 8px;
  background: var(--accent);
}
```

Avalonia:

```xaml
<StackPanel Spacing="8">
  <ColorPicker Color="{CompiledBinding AccentColor, Mode=TwoWay}" />
  <Border Width="40"
          Height="40"
          CornerRadius="8"
          Background="{CompiledBinding AccentBrush}" />
</StackPanel>
```

## Advanced Spectrum and Alpha Pattern

For web UIs that include HSVA panels and alpha controls, `ColorView` gives the equivalent out of the box.

```xaml
<ColorView Color="{CompiledBinding AccentColor, Mode=TwoWay}"
           IsAlphaEnabled="True"
           IsColorSpectrumVisible="True"
           IsColorPaletteVisible="True"
           IsColorPreviewVisible="True"
           IsColorComponentsVisible="True"
           IsColorModelVisible="True"
           IsColorSpectrumSliderVisible="True" />
```

## Conversion Example: Theme Accent Editor

```html
<section class="theme-editor">
  <h3>Theme Accent</h3>
  <input type="color" value="#ff6a00" />
  <div class="swatch"></div>
</section>
```

```css
.theme-editor {
  display: grid;
  gap: 8px;
  max-inline-size: 360px;
}
.swatch {
  inline-size: 100%;
  block-size: 28px;
  border-radius: 8px;
  background: linear-gradient(90deg, var(--accent), #ffffff);
}
```

```xaml
<StackPanel Spacing="8" MaxWidth="360">
  <TextBlock Text="Theme Accent" />

  <ColorPicker Color="{CompiledBinding AccentColor, Mode=TwoWay}" />

  <ColorView Color="{CompiledBinding AccentColor, Mode=TwoWay}"
             IsAlphaEnabled="True"
             IsColorSpectrumVisible="True"
             IsColorPaletteVisible="True" />

  <Border Height="28"
          CornerRadius="8"
          Background="{CompiledBinding AccentBrush}" />
</StackPanel>
```

## C# Equivalent: Theme Accent Editor

```csharp
using Avalonia.Controls;
using Avalonia.Media;

var accentPicker = new ColorPicker
{
    Color = Color.Parse("#FF6A00")
};

var accentView = new ColorView
{
    Color = accentPicker.Color,
    IsAlphaEnabled = true,
    IsColorSpectrumVisible = true,
    IsColorPaletteVisible = true
};

var swatch = new Border
{
    Height = 28,
    CornerRadius = new CornerRadius(8),
    Background = new SolidColorBrush(accentPicker.Color)
};

accentPicker.ColorChanged += (_, e) =>
{
    accentView.Color = e.NewColor;
    swatch.Background = new SolidColorBrush(e.NewColor);
};

accentView.ColorChanged += (_, e) =>
{
    accentPicker.Color = e.NewColor;
    swatch.Background = new SolidColorBrush(e.NewColor);
};

var panel = new StackPanel { Spacing = 8, MaxWidth = 360 };
panel.Children.Add(new TextBlock { Text = "Theme Accent" });
panel.Children.Add(accentPicker);
panel.Children.Add(accentView);
panel.Children.Add(swatch);
```

## AOT/Threading Notes

- Keep color as typed `Color` (plus derived brushes) in the VM; avoid string parsing in hot paths.
- If theme resources are updated from background workflows, apply resource mutations on `Dispatcher.UIThread`.

## Troubleshooting

1. Color picker renders without advanced controls.
- Use `ColorView` when you need spectrum/palette/model UI beyond basic pickers.

2. Alpha channel seems ignored in previews.
- Ensure preview brush and consuming style paths do not coerce opacity to 1.0.

3. Theme updates lag after color selection.
- Update shared resources or VM state in one place, then let bindings propagate.
