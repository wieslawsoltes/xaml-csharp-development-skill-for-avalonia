# WPF OnRender, DrawingVisual, Adorner, and Custom Rendering to Avalonia

## Table of Contents
1. Scope and APIs
2. Rendering Mapping
3. Conversion Example
4. Avalonia C# Equivalent
5. Troubleshooting

## Scope and APIs

Primary WPF APIs:

- `OnRender(DrawingContext)`
- `DrawingVisual`
- `Adorner`/`AdornerLayer`

Primary Avalonia APIs:

- `Control.Render(DrawingContext)`
- custom draw via `DrawingContext`
- `AdornerLayer` and overlay patterns

## Rendering Mapping

| WPF | Avalonia |
|---|---|
| `OnRender` custom control draw | `Render(DrawingContext)` |
| `DrawingVisual` scene helpers | custom controls/compositor visuals (no direct public `DrawingVisual` control API) |
| `AdornerLayer.GetAdornerLayer(...)` | `AdornerLayer` overlay patterns |

## Conversion Example

WPF C#:

```csharp
protected override void OnRender(DrawingContext dc)
{
    base.OnRender(dc);
    dc.DrawRectangle(Brushes.Black, null, new Rect(0, 0, ActualWidth, ActualHeight));
}
```

Avalonia XAML:

```xaml
<local:OverlayMeter xmlns="https://github.com/avaloniaui"
                    xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
                    xmlns:local="using:MyApp.Controls"
                    Width="220"
                    Height="24" />
```

## Avalonia C# Equivalent

```csharp
using Avalonia;
using Avalonia.Controls;
using Avalonia.Media;

public sealed class OverlayMeter : Control
{
    public override void Render(DrawingContext context)
    {
        base.Render(context);
        context.FillRectangle(Brushes.Black, Bounds);
        context.DrawRectangle(null, new Pen(Brushes.Gray, 1), new Rect(0, 0, Bounds.Width, Bounds.Height));
    }
}
```

Adorner layer usage should be constrained to focused overlays and validation/focus visuals.

## Troubleshooting

1. rendering is blurry or clipped.
- validate bounds math and keep drawing inside `Bounds`.

2. adorner overlays intercept input unexpectedly.
- ensure overlay hit testing behavior matches intended UX.

3. heavy redraw paths stutter.
- cache static geometry/brushes and limit invalidation frequency.
