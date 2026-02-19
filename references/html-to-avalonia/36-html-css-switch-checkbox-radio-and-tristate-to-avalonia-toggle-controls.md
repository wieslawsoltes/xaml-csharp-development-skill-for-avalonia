# HTML/CSS Switch, Checkbox, Radio, and Tri-State Patterns to Avalonia Toggle Controls

## Table of Contents
1. Scope and APIs
2. Mapping Table
3. Checkbox and Indeterminate Pattern
4. Radio Group Pattern
5. Switch Pattern
6. Conversion Example: Notification Preferences
7. C# Equivalent: Notification Preferences
8. AOT/Threading Notes
9. Troubleshooting

## Scope and APIs

Primary APIs:

- `ToggleButton` (`IsChecked`, `IsThreeState`)
- `CheckBox` (inherits `ToggleButton`)
- `RadioButton` (`GroupName`)
- `ToggleSwitch` (`OnContent`, `OffContent`, `OnContentTemplate`, `OffContentTemplate`, `KnobTransitions`)

Reference docs:

- [`04-html-forms-input-and-validation-to-avalonia-controls.md`](04-html-forms-input-and-validation-to-avalonia-controls)
- [`16-html-css-accessibility-semantics-and-motion-preference-mapping.md`](16-html-css-accessibility-semantics-and-motion-preference-mapping)
- [`24-html-css-buttons-links-toggle-and-split-command-surfaces.md`](24-html-css-buttons-links-toggle-and-split-command-surfaces)

## Mapping Table

| HTML/CSS idiom | Avalonia mapping |
|---|---|
| `<input type="checkbox">` | `CheckBox IsChecked` |
| checkbox indeterminate (`aria-checked="mixed"`) | `CheckBox IsThreeState="True"` + `IsChecked="{x:Null}"` |
| `<input type="radio" name="...">` | `RadioButton GroupName="..."` |
| custom switch (`role="switch"`) | `ToggleSwitch` |
| `:checked` style state | selectors with `:checked` pseudo-class |

## Checkbox and Indeterminate Pattern

HTML/CSS:

```html
<label><input type="checkbox" checked> <span>Email alerts</span></label>
<label><input type="checkbox" aria-checked="mixed"> <span>Team alerts</span></label>
```

```css
input[type="checkbox"]:checked + span {
  font-weight: 600;
}
```

Avalonia:

```xaml
<StackPanel Spacing="6">
  <CheckBox Content="Email alerts"
            IsChecked="{CompiledBinding EmailAlerts, Mode=TwoWay}" />

  <CheckBox Content="Team alerts"
            IsThreeState="True"
            IsChecked="{CompiledBinding TeamAlertsState, Mode=TwoWay}" />
</StackPanel>
```

## Radio Group Pattern

HTML:

```html
<fieldset>
  <legend>Release channel</legend>
  <label><input type="radio" name="channel" checked> Stable</label>
  <label><input type="radio" name="channel"> Preview</label>
</fieldset>
```

Avalonia:

```xaml
<StackPanel Spacing="4">
  <TextBlock Text="Release channel" />
  <RadioButton GroupName="channel"
               Content="Stable"
               IsChecked="{CompiledBinding IsStable, Mode=TwoWay}" />
  <RadioButton GroupName="channel"
               Content="Preview"
               IsChecked="{CompiledBinding IsPreview, Mode=TwoWay}" />
</StackPanel>
```

## Switch Pattern

HTML/CSS switch:

```html
<button role="switch" aria-checked="true" class="switch">On</button>
```

```css
.switch[aria-checked="true"] {
  background: #1f8f57;
  color: #fff;
}
```

Avalonia:

```xaml
<ToggleSwitch IsChecked="{CompiledBinding AutoDeploy, Mode=TwoWay}"
              OnContent="Enabled"
              OffContent="Disabled" />
```

## Conversion Example: Notification Preferences

```html
<section class="prefs">
  <label><input type="checkbox" checked> Product updates</label>
  <label><input type="checkbox"> Weekly digest</label>

  <div role="radiogroup" aria-label="Delivery channel">
    <label><input type="radio" name="delivery" checked> Email</label>
    <label><input type="radio" name="delivery"> SMS</label>
  </div>

  <button role="switch" aria-checked="false">Quiet hours</button>
</section>
```

```css
.prefs {
  display: grid;
  gap: .6rem;
  max-width: 24rem;
}
```

```xaml
<StackPanel Spacing="8" MaxWidth="420">
  <CheckBox Content="Product updates"
            IsChecked="{CompiledBinding ProductUpdates, Mode=TwoWay}" />
  <CheckBox Content="Weekly digest"
            IsChecked="{CompiledBinding WeeklyDigest, Mode=TwoWay}" />

  <TextBlock Text="Delivery channel" />
  <StackPanel Orientation="Horizontal" Spacing="12">
    <RadioButton GroupName="delivery" Content="Email"
                 IsChecked="{CompiledBinding DeliveryEmail, Mode=TwoWay}" />
    <RadioButton GroupName="delivery" Content="SMS"
                 IsChecked="{CompiledBinding DeliverySms, Mode=TwoWay}" />
  </StackPanel>

  <ToggleSwitch IsChecked="{CompiledBinding QuietHours, Mode=TwoWay}"
                OnContent="Quiet hours on"
                OffContent="Quiet hours off" />
</StackPanel>
```

## C# Equivalent: Notification Preferences

```csharp
using Avalonia.Animation;
using Avalonia.Controls;

var prefs = new StackPanel
{
    Spacing = 8,
    MaxWidth = 420
};

var productUpdates = new CheckBox
{
    Content = "Product updates",
    IsChecked = true
};

var weeklyDigest = new CheckBox
{
    Content = "Weekly digest",
    IsChecked = false
};

var deliveryEmail = new RadioButton
{
    GroupName = "delivery",
    Content = "Email",
    IsChecked = true
};

var deliverySms = new RadioButton
{
    GroupName = "delivery",
    Content = "SMS"
};

var quietHours = new ToggleSwitch
{
    IsChecked = false,
    OnContent = "Quiet hours on",
    OffContent = "Quiet hours off",
    KnobTransitions = new Transitions()
};

var teamAlerts = new CheckBox
{
    Content = "Team alerts",
    IsThreeState = true,
    IsChecked = null
};

prefs.Children.Add(productUpdates);
prefs.Children.Add(weeklyDigest);
prefs.Children.Add(new TextBlock { Text = "Delivery channel" });

var channelRow = new StackPanel { Orientation = Avalonia.Layout.Orientation.Horizontal, Spacing = 12 };
channelRow.Children.Add(deliveryEmail);
channelRow.Children.Add(deliverySms);
prefs.Children.Add(channelRow);

prefs.Children.Add(quietHours);
prefs.Children.Add(teamAlerts);
```

## AOT/Threading Notes

- Keep toggle state in nullable/bool VM properties with explicit conversion rules for tri-state UX.
- Update preference state on `Dispatcher.UIThread` when events originate from background notifications.

## Troubleshooting

1. Radio buttons are not mutually exclusive.
- Ensure related controls share the same `GroupName`.

2. Indeterminate state never appears.
- Set `IsThreeState="True"` and allow `IsChecked` to become `null`.

3. Switch content never changes.
- Confirm `OnContent`/`OffContent` is set and `IsChecked` changes as expected.
