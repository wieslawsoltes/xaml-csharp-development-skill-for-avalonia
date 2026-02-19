# HTML/CSS `position: sticky`, Scroll-Linked, and Anchor Patterns in Avalonia

## Table of Contents
1. Scope and APIs
2. Sticky Pattern Mapping
3. Scroll-Linked UI Pattern Mapping
4. Anchor/Snap Mapping
5. Conversion Example: Sticky Header + Anchored Feed
6. C# Equivalent: Sticky Header + Anchored Feed
7. Troubleshooting

## Scope and APIs

Primary APIs:

- `ScrollViewer` offsets/snap/anchor APIs
- layout composition with `Grid` for persistent header regions
- scroll change event handling for progressive effects

Reference docs:

- [`57-scrollviewer-offset-anchoring-and-snap-points.md`](../57-scrollviewer-offset-anchoring-and-snap-points)
- [`00-html-css-layout-box-model-and-positioning.md`](00-html-css-layout-box-model-and-positioning)

## Sticky Pattern Mapping

HTML/CSS sticky:

```html
<section class="feed">
  <header class="header">Activity</header>
  <div class="content">...</div>
</section>
```

```css
.header { position: sticky; top: 0; z-index: 100; }
```

Avalonia equivalent:

- separate fixed header row from scrollable content.

```xaml
<Grid RowDefinitions="Auto,*">
  <Border Grid.Row="0" ZIndex="100" Classes="header" />
  <ScrollViewer Grid.Row="1">
    <ItemsControl ItemsSource="{CompiledBinding Items}" />
  </ScrollViewer>
</Grid>
```

## Scroll-Linked UI Pattern Mapping

Web pattern (fade/compact toolbar on scroll) maps to observing `ScrollViewer.Offset` and toggling classes/properties.

```csharp
void OnScrollChanged(object? s, ScrollChangedEventArgs _)
{
    if (s is not ScrollViewer scrollViewer)
        return;

    var compact = scrollViewer.Offset.Y > 24;
    Header.Classes.Set("compact", compact);
}
```

## Anchor/Snap Mapping

| Web pattern | Avalonia mapping |
|---|---|
| CSS scroll snap | `ScrollViewer` snap-point surface |
| anchor candidate logic | `RegisterAnchorCandidate` / `UnregisterAnchorCandidate` |
| scroll chaining/inertia toggles | attached `ScrollViewer` behavior options |

## Conversion Example: Sticky Header + Anchored Feed

```html
<section class="feed-shell">
  <header class="feed-header">Activity</header>
  <ul class="feed-list">
    <li>...</li>
  </ul>
</section>
```

```css
.feed-shell { height: 100vh; overflow: auto; }
.feed-header { position: sticky; top: 0; z-index: 100; }
```

```xaml
<Grid RowDefinitions="56,*">
  <Border x:Name="Header" Grid.Row="0" Classes="feed-header" />

  <ListBox Grid.Row="1"
           ItemsSource="{CompiledBinding FeedItems}"
           ScrollViewer.VerticalScrollBarVisibility="Auto" />
</Grid>
```

## C# Equivalent: Sticky Header + Anchored Feed

```csharp
using Avalonia.Controls;

var shell = new Grid { RowDefinitions = RowDefinitions.Parse("56,*") };

var header = new Border();
Grid.SetRow(header, 0);

var feedList = new ListBox();
var scrollHost = new ScrollViewer
{
    VerticalScrollBarVisibility = ScrollBarVisibility.Auto,
    Content = feedList
};
Grid.SetRow(scrollHost, 1);

scrollHost.ScrollChanged += (_, _) =>
{
    header.Classes.Set("compact", scrollHost.Offset.Y > 24);
};

shell.Children.Add(header);
shell.Children.Add(scrollHost);
```

## Troubleshooting

1. Sticky emulation lags behind scroll.
- Keep scroll event handlers lightweight and state-only.

2. Anchoring appears inconsistent with dynamic row heights.
- Use stable item sizing where possible; review anchor candidate registration.

3. Snap points feel too aggressive.
- Tune snap alignment/type and allow inertia where UX requires it.
