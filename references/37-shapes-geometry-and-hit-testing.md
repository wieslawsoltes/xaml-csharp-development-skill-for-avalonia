# Shapes, Geometry, and Hit Testing

## Table of Contents
1. Scope and APIs
2. Shape vs PathIcon vs Custom Render
3. Built-in Shape Controls
4. Geometry Construction and Reuse
5. Hit Testing and Bounds
6. Layout and Performance Notes
7. Best Practices
8. Troubleshooting

## Scope and APIs

Primary APIs:
- `Shape`
- `Path`
- `Rectangle`
- `Ellipse`
- `Line`
- `Polygon`
- `Polyline`
- `Arc`
- `Sector`
- `Shape.Fill`, `Shape.Stroke`, `Shape.StrokeThickness`, `Shape.Stretch`
- `Geometry.Parse(...)`
- `Geometry.FillContains(...)`
- `Geometry.StrokeContains(...)`
- `Geometry.GetWidenedGeometry(...)`

Reference source files:
- `src/Avalonia.Controls/Shapes/Shape.cs`
- `src/Avalonia.Controls/Shapes/Path.cs`
- `src/Avalonia.Controls/Shapes/Rectangle.cs`
- `src/Avalonia.Controls/Shapes/Ellipse.cs`
- `src/Avalonia.Controls/Shapes/Line.cs`
- `src/Avalonia.Controls/Shapes/Polygon.cs`
- `src/Avalonia.Controls/Shapes/Polyline.cs`
- `src/Avalonia.Controls/Shapes/Arc.cs`
- `src/Avalonia.Controls/Shapes/Sector.cs`
- `src/Avalonia.Base/Media/Geometry.cs`

## Shape vs PathIcon vs Custom Render

Use the right primitive:
- `PathIcon`: semantic UI icon element.
- `Shape` controls: declarative vector UI and styling.
- `Control.Render(...)`: specialized immediate-mode drawing.

Rule of thumb:
- Prefer built-in `Shape` controls for maintainable XAML and style-driven visuals.
- Drop to custom rendering only for specialized high-frequency drawing.

## Built-in Shape Controls

Common properties from `Shape`:
- `Fill`
- `Stroke`
- `StrokeThickness`
- `StrokeDashArray`
- `StrokeDashOffset`
- `StrokeLineCap`
- `StrokeJoin`
- `StrokeMiterLimit`
- `Stretch`

Specialized APIs:
- `Path.Data`
- `Rectangle.RadiusX`, `Rectangle.RadiusY`
- `Line.StartPoint`, `Line.EndPoint`
- `Polygon.Points`, `Polygon.FillRule`
- `Polyline.Points`, `Polyline.FillRule`
- `Arc.StartAngle`, `Arc.SweepAngle`
- `Sector.StartAngle`, `Sector.SweepAngle`

## Geometry Construction and Reuse

XAML path data:

```xml
<Path xmlns="https://github.com/avaloniaui"
      Stroke="Orange"
      StrokeThickness="2"
      Fill="#2200AEEF"
      Data="M 10,10 L 90,10 90,40 10,40 Z" />
```

Shared geometry resources:

```xml
<UserControl.Resources>
  <StreamGeometry x:Key="BadgeGeometry">M 0,0 L 16,0 16,16 0,16 Z</StreamGeometry>
</UserControl.Resources>

<Path Data="{StaticResource BadgeGeometry}" Fill="LimeGreen" />
```

Code construction:

```csharp
using Avalonia.Controls.Shapes;
using Avalonia.Media;

var shape = new Path
{
    Data = Geometry.Parse("M 0,0 L 24,0 12,16 Z"),
    Fill = Brushes.DodgerBlue,
    Stroke = Brushes.Navy,
    StrokeThickness = 1
};
```

## Hit Testing and Bounds

For geometry-driven interaction logic:

```csharp
var geometry = Geometry.Parse("M 0,0 L 24,0 12,16 Z");
var point = new Avalonia.Point(8, 6);

bool insideFill = geometry.FillContains(point);
bool insideStroke = geometry.StrokeContains(new Pen(Brushes.Black, 2), point);
```

Useful APIs:
- `Geometry.Bounds`
- `Geometry.GetRenderBounds(pen)`
- `Geometry.GetWidenedGeometry(pen)`

## Layout and Performance Notes

- Shape geometry is recalculated when geometry-affecting properties change.
- `StrokeThickness` affects effective geometry and often measure behavior.
- Large counts of complex paths can increase CPU/GPU cost.
- Prefer reusable geometry resources over repeated parsing.

For render-intensive scenarios, evaluate custom drawing ([`references/14-custom-drawing-text-shapes-and-skia.md`](14-custom-drawing-text-shapes-and-skia)).

## Best Practices

- Keep vector data normalized and consistent across similar visuals.
- Use `FillRule` intentionally for self-intersecting polygons/polylines.
- Avoid unnecessary frequent property churn on many shape instances.
- Use styles to centralize stroke/fill rules.
- Keep shape choice semantic (`Rectangle`/`Ellipse` over generic `Path` when possible).

## Troubleshooting

1. Shape not visible:
- Missing `Fill` and `Stroke`.
- Zero size from layout constraints.

2. Stroke looks clipped:
- Tight layout bounds with thick stroke.
- Geometry exceeds expected bounds.

3. Dash pattern not rendering as expected:
- `StrokeThickness` too small for the dash array scale.
- Dash array values too fine for current DPI/zoom.

4. Arc/Sector appears wrong direction:
- `StartAngle` + `SweepAngle` sign/units are incorrect.
- Input assumes radians instead of degrees.
