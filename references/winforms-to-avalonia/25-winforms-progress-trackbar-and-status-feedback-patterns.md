# WinForms ProgressBar/TrackBar and Status Feedback Patterns to Avalonia

## Table of Contents
1. Scope and APIs
2. Feedback Control Mapping
3. Conversion Example
4. C# Equivalent
5. Troubleshooting

## Scope and APIs

Primary WinForms APIs:

- `ProgressBar`
- `TrackBar`
- `StatusStrip` progress/status indicators

Primary Avalonia APIs:

- `ProgressBar`
- `Slider`
- text/status regions using `TextBlock` and layout containers

## Feedback Control Mapping

| WinForms | Avalonia |
|---|---|
| `ProgressBar.Value/Maximum` | `ProgressBar.Value/Maximum` |
| indeterminate marquee | `ProgressBar.IsIndeterminate="True"` |
| `TrackBar` | `Slider` |
| status text in `StatusStrip` | bottom-aligned status region with bindings |

## Conversion Example

WinForms C#:

```csharp
var zoom = new TrackBar { Minimum = 50, Maximum = 200, Value = 100 };
zoom.ValueChanged += (_, _) => previewZoomLabel.Text = $"{zoom.Value}%";

var progress = new ProgressBar { Minimum = 0, Maximum = 100, Value = 40 };
```

Avalonia XAML:

```xaml
<UserControl xmlns="https://github.com/avaloniaui"
             xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
             xmlns:vm="using:MyApp.ViewModels"
             x:DataType="vm:ImportViewModel">
  <Grid RowDefinitions="Auto,Auto,Auto" RowSpacing="8">
    <Slider Grid.Row="0"
            Minimum="50"
            Maximum="200"
            Value="{CompiledBinding ZoomPercent, Mode=TwoWay}" />

    <ProgressBar Grid.Row="1"
                 Minimum="0"
                 Maximum="100"
                 Value="{CompiledBinding ProgressValue}" />

    <TextBlock Grid.Row="2"
               Text="{CompiledBinding StatusText}" />
  </Grid>
</UserControl>
```

## C# Equivalent

```csharp
using Avalonia.Controls;

var zoom = new Slider
{
    Minimum = 50,
    Maximum = 200,
    Value = viewModel.ZoomPercent
};

var progress = new ProgressBar
{
    Minimum = 0,
    Maximum = 100,
    Value = viewModel.ProgressValue
};
```

## Troubleshooting

1. Progress UI updates stutter.
- throttle update frequency for large batch operations.

2. Slider and view-model drift apart.
- bind `Value` in `TwoWay` mode and keep one canonical source of truth.

3. Marquee-like behavior is missing.
- use `IsIndeterminate="True"` during unknown-duration operations.
