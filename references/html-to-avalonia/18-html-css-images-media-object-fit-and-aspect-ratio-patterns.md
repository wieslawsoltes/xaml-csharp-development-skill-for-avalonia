# HTML/CSS Images, Media, `object-fit`, and Aspect-Ratio Patterns in Avalonia

## Table of Contents
1. Scope and APIs
2. `object-fit` Mapping
3. Aspect Ratio Mapping
4. Background Image and Hero Media Patterns
5. Conversion Example: Card Media Header
6. C# Equivalent: Card Media Header
7. Troubleshooting

## Scope and APIs

Primary APIs:

- `Image` and `Stretch`
- clipping and scaling containers (`Border`, `Viewbox`)
- aspect-ratio helpers (`AspectRatio` custom decorator patterns)

Reference docs:

- [`00-html-css-layout-box-model-and-positioning.md`](00-html-css-layout-box-model-and-positioning)
- [`10-html-css-backgrounds-gradients-shadows-and-glass-patterns.md`](10-html-css-backgrounds-gradients-shadows-and-glass-patterns)

## `object-fit` Mapping

| CSS `object-fit` | Avalonia mapping |
|---|---|
| `cover` | `Image Stretch="UniformToFill"` |
| `contain` | `Image Stretch="Uniform"` |
| `fill` | `Image Stretch="Fill"` |
| `none` | `Image Stretch="None"` |

HTML/CSS:

```html
<div class="avatar">
  <img src="/assets/avatar.jpg" alt="User avatar">
</div>
```

```css
.avatar img { width: 100%; height: 100%; object-fit: cover; }
```

Avalonia:

```xaml
<Border Width="48" Height="48" CornerRadius="24" ClipToBounds="True">
  <Image Source="{CompiledBinding AvatarUri}" Stretch="UniformToFill" />
</Border>
```

## Aspect Ratio Mapping

HTML/CSS:

```html
<figure class="video">
  <img src="/assets/preview.jpg" alt="Video preview">
</figure>
```

```css
.video { aspect-ratio: 16 / 9; }
```

Avalonia options:

1. fixed ratio via custom decorator/panel,
2. constrained `Viewbox` composition,
3. ratio-managed height in view model.

```xaml
<local:AspectRatioDecorator AspectRatio="1.7778">
  <Image Stretch="UniformToFill" Source="{CompiledBinding PreviewImage}" />
</local:AspectRatioDecorator>
```

## Background Image and Hero Media Patterns

Web background-image hero usually maps to layered `Grid` composition:

```html
<section class="hero">
  <img src="/assets/hero.jpg" alt="">
  <div class="overlay"></div>
  <div class="copy">...</div>
</section>
```

```xaml
<Grid>
  <Image Source="{CompiledBinding HeroImage}" Stretch="UniformToFill" />
  <Border Background="#66000000" />
  <StackPanel VerticalAlignment="Bottom" Margin="24" />
</Grid>
```

## Conversion Example: Card Media Header

```xaml
<Border CornerRadius="14" ClipToBounds="True">
  <Grid RowDefinitions="180,*">
    <Image Grid.Row="0" Source="{CompiledBinding CoverImage}" Stretch="UniformToFill" />
    <StackPanel Grid.Row="1" Margin="14" Spacing="6">
      <TextBlock Text="{CompiledBinding Title}" FontWeight="Bold" />
      <TextBlock Text="{CompiledBinding Subtitle}" Opacity="0.75" />
    </StackPanel>
  </Grid>
</Border>
```

## C# Equivalent: Card Media Header

```csharp
using Avalonia;
using Avalonia.Controls;
using Avalonia.Media;

var mediaCard = new Border
{
    CornerRadius = new CornerRadius(14),
    ClipToBounds = true
};

var grid = new Grid { RowDefinitions = RowDefinitions.Parse("180,*") };

var coverImage = new Image { Stretch = Stretch.UniformToFill };
Grid.SetRow(coverImage, 0);

var textStack = new StackPanel { Margin = new Thickness(14), Spacing = 6 };
Grid.SetRow(textStack, 1);
textStack.Children.Add(new TextBlock { Text = "Card title", FontWeight = FontWeight.Bold });
textStack.Children.Add(new TextBlock { Text = "Subtitle", Opacity = 0.75 });

grid.Children.Add(coverImage);
grid.Children.Add(textStack);
mediaCard.Child = grid;
```

## Troubleshooting

1. Image crops unexpectedly.
- Verify `Stretch` mode and container clipping.

2. Aspect ratio breaks at narrow widths.
- Enforce min width/height constraints on ratio container.

3. Background media hurts scrolling performance.
- Use appropriately sized image assets and avoid oversized textures.
