# HTML Shell, Navigation, Popups, and Layering Patterns to Avalonia

## Table of Contents
1. Scope and APIs
2. HTML Landmark Mapping
3. Navigation Pattern Mapping
4. Overlay/Popup Pattern Mapping
5. Layering and Z-Order Strategy
6. HTML/CSS Shell Comparison
7. Conversion Example: SaaS App Shell
8. C# Equivalent: SaaS App Shell
9. AOT/Threading Notes
10. Troubleshooting

## Scope and APIs

Primary APIs:

- shell: `Window`, `TopLevel`, `Grid`, `DockPanel`, `SplitView`, `TabControl`
- navigation/view switching: `ContentControl`, `TransitioningContentControl`, `DataTemplate`
- overlays: `Popup`, `Flyout`, `ContextMenu`, `ToolTip`, overlay/adorner layers
- menus/chrome: `Menu`, `MenuItem`, `NativeMenuBar`, `TitleBar`, tray/notification helpers

Reference docs:

- [`13-windowing-and-custom-decorations.md`](../13-windowing-and-custom-decorations)
- [`25-popups-flyouts-tooltips-and-overlays.md`](../25-popups-flyouts-tooltips-and-overlays)
- [`53-menu-controls-contextmenu-and-menuflyout-patterns.md`](../53-menu-controls-contextmenu-and-menuflyout-patterns)
- [`48-toplevel-window-and-runtime-services.md`](../48-toplevel-window-and-runtime-services)

## HTML Landmark Mapping

| HTML landmark pattern | Avalonia composition pattern |
|---|---|
| `<header>` | top row in `Grid` or top-docked element in `DockPanel` |
| `<nav>` / side rail | `SplitView` pane, left `Grid` column, or `TabControl` navigation |
| `<main>` | primary content `ContentControl` / `TransitioningContentControl` |
| `<aside>` | secondary panel in extra column or pane |
| `<footer>` | bottom row in `Grid` |

## Navigation Pattern Mapping

| Web pattern | Avalonia pattern |
|---|---|
| client router outlet | `ContentControl Content="{CompiledBinding CurrentViewModel}"` + templates |
| tab navigation | `TabControl` |
| drawer/sidebar | `SplitView` |
| breadcrumb toolbar area | `DockPanel` with command controls |

## Overlay/Popup Pattern Mapping

| Web pattern | Avalonia pattern |
|---|---|
| modal dialog | owned `Window`/dialog flow |
| popover | `Popup`/`Flyout` |
| tooltip | `ToolTip.Tip` attached property |
| context menu | `ContextMenu` |
| notification toast | `WindowNotificationManager` |

## Layering and Z-Order Strategy

- same parent overlap: use `ZIndex`.
- top-level transient surfaces: use `Popup`/`Flyout` rather than manual absolute overlays.
- focus-sensitive overlays: prefer built-in light-dismiss and overlay layer behavior.

## HTML/CSS Shell Comparison

HTML/CSS:

```html
<div class="app-shell">
  <header class="topbar">...</header>
  <aside class="sidebar">...</aside>
  <main class="main">...</main>
</div>
```

```css
.app-shell {
  display: grid;
  grid-template-columns: 260px 1fr;
  grid-template-rows: 56px 1fr;
  min-height: 100vh;
}
.topbar { grid-column: 1 / span 2; position: sticky; top: 0; z-index: 100; }
.sidebar { grid-row: 2; }
.main { grid-row: 2; overflow: auto; }
```

Avalonia:

```xaml
<Grid RowDefinitions="56,*" ColumnDefinitions="260,*">
  <Border Grid.Row="0" Grid.ColumnSpan="2" ZIndex="100" Classes="topbar" />
  <Border Grid.Row="1" Grid.Column="0" Classes="sidebar" />
  <ScrollViewer Grid.Row="1" Grid.Column="1">
    <ContentControl Content="{CompiledBinding CurrentPage}" />
  </ScrollViewer>
</Grid>
```

## Conversion Example: SaaS App Shell

HTML intent:

```html
<div class="shell">
  <header class="topbar">...</header>
  <aside class="nav">...</aside>
  <main class="content">...</main>
</div>
```

Avalonia XAML:

```xaml
<Grid RowDefinitions="56,*" ColumnDefinitions="260,*">
  <Border Grid.Row="0" Grid.ColumnSpan="2" Classes="topbar" />

  <SplitView Grid.Row="1" Grid.Column="0"
             DisplayMode="CompactInline"
             IsPaneOpen="True"
             OpenPaneLength="260"
             CompactPaneLength="64">
    <SplitView.Pane>
      <StackPanel Spacing="6">
        <Button Content="Dashboard" />
        <Button Content="Reports" />
      </StackPanel>
    </SplitView.Pane>
  </SplitView>

  <TransitioningContentControl Grid.Row="1" Grid.Column="1"
                               Content="{CompiledBinding CurrentPage}" />
</Grid>
```

Context actions via `Flyout`:

```xaml
<Button Content="Actions">
  <Button.Flyout>
    <MenuFlyout>
      <MenuItem Header="Duplicate" Command="{CompiledBinding DuplicateCommand}" />
      <MenuItem Header="Archive" Command="{CompiledBinding ArchiveCommand}" />
    </MenuFlyout>
  </Button.Flyout>
</Button>
```

## C# Equivalent: SaaS App Shell

```csharp
using Avalonia.Controls;

var shell = new Grid
{
    RowDefinitions = RowDefinitions.Parse("56,*"),
    ColumnDefinitions = ColumnDefinitions.Parse("260,*")
};

var topBar = new Border();
Grid.SetRow(topBar, 0);
Grid.SetColumnSpan(topBar, 2);

var splitView = new SplitView
{
    DisplayMode = SplitViewDisplayMode.CompactInline,
    IsPaneOpen = true,
    OpenPaneLength = 260,
    CompactPaneLength = 64,
    Pane = new StackPanel
    {
        Spacing = 6,
        Children =
        {
            new Button { Content = "Dashboard" },
            new Button { Content = "Reports" }
        }
    }
};
Grid.SetRow(splitView, 1);
Grid.SetColumn(splitView, 0);

var pageHost = new TransitioningContentControl();
Grid.SetRow(pageHost, 1);
Grid.SetColumn(pageHost, 1);

shell.Children.Add(topBar);
shell.Children.Add(splitView);
shell.Children.Add(pageHost);

var actionsButton = new Button { Content = "Actions" };
actionsButton.Flyout = new MenuFlyout
{
    Items =
    {
        new MenuItem { Header = "Duplicate" },
        new MenuItem { Header = "Archive" }
    }
};
```

## AOT/Threading Notes

- Keep navigation view resolution strongly typed (`DataTemplate` + compiled bindings).
- If route state changes from background tasks, update navigation state on `Dispatcher.UIThread`.

## Troubleshooting

1. Popup appears behind content.
- Use the built-in popup/flyout system instead of local panel overlays.

2. SplitView behavior diverges across screen sizes.
- Switch `DisplayMode` and pane lengths by breakpoint class/state.

3. Dialog ownership problems.
- Always open dialog windows with explicit owner where applicable.
