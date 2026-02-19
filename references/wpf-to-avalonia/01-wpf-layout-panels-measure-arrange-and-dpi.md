# WPF Layout Panels, Measure/Arrange, and DPI to Avalonia

## Table of Contents
1. Scope and APIs
2. Layout Mapping
3. Measure/Arrange Authoring
4. Conversion Example
5. Avalonia C# Equivalent
6. Troubleshooting

## Scope and APIs

Primary WPF APIs:

- `Grid`, `StackPanel`, `DockPanel`, `WrapPanel`, `Canvas`
- `MeasureOverride`, `ArrangeOverride`
- DPI-aware sizing assumptions

Primary Avalonia APIs:

- same panel family (`Grid`, `StackPanel`, `DockPanel`, `WrapPanel`, `Canvas`)
- `MeasureOverride`, `ArrangeOverride`
- `TopLevel.RenderScaling` and logical-unit layout

## Layout Mapping

| WPF | Avalonia |
|---|---|
| `Grid.RowDefinitions`/`ColumnDefinitions` | same concept and syntax |
| `DockPanel.Dock` | same concept |
| `HorizontalAlignment`/`VerticalAlignment` | same concept |
| `UseLayoutRounding` tuning | rely on logical units, tune rendering only where needed |

## Measure/Arrange Authoring

WPF custom panel logic generally ports 1:1 conceptually:

- measure children with constraints,
- arrange children in final bounds,
- invalidate measure/arrange explicitly only when required.

## Conversion Example

WPF XAML:

```xaml
<Grid Margin="12" RowDefinitions="Auto,*" ColumnDefinitions="200,*">
  <TextBlock Grid.Row="0" Grid.Column="0" Text="Name" />
  <TextBox Grid.Row="0" Grid.Column="1" />
</Grid>
```

Avalonia XAML:

```xaml
<Grid Margin="12" RowDefinitions="Auto,*" ColumnDefinitions="200,*">
  <TextBlock Grid.Row="0" Grid.Column="0" Text="Name" />
  <TextBox Grid.Row="0" Grid.Column="1" />
</Grid>
```

## Avalonia C# Equivalent

```csharp
using Avalonia.Controls;

var form = new Grid
{
    Margin = new Avalonia.Thickness(12),
    RowDefinitions = RowDefinitions.Parse("Auto,*"),
    ColumnDefinitions = ColumnDefinitions.Parse("200,*")
};

form.Children.Add(new TextBlock { Text = "Name" });
var name = new TextBox();
Grid.SetColumn(name, 1);
form.Children.Add(name);
```

## Troubleshooting

1. Ported layout uses too many absolute sizes.
- replace with star sizing and alignment where possible.

2. custom panel ports remeasure excessively.
- control invalidation discipline (`InvalidateMeasure`/`InvalidateArrange`).

3. DPI behavior differs from WPF assumptions.
- avoid pixel arithmetic in layout; use logical units and inspect `RenderScaling` only when needed.
