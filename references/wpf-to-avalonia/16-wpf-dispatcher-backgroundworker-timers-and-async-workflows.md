# WPF Dispatcher, BackgroundWorker, Timers, and Async Workflows to Avalonia

## Table of Contents
1. Scope and APIs
2. Threading Mapping
3. Conversion Example
4. Avalonia C# Equivalent
5. Troubleshooting

## Scope and APIs

Primary WPF APIs:

- `Dispatcher`
- `DispatcherTimer`
- `BackgroundWorker`

Primary Avalonia APIs:

- `Dispatcher.UIThread`
- `DispatcherTimer`
- `Task.Run` + dispatcher marshaling

## Threading Mapping

| WPF | Avalonia |
|---|---|
| `Dispatcher.Invoke` | `Dispatcher.UIThread.InvokeAsync` |
| `Dispatcher.BeginInvoke` | `Dispatcher.UIThread.Post` |
| `DispatcherTimer` | `DispatcherTimer` |
| `BackgroundWorker` | `Task.Run` + progress callbacks to UI thread |

## Conversion Example

WPF C#:

```csharp
Dispatcher.BeginInvoke(() => Status = "Running");

var timer = new DispatcherTimer { Interval = TimeSpan.FromSeconds(1) };
timer.Tick += (_, _) => Clock = DateTime.Now.ToString("T");
timer.Start();
```

Avalonia XAML:

```xaml
<StackPanel xmlns="https://github.com/avaloniaui"
            xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
            xmlns:vm="using:MyApp.ViewModels"
            x:DataType="vm:RuntimeViewModel"
            Spacing="8">
  <TextBlock Text="{CompiledBinding StatusText}" />
  <TextBlock Text="{CompiledBinding ClockText}" />
</StackPanel>
```

## Avalonia C# Equivalent

```csharp
using System;
using System.Threading.Tasks;
using Avalonia.Threading;

Dispatcher.UIThread.Post(() => viewModel.StatusText = "Running");

var timer = new DispatcherTimer
{
    Interval = TimeSpan.FromSeconds(1)
};

timer.Tick += (_, _) => viewModel.ClockText = DateTime.Now.ToString("T");
timer.Start();

await Task.Run(() =>
{
    var result = Compute();
    Dispatcher.UIThread.Post(() => viewModel.ApplyResult(result));
});
```

## Troubleshooting

1. UI updates throw thread access errors.
- marshal to `Dispatcher.UIThread` for all UI mutations.

2. timer callback performs heavy work.
- keep tick handlers lightweight and move heavy work off thread.

3. migrated async flow deadlocks.
- avoid blocking waits (`Wait`, `Result`) on UI thread.
