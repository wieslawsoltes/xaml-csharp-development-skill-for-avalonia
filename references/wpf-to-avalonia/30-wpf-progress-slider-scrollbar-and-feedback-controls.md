# WPF ProgressBar, Slider, ScrollBar, and Feedback Controls to Avalonia

## Table of Contents
1. Scope and APIs
2. Feedback Control Mapping
3. Conversion Example
4. Avalonia C# Equivalent
5. Troubleshooting

## Scope and APIs

Primary WPF APIs:

- `ProgressBar`
- `Slider`
- `ScrollBar`

Primary Avalonia APIs:

- `ProgressBar`
- `Slider`
- `ScrollBar`
- status feedback via standard text/layout controls

## Feedback Control Mapping

| WPF | Avalonia |
|---|---|
| `ProgressBar.IsIndeterminate` | same concept |
| `ProgressBar.Value/Maximum` | same concept |
| `Slider` value/range | same concept |
| `ScrollBar` as explicit range input | same concept |

## Conversion Example

WPF XAML:

```xaml
<StackPanel>
  <Slider Minimum="50" Maximum="200" Value="{Binding ZoomPercent}" />
  <ProgressBar Minimum="0" Maximum="100" Value="{Binding Progress}" />
</StackPanel>
```

Avalonia XAML:

```xaml
<UserControl xmlns="https://github.com/avaloniaui"
             xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
             xmlns:vm="using:MyApp.ViewModels"
             x:DataType="vm:ImportViewModel">
  <Grid RowDefinitions="Auto,Auto,Auto,Auto" RowSpacing="8">
    <Slider Grid.Row="0"
            Minimum="50"
            Maximum="200"
            Value="{CompiledBinding ZoomPercent, Mode=TwoWay}" />

    <ProgressBar Grid.Row="1"
                 Minimum="0"
                 Maximum="100"
                 Value="{CompiledBinding Progress}" />

    <ProgressBar Grid.Row="2"
                 IsIndeterminate="{CompiledBinding IsBusy}" />

    <ScrollBar Grid.Row="3"
               Orientation="Horizontal"
               Minimum="0"
               Maximum="100"
               Value="{CompiledBinding ScrollPosition, Mode=TwoWay}" />
  </Grid>
</UserControl>
```

## Avalonia C# Equivalent

```csharp
using Avalonia.Controls;

var zoom = new Slider { Minimum = 50, Maximum = 200, Value = viewModel.ZoomPercent };
var progress = new ProgressBar { Minimum = 0, Maximum = 100, Value = viewModel.Progress };
var busy = new ProgressBar { IsIndeterminate = viewModel.IsBusy };
var bar = new ScrollBar { Orientation = Avalonia.Layout.Orientation.Horizontal, Minimum = 0, Maximum = 100 };
```

## Troubleshooting

1. Frequent progress updates hurt responsiveness.
- throttle UI updates for high-frequency producer loops.

2. Range values drift between controls and model.
- keep one source-of-truth property per range and two-way bind consistently.

3. Indeterminate state is misleading.
- switch to determinate mode as soon as measurable progress becomes available.
