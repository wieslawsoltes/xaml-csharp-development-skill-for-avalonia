# WinForms Rendering System (WM_PAINT, GDI+/OwnerDraw) to Avalonia Render Pipeline

## Table of Contents
1. Scope and APIs
2. How WinForms Rendering Actually Runs
3. How Avalonia Rendering Actually Runs
4. Concept Mapping (WinForms -> Avalonia)
5. Migration Strategy
6. OwnerDraw Migration Example
7. Custom Paint Control Migration Example
8. Advanced Interop: `ICustomDrawOperation`
9. Do/Don't
10. Troubleshooting

## Scope and APIs

Primary WinForms APIs:

- `OnPaint(PaintEventArgs)`, `OnPaintBackground(PaintEventArgs)`
- `Graphics`, `Pen`, `Brush`, `TextRenderer`
- `Invalidate()`, `Update()`, `Refresh()`
- owner-draw hooks (`DrawItem`, `MeasureItem`, `DrawMode.OwnerDrawFixed`)
- `ControlStyles.UserPaint`, `ControlStyles.OptimizedDoubleBuffer`, `ControlStyles.AllPaintingInWmPaint`

Primary Avalonia APIs:

- `Control.Render(DrawingContext)`
- `DrawingContext` primitives (`FillRectangle`, `DrawRectangle`, `DrawText`, `DrawLine`, `PushClip`)
- `Visual.InvalidateVisual()`, `AffectsRender<T>(...)`
- `DataTemplate`, styles, pseudo-classes (`:pointerover`, `:selected`) for most owner-draw UI
- `DrawingContext.Custom(ICustomDrawOperation)` for low-level interop-only scenarios

## How WinForms Rendering Actually Runs

WinForms rendering is message-driven (`WM_PAINT`):

1. An invalid region is posted for the control.
2. `OnPaintBackground` runs (unless suppressed).
3. `OnPaint` runs with `PaintEventArgs` (`Graphics`, `ClipRectangle`).
4. Owner-draw controls raise item-level draw events.

Typical pain points in large apps:

- flicker due to background + foreground paint ordering,
- redraw storms from broad `Invalidate()` calls,
- rendering and layout logic mixed in the same code paths,
- GDI object lifetime bugs in custom paint code.

## How Avalonia Rendering Actually Runs

Avalonia rendering is visual-tree/compositor-driven:

1. `InvalidateVisual()` marks a `Visual` dirty.
2. Layout pass runs first if needed (`InvalidateMeasure`/`InvalidateArrange` were raised).
3. `Render(DrawingContext)` is called for dirty visuals.
4. Renderer/compositor submits scene updates to the platform backend.

Migration implications:

- focus on property-driven render state, not imperative paint event timing,
- use templates/styles for the majority of owner-draw UI,
- reserve custom `Render` for truly custom visuals or hot rendering paths.

## Concept Mapping (WinForms -> Avalonia)

| WinForms | Avalonia |
|---|---|
| `OnPaint` | `Render(DrawingContext)` |
| `OnPaintBackground` | style/template background, or first step in `Render` |
| `Invalidate()` | `InvalidateVisual()` |
| `Refresh()` (`Invalidate` + sync repaint) | `InvalidateVisual()`; avoid forcing sync render |
| owner-draw events (`DrawItem`) | `DataTemplate` + style selectors/pseudo-classes |
| `ControlStyles.OptimizedDoubleBuffer` | compositor pipeline already buffers rendering |
| clip rectangle from `PaintEventArgs` | explicit clips via `PushClip` and bounds discipline |

## Migration Strategy

1. Classify drawing code by intent:
- presentation-only -> styles/templates,
- custom geometry -> `Render`,
- external GPU/native interop -> `ICustomDrawOperation`.

2. Keep rendering stateless where possible:
- render from properties/viewmodel state,
- avoid hidden mutable paint state.

3. Split responsibilities:
- layout in measure/arrange or containers,
- rendering in `Render`,
- input behavior in commands/events.

4. Register render-affecting properties with `AffectsRender<T>(...)`.

## OwnerDraw Migration Example

WinForms C# (`ListBox` owner-draw):

```csharp
listBox.DrawMode = DrawMode.OwnerDrawFixed;
listBox.DrawItem += (_, e) =>
{
    e.DrawBackground();

    if (e.Index < 0)
        return;

    var item = (MetricRow)listBox.Items[e.Index];
    var back = (e.State & DrawItemState.Selected) != 0 ? Color.FromArgb(36, 99, 235) : Color.White;
    using var backBrush = new SolidBrush(back);
    e.Graphics.FillRectangle(backBrush, e.Bounds);

    TextRenderer.DrawText(e.Graphics, item.Name, listBox.Font, e.Bounds, Color.Black);
    var valueRect = new Rectangle(e.Bounds.Right - 90, e.Bounds.Top, 80, e.Bounds.Height);
    TextRenderer.DrawText(e.Graphics, item.Value.ToString("F1"), listBox.Font, valueRect, Color.DarkGreen);
};
```

Avalonia XAML:

```xaml
<UserControl xmlns="https://github.com/avaloniaui"
             xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
             xmlns:vm="using:MyApp.ViewModels"
             x:DataType="vm:MetricsViewModel">
  <ListBox ItemsSource="{CompiledBinding Rows}">
    <ListBox.Styles>
      <Style Selector="ListBoxItem:selected Border#RowRoot">
        <Setter Property="Background" Value="#2463EB" />
      </Style>
      <Style Selector="ListBoxItem Border#RowRoot">
        <Setter Property="Background" Value="White" />
      </Style>
    </ListBox.Styles>

    <ListBox.ItemTemplate>
      <DataTemplate x:DataType="vm:MetricRow">
        <Border x:Name="RowRoot" Padding="10,6">
          <Grid ColumnDefinitions="*,Auto">
            <TextBlock Text="{CompiledBinding Name}" />
            <TextBlock Grid.Column="1"
                       Foreground="#1F7A1F"
                       Text="{CompiledBinding Value, StringFormat={}{0:F1}}" />
          </Grid>
        </Border>
      </DataTemplate>
    </ListBox.ItemTemplate>
  </ListBox>
</UserControl>
```

Avalonia C#:

```csharp
using Avalonia.Controls;
using Avalonia.Controls.Templates;
using Avalonia.Layout;
using Avalonia.Media;

var listBox = new ListBox
{
    ItemsSource = viewModel.Rows,
    ItemTemplate = new FuncDataTemplate(
        typeof(MetricRow),
        (item, _) =>
        {
            var row = (MetricRow)item!;

            var grid = new Grid { ColumnDefinitions = ColumnDefinitions.Parse("*,Auto") };
            grid.Children.Add(new TextBlock { Text = row.Name });

            var value = new TextBlock
            {
                Text = row.Value.ToString("F1"),
                Foreground = Brushes.ForestGreen,
                HorizontalAlignment = HorizontalAlignment.Right
            };
            Grid.SetColumn(value, 1);
            grid.Children.Add(value);

            return new Border
            {
                Name = "RowRoot",
                Padding = new Avalonia.Thickness(10, 6),
                Background = Brushes.White,
                Child = grid
            };
        })
};
```

## Custom Paint Control Migration Example

WinForms C# (`OnPaint`):

```csharp
public sealed class GaugeBar : Control
{
    public int Value { get; set; }

    protected override void OnPaint(PaintEventArgs e)
    {
        base.OnPaint(e);
        e.Graphics.Clear(Color.Black);
        var width = Math.Max(0, Math.Min(100, Value)) * (Width - 8) / 100f;
        e.Graphics.FillRectangle(Brushes.LimeGreen, 4, 4, width, Height - 8);
        e.Graphics.DrawRectangle(Pens.Gray, 4, 4, Width - 8, Height - 8);
    }
}
```

Avalonia XAML:

```xaml
<local:GaugeBar xmlns="https://github.com/avaloniaui"
                xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
                xmlns:local="using:MyApp.Controls"
                Width="220"
                Height="24"
                Value="{Binding LoadPercent}" />
```

Avalonia C#:

```csharp
using System;
using Avalonia;
using Avalonia.Controls;
using Avalonia.Media;

public sealed class GaugeBar : Control
{
    static GaugeBar()
    {
        AffectsRender<GaugeBar>(ValueProperty);
    }

    public static readonly StyledProperty<int> ValueProperty =
        AvaloniaProperty.Register<GaugeBar, int>(nameof(Value), 0);

    public int Value
    {
        get => GetValue(ValueProperty);
        set => SetValue(ValueProperty, value);
    }

    public override void Render(DrawingContext context)
    {
        base.Render(context);

        var clamped = Math.Clamp(Value, 0, 100);
        var inner = new Rect(4, 4, Math.Max(0, Bounds.Width - 8), Math.Max(0, Bounds.Height - 8));
        var fillWidth = inner.Width * clamped / 100.0;

        context.FillRectangle(Brushes.Black, Bounds);
        context.FillRectangle(Brushes.LimeGreen, new Rect(inner.X, inner.Y, fillWidth, inner.Height));
        context.DrawRectangle(null, new Pen(Brushes.Gray, 1), inner);
    }
}
```

## Advanced Interop: `ICustomDrawOperation`

Use `DrawingContext.Custom(ICustomDrawOperation)` only when you need native/GPU drawing that is not available via `DrawingContext` primitives.

Key rules:

- keep operation bounds tight (`ICustomDrawOperation.Bounds`),
- implement `HitTest(Point)` correctly for interactivity,
- dispose unmanaged resources deterministically.

## Do/Don't

- Do replace owner-draw UI with templates first.
- Do treat `Render` as a pure function of control state.
- Do use `AffectsRender` for paint-only state changes.
- Don't port `Paint` event branching logic into view code-behind unnecessarily.
- Don't combine layout mutation and drawing in the same frame callback.
- Don't force sync repaint loops.

## Troubleshooting

1. Ported controls redraw too often.
- Check property change handlers for unnecessary `InvalidateVisual()` calls.

2. Rendering differs from WinForms item selection visuals.
- Move selection visuals into `ListBoxItem` styles (`:selected`) instead of drawing branches.

3. Flicker appears in custom control migration.
- Avoid per-frame allocations and reuse immutable brushes/pens/geometries where possible.
