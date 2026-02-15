# ScrollViewer Offset, Anchoring, and Snap Points

## Table of Contents
1. Scope and APIs
2. Baseline `ScrollViewer` Pattern
3. Offset and Viewport Semantics
4. Scroll Methods and Programmatic Navigation
5. Attached Properties for Host Behavior
6. Snap Points and Anchoring
7. Focus-Driven Bring-Into-View
8. Practical C# Patterns
9. Best Practices
10. Troubleshooting

## Scope and APIs

Primary APIs:
- `ScrollViewer`
- `IScrollAnchorProvider`
- `ScrollChangedEventArgs`
- `ScrollBarVisibility`
- `SnapPointsType`
- `SnapPointsAlignment`

Important properties/events/methods:
- `ScrollViewer.Offset`
- `ScrollViewer.Extent`
- `ScrollViewer.Viewport`
- `ScrollViewer.ScrollBarMaximum`
- `ScrollViewer.ScrollChanged`
- `LineUp()`, `LineDown()`, `LineLeft()`, `LineRight()`
- `PageUp()`, `PageDown()`, `PageLeft()`, `PageRight()`
- `ScrollToHome()`, `ScrollToEnd()`
- `RegisterAnchorCandidate(Control)`
- `UnregisterAnchorCandidate(Control)`

Attached property surface:
- `ScrollViewer.BringIntoViewOnFocusChange`
- `ScrollViewer.HorizontalScrollBarVisibility`
- `ScrollViewer.VerticalScrollBarVisibility`
- `ScrollViewer.HorizontalSnapPointsType`
- `ScrollViewer.VerticalSnapPointsType`
- `ScrollViewer.HorizontalSnapPointsAlignment`
- `ScrollViewer.VerticalSnapPointsAlignment`
- `ScrollViewer.AllowAutoHide`
- `ScrollViewer.IsScrollChainingEnabled`
- `ScrollViewer.IsScrollInertiaEnabled`
- `ScrollViewer.IsDeferredScrollingEnabled`

Reference source files:
- `src/Avalonia.Controls/ScrollViewer.cs`
- `src/Avalonia.Controls/ScrollChangedEventArgs.cs`

## Baseline `ScrollViewer` Pattern

```xml
<ScrollViewer xmlns="https://github.com/avaloniaui"
              xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
              HorizontalScrollBarVisibility="Auto"
              VerticalScrollBarVisibility="Auto"
              AllowAutoHide="True">
  <StackPanel Spacing="8" Margin="12">
    <TextBlock Text="Scrollable content" FontWeight="Bold" />
    <Border Height="800" Background="#102060" />
  </StackPanel>
</ScrollViewer>
```

Use this as the default when content size can exceed layout bounds.

## Offset and Viewport Semantics

- `Offset` is the current scroll position (`Vector`) in content coordinates.
- `Extent` is the total scrollable content size.
- `Viewport` is the currently visible content size.
- `ScrollBarMaximum` is computed from `Extent - Viewport` and clamps to non-negative values.

Pattern:

```csharp
using Avalonia;
using Avalonia.Controls;

void RestorePosition(ScrollViewer viewer, Vector savedOffset)
{
    viewer.Offset = savedOffset;
}

Vector CapturePosition(ScrollViewer viewer) => viewer.Offset;
```

## Scroll Methods and Programmatic Navigation

`ScrollViewer` exposes imperative movement methods:

- Line: `LineUp`, `LineDown`, `LineLeft`, `LineRight`
- Page: `PageUp`, `PageDown`, `PageLeft`, `PageRight`
- Bounds: `ScrollToHome`, `ScrollToEnd`

```csharp
void ScrollOnePageDown(ScrollViewer viewer)
{
    viewer.PageDown();
}

void JumpToTop(ScrollViewer viewer)
{
    viewer.ScrollToHome();
}
```

These methods use `SetCurrentValue` internally and preserve binding relationships on `Offset`.

## Attached Properties for Host Behavior

You can tune scrolling behavior directly in XAML:

```xml
<ItemsControl xmlns="https://github.com/avaloniaui"
              xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
              ScrollViewer.HorizontalScrollBarVisibility="Disabled"
              ScrollViewer.VerticalScrollBarVisibility="Auto"
              ScrollViewer.IsScrollChainingEnabled="True"
              ScrollViewer.IsScrollInertiaEnabled="True"
              ScrollViewer.IsDeferredScrollingEnabled="False"
              ScrollViewer.AllowAutoHide="True" />
```

Guidance:
- disable horizontal scroll for list-like vertical content.
- use chaining/inertia for touch-heavy layouts.
- use deferred scrolling only when content rendering is expensive and you want thumb-drag previews.

## Snap Points and Anchoring

Snap points are controlled with attached properties:

```xml
<ItemsControl xmlns="https://github.com/avaloniaui"
              xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
              ScrollViewer.HorizontalSnapPointsType="None"
              ScrollViewer.VerticalSnapPointsType="MandatorySingle"
              ScrollViewer.VerticalSnapPointsAlignment="Near" />
```

For dynamic content where insertion/removal should preserve visible context, `ScrollViewer` also supports anchoring via `IScrollAnchorProvider` (`CurrentAnchor`, `RegisterAnchorCandidate`, `UnregisterAnchorCandidate`). This is primarily useful in custom controls/presenters.

## Focus-Driven Bring-Into-View

`BringIntoViewOnFocusChange` determines whether focus transitions auto-scroll focused elements into view.

```xml
<ScrollViewer xmlns="https://github.com/avaloniaui"
              xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
              BringIntoViewOnFocusChange="True">
  <StackPanel>
    <TextBox Width="240" Margin="0,0,0,500" />
    <TextBox Width="240" />
  </StackPanel>
</ScrollViewer>
```

This is generally desirable for keyboard navigation and accessibility.

## Practical C# Patterns

Observe scroll changes:

```csharp
using Avalonia.Controls;

void AttachScrollLogging(ScrollViewer viewer)
{
    viewer.ScrollChanged += (_, e) =>
    {
        // e.OffsetDelta, e.ExtentDelta, and e.ViewportDelta are useful for diagnostics.
        _ = e.Offset;
    };
}
```

Restore last position after loading:

```csharp
using Avalonia;
using Avalonia.Controls;

void RestoreAfterLoad(ScrollViewer viewer, Vector previousOffset)
{
    viewer.Offset = previousOffset;
}
```

## Best Practices

- Prefer declarative attached-property configuration for host controls.
- Persist and restore `Offset` for navigation-heavy views.
- Keep `BringIntoViewOnFocusChange` enabled unless you intentionally own focus scrolling.
- Use snap points only when item geometry is predictable.
- Use `ScrollChanged` for diagnostics and state sync, not heavy compute work.

## Troubleshooting

1. Scrollbars never appear.
- Verify content actually exceeds viewport and visibility is not `Disabled`.

2. Scroll jumps after item insertion.
- Use anchor-aware item layouts and avoid forcing `Offset` on every collection change.

3. Keyboard focus moves but viewport does not follow.
- Check `BringIntoViewOnFocusChange` on the effective `ScrollViewer`.

4. Touch scrolling feels wrong on nested scrollers.
- Audit `IsScrollChainingEnabled` and `IsScrollInertiaEnabled` on parent/child surfaces.

5. Binding to `Offset` breaks after imperative scroll calls.
- Use built-in methods (`LineDown`, `PageDown`, etc.) or `SetCurrentValue`-equivalent flows.
