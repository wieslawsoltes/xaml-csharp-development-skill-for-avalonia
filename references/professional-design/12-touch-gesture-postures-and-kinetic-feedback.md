# Touch, Gesture Postures, and Kinetic Feedback in Avalonia

## Table of Contents
1. Scope and Primary APIs
2. Posture-Aware Design Rules
3. Gesture and Pull Patterns
4. Scroll, Snap, and Inertia Rules
5. AOT and Runtime Notes
6. Do and Don't Guidance
7. Troubleshooting
8. Official Resources

## Scope and Primary APIs

Use this reference when the product must feel good under touch, pen, touchpad, and mixed-input desktop use.

Primary APIs:
- `Gestures`
- `PinchGestureRecognizer`, `ScrollGestureRecognizer`, `PullGestureRecognizer`
- `RefreshContainer`
- `ScrollViewer`
- `SnapPointsType`, `SnapPointsAlignment`
- `PointerPressedEventArgs`, `PointerReleasedEventArgs`
- `Transitions`, `TransformOperationsTransition`

This file covers:
- touch-target posture rules,
- gesture-aware motion,
- pull-to-refresh and inertial scrolling,
- feedback patterns that feel responsive without becoming noisy.

## Posture-Aware Design Rules

Design should account for how the device is being used:

- mouse and keyboard favor compact, precise layouts,
- touch favors larger targets and fewer simultaneous actions,
- touchpad and pen sit between those extremes,
- mixed-input desktop apps should not feel broken in either mode.

Rules:
- keep tap targets comfortably separated,
- avoid placing critical actions too close together in dense toolbars,
- make touch feedback immediate,
- do not require hover-only discovery for essential actions.

## Gesture and Pull Patterns

Avalonia exposes routed gesture events and recognizers for gesture-heavy surfaces.

```xml
<RefreshContainer xmlns="https://github.com/avaloniaui"
                  xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
                  PullDirection="TopToBottom">
  <ScrollViewer>
    <ItemsControl />
  </ScrollViewer>
</RefreshContainer>
```

```csharp
using Avalonia.Input;

Gestures.AddHoldingHandler(CardHost, (_, e) =>
{
    if (e is HoldingRoutedEventArgs args && args.HoldingState == HoldingState.Started)
    {
        CardHost.Classes.Add("holding");
    }
});
```

Guidance:
- use pull-to-refresh only where it matches the product model,
- keep hold and long-press behaviors discoverable or clearly secondary,
- do not overload one surface with too many gestures,
- pair gesture feedback with visible motion or status confirmation.

## Scroll, Snap, and Inertia Rules

```xml
<ListBox xmlns="https://github.com/avaloniaui"
         xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
         ScrollViewer.VerticalScrollBarVisibility="Auto"
         ScrollViewer.IsScrollInertiaEnabled="True"
         ScrollViewer.VerticalSnapPointsType="MandatorySingle"
         ScrollViewer.VerticalSnapPointsAlignment="Near" />
```

Rules:
- use inertia where scrolling should feel natural rather than mechanical,
- use snap points when the content model has meaningful stops,
- avoid nested scroll regions unless the hierarchy is obvious,
- keep motion short and physically believable when content repositions.

## AOT and Runtime Notes

- Gesture handlers and touch-friendly scroll settings are safe in normal app code and compiled XAML.
- Keep pointer, gesture, and kinetic feedback state explicit so design behavior stays testable.
- Reuse the same motion grammar for pointer and touch feedback where possible.

## Do and Don't Guidance

Do:
- design for mixed-input reality,
- keep gesture feedback visible and immediate,
- use pull, snap, and inertia only when they support the content model.

Do not:
- hide critical actions behind hover or long-press only,
- over-stack gesture types on one control,
- let touch feedback feel slower than mouse feedback.

## Troubleshooting

1. A desktop app feels awkward on touch hardware.
- Targets are likely too dense and hover states carry too much meaning.

2. Gesture-heavy surfaces feel confusing.
- Reduce the number of gestures and make the recovery path obvious.

3. Scroll motion feels wrong.
- Revisit inertia, snap points, and nested-scroller structure together.

## Official Resources

- Touch interactions for Windows apps: [learn.microsoft.com/en-us/windows/apps/design/input/touch-interactions](https://learn.microsoft.com/en-us/windows/apps/design/input/touch-interactions)
- Fluent 2 accessibility: [fluent2.microsoft.design/accessibility](https://fluent2.microsoft.design/accessibility)
- Avalonia transitions: [docs.avaloniaui.net/docs/guides/graphics-and-animation/transitions](https://docs.avaloniaui.net/docs/guides/graphics-and-animation/transitions)
