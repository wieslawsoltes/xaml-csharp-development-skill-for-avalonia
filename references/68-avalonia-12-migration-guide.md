# Avalonia 12 Migration Guide

## Table of Contents
1. Scope and Status
2. Source Priority for This Lane
3. Upgrade Baseline First
4. Breaking Changes to Fix First
5. Behavior Changes to Re-verify
6. Platform-Specific Migration Notes
7. Additional Source-Backed Deltas Worth Keeping
8. Code Migration Examples
9. AOT, Trimming, and Build Notes
10. Troubleshooting
11. Full Reference Pointers

## Scope and Status

This lane extends the skill with Avalonia 12 migration guidance while keeping the rest of the repository pinned to Avalonia `11.3.12`.

Current status for this guide:

- official breaking-change docs page reviewed on **March 20, 2026**: [Breaking changes in Avalonia 12](https://docs.avaloniaui.net/docs/avalonia12-breaking-changes),
- Avalonia origin tags reviewed on **March 20, 2026**,
- latest published `12.0.0*` tag on origin at that point: **`12.0.0-rc1`**,
- GitHub release date of `12.0.0-rc1`: **March 19, 2026**,
- generated companion artifacts in this repository therefore still target **`12.0.0-rc1`**.

Use this guide when you are porting an application, library, or samples from `11.3.12` toward Avalonia 12. The curated guidance below follows the current official Avalonia 12 docs page, while the generated API index and generated migration report in this repo remain source-backed against `12.0.0-rc1` until a newer Avalonia 12 tag exists upstream.

## Source Priority for This Lane

Use sources in this order for Avalonia 12 migration work:

1. the official docs page: [Breaking changes in Avalonia 12](https://docs.avaloniaui.net/docs/avalonia12-breaking-changes),
2. the latest published Avalonia 12 tag on GitHub Releases,
3. this repository's generated companion references:
   - [`69-avalonia-12-breaking-changes-and-new-api-catalog.md`](69-avalonia-12-breaking-changes-and-new-api-catalog),
   - [`api-index-12.0.0-rc1-generated.md`](api-index-12.0.0-rc1-generated),
4. older Avalonia wiki pages as historical background only when they still add detail not present on the docs page.

Current generated evidence for this lane:

- `11.3.12 -> 12.0.0-rc1`: `591` approved compatibility suppressions and `1175` added public signatures,
- `12.0.0-preview2 -> 12.0.0-rc1`: `168` added public signatures and `73` removed public signatures in the parser view.

Coverage intent:

- the official docs page is treated as the authoritative user-facing migration checklist,
- the generated report remains the exhaustive source-backed inventory for the latest published Avalonia 12 tag,
- this guide focuses on sequencing, high-risk changes, and app-development-oriented examples.

## Upgrade Baseline First

Handle these before you start fixing individual compile errors.

### 1. Move the runtime baseline

- Avalonia 12 drops `.NET Framework` and `.NET Standard`.
- supported runtime line is `.NET 8+`,
- the official docs page recommends `.NET 10`,
- Android and iOS now require `.NET 10`.

Practical rule:

- upgrade target frameworks, SDKs, CI images, and mobile workloads first.

### 2. Upgrade all Avalonia packages together

The official docs page is written for the Avalonia 12 release line, not a mixed-package upgrade.

Practical rule:

- move all `Avalonia*` package references together,
- if you are using this repository's generated artifacts for symbol lookup, remember they are still anchored to `12.0.0-rc1` as of **March 20, 2026**.

### 3. Replace legacy DevTools packaging

The docs page now treats this as a first-class breaking change:

- `Avalonia.Diagnostics` is removed,
- use `AvaloniaUI.DiagnosticsSupport`,
- rename `AttachDevTools()` to `AttachDeveloperTools()`.

### 4. Expect compiled bindings by default

`<AvaloniaUseCompiledBindingsByDefault>` now defaults to `true`.

Practical rule:

- add `x:DataType`,
- fix binding compile failures early,
- use `{ReflectionBinding ...}` only for real dynamic cases.

### 5. Re-check custom startup when you call `UseSkia()` directly

The text shaper is now configured independently from the renderer.

Practical rule:

- `UsePlatformDetect()` still gives you the standard text setup,
- if you explicitly configure Skia with `.UseSkia()`, add `.UseHarfBuzz()` and reference `Avalonia.HarfBuzz`.

### 6. Remove packages that no longer exist in Avalonia 12

The official docs page calls out these removals:

- `Avalonia.Direct2D1`,
- `Avalonia.Browser.Blazor`,
- `Avalonia.Tizen`,
- `Avalonia.Diagnostics`.

## Breaking Changes to Fix First

These are the migration steps most likely to block the first successful build.

### 1. Binding hierarchy and code-only binding APIs changed

The docs page and generated diff agree on the core binding break:

- `IBinding` is removed; use `BindingBase`,
- `Binding` remains only as the compatibility reflection-binding shape,
- `InstancedBinding` is removed; use `BindingExpressionBase`,
- C# binding construction should use `ReflectionBinding` and `CompiledBinding` directly,
- old `(path, mode)` constructor overloads are gone; set `Mode` and other options explicitly.

Migration rule:

- fix `using` directives first,
- then fix code-only binding construction,
- then rebuild to catch remaining binding-path issues.

### 2. Binding plugins are gone, and data-annotations validation is no longer implicitly on

Avalonia 12 removes configurable binding plugins and disables the data-annotations plugin by default.

Migration rule:

- if your forms depended on `System.ComponentModel.DataAnnotations`, opt back in with `AppBuilder.WithDataAnnotationsValidation()`,
- remove plugin customization code,
- remove `UpdateDataValidation(...)` overrides that only forwarded errors via `DataValidationErrors.SetError(...)`.

### 3. Clipboard and drag/drop code must move off `IDataObject`

The docs page is explicit here:

- `IDataObject` is removed,
- `DataObject` no longer carries the old behavior,
- `IClipboard` now favors typed extension helpers,
- drag/drop and clipboard payloads move to `IDataTransfer` / `IAsyncDataTransfer` / `DataTransfer` / `DataTransferItem`.

Migration rule:

- replace `DataFormats.*` with `DataFormat.*`,
- replace `SetDataObjectAsync(...)` with `SetDataAsync(...)`,
- replace `GetTextAsync()` with `TryGetTextAsync()` and similar typed helpers,
- move drag/drop code to `DragDrop.DoDragDropAsync(...)` and `DragEventArgs.DataTransfer`.
- keep the Avalonia 11 dialog removals in view as well: `OpenFileDialog`, `OpenFolderDialog`, `SaveFileDialog`, and related legacy dialog types stay removed on the Avalonia 12 line,
- move picker flows to `TopLevel.StorageProvider` and the `FilePicker*Options` types.

### 4. `TopLevel` can no longer be treated as "the visual root plus every root service"

Avalonia 12 changes the root-host model:

- a `TopLevel` is not guaranteed to be the root `Visual`,
- removed public root interfaces include `IInputRoot`, `ILayoutRoot`, `IRenderRoot`, and related shapes,
- `IPresentationSource` is now part of the public host model,
- `VisualExtensions.GetVisualRoot()` is not the migration-safe path for this scenario anymore.

Migration rule:

- use `TopLevel.GetTopLevel(visual)` to reach window/runtime services,
- use `GetPresentationSource(...)` when you need the host/root bridge,
- stop depending on removed root-interface contracts.

### 5. Window decorations were renamed and reworked

This is one of the most visible app-facing breaks:

- `SystemDecorations` became `WindowDecorations`,
- `Window.ExtendClientAreaChromeHints` was removed,
- `TitleBar`, `CaptionButtons`, and `ChromeOverlayLayer` were removed,
- `WindowDrawnDecorations` is the replacement managed-decoration surface.

Migration rule:

- rename `SystemDecorations` property usage to `WindowDecorations`,
- keep `ExtendClientAreaToDecorationsHint`,
- stop building new code around `ExtendClientAreaChromeHints`,
- use `WindowDecorationProperties.ElementRole` and `WindowDrawnDecorations`-based patterns for custom chrome.

### 6. Input, selection, gesture, and access-key behavior changed

Important official docs-page changes:

- touch and pen selection now trigger on pointer release,
- container types now handle selection input directly,
- override `ShouldTriggerSelection(...)` and `UpdateSelectionFromEvent(...)` for selection customization,
- gesture attached events moved off the public `Gestures` class and are exposed directly on `InputElement`,
- `AccessText.AccessKey` changed from `char` to `string?`.

Migration rule:

- move item-selection interception closer to the item container,
- remove the `Gestures.` prefix in XAML,
- update any code that reads `AccessText.AccessKey`.

### 7. Several small but real type-shape changes now surface in app code

The official docs page also calls out these practical breaks:

- `FuncMultiValueConverter` now takes `IReadOnlyList<TIn>`,
- `Screen` is abstract; do not construct it directly,
- `ResourcesChangedEventArgs` is now a struct; use `ResourcesChangedEventArgs.Create()` if you must create one,
- text-formatting constructors moved `FontFeatureCollection` to the trailing optional position.

### 8. Platform and package removals are real migration work, not footnotes

Treat these as first-pass fixes if your codebase touches them:

- `Avalonia.Direct2D1` is gone; use Skia,
- implicit `BinaryFormatter` clipboard serialization on Windows is gone,
- `Avalonia.Browser.Blazor` is gone; use `Avalonia.Browser` and `AvaloniaView`,
- `Avalonia.Tizen` is gone from the main repository line.

## Behavior Changes to Re-verify

These are runtime checks, not just compile fixes.

- compiled bindings are now the default, so some failures move from runtime to build time,
- touch and pen selection/focus now complete on release rather than press,
- `Dispatcher.InvokeAsync(...)` now captures execution context,
- library and control code should prefer `AvaloniaObject.Dispatcher` or `Dispatcher.CurrentDispatcher` for multi-dispatcher awareness,
- window-margin and maximized-client-area workarounds on Windows should be re-tested because `ExtendClientAreaToDecorationsHint` behavior was fixed,
- access keys now trigger from the printed symbol, not the old virtual-key interpretation,
- old Type 1 fonts (`.pfb` / `.pfm`) are no longer supported,
- custom controls that used `enableDataValidation: true` should be re-tested because validation now flows automatically.

Recommended verification passes:

- build Debug and Release,
- rebuild XAML with source info enabled,
- exercise window chrome, dialogs, drag/drop, clipboard, validation, focus, gesture, and access-key flows,
- re-run mobile startup paths and headless test projects,
- re-test old Windows client-area workarounds and remove the ones Avalonia 12 fixed.

## Platform-Specific Migration Notes

### Windows

- replace `Avalonia.Direct2D1` with `Avalonia.Skia`,
- remove any assumption that arbitrary objects round-trip through the clipboard via `BinaryFormatter`,
- remove old `ExtendClientAreaToDecorationsHint` workaround margins and title-bar hacks before re-adding anything.

### Android

The docs page now expects this bootstrap shape:

- `MainActivity` inherits plain `AvaloniaMainActivity`,
- add an `[Application]` type deriving from `AvaloniaAndroidApplication<TApp>`,
- prefer `IActivityApplicationLifetime.MainViewFactory`,
- stop overriding `CreateAppBuilder()` and `CustomizeAppBuilder(...)` on `AvaloniaMainActivity`.

### iOS

- scene-based app startup is now the expected model,
- `AvaloniaAppDelegate.Window` stays `null` after initialization,
- if you need the native `UIWindow`, detect it from `AvaloniaView.MovedToWindow`.

### Browser and Tizen

- move off `Avalonia.Browser.Blazor`,
- treat Tizen support as out-of-tree for Avalonia 12.

### Headless

Avalonia 12 updates the supported unit-test baselines:

- xUnit support now targets version `3`,
- NUnit support now targets version `4`.

## Additional Source-Backed Deltas Worth Keeping

The official docs page is now the primary migration source, but the repository's source-backed RC1 scan still exposes several app-facing deltas worth keeping in this guide because they affect real migrations.

### Focus event and focus-manager changes

The generated `11.3.12 -> 12.0.0-rc1` diff still surfaces important focus changes:

- `GotFocusEventArgs` is replaced by `FocusChangedEventArgs` on `GotFocus` / `LostFocus`,
- `FocusChangedEventArgs` carries `OldFocusedElement`, `NewFocusedElement`, `NavigationMethod`, and `KeyModifiers`,
- `IFocusManager.ClearFocus()` assumptions no longer hold; move toward explicit focus transfer.

### Swipe recognizer changes

Still relevant for touch-first shells and custom paging surfaces:

- `SwipeGestureRecognizer` now uses `CanHorizontallySwipe`, `CanVerticallySwipe`, and `IsMouseEnabled`,
- `CrossAxisCancelThreshold` and `EdgeSize` are gone,
- `SwipeGestureEventArgs` now exposes incremental `Delta` plus `Velocity`,
- `SwipeGestureEndedEventArgs` was added.

### Preview2 -> RC1 deltas still worth checking in real codebases

These are not from the official docs page, but they still matter if your code moved early:

- `DrawerBreakpointWidth` became `DrawerBreakpointLength`,
- page lifecycle hooks now run after transitions complete,
- `PipsPager` landed after the preview2 baseline used by the earlier lane.

## Code Migration Examples

### Target framework, developer tools, and text shaping

Before:

```xml
<PropertyGroup>
  <TargetFramework>netstandard2.0</TargetFramework>
</PropertyGroup>

<ItemGroup>
  <PackageReference Include="Avalonia.Diagnostics" Version="11.3.12" />
</ItemGroup>
```

```csharp
public static AppBuilder BuildAvaloniaApp()
    => AppBuilder.Configure<App>()
        .UseSkia();
```

After:

```xml
<PropertyGroup>
  <TargetFramework>net10.0</TargetFramework>
</PropertyGroup>

<ItemGroup>
  <PackageReference Include="AvaloniaUI.DiagnosticsSupport" Version="2.2.0" />
  <PackageReference Include="Avalonia.HarfBuzz" Version="12.0.0-rc1" />
</ItemGroup>
```

```csharp
public static AppBuilder BuildAvaloniaApp()
    => AppBuilder.Configure<App>()
        .UseSkia()
        .UseHarfBuzz();
```

Use `AttachDeveloperTools()` on the Avalonia 12 line.

### Binding constructor migration

Before:

```csharp
using Avalonia.Data;

var nameBinding = new Binding("Customer.Name", BindingMode.TwoWay);
var titleBinding = new ReflectionBinding("WindowTitle", BindingMode.OneWay);
```

After:

```csharp
using Avalonia.Data;

var nameBinding = new Binding("Customer.Name")
{
    Mode = BindingMode.TwoWay
};

var titleBinding = new ReflectionBinding("WindowTitle")
{
    Mode = BindingMode.OneWay
};

var dirtyBinding = CompiledBinding.Create<EditorViewModel, bool>(vm => vm.IsDirty);
```

### Clipboard migration

Before:

```csharp
var data = new DataObject();
data.Set(DataFormats.Text, "some text");

await clipboard.SetDataObjectAsync(data);
var text = await clipboard.GetTextAsync();
```

After:

```csharp
var item = new DataTransferItem();
item.Set(DataFormat.Text, "some text");

var data = new DataTransfer();
data.Add(item);

await clipboard.SetDataAsync(data);
var text = await clipboard.TryGetTextAsync();
```

### `OpenFileDialog` to `StorageProvider`

Before:

```csharp
var dialog = new OpenFileDialog
{
    AllowMultiple = false
};

var result = await dialog.ShowAsync(this);
```

After:

```csharp
var topLevel = TopLevel.GetTopLevel(this)
    ?? throw new InvalidOperationException("No TopLevel available.");

var files = await topLevel.StorageProvider.OpenFilePickerAsync(
    new FilePickerOpenOptions
    {
        AllowMultiple = false,
        FileTypeFilter = new[]
        {
            new FilePickerFileType("Images")
            {
                Patterns = new[] { "*.png", "*.jpg" }
            }
        }
    });
```

### Window chrome migration

Before:

```xaml
<Window xmlns="https://github.com/avaloniaui"
        xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
        SystemDecorations="None"
        ExtendClientAreaChromeHints="NoChrome"
        ExtendClientAreaToDecorationsHint="True">
  <Grid />
</Window>
```

After:

```xaml
<Window xmlns="https://github.com/avaloniaui"
        xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
        xmlns:chrome="clr-namespace:Avalonia.Controls.Chrome;assembly=Avalonia.Controls"
        WindowDecorations="None"
        ExtendClientAreaToDecorationsHint="True">
  <Grid>
    <Button chrome:WindowDecorationProperties.ElementRole="CloseButton"
            HorizontalAlignment="Right"
            Content="Close" />
  </Grid>
</Window>
```

### Gesture event migration

Before:

```xaml
<Button Gestures.Pinch="Button_Pinch" />
```

After:

```xaml
<Button Pinch="Button_Pinch" />
```

### Android bootstrap migration

Before (`11.3.12`):

```csharp
[Activity(MainLauncher = true)]
public class MainActivity : AvaloniaMainActivity<App>
{
}
```

After (Avalonia 12 line):

```csharp
[Application]
public class AndroidApp : AvaloniaAndroidApplication<App>
{
    protected AndroidApp(nint javaReference, JniHandleOwnership transfer)
        : base(javaReference, transfer)
    {
    }
}

[Activity(MainLauncher = true)]
public class MainActivity : AvaloniaMainActivity
{
}
```

If you need dynamic content creation on Android, prefer:

```csharp
if (ApplicationLifetime is IActivityApplicationLifetime activityLifetime)
{
    activityLifetime.MainViewFactory = () => new MainView();
}
```

## AOT, Trimming, and Build Notes

- Avalonia 12's compiled-binding default is generally better for trimming than reflection-heavy binding usage.
- keep `ReflectionBinding` explicit and local,
- `AppBuilder.WithDataAnnotationsValidation()` is still a reflection-heavy opt-in,
- `CompiledBinding.Create(...)` is the preferred code-only binding path for AOT-conscious code,
- remove old developer-tools assumptions tied to `Avalonia.Diagnostics`.

## Troubleshooting

1. Build suddenly fails on views that worked in `11.3.12`.
- Add `x:DataType`, switch to `{CompiledBinding ...}`, or explicitly opt a binding into `{ReflectionBinding ...}`.

2. `AttachDevTools()` or `Avalonia.Diagnostics` no longer resolves.
- Move to `AvaloniaUI.DiagnosticsSupport` and `AttachDeveloperTools()`.

3. Startup throws `No text shaping system configured`.
- If you explicitly call `.UseSkia()`, add `.UseHarfBuzz()` and reference `Avalonia.HarfBuzz`.

4. Clipboard or drag/drop code no longer compiles.
- Replace `IDataObject`/`DataObject` usage with `IDataTransfer` / `IAsyncDataTransfer` / `DataTransfer`.

5. Touch selection, gesture handling, or item interception behaves differently.
- Re-check selection-on-release behavior and remove the old `Gestures.` prefix in XAML.

6. Custom title bar hit testing broke after the upgrade.
- Rename `SystemDecorations` to `WindowDecorations`, stop relying on `ExtendClientAreaChromeHints`, and use `WindowDecorationProperties.ElementRole`.

7. Android app starts but the Avalonia view is missing.
- Confirm the project now has an `[Application]` type inheriting `AvaloniaAndroidApplication<TApp>` and that `MainActivity` inherits plain `AvaloniaMainActivity`.

8. Headless test projects stopped restoring or running.
- Move test packages and adapters to xUnit `3` / NUnit `4` compatible versions.

## Full Reference Pointers

- curated migration lane: this file,
- source-backed break and new API catalog for the latest published Avalonia 12 tag: [`69-avalonia-12-breaking-changes-and-new-api-catalog.md`](69-avalonia-12-breaking-changes-and-new-api-catalog),
- source-backed Avalonia 12 API index for the latest published Avalonia 12 tag: [`api-index-12.0.0-rc1-generated.md`](api-index-12.0.0-rc1-generated),
- official upstream references:
  - [Breaking changes in Avalonia 12](https://docs.avaloniaui.net/docs/avalonia12-breaking-changes),
  - [Avalonia release: 12.0.0-rc1](https://github.com/AvaloniaUI/Avalonia/releases/tag/12.0.0-rc1),
  - [Avalonia wiki: v12 Breaking Changes](https://github.com/AvaloniaUI/Avalonia/wiki/v12-Breaking-Changes),
  - [Avalonia wiki: Breaking Changes](https://github.com/AvaloniaUI/Avalonia/wiki/Breaking-Changes),
- stable binding/build references:
  - [`02-bindings-xaml-aot.md`](02-bindings-xaml-aot),
  - [`41-xaml-compiler-and-build-pipeline.md`](41-xaml-compiler-and-build-pipeline),
- stable platform-service references:
  - [`29-storage-provider-and-file-pickers.md`](29-storage-provider-and-file-pickers),
  - [`31-clipboard-and-data-transfer.md`](31-clipboard-and-data-transfer),
- stable windowing/runtime references:
  - [`13-windowing-and-custom-decorations.md`](13-windowing-and-custom-decorations),
  - [`48-toplevel-window-and-runtime-services.md`](48-toplevel-window-and-runtime-services),
- stable diagnostics/testing/input references:
  - [`18-input-system-and-routed-events.md`](18-input-system-and-routed-events),
  - [`26-testing-stack-headless-render-and-ui-tests.md`](26-testing-stack-headless-render-and-ui-tests),
  - [`27-diagnostics-profiling-and-devtools.md`](27-diagnostics-profiling-and-devtools),
  - [`47-dispatcher-priority-operations-and-timers.md`](47-dispatcher-priority-operations-and-timers)
