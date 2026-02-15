# Rendering and Interop Boundaries (OpenGL, Vulkan, Linux Framebuffer)

## Table of Contents
1. Scope and Positioning
2. Core Platform Graphics Contracts
3. OpenGL Interop Surface
4. Vulkan Interop Surface
5. Linux Framebuffer Surface
6. App-Level Configuration Patterns
7. Stability and Risk Boundaries
8. Best Practices
9. Troubleshooting

## Scope and Positioning

This reference is for advanced integration work. Most app teams should stay on normal `UseSkia()` platform defaults and avoid direct graphics interop unless they must integrate native GPU surfaces.

Primary APIs:
- `IPlatformGraphics`
- `IPlatformGraphicsContext`
- `IPlatformGraphicsWithFeatures`
- `IPlatformGraphicsReadyStateFeature`
- `IGlContext`, `GlInterface`, `GlVersion`
- `IGlPlatformSurface`, `IGlPlatformSurfaceRenderTarget`, `IGlPlatformSurfaceRenderingSession`
- `IVulkanPlatformGraphicsContext`, `IVulkanDevice`, `IVulkanInstance`
- `IVulkanRenderTarget`, `IVulkanRenderSession`
- `VulkanOptions`, `VulkanInstanceCreationOptions`, `VulkanDeviceCreationOptions`
- `LinuxFramebufferPlatformOptions`, `DrmOutputOptions`, `FbdevOutput`, `DrmCard`, `DrmResources`

Reference source files:
- `src/Avalonia.Base/Platform/IPlatformGpu.cs`
- `src/Avalonia.OpenGL/IGlContext.cs`
- `src/Avalonia.OpenGL/GlInterface.cs`
- `src/Avalonia.OpenGL/GlVersion.cs`
- `src/Avalonia.OpenGL/Surfaces/*.cs`
- `src/Avalonia.Vulkan/IVulkanDevice.cs`
- `src/Avalonia.Vulkan/IVulkanRenderTarget.cs`
- `src/Avalonia.Vulkan/VulkanOptions.cs`
- `src/Linux/Avalonia.LinuxFramebuffer/*.cs`
- `src/Linux/Avalonia.LinuxFramebuffer/Output/*.cs`

## Core Platform Graphics Contracts

`IPlatformGraphics` provides context creation and shared-context access.

```csharp
using Avalonia;
using Avalonia.Platform;

IPlatformGraphics? TryGetPlatformGraphics()
{
    return AvaloniaLocator.Current.GetService<IPlatformGraphics>();
}
```

`IPlatformGraphicsContext` defines:
- `IsLost`
- `EnsureCurrent()`
- optional features via `IOptionalFeatureProvider`

Notes:
- these APIs are marked `[Unstable]` in `IPlatformGpu.cs`.
- code using them should be isolated behind explicit adapters.

## OpenGL Interop Surface

`IGlContext` extends `IPlatformGraphicsContext` and adds:
- `Version`
- `GlInterface`
- `SampleCount`, `StencilSize`
- `MakeCurrent()`
- `IsSharedWith(...)`
- `CreateSharedContext(...)`

`GlInterface` is a minimal Avalonia-facing OpenGL function loader (`GetProcAddress`, plus selected GL calls).

`IGlPlatformSurface` / `IGlPlatformSurfaceRenderTarget` / `IGlPlatformSurfaceRenderingSession` provide a render-target abstraction for GL-backed platform surfaces.

## Vulkan Interop Surface

`IVulkanPlatformGraphicsContext` exposes:
- `Device` (`IVulkanDevice`)
- `Instance` (`IVulkanInstance`)
- `CreateRenderTarget(IEnumerable<object> surfaces)`

`IVulkanRenderTarget.BeginDraw()` returns `IVulkanRenderSession` with:
- `Scaling`
- `Size`
- `IsYFlipped`
- `ImageInfo`
- `IsRgba`

`VulkanOptions` tuning surface:
- `VulkanInstanceCreationOptions` (`ApplicationName`, `VulkanVersion`, `InstanceExtensions`, `EnabledLayers`, `UseDebug`)
- `VulkanDeviceCreationOptions` (`DeviceExtensions`, `PreferDiscreteGpu`, `RequireComputeBit`)
- `CustomSharedDevice`

## Linux Framebuffer Surface

Linux framebuffer stack exposes public options and backend types for embedded/kiosk scenarios:

- `LinuxFramebufferPlatformOptions` (`Fps`, `ShouldRenderOnUIThread`)
- `DrmOutputOptions` (`Scaling`, `Orientation`, `VideoMode`, connector selection)
- `FbdevOutput`
- DRM discovery helpers: `DrmCard`, `DrmResources`, `DrmConnector`, `DrmModeInfo`

These are platform-specific and usually unsuitable for general desktop/mobile app deployments.

## App-Level Configuration Patterns

Configure advanced Vulkan options through `AppBuilder.With<T>(...)`:

```csharp
using Avalonia;
using Avalonia.Vulkan;

AppBuilder BuildAvaloniaApp()
{
    return AppBuilder.Configure<App>()
        .UsePlatformDetect()
        .UseSkia()
        .With(new VulkanOptions
        {
            VulkanInstanceCreationOptions = new VulkanInstanceCreationOptions
            {
                ApplicationName = "MyApp",
                UseDebug = false
            },
            VulkanDeviceCreationOptions = new VulkanDeviceCreationOptions
            {
                PreferDiscreteGpu = true
            }
        });
}
```

Keep this optional and behind environment/config flags when shipping across mixed hardware fleets.

## Stability and Risk Boundaries

- `IPlatformGraphics*` is explicitly unstable; avoid exposing it in long-lived app-domain contracts.
- GL/Vulkan context feature sets vary by platform backend and driver.
- Linux framebuffer APIs are specialized to constrained Linux targets.
- Interop code must handle `IsLost` contexts and recreation flow.

## Best Practices

- Keep rendering interop in a dedicated infrastructure layer.
- Probe features at runtime and fail gracefully.
- Avoid assuming a single graphics API across all deployments.
- Prefer Avalonia defaults unless interop requirements are explicit.
- Treat advanced API usage as opt-in and test across target GPUs/drivers.

## Troubleshooting

1. Graphics context unavailable.
- `IPlatformGraphics` may be absent for software or non-GPU backend scenarios.

2. Interop code fails after display reset/suspend.
- Check `IPlatformGraphicsContext.IsLost` and recreate resources/context.

3. Vulkan initialization varies by machine.
- Audit enabled extensions/layers and fallback behavior in `VulkanOptions`.

4. OpenGL function missing.
- Use `GlInterface.GetProcAddress(...)`-aware capability checks before calling optional entry points.

5. Linux framebuffer startup fails.
- Validate device access (`/dev/fb*` or `/dev/dri/*`), connector selection, and mode compatibility.
