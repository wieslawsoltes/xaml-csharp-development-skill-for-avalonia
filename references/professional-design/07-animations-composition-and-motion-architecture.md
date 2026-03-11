# Animations, Composition, and Motion Architecture in Avalonia

## Table of Contents
1. Scope and Primary APIs
2. Motion Rules
3. Transition and Page-Transition Recipes
4. Composition Animation Recipe
5. Choosing Transitions vs Keyframes vs Composition
6. AOT and Runtime Notes
7. Do and Don't Guidance
8. Troubleshooting
9. Official Resources

## Scope and Primary APIs

Use this reference to move from basic hover polish to motion architecture that feels intentional.

Primary APIs:
- `Transitions`, `DoubleTransition`, `TransformOperationsTransition`, `BrushTransition`
- `Animation`, `KeyFrame`, `Cue`
- `TransitioningContentControl`
- `IPageTransition`, `CrossFade`, `PageSlide`, `CompositePageTransition`
- `ElementComposition`, `Compositor`
- `ExpressionAnimation`, `ImplicitAnimationCollection`
- `Compositor.CreateVector3KeyFrameAnimation()`, `Compositor.CreateScalarKeyFrameAnimation()`

## Motion Rules

Motion should communicate one of four things:

1. Relationship
- how one surface relates to another during navigation or reveal.

2. Confirmation
- that an interaction was accepted.

3. Emphasis
- which surface is currently active or elevated.

4. Continuity
- how content changed without feeling disconnected.

Practical timing guidance:
- micro feedback: about `120-180ms`,
- overlays and panel reveals: about `160-220ms`,
- page or large-surface transitions: about `180-260ms`.

Reduce motion when:
- the UI updates frequently,
- the surface is data-dense,
- the same movement would repeat many times in a session.

## Transition and Page-Transition Recipes

Use transitions for simple state changes and page transitions for view swaps.

```xml
<Border xmlns="https://github.com/avaloniaui"
        xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
        Classes="interactive-card"
        Opacity="0.96"
        RenderTransform="translateY(0px)">
  <Border.Transitions>
    <Transitions>
      <TransformOperationsTransition Property="RenderTransform" Duration="0:0:0.16" />
      <DoubleTransition Property="Opacity" Duration="0:0:0.16" />
    </Transitions>
  </Border.Transitions>
</Border>
```

```xml
<CompositePageTransition xmlns="https://github.com/avaloniaui"
                         xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
                         x:Key="ShellPageTransition">
  <CompositePageTransition.PageTransitions>
    <PageSlide Duration="0:0:0.2" Orientation="Horizontal" />
    <CrossFade Duration="0:0:0.2" />
  </CompositePageTransition.PageTransitions>
</CompositePageTransition>

<TransitioningContentControl PageTransition="{StaticResource ShellPageTransition}"
                             Content="{CompiledBinding CurrentPage}" />
```

## Composition Animation Recipe

Use composition when you need smoother, higher-frequency, or shell-level motion with less UI-thread churn.

```csharp
using System;
using System.Numerics;
using Avalonia.Rendering.Composition;

var visual = ElementComposition.GetElementVisual(CardHost)!;
var compositor = visual.Compositor;

var slide = compositor.CreateVector3KeyFrameAnimation();
slide.InsertKeyFrame(0f, new Vector3(0, 8, 0));
slide.InsertKeyFrame(1f, new Vector3(0, 0, 0));
slide.Duration = TimeSpan.FromMilliseconds(180);

var fade = compositor.CreateScalarKeyFrameAnimation();
fade.InsertKeyFrame(0f, 0.88f);
fade.InsertKeyFrame(1f, 1f);
fade.Duration = TimeSpan.FromMilliseconds(180);

visual.StartAnimation("Offset", slide);
visual.StartAnimation("Opacity", fade);

var center = compositor.CreateExpressionAnimation(
    "Vector3(this.Target.Size.X * 0.5, this.Target.Size.Y * 0.5, 1)");
visual.StartAnimation("CenterPoint", center);
```

Use composition for:
- shell reveals,
- teaching surfaces,
- custom visuals,
- rich pointer or gesture feedback,
- effects that would otherwise cause heavy layout churn.

## Choosing Transitions vs Keyframes vs Composition

Use transitions when:
- a property changes because state changed,
- the effect is short and local,
- selector-driven XAML keeps the behavior readable.

Use keyframe `Animation` when:
- the sequence is choreographed,
- multiple properties must coordinate,
- the effect is still UI-thread friendly.

Use composition when:
- the motion is shell-level or high-frequency,
- a custom visual or child composition visual is involved,
- you need smoother visual continuity without large control-tree updates.

## AOT and Runtime Notes

- Keep XAML transitions and page transitions in compiled markup by default.
- Use composition from code for hotspots rather than moving all animation logic into code-behind.
- Detach custom composition visuals when the host leaves the visual tree.

## Do and Don't Guidance

Do:
- pick one motion grammar for the app,
- animate hierarchy, not everything,
- prefer composition for expensive shell effects.

Do not:
- animate dense lists just to make them feel lively,
- use long easing-heavy choreography for routine commands,
- mix unrelated motion styles across dialogs, flyouts, and pages.

## Troubleshooting

1. Motion feels expensive.
- Reduce animated properties, shorten duration, and move shell effects to composition.

2. Page transitions feel disconnected.
- Pair slide and fade only when both communicate continuity; otherwise use a simpler transition.

3. Composition animation fails silently.
- Check the target property string and ensure the visual belongs to the current compositor.

## Official Resources

- Avalonia transitions: [docs.avaloniaui.net/docs/guides/graphics-and-animation/transitions](https://docs.avaloniaui.net/docs/guides/graphics-and-animation/transitions)
- Avalonia `TransitioningContentControl` API: [api-docs.avaloniaui.net/docs/T_Avalonia_Controls_TransitioningContentControl](https://api-docs.avaloniaui.net/docs/T_Avalonia_Controls_TransitioningContentControl)
- Avalonia `CompositePageTransition` API: [api-docs.avaloniaui.net/docs/T_Avalonia_Animation_CompositePageTransition](https://api-docs.avaloniaui.net/docs/T_Avalonia_Animation_CompositePageTransition)
- Avalonia `Compositor` API: [api-docs.avaloniaui.net/docs/T_Avalonia_Rendering_Composition_Compositor](https://api-docs.avaloniaui.net/docs/T_Avalonia_Rendering_Composition_Compositor)
- Avalonia `ElementComposition` API: [api-docs.avaloniaui.net/docs/T_Avalonia_Rendering_Composition_ElementComposition](https://api-docs.avaloniaui.net/docs/T_Avalonia_Rendering_Composition_ElementComposition)
- Avalonia `ExpressionAnimation` API: [api-docs.avaloniaui.net/docs/T_Avalonia_Rendering_Composition_Animations_ExpressionAnimation](https://api-docs.avaloniaui.net/docs/T_Avalonia_Rendering_Composition_Animations_ExpressionAnimation)
- Avalonia `ImplicitAnimationCollection` API: [api-docs.avaloniaui.net/docs/T_Avalonia_Rendering_Composition_Animations_ImplicitAnimationCollection](https://api-docs.avaloniaui.net/docs/T_Avalonia_Rendering_Composition_Animations_ImplicitAnimationCollection)
- Fluent 2 motion: [fluent2.microsoft.design/motion](https://fluent2.microsoft.design/motion)
- Touch interactions for Windows apps: [learn.microsoft.com/en-us/windows/apps/design/input/touch-interactions](https://learn.microsoft.com/en-us/windows/apps/design/input/touch-interactions)
