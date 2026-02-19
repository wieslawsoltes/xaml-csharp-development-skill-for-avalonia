# HTML/CSS Range, Progress, Meter, and Scroll Feedback to Avalonia Controls

## Table of Contents
1. Scope and APIs
2. Mapping Table
3. Progress and Meter Patterns
4. Range Slider Patterns
5. Scroll Feedback and Scrollbar Patterns
6. Conversion Example: Upload + Tuning Panel
7. C# Equivalent: Upload + Tuning Panel
8. AOT/Threading Notes
9. Troubleshooting

## Scope and APIs

Primary APIs:

- `RangeBase` (`Minimum`, `Maximum`, `Value`, `SmallChange`, `LargeChange`)
- `ProgressBar` (`IsIndeterminate`, `Orientation`)
- `Slider` (`IsSnapToTickEnabled`, `TickFrequency`, `TickPlacement`)
- `ScrollBar` (`ViewportSize`, `Orientation`, `Visibility`, `AllowAutoHide`)
- `ScrollViewer` attached properties (`HorizontalScrollBarVisibility`, `VerticalScrollBarVisibility`, `AllowAutoHide`)

Reference docs:

- [`03-html-css-animations-transitions-and-motion-system.md`](03-html-css-animations-transitions-and-motion-system)
- [`19-html-css-sticky-scroll-linked-and-anchor-patterns.md`](19-html-css-sticky-scroll-linked-and-anchor-patterns)
- [`57-scrollviewer-offset-anchoring-and-snap-points.md`](../57-scrollviewer-offset-anchoring-and-snap-points)

## Mapping Table

| HTML/CSS idiom | Avalonia mapping |
|---|---|
| `<progress value="42" max="100">` | `ProgressBar Minimum="0" Maximum="100" Value="42"` |
| indeterminate loading bar | `ProgressBar IsIndeterminate="True"` |
| `<meter min max low high optimum>` | `ProgressBar` + threshold styles/classes |
| `<input type="range">` | `Slider` |
| custom scrollbar styling | `ScrollViewer` + `ScrollBar` theme/style selectors |
| scroll position indicator | bind `ScrollBar.Value` to scroll offset model |

## Progress and Meter Patterns

HTML/CSS:

```html
<progress value="58" max="100"></progress>
<meter min="0" max="100" low="30" high="80" optimum="90" value="64"></meter>
```

```css
progress,
meter {
  inline-size: 260px;
  block-size: 12px;
}
```

Avalonia:

```xaml
<StackPanel Spacing="8">
  <ProgressBar Minimum="0" Maximum="100" Value="58" />
  <ProgressBar Minimum="0"
               Maximum="100"
               Value="64"
               Classes="meter-warning" />
  <ProgressBar IsIndeterminate="True" />
</StackPanel>
```

## Range Slider Patterns

HTML/CSS:

```html
<label for="quality">Quality</label>
<input id="quality" type="range" min="0" max="100" step="5" value="65" />
```

```xaml
<StackPanel Spacing="6">
  <TextBlock Text="Quality" />
  <Slider Minimum="0"
          Maximum="100"
          TickFrequency="5"
          IsSnapToTickEnabled="True"
          Value="{CompiledBinding Quality, Mode=TwoWay}" />
</StackPanel>
```

## Scroll Feedback and Scrollbar Patterns

Web apps often restyle scrollbars with vendor selectors and keep a separate progress indicator. In Avalonia, model scroll position explicitly and use `ScrollViewer`/`ScrollBar` properties.

```xaml
<Grid RowDefinitions="Auto,*" RowSpacing="8">
  <ScrollBar Grid.Row="0"
             Orientation="Horizontal"
             Minimum="0"
             Maximum="100"
             ViewportSize="15"
             Value="{CompiledBinding ScrollPercent}" />

  <ScrollViewer Grid.Row="1"
                Height="220"
                VerticalScrollBarVisibility="Auto"
                HorizontalScrollBarVisibility="Disabled"
                AllowAutoHide="True">
    <StackPanel Spacing="6">
      <TextBlock Text="Long content line 1" />
      <TextBlock Text="Long content line 2" />
      <TextBlock Text="Long content line 3" />
      <TextBlock Text="Long content line 4" />
      <TextBlock Text="Long content line 5" />
      <TextBlock Text="Long content line 6" />
      <TextBlock Text="Long content line 7" />
      <TextBlock Text="Long content line 8" />
    </StackPanel>
  </ScrollViewer>
</Grid>
```

## Conversion Example: Upload + Tuning Panel

```html
<section class="panel">
  <h3>Upload</h3>
  <progress value="34" max="100"></progress>

  <label for="compression">Compression</label>
  <input id="compression" type="range" min="0" max="100" step="1" value="72" />
</section>
```

```css
.panel {
  display: grid;
  gap: 10px;
  max-width: 420px;
}
```

```xaml
<StackPanel Spacing="10" MaxWidth="420">
  <TextBlock Text="Upload" FontWeight="SemiBold" />
  <ProgressBar Minimum="0"
               Maximum="100"
               Value="{CompiledBinding UploadPercent}" />

  <TextBlock Text="Compression" />
  <Slider Minimum="0"
          Maximum="100"
          TickFrequency="1"
          IsSnapToTickEnabled="True"
          Value="{CompiledBinding Compression, Mode=TwoWay}" />

  <TextBlock Text="Scroll feedback" FontWeight="SemiBold" />
  <ScrollBar Orientation="Horizontal"
             Minimum="0"
             Maximum="100"
             ViewportSize="20"
             Value="{CompiledBinding ScrollPercent}" />
</StackPanel>
```

## C# Equivalent: Upload + Tuning Panel

```csharp
using Avalonia.Controls;
using Avalonia.Controls.Primitives;

var panel = new StackPanel
{
    Spacing = 10,
    MaxWidth = 420
};

var uploadProgress = new ProgressBar
{
    Minimum = 0,
    Maximum = 100,
    Value = 34
};

var compressionSlider = new Slider
{
    Minimum = 0,
    Maximum = 100,
    TickFrequency = 1,
    IsSnapToTickEnabled = true,
    Value = 72
};

var scrollIndicator = new ScrollBar
{
    Orientation = Avalonia.Layout.Orientation.Horizontal,
    Minimum = 0,
    Maximum = 100,
    ViewportSize = 20,
    Value = 0
};

compressionSlider.PropertyChanged += (_, e) =>
{
    if (e.Property == RangeBase.ValueProperty)
        uploadProgress.Value = compressionSlider.Value / 2;
};

panel.Children.Add(new TextBlock { Text = "Upload" });
panel.Children.Add(uploadProgress);
panel.Children.Add(new TextBlock { Text = "Compression" });
panel.Children.Add(compressionSlider);
panel.Children.Add(new TextBlock { Text = "Scroll feedback" });
panel.Children.Add(scrollIndicator);
```

## AOT/Threading Notes

- Range controls are binding-friendly; prefer typed VM numeric properties over converter-heavy string mappings.
- Apply progress updates from background operations via `Dispatcher.UIThread`.

## Troubleshooting

1. Slider updates but UI value jumps unexpectedly.
- Check `Minimum`/`Maximum` consistency and remove duplicate value coercion in VM logic.

2. Progress bar appears static.
- Ensure bound value actually changes and stays within range.

3. Scrollbar thumb size looks wrong.
- Set `ViewportSize` to a meaningful proportion of visible content.
