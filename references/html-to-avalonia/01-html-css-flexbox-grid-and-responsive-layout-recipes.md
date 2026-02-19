# HTML/CSS Flexbox, Grid, and Responsive Layout Recipes in Avalonia

## Table of Contents
1. Scope and APIs
2. Flexbox to Avalonia Mapping
3. Grid Template Mapping
4. Breakpoints and Container-Scoped Adaptation
5. Common Flex/Grid Snippet Conversions
6. Recipe: Responsive Card Board
7. Recipe: Mobile Drawer to Desktop Rail
8. C# Equivalent: Responsive Toolbar Shell
9. AOT/Threading Notes
10. Troubleshooting

## Scope and APIs

Primary APIs:

- `StackPanel` (`Orientation`, `Spacing`)
- `DockPanel`
- `WrapPanel`
- `Grid` (`RowDefinitions`, `ColumnDefinitions`, spacing, spans)
- `Container` (`SetSizing`, `SetName`) and style query primitives (`ContainerQuery`, `StyleQuery`, `StyleQueries`)
- `ThemeVariantScope` for adaptive visual variants

## Flexbox to Avalonia Mapping

| Flexbox idiom | Avalonia pattern |
|---|---|
| `display:flex; flex-direction:row/column` | `StackPanel Orientation="Horizontal/Vertical"` |
| `gap` | `StackPanel.Spacing` or `Grid` row/column spacing |
| `justify-content` | parent layout sizing + child alignment (`HorizontalAlignment` / `VerticalAlignment`) |
| `align-items` | per-child alignment properties |
| `flex-wrap` | `WrapPanel` |
| `flex-grow` | `Grid` star sizing (`*`) |

Use `Grid` when you need robust flex-like distribution and mixed fixed/fluid tracks.

## Grid Template Mapping

| CSS Grid idiom | Avalonia mapping |
|---|---|
| `grid-template-columns: 240px 1fr` | `ColumnDefinitions="240,*"` |
| `grid-template-rows: auto 1fr` | `RowDefinitions="Auto,*"` |
| `grid-column: 1 / span 2` | `Grid.Column` + `Grid.ColumnSpan` |
| `grid-row: 2 / span 3` | `Grid.Row` + `Grid.RowSpan` |
| `gap` | `Grid.RowSpacing`, `Grid.ColumnSpacing` |

## Breakpoints and Container-Scoped Adaptation

CSS media/container queries are usually ported with one of these approaches:

1. Root-size class toggling (`desktop`, `tablet`, `mobile`) on a view root.
2. Container metadata via `Container.SetName`/`Container.SetSizing` plus targeted style query usage.
3. View switching (`DataTemplate` or alternate layout subtree) for major breakpoint jumps.

XAML root with responsive classes:

```xaml
<Grid x:Name="Root" Classes="mobile">
  <Grid.Styles>
    <Style Selector="Grid.mobile Border.nav-rail">
      <Setter Property="IsVisible" Value="False" />
    </Style>
    <Style Selector="Grid.desktop Border.nav-rail">
      <Setter Property="IsVisible" Value="True" />
    </Style>
  </Grid.Styles>

  <Border Classes="nav-rail" Width="240" />
</Grid>
```

C# breakpoint updater:

```csharp
using Avalonia.Controls;
using Avalonia.Threading;

void ApplyBreakpoint(Grid root)
{
    var width = root.Bounds.Width;

    root.Classes.Set("mobile", width < 720);
    root.Classes.Set("tablet", width >= 720 && width < 1100);
    root.Classes.Set("desktop", width >= 1100);
}

void WireBreakpoint(Grid root)
{
    root.GetObservable(Control.BoundsProperty).Subscribe(_ =>
    {
        Dispatcher.UIThread.Post(() => ApplyBreakpoint(root));
    });
}
```

## Common Flex/Grid Snippet Conversions

HTML/CSS (toolbar with left and right groups):

```html
<div class="toolbar">
  <div class="left">...</div>
  <div class="right">...</div>
</div>
```

```css
.toolbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 8px;
}
```

Avalonia:

```xaml
<Grid ColumnDefinitions="Auto,*,Auto" ColumnSpacing="8">
  <StackPanel Grid.Column="0" Orientation="Horizontal" Spacing="8" />
  <Border Grid.Column="1" />
  <StackPanel Grid.Column="2" Orientation="Horizontal" Spacing="8" />
</Grid>
```

HTML/CSS (wrapping chips):

```css
.chips { display:flex; flex-wrap:wrap; gap:8px; }
```

Avalonia:

```xaml
<WrapPanel ItemHeight="32" Orientation="Horizontal">
  <Button Content="Design" Margin="0,0,8,8" />
  <Button Content="Backend" Margin="0,0,8,8" />
</WrapPanel>
```

HTML/CSS (equal columns):

```css
.three { display:grid; grid-template-columns: repeat(3, 1fr); gap: 12px; }
```

Avalonia:

```xaml
<Grid ColumnDefinitions="*,*,*" ColumnSpacing="12">
  <Border Grid.Column="0" />
  <Border Grid.Column="1" />
  <Border Grid.Column="2" />
</Grid>
```

## Recipe: Responsive Card Board

HTML/CSS intent:

```css
.cards { display:grid; grid-template-columns:repeat(auto-fit, minmax(280px, 1fr)); gap:12px; }
```

Avalonia recipe:

- small width: `ItemsControl` + `StackPanel`
- medium/large width: `ItemsControl` + `UniformGrid` with runtime-updated `Columns`

```csharp
int ColumnsFor(double width)
{
    if (width >= 1400) return 4;
    if (width >= 1000) return 3;
    if (width >= 680) return 2;
    return 1;
}
```

## Recipe: Mobile Drawer to Desktop Rail

- mobile: `SplitView DisplayMode="Overlay" IsPaneOpen` bound to hamburger command.
- desktop: `SplitView DisplayMode="Inline" CompactPaneLength` and always-open pane.

## C# Equivalent: Responsive Toolbar Shell

```csharp
using Avalonia.Controls;
using Avalonia.Threading;

var root = new Grid
{
    ColumnDefinitions = ColumnDefinitions.Parse("Auto,*,Auto"),
    ColumnSpacing = 8
};

var left = new StackPanel { Orientation = Avalonia.Layout.Orientation.Horizontal, Spacing = 8 };
var spacer = new Border();
var right = new StackPanel { Orientation = Avalonia.Layout.Orientation.Horizontal, Spacing = 8 };

Grid.SetColumn(left, 0);
Grid.SetColumn(spacer, 1);
Grid.SetColumn(right, 2);

root.Children.Add(left);
root.Children.Add(spacer);
root.Children.Add(right);

void ApplyBreakpoint(Grid shell)
{
    var width = shell.Bounds.Width;
    shell.Classes.Set("mobile", width < 720);
    shell.Classes.Set("tablet", width >= 720 && width < 1100);
    shell.Classes.Set("desktop", width >= 1100);
}

root.GetObservable(Control.BoundsProperty).Subscribe(_ =>
    Dispatcher.UIThread.Post(() => ApplyBreakpoint(root)));
```

## AOT/Threading Notes

- Breakpoint logic should use strongly-typed control references and compiled bindings.
- If breakpoint state is updated from background events (telemetry, remote config), marshal to `Dispatcher.UIThread`.

## Troubleshooting

1. Flex-style distribution looks uneven.
- Use `Grid` star tracks instead of stacked `StackPanel` for mixed fixed/fluid children.

2. Responsive class styles do not apply.
- Ensure class is on the same selector scope as style targets.

3. Frequent resize events cause jank.
- Debounce width updates before class changes.
