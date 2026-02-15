# Avalonia App-Building API Map

This map focuses on public APIs that matter directly when building applications (not internal rendering/runtime internals).

## 1) App Startup and Lifetime

### `AppBuilder` (`src/Avalonia.Controls/AppBuilder.cs`)

Primary composition root:
- `AppBuilder.Configure<TApp>()`
- `AppBuilder.Configure<TApp>(Func<TApp>)`
- `UseWindowingSubsystem(Action, string)`
- `UseRenderingSubsystem(Action, string)`
- `UseRuntimePlatformSubsystem(Action, string)`
- `UseStandardRuntimePlatformSubsystem()`
- `With<T>(T options)` / `With<T>(Func<T>)`
- `ConfigureFonts(Action<FontManager>)`
- `SetupWithoutStarting()`
- `SetupWithLifetime(IApplicationLifetime)`
- `Start(AppMainDelegate, string[] args)`

Use:
- Compose backend and options only in `BuildAvaloniaApp()`.
- Keep `BuildAvaloniaApp()` deterministic and side-effect-light.
- Use `With<T>` for platform option objects instead of static mutable state.

Avoid:
- Relying on dynamic `Configure(Type)` patterns outside test/design contexts.

### `Application` (`src/Avalonia.Controls/Application.cs`)

Core extension points:
- `Initialize()`
- `RegisterServices()`
- `OnFrameworkInitializationCompleted()`

Global state and resources:
- `ApplicationLifetime`
- `Resources`
- `Styles`
- `DataTemplates`
- `TryGetResource(object, ThemeVariant?, out object?)`
- `RequestedThemeVariant`, `ActualThemeVariant`

Use:
- Load app XAML in `Initialize()`.
- Assign top-level window/view in `OnFrameworkInitializationCompleted()` based on lifetime interface.
- Keep application-level resources/styles small and layered.

### Lifetime interfaces (`src/Avalonia.Controls/ApplicationLifetimes/*.cs`)

- `IClassicDesktopStyleApplicationLifetime`
  - `MainWindow`, `Windows`, `ShutdownMode`, `TryShutdown(...)`, `ShutdownRequested`
- `IControlledApplicationLifetime`
  - `Startup`, `Exit`, `Shutdown(...)`
- `ISingleViewApplicationLifetime`
  - `MainView`
- `IActivatableLifetime` (feature API)
  - `Activated`, `Deactivated`, `TryLeaveBackground()`, `TryEnterBackground()`

Desktop helpers:
- `SetupWithClassicDesktopLifetime(...)`
- `StartWithClassicDesktopLifetime(...)`

Use:
- Desktop: set `MainWindow`.
- Browser/mobile/single-view targets: set `MainView`.
- For activation/deactivation hooks, use `Application.Current?.TryGetFeature<IActivatableLifetime>()`.

## 2) XAML Loading and Binding

### XAML loader APIs

`AvaloniaXamlLoader` (`src/Markup/Avalonia.Markup.Xaml/AvaloniaXamlLoader.cs`):
- `Load(object)`
- `Load(IServiceProvider?, object)`
- `Load(Uri, Uri?)`
- `Load(IServiceProvider?, Uri, Uri?)`

`AvaloniaRuntimeXamlLoader` (`src/Markup/Avalonia.Markup.Xaml.Loader/AvaloniaRuntimeXamlLoader.cs`):
- `Load(string ...)`
- `Load(Stream ...)`
- `Load(RuntimeXamlLoaderDocument ...)`

Use:
- Standard app path: precompiled XAML via generated `InitializeComponent`.
- Runtime XAML loader only for explicit dynamic/plugin scenarios.

AOT/trimming notes:
- URI-based `AvaloniaXamlLoader.Load(...)` and runtime loaders are annotated for trim risk.

### Binding API families

Compiled path (preferred):
- `CompiledBinding`
- `CompiledBindingExtension`
- `CompiledBindingPath` / `CompiledBindingPathBuilder`

Reflection path (fallback):
- `ReflectionBinding`
- `ReflectionBindingExtension`
- `Markup Binding` (`Avalonia.Markup.Data.Binding`) inherits reflection binding

Core binding controls:
- `BindingMode`
- `BindingPriority`
- `UpdateSourceTrigger`
- `MultiBinding`
- `BindingOperations.DoNothing`

Compiled path builder capabilities:
- `Property(...)`
- `Method(...)`
- `Command(...)`
- `Self()`
- `Ancestor(Type, int)`
- `VisualAncestor(Type, int)`
- `ElementName(INameScope, string)`
- `TemplatedParent()`
- `StreamTask<T>()`
- `StreamObservable<T>()`

Use:
- XAML: set `x:DataType` and use `{CompiledBinding ...}`.
- Keep reflection binding explicit (`{ReflectionBinding ...}`) when unavoidable.

## 3) Property System and Reactive Data Flow

### Property registration and value APIs

`AvaloniaProperty` / `AvaloniaProperty<T>`:
- `Register<TOwner, TValue>(...)`
- `RegisterAttached<...>(...)`
- `RegisterDirect<TOwner, TValue>(...)`

`AvaloniaObject`:
- `GetValue(...)`
- `SetValue(...)`
- `SetCurrentValue(...)`
- `ClearValue(...)`
- `Bind(AvaloniaProperty, IBinding)`
- `Bind(AvaloniaProperty, IObservable<object?>, BindingPriority)`

Use:
- `StyledProperty` for styleable/templateable values.
- `DirectProperty` for CLR-backed/readonly-like patterns.
- `SetCurrentValue` to preserve existing binding while updating value.

### Observables and bindings

`AvaloniaObjectExtensions`:
- `GetObservable(...)`
- `GetBindingObservable(...)`
- `GetPropertyChangedObservable(...)`
- `Bind(... IObservable<T> ...)`
- `ToBinding()`

Use:
- Drive UI from `IObservable<T>` and convert with `ToBinding()`.
- Observe property changes without manual event detachment complexity.

## 4) UI Thread and Scheduling

`Dispatcher` (`src/Avalonia.Base/Threading`):
- `Dispatcher.UIThread`
- `Invoke(...)`
- `InvokeAsync(...)`
- `Post(...)`
- `MainLoop(...)`
- `BeginInvokeShutdown(...)`
- `InvokeShutdown()`

Use:
- Marshal all visual tree and control property mutations to `Dispatcher.UIThread`.
- Use `Post` for fire-and-forget UI notification.
- Use `InvokeAsync` when awaiting UI completion.

## 5) Controls, Templates, and DataTemplates

Core view types:
- `TopLevel`
- `Window`
- `UserControl`
- `TemplatedControl`
- `Control`

`Window` highlights:
- `Show()` / `Show(owner)` / `ShowDialog<TResult>(owner)`
- `Close()` / `Close(object?)`
- `SizeToContent`, `CanResize`, `WindowState`, `Title`, `Icon`, `SystemDecorations`, `WindowStartupLocation`

`TopLevel` highlights:
- `StorageProvider`, `Clipboard`, `Screens`, `InsetsManager`, `Launcher`
- `RequestedThemeVariant` / `ActualThemeVariant`

Template/data template APIs:
- `DataTemplate`
- `TreeDataTemplate`
- `FuncDataTemplate`
- `DataTemplates`

Important behavior:
- `DataTemplates` collection expects typed templates (`DataType`) for robust matching in shared/global scenarios.

## 6) Styling, Themes, and Resources

Key APIs:
- `Style`
- `Styles`
- `ControlTheme`
- `Selectors` (typed selector builder in C#)
- `ThemeVariant` (`Default`, `Light`, `Dark`)
- `ThemeVariantScope`
- `ResourceDictionary` (`MergedDictionaries`, `ThemeDictionaries`, `TryGetResource`)

XAML include APIs:
- `StyleInclude`
- `ResourceInclude`
- `MergeResourceInclude`

Use:
- Prefer typed selector construction in C# (`new Style(x => x.OfType<Button>())`) for trim-safe code paths when you need runtime selector building.
- Use `ThemeDictionaries` to isolate per-theme values instead of ad-hoc runtime checks.

## 7) Input, Commands, and Routed Events

Input/command APIs:
- `ICommandSource`
- `KeyGesture`
- `KeyBinding`
- `HotkeyManager`

Routed event APIs:
- `RoutedEvent`
- `RoutedEvent<TEventArgs>`
- `RoutedEventArgs`
- `Interactive.AddHandler(...)`
- `Interactive.RemoveHandler(...)`
- `Interactive.RaiseEvent(...)`

Use:
- Centralize keyboard and command handling for testability and accessibility.
- Use routed events for cross-control behaviors where direct references are undesirable.

## 8) Platform Bootstrapping APIs

Desktop and shared:
- `UsePlatformDetect()`
- `UseSkia()`
- `WithInterFont()`
- `UseManagedSystemDialogs()`

Platform-specific entry points:
- Windows: `UseWin32()`, `Win32PlatformOptions`
- Linux/X11: `UseX11()`, `X11PlatformOptions`
- macOS native: `UseAvaloniaNative()`, `AvaloniaNativePlatformOptions`, `MacOSPlatformOptions`
- Android: `UseAndroid()`, `AndroidPlatformOptions`
- iOS: `UseiOS()`, `iOSPlatformOptions`
- Browser: `UseBrowser()`, `StartBrowserAppAsync(...)`, `SetupBrowserAppAsync(...)`, `BrowserPlatformOptions`
- Linux framebuffer: `StartLinuxFbDev(...)`, `StartLinuxDrm(...)`, `StartLinuxDirect(...)`, `LinuxFramebufferPlatformOptions`
- Headless/testing: `UseHeadless(...)`, `AvaloniaHeadlessPlatformOptions`

Use:
- Always include software fallback in rendering mode arrays for robust deployment.

## 9) Build and Tooling Surface

MSBuild properties (package/build files):
- `EnableAvaloniaXamlCompilation`
- `AvaloniaUseCompiledBindingsByDefault`
- `AvaloniaXamlVerboseExceptions`
- `AvaloniaXamlCreateSourceInfo`
- `AvaloniaXamlIlVerifyIl`
- `IsAotCompatible` (project-level/consumer context)

Item groups:
- `AvaloniaXaml`
- `AvaloniaResource`

Source generator knobs (`Avalonia.Generators.props`):
- `AvaloniaNameGeneratorBehavior`
- `AvaloniaNameGeneratorDefaultFieldModifier`
- `AvaloniaNameGeneratorFilterByPath`
- `AvaloniaNameGeneratorFilterByNamespace`
- `AvaloniaNameGeneratorViewFileNamingStrategy`

Use:
- Keep XAML compilation enabled.
- Keep compiled bindings default-on unless explicitly debugging legacy binding issues.

## 10) High-Value Best-Practice Decisions

- Prefer compiled bindings + `x:DataType` by default.
- Treat reflection binding/runtime XAML loading as explicit exceptions.
- Keep startup in `BuildAvaloniaApp()` and view assignment in `OnFrameworkInitializationCompleted()`.
- Keep all UI-thread work on `Dispatcher.UIThread`.
- Keep styles and resources strongly structured (global app styles, control themes, per-theme dictionaries).
- Keep platform options centralized through `With<TOptions>()`.

## XAML-First and Code-Only Usage

Default guidance for this skill:
- Start with XAML for view structure, templates, styles, and bindings.
- Provide code-only UI construction only when the user explicitly requests it.

XAML-first references:
- `Application` resources/styles and `x:DataType` compiled bindings
- `DataTemplate`/`ControlTheme` declarations in `.axaml`

XAML-first usage example:

```xml
<Application xmlns="https://github.com/avaloniaui"
             xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
             xmlns:vm="using:MyApp.ViewModels"
             xmlns:views="using:MyApp.Views"
             x:Class="MyApp.App">
  <Application.Styles>
    <FluentTheme />
  </Application.Styles>

  <Application.DataTemplates>
    <DataTemplate x:DataType="vm:MainViewModel">
      <views:MainView />
    </DataTemplate>
  </Application.DataTemplates>
</Application>
```

Code-only usage example (on request):

```csharp
using Avalonia;
using Avalonia.Controls;
using Avalonia.Themes.Fluent;

public static class CodeOnlyBootstrap
{
    public static void ConfigureApp(Application app)
    {
        app.Styles.Add(new FluentTheme());

        var window = new Window
        {
            Width = 640,
            Height = 360,
            DataContext = new MainWindowViewModel(),
            Content = new TextBlock
            {
                Margin = new Thickness(16),
                Text = "Hello Avalonia"
            }
        };

        window.Show();
    }
}
```
