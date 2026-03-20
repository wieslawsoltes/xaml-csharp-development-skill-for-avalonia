# TopLevel, Window, and Runtime Services

## Table of Contents
1. Scope and APIs
2. `TopLevel` Runtime Services Surface
3. TopLevel State, Theme, and Transparency APIs
4. Window and WindowBase Integration
5. Window Metadata and Event Argument Tails
6. Lifetime-Aware Service Access Patterns
7. Practical Patterns
8. Troubleshooting

## Scope and APIs

Primary app-facing APIs:

- `TopLevel`
- `WindowBase`
- `Window`
- `TopLevel.GetTopLevel(...)`
- `WindowIcon`
- `WindowTransparencyLevel`, `WindowTransparencyLevelCollection`
- `WindowCloseReason`, `WindowClosingEventArgs`
- `WindowResizeReason`, `WindowResizedEventArgs`

Service entry points exposed by `TopLevel`:

- `StorageProvider`
- `Clipboard`
- `Launcher`
- `Screens`
- `InsetsManager`
- `InputPane`
- `FocusManager`
- `PlatformSettings`

Version note:
- this stable reference reflects the `11.3.12` `TopLevel` surface,
- for Avalonia 12 migration, see [`68-avalonia-12-migration-guide.md`](68-avalonia-12-migration-guide) because `TopLevel` is no longer guaranteed to be the visual root, `IPresentationSource` becomes part of the public host model, and some older root-service assumptions no longer hold.

## `TopLevel` Runtime Services Surface

Use `TopLevel.GetTopLevel(visual)` at runtime, then consume host services from that surface.

```csharp
var topLevel = TopLevel.GetTopLevel(this);
if (topLevel is null)
    return;

var storage = topLevel.StorageProvider;
var launcher = topLevel.Launcher;
var clipboard = topLevel.Clipboard;
var screens = topLevel.Screens;
```

Platform/host interop helpers:

- `TryGetPlatformHandle()`
- `RequestPlatformInhibition(PlatformInhibitionType type, string reason)`
- `RequestAnimationFrame(Action<TimeSpan> action)`

Use case examples:

- prevent sleep during long-running foreground workflows (`RequestPlatformInhibition`),
- schedule frame-aligned visuals (`RequestAnimationFrame`),
- bridge native interop (`TryGetPlatformHandle`).

## TopLevel State, Theme, and Transparency APIs

Core `TopLevel` properties/events:

- `ClientSizeProperty`, `ClientSize`
- `FrameSizeProperty`, `FrameSize`
- `PointerOverElementProperty`
- `TransparencyLevelHintProperty`
- `ActualTransparencyLevelProperty`
- `TransparencyBackgroundFallbackProperty`, `TransparencyBackgroundFallback`
- `ActualThemeVariantProperty`, `RequestedThemeVariantProperty`
- `SystemBarColorProperty`
- `AutoSafeAreaPaddingProperty`
- `BackRequestedEvent`
- `Opened`, `Closed`, `ScalingChanged`, `BackRequested`
- `RenderScaling`
- `TopLevel.PlatformImpl`

Attached-property helpers:

- `SetSystemBarColor(...)`, `GetSystemBarColor(...)`
- `SetAutoSafeAreaPadding(...)`, `GetAutoSafeAreaPadding(...)`

Pattern:

```csharp
if (TopLevel.GetTopLevel(this) is { } top)
{
    top.TransparencyBackgroundFallback = Brushes.Black;

    TopLevel.SetAutoSafeAreaPadding(this, true);
    TopLevel.SetSystemBarColor(this, new SolidColorBrush(Colors.Black));
}
```

## Window and WindowBase Integration

`WindowBase : TopLevel` adds window-host behavior:

- `IsActiveProperty`, `IsActive`
- `OwnerProperty`, `Owner`
- `TopmostProperty`, `Topmost`
- `DesktopScaling`
- `Activate()`
- `PositionChanged`, `Resized`, `Activated`, `Deactivated`
- `WindowBase.PlatformImpl`

`Window` adds desktop-window semantics:

- `WindowClosingBehavior`
- `SizeToContentProperty`, `SizeToContent`
- `ExtendClientAreaToDecorationsHintProperty`
- `ExtendClientAreaChromeHintsProperty`
- `ExtendClientAreaTitleBarHeightHintProperty`
- `IsExtendedIntoWindowDecorationsProperty`
- `WindowDecorationMarginProperty`, `WindowDecorationMargin`
- `OffScreenMarginProperty`, `OffScreenMargin`
- `SystemDecorationsProperty`, `SystemDecorations`
- `ShowActivatedProperty`, `ShowActivated`
- `ShowInTaskbarProperty`, `ShowInTaskbar`
- `ClosingBehaviorProperty`, `ClosingBehavior`
- `WindowStateProperty`, `WindowState`
- `IconProperty`, `Icon`
- `WindowStartupLocationProperty`, `WindowStartupLocation`
- `CanResizeProperty`, `CanResize`
- `CanMinimizeProperty`, `CanMinimize`
- `CanMaximizeProperty`, `CanMaximize`
- `WindowClosedEvent`, `WindowOpenedEvent`
- `OwnedWindows`
- `IsExtendedIntoWindowDecorations`
- `IsDialog`
- `Window.PlatformImpl`
- `SortWindowsByZOrder(Window[] windows)`

Constructors frequently used by host integrations:

- `TopLevel(ITopLevelImpl impl)`
- `TopLevel(ITopLevelImpl impl, IAvaloniaDependencyResolver? dependencyResolver)`
- `WindowBase(IWindowBaseImpl impl)`
- `WindowBase(IWindowBaseImpl impl, IAvaloniaDependencyResolver? dependencyResolver)`

## Window Metadata and Event Argument Tails

Window transparency metadata:

- `WindowTransparencyLevel` static values:
  - `None`
  - `Transparent`
  - `Blur`
  - `AcrylicBlur`
  - `Mica`
- `WindowTransparencyLevelCollection`

Window icon APIs:

- `WindowIcon(Bitmap bitmap)`
- `WindowIcon(string fileName)`
- `WindowIcon(Stream stream)`
- `Save(Stream stream)`

Window event argument tails:

- `WindowCloseReason`
- `WindowClosingEventArgs` (`CloseReason`, `IsProgrammatic`)
- `WindowResizeReason`
- `WindowResizedEventArgs` (`Reason`)

Pattern:

```csharp
if (topLevel is Window window)
{
    window.TransparencyLevelHint = new WindowTransparencyLevelCollection(new[]
    {
        WindowTransparencyLevel.Mica,
        WindowTransparencyLevel.Blur
    });

    window.Closing += (_, e) =>
    {
        if (e.CloseReason == WindowCloseReason.OSShutdown)
            return;

        if (!e.IsProgrammatic && HasInFlightOperation())
            e.Cancel = true;
    };

    window.Resized += (_, e) =>
    {
        if (e.Reason == WindowResizeReason.User)
            PersistWindowSize(window.ClientSize);
    };
}
```

## Lifetime-Aware Service Access Patterns

In desktop apps, cache only short-lived references to top-level services; resolve from the active `TopLevel` when needed.

```csharp
public async Task OpenFromWindowAsync(Window window)
{
    var storage = window.StorageProvider;
    var files = await storage.OpenFilePickerAsync(new FilePickerOpenOptions());
    _ = files.Count;
}
```

When wiring in `Application`:

- use `IClassicDesktopStyleApplicationLifetime.MainWindow` for primary service root,
- in multi-window flows, resolve services from the specific active `Window`/`TopLevel` instance.

## Practical Patterns

1. Resolve services from the current surface.
- Avoid static service singletons for `Clipboard`/`Launcher`/`StorageProvider`.

2. Handle scaling and insets as runtime signals.
- Subscribe to `ScalingChanged` and query `InsetsManager` as layout conditions change.

3. Keep platform inhibition scopes short.
- Dispose the handle returned from `RequestPlatformInhibition(...)` promptly.

4. Gate platform-handle usage.
- Treat `TryGetPlatformHandle()` as optional; include null-safe fallbacks.

## Troubleshooting

1. `StorageProvider` or `Clipboard` unavailable.
- Ensure the control is attached and `TopLevel.GetTopLevel(...)` is non-null.

2. Theme/transparency mismatch.
- Check `RequestedThemeVariant`, `ActualThemeVariant`, `TransparencyLevelHint`, and `ActualTransparencyLevel` together.

3. Window activation behavior inconsistent.
- Inspect `IsActive`, `Topmost`, `Owner`, and `WindowState` transitions.

4. Host-specific API behavior differs across platforms.
- Expected; use the portable `TopLevel`/`WindowBase` surface first and keep platform specifics isolated.
