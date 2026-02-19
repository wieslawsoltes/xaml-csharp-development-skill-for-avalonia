# HTML/CSS Accessibility, Semantics, and Motion Preference Mapping to Avalonia

## Table of Contents
1. Scope and APIs
2. ARIA/Semantics Mapping
3. Focus Order and Keyboard Navigation Mapping
4. Motion Preference Mapping
5. Conversion Example: Accessible Settings Panel
6. C# Equivalent: Accessible Settings Panel
7. Troubleshooting

## Scope and APIs

Primary APIs:

- `AutomationProperties` (`Name`, `AutomationId`, `HelpText`, `LabeledBy`, `LiveSetting`)
- focus and keyboard navigation APIs
- style/class strategies for reduced-motion and high-contrast variants

Reference docs:

- [`23-accessibility-and-automation.md`](../23-accessibility-and-automation)
- [`60-automation-properties-and-attached-behavior-patterns.md`](../60-automation-properties-and-attached-behavior-patterns)
- [`12-html-css-interaction-states-focus-gestures-and-input-ux.md`](12-html-css-interaction-states-focus-gestures-and-input-ux)

## ARIA/Semantics Mapping

| Web accessibility | Avalonia mapping |
|---|---|
| `aria-label` | `AutomationProperties.Name` |
| `aria-describedby` | `AutomationProperties.HelpText` |
| `aria-live` | `AutomationProperties.LiveSetting` |
| element `id` for tests | `AutomationProperties.AutomationId` |

HTML:

```html
<button aria-label="Refresh analytics" aria-describedby="refreshHelp">↻</button>
<small id="refreshHelp">Downloads latest data</small>
```

Avalonia:

```xaml
<Button Content="Refresh"
        AutomationProperties.Name="Refresh analytics"
        AutomationProperties.HelpText="Downloads latest data"
        AutomationProperties.AutomationId="RefreshAnalyticsButton" />
```

## Focus Order and Keyboard Navigation Mapping

HTML/CSS uses DOM order + `tabindex`; Avalonia uses visual tree ordering plus focusability/keyboard navigation configuration.

Practical mapping:

- keep natural focus order aligned with layout order,
- avoid focus traps unless inside dialog flows,
- verify key commands are discoverable and conflict-free.

## Motion Preference Mapping

Web pattern:

```css
@media (prefers-reduced-motion: reduce) {
  * { animation: none !important; transition: none !important; }
}
```

Avalonia pattern:

- maintain a `reduced-motion` app/root class,
- disable transitions/animations in styles when class is present,
- avoid non-essential continuous motion in critical flows.

```xaml
<Style Selector="*.reduced-motion Border.animated-card">
  <Setter Property="Transitions">
    <Transitions />
  </Setter>
</Style>
```

## Conversion Example: Accessible Settings Panel

```xaml
<StackPanel Spacing="10">
  <TextBlock Text="Notifications" FontWeight="SemiBold" />

  <ToggleSwitch Content="Enable email alerts"
                IsChecked="{CompiledBinding EmailAlertsEnabled}"
                AutomationProperties.AutomationId="EmailAlertsToggle"
                AutomationProperties.HelpText="Sends alerts for important account events" />

  <Button Content="Save settings"
          Command="{CompiledBinding SaveCommand}"
          AutomationProperties.Name="Save notification settings"
          AutomationProperties.AutomationId="SaveSettingsButton" />
</StackPanel>
```

## C# Equivalent: Accessible Settings Panel

```csharp
using Avalonia.Controls;
using Avalonia.Automation;
using Avalonia.Media;

var panel = new StackPanel { Spacing = 10 };

panel.Children.Add(new TextBlock { Text = "Notifications", FontWeight = FontWeight.SemiBold });

var emailToggle = new ToggleSwitch { Content = "Enable email alerts" };
AutomationProperties.SetAutomationId(emailToggle, "EmailAlertsToggle");
AutomationProperties.SetHelpText(emailToggle, "Sends alerts for important account events");
panel.Children.Add(emailToggle);

var saveButton = new Button { Content = "Save settings" };
AutomationProperties.SetName(saveButton, "Save notification settings");
AutomationProperties.SetAutomationId(saveButton, "SaveSettingsButton");
panel.Children.Add(saveButton);

// Reduced motion mode can be represented by a class toggle at root scope.
panel.Classes.Set("reduced-motion", true);
```

## Troubleshooting

1. Screen reader names are generic.
- Set explicit automation names for icon-only and ambiguous controls.

2. Keyboard users cannot reach overlay actions.
- Validate focus behavior when popups/dialogs open and close.

3. Reduced-motion mode still animates parts of UI.
- Audit control-specific transitions and disable them under motion-preference class.
