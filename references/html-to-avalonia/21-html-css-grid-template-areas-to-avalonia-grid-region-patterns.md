# HTML/CSS `grid-template-areas` to Avalonia Grid Region Patterns

## Table of Contents
1. Scope and APIs
2. Mapping `grid-template-areas` Semantics
3. Static Conversion Pattern
4. Responsive Area-Template Switching
5. Advanced Alignment with Shared Size Scope
6. C# Equivalent: Shared Size Scope Pattern
7. AOT/Threading Notes
8. Troubleshooting

## Scope and APIs

Primary APIs:

- `Grid` (`RowDefinitions`, `ColumnDefinitions`, `RowSpacing`, `ColumnSpacing`)
- `Grid.Row`, `Grid.Column`, `Grid.RowSpan`, `Grid.ColumnSpan`
- runtime placement APIs: `Grid.SetRow`, `Grid.SetColumn`, `Grid.SetRowSpan`, `Grid.SetColumnSpan`
- shared sizing APIs: `Grid.IsSharedSizeScope`, `SharedSizeGroup`

Reference docs:

- [`01-html-css-flexbox-grid-and-responsive-layout-recipes.md`](01-html-css-flexbox-grid-and-responsive-layout-recipes)
- [`00-html-css-layout-box-model-and-positioning.md`](00-html-css-layout-box-model-and-positioning)
- [`30-layout-measure-arrange-and-custom-layout-controls.md`](../30-layout-measure-arrange-and-custom-layout-controls)

## Mapping `grid-template-areas` Semantics

Avalonia `Grid` does not expose a built-in `grid-template-areas` string parser. The equivalent pattern is explicit row/column tracks plus per-child row/column/span assignment.

| CSS Grid area idiom | Avalonia mapping |
|---|---|
| named area token (`header`) | child with explicit `Grid.Row` + `Grid.Column` |
| contiguous repeated token | represent with `Grid.RowSpan`/`Grid.ColumnSpan` |
| `.` placeholder | keep that cell empty (no child) |
| `grid-area: main` on item | map item to row/column coordinates in XAML/C# |

## Static Conversion Pattern

HTML/CSS:

```html
<div class="shell">
  <header>...</header>
  <nav>...</nav>
  <main>...</main>
  <footer>...</footer>
</div>
```

```css
.shell {
  display: grid;
  grid-template-columns: 280px 1fr;
  grid-template-rows: auto 1fr auto;
  grid-template-areas:
    "header header"
    "nav    main"
    "footer footer";
  gap: 12px;
}
header { grid-area: header; }
nav { grid-area: nav; }
main { grid-area: main; }
footer { grid-area: footer; }
```

Avalonia:

```xaml
<Grid ColumnDefinitions="280,*"
      RowDefinitions="Auto,*,Auto"
      ColumnSpacing="12"
      RowSpacing="12">
  <Border Grid.Row="0" Grid.Column="0" Grid.ColumnSpan="2" Classes="header" />
  <Border Grid.Row="1" Grid.Column="0" Classes="nav" />
  <Border Grid.Row="1" Grid.Column="1" Classes="main" />
  <Border Grid.Row="2" Grid.Column="0" Grid.ColumnSpan="2" Classes="footer" />
</Grid>
```

## Responsive Area-Template Switching

Web apps commonly swap `grid-template-areas` in media queries. In Avalonia, keep the same region controls and switch row/column definitions plus attached placement.

```csharp
using System.Collections.Generic;
using Avalonia.Controls;
using Avalonia.Threading;

public readonly record struct GridArea(int Row, int Column, int RowSpan = 1, int ColumnSpan = 1);

static readonly IReadOnlyDictionary<string, GridArea> DesktopAreas = new Dictionary<string, GridArea>
{
    ["header"] = new(0, 0, 1, 2),
    ["nav"] = new(1, 0),
    ["main"] = new(1, 1),
    ["footer"] = new(2, 0, 1, 2)
};

static readonly IReadOnlyDictionary<string, GridArea> MobileAreas = new Dictionary<string, GridArea>
{
    ["header"] = new(0, 0),
    ["nav"] = new(1, 0),
    ["main"] = new(2, 0),
    ["footer"] = new(3, 0)
};

static void ApplyAreas(IReadOnlyDictionary<string, Control> regions, IReadOnlyDictionary<string, GridArea> areas)
{
    foreach (var (name, control) in regions)
    {
        if (!areas.TryGetValue(name, out var area))
            continue;

        Grid.SetRow(control, area.Row);
        Grid.SetColumn(control, area.Column);
        Grid.SetRowSpan(control, area.RowSpan);
        Grid.SetColumnSpan(control, area.ColumnSpan);
    }
}

static void UpdateTemplate(Grid shell, IReadOnlyDictionary<string, Control> regions)
{
    var mobile = shell.Bounds.Width < 900;

    if (mobile)
    {
        shell.RowDefinitions = RowDefinitions.Parse("Auto,Auto,*,Auto");
        shell.ColumnDefinitions = ColumnDefinitions.Parse("*");
        ApplyAreas(regions, MobileAreas);
    }
    else
    {
        shell.RowDefinitions = RowDefinitions.Parse("Auto,*,Auto");
        shell.ColumnDefinitions = ColumnDefinitions.Parse("280,*");
        ApplyAreas(regions, DesktopAreas);
    }
}

static void WireTemplateUpdates(Grid shell, IReadOnlyDictionary<string, Control> regions)
{
    shell.GetObservable(Control.BoundsProperty).Subscribe(_ =>
        Dispatcher.UIThread.Post(() => UpdateTemplate(shell, regions)));
}
```

## Advanced Alignment with Shared Size Scope

When multiple nested grids represent repeated area structures (for example, repeated cards with label/value columns), use shared-size groups to align tracks globally.

```xaml
<Grid Grid.IsSharedSizeScope="True" RowDefinitions="Auto,Auto" RowSpacing="8">
  <Grid Grid.Row="0" ColumnSpacing="8">
    <Grid.ColumnDefinitions>
      <ColumnDefinition Width="Auto" SharedSizeGroup="MetaLabel" />
      <ColumnDefinition Width="*" />
    </Grid.ColumnDefinitions>
    <TextBlock Grid.Column="0" Text="Orders" />
    <TextBlock Grid.Column="1" Text="1,280" />
  </Grid>

  <Grid Grid.Row="1" ColumnSpacing="8">
    <Grid.ColumnDefinitions>
      <ColumnDefinition Width="Auto" SharedSizeGroup="MetaLabel" />
      <ColumnDefinition Width="*" />
    </Grid.ColumnDefinitions>
    <TextBlock Grid.Column="0" Text="Revenue" />
    <TextBlock Grid.Column="1" Text="$420,000" />
  </Grid>
</Grid>
```

## C# Equivalent: Shared Size Scope Pattern

```csharp
using Avalonia;
using Avalonia.Controls;

var section = new Grid
{
    RowDefinitions = RowDefinitions.Parse("Auto,Auto"),
    RowSpacing = 8
};
Grid.SetIsSharedSizeScope(section, true);

Grid CreateMetricRow(string label, string value)
{
    var row = new Grid { ColumnSpacing = 8 };
    row.ColumnDefinitions.Add(new ColumnDefinition { Width = GridLength.Auto, SharedSizeGroup = "MetaLabel" });
    row.ColumnDefinitions.Add(new ColumnDefinition { Width = new GridLength(1, GridUnitType.Star) });
    row.Children.Add(new TextBlock { Text = label });
    row.Children.Add(new TextBlock { Text = value });
    Grid.SetColumn(row.Children[1], 1);
    return row;
}

var row1 = CreateMetricRow("Orders", "1,280");
var row2 = CreateMetricRow("Revenue", "$420,000");
Grid.SetRow(row2, 1);

section.Children.Add(row1);
section.Children.Add(row2);
```

## AOT/Threading Notes

- Keep region controls strongly typed and reuse them while swapping templates.
- If template switching is triggered by async/background signals, apply updates on `Dispatcher.UIThread`.
- Prefer compiled bindings (`x:DataType`) for region content; only the layout metadata should change at runtime.

## Troubleshooting

1. Area content overlaps unexpectedly.
- Verify every area assignment has explicit `Grid.Row`/`Grid.Column` and correct spans.

2. Responsive template switches but tracks look stale.
- Update both definitions (`RowDefinitions`/`ColumnDefinitions`) and child attached properties together.

3. Cross-card label columns are not aligned.
- Wrap the section with `Grid.IsSharedSizeScope="True"` and assign matching `SharedSizeGroup` values.
