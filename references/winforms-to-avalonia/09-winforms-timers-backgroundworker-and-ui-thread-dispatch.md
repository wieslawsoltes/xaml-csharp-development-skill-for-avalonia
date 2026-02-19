# WinForms Timer, BackgroundWorker, and UI Thread Dispatch to Avalonia

## Table of Contents
1. Scope and APIs
2. Threading Mapping Matrix
3. Conversion Example
4. C# Equivalent
5. Troubleshooting

## Scope and APIs

Primary WinForms APIs:

- `Timer`
- `BackgroundWorker`
- `Control.Invoke` / `BeginInvoke`

Primary Avalonia APIs:

- `DispatcherTimer`
- `Task.Run` + `Dispatcher.UIThread.Post/InvokeAsync`
- `Dispatcher.UIThread.CheckAccess()`

## Threading Mapping Matrix

| WinForms | Avalonia |
|---|---|
| `Timer.Tick` | `DispatcherTimer.Tick` |
| `BackgroundWorker.DoWork` | `Task.Run(...)` |
| `ProgressChanged` | UI-thread updates via `Dispatcher.UIThread.Post` |
| `Control.Invoke` | `Dispatcher.UIThread.InvokeAsync` |

## Conversion Example

WinForms C#:

```csharp
var timer = new System.Windows.Forms.Timer { Interval = 1000 };
timer.Tick += (_, _) => clockLabel.Text = DateTime.Now.ToString("T");
timer.Start();

var worker = new BackgroundWorker { WorkerReportsProgress = true };
worker.DoWork += (_, _) => LoadLargeData();
worker.RunWorkerCompleted += (_, _) => statusLabel.Text = "Done";
worker.RunWorkerAsync();
```

Avalonia XAML:

```xaml
<StackPanel xmlns="https://github.com/avaloniaui"
            xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
            xmlns:vm="using:MyApp.ViewModels"
            x:DataType="vm:BackgroundViewModel"
            Spacing="8">
  <TextBlock Text="{CompiledBinding ClockText}" />
  <TextBlock Text="{CompiledBinding StatusText}" />
  <Button Content="Load" Command="{CompiledBinding LoadCommand}" />
</StackPanel>
```

## C# Equivalent

```csharp
using System;
using System.Threading.Tasks;
using Avalonia.Threading;

var timer = new DispatcherTimer
{
    Interval = TimeSpan.FromSeconds(1)
};

timer.Tick += (_, _) => viewModel.ClockText = DateTime.Now.ToString("T");
timer.Start();

await Task.Run(() =>
{
    var data = LoadLargeData();
    Dispatcher.UIThread.Post(() =>
    {
        viewModel.ApplyData(data);
        viewModel.StatusText = "Done";
    });
});
```

## Troubleshooting

1. UI updates throw thread access exceptions.
- marshal changes through `Dispatcher.UIThread`.

2. Timer callbacks are too heavy.
- keep `Tick` lightweight and offload heavy work to background tasks.

3. Migrated background operations still block UI.
- remove synchronous wait patterns (`.Result`, `.Wait()`) from UI thread paths.
