# WinForms ToolTip, HelpProvider, and Context Guidance to Avalonia

## Table of Contents
1. Scope and APIs
2. Guidance Mapping
3. Conversion Example
4. C# Equivalent
5. Troubleshooting

## Scope and APIs

Primary WinForms APIs:

- `ToolTip`
- `HelpProvider`
- F1 help and context help strings

Primary Avalonia APIs:

- `ToolTip` attached properties (`ToolTip.Tip`, placement/delay options)
- `HyperlinkButton` and launcher integration
- command-based help actions

## Guidance Mapping

| WinForms | Avalonia |
|---|---|
| `toolTip.SetToolTip(control, text)` | `ToolTip.Tip="..."` or `ToolTip.SetTip(control, ...)` |
| `HelpProvider.SetHelpString(...)` | help text via tooltip/flyout + help command |
| shell help launch | `TopLevel.Launcher.LaunchUriAsync(...)` |

## Conversion Example

WinForms C#:

```csharp
var tips = new ToolTip();
tips.SetToolTip(nameTextBox, "Enter full legal name");

var help = new HelpProvider();
help.SetHelpString(saveButton, "Save all changes to the current customer.");
```

Avalonia XAML:

```xaml
<UserControl xmlns="https://github.com/avaloniaui"
             xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
             xmlns:vm="using:MyApp.ViewModels"
             x:DataType="vm:CustomerEditorViewModel">
  <StackPanel Spacing="8">
    <TextBox Watermark="Customer name"
             ToolTip.Tip="Enter full legal name"
             Text="{CompiledBinding CustomerName, Mode=TwoWay}" />

    <Button Content="Save"
            ToolTip.Tip="Save all changes to the current customer"
            Command="{CompiledBinding SaveCommand}" />

    <HyperlinkButton Content="Open Help"
                     NavigateUri="https://docs.example.com/customer-editor" />
  </StackPanel>
</UserControl>
```

## C# Equivalent

```csharp
using System;
using System.Threading.Tasks;
using Avalonia.Controls;

public static async Task OpenHelpAsync(Control anchor)
{
    ToolTip.SetTip(anchor, "Context-sensitive help");

    var top = TopLevel.GetTopLevel(anchor);
    if (top is not null)
        await top.Launcher.LaunchUriAsync(new Uri("https://docs.example.com/customer-editor"));
}
```

## Troubleshooting

1. Tooltip does not appear.
- ensure the target is enabled/visible and not covered by another input layer.

2. Help links fail on some targets.
- check `TopLevel` availability and launcher capability on platform/runtime.

3. Help content is inconsistent across screens.
- centralize help routes/IDs in a single service rather than hardcoding strings per view.
