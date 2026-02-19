# WinForms OwnerDraw, GDI, and Custom Rendering to Avalonia

## Table of Contents
1. Scope and APIs
2. Rendering Model Mapping
3. Conversion Example
4. C# Equivalent
5. Troubleshooting

## Scope and APIs

Primary WinForms APIs:

- `OnPaint(PaintEventArgs)`
- `Graphics` drawing calls
- `DoubleBuffered`
- owner-draw control events

Primary Avalonia APIs:

- `Control.Render(DrawingContext context)`
- `DrawingContext` primitives (`DrawRectangle`, `DrawLine`, `DrawText`)
- styles/templates for non-custom drawing cases

## Rendering Model Mapping

| WinForms | Avalonia |
|---|---|
| `OnPaint` override | `Render(DrawingContext)` override |
| `Graphics` | `DrawingContext` |
| `Invalidate()` | `InvalidateVisual()` |
| owner-draw list item handlers | data templates + styles, custom render only if needed |

## Conversion Example

WinForms C#:

```csharp
public sealed class MeterControl : Control
{
    public int Value { get; set; }

    protected override void OnPaint(PaintEventArgs e)
    {
        base.OnPaint(e);

        e.Graphics.Clear(Color.Black);
        e.Graphics.FillRectangle(Brushes.LimeGreen, 4, 4, Value * 2, Height - 8);
        e.Graphics.DrawRectangle(Pens.Gray, 4, 4, Width - 8, Height - 8);
    }
}
```

Avalonia XAML:

```xaml
<local:MeterControl xmlns="https://github.com/avaloniaui"
                    xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
                    xmlns:local="using:MyApp.Controls"
                    Value="64"
                    Width="220"
                    Height="24" />
```

## C# Equivalent

```csharp
using System;
using Avalonia;
using Avalonia.Controls;
using Avalonia.Media;

public sealed class MeterControl : Control
{
    static MeterControl()
    {
        AffectsRender<MeterControl>(ValueProperty);
    }

    public static readonly StyledProperty<int> ValueProperty =
        AvaloniaProperty.Register<MeterControl, int>(nameof(Value), 0);

    public int Value
    {
        get => GetValue(ValueProperty);
        set => SetValue(ValueProperty, value);
    }

    public override void Render(DrawingContext context)
    {
        base.Render(context);

        var bounds = Bounds;
        var inner = new Rect(4, 4, Math.Max(0, bounds.Width - 8), Math.Max(0, bounds.Height - 8));
        var fillWidth = Math.Clamp(Value, 0, 100) / 100.0 * inner.Width;

        context.FillRectangle(Brushes.Black, bounds);
        context.FillRectangle(Brushes.LimeGreen, new Rect(inner.X, inner.Y, fillWidth, inner.Height));
        context.DrawRectangle(null, new Pen(Brushes.Gray, 1), inner);
    }
}
```

## Troubleshooting

1. Custom control flickers after migration.
- avoid per-frame allocation and prefer immutable brushes/pens.

2. Owner-draw logic is too broad.
- use templates/styles for standard visuals and custom rendering only where required.

3. Render output does not react to property changes.
- register render-affecting properties with `AffectsRender<T>(...)` (or call `InvalidateVisual()` from a change handler).
