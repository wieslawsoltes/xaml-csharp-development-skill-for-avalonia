# HTML Shadow DOM, Slots, and CSS Parts to Avalonia Control Templates and Themes

## Table of Contents
1. Scope and APIs
2. Mapping Table
3. Slot and Part Mapping Pattern
4. Conversion Example: `app-card` with Named Slots
5. C# Equivalent: `AppCard` Templated Content Control
6. AOT/Threading Notes
7. Troubleshooting

## Scope and APIs

Primary APIs:

- templating: `ControlTemplate`, `TemplateBinding`, `ContentPresenter`
- theme scoping: `ControlTheme`, nested selectors (`^`, `/template/`)
- template metadata: `TemplatePartAttribute`, `TemplateAppliedEventArgs`, `INameScope`
- control composition: `ContentControl` with additional styled slot properties

Reference docs:

- [`10-templated-controls-and-control-themes.md`](../10-templated-controls-and-control-themes)
- [`28-custom-themes-xaml-and-code-only.md`](../28-custom-themes-xaml-and-code-only)
- [`51-template-content-and-func-template-patterns.md`](../51-template-content-and-func-template-patterns)

## Mapping Table

| Shadow DOM / CSS idiom | Avalonia mapping |
|---|---|
| `:host` | style selector for control type (`local|AppCard`) |
| `:host(.compact)` | class selector on control (`local|AppCard.compact`) |
| `<slot name="header">` | dedicated styled property + `ContentPresenter` |
| default `<slot>` | `ContentControl.Content` through `TemplateBinding Content` |
| `::part(header)` | named template element (`x:Name="PART_Header"`) + `/template/` selectors |
| Shadow-root style encapsulation | `ControlTheme`-scoped selectors anchored with `^` |

## Slot and Part Mapping Pattern

HTML/CSS baseline:

```html
<app-card class="compact">
  <h3 slot="header">Revenue</h3>
  <p>$420,000</p>
  <button slot="actions">Details</button>
</app-card>
```

```css
app-card { display: block; border-radius: 12px; }
app-card.compact { padding: .5rem; }
app-card::part(header) { font-weight: 700; }
```

```js
class AppCardElement extends HTMLElement {
  constructor() {
    super();
    const root = this.attachShadow({ mode: "open" });
    root.innerHTML = `
      <section part="container">
        <header part="header"><slot name="header"></slot></header>
        <main part="content"><slot></slot></main>
        <footer part="actions"><slot name="actions"></slot></footer>
      </section>
    `;
  }
}

customElements.define("app-card", AppCardElement);
```

Avalonia pattern:

```xaml
<local:AppCard Classes="compact"
               HeaderContent="Revenue"
               ActionsContent="Details">
  <TextBlock Text="$420,000" />
</local:AppCard>
```

## Conversion Example: `app-card` with Named Slots

```html
<section class="cards">
  <app-card>
    <span slot="header">Orders</span>
    <span>1,280</span>
    <button slot="actions">Open</button>
  </app-card>
</section>
```

```css
.cards { display: grid; gap: .75rem; }
app-card::part(container) {
  border: 1px solid #2a3348;
  background: #111827;
}
app-card.compact::part(container) { padding: .45rem .65rem; }
```

```xaml
<ControlTheme x:Key="{x:Type local:AppCard}" TargetType="local:AppCard">
  <Setter Property="Template">
    <ControlTemplate>
      <Border x:Name="PART_Container"
              Padding="12"
              CornerRadius="12"
              BorderBrush="#2A3348"
              BorderThickness="1"
              Background="#111827">
        <Grid RowDefinitions="Auto,*,Auto" RowSpacing="8">
          <ContentPresenter x:Name="PART_Header"
                            Grid.Row="0"
                            Content="{TemplateBinding HeaderContent}" />
          <ContentPresenter x:Name="PART_Content"
                            Grid.Row="1"
                            Content="{TemplateBinding Content}" />
          <ContentPresenter x:Name="PART_Actions"
                            Grid.Row="2"
                            Content="{TemplateBinding ActionsContent}" />
        </Grid>
      </Border>
    </ControlTemplate>
  </Setter>

  <Style Selector="^ /template/ ContentPresenter#PART_Header">
    <Setter Property="TextBlock.FontWeight" Value="Bold" />
  </Style>
  <Style Selector="^.compact /template/ Border#PART_Container">
    <Setter Property="Padding" Value="8" />
  </Style>
</ControlTheme>

<local:AppCard HeaderContent="Orders" Classes="compact">
  <TextBlock Text="1,280" />
</local:AppCard>
```

## C# Equivalent: `AppCard` Templated Content Control

```csharp
using Avalonia;
using Avalonia.Controls;
using Avalonia.Controls.Metadata;
using Avalonia.Controls.Primitives;

[TemplatePart("PART_Header", typeof(ContentPresenter), IsRequired = true)]
[TemplatePart("PART_Content", typeof(ContentPresenter), IsRequired = true)]
[TemplatePart("PART_Actions", typeof(ContentPresenter), IsRequired = false)]
public class AppCard : ContentControl
{
    public static readonly StyledProperty<object?> HeaderContentProperty =
        AvaloniaProperty.Register<AppCard, object?>(nameof(HeaderContent));

    public static readonly StyledProperty<object?> ActionsContentProperty =
        AvaloniaProperty.Register<AppCard, object?>(nameof(ActionsContent));

    public object? HeaderContent
    {
        get => GetValue(HeaderContentProperty);
        set => SetValue(HeaderContentProperty, value);
    }

    public object? ActionsContent
    {
        get => GetValue(ActionsContentProperty);
        set => SetValue(ActionsContentProperty, value);
    }

    protected override void OnApplyTemplate(TemplateAppliedEventArgs e)
    {
        base.OnApplyTemplate(e);
        _ = e.NameScope.Find<ContentPresenter>("PART_Header");
        _ = e.NameScope.Find<ContentPresenter>("PART_Content");
        _ = e.NameScope.Find<ContentPresenter>("PART_Actions");
    }
}

var card = new AppCard
{
    HeaderContent = "Orders",
    Content = new TextBlock { Text = "1,280" },
    ActionsContent = new Button { Content = "Open" }
};
card.Classes.Set("compact", true);
```

## AOT/Threading Notes

- Keep slot-like surfaces as typed styled properties (`HeaderContent`, `ActionsContent`) instead of late string lookups.
- Keep visual customization in `ControlTheme`; avoid runtime template parsing in hot paths.

## Troubleshooting

1. Slot content appears in wrong region.
- Verify `ContentPresenter` binds to correct template-bound property.

2. `::part`-style rules seem missing after migration.
- Move rules into control-theme nested selectors (`^ ... /template/ ...`).

3. Compact/host class styles do not apply.
- Ensure the control class (`compact`) is set on the control instance, not only on internal template elements.
