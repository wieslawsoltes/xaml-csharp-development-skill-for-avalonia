# WPF ToolTip, Popup, Context Help, and Launcher Patterns to Avalonia

## Table of Contents
1. Scope and APIs
2. Context-Help Mapping
3. Conversion Example
4. Avalonia C# Equivalent
5. Troubleshooting

## Scope and APIs

Primary WPF APIs:

- `ToolTip`
- `ToolTipService`
- context-help links/actions

Primary Avalonia APIs:

- `ToolTip` attached properties (`ToolTip.Tip`, delay/placement properties)
- `HyperlinkButton` (`NavigateUri`)
- `TopLevel.Launcher` for external help links/files

## Context-Help Mapping

| WPF | Avalonia |
|---|---|
| `ToolTipService.ToolTip` | `ToolTip.Tip` |
| tooltip timing/placement service settings | equivalent attached tooltip settings |
| help links launched from commands | `TopLevel.Launcher.LaunchUriAsync(...)` |

## Conversion Example

WPF XAML:

```xaml
<TextBox ToolTipService.ToolTip="Enter legal name" />
<Button Content="Help" />
```

Avalonia XAML:

```xaml
<UserControl xmlns="https://github.com/avaloniaui"
             xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
             xmlns:vm="using:MyApp.ViewModels"
             x:DataType="vm:HelpViewModel">
  <StackPanel Spacing="8">
    <TextBox ToolTip.Tip="Enter legal name"
             Text="{CompiledBinding Name, Mode=TwoWay}" />

    <Button Content="Save"
            ToolTip.Tip="Saves current record"
            Command="{CompiledBinding SaveCommand}" />

    <HyperlinkButton Content="Open Help"
                     NavigateUri="https://docs.example.com/app/help" />
  </StackPanel>
</UserControl>
```

## Avalonia C# Equivalent

```csharp
using System;
using System.Threading.Tasks;
using Avalonia.Controls;

public static class HelpActions
{
    public static async Task OpenHelpAsync(Control anchor)
    {
        ToolTip.SetTip(anchor, "Context help");

        var top = TopLevel.GetTopLevel(anchor);
        if (top is not null)
            await top.Launcher.LaunchUriAsync(new Uri("https://docs.example.com/app/help"));
    }
}
```

## Troubleshooting

1. Tooltips never appear.
- confirm control visibility/enabled state and overlapping popup layers.

2. Help links fail on some targets.
- guard for launcher availability and fallback behavior per platform.

3. Context help strings drift across screens.
- centralize help identifiers and resolve content through one service.
