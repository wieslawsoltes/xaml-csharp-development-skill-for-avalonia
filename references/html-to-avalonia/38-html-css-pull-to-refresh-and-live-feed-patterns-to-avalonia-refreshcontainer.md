# HTML/CSS Pull-to-Refresh and Live Feed Patterns to Avalonia RefreshContainer

## Table of Contents
1. Scope and APIs
2. Mapping Table
3. Pull-to-Refresh Event Contract Mapping
4. Conversion Example: Mobile Activity Feed
5. C# Equivalent: Activity Feed with Deferral
6. AOT/Threading Notes
7. Troubleshooting

## Scope and APIs

Primary APIs:

- `RefreshContainer` (`RefreshRequested`, `PullDirection`, `RequestRefresh()`, `Visualizer`)
- `RefreshVisualizer` (`RefreshRequested`, `RefreshVisualizerState`, `Orientation`, `RequestRefresh()`)
- `RefreshRequestedEventArgs.GetDeferral()` and `RefreshCompletionDeferral.Complete()`
- feed composition controls: `ScrollViewer`, `ItemsControl`, `Border`

Reference docs:

- [`12-html-css-animations-transitions-and-motion-system.md`](12-html-css-animations-transitions-and-motion-system)
- [`06-html-rich-content-lists-cards-tables-and-virtualization.md`](06-html-rich-content-lists-cards-tables-and-virtualization)
- [`03-reactive-threading.md`](../03-reactive-threading)

## Mapping Table

| HTML/CSS idiom | Avalonia mapping |
|---|---|
| touch pull-to-refresh gesture | `RefreshContainer PullDirection` + `RefreshRequested` |
| refresh spinner state machine | `RefreshVisualizerState` |
| explicit refresh button/JS call | `RequestRefresh()` |
| async refresh completion callback | `GetDeferral()` / `Complete()` |

## Pull-to-Refresh Event Contract Mapping

HTML/JS baseline:

```html
<section class="feed" id="feed"></section>
<button id="refresh">Refresh</button>
```

```css
.feed {
  overflow-y: auto;
  min-height: 60vh;
}
```

```js
const feed = document.getElementById("feed");
const refresh = document.getElementById("refresh");

async function reloadFeed() {
  // fetch latest feed
}

refresh?.addEventListener("click", async () => {
  await reloadFeed();
});
```

Avalonia pattern:

```xaml
<RefreshContainer PullDirection="TopToBottom"
                  RefreshRequested="OnFeedRefreshRequested">
  <ScrollViewer>
    <ItemsControl ItemsSource="{CompiledBinding FeedItems}" />
  </ScrollViewer>
</RefreshContainer>
```

## Conversion Example: Mobile Activity Feed

```html
<section class="activity-feed">
  <article class="item">Build #102 completed</article>
  <article class="item">Deployment started</article>
  <article class="item">Smoke tests passed</article>
</section>
```

```css
.activity-feed {
  display: grid;
  gap: .5rem;
}
.activity-feed .item {
  border: 1px solid #2a3348;
  border-radius: .5rem;
  padding: .6rem .75rem;
}
```

```xaml
<RefreshContainer PullDirection="TopToBottom"
                  RefreshRequested="OnFeedRefreshRequested">
  <ScrollViewer>
    <ItemsControl ItemsSource="{CompiledBinding FeedItems}">
      <ItemsControl.ItemTemplate>
        <DataTemplate>
          <Border BorderBrush="#2A3348"
                  BorderThickness="1"
                  CornerRadius="8"
                  Padding="10,8"
                  Margin="0,0,0,8">
            <TextBlock Text="{Binding}" />
          </Border>
        </DataTemplate>
      </ItemsControl.ItemTemplate>
    </ItemsControl>
  </ScrollViewer>
</RefreshContainer>
```

## C# Equivalent: Activity Feed with Deferral

```csharp
using System;
using System.Threading.Tasks;
using Avalonia.Controls;

var feedItems = new[]
{
    "Build #102 completed",
    "Deployment started",
    "Smoke tests passed"
};

var itemsControl = new ItemsControl { ItemsSource = feedItems };

var refreshContainer = new RefreshContainer
{
    PullDirection = PullDirection.TopToBottom,
    Content = new ScrollViewer { Content = itemsControl }
};

refreshContainer.RefreshRequested += async (_, e) =>
{
    var deferral = e.GetDeferral();
    try
    {
        await Task.Delay(250);
        // Reload feed items from service and update bound collection.
    }
    finally
    {
        deferral.Complete();
    }
};

// Programmatic equivalent of a "Refresh" button in web UI.
refreshContainer.RequestRefresh();
```

## AOT/Threading Notes

- Keep refresh pipelines explicit and event-driven; avoid dynamic invocation patterns for feed updates.
- Complete refresh deferrals in `finally` blocks to avoid stuck refreshing state.
- Marshal feed collection updates to `Dispatcher.UIThread` when refresh work runs off-thread.

## Troubleshooting

1. Pull gesture never triggers refresh.
- Ensure content is scrollable and `RefreshContainer` wraps the scrolling surface.

2. Indicator remains active forever.
- Confirm `GetDeferral()` result is always completed.

3. Programmatic refresh does nothing.
- Verify the control is attached to visual tree and has a refresh handler.
