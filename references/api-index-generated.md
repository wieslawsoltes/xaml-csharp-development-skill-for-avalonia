# Avalonia App-Building API Index (Generated)

- Generated at (UTC): `2026-02-15 10:46:45Z`
- Repository: `Avalonia@11.3.12`
- Git ref: `11.3.12`
- Files scanned: `197`
- Captured public signatures: `1190`

## Scope

This index intentionally targets app-construction APIs (startup, lifetime, XAML, binding, styling, threading, platform bootstrap, and build settings).

## Regenerate

```bash
python3 scripts/generate_api_index.py --repo <path-to-avalonia-repo> --git-ref 11.3.12 --output references/api-index-generated.md
```

## Android Platform

### `src/Android/Avalonia.Android/AndroidPlatform.cs`
- `public static class AndroidApplicationExtensions`
- `public static AppBuilder UseAndroid(this AppBuilder builder) {`
- `public enum AndroidRenderingMode`
- `public sealed class AndroidPlatformOptions`
- `public IReadOnlyList<AndroidRenderingMode> RenderingMode { get; set; } = new[]`

## Application Model and Controls

### `src/Avalonia.Controls/AppBuilder.cs`
- `public sealed class AppBuilder`
- `public Action? RuntimePlatformServicesInitializer { get; private set; }`
- `public string? RuntimePlatformServicesName { get; private set; }`
- `public Application? Instance { get; private set; }`
- `public Type? ApplicationType { get; private set; }`
- `public Action? WindowingSubsystemInitializer { get; private set; }`
- `public string? WindowingSubsystemName { get; private set; }`
- `public Action? RenderingSubsystemInitializer { get; private set; }`
- `public Func<Type, IApplicationLifetime?>? LifetimeOverride { get; private set; }`
- `public string? RenderingSubsystemName { get; private set; }`
- `public Action<AppBuilder> AfterSetupCallback { get; private set; } = builder => { };`
- `public Action<AppBuilder> AfterPlatformServicesSetupCallback { get; private set; } = builder => { };`
- `public static AppBuilder Configure<TApp>() where TApp : Application, new() {`
- `public static AppBuilder Configure<TApp>(Func<TApp> appFactory) where TApp : Application {`
- `public AppBuilder AfterSetup(Action<AppBuilder> callback) {`
- `public AppBuilder AfterApplicationSetup(Action<AppBuilder> callback) {`
- `public AppBuilder AfterPlatformServicesSetup(Action<AppBuilder> callback) {`
- `public delegate void AppMainDelegate(Application app, string[] args);`
- `public void Start(AppMainDelegate main, string[] args) {`
- `public AppBuilder SetupWithoutStarting() {`
- `public AppBuilder SetupWithLifetime(IApplicationLifetime lifetime) {`
- `public AppBuilder UseWindowingSubsystem(Action initializer, string name = "") {`
- `public AppBuilder UseRenderingSubsystem(Action initializer, string name = "") {`
- `public AppBuilder UseRuntimePlatformSubsystem(Action initializer, string name = "") {`
- `public AppBuilder UseStandardRuntimePlatformSubsystem() {`
- `public AppBuilder With<T>(T options) {`
- `public AppBuilder With<T>(Func<T> options) {`
- `public AppBuilder ConfigureFonts(Action<FontManager> action) {`

### `src/Avalonia.Controls/Application.cs`
- `public class Application : AvaloniaObject, IDataContextProvider, IGlobalDataTemplates, IGlobalStyles, IThemeVariantHost, IResourceHost2, IApplicationPlatformEvents, IOptionalFeatureProvider`
- `public static readonly StyledProperty<object?> DataContextProperty = StyledElement.DataContextProperty.AddOwner<Application>();`
- `public static readonly StyledProperty<ThemeVariant> ActualThemeVariantProperty = ThemeVariantScope.ActualThemeVariantProperty.AddOwner<Application>();`
- `public static readonly StyledProperty<ThemeVariant?> RequestedThemeVariantProperty = ThemeVariantScope.RequestedThemeVariantProperty.AddOwner<Application>();`
- `public event EventHandler<ResourcesChangedEventArgs>? ResourcesChanged;`
- `public event EventHandler<UrlOpenedEventArgs>? UrlsOpened;`
- `public event EventHandler? ActualThemeVariantChanged;`
- `public Application() {`
- `public object? DataContext {`
- `public ThemeVariant? RequestedThemeVariant {`
- `public ThemeVariant ActualThemeVariant => GetValue(ActualThemeVariantProperty);`
- `public static Application? Current {`
- `public DataTemplates DataTemplates => _dataTemplates ?? (_dataTemplates = new DataTemplates());`
- `public IResourceDictionary Resources {`
- `public Styles Styles => _styles ??= new Styles(this);`
- `public IApplicationLifetime? ApplicationLifetime {`
- `public IPlatformSettings? PlatformSettings => this.TryGetFeature<IPlatformSettings>();`
- `public virtual void Initialize() { }`
- `public bool TryGetResource(object key, ThemeVariant? theme, out object? value) {`
- `public virtual void RegisterServices() {`
- `public virtual void OnFrameworkInitializationCompleted() {`
- `public static readonly DirectProperty<Application, string?> NameProperty = AvaloniaProperty.RegisterDirect<Application, string?>("Name", o => o.Name, (o, v) => o.Name = v);`
- `public string? Name {`
- `public object? TryGetFeature(Type featureType) {`

### `src/Avalonia.Controls/ApplicationLifetimes/ActivatableLifetimeBase.cs`
- Namespace: `Avalonia.Controls.ApplicationLifetimes`
- `public abstract class ActivatableLifetimeBase : IActivatableLifetime`
- `public event EventHandler<ActivatedEventArgs>? Activated;`
- `public event EventHandler<ActivatedEventArgs>? Deactivated;`
- `public virtual bool TryLeaveBackground() => false;`
- `public virtual bool TryEnterBackground() => false;`

### `src/Avalonia.Controls/ApplicationLifetimes/ActivatedEventArgs.cs`
- Namespace: `Avalonia.Controls.ApplicationLifetimes`
- `public class ActivatedEventArgs : EventArgs`
- `public ActivatedEventArgs(ActivationKind kind) {`
- `public ActivationKind Kind { get; }`

### `src/Avalonia.Controls/ApplicationLifetimes/ActivationKind.cs`
- Namespace: `Avalonia.Controls.ApplicationLifetimes`
- `public enum ActivationKind`

### `src/Avalonia.Controls/ApplicationLifetimes/ClassicDesktopStyleApplicationLifetime.cs`
- `public class ClassicDesktopStyleApplicationLifetime : IClassicDesktopStyleApplicationLifetime, IDisposable`
- `public event EventHandler<ControlledApplicationLifetimeStartupEventArgs>? Startup;`
- `public event EventHandler<ShutdownRequestedEventArgs>? ShutdownRequested;`
- `public event EventHandler<ControlledApplicationLifetimeExitEventArgs>? Exit;`
- `public string[]? Args { get; set; }`
- `public ShutdownMode ShutdownMode { get; set; }`
- `public Window? MainWindow { get; set; }`
- `public IReadOnlyList<Window> Windows => _windows;`
- `public void Shutdown(int exitCode = 0) {`
- `public bool TryShutdown(int exitCode = 0) {`
- `public int Start(string[] args) {`
- `public int Start() {`
- `public void Dispose() {`
- `public class ClassicDesktopStyleApplicationLifetimeOptions`
- `public bool ProcessUrlActivationCommandLine { get; set; }`
- `public static class ClassicDesktopStyleApplicationLifetimeExtensions`
- `public static AppBuilder SetupWithClassicDesktopLifetime(this AppBuilder builder, string[] args, Action<IClassicDesktopStyleApplicationLifetime>? lifetimeBuilder = null) {`
- `public static int StartWithClassicDesktopLifetime( this AppBuilder builder, string[] args, Action<IClassicDesktopStyleApplicationLifetime>? lifetimeBuilder = null) {`
- `public static int StartWithClassicDesktopLifetime( this AppBuilder builder, string[] args, ShutdownMode shutdownMode) {`

### `src/Avalonia.Controls/ApplicationLifetimes/ControlledApplicationLifetimeExitEventArgs.cs`
- `public class ControlledApplicationLifetimeExitEventArgs : EventArgs`
- `public ControlledApplicationLifetimeExitEventArgs(int applicationExitCode) {`
- `public int ApplicationExitCode { get; set; }`

### `src/Avalonia.Controls/ApplicationLifetimes/FileActivatedEventArgs.cs`
- Namespace: `Avalonia.Controls.ApplicationLifetimes`
- `public sealed class FileActivatedEventArgs : ActivatedEventArgs`
- `public FileActivatedEventArgs(IReadOnlyList<IStorageItem> files) : base(ActivationKind.File) {`
- `public IReadOnlyList<IStorageItem> Files { get; }`

### `src/Avalonia.Controls/ApplicationLifetimes/IActivatableApplicationLifetime.cs`
- Namespace: `Avalonia.Controls.ApplicationLifetimes`
- `public interface IActivatableApplicationLifetime : IActivatableLifetime {`
- `public interface IActivatableLifetime`
- `public bool TryLeaveBackground();`
- `public bool TryEnterBackground();`

### `src/Avalonia.Controls/ApplicationLifetimes/IApplicationLifetime.cs`
- `public interface IApplicationLifetime`

### `src/Avalonia.Controls/ApplicationLifetimes/IClassicDesktopStyleApplicationLifetime.cs`
- `public interface IClassicDesktopStyleApplicationLifetime : IControlledApplicationLifetime`

### `src/Avalonia.Controls/ApplicationLifetimes/IControlledApplicationLifetime.cs`
- `public interface IControlledApplicationLifetime : IApplicationLifetime`

### `src/Avalonia.Controls/ApplicationLifetimes/ISingleTopLevelApplicationLifetime.cs`
- Namespace: `Avalonia.Controls.ApplicationLifetimes`
- `public interface ISingleTopLevelApplicationLifetime : IApplicationLifetime`

### `src/Avalonia.Controls/ApplicationLifetimes/ISingleViewApplicationLifetime.cs`
- `public interface ISingleViewApplicationLifetime : IApplicationLifetime`

### `src/Avalonia.Controls/ApplicationLifetimes/ProtocolActivatedEventArgs.cs`
- Namespace: `Avalonia.Controls.ApplicationLifetimes`
- `public sealed class ProtocolActivatedEventArgs : ActivatedEventArgs`
- `public ProtocolActivatedEventArgs(Uri uri) : base(ActivationKind.OpenUri) {`
- `public Uri Uri { get; }`

### `src/Avalonia.Controls/ApplicationLifetimes/ShutdownRequestedEventArgs.cs`
- `public class ShutdownRequestedEventArgs : CancelEventArgs`

### `src/Avalonia.Controls/ApplicationLifetimes/StartupEventArgs.cs`
- `public class ControlledApplicationLifetimeStartupEventArgs : EventArgs`
- `public ControlledApplicationLifetimeStartupEventArgs(IEnumerable<string> args) {`
- `public string[] Args { get; }`

### `src/Avalonia.Controls/DesktopApplicationExtensions.cs`
- `public static class DesktopApplicationExtensions`
- `public static void Run(this Application app, ICloseable closable) {`
- `public static void Run(this Application app, Window mainWindow) {`
- `public static void Run(this Application app, CancellationToken token) {`
- `public static void RunWithMainWindow<TWindow>(this Application app) where TWindow : Avalonia.Controls.Window, new() {`

### `src/Avalonia.Controls/Templates/DataTemplateExtensions.cs`
- `public static class DataTemplateExtensions`
- `public static IDataTemplate? FindDataTemplate( this Control control, object? data, IDataTemplate? primary = null) {`

### `src/Avalonia.Controls/Templates/DataTemplates.cs`
- `public class DataTemplates : AvaloniaList<IDataTemplate>, IAvaloniaListItemValidator<IDataTemplate>`
- `public DataTemplates() {`

### `src/Avalonia.Controls/Templates/FuncControlTemplate.cs`
- `public class FuncControlTemplate : FuncTemplate<TemplatedControl, Control>, IControlTemplate`
- `public FuncControlTemplate(Func<TemplatedControl, INameScope, Control> build) : base(build) {`
- `public new TemplateResult<Control> Build(TemplatedControl param) {`

### `src/Avalonia.Controls/Templates/FuncControlTemplate`2.cs`
- `public class FuncControlTemplate<T> : FuncControlTemplate where T : TemplatedControl`
- `public FuncControlTemplate(Func<T, INameScope, Control> build) : base((x, s) => build((T)x, s))`

### `src/Avalonia.Controls/Templates/FuncDataTemplate.cs`
- `public class FuncDataTemplate : FuncTemplate<object?, Control?>, IRecyclingDataTemplate`
- `public static readonly FuncDataTemplate Default = new FuncDataTemplate<object?>( (data, s) =>`
- `public static readonly FuncDataTemplate Access = new FuncDataTemplate<object>( (data, s) =>`
- `public FuncDataTemplate( Type type, Func<object?, INameScope, Control?> build, bool supportsRecycling = false) : this(o => IsInstance(o, type), build, supportsRecycling)`
- `public FuncDataTemplate( Func<object?, bool> match, Func<object?, INameScope, Control?> build, bool supportsRecycling = false) : base(build) {`
- `public bool Match(object? data) {`
- `public Control? Build(object? data, Control? existing) {`

### `src/Avalonia.Controls/Templates/FuncDataTemplate`1.cs`
- `public class FuncDataTemplate<T> : FuncDataTemplate`
- `public FuncDataTemplate(Func<T, INameScope, Control?> build, bool supportsRecycling = false) : base(o => TypeUtilities.CanCast<T>(o), CastBuild(build), supportsRecycling)`
- `public FuncDataTemplate( Func<T, bool> match, Func<T, INameScope, Control> build, bool supportsRecycling = false) : base(CastMatch(match), CastBuild(build), supportsRecycling) {`
- `public FuncDataTemplate( Func<T, bool> match, Func<T, Control> build, bool supportsRecycling = false) : this(match, (a, _) => build(a), supportsRecycling)`

### `src/Avalonia.Controls/Templates/FuncTemplateNameScopeExtensions.cs`
- `public static class FuncTemplateNameScopeExtensions`
- `public static T RegisterInNameScope<T>(this T control, INameScope scope) where T : StyledElement {`

### `src/Avalonia.Controls/Templates/FuncTemplate`1.cs`
- `public class FuncTemplate<TControl> : ITemplate<TControl> where TControl : Control?`
- `public FuncTemplate(Func<TControl> func) {`
- `public TControl Build() {`

### `src/Avalonia.Controls/Templates/FuncTemplate`2.cs`
- `public class FuncTemplate<TParam, TControl> : ITemplate<TParam, TControl>`
- `public FuncTemplate(Func<TParam, INameScope, TControl> func) {`
- `public TControl Build(TParam param) {`

### `src/Avalonia.Controls/Templates/FuncTreeDataTemplate.cs`
- `public class FuncTreeDataTemplate : FuncDataTemplate, ITreeDataTemplate`
- `public FuncTreeDataTemplate( Type type, Func<object?, INameScope, Control> build, Func<object?, IEnumerable> itemsSelector) : this(o => IsInstance(o, type), build, itemsSelector)`
- `public FuncTreeDataTemplate( Func<object?, bool> match, Func<object?, INameScope, Control?> build, Func<object?, IEnumerable> itemsSelector) : base(match, build) {`
- `public InstancedBinding ItemsSelector(object item) {`

### `src/Avalonia.Controls/Templates/FuncTreeDataTemplate`1.cs`
- `public class FuncTreeDataTemplate<T> : FuncTreeDataTemplate`
- `public FuncTreeDataTemplate( Func<T, INameScope, Control> build, Func<T, IEnumerable> itemsSelector) : base( typeof(T), Cast(build), Cast(itemsSelector)) {`
- `public FuncTreeDataTemplate( Func<T, bool> match, Func<T, INameScope, Control> build, Func<T, IEnumerable> itemsSelector) : base( CastMatch(match), Cast(build), Cast(itemsSelector)) {`

### `src/Avalonia.Controls/Templates/IControlTemplate.cs`
- `public interface IControlTemplate : ITemplate<TemplatedControl, TemplateResult<Control>?>`

### `src/Avalonia.Controls/Templates/IDataTemplate.cs`
- `public interface IDataTemplate : ITemplate<object?, Control?>`

### `src/Avalonia.Controls/Templates/IDataTemplateHost.cs`
- `public interface IDataTemplateHost`

### `src/Avalonia.Controls/Templates/IRecyclingDataTemplate.cs`
- `public interface IRecyclingDataTemplate : IDataTemplate`

### `src/Avalonia.Controls/Templates/ITemplate`1.cs`
- `public interface ITemplate<TControl> : ITemplate where TControl : Control?`

### `src/Avalonia.Controls/Templates/ITemplate`2.cs`
- `public interface ITemplate<TParam, TControl>`

### `src/Avalonia.Controls/Templates/ITreeDataTemplate.cs`
- `public interface ITreeDataTemplate : IDataTemplate`

### `src/Avalonia.Controls/Templates/ITypedDataTemplate.cs`
- Namespace: `Avalonia.Controls.Templates`
- `public interface ITypedDataTemplate : IDataTemplate`

### `src/Avalonia.Controls/Templates/TemplateExtensions.cs`
- `public static class TemplateExtensions`
- `public static IEnumerable<Control> GetTemplateChildren(this TemplatedControl control) {`

### `src/Avalonia.Controls/ThemeVariantScope.cs`
- `public class ThemeVariantScope : Decorator`
- `public static readonly StyledProperty<ThemeVariant> ActualThemeVariantProperty = ThemeVariant.ActualThemeVariantProperty.AddOwner<ThemeVariantScope>();`
- `public static readonly StyledProperty<ThemeVariant?> RequestedThemeVariantProperty = ThemeVariant.RequestedThemeVariantProperty.AddOwner<ThemeVariantScope>();`
- `public ThemeVariant? RequestedThemeVariant {`

### `src/Avalonia.Controls/TopLevel.cs`
- `public abstract class TopLevel : ContentControl,`
- `public static readonly DirectProperty<TopLevel, Size> ClientSizeProperty = AvaloniaProperty.RegisterDirect<TopLevel, Size>(nameof(ClientSize), o => o.ClientSize);`
- `public static readonly DirectProperty<TopLevel, Size?> FrameSizeProperty = AvaloniaProperty.RegisterDirect<TopLevel, Size?>(nameof(FrameSize), o => o.FrameSize);`
- `public static readonly StyledProperty<IInputElement?> PointerOverElementProperty = AvaloniaProperty.Register<TopLevel, IInputElement?>(nameof(IInputRoot.PointerOverElement));`
- `public static readonly StyledProperty<IReadOnlyList<WindowTransparencyLevel>> TransparencyLevelHintProperty = AvaloniaProperty.Register<TopLevel, IReadOnlyList<WindowTransparencyLevel>>(nameof(TransparencyLevelHint), Array.Empty<WindowTransparencyLevel>());`
- `public static readonly DirectProperty<TopLevel, WindowTransparencyLevel> ActualTransparencyLevelProperty = AvaloniaProperty.RegisterDirect<TopLevel, WindowTransparencyLevel>(nameof(ActualTransparencyLevel), o => o.ActualTransparencyLevel,`
- `public static readonly StyledProperty<IBrush> TransparencyBackgroundFallbackProperty = AvaloniaProperty.Register<TopLevel, IBrush>(nameof(TransparencyBackgroundFallback), Brushes.White);`
- `public static readonly StyledProperty<ThemeVariant> ActualThemeVariantProperty = ThemeVariantScope.ActualThemeVariantProperty.AddOwner<TopLevel>();`
- `public static readonly StyledProperty<ThemeVariant?> RequestedThemeVariantProperty = ThemeVariantScope.RequestedThemeVariantProperty.AddOwner<TopLevel>();`
- `public static readonly AttachedProperty<SolidColorBrush?> SystemBarColorProperty = AvaloniaProperty.RegisterAttached<TopLevel, Control, SolidColorBrush?>( "SystemBarColor", inherits: true);`
- `public static readonly AttachedProperty<bool> AutoSafeAreaPaddingProperty = AvaloniaProperty.RegisterAttached<TopLevel, Control, bool>( "AutoSafeAreaPadding", defaultValue: true);`
- `public static readonly RoutedEvent<RoutedEventArgs> BackRequestedEvent = RoutedEvent.Register<TopLevel, RoutedEventArgs>(nameof(BackRequested), RoutingStrategies.Bubble);`
- `public TopLevel(ITopLevelImpl impl) : this(impl, AvaloniaLocator.Current) {`
- `public TopLevel(ITopLevelImpl impl, IAvaloniaDependencyResolver? dependencyResolver) {`
- `public event EventHandler? Opened;`
- `public event EventHandler? Closed;`
- `public event EventHandler? ScalingChanged;`
- `public Size ClientSize {`
- `public Size? FrameSize {`
- `public IReadOnlyList<WindowTransparencyLevel> TransparencyLevelHint {`
- `public WindowTransparencyLevel ActualTransparencyLevel {`
- `public IBrush TransparencyBackgroundFallback {`
- `public ThemeVariant? RequestedThemeVariant {`
- `public event EventHandler<RoutedEventArgs> BackRequested {`
- `public ITopLevelImpl? PlatformImpl { get; private set; }`
- `public IPlatformHandle? TryGetPlatformHandle() => PlatformImpl?.Handle;`
- `public RendererDiagnostics RendererDiagnostics => Renderer.Diagnostics;`
- `public static void SetSystemBarColor(Control control, SolidColorBrush? color) {`
- `public static SolidColorBrush? GetSystemBarColor(Control control) {`
- `public static void SetAutoSafeAreaPadding(Control control, bool value) {`
- `public static bool GetAutoSafeAreaPadding(Control control) {`
- `public double RenderScaling => _scaling;`
- `public IStorageProvider StorageProvider => _storageProvider`
- `public IInsetsManager? InsetsManager => PlatformImpl?.TryGetFeature<IInsetsManager>();`
- `public IInputPane? InputPane => PlatformImpl?.TryGetFeature<IInputPane>();`
- `public ILauncher Launcher => PlatformImpl?.TryGetFeature<ILauncher>() ?? new NoopLauncher();`
- `public Screens? Screens => _screens ??=`
- `public IClipboard? Clipboard => PlatformImpl?.TryGetFeature<IClipboard>();`
- `public IFocusManager? FocusManager => AvaloniaLocator.Current.GetService<IFocusManager>();`
- `public IPlatformSettings? PlatformSettings => AvaloniaLocator.Current.GetService<IPlatformSettings>();`
- `public static TopLevel? GetTopLevel(Visual? visual) {`
- `public async Task<IDisposable> RequestPlatformInhibition(PlatformInhibitionType type, string reason) {`
- `public void RequestAnimationFrame(Action<TimeSpan> action) {`

### `src/Avalonia.Controls/UserControl.cs`
- `public class UserControl : ContentControl`

### `src/Avalonia.Controls/Window.cs`
- `public enum SizeToContent`
- `public enum SystemDecorations`
- `public enum WindowClosingBehavior`
- `public class Window : WindowBase, IFocusScope, ILayoutRoot`
- `public static readonly StyledProperty<SizeToContent> SizeToContentProperty = AvaloniaProperty.Register<Window, SizeToContent>(nameof(SizeToContent));`
- `public static readonly StyledProperty<bool> ExtendClientAreaToDecorationsHintProperty = AvaloniaProperty.Register<Window, bool>(nameof(ExtendClientAreaToDecorationsHint), false);`
- `public static readonly StyledProperty<ExtendClientAreaChromeHints> ExtendClientAreaChromeHintsProperty = AvaloniaProperty.Register<Window, ExtendClientAreaChromeHints>(nameof(ExtendClientAreaChromeHints), ExtendClientAreaChromeHints.Default);`
- `public static readonly StyledProperty<double> ExtendClientAreaTitleBarHeightHintProperty = AvaloniaProperty.Register<Window, double>(nameof(ExtendClientAreaTitleBarHeightHint), -1);`
- `public static readonly DirectProperty<Window, bool> IsExtendedIntoWindowDecorationsProperty = AvaloniaProperty.RegisterDirect<Window, bool>(nameof(IsExtendedIntoWindowDecorations), o => o.IsExtendedIntoWindowDecorations,`
- `public static readonly DirectProperty<Window, Thickness> WindowDecorationMarginProperty = AvaloniaProperty.RegisterDirect<Window, Thickness>(nameof(WindowDecorationMargin), o => o.WindowDecorationMargin);`
- `public static readonly DirectProperty<Window, Thickness> OffScreenMarginProperty = AvaloniaProperty.RegisterDirect<Window, Thickness>(nameof(OffScreenMargin), o => o.OffScreenMargin);`
- `public static readonly StyledProperty<SystemDecorations> SystemDecorationsProperty = AvaloniaProperty.Register<Window, SystemDecorations>(nameof(SystemDecorations), SystemDecorations.Full);`
- `public static readonly StyledProperty<bool> ShowActivatedProperty = AvaloniaProperty.Register<Window, bool>(nameof(ShowActivated), true);`
- `public static readonly StyledProperty<bool> ShowInTaskbarProperty = AvaloniaProperty.Register<Window, bool>(nameof(ShowInTaskbar), true);`
- `public static readonly StyledProperty<WindowClosingBehavior> ClosingBehaviorProperty = AvaloniaProperty.Register<Window, WindowClosingBehavior>(nameof(ClosingBehavior));`
- `public static readonly StyledProperty<WindowState> WindowStateProperty = AvaloniaProperty.Register<Window, WindowState>(nameof(WindowState));`
- `public static readonly StyledProperty<string?> TitleProperty = AvaloniaProperty.Register<Window, string?>(nameof(Title), "Window");`
- `public static readonly StyledProperty<WindowIcon?> IconProperty = AvaloniaProperty.Register<Window, WindowIcon?>(nameof(Icon));`
- `public static readonly StyledProperty<WindowStartupLocation> WindowStartupLocationProperty = AvaloniaProperty.Register<Window, WindowStartupLocation>(nameof(WindowStartupLocation));`
- `public static readonly StyledProperty<bool> CanResizeProperty = AvaloniaProperty.Register<Window, bool>(nameof(CanResize), true);`
- `public static readonly StyledProperty<bool> CanMinimizeProperty = AvaloniaProperty.Register<Window, bool>(nameof(CanMinimize), true);`
- `public static readonly StyledProperty<bool> CanMaximizeProperty = AvaloniaProperty.Register<Window, bool>(nameof(CanMaximize), true, coerce: CoerceCanMaximize);`
- `public static readonly RoutedEvent<RoutedEventArgs> WindowClosedEvent = RoutedEvent.Register<Window, RoutedEventArgs>("WindowClosed", RoutingStrategies.Direct);`
- `public static readonly RoutedEvent<RoutedEventArgs> WindowOpenedEvent = RoutedEvent.Register<Window, RoutedEventArgs>("WindowOpened", RoutingStrategies.Direct);`
- `public Window() : this(PlatformManager.CreateWindow()) {`
- `public Window(IWindowImpl impl) : base(impl) {`
- `public new IWindowImpl? PlatformImpl => (IWindowImpl?)base.PlatformImpl;`
- `public IReadOnlyList<Window> OwnedWindows => _children.Select(x => x.child).ToArray();`
- `public SizeToContent SizeToContent {`
- `public string? Title {`
- `public bool ExtendClientAreaToDecorationsHint {`
- `public ExtendClientAreaChromeHints ExtendClientAreaChromeHints {`
- `public double ExtendClientAreaTitleBarHeightHint {`
- `public bool IsExtendedIntoWindowDecorations {`
- `public Thickness WindowDecorationMargin {`
- `public Thickness OffScreenMargin {`
- `public SystemDecorations SystemDecorations {`
- `public bool ShowActivated {`
- `public bool ShowInTaskbar {`
- `public WindowClosingBehavior ClosingBehavior {`
- `public WindowState WindowState {`
- `public bool CanResize {`
- `public bool CanMinimize {`
- `public bool CanMaximize {`
- `public WindowIcon? Icon {`
- `public WindowStartupLocation WindowStartupLocation {`
- `public PixelPoint Position {`
- `public bool IsDialog => _showingAsDialog;`
- `public void BeginMoveDrag(PointerPressedEventArgs e) => PlatformImpl?.BeginMoveDrag(e);`
- `public void BeginResizeDrag(WindowEdge edge, PointerPressedEventArgs e) => PlatformImpl?.BeginResizeDrag(edge, e);`
- `public event EventHandler<WindowClosingEventArgs>? Closing;`
- `public void Close() {`
- `public void Close(object? dialogResult) {`
- `public override void Hide() {`
- `public override void Show() {`
- `public void Show(Window owner) {`
- `public Task ShowDialog(Window owner) {`
- `public Task<TResult> ShowDialog<TResult>(Window owner) => ShowCore<TResult>(owner, true)!;`
- `public static void SortWindowsByZOrder(Window[] windows) {`

### `src/Avalonia.Controls/WindowBase.cs`
- `public class WindowBase : TopLevel`
- `public static readonly DirectProperty<WindowBase, bool> IsActiveProperty = AvaloniaProperty.RegisterDirect<WindowBase, bool>(nameof(IsActive), o => o.IsActive);`
- `public static readonly DirectProperty<WindowBase, WindowBase?> OwnerProperty = AvaloniaProperty.RegisterDirect<WindowBase, WindowBase?>(nameof(Owner), o => o.Owner);`
- `public static readonly StyledProperty<bool> TopmostProperty = AvaloniaProperty.Register<WindowBase, bool>(nameof(Topmost));`
- `public WindowBase(IWindowBaseImpl impl) : this(impl, AvaloniaLocator.Current) {`
- `public WindowBase(IWindowBaseImpl impl, IAvaloniaDependencyResolver? dependencyResolver) : base(impl, dependencyResolver) {`
- `public event EventHandler? Activated;`
- `public event EventHandler? Deactivated;`
- `public event EventHandler<PixelPointEventArgs>? PositionChanged;`
- `public event EventHandler<WindowResizedEventArgs>? Resized;`
- `public new IWindowBaseImpl? PlatformImpl => (IWindowBaseImpl?) base.PlatformImpl;`
- `public bool IsActive {`
- `public new Screens Screens => base.Screens`
- `public WindowBase? Owner {`
- `public bool Topmost {`
- `public double DesktopScaling => DesktopScalingOverride ?? PlatformImpl?.DesktopScaling ?? 1;`
- `public void Activate() {`
- `public virtual void Hide() {`
- `public virtual void Show() {`

### `src/Avalonia.Controls/WindowClosingEventArgs.cs`
- `public enum WindowCloseReason`
- `public class WindowClosingEventArgs : CancelEventArgs`
- `public WindowCloseReason CloseReason { get; }`
- `public bool IsProgrammatic { get; }`

### `src/Avalonia.Controls/WindowEdge.cs`
- `public enum WindowEdge`

### `src/Avalonia.Controls/WindowIcon.cs`
- `public class WindowIcon`
- `public WindowIcon(Bitmap bitmap) {`
- `public WindowIcon(string fileName) {`
- `public WindowIcon(Stream stream) {`
- `public void Save(Stream stream) => PlatformImpl.Save(stream);`

### `src/Avalonia.Controls/WindowResizedEventArgs.cs`
- `public enum WindowResizeReason`
- `public class WindowResizedEventArgs : EventArgs`
- `public Size ClientSize { get; }`
- `public WindowResizeReason Reason { get; }`

### `src/Avalonia.Controls/WindowStartupLocation.cs`
- `public enum WindowStartupLocation`

### `src/Avalonia.Controls/WindowState.cs`
- `public enum WindowState`

### `src/Avalonia.Controls/WindowTransparencyLevel.cs`
- Namespace: `Avalonia.Controls`
- `public readonly record struct WindowTransparencyLevel`
- `public static WindowTransparencyLevel None { get; } = new(nameof(None));`
- `public static WindowTransparencyLevel Transparent { get; } = new(nameof(Transparent));`
- `public static WindowTransparencyLevel Blur { get; } = new(nameof(Blur));`
- `public static WindowTransparencyLevel AcrylicBlur { get; } = new(nameof(AcrylicBlur));`
- `public static WindowTransparencyLevel Mica { get; } = new(nameof(Mica));`
- `public override string ToString() {`
- `public class WindowTransparencyLevelCollection : ReadOnlyCollection<WindowTransparencyLevel>`
- `public WindowTransparencyLevelCollection(IList<WindowTransparencyLevel> list) : base(list) {`

## Browser Platform

### `src/Browser/Avalonia.Browser/BrowserAppBuilder.cs`
- Namespace: `Avalonia.Browser`
- `public enum BrowserRenderingMode`
- `public record BrowserPlatformOptions`
- `public IReadOnlyList<BrowserRenderingMode> RenderingMode { get; set; } = new[]`
- `public Func<string, string>? FrameworkAssetPathResolver { get; set; }`
- `public bool RegisterAvaloniaServiceWorker { get; set; }`
- `public string? AvaloniaServiceWorkerScope { get; set; }`
- `public bool PreferFileDialogPolyfill { get; set; }`
- `public bool? PreferManagedThreadDispatcher { get; set; } = true;`
- `public static class BrowserAppBuilder`
- `public static async Task StartBrowserAppAsync( this AppBuilder builder, string mainDivId, BrowserPlatformOptions? options = null) {`
- `public static async Task SetupBrowserAppAsync(this AppBuilder builder, BrowserPlatformOptions? options = null) {`
- `public static AppBuilder UseBrowser( this AppBuilder builder) {`

## Desktop Bootstrap

### `src/Avalonia.Desktop/AppBuilderDesktopExtensions.cs`
- `public static class AppBuilderDesktopExtensions`
- `public static AppBuilder UsePlatformDetect(this AppBuilder builder) {`

## Headless Platform

### `src/Headless/Avalonia.Headless/AvaloniaHeadlessPlatform.cs`
- `public static class AvaloniaHeadlessPlatform`
- `public static void ForceRenderTimerTick(int count = 1) {`
- `public class AvaloniaHeadlessPlatformOptions`
- `public bool UseHeadlessDrawing { get; set; } = true;`
- `public PixelFormat FrameBufferFormat { get; set; } = PixelFormat.Rgba8888;`
- `public static class AvaloniaHeadlessPlatformExtensions`
- `public static AppBuilder UseHeadless(this AppBuilder builder, AvaloniaHeadlessPlatformOptions opts) {`

## Linux Framebuffer

### `src/Linux/Avalonia.LinuxFramebuffer/LinuxFramebufferPlatform.cs`
- `public static class LinuxFramebufferPlatformExtensions`
- `public static int StartLinuxFbDev(this AppBuilder builder, string[] args, string? fbdev = null, double scaling = 1, IInputBackend? inputBackend = default) => StartLinuxDirect(builder, args, new FbdevOutput(fileName: fbdev, format: null) { Scaling = scaling }, inputBackend);`
- `public static int StartLinuxFbDev(this AppBuilder builder, string[] args, string fbdev, PixelFormat? format, double scaling, IInputBackend? inputBackend = default) => StartLinuxDirect(builder, args, new FbdevOutput(fileName: fbdev, format: format) { Scaling = scaling }, inputBackend);`
- `public static int StartLinuxFbDev(this AppBuilder builder, string[] args, FbDevOutputOptions options, IInputBackend? inputBackend = default) => StartLinuxDirect(builder, args, new FbdevOutput(options), inputBackend);`
- `public static int StartLinuxDrm(this AppBuilder builder, string[] args, string? card = null, double scaling = 1, IInputBackend? inputBackend = default) => StartLinuxDirect(builder, args, new DrmOutput(card) { Scaling = scaling }, inputBackend);`
- `public static int StartLinuxDrm(this AppBuilder builder, string[] args, string? card = null, bool connectorsForceProbe = false, DrmOutputOptions? options = null, IInputBackend? inputBackend = default) => StartLinuxDirect(builder, args, new DrmOutput(card, connectorsForceProbe, options), inputBackend);`
- `public static int StartLinuxDirect(this AppBuilder builder, string[] args, IOutputBackend outputBackend, IInputBackend? inputBackend = default) {`

### `src/Linux/Avalonia.LinuxFramebuffer/LinuxFramebufferPlatformOptions.cs`
- `public class LinuxFramebufferPlatformOptions`
- `public int Fps { get; set; } = 60;`
- `public bool ShouldRenderOnUIThread { get; set; }`

## Linux/X11 Platform

### `src/Avalonia.X11/X11Platform.cs`
- `public enum X11RenderingMode`
- `public class X11PlatformOptions`
- `public IReadOnlyList<X11RenderingMode> RenderingMode { get; set; } = new[]`
- `public bool OverlayPopups { get; set; }`
- `public bool UseDBusMenu { get; set; } = true;`
- `public bool UseDBusFilePicker { get; set; } = true;`
- `public bool? EnableIme { get; set; } = true;`
- `public bool EnableInputFocusProxy { get; set; }`
- `public bool EnableSessionManagement { get; set; } =`
- `public bool ShouldRenderOnUIThread { get; set; }`
- `public IList<GlVersion> GlProfiles { get; set; } = new List<GlVersion>`
- `public IList<string> GlxRendererBlacklist { get; set; } = new List<string>`
- `public string? WmClass { get; set; }`
- `public bool? EnableMultiTouch { get; set; } = true;`
- `public bool? UseRetainedFramebuffer { get; set; }`
- `public bool UseGLibMainLoop { get; set; }`
- `public Action<Exception>? ExterinalGLibMainLoopExceptionLogger { get; set; }`
- `public X11PlatformOptions() {`
- `public static class AvaloniaX11PlatformExtensions`
- `public static AppBuilder UseX11(this AppBuilder builder) {`
- `public static void InitializeX11Platform(X11PlatformOptions? options = null) =>`

## Other

### `src/Avalonia.Dialogs/ManagedFileDialogExtensions.cs`
- `public static class ManagedFileDialogExtensions`
- `public static AppBuilder UseManagedSystemDialogs(this AppBuilder builder) {`
- `public static AppBuilder UseManagedSystemDialogs<TWindow>(this AppBuilder builder) where TWindow : Window, new() {`
- `public static Task<string[]> ShowManagedAsync(this OpenFileDialog dialog, Window parent, ManagedFileDialogOptions? options = null) => ShowManagedAsync<Window>(dialog, parent, options);`
- `public static async Task<string[]> ShowManagedAsync<TWindow>(this OpenFileDialog dialog, Window parent, ManagedFileDialogOptions? options = null) where TWindow : Window, new() {`

## Property, Data, Styling, Threading

### `src/Avalonia.Base/AttachedProperty.cs`
- `public sealed class AttachedProperty<TValue> : StyledProperty<TValue>`
- `public new AttachedProperty<TValue> AddOwner<TOwner>(StyledPropertyMetadata<TValue>? metadata = null) where TOwner : AvaloniaObject {`

### `src/Avalonia.Base/AvaloniaObject.cs`
- `public class AvaloniaObject : IAvaloniaObjectDebug, INotifyPropertyChanged`
- `public AvaloniaObject() {`
- `public event EventHandler<AvaloniaPropertyChangedEventArgs>? PropertyChanged {`
- `public object? this[AvaloniaProperty property] {`
- `public IBinding this[IndexerDescriptor binding] {`
- `public bool CheckAccess() => Dispatcher.UIThread.CheckAccess();`
- `public void VerifyAccess() => Dispatcher.UIThread.VerifyAccess();`
- `public void ClearValue(AvaloniaProperty property) {`
- `public void ClearValue<T>(AvaloniaProperty<T> property) {`
- `public void ClearValue<T>(StyledProperty<T> property) {`
- `public void ClearValue<T>(DirectPropertyBase<T> property) {`
- `public sealed override bool Equals(object? obj) => base.Equals(obj);`
- `public sealed override int GetHashCode() => base.GetHashCode();`
- `public object? GetValue(AvaloniaProperty property) {`
- `public T GetValue<T>(StyledProperty<T> property) {`
- `public T GetValue<T>(DirectPropertyBase<T> property) {`
- `public Optional<T> GetBaseValue<T>(StyledProperty<T> property) {`
- `public bool IsAnimating(AvaloniaProperty property) {`
- `public bool IsSet(AvaloniaProperty property) {`
- `public IDisposable? SetValue( AvaloniaProperty property, object? value, BindingPriority priority = BindingPriority.LocalValue) {`
- `public IDisposable? SetValue<T>( StyledProperty<T> property, T value, BindingPriority priority = BindingPriority.LocalValue) {`
- `public void SetValue<T>(DirectPropertyBase<T> property, T value) {`
- `public void SetCurrentValue(AvaloniaProperty property, object? value) =>`
- `public void SetCurrentValue<T>(StyledProperty<T> property, T value) {`
- `public BindingExpressionBase Bind(AvaloniaProperty property, IBinding binding) {`
- `public IDisposable Bind( AvaloniaProperty property, IObservable<object?> source, BindingPriority priority = BindingPriority.LocalValue) => property.RouteBind(this, source, priority);`
- `public IDisposable Bind<T>( StyledProperty<T> property, IObservable<object?> source, BindingPriority priority = BindingPriority.LocalValue) {`
- `public IDisposable Bind<T>( StyledProperty<T> property, IObservable<T> source, BindingPriority priority = BindingPriority.LocalValue) {`
- `public IDisposable Bind<T>( StyledProperty<T> property, IObservable<BindingValue<T>> source, BindingPriority priority = BindingPriority.LocalValue) {`
- `public IDisposable Bind<T>( DirectPropertyBase<T> property, IObservable<object?> source) {`
- `public IDisposable Bind<T>( DirectPropertyBase<T> property, IObservable<T> source) {`
- `public IDisposable Bind<T>( DirectPropertyBase<T> property, IObservable<BindingValue<T>> source) {`
- `public void CoerceValue(AvaloniaProperty property) => _values.CoerceValue(property);`

### `src/Avalonia.Base/AvaloniaObjectExtensions.cs`
- `public static class AvaloniaObjectExtensions`
- `public static IBinding ToBinding<T>(this IObservable<T> source) {`
- `public static IObservable<object?> GetObservable(this AvaloniaObject o, AvaloniaProperty property) {`
- `public static IObservable<T> GetObservable<T>(this AvaloniaObject o, AvaloniaProperty<T> property) {`
- `public static IObservable<TResult> GetObservable<TSource, TResult>(this AvaloniaObject o, AvaloniaProperty<TSource> property, Func<TSource, TResult> converter) {`
- `public static IObservable<TResult> GetObservable<TResult>(this AvaloniaObject o, AvaloniaProperty property, Func<object?, TResult> converter) {`
- `public static IObservable<BindingValue<object?>> GetBindingObservable( this AvaloniaObject o, AvaloniaProperty property) {`
- `public static IObservable<BindingValue<TResult>> GetBindingObservable<TResult>(this AvaloniaObject o, AvaloniaProperty property, Func<object?, TResult> converter) {`
- `public static IObservable<BindingValue<T>> GetBindingObservable<T>( this AvaloniaObject o, AvaloniaProperty<T> property) {`
- `public static IObservable<BindingValue<TResult>> GetBindingObservable<TSource, TResult>( this AvaloniaObject o, AvaloniaProperty<TSource> property, Func<TSource, TResult> converter) {`
- `public static IObservable<AvaloniaPropertyChangedEventArgs> GetPropertyChangedObservable( this AvaloniaObject o, AvaloniaProperty property) {`
- `public static IDisposable Bind<T>( this AvaloniaObject target, AvaloniaProperty<T> property, IObservable<BindingValue<T>> source, BindingPriority priority = BindingPriority.LocalValue) {`
- `public static IDisposable Bind<T>( this AvaloniaObject target, AvaloniaProperty<T> property, IObservable<T> source, BindingPriority priority = BindingPriority.LocalValue) {`
- `public static IDisposable Bind( this AvaloniaObject target, AvaloniaProperty property, IBinding binding, object? anchor = null) {`
- `public static T GetValue<T>(this AvaloniaObject target, AvaloniaProperty<T> property) {`
- `public static object? GetBaseValue( this AvaloniaObject target, AvaloniaProperty property) {`
- `public static Optional<T> GetBaseValue<T>( this AvaloniaObject target, AvaloniaProperty<T> property) {`
- `public static IDisposable AddClassHandler<TTarget>( this IObservable<AvaloniaPropertyChangedEventArgs> observable, Action<TTarget, AvaloniaPropertyChangedEventArgs> action) where TTarget : AvaloniaObject {`
- `public static IDisposable AddClassHandler<TTarget, TValue>( this IObservable<AvaloniaPropertyChangedEventArgs<TValue>> observable, Action<TTarget, AvaloniaPropertyChangedEventArgs<TValue>> action) where TTarget : AvaloniaObject {`

### `src/Avalonia.Base/AvaloniaProperty.cs`
- `public abstract class AvaloniaProperty : IEquatable<AvaloniaProperty>, IPropertyInfo`
- `public static readonly object UnsetValue = new UnsetValueType();`
- `public string Name { get; }`
- `public Type PropertyType { get; }`
- `public Type OwnerType { get; }`
- `public bool Inherits { get; private protected set; }`
- `public bool IsAttached { get; private protected set; }`
- `public bool IsDirect { get; private protected set; }`
- `public bool IsReadOnly { get; private protected set; }`
- `public IObservable<AvaloniaPropertyChangedEventArgs> Changed => GetChanged();`
- `public static IndexerDescriptor operator !(AvaloniaProperty property) {`
- `public static IndexerDescriptor operator ~(AvaloniaProperty property) {`
- `public static bool operator ==(AvaloniaProperty? a, AvaloniaProperty? b) {`
- `public static bool operator !=(AvaloniaProperty? a, AvaloniaProperty? b) {`
- `public void Unregister(Type type) {`
- `public static StyledProperty<TValue> Register<TOwner, TValue>( string name, TValue defaultValue = default!, bool inherits = false, BindingMode defaultBindingMode = BindingMode.OneWay, Func<TValue, bool>? validate = null, Func<AvaloniaObject, TValue, TValue>? coerce = null, bool enableDataValidation = false) where TOwner : AvaloniaObject {`
- `public static AttachedProperty<TValue> RegisterAttached<TOwner, THost, TValue>( string name, TValue defaultValue = default!, bool inherits = false, BindingMode defaultBindingMode = BindingMode.OneWay, Func<TValue, bool>? validate = null, Func<AvaloniaObject, TValue, TValue>? coerce = null) where THost : AvaloniaObject {`
- `public static AttachedProperty<TValue> RegisterAttached<THost, TValue>( string name, Type ownerType, TValue defaultValue = default!, bool inherits = false, BindingMode defaultBindingMode = BindingMode.OneWay, Func<TValue, bool>? validate = null, Func<AvaloniaObject, TValue, TValue>? coerce = null) where THost : AvaloniaObject {`
- `public static DirectProperty<TOwner, TValue> RegisterDirect<TOwner, TValue>( string name, Func<TOwner, TValue> getter, Action<TOwner, TValue>? setter = null, TValue unsetValue = default!, BindingMode defaultBindingMode = BindingMode.OneWay, bool enableDataValidation = false) where TOwner : AvaloniaObject {`
- `public IndexerDescriptor Bind() {`
- `public override bool Equals(object? obj) {`
- `public bool Equals(AvaloniaProperty? other) {`
- `public override int GetHashCode() {`
- `public AvaloniaPropertyMetadata GetMetadata<T>() where T : AvaloniaObject => GetMetadata(typeof(T));`
- `public AvaloniaPropertyMetadata GetMetadata(Type type) {`
- `public AvaloniaPropertyMetadata GetMetadata(AvaloniaObject owner) {`
- `public bool IsValidValue(object? value) {`
- `public override string ToString() {`
- `public sealed class UnsetValueType`
- `public override string ToString() => "(unset)";`

### `src/Avalonia.Base/AvaloniaPropertyChangedEventArgs.cs`
- `public abstract class AvaloniaPropertyChangedEventArgs : EventArgs`
- `public AvaloniaPropertyChangedEventArgs( AvaloniaObject sender, BindingPriority priority) {`
- `public AvaloniaObject Sender { get; private set; }`
- `public AvaloniaProperty Property => GetProperty();`
- `public object? OldValue => GetOldValue();`
- `public object? NewValue => GetNewValue();`
- `public BindingPriority Priority { get; private set; }`

### `src/Avalonia.Base/AvaloniaPropertyChangedEventArgs`1.cs`
- `public class AvaloniaPropertyChangedEventArgs<T> : AvaloniaPropertyChangedEventArgs`
- `public AvaloniaPropertyChangedEventArgs( AvaloniaObject sender, AvaloniaProperty<T> property, Optional<T> oldValue, BindingValue<T> newValue, BindingPriority priority) : this(sender, property, oldValue, newValue, priority, true) {`
- `public new AvaloniaProperty<T> Property { get; }`
- `public new Optional<T> OldValue { get; private set; }`
- `public new BindingValue<T> NewValue { get; private set; }`

### `src/Avalonia.Base/AvaloniaPropertyChangedExtensions.cs`
- `public static class AvaloniaPropertyChangedExtensions`
- `public static T GetOldValue<T>(this AvaloniaPropertyChangedEventArgs e) {`
- `public static T GetNewValue<T>(this AvaloniaPropertyChangedEventArgs e) {`
- `public static (T oldValue, T newValue) GetOldAndNewValue<T>(this AvaloniaPropertyChangedEventArgs e) {`

### `src/Avalonia.Base/AvaloniaPropertyMetadata.cs`
- `public abstract class AvaloniaPropertyMetadata`
- `public AvaloniaPropertyMetadata( BindingMode defaultBindingMode = BindingMode.Default, bool? enableDataValidation = null) {`
- `public BindingMode DefaultBindingMode {`
- `public bool? EnableDataValidation { get; private set; }`
- `public bool IsReadOnly { get; private set; }`
- `public virtual void Merge( AvaloniaPropertyMetadata baseMetadata, AvaloniaProperty property) {`
- `public void Freeze() => IsReadOnly = true;`
- `public abstract AvaloniaPropertyMetadata GenerateTypeSafeMetadata();`

### `src/Avalonia.Base/AvaloniaPropertyRegistry.cs`
- `public class AvaloniaPropertyRegistry`
- `public static AvaloniaPropertyRegistry Instance { get; }`
- `public bool UnregisterByModule(IEnumerable<Type> types) {`
- `public IReadOnlyList<AvaloniaProperty> GetRegistered(Type type) {`
- `public IReadOnlyList<AvaloniaProperty> GetRegisteredAttached(Type type) {`
- `public IReadOnlyList<AvaloniaProperty> GetRegisteredDirect(Type type) {`
- `public IReadOnlyList<AvaloniaProperty> GetRegisteredInherited(Type type) {`
- `public IReadOnlyList<AvaloniaProperty> GetRegistered(AvaloniaObject o) {`
- `public DirectPropertyBase<T> GetRegisteredDirect<T>( AvaloniaObject o, DirectPropertyBase<T> property) {`
- `public AvaloniaProperty? FindRegistered(Type type, string name) {`
- `public AvaloniaProperty? FindRegistered(AvaloniaObject o, string name) {`
- `public DirectPropertyBase<T>? FindRegisteredDirect<T>( AvaloniaObject o, DirectPropertyBase<T> property) {`
- `public bool IsRegistered(Type type, AvaloniaProperty property) {`
- `public bool IsRegistered(object o, AvaloniaProperty property) {`
- `public void Register(Type type, AvaloniaProperty property) {`
- `public void RegisterAttached(Type type, AvaloniaProperty property) {`

### `src/Avalonia.Base/AvaloniaProperty`1.cs`
- `public abstract class AvaloniaProperty<TValue> : AvaloniaProperty`
- `public new IObservable<AvaloniaPropertyChangedEventArgs<TValue>> Changed => _changed;`

### `src/Avalonia.Base/Controls/ResourceDictionary.cs`
- `public class ResourceDictionary : ResourceProvider, IResourceDictionary, IThemeVariantProvider`
- `public ResourceDictionary() { }`
- `public ResourceDictionary(IResourceHost owner) : base(owner) { }`
- `public int Count => _inner?.Count ?? 0;`
- `public object? this[object key] {`
- `public ICollection<object> Keys => (ICollection<object>?)_inner?.Keys ?? Array.Empty<object>();`
- `public ICollection<object?> Values => (ICollection<object?>?)_inner?.Values ?? Array.Empty<object?>();`
- `public IList<IResourceProvider> MergedDictionaries {`
- `public IDictionary<ThemeVariant, IThemeVariantProvider> ThemeDictionaries {`
- `public sealed override bool HasResources {`
- `public void Add(object key, object? value) {`
- `public void AddDeferred(object key, Func<IServiceProvider?, object?> factory) => Add(key, new DeferredItem(factory));`
- `public void AddDeferred(object key, IDeferredContent deferredContent) => Add(key, deferredContent);`
- `public void AddNotSharedDeferred(object key, IDeferredContent deferredContent) => Add(key, new NotSharedDeferredItem(deferredContent));`
- `public void SetItems(IEnumerable<KeyValuePair<object, object?>> values) {`
- `public void Clear() {`
- `public bool ContainsKey(object key) => _inner?.ContainsKey(key) ?? false;`
- `public bool Remove(object key) {`
- `public sealed override bool TryGetResource(object key, ThemeVariant? theme, out object? value) {`
- `public bool TryGetValue(object key, out object? value) {`
- `public void EnsureCapacity(int capacity) {`
- `public IEnumerator<KeyValuePair<object, object?>> GetEnumerator() {`

### `src/Avalonia.Base/Data/AssignBindingAttribute.cs`
- `public sealed class AssignBindingAttribute : Attribute`

### `src/Avalonia.Base/Data/BindingChainException.cs`
- `public class BindingChainException : Exception`
- `public BindingChainException() {`
- `public BindingChainException(string message) {`
- `public BindingChainException(string message, string expression, string errorPoint) {`
- `public string? Expression { get; protected set; }`
- `public string? ExpressionErrorPoint { get; protected set; }`
- `public override string Message {`

### `src/Avalonia.Base/Data/BindingExpressionBase.cs`
- Namespace: `Avalonia.Data`
- `public abstract class BindingExpressionBase : IDisposable, ISetterInstance`
- `public virtual void Dispose() {`
- `public virtual void UpdateSource() { }`
- `public virtual void UpdateTarget() { }`

### `src/Avalonia.Base/Data/BindingMode.cs`
- `public enum BindingMode`

### `src/Avalonia.Base/Data/BindingNotification.cs`
- `public enum BindingErrorType`
- `public class BindingNotification`
- `public static readonly BindingNotification Null = new BindingNotification(null);`
- `public static readonly BindingNotification UnsetValue = new BindingNotification(AvaloniaProperty.UnsetValue);`
- `public BindingNotification(object? value) {`
- `public BindingNotification(Exception error, BindingErrorType errorType) {`
- `public BindingNotification(Exception error, BindingErrorType errorType, object? fallbackValue) : this(error, errorType) {`
- `public object? Value => _value;`
- `public bool HasValue => _value != AvaloniaProperty.UnsetValue;`
- `public Exception? Error { get; set; }`
- `public BindingErrorType ErrorType { get; set; }`
- `public static bool operator ==(BindingNotification? a, BindingNotification? b) {`
- `public static bool operator !=(BindingNotification? a, BindingNotification? b) {`
- `public static object? ExtractValue(object? o) {`
- `public static object? UpdateValue(object? o, object value) {`
- `public static object? ExtractError(object? o) {`
- `public override bool Equals(object? obj) {`
- `public bool Equals(BindingNotification? other) {`
- `public override int GetHashCode() {`
- `public void AddError(Exception e, BindingErrorType type) {`
- `public void ClearValue() {`
- `public void SetValue(object? value) {`
- `public override string ToString() {`

### `src/Avalonia.Base/Data/BindingOperations.cs`
- `public static class BindingOperations`
- `public static readonly object DoNothing = new DoNothingType();`
- `public static IDisposable Apply( AvaloniaObject target, AvaloniaProperty property, InstancedBinding binding) {`
- `public static IDisposable Apply( AvaloniaObject target, AvaloniaProperty property, InstancedBinding binding, object? anchor) {`
- `public static BindingExpressionBase? GetBindingExpressionBase(AvaloniaObject target, AvaloniaProperty property) {`
- `public sealed class DoNothingType`
- `public override string ToString() => "(do nothing)";`

### `src/Avalonia.Base/Data/BindingPriority.cs`
- `public enum BindingPriority`

### `src/Avalonia.Base/Data/BindingValue.cs`
- `public enum BindingValueType`
- `public readonly record struct BindingValue<T>`
- `public BindingValue(T value) {`
- `public bool HasError => Type.HasAllFlags(BindingValueType.HasError);`
- `public bool HasValue => Type.HasAllFlags(BindingValueType.HasValue);`
- `public BindingValueType Type { get; }`
- `public T Value => HasValue ? _value! : throw new InvalidOperationException("BindingValue has no value.");`
- `public Exception? Error { get; }`
- `public Optional<T> ToOptional() => HasValue ? new Optional<T>(_value) : default;`
- `public override string ToString() => HasError ? $"Error: {Error!.Message}" : _value?.ToString() ?? "(null)";`
- `public object? ToUntyped() {`
- `public BindingValue<T> WithValue(T value) {`
- `public T? GetValueOrDefault() => HasValue ? _value : default;`
- `public T? GetValueOrDefault(T defaultValue) => HasValue ? _value : defaultValue;`
- `public TResult? GetValueOrDefault<TResult>() {`
- `public TResult? GetValueOrDefault<TResult>(TResult defaultValue) {`
- `public static BindingValue<T> FromUntyped(object? value) {`
- `public static BindingValue<T> FromUntyped(object? value, Type targetType) {`
- `public static implicit operator BindingValue<T>(T value) => new BindingValue<T>(value);`
- `public static implicit operator BindingValue<T>(Optional<T> optional) {`
- `public static BindingValue<T> Unset => new BindingValue<T>(BindingValueType.UnsetValue, default, null);`
- `public static BindingValue<T> DoNothing => new BindingValue<T>(BindingValueType.DoNothing, default, null);`
- `public static BindingValue<T> BindingError(Exception e) {`
- `public static BindingValue<T> BindingError(Exception e, T fallbackValue) {`
- `public static BindingValue<T> BindingError(Exception e, Optional<T> fallbackValue) {`
- `public static BindingValue<T> DataValidationError(Exception e) {`
- `public static BindingValue<T> DataValidationError(Exception e, T fallbackValue) {`
- `public static BindingValue<T> DataValidationError(Exception e, Optional<T> fallbackValue) {`

### `src/Avalonia.Base/Data/CultureInfoIetfLanguageTagConverter.cs`
- Namespace: `Avalonia.Data`
- `public class CultureInfoIetfLanguageTagConverter : TypeConverter`
- `public override bool CanConvertFrom(ITypeDescriptorContext? context, Type sourceType) => sourceType == typeof(string);`
- `public override object? ConvertFrom(ITypeDescriptorContext? context, CultureInfo? culture, object value) {`

### `src/Avalonia.Base/Data/DataValidationException.cs`
- `public class DataValidationException : Exception`
- `public DataValidationException(object? errorData) : base(errorData?.ToString()) {`
- `public object? ErrorData { get; }`

### `src/Avalonia.Base/Data/IBinding.cs`
- `public interface IBinding`

### `src/Avalonia.Base/Data/IndexerDescriptor.cs`
- `public class IndexerDescriptor : IObservable<object?>, IDescription`
- `public BindingMode Mode {`
- `public BindingPriority Priority {`
- `public AvaloniaProperty? Property {`
- `public AvaloniaObject? Source {`
- `public IObservable<object>? SourceObservable {`
- `public string Description => $"{Source?.GetType().Name}.{Property?.Name}";`
- `public static IndexerDescriptor operator !(IndexerDescriptor binding) {`
- `public static IndexerDescriptor operator ~(IndexerDescriptor binding) {`
- `public IndexerDescriptor WithMode(BindingMode mode) {`
- `public IndexerDescriptor WithPriority(BindingPriority priority) {`
- `public IDisposable Subscribe(IObserver<object?> observer) {`

### `src/Avalonia.Base/Data/InstancedBinding.cs`
- `public sealed class InstancedBinding`
- `public BindingMode Mode { get; }`
- `public BindingPriority Priority { get; }`
- `public IObservable<object?> Source => _observable ??= _expression!.ToObservable(_target);`
- `public IObservable<object?> Observable => Source;`
- `public static InstancedBinding OneTime( object value, BindingPriority priority = BindingPriority.LocalValue) {`
- `public static InstancedBinding OneTime( IObservable<object?> observable, BindingPriority priority = BindingPriority.LocalValue) {`
- `public static InstancedBinding OneWay( IObservable<object?> observable, BindingPriority priority = BindingPriority.LocalValue) {`
- `public static InstancedBinding OneWayToSource( IObserver<object?> observer, BindingPriority priority = BindingPriority.LocalValue) {`
- `public static InstancedBinding TwoWay( IObservable<object?> observable, IObserver<object?> observer, BindingPriority priority = BindingPriority.LocalValue) {`
- `public InstancedBinding WithPriority(BindingPriority priority) {`

### `src/Avalonia.Base/Data/Optional.cs`
- `public readonly struct Optional<T> : IEquatable<Optional<T>>`
- `public Optional(T value) {`
- `public bool HasValue { get; }`
- `public T Value => HasValue ? _value : throw new InvalidOperationException("Optional has no value.");`
- `public override bool Equals(object? obj) => obj is Optional<T> o && this == o;`
- `public bool Equals(Optional<T> other) => this == other;`
- `public override int GetHashCode() => HasValue ? _value?.GetHashCode() ?? 0 : 0;`
- `public Optional<object?> ToObject() => HasValue ? new Optional<object?>(_value) : default;`
- `public override string ToString() => HasValue ? _value?.ToString() ?? "(null)" : "(empty)";`
- `public T? GetValueOrDefault() => _value;`
- `public T? GetValueOrDefault(T defaultValue) => HasValue ? _value : defaultValue;`
- `public TResult? GetValueOrDefault<TResult>() {`
- `public TResult? GetValueOrDefault<TResult>(TResult defaultValue) {`
- `public static implicit operator Optional<T>(T value) => new Optional<T>(value);`
- `public static bool operator !=(Optional<T> x, Optional<T> y) => !(x == y);`
- `public static bool operator ==(Optional<T> x, Optional<T> y) {`
- `public static Optional<T> Empty => default;`
- `public static class OptionalExtensions`
- `public static Optional<T> Cast<T>(this Optional<object?> value) {`

### `src/Avalonia.Base/Data/TemplateBinding.Observable.cs`
- `public partial class TemplateBinding : IAvaloniaSubject<object?>`
- `public IDisposable Subscribe(IObserver<object?> observer) {`

### `src/Avalonia.Base/Data/TemplateBinding.cs`
- `public partial class TemplateBinding : UntypedBindingExpressionBase,`
- `public TemplateBinding() : base(BindingPriority.Template) {`
- `public TemplateBinding([InheritDataTypeFrom(InheritDataTypeFromScopeKind.ControlTemplate)] AvaloniaProperty property) : base(BindingPriority.Template) {`
- `public IValueConverter? Converter { get; set; }`
- `public CultureInfo? ConverterCulture { get; set; }`
- `public object? ConverterParameter { get; set; }`
- `public new BindingMode Mode {`
- `public AvaloniaProperty? Property { get; set; }`
- `public override string Description => "TemplateBinding: " + Property;`
- `public IBinding ProvideValue() => this;`
- `public InstancedBinding? Initiate( AvaloniaObject target, AvaloniaProperty? targetProperty, object? anchor = null, bool enableDataValidation = false) {`

### `src/Avalonia.Base/Data/UpdateSourceTrigger.cs`
- `public enum UpdateSourceTrigger`

### `src/Avalonia.Base/DirectProperty.cs`
- `public class DirectProperty<TOwner, TValue> : DirectPropertyBase<TValue>, IDirectPropertyAccessor`
- `public Func<TOwner, TValue> Getter { get; }`
- `public Action<TOwner, TValue>? Setter { get; }`
- `public DirectProperty<TNewOwner, TValue> AddOwner<TNewOwner>( Func<TNewOwner, TValue> getter, Action<TNewOwner, TValue>? setter = null, TValue unsetValue = default!, BindingMode defaultBindingMode = BindingMode.Default, bool enableDataValidation = false) where TNewOwner : AvaloniaObject {`

### `src/Avalonia.Base/Input/ICommandSource.cs`
- `public interface ICommandSource`

### `src/Avalonia.Base/Input/KeyBinding.cs`
- `public class KeyBinding : AvaloniaObject`
- `public static readonly StyledProperty<ICommand> CommandProperty = AvaloniaProperty.Register<KeyBinding, ICommand>(nameof(Command));`
- `public ICommand Command {`
- `public static readonly StyledProperty<object> CommandParameterProperty = AvaloniaProperty.Register<KeyBinding, object>(nameof(CommandParameter));`
- `public object CommandParameter {`
- `public static readonly StyledProperty<KeyGesture> GestureProperty = AvaloniaProperty.Register<KeyBinding, KeyGesture>(nameof(Gesture));`
- `public KeyGesture Gesture {`
- `public void TryHandle(KeyEventArgs args) {`

### `src/Avalonia.Base/Input/KeyGesture.cs`
- `public sealed class KeyGesture : IEquatable<KeyGesture>, IFormattable`
- `public KeyGesture(Key key, KeyModifiers modifiers = KeyModifiers.None) {`
- `public bool Equals(KeyGesture? other) {`
- `public override bool Equals(object? obj) {`
- `public override int GetHashCode() {`
- `public static bool operator ==(KeyGesture? left, KeyGesture? right) {`
- `public static bool operator !=(KeyGesture? left, KeyGesture? right) {`
- `public Key Key { get; }`
- `public KeyModifiers KeyModifiers { get; }`
- `public static KeyGesture Parse(string gesture) {`
- `public override string ToString() => ToString(null, null);`
- `public string ToString(string? format, IFormatProvider? formatProvider) {`
- `public bool Matches(KeyEventArgs? keyEvent) =>`

### `src/Avalonia.Base/Interactivity/CancelRoutedEventArgs.cs`
- `public class CancelRoutedEventArgs : RoutedEventArgs`
- `public CancelRoutedEventArgs() {`
- `public CancelRoutedEventArgs(RoutedEvent? routedEvent) : base(routedEvent) {`
- `public CancelRoutedEventArgs(RoutedEvent? routedEvent, object? source) : base(routedEvent, source) {`
- `public bool Cancel { get; set; } = false;`

### `src/Avalonia.Base/Interactivity/EventRoute.cs`
- `public class EventRoute : IDisposable`
- `public EventRoute(RoutedEvent e) {`
- `public bool HasHandlers => _route?.Count > 0;`
- `public void Add( Interactive target, Delegate handler, RoutingStrategies routes, bool handledEventsToo = false, Action<Delegate, object, RoutedEventArgs>? adapter = null) {`
- `public void AddClassHandler(Interactive target) {`
- `public void RaiseEvent(Interactive source, RoutedEventArgs e) {`
- `public void Dispose() {`

### `src/Avalonia.Base/Interactivity/Interactive.cs`
- `public class Interactive : Layoutable`
- `public void AddHandler( RoutedEvent routedEvent, Delegate handler, RoutingStrategies routes = RoutingStrategies.Direct | RoutingStrategies.Bubble, bool handledEventsToo = false) {`
- `public void AddHandler<TEventArgs>( RoutedEvent<TEventArgs> routedEvent, EventHandler<TEventArgs>? handler, RoutingStrategies routes = RoutingStrategies.Direct | RoutingStrategies.Bubble, bool handledEventsToo = false) where TEventArgs : RoutedEventArgs {`
- `public void RemoveHandler(RoutedEvent routedEvent, Delegate handler) {`
- `public void RemoveHandler<TEventArgs>(RoutedEvent<TEventArgs> routedEvent, EventHandler<TEventArgs>? handler) where TEventArgs : RoutedEventArgs {`
- `public void RaiseEvent(RoutedEventArgs e) {`

### `src/Avalonia.Base/Interactivity/InteractiveExtensions.cs`
- `public static class InteractiveExtensions`
- `public static IDisposable AddDisposableHandler<TEventArgs>(this Interactive o, RoutedEvent<TEventArgs> routedEvent, EventHandler<TEventArgs> handler, RoutingStrategies routes = RoutingStrategies.Direct | RoutingStrategies.Bubble, bool handledEventsToo = false) where TEventArgs : RoutedEventArgs {`
- `public static Interactive? GetInteractiveParent(this Interactive o) => o.InteractiveParent;`
- `public static IObservable<TEventArgs> GetObservable<TEventArgs>( this Interactive o, RoutedEvent<TEventArgs> routedEvent, RoutingStrategies routes = RoutingStrategies.Direct | RoutingStrategies.Bubble, bool handledEventsToo = false) where TEventArgs : RoutedEventArgs {`

### `src/Avalonia.Base/Interactivity/RoutedEvent.cs`
- `public enum RoutingStrategies`
- `public class RoutedEvent`
- `public RoutedEvent( string name, RoutingStrategies routingStrategies, Type eventArgsType, Type ownerType) {`
- `public Type EventArgsType { get; }`
- `public string Name { get; }`
- `public Type OwnerType { get; }`
- `public RoutingStrategies RoutingStrategies { get; }`
- `public bool HasRaisedSubscriptions => _raised.HasObservers;`
- `public IObservable<(object, RoutedEventArgs)> Raised => _raised;`
- `public IObservable<RoutedEventArgs> RouteFinished => _routeFinished;`
- `public static RoutedEvent<TEventArgs> Register<TOwner, TEventArgs>( string name, RoutingStrategies routingStrategy) where TEventArgs : RoutedEventArgs {`
- `public static RoutedEvent<TEventArgs> Register<TEventArgs>( string name, RoutingStrategies routingStrategy, Type ownerType) where TEventArgs : RoutedEventArgs {`
- `public IDisposable AddClassHandler( Type targetType, EventHandler<RoutedEventArgs> handler, RoutingStrategies routes = RoutingStrategies.Direct | RoutingStrategies.Bubble, bool handledEventsToo = false) {`
- `public override string ToString() {`
- `public class RoutedEvent<TEventArgs> : RoutedEvent`
- `public RoutedEvent(string name, RoutingStrategies routingStrategies, Type ownerType) : base(name, routingStrategies, typeof(TEventArgs), ownerType) {`
- `public IDisposable AddClassHandler<TTarget>( Action<TTarget, TEventArgs> handler, RoutingStrategies routes = RoutingStrategies.Direct | RoutingStrategies.Bubble, bool handledEventsToo = false) where TTarget : Interactive {`

### `src/Avalonia.Base/Interactivity/RoutedEventArgs.cs`
- `public class RoutedEventArgs : EventArgs`
- `public RoutedEventArgs() {`
- `public RoutedEventArgs(RoutedEvent? routedEvent) {`
- `public RoutedEventArgs(RoutedEvent? routedEvent, object? source) {`
- `public bool Handled { get; set; }`
- `public RoutedEvent? RoutedEvent { get; set; }`
- `public RoutingStrategies Route { get; set; }`
- `public object? Source { get; set; }`

### `src/Avalonia.Base/Interactivity/RoutedEventRegistry.cs`
- `public class RoutedEventRegistry`
- `public static RoutedEventRegistry Instance { get; }`
- `public void Register(Type type, RoutedEvent @event) {`
- `public IEnumerable<RoutedEvent> GetAllRegistered() {`
- `public IReadOnlyList<RoutedEvent> GetRegistered(Type type) {`
- `public IReadOnlyList<RoutedEvent> GetRegistered<TOwner>() {`

### `src/Avalonia.Base/StyledProperty.cs`
- `public class StyledProperty<TValue> : AvaloniaProperty<TValue>, IStyledPropertyAccessor`
- `public Func<TValue, bool>? ValidateValue { get; }`
- `public StyledProperty<TValue> AddOwner<TOwner>(StyledPropertyMetadata<TValue>? metadata = null) where TOwner : AvaloniaObject {`
- `public TValue CoerceValue(AvaloniaObject instance, TValue baseValue) {`
- `public TValue GetDefaultValue(Type type) {`
- `public TValue GetDefaultValue(AvaloniaObject owner) {`
- `public new StyledPropertyMetadata<TValue> GetMetadata(Type type) => CastMetadata(base.GetMetadata(type));`
- `public new StyledPropertyMetadata<TValue> GetMetadata(AvaloniaObject owner) => CastMetadata(base.GetMetadata(owner));`
- `public void OverrideDefaultValue<T>(TValue defaultValue) where T : AvaloniaObject {`
- `public void OverrideDefaultValue(Type type, TValue defaultValue) {`
- `public void OverrideMetadata<T>(StyledPropertyMetadata<TValue> metadata) where T : AvaloniaObject => OverrideMetadata(typeof(T), metadata);`
- `public void OverrideMetadata(Type type, StyledPropertyMetadata<TValue> metadata) {`
- `public override string ToString() {`

### `src/Avalonia.Base/Styling/Container.cs`
- `public static class Container`
- `public static readonly AttachedProperty<string?> NameProperty = AvaloniaProperty.RegisterAttached<Layoutable, string?>("Name", typeof(Container));`
- `public static readonly AttachedProperty<ContainerSizing> SizingProperty = AvaloniaProperty.RegisterAttached<Layoutable, ContainerSizing>("Sizing", typeof(Container), coerce:UpdateQueryProvider);`
- `public static string? GetName(Layoutable layoutable) {`
- `public static void SetName(Layoutable layoutable, string? name) {`
- `public static ContainerSizing GetSizing(Layoutable layoutable) {`
- `public static void SetSizing(Layoutable layoutable, ContainerSizing sizing) {`

### `src/Avalonia.Base/Styling/ContainerQuery.cs`
- `public class ContainerQuery`
- `public ContainerQuery() {`
- `public ContainerQuery(Func<StyleQuery?, StyleQuery> query, string? containerName = null) {`
- `public StyleQuery? Query {`
- `public string? Name {`
- `public override string ToString() => Query?.ToString(this) ?? "ContainerQuery";`

### `src/Avalonia.Base/Styling/ContainerSizing.cs`
- `public enum ContainerSizing`

### `src/Avalonia.Base/Styling/ControlTheme.cs`
- `public class ControlTheme : StyleBase`
- `public ControlTheme() { }`
- `public ControlTheme(Type targetType) => TargetType = targetType;`
- `public Type? TargetType { get; set; }`
- `public ControlTheme? BasedOn { get; set; }`
- `public override string ToString() => TargetType?.Name ?? "ControlTheme";`

### `src/Avalonia.Base/Styling/IGlobalStyles.cs`
- `public interface IGlobalStyles : IStyleHost`
- `public event Action<IReadOnlyList<IStyle>>? GlobalStylesAdded;`
- `public event Action<IReadOnlyList<IStyle>>? GlobalStylesRemoved;`

### `src/Avalonia.Base/Styling/ISetterInstance.cs`
- `public interface ISetterInstance`

### `src/Avalonia.Base/Styling/ISetterValue.cs`
- `public interface ISetterValue`

### `src/Avalonia.Base/Styling/IStyle.cs`
- `public interface IStyle : IResourceNode`

### `src/Avalonia.Base/Styling/IStyleHost.cs`
- `public interface IStyleHost`

### `src/Avalonia.Base/Styling/IStyleable.cs`
- `public interface IStyleable : INamed`

### `src/Avalonia.Base/Styling/ITemplate.cs`
- `public interface ITemplate`

### `src/Avalonia.Base/Styling/IThemeVariantHost.cs`
- Namespace: `Avalonia.Styling`
- `public interface IThemeVariantHost : IResourceHost`

### `src/Avalonia.Base/Styling/Selector.cs`
- `public abstract class Selector`
- `public override string ToString() => ToString(null);`
- `public abstract string ToString(Style? owner);`

### `src/Avalonia.Base/Styling/Selectors.cs`
- `public static class Selectors`
- `public static Selector Child(this Selector previous) {`
- `public static Selector Class(this Selector? previous, string name) {`
- `public static Selector Descendant(this Selector? previous) {`
- `public static Selector Is(this Selector? previous, Type type) {`
- `public static Selector Is<T>(this Selector? previous) where T : StyledElement {`
- `public static Selector Name(this Selector? previous, string name) {`
- `public static Selector Nesting(this Selector? previous) {`
- `public static Selector Not(this Selector? previous, Func<Selector?, Selector> argument) {`
- `public static Selector Not(this Selector? previous, Selector argument) {`
- `public static Selector NthChild(this Selector? previous, int step, int offset) {`
- `public static Selector NthLastChild(this Selector? previous, int step, int offset) {`
- `public static Selector OfType(this Selector? previous, Type type) {`
- `public static Selector OfType<T>(this Selector? previous) where T : StyledElement {`
- `public static Selector Or(params Selector[] selectors) {`
- `public static Selector Or(IReadOnlyList<Selector> selectors) {`
- `public static Selector PropertyEquals<T>(this Selector? previous, AvaloniaProperty<T> property, object? value) {`
- `public static Selector PropertyEquals(this Selector? previous, AvaloniaProperty property, object? value) {`
- `public static Selector Template(this Selector previous) {`

### `src/Avalonia.Base/Styling/Setter.cs`
- `public class Setter : SetterBase, IValueEntry, ISetterInstance, IAnimationSetter`
- `public Setter() {`
- `public Setter(AvaloniaProperty property, object? value) {`
- `public AvaloniaProperty? Property { get; set; }`
- `public object? Value {`
- `public override string ToString() => $"Setter: {Property} = {Value}";`

### `src/Avalonia.Base/Styling/SetterBase.cs`
- `public abstract class SetterBase`

### `src/Avalonia.Base/Styling/Style.cs`
- `public class Style : StyleBase`
- `public Style() {`
- `public Style(Func<Selector?, Selector> selector) {`
- `public Selector? Selector {`
- `public override string ToString() => Selector?.ToString(this) ?? "Style";`

### `src/Avalonia.Base/Styling/StyleBase.cs`
- `public abstract class StyleBase : AvaloniaObject, IStyle, IResourceProvider`
- `public IList<IStyle> Children => _children ??= new(this);`
- `public IResourceHost? Owner {`
- `public IStyle? Parent { get; private set; }`
- `public IResourceDictionary Resources {`
- `public IList<SetterBase> Setters => _setters ??= new();`
- `public IList<IAnimation> Animations => _animations ??= new List<IAnimation>();`
- `public void Add(SetterBase setter) => Setters.Add(setter);`
- `public void Add(IStyle style) => Children.Add(style);`
- `public event EventHandler? OwnerChanged;`
- `public bool TryGetResource(object key, ThemeVariant? themeVariant, out object? result) {`

### `src/Avalonia.Base/Styling/StyleQueries.cs`
- `public static class StyleQueries`
- `public static StyleQuery Width(this StyleQuery? previous, StyleQueryComparisonOperator @operator, double value) {`
- `public static StyleQuery Height(this StyleQuery? previous, StyleQueryComparisonOperator @operator, double value) {`
- `public static StyleQuery Or(params StyleQuery[] queries) {`
- `public static StyleQuery Or(IReadOnlyList<StyleQuery> query) {`
- `public static StyleQuery And(params StyleQuery[] queries) {`
- `public static StyleQuery And(IReadOnlyList<StyleQuery> query) {`

### `src/Avalonia.Base/Styling/StyleQuery.cs`
- `public abstract class StyleQuery`
- `public override string ToString() => ToString(null);`
- `public abstract string ToString(ContainerQuery? owner);`

### `src/Avalonia.Base/Styling/StyleQueryComparisonOperator.cs`
- `public enum StyleQueryComparisonOperator`

### `src/Avalonia.Base/Styling/Styles.cs`
- `public class Styles : AvaloniaObject,`
- `public Styles() {`
- `public Styles(IResourceHost owner) : this() {`
- `public event NotifyCollectionChangedEventHandler? CollectionChanged;`
- `public event EventHandler? OwnerChanged;`
- `public int Count => _styles.Count;`
- `public IResourceHost? Owner {`
- `public IResourceDictionary Resources {`
- `public IStyle this[int index] {`
- `public bool TryGetResource(object key, ThemeVariant? theme, out object? value) {`
- `public void AddRange(IEnumerable<IStyle> items) => _styles.AddRange(items);`
- `public void InsertRange(int index, IEnumerable<IStyle> items) => _styles.InsertRange(index, items);`
- `public void Move(int oldIndex, int newIndex) => _styles.Move(oldIndex, newIndex);`
- `public void MoveRange(int oldIndex, int count, int newIndex) => _styles.MoveRange(oldIndex, count, newIndex);`
- `public void RemoveAll(IEnumerable<IStyle> items) => _styles.RemoveAll(items);`
- `public void RemoveRange(int index, int count) => _styles.RemoveRange(index, count);`
- `public int IndexOf(IStyle item) => _styles.IndexOf(item);`
- `public void Insert(int index, IStyle item) => _styles.Insert(index, item);`
- `public void RemoveAt(int index) => _styles.RemoveAt(index);`
- `public void Add(IStyle item) => _styles.Add(item);`
- `public void Clear() => _styles.Clear();`
- `public bool Contains(IStyle item) => _styles.Contains(item);`
- `public void CopyTo(IStyle[] array, int arrayIndex) => _styles.CopyTo(array, arrayIndex);`
- `public bool Remove(IStyle item) => _styles.Remove(item);`
- `public AvaloniaList<IStyle>.Enumerator GetEnumerator() => _styles.GetEnumerator();`

### `src/Avalonia.Base/Styling/ThemeVariant.cs`
- Namespace: `Avalonia.Styling`
- `public sealed record ThemeVariant`
- `public ThemeVariant(object key, ThemeVariant? inheritVariant) {`
- `public object Key { get; }`
- `public ThemeVariant? InheritVariant { get; }`
- `public static ThemeVariant Default { get; } = new(nameof(Default));`
- `public static ThemeVariant Light { get; } = new(nameof(Light));`
- `public static ThemeVariant Dark { get; } = new(nameof(Dark));`
- `public override string ToString() {`
- `public override int GetHashCode() {`
- `public bool Equals(ThemeVariant? other) {`
- `public static explicit operator ThemeVariant(PlatformThemeVariant themeVariant) {`
- `public static explicit operator PlatformThemeVariant?(ThemeVariant themeVariant) {`

### `src/Avalonia.Base/Styling/ThemeVariantTypeConverter.cs`
- Namespace: `Avalonia.Styling`
- `public class ThemeVariantTypeConverter : TypeConverter`
- `public override bool CanConvertFrom(ITypeDescriptorContext? context, Type sourceType) {`
- `public override object ConvertFrom(ITypeDescriptorContext? context, CultureInfo? culture, object value) {`

### `src/Avalonia.Base/Threading/Dispatcher.Exceptions.cs`
- Namespace: `Avalonia.Threading`
- `public partial class Dispatcher`
- `public event DispatcherUnhandledExceptionEventHandler? UnhandledException;`
- `public event DispatcherUnhandledExceptionFilterEventHandler? UnhandledExceptionFilter {`

### `src/Avalonia.Base/Threading/Dispatcher.Invoke.cs`
- Namespace: `Avalonia.Threading`
- `public partial class Dispatcher`
- `public void Invoke(Action callback) {`
- `public void Invoke(Action callback, DispatcherPriority priority) {`
- `public void Invoke(Action callback, DispatcherPriority priority, CancellationToken cancellationToken) {`
- `public void Invoke(Action callback, DispatcherPriority priority, CancellationToken cancellationToken, TimeSpan timeout) {`
- `public TResult Invoke<TResult>(Func<TResult> callback) {`
- `public TResult Invoke<TResult>(Func<TResult> callback, DispatcherPriority priority) {`
- `public TResult Invoke<TResult>(Func<TResult> callback, DispatcherPriority priority, CancellationToken cancellationToken) {`
- `public TResult Invoke<TResult>(Func<TResult> callback, DispatcherPriority priority, CancellationToken cancellationToken, TimeSpan timeout) {`
- `public DispatcherOperation InvokeAsync(Action callback) {`
- `public DispatcherOperation InvokeAsync(Action callback, DispatcherPriority priority) {`
- `public DispatcherOperation InvokeAsync(Action callback, DispatcherPriority priority, CancellationToken cancellationToken) {`
- `public DispatcherOperation<TResult> InvokeAsync<TResult>(Func<TResult> callback) {`
- `public DispatcherOperation<TResult> InvokeAsync<TResult>(Func<TResult> callback, DispatcherPriority priority) {`
- `public DispatcherOperation<TResult> InvokeAsync<TResult>(Func<TResult> callback, DispatcherPriority priority, CancellationToken cancellationToken) {`
- `public void Post(Action action, DispatcherPriority priority = default) {`
- `public Task InvokeAsync(Func<Task> callback) => InvokeAsync(callback, DispatcherPriority.Default);`
- `public Task InvokeAsync(Func<Task> callback, DispatcherPriority priority) {`
- `public Task<TResult> InvokeAsync<TResult>(Func<Task<TResult>> action) =>`
- `public Task<TResult> InvokeAsync<TResult>(Func<Task<TResult>> action, DispatcherPriority priority) {`
- `public void Post(SendOrPostCallback action, object? arg, DispatcherPriority priority = default) {`
- `public DispatcherPriorityAwaitable AwaitWithPriority(Task task, DispatcherPriority priority) =>`
- `public DispatcherPriorityAwaitable<T> AwaitWithPriority<T>(Task<T> task, DispatcherPriority priority) =>`

### `src/Avalonia.Base/Threading/Dispatcher.MainLoop.cs`
- Namespace: `Avalonia.Threading`
- `public partial class Dispatcher`
- `public event EventHandler? ShutdownStarted;`
- `public event EventHandler? ShutdownFinished;`
- `public void PushFrame(DispatcherFrame frame) {`
- `public void MainLoop(CancellationToken cancellationToken) {`
- `public void ExitAllFrames() {`
- `public void BeginInvokeShutdown(DispatcherPriority priority) => Post(StartShutdownImpl, priority);`
- `public void InvokeShutdown() => Invoke(StartShutdownImpl, DispatcherPriority.Send);`
- `public record struct DispatcherProcessingDisabled : IDisposable`
- `public void Dispose() {`
- `public DispatcherProcessingDisabled DisableProcessing() {`

### `src/Avalonia.Base/Threading/Dispatcher.Queue.cs`
- Namespace: `Avalonia.Threading`
- `public partial class Dispatcher`
- `public void RunJobs(DispatcherPriority? priority = null) {`
- `public bool HasJobsWithPriority(DispatcherPriority priority) {`

### `src/Avalonia.Base/Threading/Dispatcher.Timers.cs`
- Namespace: `Avalonia.Threading`
- `public partial class Dispatcher`

### `src/Avalonia.Base/Threading/Dispatcher.cs`
- Namespace: `Avalonia.Threading`
- `public partial class Dispatcher : IDispatcher`
- `public static Dispatcher UIThread {`
- `public bool SupportsRunLoops => _controlledImpl != null;`
- `public bool CheckAccess() => _impl.CurrentThreadIsLoopThread;`
- `public void VerifyAccess() {`

### `src/Avalonia.Base/Threading/DispatcherEventArgs.cs`
- Namespace: `Avalonia.Threading`
- `public abstract class DispatcherEventArgs : EventArgs`
- `public Dispatcher Dispatcher { get; }`

### `src/Avalonia.Base/Threading/DispatcherFrame.cs`
- Namespace: `Avalonia.Threading`
- `public class DispatcherFrame`
- `public DispatcherFrame() : this(true) {`
- `public Dispatcher Dispatcher { get; }`
- `public DispatcherFrame(bool exitWhenRequested) : this(Dispatcher.UIThread, exitWhenRequested) {`
- `public bool Continue {`

### `src/Avalonia.Base/Threading/DispatcherOperation.cs`
- Namespace: `Avalonia.Threading`
- `public class DispatcherOperation`
- `public DispatcherOperationStatus Status { get; internal set; }`
- `public Dispatcher Dispatcher { get; }`
- `public DispatcherPriority Priority {`
- `public event EventHandler Aborted {`
- `public event EventHandler Completed {`
- `public bool Abort() {`
- `public void Wait() => Wait(TimeSpan.FromMilliseconds(-1));`
- `public void Wait(TimeSpan timeout) {`
- `public Task GetTask() => GetTaskCore();`
- `public TaskAwaiter GetAwaiter() {`
- `public class DispatcherOperation<T> : DispatcherOperation`
- `public DispatcherOperation(Dispatcher dispatcher, DispatcherPriority priority, Func<T> callback) : base(dispatcher, priority, false) {`
- `public new TaskAwaiter<T> GetAwaiter() => GetTask().GetAwaiter();`
- `public new Task<T> GetTask() => TaskCompletionSource!.Task;`
- `public T Result {`
- `public enum DispatcherOperationStatus`

### `src/Avalonia.Base/Threading/DispatcherOptions.cs`
- Namespace: `Avalonia.Threading`
- `public class DispatcherOptions`
- `public TimeSpan InputStarvationTimeout { get; set; } = TimeSpan.FromSeconds(1);`

### `src/Avalonia.Base/Threading/DispatcherPriority.cs`
- `public readonly struct DispatcherPriority : IEquatable<DispatcherPriority>, IComparable<DispatcherPriority>`
- `public int Value { get; }`
- `public static readonly DispatcherPriority Default = new(0);`
- `public static readonly DispatcherPriority Input = new(Default - 1);`
- `public static readonly DispatcherPriority Background = new(Input - 1);`
- `public static readonly DispatcherPriority ContextIdle = new(Background - 1);`
- `public static readonly DispatcherPriority ApplicationIdle = new (ContextIdle - 1);`
- `public static readonly DispatcherPriority SystemIdle = new(ApplicationIdle - 1);`
- `public static readonly DispatcherPriority Inactive = new(MinimumActiveValue - 1);`
- `public static readonly DispatcherPriority Invalid = new(MinimumActiveValue - 2);`
- `public static readonly DispatcherPriority Loaded = new(Default + 1);`
- `public static readonly DispatcherPriority UiThreadRender = new(Loaded + 1);`
- `public static readonly DispatcherPriority Render = new(AfterRender + 1);`
- `public static readonly DispatcherPriority BeforeRender = new(Render + 1);`
- `public static readonly DispatcherPriority AsyncRenderTargetResize = new(BeforeRender + 1);`
- `public static readonly DispatcherPriority Normal = new(DataBind + 1);`
- `public static readonly DispatcherPriority Send = new(Normal + 1);`
- `public static readonly DispatcherPriority MaxValue = Send;`
- `public static DispatcherPriority FromValue(int value) {`
- `public static implicit operator int(DispatcherPriority priority) => priority.Value;`
- `public static implicit operator DispatcherPriority(int value) => FromValue(value);`
- `public bool Equals(DispatcherPriority other) => Value == other.Value;`
- `public override bool Equals(object? obj) => obj is DispatcherPriority other && Equals(other);`
- `public override int GetHashCode() => Value.GetHashCode();`
- `public static bool operator ==(DispatcherPriority left, DispatcherPriority right) => left.Value == right.Value;`
- `public static bool operator !=(DispatcherPriority left, DispatcherPriority right) => left.Value != right.Value;`
- `public static bool operator <(DispatcherPriority left, DispatcherPriority right) => left.Value < right.Value;`
- `public static bool operator >(DispatcherPriority left, DispatcherPriority right) => left.Value > right.Value;`
- `public static bool operator <=(DispatcherPriority left, DispatcherPriority right) => left.Value <= right.Value;`
- `public static bool operator >=(DispatcherPriority left, DispatcherPriority right) => left.Value >= right.Value;`
- `public int CompareTo(DispatcherPriority other) => Value.CompareTo(other.Value);`
- `public static void Validate(DispatcherPriority priority, string parameterName) {`
- `public override string ToString() {`

### `src/Avalonia.Base/Threading/DispatcherPriorityAwaitable.cs`
- Namespace: `Avalonia.Threading`
- `public class DispatcherPriorityAwaitable : INotifyCompletion`
- `public void OnCompleted(Action continuation) =>`
- `public bool IsCompleted => Task.IsCompleted;`
- `public void GetResult() => Task.GetAwaiter().GetResult();`
- `public DispatcherPriorityAwaitable GetAwaiter() => this;`
- `public sealed class DispatcherPriorityAwaitable<T> : DispatcherPriorityAwaitable`
- `public new T GetResult() => ((Task<T>)Task).GetAwaiter().GetResult();`
- `public new DispatcherPriorityAwaitable<T> GetAwaiter() => this;`

### `src/Avalonia.Base/Threading/DispatcherTimer.cs`
- Namespace: `Avalonia.Threading`
- `public partial class DispatcherTimer`
- `public DispatcherTimer() : this(DispatcherPriority.Background) {`
- `public DispatcherTimer(DispatcherPriority priority) : this(Threading.Dispatcher.UIThread, priority, TimeSpan.FromMilliseconds(0)) {`
- `public DispatcherTimer(TimeSpan interval, DispatcherPriority priority, EventHandler callback) : this(Threading.Dispatcher.UIThread, priority, interval) {`
- `public Dispatcher Dispatcher {`
- `public bool IsEnabled {`
- `public TimeSpan Interval {`
- `public void Start() {`
- `public void Stop() {`
- `public static IDisposable Run(Func<bool> action, TimeSpan interval, DispatcherPriority priority = default) {`
- `public static IDisposable RunOnce( Action action, TimeSpan interval, DispatcherPriority priority = default) {`
- `public event EventHandler? Tick;`
- `public object? Tag { get; set; }`

### `src/Avalonia.Base/Threading/DispatcherUnhandledExceptionEventArgs.cs`
- Namespace: `Avalonia.Threading`
- `public sealed class DispatcherUnhandledExceptionEventArgs : DispatcherEventArgs`
- `public Exception Exception => _exception;`
- `public bool Handled {`

### `src/Avalonia.Base/Threading/DispatcherUnhandledExceptionFilterEventArgs.cs`
- Namespace: `Avalonia.Threading`
- `public sealed class DispatcherUnhandledExceptionFilterEventArgs : DispatcherEventArgs`
- `public Exception Exception => _exception!;`
- `public bool RequestCatch {`

## Rendering and Text

### `src/Avalonia.Fonts.Inter/AppBuilderExtension.cs`
- `public static class AppBuilderExtension`
- `public static AppBuilder WithInterFont(this AppBuilder appBuilder) {`

### `src/Skia/Avalonia.Skia/SkiaApplicationExtensions.cs`
- `public static class SkiaApplicationExtensions`
- `public static AppBuilder UseSkia(this AppBuilder builder) {`

### `src/Skia/Avalonia.Skia/SkiaOptions.cs`
- `public class SkiaOptions`
- `public long? MaxGpuResourceSizeBytes { get; set; } = 1024 * 600 * 4 * 12;`
- `public bool UseOpacitySaveLayer { get; set; } = false;`

## Windows Platform

### `src/Windows/Avalonia.Win32/Win32Platform.cs`
- `public static class Win32ApplicationExtensions`
- `public static AppBuilder UseWin32(this AppBuilder builder) {`

### `src/Windows/Avalonia.Win32/Win32PlatformOptions.cs`
- Namespace: `Avalonia`
- `public enum Win32RenderingMode`
- `public enum Win32DpiAwareness`
- `public enum Win32CompositionMode`
- `public class Win32PlatformOptions`
- `public bool OverlayPopups { get; set; }`
- `public IReadOnlyList<Win32RenderingMode> RenderingMode { get; set; } = new[]`
- `public IReadOnlyList<Win32CompositionMode> CompositionMode { get; set; } = new[]`
- `public float? WinUICompositionBackdropCornerRadius { get; set; }`
- `public bool ShouldRenderOnUIThread { get; set; }`
- `public IList<GlVersion> WglProfiles { get; set; } = new List<GlVersion>`
- `public IPlatformGraphics? CustomPlatformGraphics { get; set; }`
- `public Win32DpiAwareness DpiAwareness { get; set; } = Win32DpiAwareness.PerMonitorDpiAware;`
- `public Func<IReadOnlyList<PlatformGraphicsDeviceAdapterDescription>, int>? GraphicsAdapterSelectionCallback { get; set; }`

## XAML and Markup

### `src/Markup/Avalonia.Markup.Xaml.Loader/AvaloniaRuntimeXamlLoader.cs`
- `public static class AvaloniaRuntimeXamlLoader`
- `public static object Load([StringSyntax(StringSyntaxAttribute.Xml)] string xaml, Assembly? localAssembly = null, object? rootInstance = null, Uri? uri = null, bool designMode = false) {`
- `public static object Load(Stream stream, Assembly? localAssembly = null, object? rootInstance = null, Uri? uri = null, bool designMode = false) => AvaloniaXamlIlRuntimeCompiler.Load(new RuntimeXamlLoaderDocument(uri, rootInstance, stream),`
- `public static object Load(RuntimeXamlLoaderDocument document, RuntimeXamlLoaderConfiguration? configuration = null) => AvaloniaXamlIlRuntimeCompiler.Load(document, configuration ?? new RuntimeXamlLoaderConfiguration());`
- `public static IReadOnlyList<object?> LoadGroup(IReadOnlyCollection<RuntimeXamlLoaderDocument> documents, RuntimeXamlLoaderConfiguration? configuration = null) => AvaloniaXamlIlRuntimeCompiler.LoadGroup(documents, configuration ?? new RuntimeXamlLoaderConfiguration());`
- `public static object Parse([StringSyntax(StringSyntaxAttribute.Xml)] string xaml, Assembly? localAssembly = null) => Load(xaml, localAssembly);`
- `public static T Parse<[DynamicallyAccessedMembers(DynamicallyAccessedMemberTypes.All)] T>([StringSyntax(StringSyntaxAttribute.Xml)] string xaml, Assembly? localAssembly = null) => (T)Parse(xaml, localAssembly);`

### `src/Markup/Avalonia.Markup.Xaml/AvaloniaXamlLoader.cs`
- `public static class AvaloniaXamlLoader`
- `public static void Load(object obj) {`
- `public static void Load(IServiceProvider? sp, object obj) {`
- `public static object Load(Uri uri, Uri? baseUri = null) {`
- `public static object Load(IServiceProvider? sp, Uri uri, Uri? baseUri = null) {`

### `src/Markup/Avalonia.Markup.Xaml/MarkupExtensions/CompiledBindingExtension.cs`
- `public class CompiledBindingExtension : BindingBase`
- `public CompiledBindingExtension() {`
- `public CompiledBindingExtension(CompiledBindingPath path) {`
- `public CompiledBindingExtension ProvideValue(IServiceProvider provider) {`
- `public CompiledBindingPath Path { get; set; }`
- `public object? Source { get; set; } = AvaloniaProperty.UnsetValue;`
- `public Type? DataType { get; set; }`
- `public override InstancedBinding? Initiate( AvaloniaObject target, AvaloniaProperty? targetProperty, object? anchor = null, bool enableDataValidation = false) {`

### `src/Markup/Avalonia.Markup.Xaml/MarkupExtensions/DynamicResourceExtension.cs`
- `public class DynamicResourceExtension : IBinding2`
- `public DynamicResourceExtension() {`
- `public DynamicResourceExtension(object resourceKey) {`
- `public object? ResourceKey { get; set; }`
- `public IBinding ProvideValue(IServiceProvider serviceProvider) {`

### `src/Markup/Avalonia.Markup.Xaml/MarkupExtensions/On.cs`
- Namespace: `Avalonia.Markup.Xaml.MarkupExtensions`
- `public class On<TReturn>`
- `public IReadOnlyList<string> Options { get; } = new List<string>();`
- `public TReturn? Content { get; set; }`
- `public class On : On<object> {}`

### `src/Markup/Avalonia.Markup.Xaml/MarkupExtensions/OnFormFactorExtension.cs`
- Namespace: `Avalonia.Markup.Xaml.MarkupExtensions`
- `public sealed class OnFormFactorExtension : OnFormFactorExtensionBase<object, On>`
- `public OnFormFactorExtension() {`
- `public OnFormFactorExtension(object defaultValue) {`
- `public static bool ShouldProvideOption(IServiceProvider serviceProvider, FormFactorType option) {`
- `public sealed class OnFormFactorExtension<TReturn> : OnFormFactorExtensionBase<TReturn, On<TReturn>>`
- `public OnFormFactorExtension() {`
- `public OnFormFactorExtension(TReturn defaultValue) {`
- `public static bool ShouldProvideOption(IServiceProvider serviceProvider, FormFactorType option) {`
- `public abstract class OnFormFactorExtensionBase<TReturn, TOn> : IAddChild<TOn>`
- `public TReturn? Default { get; set; }`
- `public TReturn? Desktop { get; set; }`
- `public TReturn? Mobile { get; set; }`
- `public TReturn? TV { get; set; }`
- `public object ProvideValue() { return this; }`

### `src/Markup/Avalonia.Markup.Xaml/MarkupExtensions/OnPlatformExtension.cs`
- Namespace: `Avalonia.Markup.Xaml.MarkupExtensions`
- `public sealed class OnPlatformExtension : OnPlatformExtensionBase<object, On>`
- `public OnPlatformExtension() {`
- `public OnPlatformExtension(object defaultValue) {`
- `public static bool ShouldProvideOption(string option) {`
- `public sealed class OnPlatformExtension<TReturn> : OnPlatformExtensionBase<TReturn, On<TReturn>>`
- `public OnPlatformExtension() {`
- `public OnPlatformExtension(TReturn defaultValue) {`
- `public static bool ShouldProvideOption(string option) {`
- `public abstract class OnPlatformExtensionBase<TReturn, TOn> : IAddChild<TOn>`
- `public TReturn? Default { get; set; }`
- `public TReturn? Windows { get; set; }`
- `public TReturn? macOS { get; set; }`
- `public TReturn? Linux { get; set; }`
- `public TReturn? Android { get; set; }`
- `public TReturn? iOS { get; set; }`
- `public TReturn? Browser { get; set; }`
- `public object ProvideValue() { return this; }`

### `src/Markup/Avalonia.Markup.Xaml/MarkupExtensions/ReflectionBindingExtension.cs`
- `public class ReflectionBindingExtension`
- `public ReflectionBindingExtension() {`
- `public ReflectionBindingExtension(string path) {`
- `public Binding ProvideValue(IServiceProvider serviceProvider) {`
- `public int Delay { get; set; }`
- `public IValueConverter? Converter { get; set; }`
- `public CultureInfo? ConverterCulture { get; set; }`
- `public object? ConverterParameter { get; set; }`
- `public string? ElementName { get; set; }`
- `public object? FallbackValue { get; set; } = AvaloniaProperty.UnsetValue;`
- `public BindingMode Mode { get; set; }`
- `public string Path { get; set; } = "";`
- `public BindingPriority Priority { get; set; } = BindingPriority.LocalValue;`
- `public object? Source { get; set; } = AvaloniaProperty.UnsetValue;`
- `public string? StringFormat { get; set; }`
- `public RelativeSource? RelativeSource { get; set; }`
- `public object? TargetNullValue { get; set; } = AvaloniaProperty.UnsetValue;`
- `public UpdateSourceTrigger UpdateSourceTrigger { get; set; }`

### `src/Markup/Avalonia.Markup.Xaml/MarkupExtensions/RelativeSourceExtension.cs`
- `public class RelativeSourceExtension`
- `public RelativeSourceExtension() {`
- `public RelativeSourceExtension(RelativeSourceMode mode) {`
- `public RelativeSource ProvideValue(IServiceProvider serviceProvider) {`
- `public RelativeSourceMode Mode { get; set; } = RelativeSourceMode.FindAncestor;`
- `public Type? AncestorType { get; set; }`
- `public TreeType Tree { get; set; }`
- `public int AncestorLevel { get; set; } = 1;`

### `src/Markup/Avalonia.Markup.Xaml/MarkupExtensions/ResolveByNameExtension.cs`
- `public class ResolveByNameExtension`
- `public ResolveByNameExtension(string name) {`
- `public string Name { get; }`
- `public object? ProvideValue(IServiceProvider serviceProvider) => ProvideValue(serviceProvider, Name);`

### `src/Markup/Avalonia.Markup.Xaml/MarkupExtensions/StaticResourceExtension.cs`
- `public class StaticResourceExtension`
- `public StaticResourceExtension() {`
- `public StaticResourceExtension(object resourceKey) {`
- `public object? ResourceKey { get; set; }`
- `public object? ProvideValue(IServiceProvider serviceProvider) => ProvideValue(serviceProvider, ResourceKey);`

### `src/Markup/Avalonia.Markup.Xaml/Styling/MergeResourceInclude.cs`
- Namespace: `Avalonia.Markup.Xaml.Styling`
- `public class MergeResourceInclude : ResourceInclude`
- `public MergeResourceInclude(Uri? baseUri) : base(baseUri) {`
- `public MergeResourceInclude(IServiceProvider serviceProvider) : base(serviceProvider) {`

### `src/Markup/Avalonia.Markup.Xaml/Styling/ResourceInclude.cs`
- `public class ResourceInclude : IResourceProvider, IThemeVariantProvider`
- `public ResourceInclude(Uri? baseUri) {`
- `public ResourceInclude(IServiceProvider serviceProvider) {`
- `public IResourceDictionary Loaded {`
- `public IResourceHost? Owner => Loaded.Owner;`
- `public Uri? Source { get; set; }`
- `public event EventHandler? OwnerChanged {`
- `public bool TryGetResource(object key, ThemeVariant? theme, out object? value) {`

### `src/Markup/Avalonia.Markup.Xaml/Styling/StyleInclude.cs`
- `public class StyleInclude : IStyle, IResourceProvider`
- `public StyleInclude(Uri? baseUri) {`
- `public StyleInclude(IServiceProvider serviceProvider) {`
- `public IResourceHost? Owner => (Loaded as IResourceProvider)?.Owner;`
- `public Uri? Source { get; set; }`
- `public IStyle Loaded {`
- `public event EventHandler? OwnerChanged {`
- `public bool TryGetResource(object key, ThemeVariant? theme, out object? value) {`

### `src/Markup/Avalonia.Markup.Xaml/Templates/ControlTemplate.cs`
- `public class ControlTemplate : IControlTemplate`
- `public object? Content { get; set; }`
- `public Type? TargetType { get; set; }`
- `public TemplateResult<Control>? Build(TemplatedControl control) => TemplateContent.Load(Content);`

### `src/Markup/Avalonia.Markup.Xaml/Templates/DataTemplate.cs`
- `public class DataTemplate : IRecyclingDataTemplate, ITypedDataTemplate`
- `public Type? DataType { get; set; }`
- `public object? Content { get; set; }`
- `public bool Match(object? data) {`
- `public Control? Build(object? data) => Build(data, null);`
- `public Control? Build(object? data, Control? existing) {`

### `src/Markup/Avalonia.Markup.Xaml/Templates/FocusAdornerTemplate.cs`
- `public class FocusAdornerTemplate : Template`

### `src/Markup/Avalonia.Markup.Xaml/Templates/ItemsPanelTemplate.cs`
- `public class ItemsPanelTemplate : ITemplate<Panel?>`
- `public object? Content { get; set; }`
- `public Panel? Build() => (Panel?)TemplateContent.Load(Content)?.Result;`

### `src/Markup/Avalonia.Markup.Xaml/Templates/Template.cs`
- `public class Template : ITemplate<Control?>`
- `public object? Content { get; set; }`
- `public Control? Build() => TemplateContent.Load(Content)?.Result;`

### `src/Markup/Avalonia.Markup.Xaml/Templates/TemplateContent.cs`
- `public static class TemplateContent`
- `public static TemplateResult<Control>? Load(object? templateContent) => Load<Control>(templateContent);`
- `public static TemplateResult<T>? Load<T>(object? templateContent) => templateContent switch`

### `src/Markup/Avalonia.Markup.Xaml/Templates/TreeDataTemplate.cs`
- `public class TreeDataTemplate : ITreeDataTemplate, ITypedDataTemplate`
- `public Type? DataType { get; set; }`
- `public object? Content { get; set; }`
- `public BindingBase? ItemsSource { get; set; }`
- `public bool Match(object? data) {`
- `public InstancedBinding? ItemsSelector(object item) {`
- `public Control? Build(object? data) {`

### `src/Markup/Avalonia.Markup/Data/Binding.cs`
- `public class Binding : BindingBase`
- `public Binding() {`
- `public Binding(string path, BindingMode mode = BindingMode.Default) : base(mode) {`
- `public string? ElementName { get; set; }`
- `public RelativeSource? RelativeSource { get; set; }`
- `public object? Source { get; set; } = AvaloniaProperty.UnsetValue;`
- `public string Path { get; set; } = "";`
- `public Func<string?, string, Type>? TypeResolver { get; set; }`
- `public override InstancedBinding? Initiate( AvaloniaObject target, AvaloniaProperty? targetProperty, object? anchor = null, bool enableDataValidation = false) {`

## iOS Platform

### `src/iOS/Avalonia.iOS/Platform.cs`
- `public enum iOSRenderingMode`
- `public class iOSPlatformOptions`
- `public IReadOnlyList<iOSRenderingMode> RenderingMode { get; set; } = new[]`
- `public static class IOSApplicationExtensions`
- `public static AppBuilder UseiOS(this AppBuilder builder, IAvaloniaAppDelegate appDelegate) {`
- `public static AppBuilder UseiOS(this AppBuilder builder) => UseiOS(builder, null!);`

## macOS Native Platform

### `src/Avalonia.Native/AvaloniaNativePlatformExtensions.cs`
- `public static class AvaloniaNativePlatformExtensions`
- `public static AppBuilder UseAvaloniaNative(this AppBuilder builder) {`
- `public enum AvaloniaNativeRenderingMode`
- `public class AvaloniaNativePlatformOptions`
- `public IReadOnlyList<AvaloniaNativeRenderingMode> RenderingMode { get; set; } = new[]`
- `public bool OverlayPopups { get; set; }`
- `public string AvaloniaNativeLibraryPath { get; set; }`
- `public bool AppSandboxEnabled { get; set; } = true;`
- `public class MacOSPlatformOptions`
- `public bool ShowInDock { get; set; } = true;`
- `public bool DisableDefaultApplicationMenuItems { get; set; }`
- `public bool DisableNativeMenus { get; set; }`
- `public bool DisableSetProcessName { get; set; }`
- `public bool DisableAvaloniaAppDelegate { get; set; }`
