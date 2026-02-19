# HTML Custom Elements and Web Components to Avalonia Custom and Templated Controls

## Table of Contents
1. Scope and APIs
2. Mapping Table
3. Custom Element Contract to Control Contract
4. Conversion Example: `status-pill` Component
5. C# Equivalent: `StatusPill` Control Authoring
6. AOT/Threading Notes
7. Troubleshooting

## Scope and APIs

Primary APIs:

- control authoring: `TemplatedControl`, `ContentControl`, `ControlTheme`, `TemplateBinding`
- custom control metadata: `TemplatePartAttribute`, `TemplateAppliedEventArgs`
- custom properties: `AvaloniaProperty.Register<TOwner, TValue>`, `StyledProperty<T>`
- lifecycle hooks: `AttachedToVisualTree`, `DetachedFromVisualTree`, `TemplateApplied`

Reference docs:

- [`10-templated-controls-and-control-themes.md`](../10-templated-controls-and-control-themes)
- [`16-property-system-attached-properties-behaviors-and-style-properties.md`](../16-property-system-attached-properties-behaviors-and-style-properties)
- [`28-custom-themes-xaml-and-code-only.md`](../28-custom-themes-xaml-and-code-only)

## Mapping Table

| Web component idiom | Avalonia mapping |
|---|---|
| `customElements.define("status-pill", ...)` | custom control class (`StatusPill`) in C# |
| observed attributes (`status="online"`) | `StyledProperty` (`IsOnline`) |
| `connectedCallback` / `disconnectedCallback` | `AttachedToVisualTree` / `DetachedFromVisualTree` |
| component template | `ControlTheme` + `ControlTemplate` |
| host state classes | `Classes.Set(...)` + style selectors |

## Custom Element Contract to Control Contract

HTML/CSS baseline:

```html
<status-pill status="online">Payments API</status-pill>
<status-pill status="offline">Reports Worker</status-pill>
```

```css
status-pill {
  display: inline-flex;
  align-items: center;
  gap: .45rem;
  border-radius: 999px;
  padding: .25rem .65rem;
  background: #17202f;
  color: #eaf0ff;
}
status-pill[status="online"] {
  border: 1px solid #23b26d;
}
```

```js
class StatusPillElement extends HTMLElement {
  static observedAttributes = ["status"];

  connectedCallback() {
    this.classList.add("mounted");
    this.syncStateClass();
  }

  disconnectedCallback() {
    this.classList.remove("mounted");
  }

  attributeChangedCallback(name) {
    if (name === "status") {
      this.syncStateClass();
    }
  }

  syncStateClass() {
    const isOnline = this.getAttribute("status") === "online";
    this.classList.toggle("online", isOnline);
    this.classList.toggle("offline", !isOnline);
  }
}

customElements.define("status-pill", StatusPillElement);
```

Avalonia usage:

```xaml
<StackPanel Orientation="Horizontal" Spacing="8">
  <local:StatusPill Label="Payments API" IsOnline="True" />
  <local:StatusPill Label="Reports Worker" IsOnline="False" />
</StackPanel>
```

## Conversion Example: `status-pill` Component

```html
<section class="service-grid">
  <status-pill status="online">Auth Gateway</status-pill>
  <status-pill status="offline">Billing Jobs</status-pill>
</section>
```

```css
.service-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
  gap: .5rem;
}
status-pill[status="online"] { box-shadow: 0 0 0 1px #23b26d inset; }
status-pill[status="offline"] { opacity: .78; }
```

```xaml
<ControlTheme x:Key="{x:Type local:StatusPill}" TargetType="local:StatusPill">
  <Setter Property="Template">
    <ControlTemplate>
      <Border x:Name="PART_Root"
              CornerRadius="999"
              Padding="10,4"
              Background="#17202F">
        <StackPanel Orientation="Horizontal" Spacing="6">
          <Border Width="8" Height="8" CornerRadius="4" Classes="dot" />
          <TextBlock Text="{TemplateBinding Label}" />
        </StackPanel>
      </Border>
    </ControlTemplate>
  </Setter>

  <Style Selector="^ /template/ Border.dot">
    <Setter Property="Background" Value="#808B9C" />
  </Style>
  <Style Selector="^.online /template/ Border.dot">
    <Setter Property="Background" Value="#23B26D" />
  </Style>
  <Style Selector="^.offline /template/ Border.dot">
    <Setter Property="Background" Value="#8B93A3" />
  </Style>
</ControlTheme>

<StackPanel Orientation="Horizontal" Spacing="8">
  <local:StatusPill Label="Auth Gateway" IsOnline="True" />
  <local:StatusPill Label="Billing Jobs" IsOnline="False" />
</StackPanel>
```

## C# Equivalent: `StatusPill` Control Authoring

```csharp
using Avalonia;
using Avalonia.Controls;
using Avalonia.Controls.Metadata;
using Avalonia.Controls.Primitives;

[TemplatePart("PART_Root", typeof(Border), IsRequired = true)]
public class StatusPill : TemplatedControl
{
    public static readonly StyledProperty<string?> LabelProperty =
        AvaloniaProperty.Register<StatusPill, string?>(nameof(Label));

    public static readonly StyledProperty<bool> IsOnlineProperty =
        AvaloniaProperty.Register<StatusPill, bool>(nameof(IsOnline));

    public string? Label
    {
        get => GetValue(LabelProperty);
        set => SetValue(LabelProperty, value);
    }

    public bool IsOnline
    {
        get => GetValue(IsOnlineProperty);
        set => SetValue(IsOnlineProperty, value);
    }

    static StatusPill()
    {
        IsOnlineProperty.Changed.AddClassHandler<StatusPill>((pill, e) =>
        {
            pill.ApplyOnlineStateClasses(e.GetNewValue<bool>());
        });
    }

    public StatusPill()
    {
        ApplyOnlineStateClasses(IsOnline);
        AttachedToVisualTree += (_, _) => Classes.Set("mounted", true);
        DetachedFromVisualTree += (_, _) => Classes.Set("mounted", false);
    }

    protected override void OnApplyTemplate(TemplateAppliedEventArgs e)
    {
        base.OnApplyTemplate(e);
        _ = e.NameScope.Find<Border>("PART_Root");
    }

    private void ApplyOnlineStateClasses(bool isOnline)
    {
        Classes.Set("online", isOnline);
        Classes.Set("offline", !isOnline);
    }
}

var servicePill = new StatusPill
{
    Label = "Auth Gateway",
    IsOnline = true
};
```

## AOT/Threading Notes

- Keep control state in strongly-typed `StyledProperty` members.
- Prefer XAML `ControlTheme` for templates; keep imperative template creation as an advanced path.
- If control state updates come from background services, marshal property updates to `Dispatcher.UIThread`.

## Troubleshooting

1. Custom control renders as empty.
- Confirm a matching `ControlTheme` is loaded and `TargetType` matches the control type.

2. Template part lookup returns `null`.
- Verify `x:Name` matches `[TemplatePart]` name and template is actually applied.

3. Host-state styles do not activate.
- Ensure the control toggles `Classes` consistently (`online`, `offline`) before style evaluation.
