# HTML/CSS Headless Tablist and Segmented Navigation to Avalonia TabStrip

## Table of Contents
1. Scope and APIs
2. Mapping Table
3. Headless Tablist Pattern
4. Segmented Navigation Pattern
5. Conversion Example: Settings Surface with TabStrip
6. C# Equivalent: Settings Surface with TabStrip
7. AOT/Threading Notes
8. Troubleshooting

## Scope and APIs

Primary APIs:

- `TabStrip` and `TabStripItem`
- `SelectingItemsControl` selection API (`SelectedIndex`, `SelectedItem`, `SelectionChanged`, `SelectionMode`)
- `TransitioningContentControl` for panel content transitions
- `ContentControl` for explicit panel host composition

Reference docs:

- [`29-html-css-tabs-offcanvas-and-carousel-shell-patterns.md`](29-html-css-tabs-offcanvas-and-carousel-shell-patterns)
- [`13-html-css-navigation-tabs-sidebars-breadcrumbs-and-routing-patterns.md`](13-html-css-navigation-tabs-sidebars-breadcrumbs-and-routing-patterns)
- [`10-templated-controls-and-control-themes.md`](../10-templated-controls-and-control-themes)

## Mapping Table

| HTML/CSS idiom | Avalonia mapping |
|---|---|
| headless tabs (`role="tablist"`) | `TabStrip` |
| tab button (`role="tab"`) | `TabStripItem` |
| selected tab state (`aria-selected`) | `SelectedIndex` / `SelectedItem` |
| tab panel outlet | `ContentControl` or `TransitioningContentControl` |
| segmented control navigation | styled `TabStrip` |

## Headless Tablist Pattern

HTML/CSS baseline:

```html
<nav class="tablist" role="tablist" aria-label="Settings sections">
  <button role="tab" aria-selected="true">General</button>
  <button role="tab" aria-selected="false">Security</button>
  <button role="tab" aria-selected="false">Billing</button>
</nav>
<section class="tabpanel">...</section>
```

```css
.tablist {
  display: inline-flex;
  gap: .25rem;
}
.tablist [aria-selected="true"] {
  background: #2f6fed;
  color: #fff;
}
```

Avalonia pattern:

```xaml
<StackPanel Spacing="10">
  <TabStrip SelectedIndex="{CompiledBinding SelectedTabIndex, Mode=TwoWay}">
    <TabStripItem Content="General" />
    <TabStripItem Content="Security" />
    <TabStripItem Content="Billing" />
  </TabStrip>

  <TransitioningContentControl Content="{CompiledBinding CurrentPanelVm}" />
</StackPanel>
```

## Segmented Navigation Pattern

HTML/CSS segmented control:

```html
<div class="segmented" role="tablist">
  <button role="tab" aria-selected="true">Week</button>
  <button role="tab">Month</button>
  <button role="tab">Quarter</button>
</div>
```

Avalonia with `TabStrip` styling intent:

```xaml
<TabStrip Classes="segmented"
          SelectionChanged="OnRangeTabChanged">
  <TabStripItem Content="Week" />
  <TabStripItem Content="Month" />
  <TabStripItem Content="Quarter" />
</TabStrip>
```

## Conversion Example: Settings Surface with TabStrip

```html
<section class="settings-shell">
  <nav class="tablist" role="tablist">
    <button role="tab" aria-selected="true">General</button>
    <button role="tab">Integrations</button>
    <button role="tab">Security</button>
  </nav>
  <section class="panel">Current panel content</section>
</section>
```

```css
.settings-shell {
  display: grid;
  gap: .75rem;
}
```

```xaml
<StackPanel Spacing="12">
  <TabStrip SelectedIndex="{CompiledBinding SelectedSettingsTab, Mode=TwoWay}">
    <TabStripItem Content="General" />
    <TabStripItem Content="Integrations" />
    <TabStripItem Content="Security" />
  </TabStrip>

  <Border BorderBrush="#2A3348" BorderThickness="1" CornerRadius="8" Padding="12">
    <TransitioningContentControl Content="{CompiledBinding CurrentSettingsPanelVm}" />
  </Border>
</StackPanel>
```

## C# Equivalent: Settings Surface with TabStrip

```csharp
using Avalonia.Controls;
using Avalonia.Controls.Primitives;

var shell = new StackPanel { Spacing = 12 };

var tabStrip = new TabStrip();
tabStrip.Items.Add(new TabStripItem { Content = "General" });
tabStrip.Items.Add(new TabStripItem { Content = "Integrations" });
tabStrip.Items.Add(new TabStripItem { Content = "Security" });
tabStrip.SelectedIndex = 0;

var panelHost = new TransitioningContentControl
{
    Content = new TextBlock { Text = "General settings panel" }
};

tabStrip.SelectionChanged += (_, _) =>
{
    panelHost.Content = tabStrip.SelectedIndex switch
    {
        0 => new TextBlock { Text = "General settings panel" },
        1 => new TextBlock { Text = "Integrations panel" },
        2 => new TextBlock { Text = "Security panel" },
        _ => new TextBlock { Text = "Unknown panel" }
    };
};

shell.Children.Add(tabStrip);
shell.Children.Add(new Border
{
    BorderBrush = Avalonia.Media.Brushes.Gray,
    BorderThickness = new Avalonia.Thickness(1),
    Padding = new Avalonia.Thickness(12),
    Child = panelHost
});
```

## AOT/Threading Notes

- Keep selected-tab state as a typed index/enum in view model and map to panel content deterministically.
- If tab content loads asynchronously, update panel host on `Dispatcher.UIThread`.

## Troubleshooting

1. Tab header selection changes but panel does not.
- Wire `SelectionChanged` to update a content host (`ContentControl`/`TransitioningContentControl`).

2. Styling looks like default tabs, not segmented control.
- Add custom `TabStrip` styles/class selectors for segmented appearance.

3. Keyboard tab navigation feels off.
- Verify `TabStrip` remains focusable and selection mode is single-select behavior.
