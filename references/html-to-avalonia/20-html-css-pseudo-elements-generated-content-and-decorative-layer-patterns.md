# HTML/CSS Pseudo-Elements, Generated Content, and Decorative Layer Patterns in Avalonia

## Table of Contents
1. Scope and APIs
2. `::before`/`::after` Mapping
3. Decorative Badge/Indicator Mapping
4. Generated Content Alternatives
5. Conversion Example: Pseudo-Element Card Accent
6. C# Equivalent: Pseudo-Element Card Accent
7. Troubleshooting

## Scope and APIs

Primary APIs:

- layered composition using `Grid`, `Border`, and `ZIndex`
- text decoration and inline runs (`TextBlock`, `Run`, `Span`)
- templates/styles for reusable decorative structures

Reference docs:

- [`00-html-css-layout-box-model-and-positioning.md`](00-html-css-layout-box-model-and-positioning)
- [`02-html-css-selectors-cascade-variables-and-theming.md`](02-html-css-selectors-cascade-variables-and-theming)
- [`10-html-css-backgrounds-gradients-shadows-and-glass-patterns.md`](10-html-css-backgrounds-gradients-shadows-and-glass-patterns)

## `::before`/`::after` Mapping

HTML/CSS pseudo-element:

```html
<article class="card">...</article>
```

```css
.card::before {
  content: "";
  position: absolute;
  inset: 0;
  border: 1px solid rgba(255,255,255,.16);
}
```

Avalonia mapping:

```xaml
<Grid>
  <Border Classes="card" />
  <Border Classes="card-outline" IsHitTestVisible="False" ZIndex="1" />
</Grid>
```

## C# Equivalent: Pseudo-Element Card Accent

```csharp
using Avalonia.Controls;
using Avalonia.Media;

var cardLayer = new Grid();

var baseCard = new Border();

var accent = new Border
{
    Width = 4,
    HorizontalAlignment = Avalonia.Layout.HorizontalAlignment.Left,
    VerticalAlignment = Avalonia.Layout.VerticalAlignment.Stretch,
    Background = new SolidColorBrush(Color.Parse("#4F8CFF")),
    ZIndex = 1,
    IsHitTestVisible = false
};

cardLayer.Children.Add(baseCard);
cardLayer.Children.Add(accent);
```

## Decorative Badge/Indicator Mapping

CSS badge bubble often maps to explicit overlay element:

```xaml
<Grid>
  <Button Content="Inbox" />
  <Border HorizontalAlignment="Right"
          VerticalAlignment="Top"
          Margin="0,-4,-4,0"
          Width="18" Height="18" CornerRadius="9"
          Background="#E53935">
    <TextBlock Text="3" FontSize="10" HorizontalAlignment="Center" VerticalAlignment="Center" />
  </Border>
</Grid>
```

## Generated Content Alternatives

| CSS generated content | Avalonia alternative |
|---|---|
| `content: "New"` | explicit `TextBlock`/`Run` |
| icon via `content` | `PathIcon`/`Image` + layout container |
| separator via `::after` | dedicated visual element (`Border`/`Rectangle`) |

## Conversion Example: Pseudo-Element Card Accent

HTML/CSS:

```html
<article class="card">...</article>
```

```css
.card::after {
  content: "";
  position: absolute;
  left: 0;
  top: 0;
  width: 4px;
  height: 100%;
  background: #4f8cff;
}
```

Avalonia:

```xaml
<Grid>
  <Border Classes="card" />
  <Border Width="4"
          HorizontalAlignment="Left"
          VerticalAlignment="Stretch"
          Background="#4F8CFF"
          ZIndex="1" />
</Grid>
```

## Troubleshooting

1. Decorative layers intercept pointer input.
- Set `IsHitTestVisible="False"` on non-interactive overlay visuals.

2. Pseudo-element replacement feels repetitive.
- Move decorative structure into control template or reusable style/template.

3. Layer ordering is inconsistent.
- Normalize `ZIndex` usage for base/decorative/content layers.
