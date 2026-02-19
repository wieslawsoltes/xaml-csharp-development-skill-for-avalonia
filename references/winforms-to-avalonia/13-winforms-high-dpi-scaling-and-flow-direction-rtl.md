# WinForms High DPI, Scaling, and RTL Flow Direction to Avalonia

## Table of Contents
1. Scope and APIs
2. DPI and Scaling Mapping
3. RTL Mapping
4. Conversion Example
5. C# Equivalent
6. Troubleshooting

## Scope and APIs

Primary WinForms APIs:

- `AutoScaleMode`
- `DpiChanged` events
- `RightToLeft`

Primary Avalonia APIs:

- `TopLevel.RenderScaling`
- `TopLevel.ScalingChanged`
- `FlowDirection` (`LeftToRight`, `RightToLeft`)

## DPI and Scaling Mapping

| WinForms | Avalonia |
|---|---|
| `AutoScaleMode.Dpi` | platform-managed scaling with logical units |
| `Form.DpiChanged` | `TopLevel.ScalingChanged` |
| manual pixel math | rely on device-independent units, convert only at interop boundaries |

## RTL Mapping

| WinForms | Avalonia |
|---|---|
| `RightToLeft = Yes` | `FlowDirection="RightToLeft"` |
| mixed-direction forms | set `FlowDirection` at subtree scope |

## Conversion Example

WinForms C#:

```csharp
AutoScaleMode = AutoScaleMode.Dpi;
RightToLeft = RightToLeft.Yes;

DpiChanged += (_, e) =>
{
    statusLabel.Text = $"DPI changed: {e.DeviceDpiNew}";
};
```

Avalonia XAML:

```xaml
<Window xmlns="https://github.com/avaloniaui"
        xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
        xmlns:vm="using:MyApp.ViewModels"
        x:DataType="vm:MainViewModel"
        FlowDirection="RightToLeft"
        Width="800"
        Height="480">
  <StackPanel Margin="12" Spacing="8">
    <TextBlock Text="{CompiledBinding ScalingText}" />
    <TextBox Watermark="Name" />
  </StackPanel>
</Window>
```

## C# Equivalent

```csharp
using Avalonia.Controls;
using Avalonia.Media;

public static void AttachScalingListener(Window window, MainViewModel viewModel)
{
    window.FlowDirection = FlowDirection.RightToLeft;
    viewModel.ScalingText = $"Scale: {window.RenderScaling:0.00}";

    window.ScalingChanged += (_, _) =>
    {
        viewModel.ScalingText = $"Scale: {window.RenderScaling:0.00}";
    };
}
```

## Troubleshooting

1. Layout appears over- or under-scaled.
- avoid pixel constants; prefer logical units and container layout rules.

2. RTL text direction is correct but layout order is not.
- set `FlowDirection` on the correct subtree root.

3. Image assets look blurry on high DPI displays.
- provide suitable source resolutions and avoid runtime upscaling where possible.
