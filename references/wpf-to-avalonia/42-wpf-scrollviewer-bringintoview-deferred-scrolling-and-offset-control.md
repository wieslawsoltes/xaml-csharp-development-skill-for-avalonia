# WPF ScrollViewer BringIntoView, Deferred Scrolling, and Offset Control to Avalonia

## Table of Contents
1. Scope and APIs
2. Scroll Behavior Mapping
3. Conversion Example
4. Avalonia C# Equivalent
5. Troubleshooting

## Scope and APIs

Primary WPF APIs:

- `ScrollViewer` offsets and commands
- `ScrollChanged`
- `BringIntoView()`
- `IsDeferredScrollingEnabled`

Primary Avalonia APIs:

- `ScrollViewer.Offset`, `Extent`, `Viewport`
- `ScrollViewer.ScrollChanged` (`ScrollChangedEventArgs`)
- `Control.BringIntoView()`
- `ScrollViewer.IsDeferredScrollingEnabled`
- `ScrollViewer.BringIntoViewOnFocusChange`

## Scroll Behavior Mapping

| WPF | Avalonia |
|---|---|
| `HorizontalOffset`/`VerticalOffset` | `Offset.X`/`Offset.Y` |
| `ScrollViewer.ScrollChanged` | `ScrollViewer.ScrollChanged` |
| `BringIntoView()` | `BringIntoView()` (same intent) |
| `IsDeferredScrollingEnabled` | `IsDeferredScrollingEnabled` |

## Conversion Example

WPF XAML:

```xaml
<ScrollViewer x:Name="FeedScroll"
              VerticalScrollBarVisibility="Auto"
              IsDeferredScrollingEnabled="True">
  <ItemsControl ItemsSource="{Binding Messages}" />
</ScrollViewer>
```

Avalonia XAML:

```xaml
<UserControl xmlns="https://github.com/avaloniaui"
             xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
             xmlns:vm="using:MyApp.ViewModels"
             x:DataType="vm:FeedViewModel">
  <Grid RowDefinitions="Auto,*" RowSpacing="8">
    <StackPanel Orientation="Horizontal" Spacing="8">
      <Button Content="Page Down" Command="{CompiledBinding PageDownCommand}" />
      <Button Content="Jump To Latest" Command="{CompiledBinding JumpToLatestCommand}" />
    </StackPanel>

    <ScrollViewer x:Name="FeedScroll"
                  Grid.Row="1"
                  IsDeferredScrollingEnabled="True"
                  BringIntoViewOnFocusChange="True"
                  AllowAutoHide="True">
      <ItemsControl ItemsSource="{CompiledBinding Messages}">
        <ItemsControl.ItemTemplate>
          <DataTemplate x:DataType="vm:MessageRowViewModel">
            <TextBlock Margin="0,0,0,6" Text="{CompiledBinding Text}" TextWrapping="Wrap" />
          </DataTemplate>
        </ItemsControl.ItemTemplate>
      </ItemsControl>
    </ScrollViewer>
  </Grid>
</UserControl>
```

## Avalonia C# Equivalent

```csharp
using Avalonia;
using Avalonia.Controls;

var scroll = new ScrollViewer
{
    IsDeferredScrollingEnabled = true,
    BringIntoViewOnFocusChange = true
};

scroll.ScrollChanged += (_, e) =>
{
    var delta = e.OffsetDelta;
    viewModel.LastScrollDelta = delta;
};

scroll.Offset = new Vector(0, 240);
scroll.PageDown();
scroll.LineDown();
scroll.ScrollToEnd();

// For a specific element in the scrolled content:
selectedRowControl.BringIntoView();
```

## Troubleshooting

1. Migrated offset logic appears inverted or clamped.
- Use `Offset.X/Y` and validate against `Extent`/`Viewport` rather than raw pixel assumptions.

2. Selection changes but item is not revealed.
- Enable `AutoScrollToSelectedItem` on selecting controls or call `BringIntoView()` on the realized container.

3. Scrolling feels too eager during drag.
- Turn on `IsDeferredScrollingEnabled` for parity with deferred WPF drag behavior.
