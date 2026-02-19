# HTML/CSS Layout Box Model and Positioning to Avalonia

## Table of Contents
1. Scope and APIs
2. Box Model Mapping
3. `display` and Flow Mapping
4. Positioning and Layering
5. Overflow and Scroll Behavior
6. Common HTML/CSS Snippet Conversions
7. End-to-End Conversion Example
8. C# Equivalent: Dashboard Shell Layout
9. AOT/Trimming Notes
10. Troubleshooting

## Scope and APIs

Primary APIs:

- `Layoutable` (`Width`, `Height`, `MinWidth`, `MaxWidth`, `Margin`, `HorizontalAlignment`, `VerticalAlignment`)
- `Panel` and `Visual.ZIndex` (set as `ZIndex`)
- `Grid`, `StackPanel`, `DockPanel`, `WrapPanel`, `Canvas`, `RelativePanel`
- `Border`, `Decorator`, `Viewbox`, `LayoutTransformControl`
- `ScrollViewer`

Reference docs:

- [`30-layout-measure-arrange-and-custom-layout-controls.md`](../30-layout-measure-arrange-and-custom-layout-controls)
- [`21-custom-layout-authoring.md`](../21-custom-layout-authoring)
- [`57-scrollviewer-offset-anchoring-and-snap-points.md`](../57-scrollviewer-offset-anchoring-and-snap-points)

## Box Model Mapping

| HTML/CSS idiom | Avalonia mapping |
|---|---|
| `width`, `height` | `Width`, `Height` on `Layoutable` |
| `min/max-width`, `min/max-height` | `MinWidth`, `MaxWidth`, `MinHeight`, `MaxHeight` |
| `margin` | `Margin` |
| `padding` | `Padding` on controls that expose it (`Border`, `TemplatedControl` templates, etc.) |
| `border` | `BorderBrush`, `BorderThickness`, `CornerRadius` |
| `box-sizing` | no direct property; Avalonia layout always uses explicit measure/arrange contracts |

## `display` and Flow Mapping

| CSS `display` | Avalonia pattern |
|---|---|
| `block` | vertical flow via `StackPanel` or row in `Grid` |
| `inline` / `inline-block` | text flow is not DOM inline layout; use `TextBlock` runs or structured controls |
| `flex` | `StackPanel`, `DockPanel`, `WrapPanel`, or custom panel |
| `grid` | `Grid` with `RowDefinitions`/`ColumnDefinitions` |
| `none` | `IsVisible="False"` |

Practical rule: choose `Grid` for most complex app layouts; use `StackPanel` for simple axis stacking.

## Positioning and Layering

| CSS idiom | Avalonia mapping |
|---|---|
| `position: relative` container | `Grid`/`Panel` parent used as overlay host |
| `position: absolute` child | `Canvas.Left`/`Canvas.Top` in `Canvas`, or overlay row/column in `Grid` |
| `z-index` | `ZIndex` on `Visual` |
| `position: fixed` | top-level overlay (`Popup`, adorner/overlay layer) |
| `position: sticky` | no direct sticky equivalent; combine `ScrollViewer` offset handling + layout logic |

## Overflow and Scroll Behavior

| CSS idiom | Avalonia mapping |
|---|---|
| `overflow: auto` | `ScrollViewer` |
| `overflow-x/y` | `ScrollViewer.HorizontalScrollBarVisibility` / `VerticalScrollBarVisibility` |
| scroll snapping | `ScrollViewer` snap-point APIs and `IScrollSnapPointsInfo` panels |

## Common HTML/CSS Snippet Conversions

HTML/CSS (absolute corner badge):

```html
<div class="tile">
  <span class="badge">NEW</span>
</div>
```

```css
.tile { position: relative; }
.badge { position: absolute; top: 8px; right: 8px; z-index: 2; }
```

Avalonia:

```xaml
<Grid>
  <Border Classes="tile" />
  <Border Classes="badge"
          HorizontalAlignment="Right"
          VerticalAlignment="Top"
          Margin="0,8,8,0"
          ZIndex="2" />
</Grid>
```

HTML/CSS (centered overlay):

```html
<div class="host">
  <div class="overlay">Loading...</div>
</div>
```

```css
.host { position: relative; }
.overlay { position: absolute; inset: 0; display: grid; place-items: center; }
```

Avalonia:

```xaml
<Grid>
  <ContentPresenter />
  <Border Background="#66000000"
          HorizontalAlignment="Stretch"
          VerticalAlignment="Stretch">
    <TextBlock HorizontalAlignment="Center"
               VerticalAlignment="Center"
               Text="Loading..." />
  </Border>
</Grid>
```

HTML/CSS (two-column form):

```css
.form { display:grid; grid-template-columns: 180px 1fr; gap: 8px 12px; }
```

Avalonia:

```xaml
<Grid ColumnDefinitions="180,*"
      RowDefinitions="Auto,Auto,Auto"
      RowSpacing="8"
      ColumnSpacing="12">
  <TextBlock Grid.Row="0" Grid.Column="0" Text="Name" />
  <TextBox Grid.Row="0" Grid.Column="1" />
</Grid>
```

## End-to-End Conversion Example

HTML/CSS:

```html
<div class="dashboard">
  <aside class="sidebar">...</aside>
  <main class="content">
    <section class="hero">...</section>
    <section class="cards">...</section>
  </main>
</div>
```

```css
.dashboard {
  display: grid;
  grid-template-columns: 280px 1fr;
  min-height: 100vh;
}
.cards {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 12px;
}
```

Avalonia XAML:

```xaml
<Grid RowDefinitions="Auto,*"
      ColumnDefinitions="280,*">
  <Border Grid.RowSpan="2" Grid.Column="0" Classes="sidebar" />

  <Border Grid.Row="0" Grid.Column="1" Classes="hero" Margin="16,16,16,8" />

  <ItemsControl Grid.Row="1" Grid.Column="1" Margin="16,8,16,16"
                ItemsSource="{CompiledBinding Metrics}">
    <ItemsControl.ItemsPanel>
      <ItemsPanelTemplate>
        <UniformGrid Columns="3" />
      </ItemsPanelTemplate>
    </ItemsControl.ItemsPanel>
  </ItemsControl>
</Grid>
```

## C# Equivalent: Dashboard Shell Layout

```csharp
using Avalonia;
using Avalonia.Controls;

var dashboard = new Grid
{
    RowDefinitions = RowDefinitions.Parse("Auto,*"),
    ColumnDefinitions = ColumnDefinitions.Parse("280,*")
};

var sidebar = new Border();
Grid.SetColumn(sidebar, 0);
Grid.SetRowSpan(sidebar, 2);

var hero = new Border { Margin = new Thickness(16, 16, 16, 8) };
Grid.SetRow(hero, 0);
Grid.SetColumn(hero, 1);

var cardsHost = new ItemsControl { Margin = new Thickness(16, 8, 16, 16) };
Grid.SetRow(cardsHost, 1);
Grid.SetColumn(cardsHost, 1);

dashboard.Children.Add(sidebar);
dashboard.Children.Add(hero);
dashboard.Children.Add(cardsHost);

// Additional absolute positioning snippet.
var canvas = new Canvas();
var badge = new Border { Width = 96, Height = 28 };
Canvas.SetLeft(badge, 12);
Canvas.SetTop(badge, 12);
badge.ZIndex = 10;
canvas.Children.Add(badge);
```

## AOT/Trimming Notes

- Layout APIs are trim-safe in normal usage.
- For custom panels, keep behavior in static-typed properties and avoid reflection-based dynamic tree manipulation.

## Troubleshooting

1. Child controls collapse unexpectedly.
- Verify parent constraints and `Grid` row/column definitions.

2. Absolute overlays disappear behind content.
- Set `ZIndex` and ensure same visual parent.

3. Scroll behavior differs from browser.
- Configure both scroll bar visibility and snap/anchor properties explicitly.
