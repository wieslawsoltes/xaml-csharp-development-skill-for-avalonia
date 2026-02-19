# HTML/CSS Animations, Transitions, and Motion System in Avalonia

## Table of Contents
1. Scope and APIs
2. Transition Mapping
3. Keyframe Animation Mapping
4. Easing Mapping
5. Additional CSS Animation Conversions
6. Compositor/Elevated Motion
7. Conversion Example: Interactive Card
8. C# Equivalent: Interactive Card
9. Reduced Motion Strategy
10. Troubleshooting

## Scope and APIs

Primary APIs:

- `Animatable.Transitions`
- transition types (`DoubleTransition`, `ColorTransition`, `ThicknessTransition`, `TransformOperationsTransition`, ...)
- `Animation`, `KeyFrame`, `Cue`, `RunAsync`
- `IPageTransition`, `CrossFade`, `PageSlide`, `CompositePageTransition`
- `TopLevel.RequestAnimationFrame(Action<TimeSpan>)`

Reference docs:

- [`12-animations-transitions-and-frame-loops.md`](../12-animations-transitions-and-frame-loops)
- [`15-compositor-and-custom-visuals.md`](../15-compositor-and-custom-visuals)

## Transition Mapping

| CSS transition idiom | Avalonia mapping |
|---|---|
| `transition: opacity .2s ease` | `DoubleTransition Property="Opacity" Duration="0:0:0.2"` |
| `transition: transform .16s ease-out` | `TransformOperationsTransition Property="RenderTransform" ...` |
| `transition: background-color .2s` | `ColorTransition`/`BrushTransition` depending property type |

Example:

```html
<button class="cta">Create</button>
```

```css
.cta {
  opacity: 1;
  transform: scale(1);
  transition: transform .16s ease, opacity .16s ease;
}
.cta:hover {
  transform: scale(1.03);
  opacity: .92;
}
```

```xaml
<Button Classes="cta" RenderTransform="scale(1)">
  <Button.Transitions>
    <Transitions>
      <TransformOperationsTransition Property="RenderTransform" Duration="0:0:0.16" />
      <DoubleTransition Property="Opacity" Duration="0:0:0.16" />
    </Transitions>
  </Button.Transitions>
</Button>
```

## Keyframe Animation Mapping

HTML/CSS:

```html
<article class="card">Revenue</article>
```

```css
.card { animation: fade-in-up .24s ease-out both; }
@keyframes fade-in-up {
  from { opacity: 0; transform: translateY(16px); }
  to { opacity: 1; transform: translateY(0); }
}
```

Avalonia XAML:

```xaml
<Animation x:Key="FadeInUp" Duration="0:0:0.24">
  <KeyFrame Cue="0%">
    <Setter Property="Opacity" Value="0" />
    <Setter Property="RenderTransform" Value="translateY(16px)" />
  </KeyFrame>
  <KeyFrame Cue="100%">
    <Setter Property="Opacity" Value="1" />
    <Setter Property="RenderTransform" Value="translateY(0px)" />
  </KeyFrame>
</Animation>
```

C# execution:

```csharp
var fadeIn = (Animation)Resources["FadeInUp"]!;
await fadeIn.RunAsync(MyCard);
```

## Easing Mapping

| CSS easing | Avalonia easing |
|---|---|
| `linear` | `LinearEasing` |
| `ease-in` | `SineEaseIn` / `CubicEaseIn` |
| `ease-out` | `SineEaseOut` / `CubicEaseOut` |
| `ease-in-out` | `SineEaseInOut` / `CubicEaseInOut` |
| `cubic-bezier(...)` | `CubicBezierEasing` or `SplineEasing` |
| spring-like JS libs | `SpringEasing` |

## Additional CSS Animation Conversions

CSS (staggered enter):

```css
.item {
  opacity: 0;
  transform: translateY(10px);
  animation: enter .22s ease-out forwards;
}
.item:nth-child(2) { animation-delay: .04s; }
.item:nth-child(3) { animation-delay: .08s; }
@keyframes enter {
  to { opacity: 1; transform: translateY(0); }
}
```

Avalonia approach:

1. Use a shared `Animation` resource for the enter motion.
2. Start each item animation with incremental delay in C#.

```csharp
for (var i = 0; i < items.Count; i++)
{
    var delay = TimeSpan.FromMilliseconds(i * 40);
    var anim = new Animation
    {
        Duration = TimeSpan.FromMilliseconds(220),
        Delay = delay,
        FillMode = FillMode.Forward,
        Easing = new Avalonia.Animation.Easings.CubicEaseOut(),
        Children =
        {
            new KeyFrame
            {
                Cue = new Cue(0),
                Setters = { new Avalonia.Styling.Setter(Avalonia.Visual.OpacityProperty, 0d) }
            },
            new KeyFrame
            {
                Cue = new Cue(1),
                Setters = { new Avalonia.Styling.Setter(Avalonia.Visual.OpacityProperty, 1d) }
            }
        }
    };
    _ = anim.RunAsync(items[i]);
}
```

CSS (`animation-direction: alternate; animation-iteration-count: infinite`):

```css
.pulse { animation: pulse .9s ease-in-out infinite alternate; }
```

Avalonia:

```csharp
var pulse = new Animation
{
    Duration = TimeSpan.FromMilliseconds(900),
    IterationCount = IterationCount.Infinite,
    PlaybackDirection = PlaybackDirection.Alternate,
    Easing = new Avalonia.Animation.Easings.SineEaseInOut()
};
```

## Compositor/Elevated Motion

For advanced motion (parallax, continuous visual effects), escalate to compositor APIs only after validating transition/keyframe limits.

Guideline:

1. start with `Transitions` for state changes,
2. use `Animation` for choreographed sequences,
3. use compositor/frame callbacks for high-frequency scenarios.

## Conversion Example: Interactive Card

HTML/CSS intent:

```html
<article class="card">...</article>
```

```css
.card { transition: transform .16s ease, box-shadow .16s ease; }
.card:hover { transform: translateY(-2px) scale(1.01); }
```

Avalonia:

```xaml
<Border Classes="card" RenderTransform="translateY(0) scale(1)">
  <Border.Transitions>
    <Transitions>
      <TransformOperationsTransition Property="RenderTransform" Duration="0:0:0.16" />
      <BoxShadowsTransition Property="BoxShadow" Duration="0:0:0.16" />
    </Transitions>
  </Border.Transitions>
</Border>

<Style Selector="Border.card:pointerover">
  <Setter Property="RenderTransform" Value="translateY(-2px) scale(1.01)" />
  <Setter Property="BoxShadow" Value="0 14 32 0 #40000000" />
</Style>
```

## C# Equivalent: Interactive Card

```csharp
using System;
using Avalonia;
using Avalonia.Controls;
using Avalonia.Animation;
using Avalonia.Animation.Transitions;
using Avalonia.Media;

var card = new Border
{
    RenderTransform = TransformOperations.Parse("translateY(0px) scale(1)"),
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
    }
};

card.PointerEntered += (_, _) =>
{
    card.RenderTransform = TransformOperations.Parse("translateY(-2px) scale(1.01)");
    card.BoxShadow = BoxShadows.Parse("0 14 32 0 #40000000");
};

card.PointerExited += (_, _) =>
{
    card.RenderTransform = TransformOperations.Parse("translateY(0px) scale(1)");
    card.BoxShadow = default;
};
```

## Reduced Motion Strategy

Implement motion classes and switch at runtime:

```csharp
void ApplyReducedMotion(StyledElement root, bool reduced)
{
    root.Classes.Set("reduced-motion", reduced);
}
```

```xaml
<Style Selector="*.reduced-motion Border.card">
  <Setter Property="Transitions">
    <Transitions />
  </Setter>
</Style>
```

## Troubleshooting

1. Transition does not fire.
- Ensure the property actually changes and type has a matching animator/transition type.

2. Keyframe animation throws at runtime.
- Check property type compatibility in each `Setter`.

3. High CPU during animations.
- Remove per-frame allocations and stop frame loops when off-screen/detached.
