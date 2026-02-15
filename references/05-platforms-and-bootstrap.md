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

## Common Cross-Platform Extensions

- `UseSkia()`
- `WithInterFont()`
- `UseManagedSystemDialogs()`

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

Guidance:
- Keep at least one software fallback in `RenderingMode`.
- Use composition mode fallback order consciously.

## Linux/X11 (`UseX11`)

Entry point:
- `UseX11()`

Options:
- `X11PlatformOptions`
  - `RenderingMode`
  - `OverlayPopups`
  - `UseDBusMenu`
  - `UseDBusFilePicker`
  - `EnableIme`
  - `EnableSessionManagement`
  - `ShouldRenderOnUIThread`
  - `UseGLibMainLoop`

Guidance:
- Keep software fallback in rendering mode list.
- Use GLib loop only when required by hosted GLib dependencies.

## macOS Native (`UseAvaloniaNative`)

Entry point:
- `UseAvaloniaNative()`

Options:
- `AvaloniaNativePlatformOptions`
  - `RenderingMode`
  - `OverlayPopups`
  - `AvaloniaNativeLibraryPath`
  - `AppSandboxEnabled`
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

Guidance:
- Choose rendering fallback order deliberately (`WebGL2`, `WebGL1`, software).
- Use managed dispatcher settings according to Wasm threading model.

## Android

Entry point:
- `UseAndroid()`

Options:
- `AndroidPlatformOptions.RenderingMode`

Guidance:
- Keep software fallback where reliability matters across device classes.

## iOS

Entry point:
- `UseiOS()` / `UseiOS(IAvaloniaAppDelegate)`

Options:
- `iOSPlatformOptions.RenderingMode`

Guidance:
- Keep rendering fallback order explicit.

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
4. Tuning options without measuring impact on startup latency and frame time.

## XAML-First and Code-Only Usage

Default mode:
- Keep UI composition in XAML.
- Keep platform bootstrapping in code (`Program.cs`), and only use full code-only UI when requested.

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
