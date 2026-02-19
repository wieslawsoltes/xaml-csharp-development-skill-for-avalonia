# WPF Layout System (`LayoutManager`, Measure/Arrange) to Avalonia Layout Pipeline

## Table of Contents
1. Scope and APIs
2. How WPF Layout Actually Runs
3. How Avalonia Layout Actually Runs
4. Concept Mapping (WPF -> Avalonia)
5. Migration Strategy
6. Shared-Size and Split Layout Migration Example
7. Custom `Panel` Migration Example
8. Do/Don't
9. Troubleshooting

## Scope and APIs

Primary WPF APIs:

- `UIElement.Measure(Size)`, `Arrange(Rect)`, `DesiredSize`
- `FrameworkElement.MeasureOverride(Size)`, `ArrangeOverride(Size)`
- `InvalidateMeasure()`, `InvalidateArrange()`, `UpdateLayout()`
- `Grid`, `DockPanel`, `WrapPanel`, `StackPanel`, `GridSplitter`, `Grid.IsSharedSizeScope`

Primary Avalonia APIs:

- `Layoutable.Measure(Size)`, `Arrange(Rect)`, `DesiredSize`
- `Layoutable.MeasureOverride(Size)`, `ArrangeOverride(Size)`
- `InvalidateMeasure()`, `InvalidateArrange()`, `UpdateLayout()`
- `Grid`, `DockPanel`, `WrapPanel`, `StackPanel`, `GridSplitter`, `Grid.IsSharedSizeScope`
- `Layoutable.UseLayoutRounding`, `Layoutable.LayoutUpdated`

## How WPF Layout Actually Runs

WPF layout is dispatcher-integrated and queue-based:

1. Measure invalidation propagates up/down where needed.
2. Arrange invalidation follows once measure is valid.
3. `LayoutManager` executes measure then arrange passes.
4. `LayoutUpdated` signals completion of a pass.

Migration implications:

- frequent `UpdateLayout()` calls in old WPF code usually indicate architectural coupling,
- `ActualWidth/ActualHeight` timing assumptions often need cleanup during migration,
- panel logic in `MeasureOverride`/`ArrangeOverride` ports conceptually 1:1.

## How Avalonia Layout Actually Runs

Avalonia uses the same high-level model:

1. Layout-affecting changes call `InvalidateMeasure`/`InvalidateArrange`.
2. Root `LayoutManager` batches and executes passes.
3. `MeasureOverride` computes desired size; `ArrangeOverride` positions children.
4. `LayoutUpdated` can be observed but should not drive main behavior logic.

Key differences to plan for:

- avoid WPF-specific assumptions around synchronous layout completion,
- keep property-driven layout deterministic and avoid recursive invalidation.

## Concept Mapping (WPF -> Avalonia)

| WPF | Avalonia |
|---|---|
| `MeasureOverride`/`ArrangeOverride` | same override model |
| `InvalidateMeasure`/`InvalidateArrange` | same methods and intent |
| `UpdateLayout` | available, but avoid in normal app flow |
| `Grid.IsSharedSizeScope` + `SharedSizeGroup` | same pattern |
| `GridSplitter` | `GridSplitter` |
| `UseLayoutRounding` | `UseLayoutRounding` on `Layoutable` |
| `LayoutUpdated` event | `LayoutUpdated` event on `Layoutable` |

## Migration Strategy

1. Keep panel semantics unchanged first; optimize after parity.
2. Remove layout side-effects from `LayoutUpdated` handlers.
3. Replace absolute sizing and imperative child bounds math with rows/columns, `Auto`, `*`, alignment.
4. Keep scroll ownership explicit (`ScrollViewer`) instead of implicit container behavior.
5. Use shared-size groups for multi-section form alignment.

## Shared-Size and Split Layout Migration Example

WPF XAML:

```xaml
<Grid Grid.IsSharedSizeScope="True"
      RowDefinitions="Auto,*"
      ColumnDefinitions="220,5,*">
  <Grid Grid.Row="0" Grid.ColumnSpan="3" ColumnDefinitions="Auto,*">
    <TextBlock Grid.Column="0" Text="Customer" />
    <TextBox Grid.Column="1" />
  </Grid>

  <TreeView Grid.Row="1" Grid.Column="0" />
  <GridSplitter Grid.Row="1" Grid.Column="1" Width="5" HorizontalAlignment="Stretch" />
  <ListView Grid.Row="1" Grid.Column="2" />
</Grid>
```

Avalonia XAML:

```xaml
<UserControl xmlns="https://github.com/avaloniaui"
             xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
             xmlns:vm="using:MyApp.ViewModels"
             x:DataType="vm:CustomerShellViewModel">
  <Grid Grid.IsSharedSizeScope="True"
        RowDefinitions="Auto,*"
        ColumnDefinitions="220,6,*"
        RowSpacing="8"
        ColumnSpacing="0">
    <Grid Grid.Row="0" Grid.ColumnSpan="3" ColumnDefinitions="Auto,*" ColumnSpacing="8">
      <TextBlock Grid.Column="0" VerticalAlignment="Center" Text="Customer" />
      <TextBox Grid.Column="1" Text="{CompiledBinding Query}" />
    </Grid>

    <TreeView Grid.Row="1" Grid.Column="0" ItemsSource="{CompiledBinding Groups}" />
    <GridSplitter Grid.Row="1" Grid.Column="1" Width="6" ResizeDirection="Columns" />
    <ListBox Grid.Row="1" Grid.Column="2" ItemsSource="{CompiledBinding Items}" />
  </Grid>
</UserControl>
```

Avalonia C#:

```csharp
using Avalonia;
using Avalonia.Controls;
using Avalonia.Layout;

var root = new Grid
{
    RowDefinitions = RowDefinitions.Parse("Auto,*"),
    ColumnDefinitions = ColumnDefinitions.Parse("220,6,*"),
    RowSpacing = 8
};
Grid.SetIsSharedSizeScope(root, true);

var header = new Grid
{
    ColumnDefinitions = ColumnDefinitions.Parse("Auto,*"),
    ColumnSpacing = 8
};
Grid.SetColumnSpan(header, 3);
header.Children.Add(new TextBlock { Text = "Customer", VerticalAlignment = VerticalAlignment.Center });

var queryBox = new TextBox { Text = viewModel.Query };
Grid.SetColumn(queryBox, 1);
header.Children.Add(queryBox);
root.Children.Add(header);

var groups = new TreeView { ItemsSource = viewModel.Groups };
Grid.SetRow(groups, 1);
root.Children.Add(groups);

var splitter = new GridSplitter { Width = 6, ResizeDirection = GridResizeDirection.Columns };
Grid.SetRow(splitter, 1);
Grid.SetColumn(splitter, 1);
root.Children.Add(splitter);

var items = new ListBox { ItemsSource = viewModel.Items };
Grid.SetRow(items, 1);
Grid.SetColumn(items, 2);
root.Children.Add(items);
```

## Custom `Panel` Migration Example

WPF C#:

```csharp
public sealed class TimelinePanel : Panel
{
    protected override Size MeasureOverride(Size availableSize)
    {
        foreach (UIElement child in InternalChildren)
        {
            child.Measure(new Size(availableSize.Width, double.PositiveInfinity));
        }

        var height = InternalChildren.Cast<UIElement>().Sum(x => x.DesiredSize.Height);
        return new Size(availableSize.Width, height);
    }

    protected override Size ArrangeOverride(Size finalSize)
    {
        double y = 0;
        foreach (UIElement child in InternalChildren)
        {
            child.Arrange(new Rect(0, y, finalSize.Width, child.DesiredSize.Height));
            y += child.DesiredSize.Height;
        }
        return finalSize;
    }
}
```

Avalonia XAML:

```xaml
<local:TimelinePanel xmlns="https://github.com/avaloniaui"
                     xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
                     xmlns:local="using:MyApp.Controls">
  <Border Height="56" />
  <Border Height="72" />
  <Border Height="40" />
</local:TimelinePanel>
```

Avalonia C#:

```csharp
using Avalonia;
using Avalonia.Controls;

public sealed class TimelinePanel : Panel
{
    protected override Size MeasureOverride(Size availableSize)
    {
        foreach (var child in Children)
        {
            child.Measure(new Size(availableSize.Width, double.PositiveInfinity));
        }

        var totalHeight = 0.0;
        foreach (var child in Children)
        {
            totalHeight += child.DesiredSize.Height;
        }

        return new Size(availableSize.Width, totalHeight);
    }

    protected override Size ArrangeOverride(Size finalSize)
    {
        var y = 0.0;
        foreach (var child in Children)
        {
            var h = child.DesiredSize.Height;
            child.Arrange(new Rect(0, y, finalSize.Width, h));
            y += h;
        }

        return finalSize;
    }
}
```

## Do/Don't

- Do keep layout invalidation minimal and property-driven.
- Do keep custom panel math in logical units, not device pixels.
- Do use shared-size groups for cross-section alignment.
- Don't force `UpdateLayout()` in command handlers unless absolutely required.
- Don't couple data loading and layout pass completion.
- Don't mutate control bounds imperatively as a default pattern.

## Troubleshooting

1. Migrated screen has layout jitter after data refresh.
- Check for back-to-back property updates that re-trigger measure; batch model updates where possible.

2. Shared labels no longer align after migration.
- Ensure `Grid.IsSharedSizeScope="True"` is set on a common ancestor and `SharedSizeGroup` names match.

3. Custom panel overflows/underflows after resize.
- Re-check measure constraints and ensure arrange uses `finalSize`, not stale measured width.
