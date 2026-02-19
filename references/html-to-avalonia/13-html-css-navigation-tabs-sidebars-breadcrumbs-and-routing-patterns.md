# HTML/CSS Navigation, Tabs, Sidebars, Breadcrumbs, and Routing Patterns in Avalonia

## Table of Contents
1. Scope and APIs
2. Navigation Pattern Mapping Matrix
3. Tabs and Workspace Patterns
4. Sidebar + Breadcrumb Composition
5. Route-to-ViewModel Mapping Pattern
6. Conversion Example: Admin Navigation Shell
7. C# Equivalent: Admin Navigation Shell
8. Troubleshooting

## Scope and APIs

Primary APIs:

- `TabControl`, `SplitView`, `Menu`, `MenuItem`
- `ContentControl`, `TransitioningContentControl`, `DataTemplate`
- command routing for navigation intents

Reference docs:

- [`11-user-views-locator-and-tree-patterns.md`](../11-user-views-locator-and-tree-patterns)
- [`38-data-templates-and-idatatemplate-selector-patterns.md`](../38-data-templates-and-idatatemplate-selector-patterns)
- [`05-html-shell-navigation-popups-and-layering-patterns.md`](05-html-shell-navigation-popups-and-layering-patterns)

## Navigation Pattern Mapping Matrix

| Web navigation pattern | Avalonia mapping |
|---|---|
| router outlet (`<main id="app">`) | `ContentControl Content="{CompiledBinding CurrentPageVm}"` |
| tabs | `TabControl` |
| collapsible side nav | `SplitView` pane |
| top nav menu | `Menu` + `MenuItem` |
| breadcrumb row | horizontal stack of controls/text |

## Tabs and Workspace Patterns

HTML/CSS tabs:

```html
<nav class="tabs"><button class="active">Overview</button><button>Billing</button></nav>
```

Avalonia:

```xaml
<TabControl SelectedIndex="{CompiledBinding SelectedTabIndex}">
  <TabItem Header="Overview" />
  <TabItem Header="Billing" />
  <TabItem Header="Audit" />
</TabControl>
```

## Sidebar + Breadcrumb Composition

HTML/CSS:

```css
.layout { display:grid; grid-template-columns: 250px 1fr; }
.breadcrumb { display:flex; gap:8px; }
```

Avalonia:

```xaml
<Grid ColumnDefinitions="250,*">
  <StackPanel Grid.Column="0" Classes="nav-rail" />
  <StackPanel Grid.Column="1" Spacing="10">
    <StackPanel Orientation="Horizontal" Spacing="8" Classes="breadcrumb" />
    <ContentControl Content="{CompiledBinding CurrentPageVm}" />
  </StackPanel>
</Grid>
```

## Route-to-ViewModel Mapping Pattern

Use route keys and data templates:

```csharp
public string CurrentRoute { get; set; } = "dashboard";
public object CurrentPageVm => CurrentRoute switch
{
    "dashboard" => DashboardVm,
    "users" => UsersVm,
    _ => NotFoundVm
};
```

```xaml
<ContentControl Content="{CompiledBinding CurrentPageVm}" />
```

## Conversion Example: Admin Navigation Shell

```xaml
<SplitView OpenPaneLength="250"
           CompactPaneLength="64"
           DisplayMode="CompactInline"
           IsPaneOpen="{CompiledBinding IsNavOpen}">
  <SplitView.Pane>
    <StackPanel Spacing="6">
      <Button Content="Dashboard" Command="{CompiledBinding GoDashboardCommand}" />
      <Button Content="Users" Command="{CompiledBinding GoUsersCommand}" />
      <Button Content="Billing" Command="{CompiledBinding GoBillingCommand}" />
    </StackPanel>
  </SplitView.Pane>

  <TransitioningContentControl Content="{CompiledBinding CurrentPageVm}" />
</SplitView>
```

## C# Equivalent: Admin Navigation Shell

```csharp
using Avalonia.Controls;

var shell = new SplitView
{
    OpenPaneLength = 250,
    CompactPaneLength = 64,
    DisplayMode = SplitViewDisplayMode.CompactInline,
    Pane = new StackPanel
    {
        Spacing = 6,
        Children =
        {
            new Button { Content = "Dashboard" },
            new Button { Content = "Users" },
            new Button { Content = "Billing" }
        }
    },
    Content = new TransitioningContentControl()
};
```

## Troubleshooting

1. Navigation flickers during route switches.
- Keep page VM lifetime stable and avoid re-creating large view models on each click.

2. Sidebar width behaves inconsistently.
- Align `OpenPaneLength`, layout columns, and breakpoint state logic.

3. Breadcrumb state drifts from current page.
- Derive breadcrumb items from the same route state source.
