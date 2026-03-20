# Platform Bootstrapping and Options

## Cross-Platform Baseline

Typical shared startup:

```csharp
public static AppBuilder BuildAvaloniaApp()
    => AppBuilder.Configure<App>()
        .UsePlatformDetect();
```

`UsePlatformDetect()` on desktop wires:

- Win32/X11/AvaloniaNative windowing backend (per OS)
- Skia rendering
- HarfBuzz text shaping through the Skia stack

Avalonia 12 migration note:
- if you explicitly switch to `.UseSkia()` instead of using `.UsePlatformDetect()`, add `.UseHarfBuzz()` and reference `Avalonia.HarfBuzz`; see [`68-avalonia-12-migration-guide.md`](68-avalonia-12-migration-guide).

Skia tuning option exposed by runtime configuration:

- `SkiaOptions.UseOpacitySaveLayer`

## Common Cross-Platform Extensions

- `UseSkia()`
- `WithInterFont()`
- `UseManagedSystemDialogs()`

Related extension host types:

- `AppBuilderExtension` (Inter font package extension host)
- `SkiaApplicationExtensions` (Skia rendering extension host)

## Platform Extension Types

Public extension classes you will see in app startup code:

- `Win32ApplicationExtensions`
- `AvaloniaX11PlatformExtensions`
- `AvaloniaNativePlatformExtensions`
- `BrowserAppBuilder`
- `LinuxFramebufferPlatformExtensions`
- `AndroidApplicationExtensions`
- `IOSApplicationExtensions`

These contain entry points like `UseWin32()`, `UseX11()`, `UseAvaloniaNative()`, `UseBrowser()`, `UseAndroid()`, and `UseiOS()`.

## Windows (`UseWin32`)

Entry point:

- `UseWin32()`

Options:

- `Win32PlatformOptions`
  - `RenderingMode`
  - `CompositionMode`
  - `DpiAwareness`
  - `OverlayPopups`
  - `ShouldRenderOnUIThread`
  - `WglProfiles`
  - `CustomPlatformGraphics`
  - `WinUICompositionBackdropCornerRadius`
  - `GraphicsAdapterSelectionCallback`

Related enums:

- `Win32RenderingMode`
- `Win32DpiAwareness`
- `Win32CompositionMode`

Guidance:

- keep at least one software fallback in `RenderingMode`,
- use composition mode fallback order consciously,
- set `GraphicsAdapterSelectionCallback` only when you have measured adapter-specific issues.

## Linux/X11 (`UseX11`)

Entry points:

- `UseX11()`
- `InitializeX11Platform(X11PlatformOptions? options = null)`

Options:

- `X11PlatformOptions`
  - `RenderingMode`
  - `OverlayPopups`
  - `UseDBusMenu`
  - `UseDBusFilePicker`
  - `EnableIme`
  - `EnableInputFocusProxy`
  - `EnableSessionManagement`
  - `ShouldRenderOnUIThread`
  - `GlProfiles`
  - `GlxRendererBlacklist`
  - `WmClass`
  - `EnableMultiTouch`
  - `UseRetainedFramebuffer`
  - `UseGLibMainLoop`
  - `ExterinalGLibMainLoopExceptionLogger`

Guidance:

- keep software fallback in rendering mode list,
- treat `InitializeX11Platform(...)` as advanced bootstrapping path,
- use GLib loop options only when integrating with GLib-hosted dependencies.

## macOS Native (`UseAvaloniaNative`)

Entry point:

- `UseAvaloniaNative()`

Options:

- `AvaloniaNativePlatformOptions`
  - `RenderingMode`
  - `OverlayPopups`
  - `AvaloniaNativeLibraryPath`
  - `AppSandboxEnabled`

Related enum:

- `AvaloniaNativeRenderingMode`

Additional macOS options:

- `MacOSPlatformOptions`
  - `ShowInDock`
  - `DisableDefaultApplicationMenuItems`
  - `DisableNativeMenus`
  - `DisableSetProcessName`
  - `DisableAvaloniaAppDelegate`

## Browser/WebAssembly

Entry points:

- `StartBrowserAppAsync(mainDivId, options)`
- `SetupBrowserAppAsync(options)`
- `UseBrowser()`

Options (`BrowserPlatformOptions`):

- `RenderingMode`
- `FrameworkAssetPathResolver`
- `RegisterAvaloniaServiceWorker`
- `AvaloniaServiceWorkerScope`
- `PreferFileDialogPolyfill`
- `PreferManagedThreadDispatcher`

Related enum:

- `BrowserRenderingMode`

Guidance:

- choose rendering fallback order deliberately (`WebGL2`, `WebGL1`, software),
- use managed dispatcher settings according to Wasm threading model.

## Android

Entry point:

- `UseAndroid()`

Options:

- `AndroidPlatformOptions.RenderingMode`

Related enum:

- `AndroidRenderingMode`

Guidance:

- keep software fallback where reliability matters across device classes.

## iOS

Entry points:

- `UseiOS()`
- `UseiOS(IAvaloniaAppDelegate)`

Options:

- `iOSPlatformOptions.RenderingMode`

Related enum:

- `iOSRenderingMode`

Guidance:

- keep rendering fallback order explicit.

## Linux Framebuffer and Headless

Framebuffer entry points:

- `StartLinuxFbDev(...)`
- `StartLinuxDrm(...)`
- `StartLinuxDirect(...)`

Framebuffer options:

- `LinuxFramebufferPlatformOptions`
  - `Fps`
  - `ShouldRenderOnUIThread`

Headless entry point:

- `UseHeadless(AvaloniaHeadlessPlatformOptions)`

Headless options:

- `UseHeadlessDrawing`
- `FrameBufferFormat`

Use headless for tests, CI rendering checks, and non-windowed automation.

## Platform Option Injection Pattern

```csharp
public static AppBuilder BuildAvaloniaApp()
    => AppBuilder.Configure<App>()
        .UsePlatformDetect()
        .With(new Win32PlatformOptions
        {
            RenderingMode = new[]
            {
                Win32RenderingMode.AngleEgl,
                Win32RenderingMode.Software
            }
        })
        .With(new X11PlatformOptions
        {
            RenderingMode = new[]
            {
                X11RenderingMode.Glx,
                X11RenderingMode.Software
            }
        });
```

## Platform Boot Mistakes

1. Selecting only GPU path with no fallback.
2. Scattering platform config across unrelated files.
3. Mixing incompatible backend options in one startup profile.
4. Tuning options without measuring startup latency and frame-time impact.
5. Applying advanced platform-only knobs (`GlProfiles`, `GraphicsAdapterSelectionCallback`) without reproducer-backed need.

## XAML-First and Code-Only Usage

Default mode:

- keep UI composition in XAML,
- keep platform bootstrapping in code (`Program.cs`),
- use full code-only UI only when explicitly requested.

XAML-first references:

- `App.axaml` style/resource includes
- `Window`/`UserControl` definitions in `.axaml`

XAML-first usage example:

```xml
<Application xmlns="https://github.com/avaloniaui"
             xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
             x:Class="MyApp.App">
  <Application.Styles>
    <FluentTheme />
    <StyleInclude Source="avares://MyApp/Styles/Common.axaml" />
  </Application.Styles>
</Application>
```

Code-only alternative (on request):

```csharp
public static AppBuilder BuildAvaloniaApp()
    => AppBuilder.Configure<App>()
        .UsePlatformDetect()
        .With(new Win32PlatformOptions
        {
            RenderingMode = new[]
            {
                Win32RenderingMode.AngleEgl,
                Win32RenderingMode.Software
            }
        });
```
