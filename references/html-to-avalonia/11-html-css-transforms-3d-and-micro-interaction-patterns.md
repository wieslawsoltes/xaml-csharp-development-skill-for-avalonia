# HTML/CSS Transforms, 3D, and Micro-Interaction Patterns in Avalonia

## Table of Contents
1. Scope and APIs
2. Transform Mapping
3. 3D/Depth Interaction Mapping
4. State-Driven Transform Recipes
5. Conversion Example: Hoverable Product Tile
6. C# Equivalent: Hoverable Product Tile
7. Performance Notes
8. Troubleshooting

## Scope and APIs

Primary APIs:

- `RenderTransform` with transform operations
- transform transitions (`TransformOperationsTransition`)
- page/content transitions (`Rotate3DTransition` on `TransitioningContentControl.PageTransition`)
- `Animation` keyframes for transform + opacity choreography
- pseudo-class selectors (`:pointerover`, `:pressed`)

Reference docs:

- [`03-html-css-animations-transitions-and-motion-system.md`](03-html-css-animations-transitions-and-motion-system)
- [`12-animations-transitions-and-frame-loops.md`](../12-animations-transitions-and-frame-loops)

## Transform Mapping

| HTML/CSS transform | Avalonia mapping |
|---|---|
| `transform: translateY(-4px)` | `RenderTransform="translateY(-4px)"` |
| `transform: scale(1.03)` | `RenderTransform="scale(1.03)"` |
| `transform: rotate(6deg)` | `RenderTransform="rotate(6deg)"` |
| compound transforms | transform operation list in `RenderTransform` |

HTML/CSS:

```html
<article class="tile">Audio Interface</article>
```

```css
.tile { transform: translateY(0) scale(1); transition: transform .14s ease; }
.tile:hover { transform: translateY(-3px) scale(1.01); }
```

Avalonia:

```xaml
<Border Classes="tile" RenderTransform="translateY(0px) scale(1)">
  <Border.Transitions>
    <Transitions>
      <TransformOperationsTransition Property="RenderTransform" Duration="0:0:0.14" />
    </Transitions>
  </Border.Transitions>
</Border>

<Style Selector="Border.tile:pointerover">
  <Setter Property="RenderTransform" Value="translateY(-3px) scale(1.01)" />
</Style>
```

## 3D/Depth Interaction Mapping

HTML/CSS:

```html
<article class="card">...</article>
```

```css
.card:hover { transform: perspective(900px) rotateX(3deg) rotateY(-4deg); }
```

Avalonia mapping for element tilt uses 3D transform operations with `TransformOperationsTransition`.
Use `Rotate3DTransition` for page/content transitions, not as a `Transitions` property entry.

```xaml
<Border RenderTransform="rotate3d(0,1,0,0deg)">
  <Border.Transitions>
    <Transitions>
      <TransformOperationsTransition Property="RenderTransform" Duration="0:0:0.18" />
    </Transitions>
  </Border.Transitions>
</Border>
```

```xaml
<TransitioningContentControl Content="{CompiledBinding CurrentPageVm}">
  <TransitioningContentControl.PageTransition>
    <Rotate3DTransition Duration="0:0:0.18" Orientation="Horizontal" Depth="0.2" />
  </TransitioningContentControl.PageTransition>
</TransitioningContentControl>
```

## State-Driven Transform Recipes

HTML/CSS press feedback:

```css
.button:active { transform: scale(.98); }
```

Avalonia:

```xaml
<Style Selector="Button.pressable:pressed">
  <Setter Property="RenderTransform" Value="scale(0.98)" />
</Style>
```

HTML/CSS tilt + glow state:

```css
.tile:hover { transform: translateY(-2px); box-shadow: 0 12px 24px rgba(0,0,0,.3); }
```

Avalonia:

```xaml
<Style Selector="Border.tile:pointerover">
  <Setter Property="RenderTransform" Value="translateY(-2px)" />
  <Setter Property="BoxShadow" Value="0 12 24 0 #4D000000" />
</Style>
```

## Conversion Example: Hoverable Product Tile

```html
<article class="product-tile">
  <h3>Audio Interface</h3>
  <p>$249</p>
</article>
```

```xaml
<Border Classes="product-tile" RenderTransform="translateY(0px) scale(1)" Padding="12">
  <Border.Transitions>
    <Transitions>
      <TransformOperationsTransition Property="RenderTransform" Duration="0:0:0.16" />
      <BoxShadowsTransition Property="BoxShadow" Duration="0:0:0.16" />
    </Transitions>
  </Border.Transitions>

  <StackPanel Spacing="4">
    <TextBlock Text="Audio Interface" />
    <TextBlock Text="$249" FontWeight="Bold" />
  </StackPanel>
</Border>

<Style Selector="Border.product-tile:pointerover">
  <Setter Property="RenderTransform" Value="translateY(-3px) scale(1.01)" />
  <Setter Property="BoxShadow" Value="0 16 30 0 #3F000000" />
</Style>
```

## C# Equivalent: Hoverable Product Tile

```csharp
using System;
using Avalonia.Controls;
using Avalonia.Media;
using Avalonia.Animation;
using Avalonia.Animation.Transitions;

var tile = new Border
{
    Padding = new Avalonia.Thickness(12),
    RenderTransform = Avalonia.Media.TransformOperations.Parse("translateY(0px) scale(1)"),
    Transitions = new Transitions
    {
        new TransformOperationsTransition
        {
            Property = Visual.RenderTransformProperty,
            Duration = TimeSpan.FromMilliseconds(160)
        },
        new BoxShadowsTransition
        {
            Property = Border.BoxShadowProperty,
            Duration = TimeSpan.FromMilliseconds(160)
        }
    },
    Child = new StackPanel
    {
        Spacing = 4,
        Children =
        {
            new TextBlock { Text = "Audio Interface" },
            new TextBlock { Text = "$249", FontWeight = FontWeight.Bold }
        }
    }
};

tile.PointerEntered += (_, _) =>
{
    tile.RenderTransform = Avalonia.Media.TransformOperations.Parse("translateY(-3px) scale(1.01)");
    tile.BoxShadow = BoxShadows.Parse("0 16 30 0 #3F000000");
};

tile.PointerExited += (_, _) =>
{
    tile.RenderTransform = Avalonia.Media.TransformOperations.Parse("translateY(0px) scale(1)");
    tile.BoxShadow = default;
};
```

## Performance Notes

- Keep interaction transforms simple in dense lists.
- Avoid deep nested animated trees when one parent transform can do the work.

## Troubleshooting

1. Transform transition does not animate.
- Ensure `RenderTransform` value actually changes between states.

2. Interaction feels laggy.
- Reduce duration and shadow blur values for frequent pointer interactions.

3. 3D transform support differs by platform/backend.
- Keep a 2D fallback style for critical interactions.
