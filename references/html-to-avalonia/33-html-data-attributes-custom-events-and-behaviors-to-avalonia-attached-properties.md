# HTML `data-*` Attributes, Custom Events, and Behavior Hooks to Avalonia Attached Properties

## Table of Contents
1. Scope and APIs
2. Mapping Table
3. Data Attributes to Attached Properties
4. Custom DOM Events to Routed Events
5. Conversion Example: Action Chip with Telemetry Metadata
6. C# Equivalent: Attached Property + Routed Event
7. AOT/Threading Notes
8. Troubleshooting

## Scope and APIs

Primary APIs:

- attached properties: `AvaloniaProperty.RegisterAttached<TOwner, THost, TValue>`
- property change hooks: `AttachedProperty<T>.Changed.AddClassHandler<TTarget>(...)`
- routed events: `RoutedEvent.Register<TOwner, TEventArgs>(...)`, `RaiseEvent(...)`, `AddHandler(...)`
- behavior state surfaces: `Classes.Set(...)`, `AutomationProperties.*`

Reference docs:

- [`16-property-system-attached-properties-behaviors-and-style-properties.md`](../16-property-system-attached-properties-behaviors-and-style-properties)
- [`18-input-system-and-routed-events.md`](../18-input-system-and-routed-events)
- [`60-automation-properties-and-attached-behavior-patterns.md`](../60-automation-properties-and-attached-behavior-patterns)

## Mapping Table

| HTML/JS idiom | Avalonia mapping |
|---|---|
| `data-kind="danger"` | attached property (`UiData.Kind`) |
| CSS `[data-kind="danger"]` selector | class set by attached property (`.kind-danger`) |
| `dispatchEvent(new CustomEvent("remove"))` | routed event (`RemoveRequestedEvent`) |
| behavior via dataset + JS listeners | attached-property class handlers + routed events/commands |

## Data Attributes to Attached Properties

HTML/CSS baseline:

```html
<button class="chip" data-kind="danger" data-track-id="delete-account">
  Delete Account
</button>
```

```css
.chip[data-kind="danger"] {
  border-color: #c7353f;
  color: #fff;
  background: #9f1f27;
}
```

Avalonia usage:

```xaml
<Button Content="Delete Account"
        local:UiData.Kind="danger"
        local:UiData.TrackId="delete-account"
        Classes="chip" />

<Style Selector="Button.chip.kind-danger">
  <Setter Property="Background" Value="#9F1F27" />
  <Setter Property="Foreground" Value="White" />
</Style>
```

## Custom DOM Events to Routed Events

HTML/JS baseline:

```html
<action-chip id="archive-chip">Archive</action-chip>
```

```css
action-chip { cursor: pointer; user-select: none; }
```

```js
const chip = document.querySelector("#archive-chip");

chip?.addEventListener("click", () => {
  chip.dispatchEvent(
    new CustomEvent("remove-requested", { bubbles: true, detail: { id: "archive-chip" } })
  );
});
```

Avalonia usage:

```xaml
<local:ActionChip Content="Archive"
                  RemoveRequested="OnChipRemoveRequested" />
```

```csharp
public class ActionChip : Button
{
    public static readonly RoutedEvent<RoutedEventArgs> RemoveRequestedEvent =
        RoutedEvent.Register<ActionChip, RoutedEventArgs>(nameof(RemoveRequested), RoutingStrategies.Bubble);

    public event EventHandler<RoutedEventArgs>? RemoveRequested
    {
        add => AddHandler(RemoveRequestedEvent, value);
        remove => RemoveHandler(RemoveRequestedEvent, value);
    }

    public ActionChip()
    {
        Click += (_, _) => RaiseEvent(new RoutedEventArgs(RemoveRequestedEvent));
    }
}
```

## Conversion Example: Action Chip with Telemetry Metadata

```html
<div class="toolbar">
  <button class="chip" data-kind="warning" data-track-id="archive-item">Archive</button>
</div>
```

```css
.toolbar { display: flex; gap: .5rem; }
.chip[data-kind="warning"] {
  background: #6f4f00;
  color: #ffe9ad;
}
```

```xaml
<StackPanel Orientation="Horizontal" Spacing="8">
  <local:ActionChip Content="Archive"
                    local:UiData.Kind="warning"
                    local:UiData.TrackId="archive-item"
                    Classes="chip" />
</StackPanel>

<Style Selector="local|ActionChip.chip.kind-warning">
  <Setter Property="Background" Value="#6F4F00" />
  <Setter Property="Foreground" Value="#FFE9AD" />
</Style>
```

## C# Equivalent: Attached Property + Routed Event

```csharp
using System;
using Avalonia;
using Avalonia.Controls;
using Avalonia.Interactivity;

public static class UiData
{
    public static readonly AttachedProperty<string?> KindProperty =
        AvaloniaProperty.RegisterAttached<UiData, Control, string?>("Kind");

    public static readonly AttachedProperty<string?> TrackIdProperty =
        AvaloniaProperty.RegisterAttached<UiData, Control, string?>("TrackId");

    static UiData()
    {
        KindProperty.Changed.AddClassHandler<Control>((control, e) =>
        {
            var kind = e.GetNewValue<string?>();
            control.Classes.Set("kind-danger", kind == "danger");
            control.Classes.Set("kind-warning", kind == "warning");
        });
    }

    public static string? GetKind(Control control) => control.GetValue(KindProperty);
    public static void SetKind(Control control, string? value) => control.SetValue(KindProperty, value);

    public static string? GetTrackId(Control control) => control.GetValue(TrackIdProperty);
    public static void SetTrackId(Control control, string? value) => control.SetValue(TrackIdProperty, value);
}

public class ActionChip : Button
{
    public static readonly RoutedEvent<RoutedEventArgs> RemoveRequestedEvent =
        RoutedEvent.Register<ActionChip, RoutedEventArgs>(nameof(RemoveRequested), RoutingStrategies.Bubble);

    public event EventHandler<RoutedEventArgs>? RemoveRequested
    {
        add => AddHandler(RemoveRequestedEvent, value);
        remove => RemoveHandler(RemoveRequestedEvent, value);
    }

    public ActionChip()
    {
        Click += (_, _) => RaiseEvent(new RoutedEventArgs(RemoveRequestedEvent));
    }
}

var archiveChip = new ActionChip { Content = "Archive" };
UiData.SetKind(archiveChip, "warning");
UiData.SetTrackId(archiveChip, "archive-item");
```

## AOT/Threading Notes

- Keep behavior metadata in attached properties; avoid runtime reflection over arbitrary string dictionaries.
- Use routed events or commands for interaction contracts; keep event payload types explicit.

## Troubleshooting

1. Attached-property style class never appears.
- Confirm property-changed handler is registered and class names match selectors.

2. Custom routed event is not observed by parent.
- Ensure event is registered with `RoutingStrategies.Bubble` and raised from the expected control.

3. Metadata value not available where needed.
- Read attached property from the correct control instance (metadata does not automatically flow to siblings).
