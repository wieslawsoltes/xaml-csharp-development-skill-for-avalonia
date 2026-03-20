# Diagnostics, Profiling, and DevTools Integration

## Table of Contents
1. Scope and APIs
2. Runtime Diagnostics Model
3. Authoring Patterns
4. Profiling Workflow
5. Troubleshooting

## Scope and APIs

Primary APIs:
- `TopLevel.RendererDiagnostics`
- `RendererDiagnostics`
- `RendererDebugOverlays`
- `TopLevel.RequestAnimationFrame(...)`
- `Layoutable.LayoutUpdated`
- `Layoutable.EffectiveViewportChanged`
- `LoggingExtensions`
- `Logger`

Important members:
- `RendererDiagnostics.DebugOverlays`
- `RendererDebugOverlays.Fps`
- `RendererDebugOverlays.DirtyRects`
- `RendererDebugOverlays.LayoutTimeGraph`
- `RendererDebugOverlays.RenderTimeGraph`
- `TopLevel.RequestAnimationFrame(Action<TimeSpan>)`
- `Layoutable.UpdateLayout()`
- `AppBuilder.LogToTrace(...)`, `LogToTextWriter(...)`, `LogToDelegate(...)`
- `Logger.IsEnabled(...)`, `Logger.TryGet(...)`

Reference source files:
- `src/Avalonia.Controls/TopLevel.cs`
- `src/Avalonia.Base/Rendering/RendererDiagnostics.cs`
- `src/Avalonia.Base/Rendering/RendererDebugOverlays.cs`
- `src/Avalonia.Base/Layout/Layoutable.cs`
- `src/Avalonia.Controls/LoggingExtensions.cs`
- `src/Avalonia.Base/Logging/Logger.cs`
- `src/tools/Avalonia.Generators/NameGenerator/InitializeComponentCodeGenerator.cs`
- `src/tools/Avalonia.Generators/README.md`

## Runtime Diagnostics Model

Core app-level diagnostics in this codebase:
- Renderer overlays for FPS, dirty rects, and layout/render timing graphs.
- Logging sinks configurable via `AppBuilder`.
- Frame callback hooks through `RequestAnimationFrame`.
- Layout lifecycle observation via `LayoutUpdated` and viewport events.

Note on DevTools:
- Runtime `AttachDevTools()` implementation on the stable `11.3.12` line is provided by the `Avalonia.Diagnostics` package (outside this repository tree).
- This repository includes generator-side hooks that emit optional `attachDevTools` wiring when that package is referenced.
- Avalonia 12 migration note: `Avalonia.Diagnostics` is removed; use `AvaloniaUI.DiagnosticsSupport` and `AttachDeveloperTools()`. See [`68-avalonia-12-migration-guide.md`](68-avalonia-12-migration-guide).

## Authoring Patterns

### Enable renderer overlays at runtime

```csharp
using Avalonia.Controls;
using Avalonia.Rendering;

var top = TopLevel.GetTopLevel(control);
if (top is not null)
{
    top.RendererDiagnostics.DebugOverlays =
        RendererDebugOverlays.Fps |
        RendererDebugOverlays.LayoutTimeGraph |
        RendererDebugOverlays.RenderTimeGraph;
}
```

### Frame-time instrumentation hook

```csharp
top.RequestAnimationFrame(ts =>
{
    // Record frame timestamp or simulation budget here.
    UpdateFrame(ts);
});
```

### Configure structured logging sink

```csharp
AppBuilder.Configure<App>()
    .LogToDelegate(
        line => MyLog.Write(line),
        Avalonia.Logging.LogEventLevel.Information,
        Avalonia.Logging.LogArea.Layout,
        Avalonia.Logging.LogArea.Visual)
    .UsePlatformDetect();
```

### Observe layout churn in control-level diagnostics

```csharp
myControl.LayoutUpdated += (_, _) =>
{
    // Count or sample layout frequency for hotspot analysis.
};
```

## Profiling Workflow

1. Turn on overlays (`Fps`, `DirtyRects`, timing graphs).
2. Reproduce scenario with realistic data size.
3. Capture logs around layout/render/input areas.
4. Identify high-frequency invalidation sources.
5. Fix at source (layout, styles, bindings, or rendering path).
6. Re-run with overlays and compare.

## Troubleshooting

1. Overlay flags set but nothing visible:
- Wrong `TopLevel` instance targeted.
- Renderer not active for that root.

2. FPS drops with many dirty rects:
- Excessive invalidation from layout/style churn.
- Per-frame allocations in render or animation callbacks.

3. Layout graph spikes:
- Expensive `MeasureOverride`/`ArrangeOverride` logic.
- Frequent property changes that trigger full remeasure.

4. DevTools attach call missing in generated code:
- `Avalonia.Diagnostics` package not referenced.
- On Avalonia 12, verify that the project moved to `AvaloniaUI.DiagnosticsSupport` and `AttachDeveloperTools()`.
- Generator option disabled for devtools attachment.

## XAML-First and Code-Only Usage

Default mode:
- Keep diagnostics UI controls/commands declared in XAML first.
- Use code-only diagnostics overlays and log hooks when requested.

XAML-first references:
- Diagnostic toggle controls bound to viewmodel commands/properties

XAML-first usage example:

```xml
<StackPanel xmlns="https://github.com/avaloniaui"
            xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
            xmlns:vm="using:MyApp.ViewModels"
            x:DataType="vm:DiagnosticsViewModel"
            Spacing="8">
  <ToggleSwitch Content="Show FPS" IsChecked="{CompiledBinding ShowFps}" />
  <Button Content="Enable Overlays" Command="{CompiledBinding EnableOverlaysCommand}" />
</StackPanel>
```

Code-only alternative (on request):

```csharp
var top = TopLevel.GetTopLevel(this);
if (top is not null)
{
    top.RendererDiagnostics.DebugOverlays =
        RendererDebugOverlays.Fps | RendererDebugOverlays.RenderTimeGraph;
}
```
