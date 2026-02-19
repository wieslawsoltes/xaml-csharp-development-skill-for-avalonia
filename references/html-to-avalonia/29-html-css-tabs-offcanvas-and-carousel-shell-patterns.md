# HTML/CSS Tabs, Off-Canvas Navigation, and Carousel Shells to Avalonia Controls

## Table of Contents
1. Scope and APIs
2. Mapping Table
3. Tabs Pattern
4. Off-Canvas Sidebar Pattern
5. Carousel Pattern
6. Conversion Example: Product Workspace Shell
7. C# Equivalent: Product Workspace Shell
8. AOT/Threading Notes
9. Troubleshooting

## Scope and APIs

Primary APIs:

- `TabControl`, `TabItem` (`SelectedItem`, `SelectedIndex`, `TabStripPlacement`)
- `SplitView` (`IsPaneOpen`, `DisplayMode`, `OpenPaneLength`, `CompactPaneLength`, `PanePlacement`)
- `Carousel` (`PageTransition`, `Next()`, `Previous()`)
- `TransitioningContentControl` for animated content swaps

Reference docs:

- [`13-html-css-navigation-tabs-sidebars-breadcrumbs-and-routing-patterns.md`](13-html-css-navigation-tabs-sidebars-breadcrumbs-and-routing-patterns)
- [`05-html-shell-navigation-popups-and-layering-patterns.md`](05-html-shell-navigation-popups-and-layering-patterns)
- [`03-html-css-animations-transitions-and-motion-system.md`](03-html-css-animations-transitions-and-motion-system)

## Mapping Table

| HTML/CSS idiom | Avalonia mapping |
|---|---|
| tablist (`role="tablist"`) + tabpanels | `TabControl` + `TabItem` |
| off-canvas sidebar (`transform: translateX(...)`) | `SplitView IsPaneOpen` + `DisplayMode` |
| CSS scroll-snap carousel | `Carousel` with `PageTransition` |
| animated route outlet | `TransitioningContentControl` |

## Tabs Pattern

HTML/CSS:

```html
<nav class="tabs" role="tablist">
  <button role="tab" aria-selected="true">Overview</button>
  <button role="tab">Analytics</button>
  <button role="tab">Billing</button>
</nav>
```

```xaml
<TabControl SelectedIndex="{CompiledBinding SelectedTabIndex, Mode=TwoWay}"
            TabStripPlacement="Top">
  <TabItem Header="Overview" />
  <TabItem Header="Analytics" />
  <TabItem Header="Billing" />
</TabControl>
```

## Off-Canvas Sidebar Pattern

HTML/CSS baseline:

```css
.sidebar {
  transform: translateX(-100%);
  transition: transform .2s ease;
}
.sidebar.open {
  transform: translateX(0);
}
```

Avalonia equivalent:

```xaml
<SplitView DisplayMode="CompactOverlay"
           IsPaneOpen="{CompiledBinding IsNavOpen, Mode=TwoWay}"
           OpenPaneLength="280"
           CompactPaneLength="56"
           PanePlacement="Left">
  <SplitView.Pane>
    <StackPanel Spacing="6">
      <Button Content="Overview" />
      <Button Content="Analytics" />
      <Button Content="Billing" />
    </StackPanel>
  </SplitView.Pane>

  <TransitioningContentControl Content="{CompiledBinding CurrentPageVm}" />
</SplitView>
```

## Carousel Pattern

HTML/CSS often implements carousels with scroll containers and `scroll-snap-type`. In Avalonia, `Carousel` gives selection + transition behavior directly.

```xaml
<Carousel SelectedIndex="{CompiledBinding HeroIndex, Mode=TwoWay}">
  <Border Padding="16"><TextBlock Text="Slide 1" /></Border>
  <Border Padding="16"><TextBlock Text="Slide 2" /></Border>
  <Border Padding="16"><TextBlock Text="Slide 3" /></Border>
</Carousel>
```

## Conversion Example: Product Workspace Shell

```html
<section class="workspace">
  <aside class="sidebar open">...</aside>
  <main>
    <nav class="tabs">...</nav>
    <section class="hero-carousel">...</section>
  </main>
</section>
```

```css
.workspace {
  display: grid;
  grid-template-columns: 280px 1fr;
  gap: 12px;
}
```

```xaml
<SplitView DisplayMode="Inline"
           OpenPaneLength="280"
           IsPaneOpen="True">
  <SplitView.Pane>
    <StackPanel Spacing="6">
      <Button Content="Overview" Command="{CompiledBinding GoOverviewCommand}" />
      <Button Content="Analytics" Command="{CompiledBinding GoAnalyticsCommand}" />
      <Button Content="Billing" Command="{CompiledBinding GoBillingCommand}" />
    </StackPanel>
  </SplitView.Pane>

  <StackPanel Spacing="10">
    <TabControl SelectedIndex="{CompiledBinding SelectedTabIndex, Mode=TwoWay}">
      <TabItem Header="Overview" />
      <TabItem Header="Analytics" />
      <TabItem Header="Billing" />
    </TabControl>

    <Carousel SelectedIndex="{CompiledBinding HeroIndex, Mode=TwoWay}">
      <Border Padding="16"><TextBlock Text="Revenue highlights" /></Border>
      <Border Padding="16"><TextBlock Text="Retention highlights" /></Border>
      <Border Padding="16"><TextBlock Text="Cost highlights" /></Border>
    </Carousel>
  </StackPanel>
</SplitView>
```

## C# Equivalent: Product Workspace Shell

```csharp
using Avalonia.Controls;

var splitView = new SplitView
{
    DisplayMode = SplitViewDisplayMode.Inline,
    OpenPaneLength = 280,
    CompactPaneLength = 56,
    IsPaneOpen = true,
    Pane = new StackPanel
    {
        Spacing = 6,
        Children =
        {
            new Button { Content = "Overview" },
            new Button { Content = "Analytics" },
            new Button { Content = "Billing" }
        }
    }
};

var tabs = new TabControl
{
    Items =
    {
        new TabItem { Header = "Overview" },
        new TabItem { Header = "Analytics" },
        new TabItem { Header = "Billing" }
    }
};

var carousel = new Carousel();
carousel.Items.Add(new Border { Padding = new Avalonia.Thickness(16), Child = new TextBlock { Text = "Revenue highlights" } });
carousel.Items.Add(new Border { Padding = new Avalonia.Thickness(16), Child = new TextBlock { Text = "Retention highlights" } });
carousel.Items.Add(new Border { Padding = new Avalonia.Thickness(16), Child = new TextBlock { Text = "Cost highlights" } });

var main = new StackPanel { Spacing = 10 };
main.Children.Add(tabs);
main.Children.Add(carousel);

splitView.Content = main;
```

## AOT/Threading Notes

- Keep selected tab/slide state in typed VM properties to preserve deterministic restore/navigation.
- Update pane-open and selected-content state from background signals on `Dispatcher.UIThread`.

## Troubleshooting

1. SplitView pane overlays unexpected content.
- Re-check `DisplayMode` choice (`Overlay`, `CompactOverlay`, `CompactInline`, `Inline`).

2. Carousel appears static.
- Verify `SelectedIndex` changes and items are present.

3. Tab content re-creates too often.
- Keep view models stable and avoid creating heavyweight content per selection event.
