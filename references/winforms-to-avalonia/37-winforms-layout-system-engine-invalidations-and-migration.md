# WinForms Layout System (LayoutEngine, Dock/Anchor, AutoSize) to Avalonia Layout Passes

## Table of Contents
1. Scope and APIs
2. How WinForms Layout Actually Runs
3. How Avalonia Layout Actually Runs
4. Concept Mapping (WinForms -> Avalonia)
5. Migration Strategy
6. End-to-End Form Migration
7. Custom Container Migration (`LayoutEngine` -> custom `Panel`)
8. Do/Don't
9. Troubleshooting

## Scope and APIs

Primary WinForms APIs:

- `Control.PerformLayout()`, `SuspendLayout()`, `ResumeLayout(bool)`
- `Control.Dock`, `Control.Anchor`, `AutoSize`, `GetPreferredSize(Size)`
- `LayoutEngine`, `LayoutEventArgs`, `LayoutTransaction`
- `FlowLayoutPanel`, `TableLayoutPanel`, `SplitContainer`, `ScrollableControl.AutoScroll`

Primary Avalonia APIs:

- `Layoutable.Measure(Size)`, `Arrange(Rect)`, `InvalidateMeasure()`, `InvalidateArrange()`, `UpdateLayout()`
- `Layoutable.MeasureOverride(Size)`, `ArrangeOverride(Size)`, `DesiredSize`
- `Layoutable.UseLayoutRounding`, `Layoutable.LayoutUpdated`
- `Grid`, `DockPanel`, `WrapPanel`, `StackPanel`, `ScrollViewer`, `GridSplitter`

## How WinForms Layout Actually Runs

WinForms layout is event/transaction-driven:

1. Property changes (`Dock`, `Anchor`, `Size`, font, visibility) trigger `PerformLayout`.
2. `LayoutEngine` on each container computes child bounds.
3. Parent `Layout` events can recurse if child sizes changed.
4. `SuspendLayout`/`ResumeLayout(true)` are used to batch and avoid repeated passes.

Implications for migration:

- WinForms code often mutates `Bounds` directly.
- Layout order can depend on control insertion order and z-order.
- `AutoSize` + `GetPreferredSize` behavior is container-specific.

## How Avalonia Layout Actually Runs

Avalonia layout is invalidation-queued and root-driven:

1. Property changes invalidate measure/arrange on affected `Layoutable` nodes.
2. `LayoutManager` executes measure pass then arrange pass for the visual root.
3. `MeasureOverride` computes desired size; `ArrangeOverride` places children.
4. Rendering happens after valid layout; layout and render invalidation are separate concerns.

Migration implications:

- Prefer declarative sizing (`Auto`, `*`, alignments, margins) over manual bounds math.
- In custom containers, only call `InvalidateMeasure`/`InvalidateArrange` when layout-affecting state changes.
- `UpdateLayout()` exists, but should stay a last resort for edge interoperability paths.

## Concept Mapping (WinForms -> Avalonia)

| WinForms | Avalonia |
|---|---|
| `SuspendLayout`/`ResumeLayout` | Not usually required; layout manager batches invalidations automatically |
| `PerformLayout` | `InvalidateMeasure`/`InvalidateArrange`, optional `UpdateLayout()` |
| `DockStyle.Fill` | `Grid` star-sized cell or last `DockPanel` child |
| `AnchorStyles.Bottom | Right` | place in bottom/right-aligned `Grid` cell |
| `AutoScroll` | `ScrollViewer` |
| `TableLayoutPanel` | `Grid` with `RowDefinitions`/`ColumnDefinitions` and optional shared-size groups |
| `FlowLayoutPanel` | `WrapPanel` or custom `Panel` |
| `Layout` event | property-driven layout invalidation + optional `LayoutUpdated` observers |

## Migration Strategy

1. Remove direct `Bounds` writes from feature code first.
2. Convert shell layout to `Grid` + `DockPanel` + `GridSplitter`.
3. Replace `AutoScroll` containers with explicit `ScrollViewer` boundaries.
4. Convert `TableLayoutPanel` forms to explicit rows/columns and shared-size groups where needed.
5. Port any custom `LayoutEngine` to a dedicated Avalonia `Panel` (`MeasureOverride`/`ArrangeOverride`).
6. Keep layout and rendering responsibilities separate (`InvalidateMeasure` vs `InvalidateVisual`).

## End-to-End Form Migration

WinForms C# (typical designer/runtime mix):

```csharp
SuspendLayout();

var header = new Panel { Dock = DockStyle.Top, Height = 48 };
var title = new Label { Text = "Orders", AutoSize = true, Left = 12, Top = 14 };
var save = new Button { Text = "Save", Width = 96, Anchor = AnchorStyles.Top | AnchorStyles.Right };
save.Left = ClientSize.Width - save.Width - 12;
save.Top = 10;
header.Controls.Add(title);
header.Controls.Add(save);

var split = new SplitContainer
{
    Dock = DockStyle.Fill,
    SplitterDistance = 280,
    FixedPanel = FixedPanel.Panel1
};
split.Panel1.Controls.Add(new TreeView { Dock = DockStyle.Fill });
split.Panel2.Controls.Add(new ListView { Dock = DockStyle.Fill, View = View.Details });

Controls.Add(split);
Controls.Add(header);

ResumeLayout(performLayout: true);
```

Avalonia XAML:

```xaml
<UserControl xmlns="https://github.com/avaloniaui"
             xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
             xmlns:vm="using:MyApp.ViewModels"
             x:DataType="vm:OrdersShellViewModel">
  <Grid RowDefinitions="Auto,*" ColumnDefinitions="280,6,*">
    <Border Grid.Row="0" Grid.ColumnSpan="3" Background="{DynamicResource ThemeControlMidBrush}" Padding="12,8">
      <Grid ColumnDefinitions="*,Auto">
        <TextBlock VerticalAlignment="Center" Text="Orders" FontSize="16" />
        <Button Grid.Column="1"
                Width="96"
                HorizontalAlignment="Right"
                Command="{CompiledBinding SaveCommand}"
                Content="Save" />
      </Grid>
    </Border>

    <ScrollViewer Grid.Row="1" Grid.Column="0">
      <TreeView ItemsSource="{CompiledBinding Groups}" />
    </ScrollViewer>

    <GridSplitter Grid.Row="1" Grid.Column="1" Width="6" ResizeDirection="Columns" />

    <ScrollViewer Grid.Row="1" Grid.Column="2">
      <ListBox ItemsSource="{CompiledBinding Orders}" />
    </ScrollViewer>
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
    ColumnDefinitions = ColumnDefinitions.Parse("280,6,*")
};

var header = new Border { Padding = new Thickness(12, 8) };
Grid.SetColumnSpan(header, 3);

var headerGrid = new Grid { ColumnDefinitions = ColumnDefinitions.Parse("*,Auto") };
headerGrid.Children.Add(new TextBlock { Text = "Orders", FontSize = 16, VerticalAlignment = VerticalAlignment.Center });

var saveButton = new Button
{
    Width = 96,
    Content = "Save",
    HorizontalAlignment = HorizontalAlignment.Right,
    Command = viewModel.SaveCommand
};
Grid.SetColumn(saveButton, 1);
headerGrid.Children.Add(saveButton);
header.Child = headerGrid;
root.Children.Add(header);

var left = new ScrollViewer { Content = new TreeView { ItemsSource = viewModel.Groups } };
Grid.SetRow(left, 1);
root.Children.Add(left);

var splitter = new GridSplitter { Width = 6, ResizeDirection = GridResizeDirection.Columns };
Grid.SetRow(splitter, 1);
Grid.SetColumn(splitter, 1);
root.Children.Add(splitter);

var right = new ScrollViewer { Content = new ListBox { ItemsSource = viewModel.Orders } };
Grid.SetRow(right, 1);
Grid.SetColumn(right, 2);
root.Children.Add(right);
```

## Custom Container Migration (`LayoutEngine` -> custom `Panel`)

WinForms C# (`LayoutEngine`):

```csharp
using System.Windows.Forms;
using System.Windows.Forms.Layout;

public sealed class TileHost : Panel
{
    private readonly LayoutEngine _engine = new TileLayoutEngine();
    public override LayoutEngine LayoutEngine => _engine;
}

file sealed class TileLayoutEngine : LayoutEngine
{
    public override bool Layout(object container, LayoutEventArgs layoutEventArgs)
    {
        var parent = (TileHost)container;
        const int spacing = 8;
        const int itemWidth = 180;
        const int itemHeight = 96;

        var x = spacing;
        var y = spacing;

        foreach (Control child in parent.Controls)
        {
            if (x + itemWidth > parent.ClientSize.Width)
            {
                x = spacing;
                y += itemHeight + spacing;
            }

            child.Bounds = new Rectangle(x, y, itemWidth, itemHeight);
            x += itemWidth + spacing;
        }

        return false;
    }
}
```

Avalonia XAML:

```xaml
<local:TilePanel xmlns="https://github.com/avaloniaui"
                 xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
                 xmlns:local="using:MyApp.Controls"
                 ItemWidth="180"
                 ItemHeight="96"
                 Spacing="8">
  <Button Content="Orders" />
  <Button Content="Invoices" />
  <Button Content="Shipments" />
  <Button Content="Returns" />
</local:TilePanel>
```

Avalonia C# (`Panel`):

```csharp
using Avalonia;
using Avalonia.Controls;

public sealed class TilePanel : Panel
{
    static TilePanel()
    {
        AffectsMeasure<TilePanel>(ItemWidthProperty, ItemHeightProperty, SpacingProperty);
    }

    public static readonly StyledProperty<double> ItemWidthProperty =
        AvaloniaProperty.Register<TilePanel, double>(nameof(ItemWidth), 180);

    public static readonly StyledProperty<double> ItemHeightProperty =
        AvaloniaProperty.Register<TilePanel, double>(nameof(ItemHeight), 96);

    public static readonly StyledProperty<double> SpacingProperty =
        AvaloniaProperty.Register<TilePanel, double>(nameof(Spacing), 8);

    public double ItemWidth
    {
        get => GetValue(ItemWidthProperty);
        set => SetValue(ItemWidthProperty, value);
    }

    public double ItemHeight
    {
        get => GetValue(ItemHeightProperty);
        set => SetValue(ItemHeightProperty, value);
    }

    public double Spacing
    {
        get => GetValue(SpacingProperty);
        set => SetValue(SpacingProperty, value);
    }

    protected override Size MeasureOverride(Size availableSize)
    {
        foreach (var child in Children)
        {
            child.Measure(new Size(ItemWidth, ItemHeight));
        }

        var width = double.IsInfinity(availableSize.Width) ? ItemWidth * Children.Count : availableSize.Width;
        var x = Spacing;
        var y = Spacing;
        var maxY = y;

        foreach (var _ in Children)
        {
            if (x + ItemWidth > width && x > Spacing)
            {
                x = Spacing;
                y += ItemHeight + Spacing;
            }

            maxY = y + ItemHeight;
            x += ItemWidth + Spacing;
        }

        return new Size(width, maxY + Spacing);
    }

    protected override Size ArrangeOverride(Size finalSize)
    {
        var x = Spacing;
        var y = Spacing;

        foreach (var child in Children)
        {
            if (x + ItemWidth > finalSize.Width && x > Spacing)
            {
                x = Spacing;
                y += ItemHeight + Spacing;
            }

            child.Arrange(new Rect(x, y, ItemWidth, ItemHeight));
            x += ItemWidth + Spacing;
        }

        return finalSize;
    }
}
```

## Do/Don't

- Do map WinForms docking/anchoring to explicit row/column semantics.
- Do keep custom layout containers pure (no rendering logic inside measure/arrange).
- Do use `ScrollViewer` intentionally at boundaries where WinForms used `AutoScroll`.
- Don't port `Left/Top/Width/Height` mutation loops directly.
- Don't call `UpdateLayout()` in normal command paths.
- Don't invalidate layout for purely visual property changes.

## Troubleshooting

1. Ported view constantly re-lays out and stutters.
- Check for recursive size mutations during `LayoutUpdated` handlers; remove or debounce.

2. Controls stop resizing as expected after replacing `Anchor`.
- Verify `Grid` row/column sizing and alignments (`Auto`, `*`, `HorizontalAlignment`, `VerticalAlignment`).

3. Custom panel looks correct initially but breaks on resize.
- Ensure wrap/placement math uses `finalSize` in `ArrangeOverride`, not old cached bounds.
