# HTML/CSS Units, `calc()`, `clamp()`, and Fluid Sizing Patterns in Avalonia

## Table of Contents
1. Scope and APIs
2. Unit Mapping (`px`, `rem`, `%`, viewport)
3. `calc()` and Derived Sizing Patterns
4. `clamp()` and Fluid Type/Layout Patterns
5. Conversion Example: Fluid Hero Layout
6. C# Equivalent: Fluid Hero Layout
7. Troubleshooting

## Scope and APIs

Primary APIs:

- sizing and constraints: `Width`, `Height`, `MinWidth`, `MaxWidth`, `MinHeight`, `MaxHeight`
- spacing: `Margin`, `Padding`, `Spacing`, `RowSpacing`, `ColumnSpacing`
- runtime adaptive logic via size observation (`Bounds`)

Reference docs:

- [`00-html-css-layout-box-model-and-positioning.md`](00-html-css-layout-box-model-and-positioning)
- [`01-html-css-flexbox-grid-and-responsive-layout-recipes.md`](01-html-css-flexbox-grid-and-responsive-layout-recipes)
- [`09-html-css-typography-fonts-text-flow-and-truncation.md`](09-html-css-typography-fonts-text-flow-and-truncation)

## Unit Mapping (`px`, `rem`, `%`, viewport)

| CSS unit idiom | Avalonia mapping |
|---|---|
| `px` | device-independent pixel values (numeric XAML values) |
| `rem` | tokenized numeric resources (for consistent typographic scale) |
| `%` width/height | star sizing (`*`) in `Grid` + alignment constraints |
| `vw` / `vh` | root bounds-driven adaptive logic |

HTML/CSS:

```html
<section class="panel">...</section>
```

```css
.panel { width: 50%; padding: 1rem; }
```

Avalonia:

```xaml
<Grid ColumnDefinitions="*,*">
  <Border Grid.Column="0" Padding="16" />
</Grid>
```

## `calc()` and Derived Sizing Patterns

HTML/CSS:

```html
<main class="main">...</main>
```

```css
.main { width: calc(100% - 280px); }
```

Avalonia equivalent:

- model layout directly with columns rather than manual subtraction.

```xaml
<Grid ColumnDefinitions="280,*">
  <Border Grid.Column="0" Classes="sidebar" />
  <Border Grid.Column="1" Classes="main" />
</Grid>
```

For truly computed values, compute in view model or code-behind and bind.

## `clamp()` and Fluid Type/Layout Patterns

HTML/CSS:

```html
<h1 class="title">Ship UI faster</h1>
```

```css
.title { font-size: clamp(1.5rem, 2.8vw, 3rem); }
```

Avalonia pattern:

1. observe container width,
2. compute clamped size in view model,
3. bind to `FontSize`.

```csharp
static double Clamp(double v, double min, double max) => Math.Min(max, Math.Max(min, v));

double TitleFontSizeFor(double width)
{
    // Example: fluid scale with min/max caps
    return Clamp(width * 0.03, 24, 48);
}
```

## Conversion Example: Fluid Hero Layout

```html
<section class="hero">
  <div class="copy">
    <h1>Ship UI faster</h1>
    <p>One codebase across targets.</p>
  </div>
  <div class="visual"></div>
</section>
```

```xaml
<Grid x:Name="Root" ColumnDefinitions="*,*" Margin="24">
  <StackPanel Grid.Column="0" Spacing="10">
    <TextBlock Text="Ship UI faster" FontSize="{CompiledBinding HeroTitleSize}" />
    <TextBlock Text="One codebase across targets." MaxWidth="520" TextWrapping="Wrap" />
  </StackPanel>
  <Border Grid.Column="1" Classes="hero-visual" />
</Grid>
```

## C# Equivalent: Fluid Hero Layout

```csharp
using System;
using Avalonia.Controls;

var root = new Grid
{
    ColumnDefinitions = ColumnDefinitions.Parse("*,*"),
    Margin = new Avalonia.Thickness(24)
};

var copy = new StackPanel { Spacing = 10 };
Grid.SetColumn(copy, 0);

var title = new TextBlock { Text = "Ship UI faster" };
copy.Children.Add(title);
copy.Children.Add(new TextBlock
{
    Text = "One codebase across targets.",
    MaxWidth = 520,
    TextWrapping = TextWrapping.Wrap
});

var visual = new Border();
Grid.SetColumn(visual, 1);

root.Children.Add(copy);
root.Children.Add(visual);

void UpdateHeroTitleSize(double width) =>
    title.FontSize = Math.Min(48, Math.Max(24, width * 0.03));
```

## Troubleshooting

1. Fluid sizing flickers during resize.
- Debounce width-driven updates.

2. `%`-style behavior seems off.
- Use explicit `Grid` star columns/rows instead of manual width math.

3. Font scale gets too large on ultrawide displays.
- Always clamp with min/max limits.
