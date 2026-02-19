# HTML/CSS Cascade Layers, Scope, and `:has()` State to Avalonia Style Architecture

## Table of Contents
1. Scope and APIs
2. Mapping Table
3. Cascade Layers and Style Order
4. Scoped Styling and Parent-Driven State
5. `:has()`-Style Parent State Mapping
6. Conversion Example: Dashboard Layout Rules
7. C# Equivalent: Parent-State Class and Container Query Setup
8. AOT/Threading Notes
9. Troubleshooting

## Scope and APIs

Primary APIs:

- style organization: `Styles`, `StyleInclude`, selector ordering
- scoped style composition: parent class selectors, nested selectors
- state architecture: `Classes.Set(...)`, control pseudo-classes and classes
- adaptive styles: `ContainerQuery`, `Container.Name`, `Container.Sizing`

Reference docs:

- [`02-html-css-selectors-cascade-variables-and-theming.md`](02-html-css-selectors-cascade-variables-and-theming)
- [`07-html-css-design-system-utilities-and-component-variants.md`](07-html-css-design-system-utilities-and-component-variants)
- [`16-property-system-attached-properties-behaviors-and-style-properties.md`](../16-property-system-attached-properties-behaviors-and-style-properties)

## Mapping Table

| Advanced CSS idiom | Avalonia mapping |
|---|---|
| `@layer reset, components, overrides` | style ordering in `Styles` / merged dictionaries |
| `@scope (.shell) { ... }` | parent-qualified selectors (`Grid.shell ...`) |
| `:where(...)` low-specificity grouping | shared class selectors + explicit style ordering |
| `:is(...)` selector grouping | multiple explicit selectors or class normalization |
| `:has(...)` parent dependent style | set parent class from state (`has-*`) and style by class |
| `@container (min-width: 900px)` | `ContainerQuery Query="min-width:900"` |

## Cascade Layers and Style Order

HTML/CSS baseline:

```html
<div class="panel card warning">...</div>
```

```css
@layer reset, components, overrides;

@layer components {
  .card { border-radius: 12px; background: #151b28; }
}

@layer overrides {
  .warning { border: 1px solid #d18a00; }
}
```

Avalonia equivalent (ordered styles):

```xaml
<Styles>
  <!-- Components layer -->
  <Style Selector="Border.card">
    <Setter Property="CornerRadius" Value="12" />
    <Setter Property="Background" Value="#151B28" />
  </Style>

  <!-- Overrides layer (later wins) -->
  <Style Selector="Border.warning">
    <Setter Property="BorderBrush" Value="#D18A00" />
    <Setter Property="BorderThickness" Value="1" />
  </Style>
</Styles>
```

## Scoped Styling and Parent-Driven State

HTML/CSS scoped rule:

```html
<section class="shell">
  <button class="cta">Save</button>
</section>
```

```css
@scope (.shell) {
  .cta { min-inline-size: 8rem; }
}
```

Avalonia scope pattern:

```xaml
<Grid Classes="shell">
  <Grid.Styles>
    <Style Selector="Grid.shell Button.cta">
      <Setter Property="MinWidth" Value="128" />
    </Style>
  </Grid.Styles>

  <Button Classes="cta" Content="Save" />
</Grid>
```

## `:has()`-Style Parent State Mapping

HTML/CSS baseline:

```html
<div class="toolbar">
  <button class="chip danger">Delete</button>
</div>
```

```css
.toolbar:has(.danger) {
  outline: 1px solid #c7353f;
}
```

Avalonia does not use CSS `:has()`. The practical pattern is to set a class on parent when child state changes.

```xaml
<Border Classes="toolbar has-danger">
  <Border.Styles>
    <Style Selector="Border.toolbar.has-danger">
      <Setter Property="BorderBrush" Value="#C7353F" />
      <Setter Property="BorderThickness" Value="1" />
    </Style>
  </Border.Styles>
  <StackPanel Orientation="Horizontal" Spacing="8">
    <Button Classes="chip danger" Content="Delete" />
  </StackPanel>
</Border>
```

## Conversion Example: Dashboard Layout Rules

```html
<section class="dashboard" data-density="compact">
  <div class="cards">
    <article class="card warning">Service latency high</article>
  </div>
</section>
```

```css
@layer base, components, state;

.dashboard { container-type: inline-size; }

@container (min-width: 900px) {
  .cards { grid-template-columns: repeat(3, 1fr); }
}

.dashboard[data-density="compact"] .card { padding: .45rem .65rem; }
```

```xaml
<Grid Classes="dashboard compact"
      Container.Name="Host"
      Container.Sizing="Width">
  <Grid.Styles>
    <Style Selector="Grid.dashboard Border.card">
      <Setter Property="Padding" Value="12" />
    </Style>
    <Style Selector="Grid.dashboard.compact Border.card">
      <Setter Property="Padding" Value="8" />
    </Style>

    <ContainerQuery Name="Host" Query="min-width:900">
      <Style Selector="UniformGrid#CardsGrid">
        <Setter Property="Columns" Value="3" />
      </Style>
    </ContainerQuery>
  </Grid.Styles>

  <UniformGrid x:Name="CardsGrid" Columns="1">
    <Border Classes="card warning">
      <TextBlock Text="Service latency high" />
    </Border>
  </UniformGrid>
</Grid>
```

## C# Equivalent: Parent-State Class and Container Query Setup

```csharp
using Avalonia;
using System.Linq;
using Avalonia.Controls;
using Avalonia.Styling;

var toolbar = new Border
{
    Child = new StackPanel
    {
        Orientation = Avalonia.Layout.Orientation.Horizontal,
        Spacing = 8,
        Children =
        {
            new Button { Content = "Delete", Classes = { "chip", "danger" } },
            new Button { Content = "Duplicate", Classes = { "chip" } }
        }
    }
};

void UpdateToolbarState()
{
    var panel = (StackPanel)toolbar.Child!;
    var hasDanger = panel.Children
        .OfType<StyledElement>()
        .Any(c => c.Classes.Contains("danger"));

    toolbar.Classes.Set("toolbar", true);
    toolbar.Classes.Set("has-danger", hasDanger);
}

UpdateToolbarState();

var host = new Grid();
Container.SetName(host, "Host");
Container.SetSizing(host, ContainerSizing.Width);
```

## AOT/Threading Notes

- Prefer explicit classes and deterministic style order over runtime selector construction.
- Keep parent-state class updates cheap and event-driven.
- Run class/style mutations on `Dispatcher.UIThread` if driven from async background signals.

## Troubleshooting

1. Style precedence seems different from CSS expectations.
- In Avalonia, style order and selector matching determine final values; reorganize style order explicitly.

2. `:has()` migration seems hard to maintain.
- Move parent-dependent logic into VM state flags or centralized class toggling helpers.

3. Container query styles never activate.
- Ensure both `Container.Name` and `Container.Sizing` are set on the intended container.
