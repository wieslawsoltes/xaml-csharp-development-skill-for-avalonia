# WPF Rendering System (`Visual`, `OnRender`, `DrawingVisual`) to Avalonia Render Pipeline

## Table of Contents
1. Scope and APIs
2. How WPF Rendering Actually Runs
3. How Avalonia Rendering Actually Runs
4. Concept Mapping (WPF -> Avalonia)
5. Migration Strategy
6. `OnRender` Migration Example
7. Adorner/Overlay Migration Example
8. Advanced Interop: `ICustomDrawOperation`
9. Do/Don't
10. Troubleshooting

## Scope and APIs

Primary WPF APIs:

- `UIElement.OnRender(DrawingContext)`
- `DrawingVisual`, `VisualCollection`, `RenderOpen()`
- `Adorner`, `AdornerLayer`, `AdornerDecorator`
- `InvalidateVisual()`
- `CompositionTarget.Rendering` (frame-driven callback patterns)

Primary Avalonia APIs:

- `Control.Render(DrawingContext)`
- `Visual.InvalidateVisual()`, `AffectsRender<T>(...)` in derived controls
- `AdornerLayer`, `AdornerLayer.SetAdorner`, `AdornerLayer.GetAdornerLayer`
- `DrawingContext.Custom(ICustomDrawOperation)` for low-level drawing interop
- animations/transitions or `DispatcherTimer` for frame-like updates when required

## How WPF Rendering Actually Runs

WPF render flow (high level):

1. Layout updates produce final visual bounds.
2. Dirty visuals are repainted during render traversal.
3. `OnRender` emits draw instructions into the retained scene.
4. `DrawingVisual` trees can be used for low-level retained drawing structures.
5. `CompositionTarget.Rendering` is commonly used for per-frame updates.

Migration implications:

- many legacy `CompositionTarget.Rendering` loops can become declarative animations,
- `DrawingVisual` heavy architectures usually migrate better to custom controls or scene operations,
- ensure invalidation granularity is preserved to avoid over-rendering.

## How Avalonia Rendering Actually Runs

Avalonia render flow:

1. `InvalidateVisual()` marks visual nodes dirty.
2. Layout pass runs first if invalid.
3. `Render(DrawingContext)` emits draw commands for dirty visuals.
4. Renderer/compositor submits scene updates to the active backend.

Practical migration notes:

- custom rendering ports cleanly via `Render`,
- avoid forcing repaint synchronously,
- prefer style/template-driven visuals first, custom draw second.

## Concept Mapping (WPF -> Avalonia)

| WPF | Avalonia |
|---|---|
| `OnRender(DrawingContext)` | `Render(DrawingContext)` |
| `InvalidateVisual()` | `InvalidateVisual()` |
| `DrawingVisual` graph for custom retained drawing | custom `Control` rendering, compositor visuals, or `ICustomDrawOperation` for low-level paths |
| `AdornerLayer` | `AdornerLayer` with attached adorner APIs |
| `CompositionTarget.Rendering` loop | animations/transitions; `DispatcherTimer` + `InvalidateVisual` for explicit loops |

## Migration Strategy

1. Move presentation state out of paint callbacks into properties/viewmodels.
2. Replace trigger-heavy brush swaps with styles/pseudo-classes when possible.
3. Keep `Render` logic deterministic and allocation-light.
4. Port adorner overlays with explicit `AdornerLayer` attachment.
5. Use `ICustomDrawOperation` only for integration scenarios that truly need it.

## `OnRender` Migration Example

WPF C#:

```csharp
public sealed class SignalMeter : Control
{
    public double Level { get; set; }

    protected override void OnRender(DrawingContext drawingContext)
    {
        base.OnRender(drawingContext);

        var bounds = new Rect(0, 0, ActualWidth, ActualHeight);
        drawingContext.DrawRectangle(Brushes.Black, null, bounds);
        drawingContext.DrawRectangle(Brushes.LimeGreen, null, new Rect(4, 4, Math.Max(0, Level) * (ActualWidth - 8), ActualHeight - 8));
    }
}
```

Avalonia XAML:

```xaml
<local:SignalMeter xmlns="https://github.com/avaloniaui"
                   xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
                   xmlns:local="using:MyApp.Controls"
                   Width="220"
                   Height="24"
                   Level="{Binding ProgressRatio}" />
```

Avalonia C#:

```csharp
using System;
using Avalonia;
using Avalonia.Controls;
using Avalonia.Media;

public sealed class SignalMeter : Control
{
    static SignalMeter()
    {
        AffectsRender<SignalMeter>(LevelProperty);
    }

    public static readonly StyledProperty<double> LevelProperty =
        AvaloniaProperty.Register<SignalMeter, double>(nameof(Level), 0.0);

    public double Level
    {
        get => GetValue(LevelProperty);
        set => SetValue(LevelProperty, value);
    }

    public override void Render(DrawingContext context)
    {
        base.Render(context);

        var clamped = Math.Clamp(Level, 0.0, 1.0);
        var inner = new Rect(4, 4, Math.Max(0, Bounds.Width - 8), Math.Max(0, Bounds.Height - 8));

        context.FillRectangle(Brushes.Black, Bounds);
        context.FillRectangle(Brushes.LimeGreen, new Rect(inner.X, inner.Y, inner.Width * clamped, inner.Height));
        context.DrawRectangle(null, new Pen(Brushes.Gray, 1), inner);
    }
}
```

## Adorner/Overlay Migration Example

WPF XAML:

```xaml
<TextBox Text="{Binding Email, UpdateSourceTrigger=PropertyChanged}" />
```

WPF C# (conceptual):

```csharp
var layer = AdornerLayer.GetAdornerLayer(emailTextBox);
layer?.Add(new ValidationAdorner(emailTextBox));
```

Avalonia XAML:

```xaml
<UserControl xmlns="https://github.com/avaloniaui"
             xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml">
  <TextBox x:Name="EmailBox"
           Width="260"
           Text="{Binding Email}">
    <AdornerLayer.Adorner>
      <Border IsVisible="{Binding HasEmailError}"
              Background="#A0FF3B30"
              IsHitTestVisible="False">
        <TextBlock Margin="6,2" Text="{Binding EmailError}" />
      </Border>
    </AdornerLayer.Adorner>
  </TextBox>
</UserControl>
```

Avalonia C#:

```csharp
using Avalonia.Controls;
using Avalonia.Controls.Primitives;
using Avalonia.Media;

var emailBox = new TextBox { Width = 260 };
var errorOverlay = new Border
{
    Background = new SolidColorBrush(Color.Parse("#A0FF3B30")),
    IsHitTestVisible = false,
    Child = new TextBlock { Text = "Invalid email", Margin = new Avalonia.Thickness(6, 2) }
};

AdornerLayer.SetAdorner(emailBox, errorOverlay);
```

## Advanced Interop: `ICustomDrawOperation`

For custom native rendering integration:

1. implement `ICustomDrawOperation` (`Bounds`, `HitTest`, `Render`, `Dispose`),
2. enqueue it from `Render` using `context.Custom(...)`,
3. keep bounds and lifetime strict to prevent stale draw nodes.

Use this for advanced scenarios, not for normal control styling.

## Do/Don't

- Do migrate `OnRender` to `Render` with `AffectsRender` on relevant properties.
- Do move recurring frame logic to animations where possible.
- Do keep adorner overlays non-interactive unless intentional (`IsHitTestVisible=False`).
- Don't replicate WPF render-loop patterns blindly.
- Don't use low-level custom draw operations when templates/styles solve the requirement.
- Don't trigger layout invalidation for paint-only changes.

## Troubleshooting

1. Render logic updates but UI does not repaint.
- Ensure property changes call `AffectsRender` or explicitly call `InvalidateVisual`.

2. Overlay/adorner blocks input unexpectedly.
- Set adorner visuals to `IsHitTestVisible="False"` unless interactive behavior is required.

3. Ported render loop consumes too much CPU.
- reduce invalidation frequency, cache expensive geometry, and prefer built-in animations for interpolation.
