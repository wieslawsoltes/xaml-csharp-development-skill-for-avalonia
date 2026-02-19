# HTML/CSS Resizable Split Panes and Drag Handles to Avalonia GridSplitter and Thumb

## Table of Contents
1. Scope and APIs
2. Mapping Table
3. CSS `resize` and Splitter Pattern
4. Advanced GridSplitter Behavior
5. Custom Drag Handle Pattern with Thumb
6. Conversion Example: Log Console Layout
7. C# Equivalent: Log Console Layout
8. AOT/Threading Notes
9. Troubleshooting

## Scope and APIs

Primary APIs:

- `Grid` (`ColumnDefinitions`, `RowDefinitions`)
- `GridSplitter` (`ResizeDirection`, `ResizeBehavior`, `ShowsPreview`, `KeyboardIncrement`, `DragIncrement`, `PreviewContent`)
- `Thumb` (`DragStarted`, `DragDelta`, `DragCompleted`)
- supporting layout controls: `Border`, `ScrollViewer`, `TextBox`

Reference docs:

- [`15-html-css-data-table-list-and-master-detail-patterns.md`](15-html-css-data-table-list-and-master-detail-patterns)
- [`30-layout-measure-arrange-and-custom-layout-controls.md`](../30-layout-measure-arrange-and-custom-layout-controls)
- [`21-custom-layout-authoring.md`](../21-custom-layout-authoring)

## Mapping Table

| HTML/CSS idiom | Avalonia mapping |
|---|---|
| `display: grid` split columns | `Grid` with star/pixel columns |
| drag separator (`col-resize`) | `GridSplitter` |
| splitter preview ghost line | `GridSplitter ShowsPreview="True"` |
| keyboard resize step | `GridSplitter KeyboardIncrement` |
| custom drag bar (`pointermove`) | `Thumb` + `DragDelta` |

## CSS `resize` and Splitter Pattern

HTML/CSS:

```html
<section class="two-pane">
  <aside class="left">Navigator</aside>
  <div class="splitter" aria-hidden="true"></div>
  <main class="right">Editor</main>
</section>
```

```css
.two-pane {
  display: grid;
  grid-template-columns: 300px 6px 1fr;
}
.splitter {
  cursor: col-resize;
  background: #25324a;
}
```

Avalonia:

```xaml
<Grid ColumnDefinitions="300,6,*">
  <Border Grid.Column="0" Background="#141B2A" />

  <GridSplitter Grid.Column="1"
                Width="6"
                ResizeDirection="Columns"
                ResizeBehavior="PreviousAndNext"
                ShowsPreview="True"
                KeyboardIncrement="16"
                DragIncrement="4" />

  <Border Grid.Column="2" Background="#0F1624" />
</Grid>
```

## Advanced GridSplitter Behavior

`ResizeBehavior` and increments let you control desktop-like resize feel:

```xaml
<GridSplitter Grid.Column="1"
              Width="8"
              ResizeDirection="Columns"
              ResizeBehavior="PreviousAndNext"
              ShowsPreview="True"
              KeyboardIncrement="20"
              DragIncrement="2" />
```

## Custom Drag Handle Pattern with Thumb

For custom pane logic (not direct grid definition resizing), map JS pointer-drag logic to `Thumb` events.

```html
<div class="timeline">
  <div class="handle"></div>
</div>
```

```css
.handle {
  width: 12px;
  cursor: ew-resize;
}
```

```xaml
<Thumb Width="12"
       HorizontalAlignment="Right"
       DragDelta="OnPaneHandleDragDelta" />
```

## Conversion Example: Log Console Layout

```html
<section class="console-layout">
  <main class="results">Query results</main>
  <div class="splitter"></div>
  <aside class="logs">Logs</aside>
</section>
```

```css
.console-layout {
  display: grid;
  grid-template-rows: 1fr 6px 240px;
  min-block-size: 32rem;
}
.splitter { cursor: row-resize; }
```

```xaml
<Grid RowDefinitions="*,6,240" MinHeight="520">
  <Border Grid.Row="0" Background="#101725">
    <TextBlock Margin="10" Text="Query results" />
  </Border>

  <GridSplitter Grid.Row="1"
                Height="6"
                ResizeDirection="Rows"
                ResizeBehavior="PreviousAndNext"
                ShowsPreview="True"
                KeyboardIncrement="24"
                DragIncrement="3" />

  <Border Grid.Row="2" Background="#0A101B">
    <ScrollViewer>
      <TextBox AcceptsReturn="True"
               IsReadOnly="True"
               Text="Logs..."
               TextWrapping="NoWrap" />
    </ScrollViewer>
  </Border>
</Grid>
```

## C# Equivalent: Log Console Layout

```csharp
using Avalonia.Controls;
using Avalonia.Input;

var layout = new Grid
{
    RowDefinitions = new RowDefinitions("*,6,240"),
    MinHeight = 520
};

layout.Children.Add(new Border
{
    [Grid.RowProperty] = 0,
    Background = Avalonia.Media.Brushes.Transparent,
    Child = new TextBlock { Margin = new Avalonia.Thickness(10), Text = "Query results" }
});

var splitter = new GridSplitter
{
    [Grid.RowProperty] = 1,
    Height = 6,
    ResizeDirection = GridResizeDirection.Rows,
    ResizeBehavior = GridResizeBehavior.PreviousAndNext,
    ShowsPreview = true,
    KeyboardIncrement = 24,
    DragIncrement = 3,
    Cursor = new Cursor(StandardCursorType.SizeNorthSouth)
};

var logs = new TextBox
{
    AcceptsReturn = true,
    IsReadOnly = true,
    TextWrapping = Avalonia.Media.TextWrapping.NoWrap,
    Text = "Logs..."
};

layout.Children.Add(splitter);
layout.Children.Add(new Border
{
    [Grid.RowProperty] = 2,
    Child = new ScrollViewer { Content = logs }
});

var customHandle = new Avalonia.Controls.Primitives.Thumb { Width = 12 };
customHandle.DragDelta += (_, _) =>
{
    // Update custom pane sizing state here for non-grid splitter scenarios.
};
```

## AOT/Threading Notes

- Keep pane sizes in strongly typed VM state (for example `GridLength`-compatible values) and persist them explicitly.
- Apply size updates on `Dispatcher.UIThread` when restored from async settings storage.

## Troubleshooting

1. Splitter cannot resize panes.
- Ensure adjacent rows/columns can change (avoid all fixed sizes).

2. Keyboard resize does nothing.
- Verify splitter can receive focus and `KeyboardIncrement` is non-zero.

3. Dragging feels too jumpy.
- Decrease `DragIncrement` or disable snapping increments for finer control.
