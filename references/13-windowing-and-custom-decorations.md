# Windowing System and Custom Decorations

## Table of Contents
1. Scope and APIs
2. `Window` Surface and Decoration APIs
3. `WindowBase` Integration APIs
4. `TopLevel` Bridge APIs
5. Custom Client Area and Drag/Resize
6. Window Metadata and Event Argument APIs
7. Platform-Specific Decoration Hooks
8. Best Practices
9. Troubleshooting

## Scope and APIs

Primary app-building APIs:

- `Window`, `WindowBase`, `TopLevel`
- `SystemDecorations`, `SizeToContent`, `WindowClosingBehavior`
- `WindowTransparencyLevel`, `WindowTransparencyLevelCollection`
- `ExtendClientAreaToDecorationsHint`, `ExtendClientAreaChromeHints`, `ExtendClientAreaTitleBarHeightHint`
- `Window.BeginMoveDrag(...)`, `Window.BeginResizeDrag(...)`
- `Window.WindowDecorationMargin`, `Window.OffScreenMargin`
- `WindowIcon`
- `WindowCloseReason`, `WindowClosingEventArgs`
- `WindowResizeReason`, `WindowResizedEventArgs`

Related platform-facing interfaces (mostly backend-level):

- `ITopLevelImpl`
- `IWindowBaseImpl`
- `IWindowImpl`
- `IWindowingPlatform`

For service access from top-level surfaces (`StorageProvider`, `Clipboard`, `Launcher`, `Screens`, platform handle), see:
- [`48-toplevel-window-and-runtime-services.md`](48-toplevel-window-and-runtime-services)

## `Window` Surface and Decoration APIs

Key `Window` properties/events for custom chrome and host behavior:

- `SizeToContentProperty`, `SizeToContent`
- `ExtendClientAreaChromeHintsProperty`, `ExtendClientAreaChromeHints`
- `WindowDecorationMarginProperty`, `WindowDecorationMargin`
- `OffScreenMarginProperty`, `OffScreenMargin`
- `SystemDecorationsProperty`, `SystemDecorations`
- `ClosingBehaviorProperty`, `ClosingBehavior`
- `WindowStateProperty`, `WindowState`
- `IconProperty`, `Icon`
- `WindowStartupLocationProperty`, `WindowStartupLocation`
- `OwnedWindows`
- `IsExtendedIntoWindowDecorations`
- `IsDialog`
- `Closing`

Lifecycle and ordering helpers:

- `Show()`, `Show(owner)`, `ShowDialog(owner)`, `ShowDialog<TResult>(owner)`
- `Hide()`, `Close()`, `Close(dialogResult)`
- `SortWindowsByZOrder(Window[] windows)`

Platform access:

- `Window.PlatformImpl`

## `WindowBase` Integration APIs

Useful `WindowBase` APIs for host-level coordination:

- `OwnerProperty`, `Owner`
- `IsActive`
- `Topmost`
- `DesktopScaling`
- `Activate()`
- `PositionChanged`, `Resized`, `Activated`, `Deactivated`
- `WindowBase.PlatformImpl`

Use `WindowBase` events when writing shared behaviors that apply to normal windows and derived host surfaces.

## `TopLevel` Bridge APIs

`WindowBase : TopLevel`, so decoration code is often coupled with these shared members:

- `ClientSizeProperty`, `ClientSize`
- `FrameSizeProperty`, `FrameSize`
- `PointerOverElementProperty`
- `TransparencyLevelHintProperty`
- `ActualTransparencyLevelProperty`
- `TransparencyBackgroundFallbackProperty`, `TransparencyBackgroundFallback`
- `SystemBarColorProperty`, `SetSystemBarColor(...)`, `GetSystemBarColor(...)`
- `SetAutoSafeAreaPadding(...)`, `GetAutoSafeAreaPadding(...)`
- `RenderScaling`
- `Opened`, `ScalingChanged`, `BackRequested`
- `TopLevel.PlatformImpl`, `TryGetPlatformHandle()`

## Custom Client Area and Drag/Resize

To build custom title bars/chrome:

1. Set `ExtendClientAreaToDecorationsHint="True"`.
2. Configure `ExtendClientAreaChromeHints`.
3. Set `SystemDecorations` as needed.
4. Handle dragging/resizing via window APIs.

Example:

```xml
<Window x:Class="MyApp.MainWindow"
        ExtendClientAreaToDecorationsHint="True"
        ExtendClientAreaChromeHints="PreferSystemChrome"
        ExtendClientAreaTitleBarHeightHint="32"
        SystemDecorations="Full" />
```

For custom drag handles:

```csharp
private void TitlePointerPressed(object? sender, PointerPressedEventArgs e)
{
    if (e.GetCurrentPoint(this).Properties.IsLeftButtonPressed)
        BeginMoveDrag(e);
}
```

For custom resize grips:

```csharp
private void ResizeGripPressed(object? sender, PointerPressedEventArgs e)
{
    BeginResizeDrag(WindowEdge.SouthEast, e);
}
```

Built-in managed decoration controls:

- `Avalonia.Controls.Chrome.TitleBar`
- `Avalonia.Controls.Chrome.CaptionButtons`

## Window Metadata and Event Argument APIs

Transparency APIs:

- `WindowTransparencyLevel` (record struct)
- static values:
  - `WindowTransparencyLevel.None`
  - `WindowTransparencyLevel.Transparent`
  - `WindowTransparencyLevel.Blur`
  - `WindowTransparencyLevel.AcrylicBlur`
  - `WindowTransparencyLevel.Mica`
- `WindowTransparencyLevelCollection`

Example transparency hint ordering:

```csharp
TransparencyLevelHint = new WindowTransparencyLevelCollection(new[]
{
    WindowTransparencyLevel.Mica,
    WindowTransparencyLevel.AcrylicBlur,
    WindowTransparencyLevel.Blur,
    WindowTransparencyLevel.Transparent,
    WindowTransparencyLevel.None
});
```

Window icon APIs:

- `WindowIcon(Bitmap bitmap)`
- `WindowIcon(string fileName)`
- `WindowIcon(Stream stream)`
- `Save(Stream stream)`

Example:

```csharp
using var iconStream = File.OpenRead("Assets/app-icon.ico");
Icon = new WindowIcon(iconStream);

using var outStream = File.Create("Assets/icon-copy.ico");
Icon?.Save(outStream);
```

Closing and resize event argument types:

- `WindowCloseReason`
- `WindowClosingEventArgs`
  - `CloseReason`
  - `IsProgrammatic`
- `WindowResizeReason`
- `WindowResizedEventArgs`
  - `Reason`

Example:

```csharp
Closing += (_, e) =>
{
    if (e.CloseReason == WindowCloseReason.ApplicationShutdown)
        return;

    if (!e.IsProgrammatic && HasUnsavedChanges())
        e.Cancel = true;
};

Resized += (_, e) =>
{
    if (e.Reason == WindowResizeReason.DpiChange)
        RecomputeDpiSensitiveLayout();
};
```

## Platform-Specific Decoration Hooks

Platform extension APIs for deeper control:

- Win32: `Win32Properties`
  - `AddWindowStylesCallback`
  - `AddWndProcHookCallback`
  - `NonClientHitTestResultProperty`
- X11: `X11Properties`
  - `NetWmWindowTypeProperty`
  - `WmClassProperty`

Use these only when cross-platform `Window`/`TopLevel` APIs are insufficient.

## Best Practices

- Start with portable `Window`/`WindowBase` APIs first.
- Keep drag/resize handlers in one chrome component.
- Observe `WindowDecorationMargin` and `OffScreenMargin` in layout/pointer hit regions.
- Treat `PlatformImpl` as an escape hatch, not baseline app code.

## Troubleshooting

1. Title bar visible but dragging fails.
- Ensure pointer handler calls `BeginMoveDrag` with left button pressed.

2. Resize handles do nothing.
- Confirm `CanResize=true` and call `BeginResizeDrag` with correct `WindowEdge`.

3. Client content overlaps system chrome.
- Use `WindowDecorationMargin`/`OffScreenMargin` to compensate.

4. Window close flow is inconsistent with owned windows.
- Check `ClosingBehavior` (`OwnerAndChildWindows` vs `OwnerWindowOnly`).

5. Cross-OS decoration differences.
- Expected; prefer portable APIs for baseline behavior and gate platform-specific hooks.
