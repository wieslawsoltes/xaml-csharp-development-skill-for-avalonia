# WPF Accessibility, Automation, RTL, and Localization to Avalonia

## Table of Contents
1. Scope and APIs
2. Accessibility and Flow Mapping
3. Conversion Example
4. Avalonia C# Equivalent
5. Troubleshooting

## Scope and APIs

Primary WPF APIs:

- automation peers and automation properties
- `FlowDirection`
- localization resources and culture-specific text

Primary Avalonia APIs:

- `AutomationProperties` attached properties
- accessibility + automation peers
- `FlowDirection` on visual tree
- localized view-model text/resource patterns

## Accessibility and Flow Mapping

| WPF | Avalonia |
|---|---|
| automation naming/help text | `AutomationProperties.Name`/`HelpText` |
| required field semantics | `AutomationProperties.IsRequiredForForm` |
| RTL flow | `FlowDirection="RightToLeft"` |
| localized strings from resources | localization service + bindable text |

## Conversion Example

WPF XAML:

```xaml
<TextBox AutomationProperties.Name="Email"
         FlowDirection="RightToLeft" />
```

Avalonia XAML:

```xaml
<TextBox xmlns="https://github.com/avaloniaui"
         xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
         AutomationProperties.Name="Email"
         AutomationProperties.IsRequiredForForm="True"
         FlowDirection="RightToLeft" />
```

## Avalonia C# Equivalent

```csharp
using Avalonia.Controls;
using Avalonia.Automation;
using Avalonia.Media;

var email = new TextBox();
AutomationProperties.SetName(email, "Email");
AutomationProperties.SetIsRequiredForForm(email, true);
email.FlowDirection = FlowDirection.RightToLeft;
```

## Troubleshooting

1. screen reader output is generic.
- set explicit automation names/help text for important controls.

2. RTL text renders but layout remains LTR.
- apply `FlowDirection` on the correct subtree root.

3. localization updates not reflected live.
- notify bound properties after culture changes.
