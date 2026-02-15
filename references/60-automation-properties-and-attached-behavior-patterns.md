# Automation Properties and Attached Behavior Patterns

## Table of Contents
1. Scope and APIs
2. Automation Metadata Basics
3. Labeling, Identity, and Landmark Patterns
4. Live Regions and Offscreen Semantics
5. Attached Behavior APIs in Existing Controls
6. Custom Attached Property Pattern
7. Runtime Inspection and Updates
8. Best Practices
9. Troubleshooting

## Scope and APIs

Primary APIs:
- `AutomationProperties`
- `AccessibilityView`
- `AutomationControlType`
- `AutomationLandmarkType`
- `AutomationLiveSetting`
- `IsOffscreenBehavior`

Important automation attached properties:
- `AutomationProperties.Name`
- `AutomationProperties.AutomationId`
- `AutomationProperties.HelpText`
- `AutomationProperties.LabeledBy`
- `AutomationProperties.AccessKey`
- `AutomationProperties.AcceleratorKey`
- `AutomationProperties.ControlTypeOverride`
- `AutomationProperties.LandmarkType`
- `AutomationProperties.HeadingLevel`
- `AutomationProperties.AccessibilityView`
- `AutomationProperties.LiveSetting`
- `AutomationProperties.IsOffscreenBehavior`
- `AutomationProperties.PositionInSet`
- `AutomationProperties.SizeOfSet`

Related attached-behavior surfaces:
- `ToolTip.Tip`, `ToolTip.IsOpen`, `ToolTip.Placement`, `ToolTip.ShowDelay`, `ToolTip.BetweenShowDelay`, `ToolTip.ShowOnDisabled`, `ToolTip.ServiceEnabled`
- `RelativePanel` attached layout relationships (`Above`, `Below`, `LeftOf`, `RightOf`, `Align*With*`)

Reference source files:
- `src/Avalonia.Controls/Automation/AutomationProperties.cs`
- `src/Avalonia.Controls/ToolTip.cs`
- `src/Avalonia.Controls/RelativePanel.AttachedProperties.cs`
- `src/Avalonia.Controls/RelativePanel.cs`

## Automation Metadata Basics

Attach automation metadata directly in XAML:

```xml
<TextBox xmlns="https://github.com/avaloniaui"
         xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
         AutomationProperties.Name="Email address"
         AutomationProperties.AutomationId="Login_Email"
         AutomationProperties.HelpText="Work email used for sign in" />
```

This metadata feeds automation peers used by accessibility tools and UI automation tests.

## Labeling, Identity, and Landmark Patterns

Use `LabeledBy` to connect labels and inputs explicitly:

```xml
<StackPanel xmlns="https://github.com/avaloniaui"
            xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
            Spacing="6">
  <TextBlock x:Name="EmailLabel" Text="Email" />
  <TextBox AutomationProperties.LabeledBy="{Binding #EmailLabel}"
           AutomationProperties.AutomationId="Settings_Email" />
</StackPanel>
```

Landmark/heading pattern:

```xml
<TextBlock xmlns="https://github.com/avaloniaui"
           xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
           Text="Security"
           AutomationProperties.LandmarkType="Main"
           AutomationProperties.HeadingLevel="1" />
```

## Live Regions and Offscreen Semantics

Use `LiveSetting` for status regions that need announcement behavior:

```xml
<TextBlock xmlns="https://github.com/avaloniaui"
           xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
           Text="Upload complete"
           AutomationProperties.LiveSetting="Polite" />
```

For virtualization or overlays, set offscreen behavior intentionally:

```xml
<Border xmlns="https://github.com/avaloniaui"
        xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
        AutomationProperties.IsOffscreenBehavior="FromClip" />
```

Note: some properties (`IsColumnHeader`, `IsRequiredForForm`, `IsRowHeader`, `ItemStatus`, `ItemType`, `PositionInSet`, `SizeOfSet`) are present for compatibility and may have limited or no effect in current implementations.

## Attached Behavior APIs in Existing Controls

ToolTip behavior wiring:

```xml
<Button xmlns="https://github.com/avaloniaui"
        xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
        Content="Deploy"
        ToolTip.Tip="Deploy current branch"
        ToolTip.ShowDelay="200"
        ToolTip.BetweenShowDelay="100"
        ToolTip.ShowOnDisabled="True" />
```

Relative layout via attached properties:

```xml
<RelativePanel xmlns="https://github.com/avaloniaui"
               xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml">
  <TextBlock x:Name="Title" Text="Dashboard" />
  <Button Content="Refresh"
          RelativePanel.RightOf="Title"
          RelativePanel.AlignVerticalCenterWith="Title" />
</RelativePanel>
```

## Custom Attached Property Pattern

Use `AvaloniaProperty.RegisterAttached<TOwner, THost, TValue>` for reusable behavior metadata.

```csharp
using Avalonia;
using Avalonia.Controls;

public static class ValidationHints
{
    public static readonly AttachedProperty<string?> HintProperty =
        AvaloniaProperty.RegisterAttached<ValidationHints, Control, string?>("Hint");

    public static void SetHint(Control element, string? value) => element.SetValue(HintProperty, value);

    public static string? GetHint(Control element) => element.GetValue(HintProperty);
}
```

This pattern mirrors built-in attached APIs like `AutomationProperties.*` and `ToolTip.*`.

## Runtime Inspection and Updates

```csharp
using Avalonia;
using Avalonia.Automation;
using Avalonia.Controls;

void ApplyAutomationName(Control control, string name)
{
    AutomationProperties.SetName(control, name);
}

string? ReadAutomationId(Control control)
{
    return AutomationProperties.GetAutomationId(control);
}

void EnsureTooltip(Control control, string text)
{
    ToolTip.SetTip(control, text);
    ToolTip.SetShowDelay(control, 250);
}
```

## Best Practices

- Set stable `AutomationId` values for test automation targets.
- Use meaningful `Name`/`HelpText` that reflect user intent, not internal IDs.
- Prefer `LabeledBy` over duplicated label strings where possible.
- Keep attached-behavior properties co-located with affected controls in XAML.
- Treat compatibility/no-op automation properties as optional and verify behavior with real tools.

## Troubleshooting

1. Screen reader announces unexpected text.
- Check precedence between visual label content and `AutomationProperties.Name`.

2. UI tests fail to find controls by automation id.
- Ensure `AutomationProperties.AutomationId` is set on the actual target element, not only containers.

3. Tooltip settings appear ignored.
- Verify `ToolTip.ServiceEnabled` is true in the inheritance chain.

4. RelativePanel constraints produce overlapping elements.
- Check conflicting attached constraints (`LeftOf` + `AlignLeftWithPanel`, etc.).

5. Live region updates are silent.
- Confirm `AutomationProperties.LiveSetting` is set and updates occur on the live element instance.
