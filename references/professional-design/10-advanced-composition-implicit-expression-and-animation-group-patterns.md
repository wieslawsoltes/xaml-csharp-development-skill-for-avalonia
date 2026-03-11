# Advanced Composition, Implicit Animations, and Expression Patterns in Avalonia

## Table of Contents
1. Scope and Primary APIs
2. Implicit Animation Pattern
3. Expression and Parameter Pattern
4. Animation Groups and Shared State
5. AOT and Runtime Notes
6. Do and Don't Guidance
7. Troubleshooting
8. Official Resources

## Scope and Primary APIs

Use this reference when basic composition recipes are not enough and the UI needs coordinated shell polish.

Primary APIs:
- `ElementComposition`, `Compositor`
- `ImplicitAnimationCollection`
- `CompositionAnimationGroup`
- `CompositionPropertySet`
- `CompositionObject.StartAnimationGroup(...)`
- `ExpressionAnimation`
- `Compositor.CreateColorKeyFrameAnimation()`, `CreateVector3KeyFrameAnimation()`, `CreateScalarKeyFrameAnimation()`
- `ExpressionAnimation.SetScalarParameter(...)`, `SetReferenceParameter(...)`, `SetVector3Parameter(...)`
- `CompositionPropertySet.InsertScalar(...)`, `InsertVector3(...)`

## Implicit Animation Pattern

Implicit animations are the right fit when property changes should animate automatically.

```csharp
using System;
using Avalonia.Rendering.Composition;

var visual = ElementComposition.GetElementVisual(CardHost)!;
var compositor = visual.Compositor;

var offsetAnimation = compositor.CreateVector3KeyFrameAnimation();
offsetAnimation.Target = "Offset";
offsetAnimation.InsertExpressionKeyFrame(1f, "this.FinalValue");
offsetAnimation.Duration = TimeSpan.FromMilliseconds(180);

var implicitAnimations = compositor.CreateImplicitAnimationCollection();
implicitAnimations["Offset"] = offsetAnimation;

visual.ImplicitAnimations = implicitAnimations;
```

Use this pattern for:
- cards that reflow,
- shell panes that slide,
- objects whose offset or scale changes often.

## Expression and Parameter Pattern

Use expression animations when the animated value should follow another value or a mathematical rule.

```csharp
using System.Numerics;
using Avalonia.Rendering.Composition;

var visual = ElementComposition.GetElementVisual(CardHost)!;
var compositor = visual.Compositor;

var center = compositor.CreateExpressionAnimation(
    "Vector3(this.Target.Size.X * 0.5, this.Target.Size.Y * 0.5, 1)");
visual.StartAnimation("CenterPoint", center);

var pulse = compositor.CreateExpressionAnimation("this.Target.Opacity * progress");
pulse.Target = "Opacity";
pulse.SetScalarParameter("progress", 0.96f);
visual.StartAnimation("Opacity", pulse);
```

Use `SetReferenceParameter(...)` and `SetVector3Parameter(...)` when the expression should depend on another composition object or vector value.

## Animation Groups and Shared State

Coordinate several animations together with `CompositionAnimationGroup`.

```csharp
using System;
using System.Numerics;
using Avalonia.Rendering.Composition;

var visual = ElementComposition.GetElementVisual(CommandSurface)!;
var compositor = visual.Compositor;

var scale = compositor.CreateVector3KeyFrameAnimation();
scale.Target = "Scale";
scale.InsertKeyFrame(0f, new Vector3(0.98f, 0.98f, 1f));
scale.InsertKeyFrame(1f, new Vector3(1f, 1f, 1f));
scale.Duration = TimeSpan.FromMilliseconds(140);

var fade = compositor.CreateScalarKeyFrameAnimation();
fade.Target = "Opacity";
fade.InsertKeyFrame(0f, 0.9f);
fade.InsertKeyFrame(1f, 1f);
fade.Duration = TimeSpan.FromMilliseconds(140);

var group = compositor.CreateAnimationGroup();
group.Add(scale);
group.Add(fade);

visual.StartAnimationGroup(group);
```

`CompositionPropertySet` exists in Avalonia `11.3.12`, but normal app code does not get a public compositor factory for creating one directly. In practice, app code usually shares animation input through `SetScalarParameter(...)`, `SetVector3Parameter(...)`, and `SetReferenceParameter(...)` on the animation itself, while `CompositionPropertySet` remains part of the underlying composition model.

## AOT and Runtime Notes

- Composition stays code-driven; keep the host surfaces and interaction states declared in XAML.
- Keep advanced composition isolated to shell hotspots rather than spreading it across routine controls.
- Treat `CompositionPropertySet` as a lower-level composition concept in Avalonia `11.3.12`; prefer the public animation parameter APIs in app code.
- Detach child visuals and stop animation groups when the host leaves the visual tree.

## Do and Don't Guidance

Do:
- use implicit animations for natural property-follow behavior,
- use expression animations for live mathematical relationships,
- coordinate groups when several properties should land together.

Do not:
- rebuild the same effect independently on many controls,
- hide weak information architecture behind elaborate motion,
- keep long-running composition objects attached after navigation.

## Troubleshooting

1. Implicit animation never runs.
- Confirm the animation `Target` is set and the property is actually changing on the composition visual.

2. Expression animation behaves unexpectedly.
- Re-check the expression string and any parameter names passed into the animation.

3. Coordinated motion feels off.
- The group may start together, but the individual durations or keyframes are still mismatched.

## Official Resources

- Avalonia `Compositor` API: [api-docs.avaloniaui.net/docs/T_Avalonia_Rendering_Composition_Compositor](https://api-docs.avaloniaui.net/docs/T_Avalonia_Rendering_Composition_Compositor)
- Avalonia `CompositionPropertySet` API: [api-docs.avaloniaui.net/docs/T_Avalonia_Rendering_Composition_CompositionPropertySet](https://api-docs.avaloniaui.net/docs/T_Avalonia_Rendering_Composition_CompositionPropertySet)
- Avalonia `CompositionAnimationGroup` API: [api-docs.avaloniaui.net/docs/T_Avalonia_Rendering_Composition_Animations_CompositionAnimationGroup](https://api-docs.avaloniaui.net/docs/T_Avalonia_Rendering_Composition_Animations_CompositionAnimationGroup)
- Avalonia `StartAnimationGroup` API: [api-docs.avaloniaui.net/docs/M_Avalonia_Rendering_Composition_CompositionObject_StartAnimationGroup](https://api-docs.avaloniaui.net/docs/M_Avalonia_Rendering_Composition_CompositionObject_StartAnimationGroup)
- Avalonia `CreateColorKeyFrameAnimation` API: [api-docs.avaloniaui.net/docs/M_Avalonia_Rendering_Composition_Compositor_CreateColorKeyFrameAnimation](https://api-docs.avaloniaui.net/docs/M_Avalonia_Rendering_Composition_Compositor_CreateColorKeyFrameAnimation)
- Avalonia `InsertScalar` API: [api-docs.avaloniaui.net/docs/M_Avalonia_Rendering_Composition_CompositionPropertySet_InsertScalar](https://api-docs.avaloniaui.net/docs/M_Avalonia_Rendering_Composition_CompositionPropertySet_InsertScalar)
- Avalonia `SetScalarParameter` API: [api-docs.avaloniaui.net/docs/M_Avalonia_Rendering_Composition_Animations_ExpressionAnimation_SetScalarParameter](https://api-docs.avaloniaui.net/docs/M_Avalonia_Rendering_Composition_Animations_ExpressionAnimation_SetScalarParameter)
