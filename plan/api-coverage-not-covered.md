# API Coverage Gap Report

- API index: `references/api-index-generated.md`
- References scanned: `references`
- Reference docs scanned: `431`
- API signatures parsed: `9895`
- Covered APIs: `5528`
- Not covered APIs: `4367`

## Not Covered API Signatures

### `src/Android/Avalonia.Android/AndroidViewControlHandle.cs`
- `public class AndroidViewControlHandle : PlatformHandle, INativeControlHostDestroyableControlHandle`
- `public AndroidViewControlHandle(View view) : base(view.Handle, AndroidViewDescriptor) {`
- `public View View { get; private set; }`
- `public void Destroy() {`

### `src/Android/Avalonia.Android/Automation/INodeInfoProvider.cs`
- `public interface INodeInfoProvider`

### `src/Android/Avalonia.Android/AvaloniaActivity.cs`
- `public class AvaloniaActivity : AppCompatActivity, IAvaloniaActivity`
- `public Action<int, Result, Intent?>? ActivityResult { get; set; }`
- `public Action<int, string[], Permission[]>? RequestPermissionsResult { get; set; }`
- `public override void OnBackPressed() {`
- `public override void OnRequestPermissionsResult(int requestCode, string[] permissions, Permission[] grantResults) {`
- `public void OnBackInvoked() {`

### `src/Android/Avalonia.Android/AvaloniaView.Input.cs`
- `public override IInputConnection OnCreateInputConnection(EditorInfo? outAttrs) {`
- `public override bool DispatchTouchEvent(MotionEvent? e) {`
- `public override bool DispatchKeyEvent(KeyEvent? e) {`

### `src/Android/Avalonia.Android/AvaloniaView.cs`
- `public override void OnVisibilityAggregated(bool isVisible) {`

### `src/Android/Avalonia.Android/IActivityResultHandler.cs`
- `public interface IActivityResultHandler`
- `public Action<int, Result, Intent?>? ActivityResult { get; set; }`
- `public Action<int, string[], Permission[]>? RequestPermissionsResult { get; set; }`

### `src/Android/Avalonia.Android/IAndroidNavigationService.cs`
- `public interface IActivityNavigationService`
- `public class AndroidBackRequestedEventArgs : EventArgs`

### `src/Android/Avalonia.Android/IAvaloniaActivity.cs`
- `public interface IAvaloniaActivity : IActivityResultHandler, IActivityNavigationService`

### `src/Android/Avalonia.Android/Platform/SkiaPlatform/AndroidFramebuffer.cs`
- `public enum AndroidPixelFormat`

### `src/Android/Avalonia.Android/Platform/Specific/IAndroidView.cs`
- `public interface IAndroidView`

### `src/Avalonia.Base/Animation/Animatable.cs`
- `public static readonly StyledProperty<Transitions?> TransitionsProperty = AvaloniaProperty.Register<Animatable, Transitions?>(nameof(Transitions));`

### `src/Avalonia.Base/Animation/Animation.cs`
- `public static readonly DirectProperty<Animation, TimeSpan> DurationProperty = AvaloniaProperty.RegisterDirect<Animation, TimeSpan>( nameof(Duration), o => o._duration,`
- `public static readonly DirectProperty<Animation, IterationCount> IterationCountProperty = AvaloniaProperty.RegisterDirect<Animation, IterationCount>( nameof(IterationCount), o => o._iterationCount,`
- `public static readonly DirectProperty<Animation, PlaybackDirection> PlaybackDirectionProperty = AvaloniaProperty.RegisterDirect<Animation, PlaybackDirection>( nameof(PlaybackDirection), o => o._playbackDirection,`
- `public static readonly DirectProperty<Animation, FillMode> FillModeProperty = AvaloniaProperty.RegisterDirect<Animation, FillMode>( nameof(FillMode), o => o._fillMode,`
- `public static readonly DirectProperty<Animation, Easing> EasingProperty = AvaloniaProperty.RegisterDirect<Animation, Easing>( nameof(Easing), o => o._easing,`
- `public static readonly DirectProperty<Animation, TimeSpan> DelayBetweenIterationsProperty = AvaloniaProperty.RegisterDirect<Animation, TimeSpan>( nameof(DelayBetweenIterations), o => o._delayBetweenIterations,`
- `public static readonly DirectProperty<Animation, double> SpeedRatioProperty = AvaloniaProperty.RegisterDirect<Animation, double>( nameof(SpeedRatio), o => o._speedRatio,`
- `public Easing Easing {`

### `src/Avalonia.Base/Animation/CrossFade.cs`
- `public Easing FadeInEasing {`
- `public Easing FadeOutEasing {`

### `src/Avalonia.Base/Animation/Cue.cs`
- `public double CueValue { get; }`
- `public class CueTypeConverter : TypeConverter`

### `src/Avalonia.Base/Animation/Easings/BackEaseIn.cs`
- `public class BackEaseIn : Easing`
- `public override double Ease(double p) {`

### `src/Avalonia.Base/Animation/Easings/BackEaseInOut.cs`
- `public class BackEaseInOut : Easing`
- `public override double Ease(double progress) {`

### `src/Avalonia.Base/Animation/Easings/BackEaseOut.cs`
- `public class BackEaseOut : Easing`
- `public override double Ease(double progress) {`

### `src/Avalonia.Base/Animation/Easings/BounceEaseIn.cs`
- `public class BounceEaseIn : Easing`
- `public override double Ease(double progress) {`

### `src/Avalonia.Base/Animation/Easings/BounceEaseInOut.cs`
- `public class BounceEaseInOut : Easing`
- `public override double Ease(double progress) {`

### `src/Avalonia.Base/Animation/Easings/BounceEaseOut.cs`
- `public class BounceEaseOut : Easing`
- `public override double Ease(double progress) {`

### `src/Avalonia.Base/Animation/Easings/CircularEaseIn.cs`
- `public class CircularEaseIn : Easing`
- `public override double Ease(double p) {`

### `src/Avalonia.Base/Animation/Easings/CircularEaseInOut.cs`
- `public class CircularEaseInOut : Easing`
- `public override double Ease(double progress) {`

### `src/Avalonia.Base/Animation/Easings/CircularEaseOut.cs`
- `public class CircularEaseOut : Easing`
- `public override double Ease(double progress) {`

### `src/Avalonia.Base/Animation/Easings/CubicBezierEasing.cs`
- `public Point ControlPoint2 { get; set; }`
- `public Point ControlPoint1 { get; set; }`

### `src/Avalonia.Base/Animation/Easings/CubicEaseIn.cs`
- `public override double Ease(double progress) {`

### `src/Avalonia.Base/Animation/Easings/CubicEaseInOut.cs`
- `public override double Ease(double progress) {`

### `src/Avalonia.Base/Animation/Easings/CubicEaseOut.cs`
- `public override double Ease(double progress) {`

### `src/Avalonia.Base/Animation/Easings/Easing.cs`
- `public abstract double Ease(double progress);`

### `src/Avalonia.Base/Animation/Easings/EasingTypeConverter.cs`
- `public class EasingTypeConverter : TypeConverter`

### `src/Avalonia.Base/Animation/Easings/ElasticEaseIn.cs`
- `public class ElasticEaseIn : Easing`
- `public override double Ease(double progress) {`

### `src/Avalonia.Base/Animation/Easings/ElasticEaseInOut.cs`
- `public class ElasticEaseInOut : Easing`
- `public override double Ease(double progress) {`

### `src/Avalonia.Base/Animation/Easings/ElasticEaseOut.cs`
- `public class ElasticEaseOut : Easing`
- `public override double Ease(double progress) {`

### `src/Avalonia.Base/Animation/Easings/ExponentialEaseIn.cs`
- `public class ExponentialEaseIn : Easing`
- `public override double Ease(double progress) {`

### `src/Avalonia.Base/Animation/Easings/ExponentialEaseInOut.cs`
- `public class ExponentialEaseInOut : Easing`
- `public override double Ease(double progress) {`

### `src/Avalonia.Base/Animation/Easings/ExponentialEaseOut.cs`
- `public class ExponentialEaseOut : Easing`
- `public override double Ease(double progress) {`

### `src/Avalonia.Base/Animation/Easings/IEasing.cs`
- `public interface IEasing`

### `src/Avalonia.Base/Animation/Easings/LinearEasing.cs`
- `public override double Ease(double progress) {`

### `src/Avalonia.Base/Animation/Easings/QuadraticEaseIn.cs`
- `public class QuadraticEaseIn : Easing`
- `public override double Ease(double progress) {`

### `src/Avalonia.Base/Animation/Easings/QuadraticEaseInOut.cs`
- `public class QuadraticEaseInOut : Easing`
- `public override double Ease(double progress) {`

### `src/Avalonia.Base/Animation/Easings/QuadraticEaseOut.cs`
- `public class QuadraticEaseOut : Easing`
- `public override double Ease(double progress) {`

### `src/Avalonia.Base/Animation/Easings/QuarticEaseIn.cs`
- `public class QuarticEaseIn : Easing`
- `public override double Ease(double progress) {`

### `src/Avalonia.Base/Animation/Easings/QuarticEaseInOut.cs`
- `public class QuarticEaseInOut : Easing`
- `public override double Ease(double progress) {`

### `src/Avalonia.Base/Animation/Easings/QuarticEaseOut.cs`
- `public class QuarticEaseOut : Easing`
- `public override double Ease(double progress) {`

### `src/Avalonia.Base/Animation/Easings/QuinticEaseIn.cs`
- `public class QuinticEaseIn : Easing`
- `public override double Ease(double progress) {`

### `src/Avalonia.Base/Animation/Easings/QuinticEaseInOut.cs`
- `public class QuinticEaseInOut : Easing`
- `public override double Ease(double progress) {`

### `src/Avalonia.Base/Animation/Easings/QuinticEaseOut.cs`
- `public class QuinticEaseOut : Easing`
- `public override double Ease(double progress) {`

### `src/Avalonia.Base/Animation/Easings/SineEaseIn.cs`
- `public override double Ease(double progress) {`

### `src/Avalonia.Base/Animation/Easings/SineEaseInOut.cs`
- `public override double Ease(double progress) {`

### `src/Avalonia.Base/Animation/Easings/SineEaseOut.cs`
- `public override double Ease(double progress) {`

### `src/Avalonia.Base/Animation/Easings/SplineEasing.cs`
- `public double X1 {`
- `public double Y1 {`
- `public double X2 {`
- `public double Y2 {`
- `public override double Ease(double progress) =>`

### `src/Avalonia.Base/Animation/Easings/SpringEasing.cs`
- `public double Mass {`
- `public double Stiffness {`
- `public double Damping {`
- `public double InitialVelocity {`
- `public override double Ease(double progress) => _internalSpring.GetSpringProgress(progress);`

### `src/Avalonia.Base/Animation/IAnimation.cs`
- `public interface IAnimation`

### `src/Avalonia.Base/Animation/IAnimationSetter.cs`
- `public interface IAnimationSetter`

### `src/Avalonia.Base/Animation/ICustomAnimator.cs`
- `public abstract class CustomAnimatorBase`
- `public abstract class CustomAnimatorBase<T> : CustomAnimatorBase`
- `public abstract T Interpolate(double progress, T oldValue, T newValue);`
- `public interface ICustomAnimator`
- `public abstract class InterpolatingAnimator<T> : ICustomAnimator`

### `src/Avalonia.Base/Animation/InterpolatingTransitionBase.cs`
- `public abstract class InterpolatingTransitionBase<T> : Transition<T>`

### `src/Avalonia.Base/Animation/IterationCount.cs`
- `public enum IterationType`
- `public IterationType RepeatType => _type;`
- `public bool IsInfinite => _type == IterationType.Infinite;`

### `src/Avalonia.Base/Animation/IterationCountTypeConverter.cs`
- `public class IterationCountTypeConverter : TypeConverter`

### `src/Avalonia.Base/Animation/KeyFrame.cs`
- `public AvaloniaList<IAnimationSetter> Setters { get; } = new AvaloniaList<IAnimationSetter>();`
- `public TimeSpan KeyTime {`
- `public KeySpline? KeySpline {`

### `src/Avalonia.Base/Animation/KeyFrames.cs`
- `public sealed class KeyFrames : AvaloniaList<KeyFrame>`
- `public KeyFrames() {`
- `public KeyFrames(IEnumerable<KeyFrame> items) : base(items) {`

### `src/Avalonia.Base/Animation/KeySpline.cs`
- `public sealed class KeySpline : AvaloniaObject`
- `public KeySpline() {`
- `public KeySpline(double x1, double y1, double x2, double y2) {`
- `public double ControlPointX1 {`
- `public double ControlPointY1 {`
- `public double ControlPointX2 {`
- `public double ControlPointY2 {`
- `public double GetSplineProgress(double linearProgress) {`
- `public bool IsValid() {`

### `src/Avalonia.Base/Animation/KeySplineTypeConverter.cs`
- `public class KeySplineTypeConverter : TypeConverter`

### `src/Avalonia.Base/Animation/PageSlide.cs`
- `public enum SlideAxis`
- `public Easing SlideInEasing { get; set; } = new LinearEasing();`
- `public Easing SlideOutEasing { get; set; } = new LinearEasing();`

### `src/Avalonia.Base/Animation/PlayState.cs`
- `public enum PlayState`

### `src/Avalonia.Base/Animation/TransitionBase.cs`
- `public abstract class TransitionBase : AvaloniaObject, ITransition`
- `public static readonly DirectProperty<TransitionBase, TimeSpan> DurationProperty = AvaloniaProperty.RegisterDirect<TransitionBase, TimeSpan>( nameof(Duration), o => o._duration,`
- `public static readonly DirectProperty<TransitionBase, Easing> EasingProperty = AvaloniaProperty.RegisterDirect<TransitionBase, Easing>( nameof(Easing), o => o._easing,`
- `public static readonly DirectProperty<TransitionBase, AvaloniaProperty?> PropertyProperty = AvaloniaProperty.RegisterDirect<TransitionBase, AvaloniaProperty?>( nameof(Property), o => o._prop,`
- `public Easing Easing {`

### `src/Avalonia.Base/Animation/Transitions/BoolTransition.cs`
- `public class BoolTransition : Transition<bool>`

### `src/Avalonia.Base/Animation/Transitions/FloatTransition.cs`
- `public class FloatTransition : Transition<float>`

### `src/Avalonia.Base/Animation/Transitions/IntegerTransition.cs`
- `public class IntegerTransition : Transition<int>`

### `src/Avalonia.Base/Animation/Transitions/PointTransition.cs`
- `public class PointTransition : Transition<Point>`

### `src/Avalonia.Base/Animation/Transitions/RelativePointTransition.cs`
- `public class RelativePointTransition : Transition<RelativePoint>`

### `src/Avalonia.Base/Animation/Transitions/Rotate3DTransition.cs`
- `public double? Depth { get; set; }`

### `src/Avalonia.Base/Animation/Transitions/SizeTransition.cs`
- `public class SizeTransition : Transition<Size>`

### `src/Avalonia.Base/Animation/Transitions/VectorTransition.cs`
- `public class VectorTransition : Transition<Vector>`

### `src/Avalonia.Base/AvaloniaInternalException.cs`
- `public class AvaloniaInternalException : Exception`
- `public AvaloniaInternalException(string message) : base(message) {`

### `src/Avalonia.Base/AvaloniaLocator.cs`
- `public static AvaloniaLocator CurrentMutable { get; set; }`
- `public AvaloniaLocator() {`
- `public AvaloniaLocator(IAvaloniaDependencyResolver parentScope) {`
- `public class RegistrationHelper<TService>`
- `public RegistrationHelper(AvaloniaLocator locator) {`
- `public AvaloniaLocator ToConstant<TImpl>(TImpl constant) where TImpl : TService {`
- `public AvaloniaLocator ToFunc<TImlp>(Func<TImlp> func) where TImlp : TService {`
- `public AvaloniaLocator ToLazy<TImlp>(Func<TImlp> func) where TImlp : TService {`
- `public AvaloniaLocator ToSingleton<TImpl>() where TImpl : class, TService, new() {`
- `public AvaloniaLocator ToTransient<TImpl>() where TImpl : class, TService, new() => ToFunc(() => new TImpl());`
- `public AvaloniaLocator BindToSelf<T>(T constant) => Bind<T>().ToConstant(constant);`
- `public AvaloniaLocator BindToSelfSingleton<T>() where T : class, new() => Bind<T>().ToSingleton<T>();`
- `public static IDisposable EnterScope() {`
- `public static class LocatorExtensions`
- `public static object GetRequiredService(this IAvaloniaDependencyResolver resolver, Type t) {`
- `public static T GetRequiredService<T>(this IAvaloniaDependencyResolver resolver) {`

### `src/Avalonia.Base/Collections/AvaloniaDictionary.cs`
- `public class AvaloniaDictionary<TKey, TValue> : IAvaloniaDictionary<TKey, TValue> where TKey : notnull`
- `public AvaloniaDictionary() {`
- `public AvaloniaDictionary(int capacity) {`
- `public AvaloniaDictionary(IDictionary<TKey, TValue> dictionary, IEqualityComparer<TKey>? comparer = null) {`

### `src/Avalonia.Base/Collections/AvaloniaDictionaryExtensions.cs`
- `public static class AvaloniaDictionaryExtensions`
- `public static IDisposable ForEachItem<TKey, TValue>( this IAvaloniaReadOnlyDictionary<TKey, TValue> collection, Action<TKey, TValue> added, Action<TKey, TValue> removed, Action reset, bool weakSubscription = false) where TKey : notnull {`

### `src/Avalonia.Base/Collections/AvaloniaList.cs`
- `public enum ResetBehavior`
- `public AvaloniaList() {`
- `public AvaloniaList(int capacity) {`
- `public AvaloniaList(IEnumerable<T> items) {`
- `public AvaloniaList(params T[] items) {`
- `public ResetBehavior ResetBehavior { get; set; }`
- `public int Capacity {`
- `public IEnumerable<T> GetRange(int index, int count) {`
- `public struct Enumerator : IEnumerator<T>`
- `public Enumerator(List<T> inner) {`
- `public bool MoveNext() {`
- `public T Current => _innerEnumerator.Current;`

### `src/Avalonia.Base/Collections/AvaloniaListConverter.cs`
- `public class AvaloniaListConverter<[DynamicallyAccessedMembers(DynamicallyAccessedMemberTypes.All)] T> : TypeConverter`

### `src/Avalonia.Base/Collections/AvaloniaListExtensions.cs`
- `public static class AvaloniaListExtensions`
- `public static IDisposable ForEachItem<T>( this IAvaloniaReadOnlyList<T> collection, Action<T> added, Action<T> removed, Action reset, bool weakSubscription = false) {`
- `public static IDisposable ForEachItem<T>( this IAvaloniaReadOnlyList<T> collection, Action<int, T> added, Action<int, T> removed, Action reset, bool weakSubscription = false) {`
- `public static IDisposable TrackItemPropertyChanged<T>( this IAvaloniaReadOnlyList<T> collection, Action<Tuple<object?, PropertyChangedEventArgs>> callback) {`

### `src/Avalonia.Base/Collections/IAvaloniaDictionary.cs`
- `public interface IAvaloniaDictionary<TKey, TValue>`

### `src/Avalonia.Base/Collections/IAvaloniaList.cs`
- `public interface IAvaloniaList<T> : IList<T>, IAvaloniaReadOnlyList<T>`

### `src/Avalonia.Base/Collections/IAvaloniaReadOnlyDictionary.cs`
- `public interface IAvaloniaReadOnlyDictionary<TKey, TValue>`

### `src/Avalonia.Base/Collections/IAvaloniaReadOnlyList.cs`
- `public interface IAvaloniaReadOnlyList<out T> : IReadOnlyList<T>, INotifyCollectionChanged, INotifyPropertyChanged`

### `src/Avalonia.Base/Collections/NotifyCollectionChangedExtensions.cs`
- `public static class NotifyCollectionChangedExtensions`
- `public static IObservable<NotifyCollectionChangedEventArgs> GetWeakCollectionChangedObservable( this INotifyCollectionChanged collection) {`
- `public static IDisposable WeakSubscribe( this INotifyCollectionChanged collection, NotifyCollectionChangedEventHandler handler) {`
- `public static IDisposable WeakSubscribe( this INotifyCollectionChanged collection, Action<NotifyCollectionChangedEventArgs> handler) {`

### `src/Avalonia.Base/CombinedGeometry.cs`
- `public enum GeometryCombineMode`
- `public static readonly StyledProperty<Geometry?> Geometry1Property = AvaloniaProperty.Register<CombinedGeometry, Geometry?>(nameof(Geometry1));`
- `public static readonly StyledProperty<Geometry?> Geometry2Property = AvaloniaProperty.Register<CombinedGeometry, Geometry?>(nameof(Geometry2));`
- `public static readonly StyledProperty<GeometryCombineMode> GeometryCombineModeProperty = AvaloniaProperty.Register<CombinedGeometry, GeometryCombineMode>(nameof(GeometryCombineMode));`
- `public Geometry? Geometry1 {`
- `public Geometry? Geometry2 {`
- `public GeometryCombineMode GeometryCombineMode {`
- `public override Geometry Clone() {`

### `src/Avalonia.Base/Controls/Classes.cs`
- `public void Replace(IList<string> source) {`

### `src/Avalonia.Base/Controls/IResourceHost.cs`
- `public interface IResourceHost : IResourceNode`

### `src/Avalonia.Base/Controls/IResourceNode.cs`
- `public interface IResourceNode`

### `src/Avalonia.Base/Controls/IResourceProvider.cs`
- `public interface IResourceProvider : IResourceNode`

### `src/Avalonia.Base/Controls/ISetInheritanceParent.cs`
- `public interface ISetInheritanceParent`

### `src/Avalonia.Base/Controls/ISetLogicalParent.cs`
- `public interface ISetLogicalParent`

### `src/Avalonia.Base/Controls/IThemeVariantProvider.cs`
- `public interface IThemeVariantProvider : IResourceProvider`

### `src/Avalonia.Base/Controls/Metadata/PseudoClassesAttribute.cs`
- `public sealed class PseudoClassesAttribute : Attribute`
- `public PseudoClassesAttribute(params string[] pseudoClasses) {`

### `src/Avalonia.Base/Controls/NameScope.cs`
- `public static readonly AttachedProperty<INameScope> NameScopeProperty = AvaloniaProperty.RegisterAttached<NameScope, StyledElement, INameScope>("NameScope");`
- `public static INameScope GetNameScope(StyledElement styled) {`
- `public static void SetNameScope(StyledElement styled, INameScope value) {`
- `public SynchronousCompletionAsyncResult<object?> FindAsync(string name) {`

### `src/Avalonia.Base/Controls/NameScopeExtensions.cs`
- `public static T Get<T>(this INameScope nameScope, string name) where T : class {`
- `public static T Get<T>(this ILogical anchor, string name) where T : class {`
- `public static INameScope? FindNameScope(this ILogical control) {`

### `src/Avalonia.Base/Controls/NameScopeLocator.cs`
- `public class NameScopeLocator`

### `src/Avalonia.Base/Controls/PseudoClassesExtensions.cs`
- `public static class PseudolassesExtensions`

### `src/Avalonia.Base/Controls/ResourceNodeExtensions.cs`
- `public static class ResourceNodeExtensions`
- `public static bool TryFindResource(this IResourceHost control, object key, out object? value) {`
- `public static bool TryFindResource(this IResourceHost control, object key, ThemeVariant? theme, out object? value) {`
- `public static IObservable<object?> GetResourceObservable( this IResourceHost control, object key, Func<object?, object?>? converter = null) {`
- `public static IObservable<object?> GetResourceObservable( this IResourceProvider resourceProvider, object key, Func<object?, object?>? converter = null) {`
- `public static IObservable<object?> GetResourceObservable( this IResourceProvider resourceProvider, object key, ThemeVariant? defaultThemeVariant, Func<object?, object?>? converter = null) {`

### `src/Avalonia.Base/Controls/ResourceProvider.cs`
- `public abstract class ResourceProvider : AvaloniaObject, IResourceProvider`
- `public ResourceProvider() {`
- `public ResourceProvider(IResourceHost owner) {`

### `src/Avalonia.Base/Controls/Templates/ITemplateResult.cs`
- `public interface ITemplateResult`

### `src/Avalonia.Base/Controls/Templates/TemplateResult.cs`
- `public TemplateResult(T result, INameScope nameScope) {`
- `public void Deconstruct(out T result, out INameScope scope) {`

### `src/Avalonia.Base/Data/Converters/DefaultValueConverter.cs`
- `public class DefaultValueConverter : IValueConverter`

### `src/Avalonia.Base/Data/Converters/StringFormatMultiValueConverter.cs`
- `public class StringFormatMultiValueConverter : IMultiValueConverter`
- `public StringFormatMultiValueConverter(string format, IMultiValueConverter? inner) {`
- `public IMultiValueConverter? Inner { get; }`
- `public string Format { get; }`

### `src/Avalonia.Base/Data/Converters/StringFormatValueConverter.cs`
- `public class StringFormatValueConverter : IValueConverter`
- `public StringFormatValueConverter(string format, IValueConverter? inner) {`
- `public IValueConverter? Inner { get; }`
- `public string Format { get; }`

### `src/Avalonia.Base/Data/Core/ClrPropertyInfo.cs`
- `public class ClrPropertyInfo : IPropertyInfo`
- `public ClrPropertyInfo(string name, Func<object, object?>? getter, Action<object, object?>? setter, Type propertyType) {`
- `public object? Get(object target) {`
- `public bool CanSet => _setter != null;`
- `public bool CanGet => _getter != null;`
- `public class ReflectionClrPropertyInfo : ClrPropertyInfo`
- `public ReflectionClrPropertyInfo(PropertyInfo info) : base(info.Name, CreateGetter(info), CreateSetter(info), info.PropertyType) {`

### `src/Avalonia.Base/Data/Core/IPropertyInfo.cs`
- `public interface IPropertyInfo`

### `src/Avalonia.Base/Data/Core/Plugins/BindingPlugins.cs`
- `public static IList<IPropertyAccessorPlugin> PropertyAccessors => s_propertyAccessors;`
- `public static IList<IStreamPlugin> StreamHandlers => s_streamHandlers;`

### `src/Avalonia.Base/Data/Core/Plugins/DataValidationBase.cs`
- `public abstract class DataValidationBase : PropertyAccessorBase, IObserver<object?>`

### `src/Avalonia.Base/Data/Core/Plugins/ExceptionValidationPlugin.cs`
- `public class ExceptionValidationPlugin : IDataValidationPlugin`

### `src/Avalonia.Base/Data/Core/Plugins/IDataValidationPlugin.cs`
- `public interface IDataValidationPlugin`

### `src/Avalonia.Base/Data/Core/Plugins/IPropertyAccessor.cs`
- `public interface IPropertyAccessor : IDisposable`

### `src/Avalonia.Base/Data/Core/Plugins/IPropertyAccessorPlugin.cs`
- `public interface IPropertyAccessorPlugin`

### `src/Avalonia.Base/Data/Core/Plugins/IStreamPlugin.cs`
- `public interface IStreamPlugin`

### `src/Avalonia.Base/Data/Core/Plugins/IndeiValidationPlugin.cs`
- `public class IndeiValidationPlugin : IDataValidationPlugin`

### `src/Avalonia.Base/Data/Core/Plugins/PropertyAccessorBase.cs`
- `public abstract class PropertyAccessorBase : IPropertyAccessor`
- `public void Unsubscribe() {`

### `src/Avalonia.Base/Data/Core/Plugins/PropertyError.cs`
- `public class PropertyError : IPropertyAccessor`
- `public PropertyError(BindingNotification error) {`
- `public void Unsubscribe() {`

### `src/Avalonia.Base/Data/Core/PropertyPath.cs`
- `public class PropertyPath`
- `public PropertyPath(IEnumerable<IPropertyPathElement> elements) {`
- `public class PropertyPathBuilder`
- `public PropertyPathBuilder ChildTraversal() {`
- `public PropertyPathBuilder EnsureType(Type type) {`
- `public interface IPropertyPathElement`
- `public class PropertyPropertyPathElement : IPropertyPathElement`
- `public PropertyPropertyPathElement(IPropertyInfo property) {`
- `public class ChildTraversalPropertyPathElement : IPropertyPathElement`
- `public class EnsureTypePropertyPathElement : IPropertyPathElement`
- `public EnsureTypePropertyPathElement(Type type) {`
- `public class CastTypePropertyPathElement : IPropertyPathElement`
- `public CastTypePropertyPathElement(Type type) {`

### `src/Avalonia.Base/Data/Core/StreamBindingExtensions.cs`
- `public static class StreamBindingExtensions`
- `public static T StreamBinding<T>(this Task<T> @this) {`
- `public static object StreamBinding(this Task @this) {`
- `public static T StreamBinding<T>(this IObservable<T> @this) {`

### `src/Avalonia.Base/Data/Core/UntypedBindingExpressionBase.cs`
- `public abstract class UntypedBindingExpressionBase : BindingExpressionBase,`
- `public UntypedBindingExpressionBase( BindingPriority defaultPriority, AvaloniaProperty? targetProperty = null, bool isDataValidationEnabled = false) {`
- `public bool IsDataValidationEnabled => _isDataValidationEnabled;`
- `public bool IsRunning => _isRunning;`

### `src/Avalonia.Base/Diagnostics/AvaloniaObjectExtensions.cs`
- `public static ValueStoreDiagnostic GetValueStoreDiagnostic(this AvaloniaObject avaloniaObject) {`

### `src/Avalonia.Base/Diagnostics/AvaloniaPropertyValue.cs`
- `public sealed class AvaloniaPropertyValue`
- `public bool IsOverriddenCurrentValue { get; }`

### `src/Avalonia.Base/Diagnostics/IValueFrameDiagnostic.cs`
- `public record ValueEntryDiagnostic(AvaloniaProperty Property, object? Value);`
- `public interface IValueFrameDiagnostic`
- `public enum FrameType`

### `src/Avalonia.Base/Diagnostics/StyleDiagnostics.cs`
- `public class StyleDiagnostics`
- `public IReadOnlyList<AppliedStyle> AppliedStyles { get; }`
- `public StyleDiagnostics(IReadOnlyList<AppliedStyle> appliedStyles) {`
- `public sealed class AppliedStyle`
- `public bool HasActivator => _instance.HasActivator;`

### `src/Avalonia.Base/Diagnostics/ValueStoreDiagnostic.cs`
- `public class ValueStoreDiagnostic`
- `public IReadOnlyList<IValueFrameDiagnostic> AppliedFrames { get; }`

### `src/Avalonia.Base/DirectPropertyBase.cs`
- `public TValue GetUnsetValue(Type type) => GetMetadata(type).UnsetValue;`
- `public TValue GetUnsetValue(AvaloniaObject owner) => GetMetadata(owner).UnsetValue;`
- `public class DirectPropertyMetadata<TValue> : AvaloniaPropertyMetadata, IDirectPropertyMetadata`
- `public DirectPropertyMetadata( TValue unsetValue = default!, BindingMode defaultBindingMode = BindingMode.Default, bool? enableDataValidation = null) : base(defaultBindingMode, enableDataValidation) {`

### `src/Avalonia.Base/IDataContextProvider.cs`
- `public interface IDataContextProvider`

### `src/Avalonia.Base/IDescription.cs`
- `public interface IDescription`

### `src/Avalonia.Base/IDirectPropertyMetadata.cs`
- `public interface IDirectPropertyMetadata`

### `src/Avalonia.Base/INamed.cs`
- `public interface INamed`

### `src/Avalonia.Base/IStyledPropertyMetadata.cs`
- `public interface IStyledPropertyMetadata`

### `src/Avalonia.Base/Input/AsyncDataTransferExtensions.cs`
- `public static class AsyncDataTransferExtensions`
- `public static IEnumerable<IAsyncDataTransferItem> GetItems(this IAsyncDataTransfer dataTransfer, DataFormat format) {`
- `public static Task<T?> TryGetValueAsync<T>(this IAsyncDataTransfer dataTransfer, DataFormat<T> format) where T : class => dataTransfer.GetItems(format).FirstOrDefault() is { } item ?`
- `public static async Task<T[]?> TryGetValuesAsync<T>(this IAsyncDataTransfer dataTransfer, DataFormat<T> format) where T : class {`

### `src/Avalonia.Base/Input/AsyncDataTransferItemExtensions.cs`
- `public static class AsyncDataTransferItemExtensions`
- `public static async Task<T?> TryGetValueAsync<T>(this IAsyncDataTransferItem dataTransferItem, DataFormat<T> format) where T : class => await dataTransferItem.TryGetRawAsync(format).ConfigureAwait(false) as T;`

### `src/Avalonia.Base/Input/DataFormat.cs`
- `public string Identifier { get; }`
- `public static DataFormat<IStorageItem> File { get; } = CreateUniversalFormat<IStorageItem>("File");`
- `public string ToSystemName(string applicationPrefix) {`
- `public static DataFormat<byte[]> CreateBytesApplicationFormat(string identifier) => CreateApplicationFormat<byte[]>(identifier);`
- `public static DataFormat<string> CreateStringApplicationFormat(string identifier) => CreateApplicationFormat<string>(identifier);`
- `public static DataFormat<byte[]> CreateBytesPlatformFormat(string identifier) => CreatePlatformFormat<byte[]>(identifier);`
- `public static DataFormat<string> CreateStringPlatformFormat(string identifier) => CreatePlatformFormat<string>(identifier);`
- `public static DataFormat<T> FromSystemName<T>(string systemName, string applicationPrefix) where T : class {`

### `src/Avalonia.Base/Input/DataFormatKind.cs`
- `public enum DataFormatKind`

### `src/Avalonia.Base/Input/DataFormats.cs`
- `public static readonly string FileNames = nameof(FileNames);`

### `src/Avalonia.Base/Input/DataObject.cs`
- `public object? Get(string dataFormat) {`
- `public IEnumerable<string> GetDataFormats() {`

### `src/Avalonia.Base/Input/DataObjectExtensions.cs`
- `public static class DataObjectExtensions`
- `public static IEnumerable<IStorageItem>? GetFiles(this IDataObject dataObject) {`
- `public static IEnumerable<string>? GetFileNames(this IDataObject dataObject) {`
- `public static string? GetText(this IDataObject dataObject) {`

### `src/Avalonia.Base/Input/DataTransfer.cs`
- `public IReadOnlyList<DataFormat> Formats {`

### `src/Avalonia.Base/Input/DataTransferExtensions.cs`
- `public static IEnumerable<IDataTransferItem> GetItems(this IDataTransfer dataTransfer, DataFormat format) {`
- `public static T[]? TryGetValues<T>(this IDataTransfer dataTransfer, DataFormat<T> format) where T : class {`
- `public static IStorageItem? TryGetFile(this IDataTransfer dataTransfer) => dataTransfer.TryGetValue(DataFormat.File);`
- `public static Bitmap? TryGetBitmap(this IDataTransfer dataTransfer) => dataTransfer.TryGetValue(DataFormat.Bitmap);`

### `src/Avalonia.Base/Input/DataTransferItem.cs`
- `public IReadOnlyList<DataFormat> Formats {`
- `public object? TryGetRaw(DataFormat format) => FindAccessor(format)?.GetValue();`
- `public void SetBitmap(Bitmap? value) => Set(DataFormat.Bitmap, value);`

### `src/Avalonia.Base/Input/DataTransferItemExtensions.cs`
- `public static class DataTransferItemExtensions`
- `public static IStorageItem? TryGetFile(this IDataTransferItem dataTransferItem) => dataTransferItem.TryGetValue(DataFormat.File);`
- `public static Bitmap? TryGetBitmap(this IDataTransferItem dataTransferItem) => dataTransferItem.TryGetValue(DataFormat.Bitmap);`

### `src/Avalonia.Base/Input/DragDrop.cs`
- `public static bool GetAllowDrop(Interactive interactive) {`
- `public static void AddDragEnterHandler(Interactive element, EventHandler<DragEventArgs> handler) {`
- `public static void RemoveDragEnterHandler(Interactive element, EventHandler<DragEventArgs> handler) {`
- `public static void AddDragLeaveHandler(Interactive element, EventHandler<DragEventArgs> handler) {`
- `public static void RemoveDragLeaveHandler(Interactive element, EventHandler<DragEventArgs> handler) {`
- `public static void RemoveDragOverHandler(Interactive element, EventHandler<DragEventArgs> handler) {`
- `public static void RemoveDropHandler(Interactive element, EventHandler<DragEventArgs> handler) {`

### `src/Avalonia.Base/Input/DragDropDevice.cs`
- `public class DragDropDevice : IDragDropDevice`
- `public void ProcessRawEvent(RawInputEventArgs e) {`

### `src/Avalonia.Base/Input/FocusManager.cs`
- `public void ClearFocusOnElementRemoved(IInputElement removedElement, Visual oldParent) {`
- `public void SetFocusScope(IFocusScope scope) {`
- `public void RemoveFocusRoot(IFocusScope scope) {`
- `public static bool GetIsFocusScope(IInputElement e) => e is IFocusScope;`

### `src/Avalonia.Base/Input/GestureRecognizers/GestureRecognizerCollection.cs`
- `public class GestureRecognizerCollection : IReadOnlyCollection<GestureRecognizer>`
- `public GestureRecognizerCollection(IInputElement inputElement) {`

### `src/Avalonia.Base/Input/GestureRecognizers/ScrollGestureRecognizer.cs`
- `public const double InertialResistance = 0.15;`
- `public static readonly DirectProperty<ScrollGestureRecognizer, bool> IsScrollInertiaEnabledProperty = AvaloniaProperty.RegisterDirect<ScrollGestureRecognizer, bool>(nameof(IsScrollInertiaEnabled), o => o.IsScrollInertiaEnabled, (o,v) => o.IsScrollInertiaEnabled = v);`
- `public static readonly DirectProperty<ScrollGestureRecognizer, int> ScrollStartDistanceProperty = AvaloniaProperty.RegisterDirect<ScrollGestureRecognizer, int>(nameof(ScrollStartDistance), o => o.ScrollStartDistance, (o, v) => o.ScrollStartDistance = v,`
- `public int ScrollStartDistance {`

### `src/Avalonia.Base/Input/Gestures.cs`
- `public static readonly AttachedProperty<bool> IsHoldingEnabledProperty = AvaloniaProperty.RegisterAttached<StyledElement, bool>("IsHoldingEnabled", typeof(Gestures), true);`
- `public static readonly AttachedProperty<bool> IsHoldWithMouseEnabledProperty = AvaloniaProperty.RegisterAttached<StyledElement, bool>("IsHoldWithMouseEnabled", typeof(Gestures), false);`
- `public static readonly RoutedEvent<TappedEventArgs> RightTappedEvent = RoutedEvent.Register<TappedEventArgs>( "RightTapped", RoutingStrategies.Bubble, typeof(Gestures));`
- `public static readonly RoutedEvent<ScrollGestureInertiaStartingEventArgs> ScrollGestureInertiaStartingEvent = RoutedEvent.Register<ScrollGestureInertiaStartingEventArgs>( "ScrollGestureInertiaStarting", RoutingStrategies.Bubble, typeof(Gestures));`
- `public static readonly RoutedEvent<ScrollGestureEndedEventArgs> ScrollGestureEndedEvent = RoutedEvent.Register<ScrollGestureEndedEventArgs>( "ScrollGestureEnded", RoutingStrategies.Bubble, typeof(Gestures));`
- `public static readonly RoutedEvent<PointerDeltaEventArgs> PointerTouchPadGestureMagnifyEvent = RoutedEvent.Register<PointerDeltaEventArgs>( "PointerTouchPadGestureMagnify", RoutingStrategies.Bubble, typeof(Gestures));`
- `public static readonly RoutedEvent<PointerDeltaEventArgs> PointerTouchPadGestureRotateEvent = RoutedEvent.Register<PointerDeltaEventArgs>( "PointerTouchPadGestureRotate", RoutingStrategies.Bubble, typeof(Gestures));`
- `public static readonly RoutedEvent<PointerDeltaEventArgs> PointerTouchPadGestureSwipeEvent = RoutedEvent.Register<PointerDeltaEventArgs>( "PointerTouchPadGestureSwipe", RoutingStrategies.Bubble, typeof(Gestures));`
- `public static readonly RoutedEvent<PinchEndedEventArgs> PinchEndedEvent = RoutedEvent.Register<PinchEndedEventArgs>( "PinchEnded", RoutingStrategies.Bubble, typeof(Gestures));`
- `public static readonly RoutedEvent<PullGestureEventArgs> PullGestureEvent = RoutedEvent.Register<PullGestureEventArgs>( "PullGesture", RoutingStrategies.Bubble, typeof(Gestures));`
- `public static readonly RoutedEvent<PullGestureEndedEventArgs> PullGestureEndedEvent = RoutedEvent.Register<PullGestureEndedEventArgs>( "PullGestureEnded", RoutingStrategies.Bubble, typeof(Gestures));`
- `public static bool GetIsHoldingEnabled(StyledElement element) {`
- `public static void SetIsHoldingEnabled(StyledElement element, bool value) {`
- `public static bool GetIsHoldWithMouseEnabled(StyledElement element) {`
- `public static void SetIsHoldWithMouseEnabled(StyledElement element, bool value) {`
- `public static void AddDoubleTappedHandler(Interactive element, EventHandler<RoutedEventArgs> handler) {`
- `public static void AddRightTappedHandler(Interactive element, EventHandler<RoutedEventArgs> handler) {`
- `public static void AddPinchEndedHandler(Interactive element, EventHandler<PinchEndedEventArgs> handler) =>`
- `public static void AddPullGestureHandler(Interactive element, EventHandler<PullGestureEventArgs> handler) =>`
- `public static void AddPullGestureEndedHandler(Interactive element, EventHandler<PullGestureEndedEventArgs> handler) =>`
- `public static void AddPointerTouchPadGestureMagnifyHandler(Interactive element, EventHandler<PointerDeltaEventArgs> handler) =>`
- `public static void AddPointerTouchPadGestureRotateHandler(Interactive element, EventHandler<PointerDeltaEventArgs> handler) =>`
- `public static void AddPointerTouchPadGestureSwipeHandler(Interactive element, EventHandler<PointerDeltaEventArgs> handler) =>`
- `public static void AddScrollGestureHandler(Interactive element, EventHandler<RoutedEventArgs> handler) =>`
- `public static void AddScrollGestureEndedHandler(Interactive element, EventHandler<ScrollGestureEndedEventArgs> handler) =>`
- `public static void AddScrollGestureInertiaStartingHandler(Interactive element, EventHandler<ScrollGestureInertiaStartingEventArgs> handler) =>`
- `public static void RemoveTappedHandler(Interactive element, EventHandler<RoutedEventArgs> handler) {`
- `public static void RemoveDoubleTappedHandler(Interactive element, EventHandler<RoutedEventArgs> handler) {`
- `public static void RemoveRightTappedHandler(Interactive element, EventHandler<RoutedEventArgs> handler) {`
- `public static void RemoveHoldingHandler(Interactive element, EventHandler<RoutedEventArgs> handler) =>`
- `public static void RemovePinchHandler(Interactive element, EventHandler<PinchEventArgs> handler) =>`
- `public static void RemovePinchEndedHandler(Interactive element, EventHandler<PinchEndedEventArgs> handler) =>`
- `public static void RemovePullGestureHandler(Interactive element, EventHandler<PullGestureEventArgs> handler) =>`
- `public static void RemovePullGestureEndedHandler(Interactive element, EventHandler<PullGestureEndedEventArgs> handler) =>`
- `public static void RemovePointerTouchPadGestureMagnifyHandler(Interactive element, EventHandler<PointerDeltaEventArgs> handler) =>`
- `public static void RemovePointerTouchPadGestureRotateHandler(Interactive element, EventHandler<PointerDeltaEventArgs> handler) =>`
- `public static void RemovePointerTouchPadGestureSwipeHandler(Interactive element, EventHandler<PointerDeltaEventArgs> handler) =>`
- `public static void RemoveScrollGestureHandler(Interactive element, EventHandler<ScrollGestureEventArgs> handler) =>`
- `public static void RemoveScrollGestureEndedHandler(Interactive element,EventHandler<ScrollGestureEndedEventArgs> handler) =>`
- `public static void RemoveScrollGestureInertiaStartingHandler(Interactive element, EventHandler<ScrollGestureInertiaStartingEventArgs> handler) =>`

### `src/Avalonia.Base/Input/IAsyncDataTransferItem.cs`
- `public interface IAsyncDataTransferItem`

### `src/Avalonia.Base/Input/ICloseable.cs`
- `public interface ICloseable`

### `src/Avalonia.Base/Input/IDataTransferItem.cs`
- `public interface IDataTransferItem`

### `src/Avalonia.Base/Input/IInputDevice.cs`
- `public interface IInputDevice`

### `src/Avalonia.Base/Input/IInputManager.cs`
- `public interface IInputManager`

### `src/Avalonia.Base/Input/IKeyboardDevice.cs`
- `public enum KeyStates`
- `public enum RawInputModifiers`
- `public interface IKeyboardDevice : IInputDevice`

### `src/Avalonia.Base/Input/IKeyboardNavigationHandler.cs`
- `public interface IKeyboardNavigationHandler`

### `src/Avalonia.Base/Input/IMouseDevice.cs`
- `public interface IMouseDevice : IPointerDevice`

### `src/Avalonia.Base/Input/IPenDevice.cs`
- `public interface IPenDevice : IPointerDevice`

### `src/Avalonia.Base/Input/IPointer.cs`
- `public interface IPointer`

### `src/Avalonia.Base/Input/IPointerDevice.cs`
- `public interface IPointerDevice : IInputDevice`

### `src/Avalonia.Base/Input/InputElement.cs`
- `public static readonly StyledProperty<bool> FocusableProperty = AvaloniaProperty.Register<InputElement, bool>(nameof(Focusable));`
- `public static readonly StyledProperty<bool> IsEnabledProperty = AvaloniaProperty.Register<InputElement, bool>(nameof(IsEnabled), true);`
- `public static readonly DirectProperty<InputElement, bool> IsEffectivelyEnabledProperty = AvaloniaProperty.RegisterDirect<InputElement, bool>( nameof(IsEffectivelyEnabled), o => o.IsEffectivelyEnabled);`
- `public static readonly StyledProperty<Cursor?> CursorProperty = AvaloniaProperty.Register<InputElement, Cursor?>(nameof(Cursor), null, true);`
- `public static readonly DirectProperty<InputElement, bool> IsKeyboardFocusWithinProperty = AvaloniaProperty.RegisterDirect<InputElement, bool>( nameof(IsKeyboardFocusWithin), o => o.IsKeyboardFocusWithin);`
- `public static readonly DirectProperty<InputElement, bool> IsFocusedProperty = AvaloniaProperty.RegisterDirect<InputElement, bool>(nameof(IsFocused), o => o.IsFocused);`
- `public static readonly StyledProperty<bool> IsHitTestVisibleProperty = AvaloniaProperty.Register<InputElement, bool>(nameof(IsHitTestVisible), true);`
- `public static readonly DirectProperty<InputElement, bool> IsPointerOverProperty = AvaloniaProperty.RegisterDirect<InputElement, bool>(nameof(IsPointerOver), o => o.IsPointerOver);`
- `public static readonly RoutedEvent<GotFocusEventArgs> GotFocusEvent = RoutedEvent.Register<InputElement, GotFocusEventArgs>(nameof(GotFocus), RoutingStrategies.Bubble);`
- `public static readonly RoutedEvent<RoutedEventArgs> LostFocusEvent = RoutedEvent.Register<InputElement, RoutedEventArgs>(nameof(LostFocus), RoutingStrategies.Bubble);`
- `public static readonly StyledProperty<int> TabIndexProperty = KeyboardNavigation.TabIndexProperty.AddOwner<InputElement>();`
- `public static readonly RoutedEvent<PointerEventArgs> PointerEnteredEvent = RoutedEvent.Register<InputElement, PointerEventArgs>( nameof(PointerEntered), RoutingStrategies.Direct);`
- `public static readonly RoutedEvent<PointerEventArgs> PointerExitedEvent = RoutedEvent.Register<InputElement, PointerEventArgs>( nameof(PointerExited), RoutingStrategies.Direct);`
- `public static readonly RoutedEvent<PointerCaptureLostEventArgs> PointerCaptureLostEvent = RoutedEvent.Register<InputElement, PointerCaptureLostEventArgs>( nameof(PointerCaptureLost), RoutingStrategies.Direct);`
- `public event EventHandler<KeyEventArgs>? KeyUp {`
- `public event EventHandler<TextInputMethodClientRequestedEventArgs>? TextInputMethodClientRequested {`
- `public event EventHandler<PointerCaptureLostEventArgs>? PointerCaptureLost {`
- `public event EventHandler<PointerWheelEventArgs>? PointerWheelChanged {`
- `public Cursor? Cursor {`
- `public bool IsKeyboardFocusWithin {`
- `public bool IsFocused {`
- `public bool IsPointerOver {`

### `src/Avalonia.Base/Input/InputExtensions.cs`
- `public static class InputExtensions`
- `public static IEnumerable<IInputElement> GetInputElementsAt(this IInputElement element, Point p, bool enabledElementsOnly = true) {`
- `public static IEnumerable<IInputElement> GetInputElementsAt(this IInputElement element, Point p) => GetInputElementsAt(element, p, true);`
- `public static IInputElement? InputHitTest(this IInputElement element, Point p, bool enabledElementsOnly = true) {`
- `public static IInputElement? InputHitTest(this IInputElement element, Point p) => InputHitTest(element, p, true);`
- `public static IInputElement? InputHitTest( this IInputElement element, Point p, Func<Visual, bool> filter, bool enabledElementsOnly = true) {`
- `public static IInputElement? InputHitTest(this IInputElement element, Point p, Func<Visual, bool> filter) => InputHitTest(element, p, filter, true);`

### `src/Avalonia.Base/Input/InputMethod.cs`
- `public class InputMethod`
- `public static readonly AvaloniaProperty<bool> IsInputMethodEnabledProperty = AvaloniaProperty.RegisterAttached<InputMethod, InputElement, bool>("IsInputMethodEnabled", true);`
- `public static void SetIsInputMethodEnabled(InputElement target, bool value) {`
- `public static bool GetIsInputMethodEnabled(InputElement target) {`
- `public static readonly RoutedEvent<TextInputMethodClientRequeryRequestedEventArgs> TextInputMethodClientRequeryRequestedEvent = RoutedEvent.Register<InputElement, TextInputMethodClientRequeryRequestedEventArgs>( "TextInputMethodClientRequeryRequested", RoutingStrategies.Bubble);`
- `public static void AddTextInputMethodClientRequeryRequestedHandler(Interactive element, EventHandler<RoutedEventArgs> handler) {`
- `public static void RemoveTextInputMethodClientRequeryRequestedHandler(Interactive element, EventHandler<RoutedEventArgs> handler) {`

### `src/Avalonia.Base/Input/KeyDeviceType.cs`
- `public enum KeyDeviceType`

### `src/Avalonia.Base/Input/KeyEventArgs.cs`
- `public string? KeySymbol { get; init; }`
- `public KeyDeviceType KeyDeviceType { get; init; }`

### `src/Avalonia.Base/Input/KeyboardDevice.cs`
- `public class KeyboardDevice : IKeyboardDevice, INotifyPropertyChanged`
- `public IInputManager? InputManager => AvaloniaLocator.Current.GetService<IInputManager>();`
- `public IInputElement? FocusedElement => _focusedElement;`
- `public void SetFocusedElement( IInputElement? element, NavigationMethod method, KeyModifiers keyModifiers) {`
- `public void ProcessRawEvent(RawInputEventArgs e) {`

### `src/Avalonia.Base/Input/KeyboardNavigation.cs`
- `public static readonly AttachedProperty<int> TabIndexProperty = AvaloniaProperty.RegisterAttached<StyledElement, int>( "TabIndex", typeof(KeyboardNavigation), int.MaxValue);`
- `public static int GetTabIndex(IInputElement element) {`
- `public static KeyboardNavigationMode GetTabNavigation(InputElement element) {`
- `public static IInputElement? GetTabOnceActiveElement(InputElement element) {`
- `public static void SetTabOnceActiveElement(InputElement element, IInputElement? value) {`
- `public static void SetIsTabStop(InputElement element, bool value) {`
- `public static bool GetIsTabStop(InputElement element) {`

### `src/Avalonia.Base/Input/KeyboardNavigationHandler.cs`
- `public sealed class KeyboardNavigationHandler : IKeyboardNavigationHandler`
- `public void SetOwner(IInputRoot owner) {`
- `public static IInputElement? GetNext( IInputElement element, NavigationDirection direction) {`

### `src/Avalonia.Base/Input/MouseDevice.cs`
- `public class MouseDevice : IMouseDevice, IDisposable`
- `public MouseDevice(Pointer? pointer = null) {`
- `public void ProcessRawEvent(RawInputEventArgs e) {`
- `public IPointer? TryGetPointer(RawPointerEventArgs ev) {`

### `src/Avalonia.Base/Input/Navigation/XYFocus.Properties.cs`
- `public static void SetDown(InputElement obj, InputElement value) => obj.SetValue(DownProperty, value);`
- `public static InputElement GetDown(InputElement obj) => obj.GetValue(DownProperty);`
- `public static void SetUp(InputElement obj, InputElement value) => obj.SetValue(UpProperty, value);`
- `public static InputElement GetUp(InputElement obj) => obj.GetValue(UpProperty);`
- `public static readonly AttachedProperty<XYFocusNavigationStrategy> DownNavigationStrategyProperty = AvaloniaProperty.RegisterAttached<XYFocus, InputElement, XYFocusNavigationStrategy>( "DownNavigationStrategy", inherits: true);`
- `public static void SetDownNavigationStrategy(InputElement obj, XYFocusNavigationStrategy value) =>`
- `public static XYFocusNavigationStrategy GetDownNavigationStrategy(InputElement obj) =>`
- `public static readonly AttachedProperty<XYFocusNavigationStrategy> UpNavigationStrategyProperty = AvaloniaProperty.RegisterAttached<XYFocus, InputElement, XYFocusNavigationStrategy>( "UpNavigationStrategy", inherits: true);`
- `public static void SetUpNavigationStrategy(InputElement obj, XYFocusNavigationStrategy value) =>`
- `public static XYFocusNavigationStrategy GetUpNavigationStrategy(InputElement obj) =>`
- `public static readonly AttachedProperty<XYFocusNavigationStrategy> LeftNavigationStrategyProperty = AvaloniaProperty.RegisterAttached<XYFocus, InputElement, XYFocusNavigationStrategy>( "LeftNavigationStrategy", inherits: true);`
- `public static void SetLeftNavigationStrategy(InputElement obj, XYFocusNavigationStrategy value) =>`
- `public static XYFocusNavigationStrategy GetLeftNavigationStrategy(InputElement obj) =>`
- `public static readonly AttachedProperty<XYFocusNavigationStrategy> RightNavigationStrategyProperty = AvaloniaProperty.RegisterAttached<XYFocus, InputElement, XYFocusNavigationStrategy>( "RightNavigationStrategy", inherits: true);`
- `public static void SetRightNavigationStrategy(InputElement obj, XYFocusNavigationStrategy value) =>`
- `public static XYFocusNavigationStrategy GetRightNavigationStrategy(InputElement obj) =>`
- `public static void SetNavigationModes(InputElement obj, XYFocusNavigationModes value) =>`
- `public static XYFocusNavigationModes GetNavigationModes(InputElement obj) =>`

### `src/Avalonia.Base/Input/Navigation/XYFocusNavigationModes.cs`
- `public enum XYFocusNavigationModes`

### `src/Avalonia.Base/Input/Navigation/XYFocusNavigationStrategy.cs`
- `public enum XYFocusNavigationStrategy`

### `src/Avalonia.Base/Input/NavigationDirection.cs`
- `public static class NavigationDirectionExtensions`
- `public static bool IsTab(this NavigationDirection direction) {`
- `public static bool IsDirectional(this NavigationDirection direction) {`
- `public static NavigationDirection? ToNavigationDirection( this Key key, KeyModifiers modifiers = KeyModifiers.None) {`

### `src/Avalonia.Base/Input/PenDevice.cs`
- `public class PenDevice : IPenDevice, IDisposable`
- `public PenDevice(bool releasePointerOnPenUp = false) {`
- `public void ProcessRawEvent(RawInputEventArgs e) {`
- `public IPointer? TryGetPointer(RawPointerEventArgs ev) {`

### `src/Avalonia.Base/Input/PhysicalKeyExtensions.cs`
- `public static class PhysicalKeyExtensions`
- `public static Key ToQwertyKey(this PhysicalKey physicalKey) => physicalKey switch`
- `public static string? ToQwertyKeySymbol(this PhysicalKey physicalKey, bool useShiftModifier = false) => physicalKey switch`

### `src/Avalonia.Base/Input/PinchEventArgs.cs`
- `public class PinchEventArgs : RoutedEventArgs`
- `public PinchEventArgs(double scale, Point scaleOrigin) : base(Gestures.PinchEvent) {`
- `public PinchEventArgs(double scale, Point scaleOrigin, double angle, double angleDelta) : base(Gestures.PinchEvent) {`
- `public double Scale { get; } = 1;`
- `public Point ScaleOrigin { get; }`
- `public double Angle { get; }`
- `public double AngleDelta { get; }`
- `public class PinchEndedEventArgs : RoutedEventArgs`
- `public PinchEndedEventArgs() : base(Gestures.PinchEndedEvent) {`

### `src/Avalonia.Base/Input/Platform/ClipboardExtensions.cs`
- `public static async Task<IReadOnlyList<DataFormat>> GetDataFormatsAsync(this IClipboard clipboard) {`
- `public static async Task<T?> TryGetValueAsync<T>(this IClipboard clipboard, DataFormat<T> format) where T : class {`
- `public static async Task<T[]?> TryGetValuesAsync<T>(this IClipboard clipboard, DataFormat<T> format) where T : class {`
- `public static Task SetValueAsync<T>(this IClipboard clipboard, DataFormat<T> format, T? value) where T : class {`
- `public static Task SetValuesAsync<T>(this IClipboard clipboard, DataFormat<T> format, IEnumerable<T>? values) where T : class {`
- `public static Task SetFilesAsync(this IClipboard clipboard, IEnumerable<IStorageItem>? files) => clipboard.SetValuesAsync(DataFormat.File, files);`

### `src/Avalonia.Base/Input/Platform/IClipboardImpl.cs`
- `public interface IClipboardImpl`

### `src/Avalonia.Base/Input/Platform/IFlushableClipboardImpl.cs`
- `public interface IFlushableClipboardImpl : IClipboardImpl`

### `src/Avalonia.Base/Input/Platform/IOwnedClipboardImpl.cs`
- `public interface IOwnedClipboardImpl : IClipboardImpl`

### `src/Avalonia.Base/Input/Platform/IPlatformDragSource.cs`
- `public interface IPlatformDragSource`

### `src/Avalonia.Base/Input/Platform/KeyGestureFormatInfo.cs`
- `public sealed class KeyGestureFormatInfo(IReadOnlyDictionary<Key, string>? platformKeyOverrides = null,`
- `public static KeyGestureFormatInfo Invariant { get; } = new();`
- `public string Meta { get; } = meta;`
- `public string Ctrl { get; } = ctrl;`
- `public string Alt { get; } = alt;`
- `public string Shift { get; } = shift;`
- `public object? GetFormat(Type? formatType) => formatType == typeof(KeyGestureFormatInfo) ? this : null;`
- `public static KeyGestureFormatInfo GetInstance(IFormatProvider? formatProvider) => formatProvider?.GetFormat(typeof(KeyGestureFormatInfo)) as KeyGestureFormatInfo`
- `public string FormatKey(Key key) {`

### `src/Avalonia.Base/Input/Platform/PlatformHotkeyConfiguration.cs`
- `public sealed class PlatformHotkeyConfiguration`
- `public PlatformHotkeyConfiguration() : this(KeyModifiers.Control) {`
- `public PlatformHotkeyConfiguration(KeyModifiers commandModifiers, KeyModifiers selectionModifiers = KeyModifiers.Shift, KeyModifiers wholeWordTextActionModifiers = KeyModifiers.Control) {`
- `public KeyModifiers CommandModifiers { get; set; }`
- `public KeyModifiers WholeWordTextActionModifiers { get; set; }`
- `public KeyModifiers SelectionModifiers { get; set; }`
- `public List<KeyGesture> MoveCursorToTheStartOfLine { get; set; }`
- `public List<KeyGesture> MoveCursorToTheEndOfLine { get; set; }`
- `public List<KeyGesture> MoveCursorToTheStartOfDocument { get; set; }`
- `public List<KeyGesture> MoveCursorToTheEndOfDocument { get; set; }`
- `public List<KeyGesture> MoveCursorToTheStartOfLineWithSelection { get; set; }`
- `public List<KeyGesture> MoveCursorToTheEndOfLineWithSelection { get; set; }`
- `public List<KeyGesture> MoveCursorToTheStartOfDocumentWithSelection { get; set; }`
- `public List<KeyGesture> MoveCursorToTheEndOfDocumentWithSelection { get; set; }`
- `public List<KeyGesture> OpenContextMenu { get; set; }`
- `public List<KeyGesture> Back { get; set; }`

### `src/Avalonia.Base/Input/Pointer.cs`
- `public static int GetNextFreeId() => s_NextFreePointerId++;`
- `public int Id { get; }`
- `public void Capture(IInputElement? control) {`
- `public IInputElement? Captured { get; private set; }`
- `public bool IsGestureRecognitionSkipped { get; set; }`

### `src/Avalonia.Base/Input/PointerDeltaEventArgs.cs`
- `public class PointerDeltaEventArgs : PointerEventArgs`
- `public PointerDeltaEventArgs(RoutedEvent routedEvent, object? source, IPointer pointer, Visual rootVisual, Point rootVisualPosition, ulong timestamp, PointerPointProperties properties, KeyModifiers modifiers, Vector delta) : base(routedEvent, source, pointer, rootVisual, rootVisualPosition, timestamp, properties, modifiers) {`

### `src/Avalonia.Base/Input/PointerEventArgs.cs`
- `public ulong Timestamp { get; }`
- `public IReadOnlyList<PointerPoint> GetIntermediatePoints(Visual? relativeTo) {`
- `public int ClickCount { get; }`
- `public MouseButton InitialPressMouseButton { get; }`
- `public class PointerCaptureLostEventArgs : RoutedEventArgs`
- `public PointerCaptureLostEventArgs(object source, IPointer pointer) : base(InputElement.PointerCaptureLostEvent) {`

### `src/Avalonia.Base/Input/PointerPoint.cs`
- `public record struct PointerPoint`
- `public PointerPoint(IPointer pointer, Point position, PointerPointProperties properties) {`
- `public record struct PointerPointProperties`
- `public Rect ContactRect { get; }`
- `public bool IsMiddleButtonPressed { get; } = false;`
- `public bool IsRightButtonPressed { get; } = false;`
- `public bool IsXButton1Pressed { get; } = false;`
- `public bool IsXButton2Pressed { get; } = false;`
- `public bool IsBarrelButtonPressed { get; } = false;`
- `public bool IsEraser { get; } = false;`
- `public bool IsInverted { get; } = false;`
- `public float Twist { get; } = 0.0F;`
- `public float Pressure { get; } = 0.5f;`
- `public float XTilt { get; } = 0.0F;`
- `public float YTilt { get; } = 0.0F;`
- `public PointerUpdateKind PointerUpdateKind { get; } = PointerUpdateKind.LeftButtonPressed;`
- `public PointerPointProperties() {`
- `public PointerPointProperties(RawInputModifiers modifiers, PointerUpdateKind kind) {`
- `public PointerPointProperties(RawInputModifiers modifiers, PointerUpdateKind kind, float twist, float pressure, float xTilt, float yTilt) : this(modifiers, kind, twist, pressure, xTilt, yTilt, default) {`
- `public PointerPointProperties(RawInputModifiers modifiers, PointerUpdateKind kind, float twist, float pressure, float xTilt, float yTilt, Rect contactRect) : this(modifiers, kind) {`
- `public enum PointerUpdateKind`
- `public static class PointerUpdateKindExtensions`
- `public static MouseButton GetMouseButton(this PointerUpdateKind kind) {`

### `src/Avalonia.Base/Input/PointerWheelEventArgs.cs`
- `public class PointerWheelEventArgs : PointerEventArgs`
- `public PointerWheelEventArgs(object source, IPointer pointer, Visual rootVisual, Point rootVisualPosition, ulong timestamp, PointerPointProperties properties, KeyModifiers modifiers, Vector delta) : base(InputElement.PointerWheelChangedEvent, source, pointer, rootVisual, rootVisualPosition, timestamp, properties, modifiers) {`

### `src/Avalonia.Base/Input/PullGestureEventArgs.cs`
- `public class PullGestureEventArgs : RoutedEventArgs`
- `public int Id { get; }`
- `public PullGestureEventArgs(int id, Vector delta, PullDirection pullDirection) : base(Gestures.PullGestureEvent) {`
- `public class PullGestureEndedEventArgs : RoutedEventArgs`
- `public PullGestureEndedEventArgs(int id, PullDirection pullDirection) : base(Gestures.PullGestureEndedEvent) {`

### `src/Avalonia.Base/Input/Raw/IDragDropDevice.cs`
- `public interface IDragDropDevice : IInputDevice`

### `src/Avalonia.Base/Input/Raw/RawDragEvent.cs`
- `public class RawDragEvent : RawInputEventArgs`
- `public DragDropEffects Effects { get; set; }`
- `public RawDragEvent(IDragDropDevice inputDevice, RawDragEventType type, IInputRoot root, Point location, IDataObject data, DragDropEffects effects, RawInputModifiers modifiers) : this(inputDevice, type, root, location, new DataObjectToDataTransferWrapper(data), effects, modifiers) {`
- `public RawDragEvent( IDragDropDevice inputDevice, RawDragEventType type, IInputRoot root, Point location, IDataTransfer dataTransfer, DragDropEffects effects, RawInputModifiers modifiers) : base(inputDevice, 0, root) {`

### `src/Avalonia.Base/Input/Raw/RawDragEventType.cs`
- `public enum RawDragEventType`

### `src/Avalonia.Base/Input/Raw/RawInputEventArgs.cs`
- `public class RawInputEventArgs : EventArgs`
- `public RawInputEventArgs(IInputDevice device, ulong timestamp, IInputRoot root) {`
- `public IInputRoot Root { get; }`
- `public ulong Timestamp { get; set; }`

### `src/Avalonia.Base/Input/Raw/RawKeyEventArgs.cs`
- `public enum RawKeyEventType`
- `public class RawKeyEventArgs : RawInputEventArgs`
- `public RawKeyEventArgs( IKeyboardDevice device, ulong timestamp, IInputRoot root, RawKeyEventType type, Key key, RawInputModifiers modifiers) : this(device, timestamp, root, type, key, modifiers, PhysicalKey.None, KeyDeviceType.Keyboard, null) {`
- `public RawKeyEventArgs( IInputDevice device, ulong timestamp, IInputRoot root, RawKeyEventType type, Key key, RawInputModifiers modifiers, PhysicalKey physicalKey, string? keySymbol) : this(device, timestamp, root, type, key, modifiers, physicalKey, KeyDeviceType.Keyboard, keySymbol) { }`
- `public RawKeyEventArgs( IInputDevice device, ulong timestamp, IInputRoot root, RawKeyEventType type, Key key, RawInputModifiers modifiers, PhysicalKey physicalKey, KeyDeviceType keyDeviceType, string? keySymbol) : base(device, timestamp, root) {`
- `public KeyDeviceType KeyDeviceType { get; set; }`
- `public string? KeySymbol { get; set; }`

### `src/Avalonia.Base/Input/Raw/RawMouseWheelEventArgs.cs`
- `public class RawMouseWheelEventArgs : RawPointerEventArgs`
- `public RawMouseWheelEventArgs( IInputDevice device, ulong timestamp, IInputRoot root, Point position, Vector delta, RawInputModifiers inputModifiers) : base(device, timestamp, root, RawPointerEventType.Wheel, position, inputModifiers) {`

### `src/Avalonia.Base/Input/Raw/RawPointerEventArgs.cs`
- `public enum RawPointerEventType`
- `public class RawPointerEventArgs : RawInputEventArgs`
- `public RawPointerEventArgs( IInputDevice device, ulong timestamp, IInputRoot root, RawPointerEventType type, Point position, RawInputModifiers inputModifiers) : base(device, timestamp, root) {`
- `public RawPointerEventArgs( IInputDevice device, ulong timestamp, IInputRoot root, RawPointerEventType type, RawPointerPoint point, RawInputModifiers inputModifiers) : base(device, timestamp, root) {`
- `public long RawPointerId { get; set; }`
- `public RawPointerPoint Point {`
- `public RawInputModifiers InputModifiers { get; set; }`
- `public Lazy<IReadOnlyList<RawPointerPoint>?>? IntermediatePoints { get; set; }`
- `public record struct RawPointerPoint`
- `public float Twist { get; set; }`
- `public float Pressure { get; set; }`
- `public float XTilt { get; set; }`
- `public float YTilt { get; set; }`
- `public Rect ContactRect {`
- `public RawPointerPoint() {`

### `src/Avalonia.Base/Input/Raw/RawPointerGestureEventArgs.cs`
- `public class RawPointerGestureEventArgs : RawPointerEventArgs`
- `public RawPointerGestureEventArgs( IInputDevice device, ulong timestamp, IInputRoot root, RawPointerEventType gestureType, Point position, Vector delta, RawInputModifiers inputModifiers) : base(device, timestamp, root, gestureType, position, inputModifiers) {`

### `src/Avalonia.Base/Input/Raw/RawSizeEventArgs.cs`
- `public class RawSizeEventArgs : EventArgs`
- `public RawSizeEventArgs(Size size) {`
- `public RawSizeEventArgs(double width, double height) {`

### `src/Avalonia.Base/Input/Raw/RawTextInputEventArgs.cs`
- `public class RawTextInputEventArgs : RawInputEventArgs`
- `public RawTextInputEventArgs( IKeyboardDevice device, ulong timestamp, IInputRoot root, string text) : base(device, timestamp, root) {`

### `src/Avalonia.Base/Input/Raw/RawTouchEventArgs.cs`
- `public class RawTouchEventArgs : RawPointerEventArgs`
- `public RawTouchEventArgs(IInputDevice device, ulong timestamp, IInputRoot root, RawPointerEventType type, Point position, RawInputModifiers inputModifiers, long rawPointerId) : base(device, timestamp, root, type, position, inputModifiers) {`
- `public RawTouchEventArgs(IInputDevice device, ulong timestamp, IInputRoot root, RawPointerEventType type, RawPointerPoint point, RawInputModifiers inputModifiers, long rawPointerId) : base(device, timestamp, root, type, point, inputModifiers) {`

### `src/Avalonia.Base/Input/ScrollGestureEventArgs.cs`
- `public class ScrollGestureEventArgs : RoutedEventArgs`
- `public int Id { get; }`
- `public bool ShouldEndScrollGesture { get; set; }`
- `public static int GetNextFreeId() => _nextId++;`
- `public ScrollGestureEventArgs(int id, Vector delta) : base(Gestures.ScrollGestureEvent) {`
- `public class ScrollGestureEndedEventArgs : RoutedEventArgs`
- `public ScrollGestureEndedEventArgs(int id) : base(Gestures.ScrollGestureEndedEvent) {`
- `public sealed class ScrollGestureInertiaStartingEventArgs : RoutedEventArgs`
- `public Vector Inertia { get; }`

### `src/Avalonia.Base/Input/TappedEventArgs.cs`
- `public class TappedEventArgs : RoutedEventArgs`
- `public TappedEventArgs(RoutedEvent routedEvent, PointerEventArgs lastPointerEventArgs) : base(routedEvent) {`
- `public ulong Timestamp => lastPointerEventArgs.Timestamp;`

### `src/Avalonia.Base/Input/TextInput/ITextInputMethodImpl.cs`
- `public interface ITextInputMethodImpl`
- `public interface ITextInputMethodRoot : IInputRoot`

### `src/Avalonia.Base/Input/TextInput/TextInputMethodClient.cs`
- `public abstract class TextInputMethodClient`
- `public event EventHandler? TextViewVisualChanged;`
- `public event EventHandler? CursorRectangleChanged;`
- `public event EventHandler? SurroundingTextChanged;`
- `public event EventHandler? ResetRequested;`
- `public event EventHandler? InputPaneActivationRequested;`
- `public abstract Visual TextViewVisual { get; }`
- `public abstract bool SupportsPreedit { get; }`
- `public abstract bool SupportsSurroundingText { get; }`
- `public abstract string SurroundingText { get; }`
- `public abstract Rect CursorRectangle { get; }`
- `public virtual void SetPreeditText(string? preeditText) { }`
- `public virtual void ExecuteContextMenuAction(ContextMenuAction action) { }`
- `public virtual void SetPreeditText(string? preeditText, int? cursorPos) {`
- `public virtual void ShowInputPanel() {`
- `public record struct TextSelection(int Start, int End);`
- `public enum ContextMenuAction`

### `src/Avalonia.Base/Input/TextInput/TextInputMethodClientRequeryRequestedEventArgs.cs`
- `public class TextInputMethodClientRequeryRequestedEventArgs : RoutedEventArgs`

### `src/Avalonia.Base/Input/TextInput/TextInputMethodClientRequestedEventArgs.cs`
- `public class TextInputMethodClientRequestedEventArgs : RoutedEventArgs`
- `public TextInputMethodClient? Client { get; set; }`

### `src/Avalonia.Base/Input/TextInput/TextInputOptions.cs`
- `public static readonly AttachedProperty<TextInputContentType> ContentTypeProperty = AvaloniaProperty.RegisterAttached<TextInputOptions, StyledElement, TextInputContentType>( "ContentType", defaultValue: TextInputContentType.Normal, inherits: true);`
- `public static TextInputContentType GetContentType(StyledElement avaloniaObject) {`
- `public static readonly AttachedProperty<TextInputReturnKeyType> ReturnKeyTypeProperty = AvaloniaProperty.RegisterAttached<TextInputOptions, StyledElement, TextInputReturnKeyType>( "ReturnKeyType", defaultValue: TextInputReturnKeyType.Default, inherits: true);`
- `public static TextInputReturnKeyType GetReturnKeyType(StyledElement avaloniaObject) {`
- `public static readonly AttachedProperty<bool> MultilineProperty = AvaloniaProperty.RegisterAttached<TextInputOptions, StyledElement, bool>( "Multiline", inherits: true);`
- `public static void SetMultiline(StyledElement avaloniaObject, bool value) {`
- `public static bool GetMultiline(StyledElement avaloniaObject) {`
- `public static readonly AttachedProperty<bool> LowercaseProperty = AvaloniaProperty.RegisterAttached<TextInputOptions, StyledElement, bool>( "Lowercase", inherits: true);`
- `public static void SetLowercase(StyledElement avaloniaObject, bool value) {`
- `public static bool GetLowercase(StyledElement avaloniaObject) {`
- `public static readonly AttachedProperty<bool> UppercaseProperty = AvaloniaProperty.RegisterAttached<TextInputOptions, StyledElement, bool>( "Uppercase", inherits: true);`
- `public static void SetUppercase(StyledElement avaloniaObject, bool value) {`
- `public static bool GetUppercase(StyledElement avaloniaObject) {`
- `public static readonly AttachedProperty<bool> AutoCapitalizationProperty = AvaloniaProperty.RegisterAttached<TextInputOptions, StyledElement, bool>( "AutoCapitalization", inherits: true);`
- `public static void SetAutoCapitalization(StyledElement avaloniaObject, bool value) {`
- `public static bool GetAutoCapitalization(StyledElement avaloniaObject) {`
- `public static readonly AttachedProperty<bool> IsSensitiveProperty = AvaloniaProperty.RegisterAttached<TextInputOptions, StyledElement, bool>( "IsSensitive", inherits: true);`
- `public static void SetIsSensitive(StyledElement avaloniaObject, bool value) {`
- `public static bool GetIsSensitive(StyledElement avaloniaObject) {`
- `public static readonly AttachedProperty<bool?> ShowSuggestionsProperty = AvaloniaProperty.RegisterAttached<TextInputOptions, StyledElement, bool?>( "ShowSuggestions", inherits: true);`
- `public static bool? GetShowSuggestions(StyledElement avaloniaObject) {`

### `src/Avalonia.Base/Input/TextInputEventArgs.cs`
- `public class TextInputEventArgs : RoutedEventArgs`

### `src/Avalonia.Base/Input/TouchDevice.cs`
- `public class TouchDevice : IPointerDevice, IDisposable`
- `public void ProcessRawEvent(RawInputEventArgs ev) {`
- `public IPointer? TryGetPointer(RawPointerEventArgs ev) {`

### `src/Avalonia.Base/Layout/EffectiveViewportChangedEventArgs.cs`
- `public Rect EffectiveViewport { get; }`

### `src/Avalonia.Base/Layout/IEmbeddedLayoutRoot.cs`
- `public interface IEmbeddedLayoutRoot : ILayoutRoot`

### `src/Avalonia.Base/Layout/LayoutExtensions.cs`
- `public static class LayoutExtensions`
- `public static Rect Align( this Rect rect, Rect constraint, HorizontalAlignment horizontalAlignment, VerticalAlignment verticalAlignment) {`

### `src/Avalonia.Base/Layout/LayoutHelper.cs`
- `public static class LayoutHelper`
- `public static double LayoutEpsilon { get; } = 0.00000153;`
- `public static Size ApplyLayoutConstraints(Layoutable control, Size constraints) => ApplyLayoutConstraints(new MinMax(control), constraints);`
- `public static Size MeasureChild(Layoutable? control, Size availableSize, Thickness padding, Thickness borderThickness) {`
- `public static Size MeasureChild(Layoutable? control, Size availableSize, Thickness padding) {`
- `public static Size ArrangeChild(Layoutable? child, Size availableSize, Thickness padding, Thickness borderThickness) {`
- `public static Size ArrangeChild(Layoutable? child, Size availableSize, Thickness padding) {`
- `public static void InvalidateSelfAndChildrenMeasure(Layoutable control) {`
- `public static double GetLayoutScale(Layoutable control) => control.VisualRoot is ILayoutRoot layoutRoot ? layoutRoot.LayoutScaling : 1.0;`
- `public static Size RoundLayoutSizeUp(Size size, double dpiScaleX, double dpiScaleY) {`
- `public static Thickness RoundLayoutThickness(Thickness thickness, double dpiScaleX, double dpiScaleY) {`
- `public static double RoundLayoutValue(double value, double dpiScale) {`
- `public static double RoundLayoutValueUp(double value, double dpiScale) {`

### `src/Avalonia.Base/Layout/LayoutInformation.cs`
- `public static class LayoutInformation`
- `public static Size? GetPreviousMeasureConstraint(Layoutable control) {`
- `public static Rect? GetPreviousArrangeBounds(Layoutable control) {`

### `src/Avalonia.Base/Layout/LayoutManager.cs`
- `public virtual void ExecuteInitialLayoutPass() {`

### `src/Avalonia.Base/Layout/Layoutable.cs`
- `public static readonly DirectProperty<Layoutable, Size> DesiredSizeProperty = AvaloniaProperty.RegisterDirect<Layoutable, Size>(nameof(DesiredSize), o => o.DesiredSize);`
- `public static readonly StyledProperty<double> WidthProperty = AvaloniaProperty.Register<Layoutable, double>(nameof(Width), double.NaN, validate: ValidateDimension);`
- `public static readonly StyledProperty<double> HeightProperty = AvaloniaProperty.Register<Layoutable, double>(nameof(Height), double.NaN, validate: ValidateDimension);`
- `public static readonly StyledProperty<double> MinWidthProperty = AvaloniaProperty.Register<Layoutable, double>(nameof(MinWidth), validate: ValidateMinimumDimension);`
- `public static readonly StyledProperty<double> MaxWidthProperty = AvaloniaProperty.Register<Layoutable, double>(nameof(MaxWidth), double.PositiveInfinity, validate: ValidateMaximumDimension);`
- `public static readonly StyledProperty<double> MinHeightProperty = AvaloniaProperty.Register<Layoutable, double>(nameof(MinHeight), validate: ValidateMinimumDimension);`
- `public static readonly StyledProperty<double> MaxHeightProperty = AvaloniaProperty.Register<Layoutable, double>(nameof(MaxHeight), double.PositiveInfinity, validate: ValidateMaximumDimension);`
- `public static readonly StyledProperty<Thickness> MarginProperty = AvaloniaProperty.Register<Layoutable, Thickness>(nameof(Margin));`
- `public static readonly StyledProperty<HorizontalAlignment> HorizontalAlignmentProperty = AvaloniaProperty.Register<Layoutable, HorizontalAlignment>(nameof(HorizontalAlignment));`
- `public static readonly StyledProperty<VerticalAlignment> VerticalAlignmentProperty = AvaloniaProperty.Register<Layoutable, VerticalAlignment>(nameof(VerticalAlignment));`
- `public static readonly StyledProperty<bool> UseLayoutRoundingProperty = AvaloniaProperty.Register<Layoutable, bool>(nameof(UseLayoutRounding), defaultValue: true, inherits: true);`

### `src/Avalonia.Base/Logging/ILogSink.cs`
- `public interface ILogSink`

### `src/Avalonia.Base/Logging/LogArea.cs`
- `public const string Win32Platform = nameof(Win32Platform);`
- `public const string X11Platform = nameof(X11Platform);`
- `public const string AndroidPlatform = nameof(AndroidPlatform);`
- `public const string IOSPlatform = nameof(IOSPlatform);`
- `public const string LinuxFramebufferPlatform = nameof(LinuxFramebufferPlatform);`
- `public const string FreeDesktopPlatform = nameof(FreeDesktopPlatform);`
- `public const string macOSPlatform = nameof(macOSPlatform);`
- `public const string BrowserPlatform = nameof(BrowserPlatform);`
- `public const string VncPlatform = nameof(VncPlatform);`

### `src/Avalonia.Base/Logging/Logger.cs`
- `public static ILogSink? Sink { get; set; }`

### `src/Avalonia.Base/Logging/ParametrizedLogger.cs`
- `public readonly record struct ParametrizedLogger`
- `public ParametrizedLogger(ILogSink sink, LogEventLevel level, string area) {`
- `public bool IsValid => _sink != null;`
- `public void Log( object? source, string messageTemplate) {`
- `public void Log<T0>( object? source, string messageTemplate, T0 propertyValue0) {`
- `public void Log<T0, T1>( object? source, string messageTemplate, T0 propertyValue0, T1 propertyValue1) {`
- `public void Log<T0, T1, T2>( object? source, string messageTemplate, T0 propertyValue0, T1 propertyValue1, T2 propertyValue2) {`
- `public void Log<T0, T1, T2, T3>( object? source, string messageTemplate, T0 propertyValue0, T1 propertyValue1, T2 propertyValue2, T3 propertyValue3) {`
- `public void Log<T0, T1, T2, T3, T4>( object? source, string messageTemplate, T0 propertyValue0, T1 propertyValue1, T2 propertyValue2, T3 propertyValue3, T4 propertyValue4) {`
- `public void Log<T0, T1, T2, T3, T4, T5>( object? source, string messageTemplate, T0 propertyValue0, T1 propertyValue1, T2 propertyValue2, T3 propertyValue3, T4 propertyValue4, T5 propertyValue5) {`

### `src/Avalonia.Base/LogicalTree/ChildIndexChangedEventArgs.cs`
- `public enum ChildIndexChangedAction`
- `public class ChildIndexChangedEventArgs : EventArgs`
- `public ChildIndexChangedEventArgs(ILogical child, int index) {`
- `public ChildIndexChangedAction Action { get; }`
- `public int Index { get; }`
- `public static ChildIndexChangedEventArgs ChildIndexesReset { get; } = new(ChildIndexChangedAction.ChildIndexesReset);`
- `public static ChildIndexChangedEventArgs TotalCountChanged { get; } = new(ChildIndexChangedAction.TotalCountChanged);`

### `src/Avalonia.Base/LogicalTree/ControlLocator.cs`
- `public static class ControlLocator`

### `src/Avalonia.Base/LogicalTree/ILogicalRoot.cs`
- `public interface ILogicalRoot : ILogical`

### `src/Avalonia.Base/LogicalTree/LogicalTreeAttachmentEventArgs.cs`
- `public ILogicalRoot Root { get; }`
- `public ILogical? Parent { get; }`

### `src/Avalonia.Base/Matrix.cs`
- `public record struct Decomposed`
- `public Vector Scale;`
- `public Vector Skew;`
- `public double Angle;`

### `src/Avalonia.Base/Media/AcrylicBackgroundSource.cs`
- `public enum AcrylicBackgroundSource`

### `src/Avalonia.Base/Media/AlignmentX.cs`
- `public enum AlignmentX`

### `src/Avalonia.Base/Media/AlignmentY.cs`
- `public enum AlignmentY`

### `src/Avalonia.Base/Media/ArcSegment.cs`
- `public sealed class ArcSegment : PathSegment`
- `public static readonly StyledProperty<bool> IsLargeArcProperty = AvaloniaProperty.Register<ArcSegment, bool>(nameof(IsLargeArc), false);`
- `public static readonly StyledProperty<Point> PointProperty = AvaloniaProperty.Register<ArcSegment, Point>(nameof(Point));`
- `public static readonly StyledProperty<double> RotationAngleProperty = AvaloniaProperty.Register<ArcSegment, double>(nameof(RotationAngle), 0);`
- `public static readonly StyledProperty<Size> SizeProperty = AvaloniaProperty.Register<ArcSegment, Size>(nameof(Size));`
- `public static readonly StyledProperty<SweepDirection> SweepDirectionProperty = AvaloniaProperty.Register<ArcSegment, SweepDirection>(nameof(SweepDirection), SweepDirection.Clockwise);`
- `public bool IsLargeArc {`
- `public Point Point {`
- `public double RotationAngle {`
- `public SweepDirection SweepDirection {`

### `src/Avalonia.Base/Media/BaselineAlignment.cs`
- `public enum BaselineAlignment`

### `src/Avalonia.Base/Media/BezierSegment .cs`
- `public sealed class BezierSegment : PathSegment`
- `public static readonly StyledProperty<Point> Point1Property = AvaloniaProperty.Register<BezierSegment, Point>(nameof(Point1));`
- `public static readonly StyledProperty<Point> Point2Property = AvaloniaProperty.Register<BezierSegment, Point>(nameof(Point2));`
- `public static readonly StyledProperty<Point> Point3Property = AvaloniaProperty.Register<BezierSegment, Point>(nameof(Point3));`
- `public Point Point1 {`
- `public Point Point2 {`
- `public Point Point3 {`

### `src/Avalonia.Base/Media/BoxShadow.cs`
- `public double OffsetX { get; set; }`
- `public double OffsetY { get; set; }`
- `public double Spread { get; set; }`
- `public bool IsInset { get; set; }`
- `public Rect TransformBounds(in Rect rect) => IsInset ? rect : rect.Translate(new Vector(OffsetX, OffsetY)).Inflate(Spread + Blur);`

### `src/Avalonia.Base/Media/BoxShadows.cs`
- `public struct BoxShadowsEnumerator`
- `public BoxShadowsEnumerator(BoxShadows shadows) {`
- `public BoxShadow Current => _shadows[_index];`
- `public bool MoveNext() {`
- `public Rect TransformBounds(in Rect rect) {`
- `public bool HasInsetShadows {`

### `src/Avalonia.Base/Media/Brush.cs`
- `public static readonly StyledProperty<RelativePoint> TransformOriginProperty = AvaloniaProperty.Register<Brush, RelativePoint>(nameof(TransformOrigin));`
- `public double Opacity {`
- `public RelativePoint TransformOrigin {`

### `src/Avalonia.Base/Media/BrushExtensions.cs`
- `public static class BrushExtensions`

### `src/Avalonia.Base/Media/BrushMappingMode.cs`
- `public enum BrushMappingMode`

### `src/Avalonia.Base/Media/Brushes.cs`
- `public static IImmutableSolidColorBrush AliceBlue => KnownColor.AliceBlue.ToBrush();`
- `public static IImmutableSolidColorBrush AntiqueWhite => KnownColor.AntiqueWhite.ToBrush();`
- `public static IImmutableSolidColorBrush Aqua => KnownColor.Aqua.ToBrush();`
- `public static IImmutableSolidColorBrush Aquamarine => KnownColor.Aquamarine.ToBrush();`
- `public static IImmutableSolidColorBrush Azure => KnownColor.Azure.ToBrush();`
- `public static IImmutableSolidColorBrush Beige => KnownColor.Beige.ToBrush();`
- `public static IImmutableSolidColorBrush Bisque => KnownColor.Bisque.ToBrush();`
- `public static IImmutableSolidColorBrush BlanchedAlmond => KnownColor.BlanchedAlmond.ToBrush();`
- `public static IImmutableSolidColorBrush Blue => KnownColor.Blue.ToBrush();`
- `public static IImmutableSolidColorBrush BlueViolet => KnownColor.BlueViolet.ToBrush();`
- `public static IImmutableSolidColorBrush Brown => KnownColor.Brown.ToBrush();`
- `public static IImmutableSolidColorBrush BurlyWood => KnownColor.BurlyWood.ToBrush();`
- `public static IImmutableSolidColorBrush CadetBlue => KnownColor.CadetBlue.ToBrush();`
- `public static IImmutableSolidColorBrush Chartreuse => KnownColor.Chartreuse.ToBrush();`
- `public static IImmutableSolidColorBrush Chocolate => KnownColor.Chocolate.ToBrush();`
- `public static IImmutableSolidColorBrush Coral => KnownColor.Coral.ToBrush();`
- `public static IImmutableSolidColorBrush Cornsilk => KnownColor.Cornsilk.ToBrush();`
- `public static IImmutableSolidColorBrush Cyan => KnownColor.Cyan.ToBrush();`
- `public static IImmutableSolidColorBrush DarkBlue => KnownColor.DarkBlue.ToBrush();`
- `public static IImmutableSolidColorBrush DarkCyan => KnownColor.DarkCyan.ToBrush();`
- `public static IImmutableSolidColorBrush DarkGoldenrod => KnownColor.DarkGoldenrod.ToBrush();`
- `public static IImmutableSolidColorBrush DarkGray => KnownColor.DarkGray.ToBrush();`
- `public static IImmutableSolidColorBrush DarkKhaki => KnownColor.DarkKhaki.ToBrush();`
- `public static IImmutableSolidColorBrush DarkMagenta => KnownColor.DarkMagenta.ToBrush();`
- `public static IImmutableSolidColorBrush DarkOliveGreen => KnownColor.DarkOliveGreen.ToBrush();`
- `public static IImmutableSolidColorBrush DarkOrange => KnownColor.DarkOrange.ToBrush();`
- `public static IImmutableSolidColorBrush DarkOrchid => KnownColor.DarkOrchid.ToBrush();`
- `public static IImmutableSolidColorBrush DarkRed => KnownColor.DarkRed.ToBrush();`
- `public static IImmutableSolidColorBrush DarkSalmon => KnownColor.DarkSalmon.ToBrush();`
- `public static IImmutableSolidColorBrush DarkSeaGreen => KnownColor.DarkSeaGreen.ToBrush();`
- `public static IImmutableSolidColorBrush DarkSlateBlue => KnownColor.DarkSlateBlue.ToBrush();`
- `public static IImmutableSolidColorBrush DarkSlateGray => KnownColor.DarkSlateGray.ToBrush();`
- `public static IImmutableSolidColorBrush DarkTurquoise => KnownColor.DarkTurquoise.ToBrush();`
- `public static IImmutableSolidColorBrush DarkViolet => KnownColor.DarkViolet.ToBrush();`
- `public static IImmutableSolidColorBrush DeepPink => KnownColor.DeepPink.ToBrush();`
- `public static IImmutableSolidColorBrush Firebrick => KnownColor.Firebrick.ToBrush();`
- `public static IImmutableSolidColorBrush FloralWhite => KnownColor.FloralWhite.ToBrush();`
- `public static IImmutableSolidColorBrush Fuchsia => KnownColor.Fuchsia.ToBrush();`
- `public static IImmutableSolidColorBrush Gainsboro => KnownColor.Gainsboro.ToBrush();`
- `public static IImmutableSolidColorBrush GhostWhite => KnownColor.GhostWhite.ToBrush();`
- `public static IImmutableSolidColorBrush Goldenrod => KnownColor.Goldenrod.ToBrush();`
- `public static IImmutableSolidColorBrush Green => KnownColor.Green.ToBrush();`
- `public static IImmutableSolidColorBrush GreenYellow => KnownColor.GreenYellow.ToBrush();`
- `public static IImmutableSolidColorBrush Honeydew => KnownColor.Honeydew.ToBrush();`
- `public static IImmutableSolidColorBrush HotPink => KnownColor.HotPink.ToBrush();`
- `public static IImmutableSolidColorBrush IndianRed => KnownColor.IndianRed.ToBrush();`
- `public static IImmutableSolidColorBrush Indigo => KnownColor.Indigo.ToBrush();`
- `public static IImmutableSolidColorBrush Ivory => KnownColor.Ivory.ToBrush();`
- `public static IImmutableSolidColorBrush Khaki => KnownColor.Khaki.ToBrush();`
- `public static IImmutableSolidColorBrush Lavender => KnownColor.Lavender.ToBrush();`
- `public static IImmutableSolidColorBrush LavenderBlush => KnownColor.LavenderBlush.ToBrush();`
- `public static IImmutableSolidColorBrush LawnGreen => KnownColor.LawnGreen.ToBrush();`
- `public static IImmutableSolidColorBrush LemonChiffon => KnownColor.LemonChiffon.ToBrush();`
- `public static IImmutableSolidColorBrush LightBlue => KnownColor.LightBlue.ToBrush();`
- `public static IImmutableSolidColorBrush LightCoral => KnownColor.LightCoral.ToBrush();`
- `public static IImmutableSolidColorBrush LightCyan => KnownColor.LightCyan.ToBrush();`
- `public static IImmutableSolidColorBrush LightGoldenrodYellow => KnownColor.LightGoldenrodYellow.ToBrush();`
- `public static IImmutableSolidColorBrush LightGray => KnownColor.LightGray.ToBrush();`
- `public static IImmutableSolidColorBrush LightGreen => KnownColor.LightGreen.ToBrush();`
- `public static IImmutableSolidColorBrush LightPink => KnownColor.LightPink.ToBrush();`
- `public static IImmutableSolidColorBrush LightSalmon => KnownColor.LightSalmon.ToBrush();`
- `public static IImmutableSolidColorBrush LightSeaGreen => KnownColor.LightSeaGreen.ToBrush();`
- `public static IImmutableSolidColorBrush LightSkyBlue => KnownColor.LightSkyBlue.ToBrush();`
- `public static IImmutableSolidColorBrush LightSlateGray => KnownColor.LightSlateGray.ToBrush();`
- `public static IImmutableSolidColorBrush LightSteelBlue => KnownColor.LightSteelBlue.ToBrush();`
- `public static IImmutableSolidColorBrush LightYellow => KnownColor.LightYellow.ToBrush();`
- `public static IImmutableSolidColorBrush Linen => KnownColor.Linen.ToBrush();`
- `public static IImmutableSolidColorBrush Magenta => KnownColor.Magenta.ToBrush();`
- `public static IImmutableSolidColorBrush Maroon => KnownColor.Maroon.ToBrush();`
- `public static IImmutableSolidColorBrush MediumAquamarine => KnownColor.MediumAquamarine.ToBrush();`
- `public static IImmutableSolidColorBrush MediumBlue => KnownColor.MediumBlue.ToBrush();`
- `public static IImmutableSolidColorBrush MediumOrchid => KnownColor.MediumOrchid.ToBrush();`
- `public static IImmutableSolidColorBrush MediumPurple => KnownColor.MediumPurple.ToBrush();`
- `public static IImmutableSolidColorBrush MediumSeaGreen => KnownColor.MediumSeaGreen.ToBrush();`
- `public static IImmutableSolidColorBrush MediumSlateBlue => KnownColor.MediumSlateBlue.ToBrush();`
- `public static IImmutableSolidColorBrush MediumSpringGreen => KnownColor.MediumSpringGreen.ToBrush();`
- `public static IImmutableSolidColorBrush MediumTurquoise => KnownColor.MediumTurquoise.ToBrush();`
- `public static IImmutableSolidColorBrush MediumVioletRed => KnownColor.MediumVioletRed.ToBrush();`
- `public static IImmutableSolidColorBrush MidnightBlue => KnownColor.MidnightBlue.ToBrush();`
- `public static IImmutableSolidColorBrush MintCream => KnownColor.MintCream.ToBrush();`
- `public static IImmutableSolidColorBrush MistyRose => KnownColor.MistyRose.ToBrush();`
- `public static IImmutableSolidColorBrush Moccasin => KnownColor.Moccasin.ToBrush();`
- `public static IImmutableSolidColorBrush NavajoWhite => KnownColor.NavajoWhite.ToBrush();`
- `public static IImmutableSolidColorBrush OldLace => KnownColor.OldLace.ToBrush();`
- `public static IImmutableSolidColorBrush Olive => KnownColor.Olive.ToBrush();`
- `public static IImmutableSolidColorBrush OliveDrab => KnownColor.OliveDrab.ToBrush();`
- `public static IImmutableSolidColorBrush Orange => KnownColor.Orange.ToBrush();`
- `public static IImmutableSolidColorBrush Orchid => KnownColor.Orchid.ToBrush();`
- `public static IImmutableSolidColorBrush PaleGoldenrod => KnownColor.PaleGoldenrod.ToBrush();`
- `public static IImmutableSolidColorBrush PaleGreen => KnownColor.PaleGreen.ToBrush();`
- `public static IImmutableSolidColorBrush PaleTurquoise => KnownColor.PaleTurquoise.ToBrush();`
- `public static IImmutableSolidColorBrush PaleVioletRed => KnownColor.PaleVioletRed.ToBrush();`
- `public static IImmutableSolidColorBrush PapayaWhip => KnownColor.PapayaWhip.ToBrush();`
- `public static IImmutableSolidColorBrush PeachPuff => KnownColor.PeachPuff.ToBrush();`
- `public static IImmutableSolidColorBrush Peru => KnownColor.Peru.ToBrush();`
- `public static IImmutableSolidColorBrush Pink => KnownColor.Pink.ToBrush();`
- `public static IImmutableSolidColorBrush Plum => KnownColor.Plum.ToBrush();`
- `public static IImmutableSolidColorBrush PowderBlue => KnownColor.PowderBlue.ToBrush();`
- `public static IImmutableSolidColorBrush Purple => KnownColor.Purple.ToBrush();`
- `public static IImmutableSolidColorBrush Red => KnownColor.Red.ToBrush();`
- `public static IImmutableSolidColorBrush RosyBrown => KnownColor.RosyBrown.ToBrush();`
- `public static IImmutableSolidColorBrush RoyalBlue => KnownColor.RoyalBlue.ToBrush();`
- `public static IImmutableSolidColorBrush SaddleBrown => KnownColor.SaddleBrown.ToBrush();`
- `public static IImmutableSolidColorBrush Salmon => KnownColor.Salmon.ToBrush();`
- `public static IImmutableSolidColorBrush SandyBrown => KnownColor.SandyBrown.ToBrush();`

### `src/Avalonia.Base/Media/CharacterHit.cs`
- `public readonly struct CharacterHit : IEquatable<CharacterHit>`
- `public CharacterHit(int firstCharacterIndex, int trailingLength = 0) {`
- `public int FirstCharacterIndex { get; }`
- `public int TrailingLength { get; }`

### `src/Avalonia.Base/Media/Colors.cs`
- `public static Color AliceBlue => KnownColor.AliceBlue.ToColor();`
- `public static Color AntiqueWhite => KnownColor.AntiqueWhite.ToColor();`
- `public static Color Aqua => KnownColor.Aqua.ToColor();`
- `public static Color Aquamarine => KnownColor.Aquamarine.ToColor();`
- `public static Color Azure => KnownColor.Azure.ToColor();`
- `public static Color Beige => KnownColor.Beige.ToColor();`
- `public static Color Bisque => KnownColor.Bisque.ToColor();`
- `public static Color BlanchedAlmond => KnownColor.BlanchedAlmond.ToColor();`
- `public static Color BlueViolet => KnownColor.BlueViolet.ToColor();`
- `public static Color Brown => KnownColor.Brown.ToColor();`
- `public static Color BurlyWood => KnownColor.BurlyWood.ToColor();`
- `public static Color CadetBlue => KnownColor.CadetBlue.ToColor();`
- `public static Color Chartreuse => KnownColor.Chartreuse.ToColor();`
- `public static Color Chocolate => KnownColor.Chocolate.ToColor();`
- `public static Color Coral => KnownColor.Coral.ToColor();`
- `public static Color Cornsilk => KnownColor.Cornsilk.ToColor();`
- `public static Color Crimson => KnownColor.Crimson.ToColor();`
- `public static Color Cyan => KnownColor.Cyan.ToColor();`
- `public static Color DarkBlue => KnownColor.DarkBlue.ToColor();`
- `public static Color DarkCyan => KnownColor.DarkCyan.ToColor();`
- `public static Color DarkGoldenrod => KnownColor.DarkGoldenrod.ToColor();`
- `public static Color DarkGray => KnownColor.DarkGray.ToColor();`
- `public static Color DarkKhaki => KnownColor.DarkKhaki.ToColor();`
- `public static Color DarkMagenta => KnownColor.DarkMagenta.ToColor();`
- `public static Color DarkOliveGreen => KnownColor.DarkOliveGreen.ToColor();`
- `public static Color DarkOrange => KnownColor.DarkOrange.ToColor();`
- `public static Color DarkOrchid => KnownColor.DarkOrchid.ToColor();`
- `public static Color DarkRed => KnownColor.DarkRed.ToColor();`
- `public static Color DarkSalmon => KnownColor.DarkSalmon.ToColor();`
- `public static Color DarkSeaGreen => KnownColor.DarkSeaGreen.ToColor();`
- `public static Color DarkSlateBlue => KnownColor.DarkSlateBlue.ToColor();`
- `public static Color DarkSlateGray => KnownColor.DarkSlateGray.ToColor();`
- `public static Color DarkTurquoise => KnownColor.DarkTurquoise.ToColor();`
- `public static Color DarkViolet => KnownColor.DarkViolet.ToColor();`
- `public static Color DeepPink => KnownColor.DeepPink.ToColor();`
- `public static Color DimGray => KnownColor.DimGray.ToColor();`
- `public static Color Firebrick => KnownColor.Firebrick.ToColor();`
- `public static Color FloralWhite => KnownColor.FloralWhite.ToColor();`
- `public static Color Fuchsia => KnownColor.Fuchsia.ToColor();`
- `public static Color Gainsboro => KnownColor.Gainsboro.ToColor();`
- `public static Color GhostWhite => KnownColor.GhostWhite.ToColor();`
- `public static Color Gold => KnownColor.Gold.ToColor();`
- `public static Color Goldenrod => KnownColor.Goldenrod.ToColor();`
- `public static Color Gray => KnownColor.Gray.ToColor();`
- `public static Color Green => KnownColor.Green.ToColor();`
- `public static Color GreenYellow => KnownColor.GreenYellow.ToColor();`
- `public static Color Honeydew => KnownColor.Honeydew.ToColor();`
- `public static Color HotPink => KnownColor.HotPink.ToColor();`
- `public static Color IndianRed => KnownColor.IndianRed.ToColor();`
- `public static Color Indigo => KnownColor.Indigo.ToColor();`
- `public static Color Ivory => KnownColor.Ivory.ToColor();`
- `public static Color Khaki => KnownColor.Khaki.ToColor();`
- `public static Color Lavender => KnownColor.Lavender.ToColor();`
- `public static Color LavenderBlush => KnownColor.LavenderBlush.ToColor();`
- `public static Color LawnGreen => KnownColor.LawnGreen.ToColor();`
- `public static Color LemonChiffon => KnownColor.LemonChiffon.ToColor();`
- `public static Color LightBlue => KnownColor.LightBlue.ToColor();`
- `public static Color LightCoral => KnownColor.LightCoral.ToColor();`
- `public static Color LightCyan => KnownColor.LightCyan.ToColor();`
- `public static Color LightGoldenrodYellow => KnownColor.LightGoldenrodYellow.ToColor();`
- `public static Color LightGray => KnownColor.LightGray.ToColor();`
- `public static Color LightGreen => KnownColor.LightGreen.ToColor();`
- `public static Color LightPink => KnownColor.LightPink.ToColor();`
- `public static Color LightSalmon => KnownColor.LightSalmon.ToColor();`
- `public static Color LightSeaGreen => KnownColor.LightSeaGreen.ToColor();`
- `public static Color LightSkyBlue => KnownColor.LightSkyBlue.ToColor();`
- `public static Color LightSlateGray => KnownColor.LightSlateGray.ToColor();`
- `public static Color LightSteelBlue => KnownColor.LightSteelBlue.ToColor();`
- `public static Color LightYellow => KnownColor.LightYellow.ToColor();`
- `public static Color Lime => KnownColor.Lime.ToColor();`
- `public static Color Linen => KnownColor.Linen.ToColor();`
- `public static Color Magenta => KnownColor.Magenta.ToColor();`
- `public static Color Maroon => KnownColor.Maroon.ToColor();`
- `public static Color MediumAquamarine => KnownColor.MediumAquamarine.ToColor();`
- `public static Color MediumBlue => KnownColor.MediumBlue.ToColor();`
- `public static Color MediumOrchid => KnownColor.MediumOrchid.ToColor();`
- `public static Color MediumPurple => KnownColor.MediumPurple.ToColor();`
- `public static Color MediumSeaGreen => KnownColor.MediumSeaGreen.ToColor();`
- `public static Color MediumSlateBlue => KnownColor.MediumSlateBlue.ToColor();`
- `public static Color MediumSpringGreen => KnownColor.MediumSpringGreen.ToColor();`
- `public static Color MediumTurquoise => KnownColor.MediumTurquoise.ToColor();`
- `public static Color MediumVioletRed => KnownColor.MediumVioletRed.ToColor();`
- `public static Color MidnightBlue => KnownColor.MidnightBlue.ToColor();`
- `public static Color MintCream => KnownColor.MintCream.ToColor();`
- `public static Color MistyRose => KnownColor.MistyRose.ToColor();`
- `public static Color Moccasin => KnownColor.Moccasin.ToColor();`
- `public static Color NavajoWhite => KnownColor.NavajoWhite.ToColor();`
- `public static Color Navy => KnownColor.Navy.ToColor();`
- `public static Color OldLace => KnownColor.OldLace.ToColor();`
- `public static Color Olive => KnownColor.Olive.ToColor();`
- `public static Color OliveDrab => KnownColor.OliveDrab.ToColor();`
- `public static Color Orange => KnownColor.Orange.ToColor();`
- `public static Color Orchid => KnownColor.Orchid.ToColor();`
- `public static Color PaleGoldenrod => KnownColor.PaleGoldenrod.ToColor();`
- `public static Color PaleGreen => KnownColor.PaleGreen.ToColor();`
- `public static Color PaleTurquoise => KnownColor.PaleTurquoise.ToColor();`
- `public static Color PaleVioletRed => KnownColor.PaleVioletRed.ToColor();`
- `public static Color PapayaWhip => KnownColor.PapayaWhip.ToColor();`
- `public static Color PeachPuff => KnownColor.PeachPuff.ToColor();`
- `public static Color Peru => KnownColor.Peru.ToColor();`
- `public static Color Pink => KnownColor.Pink.ToColor();`
- `public static Color Plum => KnownColor.Plum.ToColor();`
- `public static Color PowderBlue => KnownColor.PowderBlue.ToColor();`
- `public static Color Purple => KnownColor.Purple.ToColor();`
- `public static Color RosyBrown => KnownColor.RosyBrown.ToColor();`
- `public static Color RoyalBlue => KnownColor.RoyalBlue.ToColor();`
- `public static Color SaddleBrown => KnownColor.SaddleBrown.ToColor();`
- `public static Color Salmon => KnownColor.Salmon.ToColor();`
- `public static Color SandyBrown => KnownColor.SandyBrown.ToColor();`

### `src/Avalonia.Base/Media/ConicGradientBrush.cs`
- `public sealed class ConicGradientBrush : GradientBrush, IConicGradientBrush`
- `public static readonly StyledProperty<RelativePoint> CenterProperty = AvaloniaProperty.Register<ConicGradientBrush, RelativePoint>( nameof(Center), RelativePoint.Center);`
- `public static readonly StyledProperty<double> AngleProperty = AvaloniaProperty.Register<ConicGradientBrush, double>( nameof(Angle), 0);`
- `public RelativePoint Center {`
- `public double Angle {`

### `src/Avalonia.Base/Media/DashStyle.cs`
- `public sealed class DashStyle : Animatable, IDashStyle`
- `public static readonly StyledProperty<AvaloniaList<double>?> DashesProperty = AvaloniaProperty.Register<DashStyle, AvaloniaList<double>?>(nameof(Dashes));`
- `public DashStyle() {`
- `public DashStyle(IEnumerable<double>? dashes, double offset) {`
- `public static IDashStyle Dash => s_dash ??= new ImmutableDashStyle(new double[] { 2, 2 }, 1);`
- `public static IDashStyle Dot => s_dot ??= new ImmutableDashStyle(new double[] { 0, 2 }, 0);`
- `public static IDashStyle DashDot => s_dashDot ??= new ImmutableDashStyle(new double[] { 2, 2, 0, 2 }, 1);`
- `public static IDashStyle DashDotDot => s_dashDotDot ??= new ImmutableDashStyle(new double[] { 2, 2, 0, 2, 0, 2 }, 1);`
- `public AvaloniaList<double>? Dashes {`

### `src/Avalonia.Base/Media/Drawing.cs`
- `public abstract Rect GetBounds();`

### `src/Avalonia.Base/Media/DrawingBrush.cs`
- `public sealed class DrawingBrush : TileBrush, ISceneBrush`
- `public static readonly StyledProperty<Drawing?> DrawingProperty = AvaloniaProperty.Register<DrawingBrush, Drawing?>(nameof(Drawing));`
- `public DrawingBrush() {`
- `public DrawingBrush(Drawing visual) {`
- `public Drawing? Drawing {`

### `src/Avalonia.Base/Media/DrawingCollection.cs`
- `public sealed class DrawingCollection : AvaloniaList<Drawing>`
- `public DrawingCollection() {`
- `public DrawingCollection(IEnumerable<Drawing> items) : base(items) {`

### `src/Avalonia.Base/Media/DrawingContext.cs`
- `public virtual void DrawImage(IImage source, Rect rect) {`
- `public virtual void DrawImage(IImage source, Rect sourceRect, Rect destRect) {`
- `public record struct PushedState : IDisposable`
- `public PushedState(DrawingContext context) {`
- `public PushedState PushGeometryClip(Geometry clip) {`
- `public PushedState PushOpacity(double opacity) {`
- `public PushedState PushOpacityMask(IBrush mask, Rect bounds) {`
- `public PushedState PushTransform(Matrix matrix) {`
- `public PushedState PushRenderOptions(RenderOptions renderOptions) {`
- `public PushedState PushPreTransform(Matrix matrix) => PushTransform(matrix);`
- `public PushedState PushPostTransform(Matrix matrix) => PushTransform(matrix);`
- `public PushedState PushTransformContainer() => PushTransform(Matrix.Identity);`

### `src/Avalonia.Base/Media/DrawingGroup.cs`
- `public sealed class DrawingGroup : Drawing`
- `public static readonly StyledProperty<Geometry?> ClipGeometryProperty = AvaloniaProperty.Register<DrawingGroup, Geometry?>(nameof(ClipGeometry));`
- `public static readonly StyledProperty<IBrush?> OpacityMaskProperty = AvaloniaProperty.Register<DrawingGroup, IBrush?>(nameof(OpacityMask));`
- `public static readonly DirectProperty<DrawingGroup, DrawingCollection> ChildrenProperty = AvaloniaProperty.RegisterDirect<DrawingGroup, DrawingCollection>( nameof(Children), o => o.Children,`
- `public double Opacity {`
- `public Geometry? ClipGeometry {`
- `public IBrush? OpacityMask {`
- `public override Rect GetBounds() {`

### `src/Avalonia.Base/Media/DrawingImage.cs`
- `public static readonly StyledProperty<Drawing?> DrawingProperty = AvaloniaProperty.Register<DrawingImage, Drawing?>(nameof(Drawing));`
- `public event EventHandler? Invalidated;`

### `src/Avalonia.Base/Media/EdgeMode.cs`
- `public enum EdgeMode : byte`

### `src/Avalonia.Base/Media/Effects/BlurEffect.cs`
- `public sealed class BlurEffect : Effect, IBlurEffect, IMutableEffect`
- `public static readonly StyledProperty<double> RadiusProperty = AvaloniaProperty.Register<BlurEffect, double>( nameof(Radius), 5);`
- `public double Radius {`

### `src/Avalonia.Base/Media/Effects/DropShadowEffect.cs`
- `public abstract class DropShadowEffectBase : Effect`
- `public static readonly StyledProperty<double> BlurRadiusProperty = AvaloniaProperty.Register<DropShadowEffectBase, double>( nameof(BlurRadius), 5);`
- `public double BlurRadius {`
- `public double Opacity {`
- `public sealed class DropShadowEffect : DropShadowEffectBase, IDropShadowEffect, IMutableEffect`
- `public static readonly StyledProperty<double> OffsetXProperty = AvaloniaProperty.Register<DropShadowEffect, double>( nameof(OffsetX), 3.5355);`
- `public double OffsetX {`
- `public static readonly StyledProperty<double> OffsetYProperty = AvaloniaProperty.Register<DropShadowEffect, double>( nameof(OffsetY), 3.5355);`
- `public double OffsetY {`
- `public sealed class DropShadowDirectionEffect : DropShadowEffectBase, IDirectionDropShadowEffect, IMutableEffect`
- `public static readonly StyledProperty<double> ShadowDepthProperty = AvaloniaProperty.Register<DropShadowDirectionEffect, double>( nameof(ShadowDepth), 5);`
- `public double ShadowDepth {`
- `public static readonly StyledProperty<double> DirectionProperty = AvaloniaProperty.Register<DropShadowDirectionEffect, double>( nameof(Direction), 315);`
- `public double OffsetX => Math.Cos(Direction * Math.PI / 180) * ShadowDepth;`
- `public double OffsetY => Math.Sin(Direction * Math.PI / 180) * ShadowDepth;`

### `src/Avalonia.Base/Media/Effects/Effect.cs`
- `public event EventHandler? Invalidated;`

### `src/Avalonia.Base/Media/Effects/EffectConverter.cs`
- `public class EffectConverter : TypeConverter`

### `src/Avalonia.Base/Media/Effects/EffectExtesions.cs`
- `public static class EffectExtensions`

### `src/Avalonia.Base/Media/Effects/EffectTransition.cs`
- `public class EffectTransition : Transition<IEffect?>`

### `src/Avalonia.Base/Media/Effects/IBlurEffect.cs`
- `public interface IBlurEffect : IEffect`
- `public class ImmutableBlurEffect : IBlurEffect, IImmutableEffect`
- `public ImmutableBlurEffect(double radius) {`
- `public double Radius { get; }`

### `src/Avalonia.Base/Media/Effects/IDropShadowEffect.cs`
- `public interface IDropShadowEffect : IEffect`
- `public class ImmutableDropShadowEffect : IDropShadowEffect, IImmutableEffect`
- `public ImmutableDropShadowEffect(double offsetX, double offsetY, double blurRadius, Color color, double opacity) {`
- `public double OffsetX { get; }`
- `public double OffsetY { get; }`
- `public double BlurRadius { get; }`
- `public double Opacity { get; }`
- `public class ImmutableDropShadowDirectionEffect : IDirectionDropShadowEffect, IImmutableEffect`
- `public ImmutableDropShadowDirectionEffect(double direction, double shadowDepth, double blurRadius, Color color, double opacity) {`
- `public double OffsetX => Math.Cos(Direction * Math.PI / 180) * ShadowDepth;`
- `public double OffsetY => Math.Sin(Direction * Math.PI / 180) * ShadowDepth;`
- `public double ShadowDepth { get; }`

### `src/Avalonia.Base/Media/Effects/IEffect.cs`
- `public interface IEffect`
- `public interface IMutableEffect : IEffect`
- `public interface IImmutableEffect : IEffect, IEquatable<IEffect>`

### `src/Avalonia.Base/Media/EllipseGeometry.cs`
- `public static readonly StyledProperty<Rect> RectProperty = AvaloniaProperty.Register<EllipseGeometry, Rect>(nameof(Rect));`
- `public static readonly StyledProperty<Point> CenterProperty = AvaloniaProperty.Register<EllipseGeometry, Point>(nameof(Center));`
- `public Rect Rect {`
- `public double RadiusX {`
- `public double RadiusY {`
- `public Point Center {`
- `public override Geometry Clone() {`

### `src/Avalonia.Base/Media/ExperimentalAcrylicMaterial.cs`
- `public event EventHandler? Invalidated;`

### `src/Avalonia.Base/Media/FontFallback.cs`
- `public class FontFallback`
- `public UnicodeRange UnicodeRange { get; set; } = UnicodeRange.Default;`

### `src/Avalonia.Base/Media/FontFamily.cs`
- `public const string DefaultFontFamilyName = "$Default";`
- `public FamilyNameCollection FamilyNames { get; }`
- `public IReadOnlyList<Typeface> FamilyTypefaces => FontManager.Current.GetFamilyTypefaces(this);`
- `public static implicit operator FontFamily(string s) {`

### `src/Avalonia.Base/Media/FontFeature.cs`
- `public record FontFeature`
- `public FontFeature() {`

### `src/Avalonia.Base/Media/FontManager.cs`
- `public const string FontCollectionScheme = "fonts";`
- `public const string SystemFontScheme = "systemfont";`
- `public const string CompositeFontScheme = "compositefont";`
- `public FontManager(IFontManagerImpl platformImpl) {`
- `public static FontManager Current {`
- `public FontFamily DefaultFontFamily {`
- `public IFontCollection SystemFonts => _fontCollections[SystemFontsKey];`
- `public bool TryGetGlyphTypeface(Typeface typeface, [NotNullWhen(true)] out IGlyphTypeface? glyphTypeface) {`
- `public void AddFontCollection(IFontCollection fontCollection) {`
- `public void RemoveFontCollection(Uri key) {`
- `public bool TryMatchCharacter(int codepoint, FontStyle fontStyle, FontWeight fontWeight, FontStretch fontStretch, FontFamily? fontFamily, CultureInfo? culture, out Typeface typeface) {`

### `src/Avalonia.Base/Media/FontManagerOptions.cs`
- `public class FontManagerOptions`
- `public string? DefaultFamilyName { get; set; }`
- `public IReadOnlyList<FontFallback>? FontFallbacks { get; set; }`
- `public IReadOnlyDictionary<string, FontFamily>? FontFamilyMappings { get; set; }`

### `src/Avalonia.Base/Media/FontMetrics.cs`
- `public readonly record struct FontMetrics`
- `public short DesignEmHeight { get; init; }`
- `public bool IsFixedPitch { get; init; }`
- `public int Ascent { get; init; }`
- `public int Descent { get; init; }`
- `public int LineGap { get; init; }`
- `public int UnderlinePosition { get; init; }`
- `public int UnderlineThickness { get; init; }`
- `public int StrikethroughPosition { get; init; }`
- `public int StrikethroughThickness { get; init; }`

### `src/Avalonia.Base/Media/FontSimulations.cs`
- `public enum FontSimulations : byte`

### `src/Avalonia.Base/Media/Fonts/EmbeddedFontCollection.cs`
- `public class EmbeddedFontCollection : FontCollectionBase, IFontCollection2`
- `public EmbeddedFontCollection(Uri key, Uri source) {`
- `public override bool TryGetGlyphTypeface(string familyName, FontStyle style, FontWeight weight, FontStretch stretch, [NotNullWhen(true)] out IGlyphTypeface? glyphTypeface) {`
- `public bool TryGetFamilyTypefaces(string familyName, [NotNullWhen(true)] out IReadOnlyList<Typeface>? familyTypefaces) {`

### `src/Avalonia.Base/Media/Fonts/FamilyNameCollection.cs`
- `public sealed class FamilyNameCollection : IReadOnlyList<string>`
- `public FamilyNameCollection(string familyNames) {`
- `public string PrimaryFamilyName { get; }`
- `public bool HasFallbacks { get; }`

### `src/Avalonia.Base/Media/Fonts/FontCollectionBase.cs`
- `public abstract class FontCollectionBase : IFontCollection`
- `public abstract bool TryGetGlyphTypeface(string familyName, FontStyle style, FontWeight weight, FontStretch stretch, [NotNullWhen(true)] out IGlyphTypeface? glyphTypeface);`
- `public virtual bool TryMatchCharacter(int codepoint, FontStyle style, FontWeight weight, FontStretch stretch, string? familyName, CultureInfo? culture, out Typeface match) {`
- `public virtual bool TryCreateSyntheticGlyphTypeface( IGlyphTypeface glyphTypeface, FontStyle style, FontWeight weight, FontStretch stretch, [NotNullWhen(true)] out IGlyphTypeface? syntheticGlyphTypeface) {`

### `src/Avalonia.Base/Media/Fonts/FontCollectionKey.cs`
- `public readonly record struct FontCollectionKey(FontStyle Style, FontWeight Weight, FontStretch Stretch);`

### `src/Avalonia.Base/Media/Fonts/FontFamilyKey.cs`
- `public class FontFamilyKey`
- `public FontFamilyKey(Uri source, Uri? baseUri = null) {`

### `src/Avalonia.Base/Media/Fonts/FontFamilyLoader.cs`
- `public static class FontFamilyLoader`
- `public static IEnumerable<Uri> LoadFontAssets(Uri source) {`

### `src/Avalonia.Base/Media/Fonts/IFontCollection.cs`
- `public interface IFontCollection : IReadOnlyList<FontFamily>, IDisposable`

### `src/Avalonia.Base/Media/FormattedText.cs`
- `public const double DefaultRealToIdeal = 28800.0 / 96;`
- `public const double DefaultIdealToReal = 1 / DefaultRealToIdeal;`
- `public const int IdealInfiniteWidth = 0x3FFFFFFE;`
- `public const double RealInfiniteWidth = IdealInfiniteWidth * DefaultIdealToReal;`
- `public const double GreatestMultiplierOfEm = 100;`
- `public double[] GetMaxTextWidths() {`

### `src/Avalonia.Base/Media/Geometry.cs`
- `public event EventHandler? Changed;`
- `public abstract Geometry Clone();`
- `public double ContourLength => PlatformImpl?.ContourLength ?? 0;`
- `public static Geometry Combine(Geometry geometry1, RectangleGeometry geometry2, GeometryCombineMode combineMode, Transform? transform = null) {`
- `public bool TryGetPointAtDistance(double distance, out Point point) {`
- `public bool TryGetPointAndTangentAtDistance(double distance, out Point point, out Point tangent) {`
- `public bool TryGetSegment(double startDistance, double stopDistance, bool startOnBeginFigure, [NotNullWhen(true)] out Geometry? segmentGeometry) {`
- `public class GeometryTypeConverter : TypeConverter`

### `src/Avalonia.Base/Media/GeometryCollection.cs`
- `public sealed class GeometryCollection : AvaloniaList<Geometry>`
- `public GeometryCollection() {`
- `public GeometryCollection(IEnumerable<Geometry> items) : base(items) {`
- `public GeometryGroup? Parent { get; set; }`

### `src/Avalonia.Base/Media/GeometryDrawing.cs`
- `public static readonly StyledProperty<Geometry?> GeometryProperty = AvaloniaProperty.Register<GeometryDrawing, Geometry?>(nameof(Geometry));`
- `public static readonly StyledProperty<IBrush?> BrushProperty = AvaloniaProperty.Register<GeometryDrawing, IBrush?>(nameof(Brush), Brushes.Transparent);`
- `public static readonly StyledProperty<IPen?> PenProperty = AvaloniaProperty.Register<GeometryDrawing, IPen?>(nameof(Pen));`
- `public override Rect GetBounds() {`

### `src/Avalonia.Base/Media/GeometryGroup.cs`
- `public static readonly DirectProperty<GeometryGroup, GeometryCollection> ChildrenProperty = AvaloniaProperty.RegisterDirect<GeometryGroup, GeometryCollection> ( nameof(Children), o => o.Children,`
- `public override Geometry Clone() {`

### `src/Avalonia.Base/Media/GlyphMetrics.cs`
- `public readonly record struct GlyphMetrics`
- `public int XBearing { get; init; }`
- `public int YBearing{ get; init; }`

### `src/Avalonia.Base/Media/GlyphRun.cs`
- `public IGlyphTypeface GlyphTypeface { get; }`
- `public double FontRenderingEmSize {`
- `public Rect InkBounds => PlatformImpl.Item.Bounds;`
- `public GlyphRunMetrics Metrics => _glyphRunMetrics ??= CreateGlyphRunMetrics();`
- `public Point BaselineOrigin {`
- `public ReadOnlyMemory<char> Characters {`
- `public IReadOnlyList<GlyphInfo> GlyphInfos {`
- `public int BiDiLevel {`
- `public bool IsLeftToRight => ((BiDiLevel & 1) == 0);`
- `public double GetDistanceFromCharacterHit(CharacterHit characterHit) {`
- `public CharacterHit GetCharacterHitFromDistance(double distance, out bool isInside) {`
- `public CharacterHit GetNextCaretCharacterHit(CharacterHit characterHit) {`
- `public CharacterHit GetPreviousCaretCharacterHit(CharacterHit characterHit) {`
- `public int FindGlyphIndex(int characterIndex) {`
- `public CharacterHit FindNearestCharacterHit(int index, out double width) {`
- `public IReadOnlyList<float> GetIntersections(float lowerLimit, float upperLimit) {`
- `public IImmutableGlyphRunReference? TryCreateImmutableGlyphRunReference() => new ImmutableGlyphRunReference(PlatformImpl.Clone());`

### `src/Avalonia.Base/Media/GlyphRunDrawing.cs`
- `public sealed class GlyphRunDrawing : Drawing`
- `public static readonly StyledProperty<GlyphRun?> GlyphRunProperty = AvaloniaProperty.Register<GlyphRunDrawing, GlyphRun?>(nameof(GlyphRun));`
- `public override Rect GetBounds() {`

### `src/Avalonia.Base/Media/GlyphRunMetrics.cs`
- `public readonly record struct GlyphRunMetrics`
- `public int TrailingWhitespaceLength { get; init; }`
- `public int NewLineLength { get; init; }`
- `public int FirstCluster { get; init; }`
- `public int LastCluster { get; init; }`

### `src/Avalonia.Base/Media/GradientBrush.cs`
- `public abstract class GradientBrush : Brush, IGradientBrush, IMutableBrush`
- `public static readonly StyledProperty<GradientSpreadMethod> SpreadMethodProperty = AvaloniaProperty.Register<GradientBrush, GradientSpreadMethod>(nameof(SpreadMethod));`
- `public static readonly StyledProperty<GradientStops> GradientStopsProperty = AvaloniaProperty.Register<GradientBrush, GradientStops>(nameof(GradientStops));`
- `public GradientSpreadMethod SpreadMethod {`
- `public GradientStops GradientStops {`

### `src/Avalonia.Base/Media/GradientSpreadMethod.cs`
- `public enum GradientSpreadMethod`

### `src/Avalonia.Base/Media/GradientStop.cs`
- `public GradientStop() { }`
- `public GradientStop(Color color, double offset) {`

### `src/Avalonia.Base/Media/GradientStops.cs`
- `public class GradientStops : AvaloniaList<GradientStop>`
- `public GradientStops() {`

### `src/Avalonia.Base/Media/IConicGradientBrush.cs`
- `public interface IConicGradientBrush : IGradientBrush`

### `src/Avalonia.Base/Media/IDashStyle.cs`
- `public interface IDashStyle`

### `src/Avalonia.Base/Media/IExperimentalAcrylicMaterial.cs`
- `public interface IExperimentalAcrylicMaterial`

### `src/Avalonia.Base/Media/IGlyphTypeface.cs`
- `public interface IGlyphTypeface : IDisposable`

### `src/Avalonia.Base/Media/IGradientBrush.cs`
- `public interface IGradientBrush : IBrush`

### `src/Avalonia.Base/Media/IGradientStop.cs`
- `public interface IGradientStop`

### `src/Avalonia.Base/Media/IImageBrush.cs`
- `public interface IImageBrush : ITileBrush`
- `public interface IImageBrushSource`

### `src/Avalonia.Base/Media/IImmutableGlyphRunReference.cs`
- `public interface IImmutableGlyphRunReference : IDisposable`

### `src/Avalonia.Base/Media/ILinearGradientBrush.cs`
- `public interface ILinearGradientBrush : IGradientBrush`

### `src/Avalonia.Base/Media/IMutableExperimentalAcrylicMaterial.cs`
- `public interface IMutableExperimentalAcrylicMaterial : IExperimentalAcrylicMaterial`

### `src/Avalonia.Base/Media/IMutableTransform.cs`
- `public interface IMutableTransform : ITransform`

### `src/Avalonia.Base/Media/IPen.cs`
- `public interface IPen`

### `src/Avalonia.Base/Media/IRadialGradientBrush.cs`
- `public interface IRadialGradientBrush : IGradientBrush`

### `src/Avalonia.Base/Media/ISceneBrush.cs`
- `public interface ISceneBrush : ITileBrush`
- `public interface ISceneBrushContent : IImmutableBrush, IDisposable`

### `src/Avalonia.Base/Media/ISolidColorBrush.cs`
- `public interface ISolidColorBrush : IBrush`

### `src/Avalonia.Base/Media/ITileBrush.cs`
- `public interface ITileBrush : IBrush`

### `src/Avalonia.Base/Media/ImageBrush.cs`
- `public sealed class ImageBrush : TileBrush, IImageBrush, IMutableBrush`
- `public ImageBrush() {`
- `public ImageBrush(IImageBrushSource? source) {`

### `src/Avalonia.Base/Media/ImageDrawing.cs`
- `public sealed class ImageDrawing : Drawing`
- `public static readonly StyledProperty<IImage?> ImageSourceProperty = AvaloniaProperty.Register<ImageDrawing, IImage?>(nameof(ImageSource));`
- `public static readonly StyledProperty<Rect> RectProperty = AvaloniaProperty.Register<ImageDrawing, Rect>(nameof(Rect));`
- `public Rect Rect {`
- `public override Rect GetBounds() => Rect;`

### `src/Avalonia.Base/Media/Imaging/Bitmap.cs`
- `public static Bitmap DecodeToWidth(Stream stream, int width, BitmapInterpolationMode interpolationMode = BitmapInterpolationMode.HighQuality) {`
- `public static Bitmap DecodeToHeight(Stream stream, int height, BitmapInterpolationMode interpolationMode = BitmapInterpolationMode.HighQuality) {`
- `public Bitmap CreateScaledBitmap(PixelSize destinationSize, BitmapInterpolationMode interpolationMode = BitmapInterpolationMode.HighQuality) {`
- `public Vector Dpi => PlatformImpl.Item.Dpi;`
- `public PixelSize PixelSize => PlatformImpl.Item.PixelSize;`
- `public virtual PixelFormat? Format => (PlatformImpl.Item as IReadableBitmapImpl)?.Format;`
- `public virtual AlphaFormat? AlphaFormat => (PlatformImpl.Item as IReadableBitmapWithAlphaImpl)?.AlphaFormat;`
- `public virtual void CopyPixels(PixelRect sourceRect, IntPtr buffer, int bufferSize, int stride) {`
- `public void CopyPixels(ILockedFramebuffer buffer, AlphaFormat alphaFormat) {`

### `src/Avalonia.Base/Media/Imaging/BitmapInterpolationMode.cs`
- `public enum BitmapInterpolationMode : byte`

### `src/Avalonia.Base/Media/Imaging/CroppedBitmap.cs`
- `public static readonly StyledProperty<PixelRect> SourceRectProperty = AvaloniaProperty.Register<CroppedBitmap, PixelRect>(nameof(SourceRect));`
- `public event EventHandler? Invalidated;`
- `public PixelRect SourceRect {`

### `src/Avalonia.Base/Media/Imaging/RenderTargetBitmap.cs`
- `public class RenderTargetBitmap : Bitmap`
- `public RenderTargetBitmap(PixelSize pixelSize) : this(pixelSize, new Vector(96, 96)) {`
- `public RenderTargetBitmap(PixelSize pixelSize, Vector dpi) : this(RefCountable.Create(CreateImpl(pixelSize, dpi))) {`
- `public DrawingContext CreateDrawingContext() => CreateDrawingContext(true);`
- `public DrawingContext CreateDrawingContext(bool clear) {`

### `src/Avalonia.Base/Media/Imaging/WriteableBitmap.cs`
- `public class WriteableBitmap : Bitmap`
- `public WriteableBitmap(PixelSize size, Vector dpi, PixelFormat? format = null, AlphaFormat? alphaFormat = null) : this(CreatePlatformImpl(size, dpi, format, alphaFormat)) {`
- `public unsafe WriteableBitmap(PixelFormat format, AlphaFormat alphaFormat, IntPtr data, PixelSize size, Vector dpi, int stride) : this(size, dpi, format, alphaFormat) {`
- `public override PixelFormat? Format => _pixelFormatMemory?.Format ?? base.Format;`
- `public ILockedFramebuffer Lock() {`
- `public override void CopyPixels(PixelRect sourceRect, IntPtr buffer, int bufferSize, int stride) {`
- `public static WriteableBitmap Decode(Stream stream) {`
- `public new static WriteableBitmap DecodeToWidth(Stream stream, int width, BitmapInterpolationMode interpolationMode = BitmapInterpolationMode.HighQuality) {`
- `public new static WriteableBitmap DecodeToHeight(Stream stream, int height, BitmapInterpolationMode interpolationMode = BitmapInterpolationMode.HighQuality) {`

### `src/Avalonia.Base/Media/ImmediateDrawingContext.cs`
- `public Matrix CurrentTransform {`
- `public void DrawBitmap(Bitmap source, Rect rect) {`
- `public void DrawBitmap(Bitmap source, Rect sourceRect, Rect destRect) {`
- `public readonly record struct PushedState : IDisposable`
- `public enum PushedStateType`
- `public PushedState PushOpacity(double opacity, Rect bounds) {`
- `public PushedState PushOpacityMask(IImmutableBrush mask, Rect bounds) {`
- `public PushedState PushPostTransform(Matrix matrix) => PushSetTransform(CurrentTransform * matrix);`
- `public PushedState PushPreTransform(Matrix matrix) => PushSetTransform(matrix * CurrentTransform);`
- `public PushedState PushSetTransform(Matrix matrix) {`
- `public PushedState PushTransformContainer() {`

### `src/Avalonia.Base/Media/Immutable/ImmutableConicGradientBrush.cs`
- `public class ImmutableConicGradientBrush : ImmutableGradientBrush, IConicGradientBrush`
- `public ImmutableConicGradientBrush( IReadOnlyList<ImmutableGradientStop> gradientStops, double opacity = 1, ImmutableTransform? transform = null, RelativePoint? transformOrigin = null, GradientSpreadMethod spreadMethod = GradientSpreadMethod.Pad, RelativePoint? center = null, double angle = 0) : base(gradientStops, opacity, transform, transformOrigin, spreadMethod) {`
- `public ImmutableConicGradientBrush(ConicGradientBrush source) : base(source) {`
- `public RelativePoint Center { get; }`
- `public double Angle { get; }`

### `src/Avalonia.Base/Media/Immutable/ImmutableDashStyle.cs`
- `public class ImmutableDashStyle : IDashStyle, IEquatable<IDashStyle>`
- `public ImmutableDashStyle(IEnumerable<double>? dashes, double offset) {`
- `public IReadOnlyList<double> Dashes => _dashes;`

### `src/Avalonia.Base/Media/Immutable/ImmutableGradientBrush.cs`
- `public abstract class ImmutableGradientBrush : IGradientBrush, IImmutableBrush`
- `public IReadOnlyList<IGradientStop> GradientStops { get; }`
- `public double Opacity { get; }`
- `public RelativePoint TransformOrigin { get; }`
- `public GradientSpreadMethod SpreadMethod { get; }`

### `src/Avalonia.Base/Media/Immutable/ImmutableGradientStop.cs`
- `public class ImmutableGradientStop : IGradientStop`
- `public ImmutableGradientStop(double offset, Color color) {`

### `src/Avalonia.Base/Media/Immutable/ImmutableLinearGradientBrush.cs`
- `public class ImmutableLinearGradientBrush : ImmutableGradientBrush, ILinearGradientBrush`
- `public ImmutableLinearGradientBrush( IReadOnlyList<ImmutableGradientStop> gradientStops, double opacity = 1, ImmutableTransform? transform = null, RelativePoint? transformOrigin = null, GradientSpreadMethod spreadMethod = GradientSpreadMethod.Pad, RelativePoint? startPoint = null, RelativePoint? endPoint = null) : base(gradientStops, opacity, transform, transformOrigin, spreadMethod) {`
- `public ImmutableLinearGradientBrush(LinearGradientBrush source) : base(source) {`

### `src/Avalonia.Base/Media/Immutable/ImmutablePen.cs`
- `public class ImmutablePen : IPen, IEquatable<IPen>`
- `public ImmutablePen( uint color, double thickness = 1.0, ImmutableDashStyle? dashStyle = null, PenLineCap lineCap = PenLineCap.Flat, PenLineJoin lineJoin = PenLineJoin.Miter, double miterLimit = 10.0) : this(new ImmutableSolidColorBrush(color), thickness, dashStyle, lineCap, lineJoin, miterLimit) {`
- `public ImmutablePen( IImmutableBrush? brush, double thickness = 1.0, ImmutableDashStyle? dashStyle = null, PenLineCap lineCap = PenLineCap.Flat, PenLineJoin lineJoin = PenLineJoin.Miter, double miterLimit = 10.0) {`
- `public IDashStyle? DashStyle { get; }`
- `public PenLineCap LineCap { get; }`
- `public PenLineJoin LineJoin { get; }`
- `public double MiterLimit { get; }`

### `src/Avalonia.Base/Media/Immutable/ImmutableRadialGradientBrush.cs`
- `public class ImmutableRadialGradientBrush : ImmutableGradientBrush, IRadialGradientBrush`
- `public ImmutableRadialGradientBrush( IReadOnlyList<ImmutableGradientStop> gradientStops, double opacity = 1, ImmutableTransform? transform = null, RelativePoint? transformOrigin = null, GradientSpreadMethod spreadMethod = GradientSpreadMethod.Pad, RelativePoint? center = null, RelativePoint? gradientOrigin = null, double radius = 0.5) : this(gradientStops, opacity, transform, transformOrigin, spreadMethod, center, gradientOrigin, new RelativeScalar(radius, RelativeUnit.Relative), new RelativeScalar(radius, RelativeUnit.Relative) ) {`
- `public ImmutableRadialGradientBrush( IReadOnlyList<ImmutableGradientStop> gradientStops, double opacity = 1, ImmutableTransform? transform = null, RelativePoint? transformOrigin = null, GradientSpreadMethod spreadMethod = GradientSpreadMethod.Pad, RelativePoint? center = null, RelativePoint? gradientOrigin = null, RelativeScalar? radiusX = null, RelativeScalar? radiusY = null ) : base(gradientStops, opacity, transform, transformOrigin, spreadMethod) {`
- `public ImmutableRadialGradientBrush(RadialGradientBrush source) : base(source) {`
- `public RelativePoint Center { get; }`
- `public RelativeScalar RadiusX { get; }`
- `public RelativeScalar RadiusY { get; }`

### `src/Avalonia.Base/Media/Immutable/ImmutableSolidColorBrush.cs`
- `public double Opacity { get; }`
- `public RelativePoint TransformOrigin { get; }`

### `src/Avalonia.Base/Media/Immutable/ImmutableTextDecoration.cs`
- `public class ImmutableTextDecoration`
- `public ImmutableTextDecoration(TextDecorationLocation location, ImmutablePen pen, TextDecorationUnit penThicknessUnit, double penOffset, TextDecorationUnit penOffsetUnit) {`
- `public TextDecorationUnit PenThicknessUnit { get; }`
- `public double PenOffset { get; }`
- `public TextDecorationUnit PenOffsetUnit { get; }`

### `src/Avalonia.Base/Media/Immutable/ImmutableTileBrush.cs`
- `public abstract class ImmutableTileBrush : ITileBrush, IImmutableBrush`
- `public AlignmentX AlignmentX { get; }`
- `public AlignmentY AlignmentY { get; }`
- `public RelativeRect DestinationRect { get; }`
- `public double Opacity { get; }`
- `public RelativePoint TransformOrigin { get; }`
- `public RelativeRect SourceRect { get; }`
- `public TileMode TileMode { get; }`

### `src/Avalonia.Base/Media/Immutable/ImmutableTransform.cs`
- `public class ImmutableTransform : ITransform`
- `public ImmutableTransform(Matrix matrix) {`

### `src/Avalonia.Base/Media/ImmutableExperimentalAcrylicMaterial.cs`
- `public readonly struct ImmutableExperimentalAcrylicMaterial : IExperimentalAcrylicMaterial, IEquatable<ImmutableExperimentalAcrylicMaterial>`
- `public ImmutableExperimentalAcrylicMaterial(IExperimentalAcrylicMaterial brush) {`
- `public Color MaterialColor { get; }`
- `public Color GetEffectiveTintColor() {`

### `src/Avalonia.Base/Media/LineGeometry.cs`
- `public class LineGeometry : Geometry`
- `public LineGeometry() {`
- `public LineGeometry(Point startPoint, Point endPoint) : this() {`
- `public override Geometry Clone() {`

### `src/Avalonia.Base/Media/LineSegment.cs`
- `public sealed class LineSegment : PathSegment`
- `public static readonly StyledProperty<Point> PointProperty = AvaloniaProperty.Register<LineSegment, Point>(nameof(Point));`
- `public Point Point {`

### `src/Avalonia.Base/Media/MaterialExtensions.cs`
- `public static class MaterialExtensions`

### `src/Avalonia.Base/Media/MatrixTransform.cs`
- `public sealed class MatrixTransform : Transform`
- `public static readonly StyledProperty<Matrix> MatrixProperty = AvaloniaProperty.Register<MatrixTransform, Matrix>(nameof(Matrix), Matrix.Identity);`
- `public MatrixTransform() {`
- `public MatrixTransform(Matrix matrix) : this() {`
- `public Matrix Matrix {`

### `src/Avalonia.Base/Media/MediaExtensions.cs`
- `public static class MediaExtensions`
- `public static Vector CalculateScaling( this Stretch stretch, Size destinationSize, Size sourceSize, StretchDirection stretchDirection = StretchDirection.Both) {`
- `public static Size CalculateSize( this Stretch stretch, Size destinationSize, Size sourceSize, StretchDirection stretchDirection = StretchDirection.Both) {`

### `src/Avalonia.Base/Media/PathFigure.cs`
- `public sealed class PathFigure : AvaloniaObject`
- `public static readonly StyledProperty<bool> IsFilledProperty = AvaloniaProperty.Register<PathFigure, bool>(nameof(IsFilled), true);`
- `public static readonly DirectProperty<PathFigure, PathSegments?> SegmentsProperty = AvaloniaProperty.RegisterDirect<PathFigure, PathSegments?>( nameof(Segments), f => f.Segments,`
- `public PathFigure() {`
- `public bool IsFilled {`
- `public PathSegments? Segments {`

### `src/Avalonia.Base/Media/PathGeometry.cs`
- `public static readonly DirectProperty<PathGeometry, PathFigures?> FiguresProperty = AvaloniaProperty.RegisterDirect<PathGeometry, PathFigures?>(nameof(Figures), g => g.Figures, (g, f) => g.Figures = f);`
- `public PathFigures? Figures {`

### `src/Avalonia.Base/Media/PathGeometryCollections.cs`
- `public sealed class PathFigures : AvaloniaList<PathFigure>`
- `public PathSegments() {`
- `public PathSegments(IEnumerable<PathSegment> collection) : base(collection) {`
- `public PathSegments(int capacity) : base(capacity) {`

### `src/Avalonia.Base/Media/PathMarkupParser.cs`
- `public class PathMarkupParser : IDisposable`
- `public PathMarkupParser(IGeometryContext geometryContext) {`

### `src/Avalonia.Base/Media/PathSegment.cs`
- `public abstract class PathSegment : AvaloniaObject`
- `public static readonly StyledProperty<bool> IsStrokedProperty = AvaloniaProperty.Register<PathSegment, bool>(nameof(IsStroked), true);`
- `public bool IsStroked {`

### `src/Avalonia.Base/Media/Pen.cs`
- `public static readonly StyledProperty<IBrush?> BrushProperty = AvaloniaProperty.Register<Pen, IBrush?>(nameof(Brush));`
- `public static readonly StyledProperty<double> ThicknessProperty = AvaloniaProperty.Register<Pen, double>(nameof(Thickness), 1.0);`
- `public static readonly StyledProperty<IDashStyle?> DashStyleProperty = AvaloniaProperty.Register<Pen, IDashStyle?>(nameof(DashStyle));`
- `public static readonly StyledProperty<PenLineCap> LineCapProperty = AvaloniaProperty.Register<Pen, PenLineCap>(nameof(LineCap));`
- `public static readonly StyledProperty<PenLineJoin> LineJoinProperty = AvaloniaProperty.Register<Pen, PenLineJoin>(nameof(LineJoin));`
- `public static readonly StyledProperty<double> MiterLimitProperty = AvaloniaProperty.Register<Pen, double>(nameof(MiterLimit), 10.0);`
- `public IDashStyle? DashStyle {`
- `public PenLineCap LineCap {`
- `public PenLineJoin LineJoin {`
- `public double MiterLimit {`

### `src/Avalonia.Base/Media/PolyBezierSegment.cs`
- `public sealed class PolyBezierSegment : PathSegment`
- `public PolyBezierSegment() {`
- `public PolyBezierSegment(IEnumerable<Point> points, bool isStroked) {`
- `public Points? Points {`

### `src/Avalonia.Base/Media/PolyLineSegment.cs`
- `public sealed class PolyLineSegment : PathSegment`
- `public IList<Point> Points {`
- `public PolyLineSegment() {`
- `public PolyLineSegment(IEnumerable<Point> points) {`

### `src/Avalonia.Base/Media/PolylineGeometry.cs`
- `public class PolylineGeometry : Geometry`
- `public static readonly StyledProperty<bool> IsFilledProperty = AvaloniaProperty.Register<PolylineGeometry, bool>(nameof(IsFilled));`
- `public PolylineGeometry() {`
- `public PolylineGeometry(IEnumerable<Point> points, bool isFilled) {`
- `public PolylineGeometry(IEnumerable<Point> points, bool isFilled, FillRule fillRule) {`
- `public IList<Point> Points {`
- `public bool IsFilled {`
- `public override Geometry Clone() {`

### `src/Avalonia.Base/Media/PreciseEllipticArcHelper.cs`
- `public sealed class EllipticalArc`
- `public bool DrawInOppositeDirection { get; set; }`
- `public EllipticalArc() {`
- `public EllipticalArc(Point center, double a, double b, double theta, double lambda1, double lambda2, bool isPieSlice) : this(center.X, center.Y, a, b, theta, lambda1, lambda2, isPieSlice) {`
- `public EllipticalArc(double cx, double cy, double a, double b, double theta, double lambda1, double lambda2, bool isPieSlice) {`
- `public EllipticalArc(Point center, double a, double b, double theta) : this(center.X, center.Y, a, b, theta) {`
- `public EllipticalArc(double cx, double cy, double a, double b, double theta) {`
- `public void SetMaxDegree(int maxDegree) {`
- `public void SetDefaultFlatness(double defaultFlatness) {`
- `public double EstimateError(int degree, double etaA, double etaB) {`
- `public Point PointAt(double lambda) {`
- `public Rect GetBounds() {`
- `public void BuildArc(StreamGeometryContext path) {`
- `public void BuildArc(StreamGeometryContext path, int degree, double threshold, bool openNewFigure) {`
- `public static void BuildArc(StreamGeometryContext path, Point p1, Point p2, Size size, double theta, bool isLargeArc, bool clockwise) {`
- `public bool Intersects(double x, double y, double w, double h) {`
- `public bool Intersects(Rect r) {`

### `src/Avalonia.Base/Media/QuadraticBezierSegment .cs`
- `public sealed class QuadraticBezierSegment : PathSegment`
- `public static readonly StyledProperty<Point> Point1Property = AvaloniaProperty.Register<QuadraticBezierSegment, Point>(nameof(Point1));`
- `public static readonly StyledProperty<Point> Point2Property = AvaloniaProperty.Register<QuadraticBezierSegment, Point>(nameof(Point2));`
- `public Point Point1 {`
- `public Point Point2 {`

### `src/Avalonia.Base/Media/RadialGradientBrush.cs`
- `public static readonly StyledProperty<RelativePoint> CenterProperty = AvaloniaProperty.Register<RadialGradientBrush, RelativePoint>( nameof(Center), RelativePoint.Center);`
- `public static readonly StyledProperty<RelativePoint> GradientOriginProperty = AvaloniaProperty.Register<RadialGradientBrush, RelativePoint>( nameof(GradientOrigin), RelativePoint.Center);`
- `public static readonly StyledProperty<double> RadiusProperty = AvaloniaProperty.Register<RadialGradientBrush, double>( nameof(Radius), 0.5);`
- `public RelativePoint Center {`
- `public RelativeScalar RadiusX {`
- `public RelativeScalar RadiusY {`
- `public double Radius {`

### `src/Avalonia.Base/Media/RectangleGeometry.cs`
- `public class RectangleGeometry : Geometry`
- `public static readonly StyledProperty<Rect> RectProperty = AvaloniaProperty.Register<RectangleGeometry, Rect>(nameof(Rect));`
- `public RectangleGeometry() {`
- `public RectangleGeometry(Rect rect) {`
- `public RectangleGeometry(Rect rect, double radiusX, double radiusY) {`
- `public double RadiusX {`
- `public double RadiusY {`
- `public Rect Rect {`
- `public override Geometry Clone() => new RectangleGeometry(Rect, RadiusX, RadiusY);`

### `src/Avalonia.Base/Media/RenderOptions.cs`
- `public readonly record struct RenderOptions`
- `public BitmapInterpolationMode BitmapInterpolationMode { get; init; }`
- `public EdgeMode EdgeMode { get; init; }`
- `public TextRenderingMode TextRenderingMode { get; init; }`
- `public bool? RequiresFullOpacityHandling { get; init; }`
- `public static BitmapInterpolationMode GetBitmapInterpolationMode(Visual visual) {`
- `public static void SetBitmapInterpolationMode(Visual visual, BitmapInterpolationMode value) {`
- `public static BitmapBlendingMode GetBitmapBlendingMode(Visual visual) {`
- `public static void SetBitmapBlendingMode(Visual visual, BitmapBlendingMode value) {`
- `public static EdgeMode GetEdgeMode(Visual visual) {`
- `public static void SetEdgeMode(Visual visual, EdgeMode value) {`
- `public static TextRenderingMode GetTextRenderingMode(Visual visual) {`
- `public static void SetTextRenderingMode(Visual visual, TextRenderingMode value) {`
- `public static bool? GetRequiresFullOpacityHandling(Visual visual) {`
- `public static void SetRequiresFullOpacityHandling(Visual visual, bool? value) {`
- `public RenderOptions MergeWith(RenderOptions other) {`

### `src/Avalonia.Base/Media/RotateTransform.cs`
- `public sealed class RotateTransform : Transform`
- `public static readonly StyledProperty<double> AngleProperty = AvaloniaProperty.Register<RotateTransform, double>(nameof(Angle));`
- `public static readonly StyledProperty<double> CenterXProperty = AvaloniaProperty.Register<RotateTransform, double>(nameof(CenterX));`
- `public static readonly StyledProperty<double> CenterYProperty = AvaloniaProperty.Register<RotateTransform, double>(nameof(CenterY));`
- `public RotateTransform() {`
- `public RotateTransform(double angle) : this() {`
- `public RotateTransform(double angle, double centerX, double centerY) : this() {`
- `public double Angle {`
- `public double CenterX {`
- `public double CenterY {`

### `src/Avalonia.Base/Media/ScaleTransform.cs`
- `public sealed class ScaleTransform : Transform`
- `public static readonly StyledProperty<double> ScaleXProperty = AvaloniaProperty.Register<ScaleTransform, double>(nameof(ScaleX), 1);`
- `public static readonly StyledProperty<double> ScaleYProperty = AvaloniaProperty.Register<ScaleTransform, double>(nameof(ScaleY), 1);`
- `public ScaleTransform() {`
- `public ScaleTransform(double scaleX, double scaleY) : this() {`
- `public double ScaleX {`
- `public double ScaleY {`

### `src/Avalonia.Base/Media/SkewTransform.cs`
- `public sealed class SkewTransform : Transform`
- `public static readonly StyledProperty<double> AngleXProperty = AvaloniaProperty.Register<SkewTransform, double>(nameof(AngleX));`
- `public static readonly StyledProperty<double> AngleYProperty = AvaloniaProperty.Register<SkewTransform, double>(nameof(AngleY));`
- `public SkewTransform() {`
- `public SkewTransform(double angleX, double angleY) : this() {`
- `public double AngleX {`
- `public double AngleY {`

### `src/Avalonia.Base/Media/StreamGeometry.cs`
- `public override Geometry Clone() {`

### `src/Avalonia.Base/Media/StreamGeometryContext.cs`
- `public class StreamGeometryContext : IGeometryContext, IGeometryContext2`
- `public StreamGeometryContext(IStreamGeometryContextImpl impl) {`
- `public void SetFillRule(FillRule fillRule) {`
- `public void ArcTo(Point point, Size size, double rotationAngle, bool isLargeArc, SweepDirection sweepDirection) {`
- `public void PreciseArcTo(Point point, Size size, double rotationAngle, bool isLargeArc, SweepDirection sweepDirection) {`
- `public void BeginFigure(Point startPoint, bool isFilled) {`
- `public void CubicBezierTo(Point controlPoint1, Point controlPoint2, Point endPoint) {`
- `public void QuadraticBezierTo(Point controlPoint , Point endPoint) {`
- `public void LineTo(Point endPoint) {`
- `public void EndFigure(bool isClosed) {`
- `public void LineTo(Point point, bool isStroked) {`
- `public void ArcTo(Point point, Size size, double rotationAngle, bool isLargeArc, SweepDirection sweepDirection, bool isStroked) {`
- `public void CubicBezierTo(Point controlPoint1, Point controlPoint2, Point endPoint, bool isStroked) {`
- `public void QuadraticBezierTo(Point controlPoint, Point endPoint, bool isStroked) {`

### `src/Avalonia.Base/Media/SweepDirection.cs`
- `public enum SweepDirection`

### `src/Avalonia.Base/Media/TextCollapsingCreateInfo.cs`
- `public readonly record struct TextCollapsingCreateInfo`
- `public readonly TextRunProperties TextRunProperties;`
- `public TextCollapsingCreateInfo(double width, TextRunProperties textRunProperties, FlowDirection flowDirection) {`

### `src/Avalonia.Base/Media/TextDecoration.cs`
- `public class TextDecoration : AvaloniaObject`
- `public static readonly StyledProperty<TextDecorationLocation> LocationProperty = AvaloniaProperty.Register<TextDecoration, TextDecorationLocation>(nameof(Location));`
- `public static readonly StyledProperty<TextDecorationUnit> StrokeThicknessUnitProperty = AvaloniaProperty.Register<TextDecoration, TextDecorationUnit>(nameof(StrokeThicknessUnit));`
- `public static readonly StyledProperty<double> StrokeOffsetProperty = AvaloniaProperty.Register<TextDecoration, double>(nameof(StrokeOffset));`
- `public static readonly StyledProperty<TextDecorationUnit> StrokeOffsetUnitProperty = AvaloniaProperty.Register<TextDecoration, TextDecorationUnit>(nameof(StrokeOffsetUnit));`
- `public TextDecorationUnit StrokeThicknessUnit {`
- `public double StrokeOffset {`
- `public TextDecorationUnit StrokeOffsetUnit {`

### `src/Avalonia.Base/Media/TextDecorationCollection.cs`
- `public class TextDecorationCollection : AvaloniaList<TextDecoration>`
- `public TextDecorationCollection() {`
- `public TextDecorationCollection(IEnumerable<TextDecoration> textDecorations) : base(textDecorations) {`

### `src/Avalonia.Base/Media/TextDecorationLocation.cs`
- `public enum TextDecorationLocation`

### `src/Avalonia.Base/Media/TextDecorationUnit.cs`
- `public enum TextDecorationUnit`

### `src/Avalonia.Base/Media/TextDecorations.cs`
- `public static TextDecorationCollection Strikethrough { get; }`
- `public static TextDecorationCollection Overline { get; }`

### `src/Avalonia.Base/Media/TextFormatting/DrawableTextRun.cs`
- `public abstract class DrawableTextRun : TextRun`

### `src/Avalonia.Base/Media/TextFormatting/GenericTextParagraphProperties.cs`
- `public sealed class GenericTextParagraphProperties : TextParagraphProperties`
- `public GenericTextParagraphProperties(TextRunProperties defaultTextRunProperties, TextAlignment textAlignment = TextAlignment.Left, TextWrapping textWrap = TextWrapping.NoWrap, double lineHeight = 0, double letterSpacing = 0) {`
- `public GenericTextParagraphProperties( FlowDirection flowDirection, TextAlignment textAlignment, bool firstLineInParagraph, bool alwaysCollapsible, TextRunProperties defaultTextRunProperties, TextWrapping textWrap, double lineHeight, double indent, double letterSpacing) {`
- `public GenericTextParagraphProperties(TextParagraphProperties textParagraphProperties) : this(textParagraphProperties.FlowDirection, textParagraphProperties.TextAlignment, textParagraphProperties.FirstLineInParagraph, textParagraphProperties.AlwaysCollapsible, textParagraphProperties.DefaultTextRunProperties, textParagraphProperties.TextWrapping, textParagraphProperties.LineHeight, textParagraphProperties.Indent, textParagraphProperties.LetterSpacing) {`
- `public override bool FirstLineInParagraph { get; }`
- `public override bool AlwaysCollapsible { get; }`
- `public override TextRunProperties DefaultTextRunProperties { get; }`
- `public override double Indent { get; }`

### `src/Avalonia.Base/Media/TextFormatting/GenericTextRunProperties.cs`
- `public class GenericTextRunProperties : TextRunProperties`
- `public GenericTextRunProperties(Typeface typeface, double fontRenderingEmSize = DefaultFontRenderingEmSize, TextDecorationCollection? textDecorations = null, IBrush? foregroundBrush = null, IBrush? backgroundBrush = null, BaselineAlignment baselineAlignment = BaselineAlignment.Baseline, CultureInfo? cultureInfo = null) : this(typeface, null, fontRenderingEmSize, textDecorations, foregroundBrush, backgroundBrush, baselineAlignment, cultureInfo) {`
- `public GenericTextRunProperties( Typeface typeface, FontFeatureCollection? fontFeatures, double fontRenderingEmSize = DefaultFontRenderingEmSize, TextDecorationCollection? textDecorations = null, IBrush? foregroundBrush = null, IBrush? backgroundBrush = null, BaselineAlignment baselineAlignment = BaselineAlignment.Baseline, CultureInfo? cultureInfo = null) {`
- `public override double FontRenderingEmSize { get; }`
- `public override IBrush? ForegroundBrush { get; }`
- `public override IBrush? BackgroundBrush { get; }`
- `public override FontFeatureCollection? FontFeatures { get; }`
- `public override BaselineAlignment BaselineAlignment { get; }`

### `src/Avalonia.Base/Media/TextFormatting/GlyphInfo.cs`
- `public readonly record struct GlyphInfo(ushort GlyphIndex, int GlyphCluster, double GlyphAdvance, Vector GlyphOffset = default)`
- `public ushort GlyphIndex { get; } = GlyphIndex;`
- `public int GlyphCluster { get; } = GlyphCluster;`
- `public double GlyphAdvance { get; } = GlyphAdvance;`
- `public Vector GlyphOffset { get; } = GlyphOffset;`

### `src/Avalonia.Base/Media/TextFormatting/ITextSource.cs`
- `public interface ITextSource`

### `src/Avalonia.Base/Media/TextFormatting/JustificationProperties.cs`
- `public abstract class JustificationProperties`
- `public abstract void Justify(TextLine textLine);`

### `src/Avalonia.Base/Media/TextFormatting/LogicalDirection.cs`
- `public enum LogicalDirection`

### `src/Avalonia.Base/Media/TextFormatting/ShapedBuffer.cs`
- `public sealed class ShapedBuffer : IReadOnlyList<GlyphInfo>, IDisposable`
- `public ShapedBuffer(ReadOnlyMemory<char> text, int bufferLength, IGlyphTypeface glyphTypeface, double fontRenderingEmSize, sbyte bidiLevel) {`
- `public int Length => _glyphInfos.Length;`
- `public IGlyphTypeface GlyphTypeface { get; }`
- `public double FontRenderingEmSize { get; }`
- `public sbyte BidiLevel { get; private set; }`
- `public bool IsLeftToRight => (BidiLevel & 1) == 0;`
- `public void Reverse() {`
- `public SplitResult<ShapedBuffer> Split(int textLength) {`

### `src/Avalonia.Base/Media/TextFormatting/ShapedTextRun.cs`
- `public sealed class ShapedTextRun : DrawableTextRun, IDisposable`
- `public ShapedTextRun(ShapedBuffer shapedBuffer, TextRunProperties properties) {`
- `public bool IsReversed { get; private set; }`
- `public sbyte BidiLevel => ShapedBuffer.BidiLevel;`
- `public ShapedBuffer ShapedBuffer { get; }`
- `public override int Length => ShapedBuffer.Text.Length;`
- `public TextMetrics TextMetrics { get; }`
- `public bool TryMeasureCharacters(double availableWidth, out int length) {`

### `src/Avalonia.Base/Media/TextFormatting/SplitResult.cs`
- `public readonly struct SplitResult<T>`
- `public SplitResult(T? first, T? second) {`
- `public T? First { get; }`
- `public T? Second { get; }`
- `public void Deconstruct(out T? first, out T? second) {`

### `src/Avalonia.Base/Media/TextFormatting/TextBounds.cs`
- `public sealed class TextBounds`
- `public IList<TextRunBounds> TextRunBounds { get; }`

### `src/Avalonia.Base/Media/TextFormatting/TextCharacters.cs`
- `public class TextCharacters : TextRun`
- `public TextCharacters(string text, TextRunProperties textRunProperties) : this(text.AsMemory(), textRunProperties) {`
- `public TextCharacters(ReadOnlyMemory<char> text, TextRunProperties textRunProperties) {`
- `public override int Length => Text.Length;`

### `src/Avalonia.Base/Media/TextFormatting/TextCollapsingProperties.cs`
- `public abstract class TextCollapsingProperties`
- `public abstract TextRun Symbol { get; }`
- `public abstract TextRun[]? Collapse(TextLine textLine);`
- `public static TextRun[] CreateCollapsedRuns(TextLine textLine, int collapsedLength, FlowDirection flowDirection, TextRun shapedSymbol) {`

### `src/Avalonia.Base/Media/TextFormatting/TextEndOfLine.cs`
- `public class TextEndOfLine : TextRun`
- `public TextEndOfLine(int textSourceLength = DefaultTextSourceLength) {`
- `public override int Length { get; }`

### `src/Avalonia.Base/Media/TextFormatting/TextEndOfParagraph.cs`
- `public class TextEndOfParagraph : TextEndOfLine`
- `public TextEndOfParagraph() {`
- `public TextEndOfParagraph(int textSourceLength) : base(textSourceLength) {`

### `src/Avalonia.Base/Media/TextFormatting/TextFormatter.cs`
- `public abstract class TextFormatter`
- `public static TextFormatter Current {`
- `public abstract TextLine? FormatLine(ITextSource textSource, int firstTextSourceIndex, double paragraphWidth, TextParagraphProperties paragraphProperties, TextLineBreak? previousLineBreak = null);`
- `public static ShapedTextRun CreateSymbol(TextRun textRun, FlowDirection flowDirection) {`

### `src/Avalonia.Base/Media/TextFormatting/TextLayout.cs`
- `public IReadOnlyList<TextLine> TextLines => _textLines;`
- `public IEnumerable<Rect> HitTestTextRange(int start, int length) {`
- `public TextHitTestResult HitTestPoint(in Point point) {`
- `public int GetLineIndexFromCharacterIndex(int charIndex, bool trailingEdge) {`

### `src/Avalonia.Base/Media/TextFormatting/TextLeadingPrefixCharacterEllipsis.cs`
- `public sealed class TextLeadingPrefixCharacterEllipsis : TextCollapsingProperties`
- `public TextLeadingPrefixCharacterEllipsis( string ellipsis, int prefixLength, double width, TextRunProperties textRunProperties, FlowDirection flowDirection) {`
- `public override TextRun Symbol { get; }`
- `public override TextRun[]? Collapse(TextLine textLine) {`

### `src/Avalonia.Base/Media/TextFormatting/TextLine.cs`
- `public abstract class TextLine : IDisposable`
- `public abstract IReadOnlyList<TextRun> TextRuns { get; }`
- `public abstract int FirstTextSourceIndex { get; }`
- `public abstract int Length { get; }`
- `public abstract TextLineBreak? TextLineBreak { get; }`
- `public abstract bool HasCollapsed { get; }`
- `public abstract bool HasOverflowed { get; }`
- `public abstract int NewLineLength { get; }`
- `public abstract int TrailingWhitespaceLength { get; }`
- `public abstract TextLine Collapse(params TextCollapsingProperties?[] collapsingPropertiesList);`
- `public abstract void Justify(JustificationProperties justificationProperties);`
- `public abstract CharacterHit GetCharacterHitFromDistance(double distance);`
- `public abstract double GetDistanceFromCharacterHit(CharacterHit characterHit);`
- `public abstract CharacterHit GetNextCaretCharacterHit(CharacterHit characterHit);`
- `public abstract CharacterHit GetPreviousCaretCharacterHit(CharacterHit characterHit);`
- `public abstract CharacterHit GetBackspaceCaretCharacterHit(CharacterHit characterHit);`
- `public abstract IReadOnlyList<TextBounds> GetTextBounds(int firstTextSourceCharacterIndex, int textLength);`

### `src/Avalonia.Base/Media/TextFormatting/TextLineBreak.cs`
- `public class TextLineBreak`
- `public TextLineBreak(TextEndOfLine? textEndOfLine = null, FlowDirection flowDirection = FlowDirection.LeftToRight, bool isSplit = false) {`
- `public TextEndOfLine? TextEndOfLine { get; }`
- `public bool IsSplit { get; }`

### `src/Avalonia.Base/Media/TextFormatting/TextLineMetrics.cs`
- `public readonly record struct TextLineMetrics`
- `public bool HasOverflowed { get; init; }`
- `public int NewlineLength { get; init; }`
- `public double TextBaseline { get; init; }`
- `public int TrailingWhitespaceLength { get; init; }`

### `src/Avalonia.Base/Media/TextFormatting/TextMetrics.cs`
- `public readonly record struct TextMetrics`
- `public TextMetrics(IGlyphTypeface glyphTypeface, double fontRenderingEmSize) {`
- `public double FontRenderingEmSize { get; }`
- `public double Ascent { get; }`
- `public double Descent { get; }`
- `public double LineGap { get; }`
- `public double UnderlineThickness { get; }`
- `public double UnderlinePosition { get; }`
- `public double StrikethroughThickness { get; }`
- `public double StrikethroughPosition { get; }`

### `src/Avalonia.Base/Media/TextFormatting/TextParagraphProperties.cs`
- `public abstract class TextParagraphProperties`
- `public abstract bool FirstLineInParagraph { get; }`
- `public virtual bool AlwaysCollapsible {`
- `public abstract TextRunProperties DefaultTextRunProperties { get; }`
- `public abstract double Indent { get; }`
- `public virtual double ParagraphIndent {`
- `public virtual double DefaultIncrementalTab => 0;`

### `src/Avalonia.Base/Media/TextFormatting/TextRange.cs`
- `public readonly record struct TextRange`
- `public TextRange(int start, int length) {`
- `public int Length { get; }`
- `public TextRange Take(int length) {`
- `public TextRange Skip(int length) {`

### `src/Avalonia.Base/Media/TextFormatting/TextRun.cs`
- `public abstract class TextRun`
- `public const int DefaultTextSourceLength = 1;`
- `public virtual int Length => DefaultTextSourceLength;`

### `src/Avalonia.Base/Media/TextFormatting/TextRunBounds.cs`
- `public readonly record struct TextRunBounds`
- `public int TextSourceCharacterIndex { get; }`
- `public int Length { get; }`
- `public TextRun TextRun { get; }`

### `src/Avalonia.Base/Media/TextFormatting/TextRunProperties.cs`
- `public abstract class TextRunProperties : IEquatable<TextRunProperties>`
- `public abstract double FontRenderingEmSize { get; }`
- `public abstract IBrush? ForegroundBrush { get; }`
- `public abstract IBrush? BackgroundBrush { get; }`
- `public virtual FontFeatureCollection? FontFeatures => null;`
- `public virtual BaselineAlignment BaselineAlignment => BaselineAlignment.Baseline;`

### `src/Avalonia.Base/Media/TextFormatting/TextShaper.cs`
- `public class TextShaper`
- `public TextShaper(ITextShaperImpl platformImpl) {`
- `public static TextShaper Current {`
- `public ShapedBuffer ShapeText(ReadOnlyMemory<char> text, TextShaperOptions options = default) {`
- `public ShapedBuffer ShapeText(string text, TextShaperOptions options = default) {`

### `src/Avalonia.Base/Media/TextFormatting/TextShaperOptions.cs`
- `public readonly record struct TextShaperOptions`
- `public TextShaperOptions( IGlyphTypeface typeface, double fontRenderingEmSize = 12, sbyte bidiLevel = 0, CultureInfo? culture = null, double incrementalTabWidth = 0, double letterSpacing = 0) : this(typeface, null, fontRenderingEmSize, bidiLevel, culture, incrementalTabWidth, letterSpacing) {`
- `public TextShaperOptions( IGlyphTypeface typeface, IReadOnlyList<FontFeature>? fontFeatures, double fontRenderingEmSize = 12, sbyte bidiLevel = 0, CultureInfo? culture = null, double incrementalTabWidth = 0, double letterSpacing = 0) {`
- `public double FontRenderingEmSize { get; }`
- `public sbyte BidiLevel { get; }`
- `public CultureInfo? Culture { get; }`
- `public double IncrementalTabWidth { get; }`
- `public IReadOnlyList<FontFeature>? FontFeatures { get; }`

### `src/Avalonia.Base/Media/TextFormatting/TextTrailingCharacterEllipsis.cs`
- `public sealed class TextTrailingCharacterEllipsis : TextCollapsingProperties`
- `public TextTrailingCharacterEllipsis(string ellipsis, double width, TextRunProperties textRunProperties, FlowDirection flowDirection) {`
- `public override TextRun Symbol { get; }`
- `public override TextRun[]? Collapse(TextLine textLine) {`

### `src/Avalonia.Base/Media/TextFormatting/TextTrailingWordEllipsis.cs`
- `public sealed class TextTrailingWordEllipsis : TextCollapsingProperties`
- `public TextTrailingWordEllipsis( string ellipsis, double width, TextRunProperties textRunProperties, FlowDirection flowDirection ) {`
- `public override TextRun Symbol { get; }`
- `public override TextRun[]? Collapse(TextLine textLine) {`

### `src/Avalonia.Base/Media/TextFormatting/Unicode/BiDiClass.cs`
- `public enum BidiClass`

### `src/Avalonia.Base/Media/TextFormatting/Unicode/BiDiPairedBracketType.cs`
- `public enum BidiPairedBracketType`

### `src/Avalonia.Base/Media/TextFormatting/Unicode/Codepoint.cs`
- `public readonly record struct Codepoint`
- `public static Codepoint ReplacementCodepoint {`
- `public Codepoint(uint value) => _value = value;`
- `public GeneralCategory GeneralCategory => UnicodeData.GetGeneralCategory(_value);`
- `public Script Script => UnicodeData.GetScript(_value);`
- `public BidiClass BiDiClass => UnicodeData.GetBiDiClass(_value);`
- `public BidiPairedBracketType PairedBracketType => UnicodeData.GetBiDiPairedBracketType(_value);`
- `public LineBreakClass LineBreakClass => UnicodeData.GetLineBreakClass(_value);`
- `public GraphemeBreakClass GraphemeBreakClass => UnicodeData.GetGraphemeClusterBreak(_value);`
- `public EastAsianWidthClass EastAsianWidthClass => UnicodeData.GetEastAsianWidthClass(_value);`
- `public bool IsEastAsian {`
- `public bool IsBreakChar {`
- `public bool IsWhiteSpace {`
- `public bool TryGetPairedBracket(out Codepoint codepoint) {`
- `public static implicit operator uint(Codepoint codepoint) {`
- `public static Codepoint ReadAt(ReadOnlySpan<char> text, int index, out int count) {`
- `public static bool IsInRangeInclusive(Codepoint cp, uint lowerBound, uint upperBound) => IsInRangeInclusive(cp._value, lowerBound, upperBound);`

### `src/Avalonia.Base/Media/TextFormatting/Unicode/CodepointEnumerator.cs`
- `public ref struct CodepointEnumerator`
- `public CodepointEnumerator(ReadOnlySpan<char> text) => _text = text;`
- `public bool MoveNext(out Codepoint codepoint) {`

### `src/Avalonia.Base/Media/TextFormatting/Unicode/EastAsianWidthClass.cs`
- `public enum EastAsianWidthClass`

### `src/Avalonia.Base/Media/TextFormatting/Unicode/GeneralCategory.cs`
- `public enum GeneralCategory`

### `src/Avalonia.Base/Media/TextFormatting/Unicode/Grapheme.cs`
- `public readonly ref struct Grapheme`
- `public Grapheme(Codepoint firstCodepoint, int offset, int length) {`
- `public Codepoint FirstCodepoint { get; }`
- `public int Length { get; }`

### `src/Avalonia.Base/Media/TextFormatting/Unicode/GraphemeBreakClass.cs`
- `public enum GraphemeBreakClass`

### `src/Avalonia.Base/Media/TextFormatting/Unicode/GraphemeEnumerator.cs`
- `public ref struct GraphemeEnumerator`
- `public GraphemeEnumerator(ReadOnlySpan<char> text) {`
- `public bool MoveNext(out Grapheme grapheme) {`

### `src/Avalonia.Base/Media/TextFormatting/Unicode/LineBreak.cs`
- `public readonly record struct LineBreak`
- `public LineBreak(int positionMeasure, int positionWrap, bool required = false) {`
- `public int PositionMeasure { get; }`
- `public int PositionWrap { get; }`

### `src/Avalonia.Base/Media/TextFormatting/Unicode/LineBreakClass.cs`
- `public enum LineBreakClass`

### `src/Avalonia.Base/Media/TextFormatting/Unicode/LineBreakEnumerator.cs`
- `public ref struct LineBreakEnumerator`
- `public readonly ReadOnlySpan<char> _text;`
- `public LineBreakEnumerator(ReadOnlySpan<char> text) {`
- `public bool MoveNext([NotNullWhen(true)] out LineBreak lineBreak) {`

### `src/Avalonia.Base/Media/TextFormatting/UnshapedTextRun.cs`
- `public sealed class UnshapedTextRun : TextRun`
- `public UnshapedTextRun(ReadOnlyMemory<char> text, TextRunProperties properties, sbyte biDiLevel) {`
- `public override int Length => Text.Length;`
- `public sbyte BidiLevel { get; }`

### `src/Avalonia.Base/Media/TextHitTestResult.cs`
- `public readonly record struct TextHitTestResult`
- `public TextHitTestResult(CharacterHit characterHit, int textPosition, bool isInside, bool isTrailing) {`
- `public CharacterHit CharacterHit { get; }`
- `public bool IsInside { get; }`
- `public int TextPosition { get; }`
- `public bool IsTrailing { get; }`

### `src/Avalonia.Base/Media/TextLeadingPrefixTrimming.cs`
- `public sealed class TextLeadingPrefixTrimming : TextTrimming`
- `public TextLeadingPrefixTrimming(string ellipsis, int prefixLength) {`
- `public override TextCollapsingProperties CreateCollapsingProperties(TextCollapsingCreateInfo createInfo) {`

### `src/Avalonia.Base/Media/TextPathSegmentEllipsis.cs`
- `public sealed class TextPathSegmentEllipsis : TextCollapsingProperties`
- `public TextPathSegmentEllipsis(string ellipsis, double width, TextRunProperties textRunProperties, FlowDirection flowDirection) {`
- `public override TextRun Symbol { get; }`
- `public override TextRun[]? Collapse(TextLine textLine) {`

### `src/Avalonia.Base/Media/TextPathSegmentTrimming.cs`
- `public sealed class TextPathSegmentTrimming : TextTrimming`
- `public TextPathSegmentTrimming(string ellipsis) {`
- `public override TextCollapsingProperties CreateCollapsingProperties(TextCollapsingCreateInfo createInfo) {`

### `src/Avalonia.Base/Media/TextRenderingMode.cs`
- `public enum TextRenderingMode : byte`

### `src/Avalonia.Base/Media/TextTrailingTrimming.cs`
- `public sealed class TextTrailingTrimming : TextTrimming`
- `public TextTrailingTrimming(string ellipsis, bool isWordBased) {`
- `public override TextCollapsingProperties CreateCollapsingProperties(TextCollapsingCreateInfo createInfo) {`

### `src/Avalonia.Base/Media/TextTrimming.cs`
- `public static TextTrimming WordEllipsis { get; } = new TextTrailingTrimming(DefaultEllipsisChar, true);`
- `public static TextTrimming PrefixCharacterEllipsis { get; } = new TextLeadingPrefixTrimming(DefaultEllipsisChar, 8);`
- `public static TextTrimming LeadingCharacterEllipsis { get; } = new TextLeadingPrefixTrimming(DefaultEllipsisChar, 0);`
- `public static TextTrimming PathSegmentEllipsis { get; } = new TextPathSegmentTrimming(DefaultEllipsisChar);`
- `public abstract TextCollapsingProperties CreateCollapsingProperties(TextCollapsingCreateInfo createInfo);`

### `src/Avalonia.Base/Media/TileBrush.cs`
- `public enum TileMode`
- `public abstract class TileBrush : Brush, ITileBrush`
- `public static readonly StyledProperty<AlignmentX> AlignmentXProperty = AvaloniaProperty.Register<TileBrush, AlignmentX>(nameof(AlignmentX), AlignmentX.Center);`
- `public static readonly StyledProperty<AlignmentY> AlignmentYProperty = AvaloniaProperty.Register<TileBrush, AlignmentY>(nameof(AlignmentY), AlignmentY.Center);`
- `public static readonly StyledProperty<RelativeRect> DestinationRectProperty = AvaloniaProperty.Register<TileBrush, RelativeRect>(nameof(DestinationRect), RelativeRect.Fill);`
- `public static readonly StyledProperty<RelativeRect> SourceRectProperty = AvaloniaProperty.Register<TileBrush, RelativeRect>(nameof(SourceRect), RelativeRect.Fill);`
- `public static readonly StyledProperty<TileMode> TileModeProperty = AvaloniaProperty.Register<TileBrush, TileMode>(nameof(TileMode));`
- `public AlignmentX AlignmentX {`
- `public AlignmentY AlignmentY {`
- `public RelativeRect DestinationRect {`
- `public RelativeRect SourceRect {`
- `public TileMode TileMode {`

### `src/Avalonia.Base/Media/Transform.cs`
- `public event EventHandler? Changed;`

### `src/Avalonia.Base/Media/TransformConverter.cs`
- `public class TransformConverter : TypeConverter`

### `src/Avalonia.Base/Media/TransformExtensions.cs`
- `public static class TransformExtensions`

### `src/Avalonia.Base/Media/TransformGroup.cs`
- `public sealed class TransformGroup : Transform`
- `public static readonly StyledProperty<Transforms> ChildrenProperty = AvaloniaProperty.Register<TransformGroup, Transforms>(nameof(Children));`
- `public TransformGroup() {`

### `src/Avalonia.Base/Media/Transformation/TransformOperation.cs`
- `public record struct TransformOperation`
- `public Matrix Matrix;`
- `public enum OperationType`
- `public bool IsIdentity => Matrix.IsIdentity;`
- `public void Bake() {`
- `public static bool TryInterpolate(TransformOperation? from, TransformOperation? to, double progress, ref TransformOperation result) {`
- `public record struct DataLayout`
- `public record struct SkewLayout`
- `public double X;`
- `public double Y;`
- `public record struct ScaleLayout`
- `public record struct TranslateLayout`
- `public record struct RotateLayout`
- `public double Angle;`

### `src/Avalonia.Base/Media/Transformation/TransformOperations.cs`
- `public bool IsIdentity { get; }`
- `public static Builder CreateBuilder(int capacity) {`
- `public static TransformOperations Interpolate(TransformOperations from, TransformOperations to, double progress) {`
- `public readonly record struct Builder`
- `public Builder(int capacity) {`
- `public void AppendTranslate(double x, double y) {`
- `public void AppendRotate(double angle) {`
- `public void AppendScale(double x, double y) {`
- `public void AppendSkew(double x, double y) {`
- `public void AppendMatrix(Matrix matrix) {`
- `public void AppendIdentity() {`
- `public void Append(TransformOperation toAdd) {`

### `src/Avalonia.Base/Media/TranslateTransform.cs`
- `public sealed class TranslateTransform : Transform`
- `public static readonly StyledProperty<double> XProperty = AvaloniaProperty.Register<TranslateTransform, double>(nameof(X));`
- `public static readonly StyledProperty<double> YProperty = AvaloniaProperty.Register<TranslateTransform, double>(nameof(Y));`
- `public TranslateTransform() {`
- `public TranslateTransform(double x, double y) : this() {`
- `public double X {`
- `public double Y {`

### `src/Avalonia.Base/Media/Typeface.cs`
- `public FontWeight Weight { get; }`
- `public IGlyphTypeface GlyphTypeface {`

### `src/Avalonia.Base/Media/UnicodeRange.cs`
- `public readonly record struct UnicodeRange`
- `public UnicodeRange(int start, int end) {`
- `public UnicodeRange(UnicodeRangeSegment single) {`
- `public UnicodeRange(IReadOnlyList<UnicodeRangeSegment> segments) {`
- `public bool IsInRange(int value) {`
- `public readonly record struct UnicodeRangeSegment`
- `public UnicodeRangeSegment(int start, int end) {`

### `src/Avalonia.Base/Media/VisualBrush.cs`
- `public sealed class VisualBrush : TileBrush, ISceneBrush`
- `public static readonly StyledProperty<Visual?> VisualProperty = AvaloniaProperty.Register<VisualBrush, Visual?>(nameof(Visual));`
- `public VisualBrush() {`
- `public VisualBrush(Visual visual) {`

### `src/Avalonia.Base/Metadata/AmbientAttribute.cs`
- `public sealed class AmbientAttribute : Attribute`

### `src/Avalonia.Base/Metadata/AvaloniaListAttribute.cs`
- `public sealed class AvaloniaListAttribute : Attribute`
- `public string[]? Separators { get; init; }`
- `public StringSplitOptions SplitOptions { get; init; } = StringSplitOptions.RemoveEmptyEntries | (StringSplitOptions)2;`

### `src/Avalonia.Base/Metadata/ContentAttribute.cs`
- `public sealed class ContentAttribute : Attribute`

### `src/Avalonia.Base/Metadata/ControlTemplateScopeAttribute.cs`
- `public sealed class ControlTemplateScopeAttribute : Attribute;`

### `src/Avalonia.Base/Metadata/DataTypeAttribute.cs`
- `public sealed class DataTypeAttribute : Attribute`

### `src/Avalonia.Base/Metadata/DependsOnAttribute.cs`
- `public sealed class DependsOnAttribute : Attribute`
- `public DependsOnAttribute(string propertyName) {`

### `src/Avalonia.Base/Metadata/InheritDataTypeFromAttribute.cs`
- `public enum InheritDataTypeFromScopeKind`
- `public sealed class InheritDataTypeFromAttribute : Attribute`
- `public InheritDataTypeFromAttribute(InheritDataTypeFromScopeKind scopeKind) {`
- `public InheritDataTypeFromScopeKind ScopeKind { get; }`

### `src/Avalonia.Base/Metadata/InheritDataTypeFromItemsAttribute.cs`
- `public sealed class InheritDataTypeFromItemsAttribute : Attribute`
- `public InheritDataTypeFromItemsAttribute(string ancestorItemsProperty) {`
- `public string AncestorItemsProperty { get; }`

### `src/Avalonia.Base/Metadata/MarkupExtensionOption.cs`
- `public sealed class MarkupExtensionOptionAttribute : Attribute`
- `public MarkupExtensionOptionAttribute(object value) {`
- `public sealed class MarkupExtensionDefaultOptionAttribute : Attribute`

### `src/Avalonia.Base/Metadata/NotClientImplementableAttribute.cs`
- `public sealed class NotClientImplementableAttribute : Attribute`

### `src/Avalonia.Base/Metadata/PrivateApiAttribute.cs`
- `public sealed class PrivateApiAttribute : Attribute`

### `src/Avalonia.Base/Metadata/TemplateContent.cs`
- `public sealed class TemplateContentAttribute : Attribute`
- `public Type? TemplateResultType { get; set; }`

### `src/Avalonia.Base/Metadata/TrimSurroundingWhitespaceAttribute.cs`
- `public sealed class TrimSurroundingWhitespaceAttribute : Attribute`

### `src/Avalonia.Base/Metadata/UnstableAttribute.cs`
- `public sealed class UnstableAttribute : Attribute`
- `public UnstableAttribute() {`
- `public UnstableAttribute(string? message) {`

### `src/Avalonia.Base/Metadata/UsableDuringInitializationAttribute.cs`
- `public sealed class UsableDuringInitializationAttribute : Attribute`

### `src/Avalonia.Base/Metadata/WhitespaceSignificantCollectionAttribute.cs`
- `public sealed class WhitespaceSignificantCollectionAttribute : Attribute`

### `src/Avalonia.Base/Metadata/XmlnsDefinitionAttribute.cs`
- `public string XmlNamespace { get; }`
- `public string ClrNamespace { get; }`

### `src/Avalonia.Base/Metadata/XmlnsPrefixAttribute.cs`
- `public string XmlNamespace { get; }`
- `public string Prefix { get; }`

### `src/Avalonia.Base/PixelPoint.cs`
- `public readonly struct PixelPoint : IEquatable<PixelPoint>`
- `public static readonly PixelPoint Origin = new PixelPoint(0, 0);`
- `public PixelPoint(int x, int y) {`
- `public int X { get; }`
- `public int Y { get; }`
- `public static implicit operator PixelVector(PixelPoint p) {`
- `public static PixelPoint operator +(PixelPoint a, PixelPoint b) {`
- `public static PixelPoint operator +(PixelPoint a, PixelVector b) {`
- `public static PixelPoint operator -(PixelPoint a, PixelPoint b) {`
- `public static PixelPoint operator -(PixelPoint a, PixelVector b) {`
- `public PixelPoint WithX(int x) => new PixelPoint(x, Y);`
- `public PixelPoint WithY(int y) => new PixelPoint(X, y);`
- `public Point ToPoint(double scale) => new Point(X / scale, Y / scale);`
- `public Point ToPoint(Vector scale) => new Point(X / scale.X, Y / scale.Y);`
- `public Point ToPointWithDpi(double dpi) => ToPoint(dpi / 96);`
- `public Point ToPointWithDpi(Vector dpi) => ToPoint(new Vector(dpi.X / 96, dpi.Y / 96));`
- `public static PixelPoint FromPoint(Point point, double scale) => new PixelPoint(`
- `public static PixelPoint FromPoint(Point point, Vector scale) => new PixelPoint(`
- `public static PixelPoint FromPointWithDpi(Point point, double dpi) => FromPoint(point, dpi / 96);`
- `public static PixelPoint FromPointWithDpi(Point point, Vector dpi) => FromPoint(point, new Vector(dpi.X / 96, dpi.Y / 96));`

### `src/Avalonia.Base/PixelRect.cs`
- `public int X { get; }`
- `public int Y { get; }`
- `public PixelPoint Center => new PixelPoint(X + (Width / 2), Y + (Height / 2));`
- `public bool ContainsExclusive(PixelPoint p) {`
- `public PixelRect CenterRect(PixelRect rect) {`
- `public PixelRect Intersect(PixelRect rect) {`
- `public bool Intersects(PixelRect rect) {`
- `public PixelRect Translate(PixelVector offset) {`
- `public PixelRect Union(PixelRect rect) {`
- `public PixelRect WithX(int x) {`
- `public PixelRect WithY(int y) {`
- `public PixelRect WithWidth(int width) {`
- `public PixelRect WithHeight(int height) {`
- `public Rect ToRect(double scale) => new Rect(Position.ToPoint(scale), Size.ToSize(scale));`
- `public Rect ToRect(Vector scale) => new Rect(Position.ToPoint(scale), Size.ToSize(scale));`
- `public Rect ToRectWithDpi(double dpi) => new Rect(Position.ToPointWithDpi(dpi), Size.ToSizeWithDpi(dpi));`
- `public Rect ToRectWithDpi(Vector dpi) => new Rect(Position.ToPointWithDpi(dpi), Size.ToSizeWithDpi(dpi));`
- `public static PixelRect FromRect(Rect rect, double scale) => new PixelRect(`
- `public static PixelRect FromRect(Rect rect, Vector scale) => new PixelRect(`
- `public static PixelRect FromRectWithDpi(Rect rect, double dpi) => new PixelRect(`
- `public static PixelRect FromRectWithDpi(Rect rect, Vector dpi) => new PixelRect(`

### `src/Avalonia.Base/PixelSize.cs`
- `public readonly struct PixelSize : IEquatable<PixelSize>`
- `public PixelSize(int width, int height) {`
- `public static bool TryParse([NotNullWhen(true)] string? source, out PixelSize result) {`
- `public PixelSize WithWidth(int width) => new PixelSize(width, Height);`
- `public PixelSize WithHeight(int height) => new PixelSize(Width, height);`
- `public Size ToSize(double scale) => new Size(Width / scale, Height / scale);`
- `public Size ToSize(Vector scale) => new Size(Width / scale.X, Height / scale.Y);`
- `public Size ToSizeWithDpi(double dpi) => ToSize(dpi / 96);`
- `public Size ToSizeWithDpi(Vector dpi) => ToSize(new Vector(dpi.X / 96, dpi.Y / 96));`
- `public static PixelSize FromSize(Size size, double scale) => new PixelSize(`
- `public static PixelSize FromSize(Size size, Vector scale) => new PixelSize(`
- `public static PixelSize FromSizeWithDpi(Size size, double dpi) => FromSize(size, dpi / 96);`
- `public static PixelSize FromSizeWithDpi(Size size, Vector dpi) => FromSize(size, new Vector(dpi.X / 96, dpi.Y / 96));`

### `src/Avalonia.Base/PixelVector.cs`
- `public readonly struct PixelVector`
- `public PixelVector(int x, int y) {`
- `public int X => _x;`
- `public int Y => _y;`
- `public static explicit operator PixelPoint(PixelVector a) {`
- `public static int operator *(PixelVector a, PixelVector b) {`
- `public static PixelVector operator *(PixelVector vector, int scale) {`
- `public static PixelVector operator /(PixelVector vector, int scale) {`
- `public double Length => Math.Sqrt(X * X + Y * Y);`
- `public static PixelVector operator -(PixelVector a) {`
- `public static PixelVector operator +(PixelVector a, PixelVector b) {`
- `public static PixelVector operator -(PixelVector a, PixelVector b) {`
- `public bool NearlyEquals(PixelVector other) {`
- `public PixelVector WithX(int x) {`
- `public PixelVector WithY(int y) {`

### `src/Avalonia.Base/Platform/AlphaFormat.cs`
- `public enum AlphaFormat`

### `src/Avalonia.Base/Platform/AssetLoader.cs`
- `public static void SetDefaultAssembly(Assembly assembly) => GetAssetLoader().SetDefaultAssembly(assembly);`
- `public static Assembly? GetAssembly(Uri uri, Uri? baseUri = null) => GetAssetLoader().GetAssembly(uri, baseUri);`
- `public static void InvalidateAssemblyCache(string name) => GetAssetLoader().InvalidateAssemblyCache(name);`
- `public static void InvalidateAssemblyCache() => GetAssetLoader().InvalidateAssemblyCache();`

### `src/Avalonia.Base/Platform/DefaultPlatformSettings.cs`
- `public class DefaultPlatformSettings : IPlatformSettings`
- `public virtual Size GetTapSize(PointerType type) {`
- `public virtual Size GetDoubleTapSize(PointerType type) {`
- `public virtual TimeSpan GetDoubleTapTime(PointerType type) => TimeSpan.FromMilliseconds(500);`
- `public virtual TimeSpan HoldWaitDuration => TimeSpan.FromMilliseconds(300);`

### `src/Avalonia.Base/Platform/IBitmapImpl.cs`
- `public interface IBitmapImpl : IDisposable`

### `src/Avalonia.Base/Platform/ICursorFactory.cs`
- `public interface ICursorFactory`

### `src/Avalonia.Base/Platform/ICursorImpl.cs`
- `public interface ICursorImpl : IDisposable`

### `src/Avalonia.Base/Platform/IDrawingContextImpl.cs`
- `public interface IDrawingContextImpl : IDisposable`
- `public interface IDrawingContextImplWithEffects : IDrawingContextImpl`
- `public static class DrawingContextImplExtensions`
- `public static T? GetFeature<T>(this IDrawingContextImpl context) where T : class =>`
- `public interface IDrawingContextLayerImpl : IRenderTargetBitmapImpl`
- `public interface IDrawingContextLayerWithRenderContextAffinityImpl : IDrawingContextLayerImpl`

### `src/Avalonia.Base/Platform/IDrawingContextWithAcrylicLikeSupport.cs`
- `public interface IDrawingContextWithAcrylicLikeSupport`

### `src/Avalonia.Base/Platform/IExternalObjectsRenderInterfaceContextFeature.cs`
- `public interface IExternalObjectsRenderInterfaceContextFeature`
- `public byte[]? DeviceUuid { get; }`
- `public byte[]? DeviceLuid { get; }`
- `public interface IExternalObjectsHandleWrapRenderInterfaceContextFeature`
- `public interface IExternalObjectsWrappedGpuHandle : IPlatformHandle, IDisposable`
- `public interface IPlatformRenderInterfaceImportedObject : IDisposable`
- `public interface IPlatformRenderInterfaceImportedImage : IPlatformRenderInterfaceImportedObject`
- `public interface IPlatformRenderInterfaceImportedSemaphore : IPlatformRenderInterfaceImportedObject`

### `src/Avalonia.Base/Platform/IFontManagerImpl.cs`
- `public interface IFontManagerImpl`

### `src/Avalonia.Base/Platform/IGeometryContext.cs`
- `public interface IGeometryContext : IDisposable`

### `src/Avalonia.Base/Platform/IGeometryContext2.cs`
- `public interface IGeometryContext2 : IGeometryContext`

### `src/Avalonia.Base/Platform/IGeometryImpl.cs`
- `public interface IGeometryImpl`

### `src/Avalonia.Base/Platform/IGlyphRunImpl.cs`
- `public interface IGlyphRunImpl : IDisposable`

### `src/Avalonia.Base/Platform/ILockedFramebuffer.cs`
- `public interface ILockedFramebuffer : IDisposable`

### `src/Avalonia.Base/Platform/IMacOSTopLevelPlatformHandle.cs`
- `public interface IMacOSTopLevelPlatformHandle`

### `src/Avalonia.Base/Platform/IOptionalFeatureProvider.cs`
- `public static class OptionalFeatureProviderExtensions`

### `src/Avalonia.Base/Platform/IPlatformBehaviorInhibition.cs`
- `public interface IPlatformBehaviorInhibition`

### `src/Avalonia.Base/Platform/IPlatformGpu.cs`
- `public class PlatformGraphicsContextLostException : Exception`

### `src/Avalonia.Base/Platform/IPlatformRenderInterface.cs`
- `public interface IPlatformRenderInterface`
- `public AlphaFormat DefaultAlphaFormat { get; }`
- `public PixelFormat DefaultPixelFormat { get; }`
- `public interface IPlatformRenderInterfaceContext : IOptionalFeatureProvider, IDisposable`

### `src/Avalonia.Base/Platform/IPlatformRenderInterfaceRegion.cs`
- `public interface IPlatformRenderInterfaceRegion : IDisposable`

### `src/Avalonia.Base/Platform/IPlatformThreadingInterface.cs`
- `public interface IPlatformThreadingInterface`

### `src/Avalonia.Base/Platform/IReadableBitmapImpl.cs`
- `public interface IReadableBitmapImpl`
- `public interface IReadableBitmapWithAlphaImpl : IReadableBitmapImpl`

### `src/Avalonia.Base/Platform/IRenderTarget.cs`
- `public interface IRenderTarget : IDisposable`
- `public bool IsCorrupted { get; }`
- `public interface IRenderTargetWithProperties : IRenderTarget`
- `public interface IRenderTarget2 : IRenderTarget`

### `src/Avalonia.Base/Platform/IRenderTargetBitmapImpl.cs`
- `public interface IRenderTargetBitmapImpl : IBitmapImpl, IRenderTarget`

### `src/Avalonia.Base/Platform/IRuntimePlatform.cs`
- `public interface IRuntimePlatform`
- `public record struct RuntimePlatformInfo`
- `public FormFactorType FormFactor => IsDesktop ? FormFactorType.Desktop :`
- `public bool IsDesktop { get; set; }`
- `public bool IsMobile { get; set; }`
- `public bool IsTV { get; set; }`

### `src/Avalonia.Base/Platform/IScopedResource.cs`
- `public interface IScopedResource<T> : IDisposable`
- `public class ScopedResource<T> : IScopedResource<T>`

### `src/Avalonia.Base/Platform/IStreamGeometryContextImpl.cs`
- `public interface IStreamGeometryContextImpl : IGeometryContext`

### `src/Avalonia.Base/Platform/IStreamGeometryImpl.cs`
- `public interface IStreamGeometryImpl : IGeometryImpl`

### `src/Avalonia.Base/Platform/ITextShaperImpl.cs`
- `public interface ITextShaperImpl`

### `src/Avalonia.Base/Platform/ITransformedGeometryImpl.cs`
- `public interface ITransformedGeometryImpl : IGeometryImpl`

### `src/Avalonia.Base/Platform/IWriteableBitmapImpl.cs`
- `public interface IWriteableBitmapImpl : IBitmapImpl, IReadableBitmapWithAlphaImpl`

### `src/Avalonia.Base/Platform/LockedFramebuffer.cs`
- `public class LockedFramebuffer : ILockedFramebuffer`
- `public LockedFramebuffer(IntPtr address, PixelSize size, int rowBytes, Vector dpi, PixelFormat format, Action? onDispose) {`
- `public IntPtr Address { get; }`
- `public int RowBytes { get; }`
- `public Vector Dpi { get; }`
- `public PixelFormat Format { get; }`

### `src/Avalonia.Base/Platform/LtrbRect.cs`
- `public struct LtrbRect`
- `public struct LtrbPixelRect`

### `src/Avalonia.Base/Platform/PathGeometryContext.cs`
- `public class PathGeometryContext : IGeometryContext`
- `public PathGeometryContext(PathGeometry pathGeometry) {`
- `public void ArcTo(Point point, Size size, double rotationAngle, bool isLargeArc, SweepDirection sweepDirection) {`
- `public void BeginFigure(Point startPoint, bool isFilled) {`
- `public void CubicBezierTo(Point controlPoint1, Point controlPoint2, Point endPoint) {`
- `public void QuadraticBezierTo(Point controlPoint , Point endPoint) {`
- `public void LineTo(Point endPoint) {`
- `public void EndFigure(bool isClosed) {`
- `public void SetFillRule(FillRule fillRule) {`

### `src/Avalonia.Base/Platform/PixelFormat.cs`
- `public record struct PixelFormat`
- `public int BitsPerPixel {`
- `public static PixelFormat Rgb565 => PixelFormats.Rgb565;`
- `public static PixelFormat Rgba8888 => PixelFormats.Rgba8888;`
- `public static PixelFormat Rgb32 => PixelFormats.Rgb32;`
- `public static PixelFormat Bgra8888 => PixelFormats.Bgra8888;`
- `public static class PixelFormats`
- `public static PixelFormat Rgb565 { get; } = new PixelFormat(PixelFormatEnum.Rgb565);`
- `public static PixelFormat Rgba8888 { get; } = new PixelFormat(PixelFormatEnum.Rgba8888);`
- `public static PixelFormat Rgba64 { get; } = new PixelFormat(PixelFormatEnum.Rgba64);`
- `public static PixelFormat Bgra8888 { get; } = new PixelFormat(PixelFormatEnum.Bgra8888);`
- `public static PixelFormat BlackWhite { get; } = new PixelFormat(PixelFormatEnum.BlackWhite);`
- `public static PixelFormat Gray2 { get; } = new PixelFormat(PixelFormatEnum.Gray2);`
- `public static PixelFormat Gray4 { get; } = new PixelFormat(PixelFormatEnum.Gray4);`
- `public static PixelFormat Gray8 { get; } = new PixelFormat(PixelFormatEnum.Gray8);`
- `public static PixelFormat Gray16 { get; } = new PixelFormat(PixelFormatEnum.Gray16);`
- `public static PixelFormat Gray32Float { get; } = new PixelFormat(PixelFormatEnum.Gray32Float);`
- `public static PixelFormat Rgb24 { get; } = new PixelFormat(PixelFormatEnum.Rgb24);`
- `public static PixelFormat Rgb32 { get; } = new PixelFormat(PixelFormatEnum.Rgb32);`
- `public static PixelFormat Bgr24 { get; } = new PixelFormat(PixelFormatEnum.Bgr24);`
- `public static PixelFormat Bgr32 { get; } = new PixelFormat(PixelFormatEnum.Bgr32);`
- `public static PixelFormat Bgr555 { get; } = new PixelFormat(PixelFormatEnum.Bgr555);`
- `public static PixelFormat Bgr565 { get; } = new PixelFormat(PixelFormatEnum.Bgr565);`

### `src/Avalonia.Base/Platform/PlatformColorValues.cs`
- `public Color AccentColor1 { get; init; }`
- `public Color AccentColor2 {`
- `public Color AccentColor3 {`
- `public PlatformColorValues() {`

### `src/Avalonia.Base/Platform/PlatformGraphicsDeviceAdapterDescription.cs`
- `public class PlatformGraphicsDeviceAdapterDescription`
- `public byte[]? DeviceLuid { get; set; }`
- `public byte[]? DeviceUuid { get; set; }`

### `src/Avalonia.Base/Platform/PlatformGraphicsExternalMemory.cs`
- `public record struct PlatformGraphicsExternalImageProperties`
- `public PlatformGraphicsExternalImageFormat Format { get; set; }`
- `public ulong MemorySize { get; set; }`
- `public ulong MemoryOffset { get; set; }`
- `public bool TopLeftOrigin { get; set; }`
- `public enum PlatformGraphicsExternalImageFormat`
- `public static class KnownPlatformGraphicsExternalImageHandleTypes`
- `public const string D3D11TextureGlobalSharedHandle = nameof(D3D11TextureGlobalSharedHandle);`
- `public const string D3D11TextureNtHandle = nameof(D3D11TextureNtHandle);`
- `public const string VulkanOpaquePosixFileDescriptor = nameof(VulkanOpaquePosixFileDescriptor);`
- `public const string VulkanOpaqueNtHandle = nameof(VulkanOpaqueNtHandle);`
- `public const string VulkanOpaqueKmtHandle = nameof(VulkanOpaqueKmtHandle);`
- `public const string IOSurfaceRef = nameof(IOSurfaceRef);`
- `public static class KnownPlatformGraphicsExternalSemaphoreHandleTypes`
- `public const string Direct3D12FenceNtHandle = nameof(Direct3D12FenceNtHandle);`
- `public const string MetalSharedEvent = nameof(MetalSharedEvent);`

### `src/Avalonia.Base/Platform/PlatformHandle.cs`
- `public class PlatformHandle : IPlatformHandle, IEquatable<PlatformHandle>`
- `public PlatformHandle(IntPtr handle, string? descriptor) {`
- `public IntPtr Handle { get; }`
- `public string? HandleDescriptor { get; }`

### `src/Avalonia.Base/Platform/RenderTargetProperties.cs`
- `public struct RenderTargetProperties`
- `public bool RetainsPreviousFrameContents { get; init; }`
- `public bool IsSuitableForDirectRendering { get; init; }`
- `public struct RenderTargetDrawingContextProperties`
- `public bool PreviousFrameIsRetained { get; init; }`

### `src/Avalonia.Base/Platform/StandardAssetLoader.cs`
- `public class StandardAssetLoader : IAssetLoader`
- `public StandardAssetLoader(Assembly? assembly = null) : this(new AssemblyDescriptorResolver(), assembly) {`
- `public void SetDefaultAssembly(Assembly assembly) {`
- `public (Stream stream, Assembly assembly) OpenAndGetAssembly(Uri uri, Uri? baseUri = null) {`
- `public Assembly? GetAssembly(Uri uri, Uri? baseUri) {`
- `public void InvalidateAssemblyCache(string name) {`
- `public void InvalidateAssemblyCache() {`
- `public static void RegisterResUriParsers() => AssetLoader.RegisterResUriParsers();`

### `src/Avalonia.Base/Platform/StandardRuntimePlatform.cs`
- `public class StandardRuntimePlatform : IRuntimePlatform`
- `public virtual RuntimePlatformInfo GetRuntimeInfo() => new()`

### `src/Avalonia.Base/Platform/Storage/FilePickerFileType.cs`
- `public IReadOnlyList<string>? AppleUniformTypeIdentifiers { get; set; }`

### `src/Avalonia.Base/Platform/Storage/FilePickerFileTypes.cs`
- `public static class FilePickerFileTypes`

### `src/Avalonia.Base/Platform/Storage/IStorageBookmarkItem.cs`
- `public interface IStorageBookmarkItem : IStorageItem`
- `public interface IStorageBookmarkFile : IStorageFile, IStorageBookmarkItem`
- `public interface IStorageBookmarkFolder : IStorageFolder, IStorageBookmarkItem`

### `src/Avalonia.Base/Platform/Storage/PickerOptions.cs`
- `public class PickerOptions`

### `src/Avalonia.Base/Platform/Storage/SaveFilePickerResult.cs`
- `public readonly struct SaveFilePickerResult`
- `public IStorageFile? File { get; init; }`
- `public FilePickerFileType? SelectedFileType { get; init; }`

### `src/Avalonia.Base/Platform/Storage/StorageItemProperties.cs`
- `public class StorageItemProperties`
- `public StorageItemProperties( ulong? size = null, DateTimeOffset? dateCreated = null, DateTimeOffset? dateModified = null) {`
- `public DateTimeOffset? DateCreated { get; }`
- `public DateTimeOffset? DateModified { get; }`

### `src/Avalonia.Base/Platform/SystemNavigationManagerImpl.cs`
- `public interface ISystemNavigationManagerImpl`

### `src/Avalonia.Base/Points.cs`
- `public Points() {`
- `public Points(IEnumerable<Point> points) : base(points) {`

### `src/Avalonia.Base/Reactive/AnonymousObserver.cs`
- `public class AnonymousObserver<T> : IObserver<T>`
- `public AnonymousObserver(TaskCompletionSource<T> tcs) {`
- `public AnonymousObserver(Action<T> onNext, Action<Exception> onError, Action onCompleted) {`
- `public AnonymousObserver(Action<T> onNext) : this(onNext, ThrowsOnError, NoOpCompleted) {`
- `public AnonymousObserver(Action<T> onNext, Action<Exception> onError) : this(onNext, onError, NoOpCompleted) {`
- `public AnonymousObserver(Action<T> onNext, Action onCompleted) : this(onNext, ThrowsOnError, onCompleted) {`
- `public void OnError(Exception error) {`
- `public void OnNext(T value) {`

### `src/Avalonia.Base/Rect.cs`
- `public double X => _x;`
- `public double Y => _y;`
- `public double Top => _y;`
- `public Point Center => new Point(_x + (_width / 2), _y + (_height / 2));`
- `public static Rect operator *(Rect rect, Vector scale) {`
- `public static Rect operator *(Rect rect, double scale) {`
- `public static Rect operator /(Rect rect, Vector scale) {`
- `public bool ContainsExclusive(Point p) {`
- `public Rect CenterRect(Rect rect) {`
- `public Rect Inflate(double thickness) {`
- `public Rect Inflate(Thickness thickness) {`
- `public Rect Deflate(double thickness) {`
- `public Rect Deflate(Thickness thickness) {`
- `public Rect Intersect(Rect rect) {`
- `public bool Intersects(Rect rect) {`
- `public Rect TransformToAABB(Matrix matrix) {`
- `public Rect Translate(Vector offset) {`
- `public Rect Normalize() {`
- `public Rect Union(Rect rect) {`
- `public Rect WithX(double x) {`
- `public Rect WithY(double y) {`
- `public Rect WithWidth(double width) {`
- `public Rect WithHeight(double height) {`

### `src/Avalonia.Base/RelativeRect.cs`
- `public readonly struct RelativeRect : IEquatable<RelativeRect>`
- `public RelativeRect(double x, double y, double width, double height, RelativeUnit unit) {`
- `public RelativeRect(Rect rect, RelativeUnit unit) {`
- `public RelativeRect(Size size, RelativeUnit unit) {`
- `public RelativeRect(Point position, Size size, RelativeUnit unit) {`
- `public RelativeRect(Point topLeft, Point bottomRight, RelativeUnit unit) {`
- `public RelativeUnit Unit { get; }`
- `public Rect Rect { get; }`
- `public Rect ToPixels(Size size) {`
- `public Rect ToPixels(Rect boundingBox) {`

### `src/Avalonia.Base/RelativeScalar.cs`
- `public struct RelativeScalar : IEquatable<RelativeScalar>`
- `public RelativeScalar(double scalar, RelativeUnit unit) {`
- `public double Scalar => _scalar;`
- `public RelativeUnit Unit => _unit;`
- `public static RelativeScalar Beginning { get; } = new RelativeScalar(0, RelativeUnit.Relative);`
- `public static RelativeScalar Middle { get; } = new RelativeScalar(0.5, RelativeUnit.Relative);`
- `public double ToValue(double size) {`

### `src/Avalonia.Base/RenderTargetCorruptedException.cs`
- `public class RenderTargetCorruptedException : Exception`
- `public RenderTargetCorruptedException() {`
- `public RenderTargetCorruptedException(string message) : base(message) {`
- `public RenderTargetCorruptedException(Exception innerException) : base(null, innerException) {`
- `public RenderTargetCorruptedException(string message, Exception innerException) : base(message, innerException) {`

### `src/Avalonia.Base/RenderTargetNotReadyException.cs`
- `public class RenderTargetNotReadyException : Exception`
- `public RenderTargetNotReadyException() {`
- `public RenderTargetNotReadyException(string message) : base(message) {`
- `public RenderTargetNotReadyException(Exception innerException) : base(null, innerException) {`
- `public RenderTargetNotReadyException(string message, Exception innerException) : base(message, innerException) {`

### `src/Avalonia.Base/Rendering/Composition/Animations/CompositionAnimation.cs`
- `public void ClearAllParameters() => _propertySet.ClearAll();`
- `public void ClearParameter(string key) => _propertySet.Clear(key);`
- `public void SetColorParameter(string key, Media.Color value) => SetVariant(key, value);`
- `public void SetMatrix3x2Parameter(string key, Matrix3x2 value) => SetVariant(key, value);`
- `public void SetMatrix4x4Parameter(string key, Matrix4x4 value) => SetVariant(key, value);`
- `public void SetQuaternionParameter(string key, Quaternion value) => SetVariant(key, value);`
- `public void SetVector2Parameter(string key, Vector2 value) => SetVariant(key, value);`
- `public void SetVector4Parameter(string key, Vector4 value) => SetVariant(key, value);`

### `src/Avalonia.Base/Rendering/Composition/Animations/ICompositionAnimationBase.cs`
- `public interface ICompositionAnimationBase`

### `src/Avalonia.Base/Rendering/Composition/Animations/ImplicitAnimationCollection.cs`
- `public IReadOnlyDictionary<string, ICompositionAnimationBase> GetView() =>`
- `public bool HasKey(string key) => ContainsKey(key);`
- `public ICompositionAnimationBase? Lookup(string key) {`

### `src/Avalonia.Base/Rendering/Composition/Animations/KeyFrameAnimation.cs`
- `public abstract class KeyFrameAnimation : CompositionAnimation`
- `public AnimationDelayBehavior DelayBehavior { get; set; }`
- `public System.TimeSpan DelayTime { get; set; }`
- `public AnimationStopBehavior StopBehavior { get; set; }`
- `public enum AnimationDelayBehavior`
- `public enum AnimationStopBehavior`

### `src/Avalonia.Base/Rendering/Composition/CompositionCustomVisual.cs`
- `public void SendHandlerMessage(object message) {`

### `src/Avalonia.Base/Rendering/Composition/CompositionDrawingSurface.cs`
- `public sealed class CompositionDrawingSurface : CompositionSurface, IDisposable`
- `public Task UpdateWithKeyedMutexAsync(ICompositionImportedGpuImage image, uint acquireIndex, uint releaseIndex) {`
- `public Task UpdateWithSemaphoresAsync(ICompositionImportedGpuImage image, ICompositionImportedGpuSemaphore waitForSemaphore, ICompositionImportedGpuSemaphore signalSemaphore) {`
- `public Task UpdateWithTimelineSemaphoresAsync(ICompositionImportedGpuImage image, ICompositionImportedGpuSemaphore waitForSemaphore, ulong waitForValue, ICompositionImportedGpuSemaphore signalSemaphore, ulong signalValue) {`
- `public Task UpdateAsync(ICompositionImportedGpuImage image) {`

### `src/Avalonia.Base/Rendering/Composition/CompositionExternalMemory.cs`
- `public interface ICompositionGpuInterop`
- `public byte[]? DeviceLuid { get; set; }`
- `public byte[]? DeviceUuid { get; set; }`
- `public enum CompositionGpuImportedImageSynchronizationCapabilities`
- `public interface ICompositionGpuImportedObject : IAsyncDisposable`
- `public interface ICompositionImportedGpuImage : ICompositionGpuImportedObject`
- `public interface ICompositionImportedGpuSemaphore : ICompositionGpuImportedObject`
- `public interface ICompositionImportableSharedGpuContextObject : IDisposable`
- `public interface ICompositionImportableSharedGpuContextImage : IDisposable`
- `public interface ICompositionImportableSharedGpuContextSemaphore : IDisposable`

### `src/Avalonia.Base/Rendering/Composition/CompositionObject.cs`
- `public void StopAnimationGroup(ICompositionAnimationBase grp) {`

### `src/Avalonia.Base/Rendering/Composition/CompositionOptions.cs`
- `public class CompositionOptions`
- `public bool? UseRegionDirtyRectClipping { get; set; }`
- `public bool? UseSaveLayerRootClip { get; set; }`

### `src/Avalonia.Base/Rendering/Composition/CompositionPropertySet.cs`
- `public void InsertColor(string propertyName, Avalonia.Media.Color value) => Set(propertyName, value);`
- `public void InsertMatrix3x2(string propertyName, Matrix3x2 value) => Set(propertyName, value);`
- `public void InsertMatrix4x4(string propertyName, Matrix4x4 value) => Set(propertyName, value);`
- `public void InsertQuaternion(string propertyName, Quaternion value) => Set(propertyName, value);`
- `public void InsertVector2(string propertyName, Vector2 value) => Set(propertyName, value);`
- `public void InsertVector4(string propertyName, Vector4 value) => Set(propertyName, value);`
- `public CompositionGetValueStatus TryGetColor(string propertyName, out Avalonia.Media.Color value) => TryGetVariant(propertyName, out value);`
- `public CompositionGetValueStatus TryGetMatrix3x2(string propertyName, out Matrix3x2 value) => TryGetVariant(propertyName, out value);`
- `public CompositionGetValueStatus TryGetMatrix4x4(string propertyName, out Matrix4x4 value) => TryGetVariant(propertyName, out value);`
- `public CompositionGetValueStatus TryGetQuaternion(string propertyName, out Quaternion value) => TryGetVariant(propertyName, out value);`
- `public CompositionGetValueStatus TryGetScalar(string propertyName, out float value) => TryGetVariant(propertyName, out value);`
- `public CompositionGetValueStatus TryGetVector2(string propertyName, out Vector2 value) => TryGetVariant(propertyName, out value);`
- `public CompositionGetValueStatus TryGetVector3(string propertyName, out Vector3 value) => TryGetVariant(propertyName, out value);`
- `public CompositionGetValueStatus TryGetVector4(string propertyName, out Vector4 value) => TryGetVariant(propertyName, out value);`
- `public void InsertBoolean(string propertyName, bool value) => Set(propertyName, value);`
- `public CompositionGetValueStatus TryGetBoolean(string propertyName, out bool value) => TryGetVariant(propertyName, out value);`
- `public enum CompositionGetValueStatus`

### `src/Avalonia.Base/Rendering/Composition/CompositionSurface.cs`
- `public class CompositionSurface : CompositionObject`

### `src/Avalonia.Base/Rendering/Composition/Compositor.Factories.cs`
- `public CompositionDrawingSurface CreateDrawingSurface() => new(this);`

### `src/Avalonia.Base/Rendering/Composition/Compositor.cs`
- `public CompositionBatch RequestCompositionBatchCommitAsync() {`
- `public async ValueTask<object?> TryGetRenderInterfaceFeature(Type featureType) {`
- `public async Task<Bitmap> CreateCompositionVisualSnapshot(CompositionVisual visual, double scaling) {`
- `public async ValueTask<ICompositionGpuInterop?> TryGetCompositionGpuInterop() {`
- `public static Compositor? TryGetDefaultCompositor() => AvaloniaLocator.Current.GetService<Compositor>();`

### `src/Avalonia.Base/Rendering/Composition/ContainerVisual.cs`
- `public partial class CompositionContainerVisual : CompositionVisual`

### `src/Avalonia.Base/Rendering/Composition/ElementCompositionPreview.cs`
- `public static CompositionVisual? GetElementChildVisual(Visual visual) => visual.ChildCompositionVisual;`

### `src/Avalonia.Base/Rendering/Composition/Enums.cs`
- `public enum CompositionBlendMode`
- `public enum CompositionGradientExtendMode`
- `public enum CompositionTileMode`
- `public enum CompositionStretch`

### `src/Avalonia.Base/Rendering/Composition/Server/ServerCompositionVisual.cs`
- `public record struct UpdateResult(LtrbRect? Bounds, bool InvalidatedOld, bool InvalidatedNew)`
- `public UpdateResult() : this(null, false, false) {`
- `public struct ReadbackData`
- `public Matrix Matrix;`
- `public ulong Revision;`
- `public long TargetId;`
- `public bool Visible;`

### `src/Avalonia.Base/Rendering/Composition/Transport/Batch.cs`
- `public sealed class CompositionBatch`
- `public Task Processed => _acceptedTcs.Task;`
- `public Task Rendered => _renderedTcs.Task;`

### `src/Avalonia.Base/Rendering/Composition/Transport/BatchStream.cs`
- `public record struct BatchStreamSegment<TData>`
- `public int ElementCount { get; set; }`

### `src/Avalonia.Base/Rendering/Composition/Transport/ServerListProxyHelper.cs`
- `public interface IRegisterForSerialization`

### `src/Avalonia.Base/Rendering/Composition/Visual.cs`
- `public abstract partial class CompositionVisual`
- `public IBrush? OpacityMask {`

### `src/Avalonia.Base/Rendering/Composition/VisualCollection.cs`
- `public partial class CompositionVisualCollection : CompositionObject`
- `public void InsertAbove(CompositionVisual newChild, CompositionVisual sibling) {`
- `public void InsertBelow(CompositionVisual newChild, CompositionVisual sibling) {`
- `public void InsertAtTop(CompositionVisual newChild) => Insert(_list.Count, newChild);`
- `public void InsertAtBottom(CompositionVisual newChild) => Insert(0, newChild);`

### `src/Avalonia.Base/Rendering/DefaultRenderTimer.cs`
- `public class DefaultRenderTimer : IRenderTimer`
- `public DefaultRenderTimer(int framesPerSecond) {`
- `public int FramesPerSecond { get; }`
- `public virtual bool RunsInBackground => true;`

### `src/Avalonia.Base/Rendering/IRenderRoot.cs`
- `public IHitTester HitTester { get; }`

### `src/Avalonia.Base/Rendering/IRenderTimer.cs`
- `public interface IRenderTimer`

### `src/Avalonia.Base/Rendering/IRenderer.cs`
- `public interface IRenderer : IDisposable`
- `public ValueTask<object?> TryGetRenderInterfaceFeature(Type featureType);`
- `public interface IHitTester`

### `src/Avalonia.Base/Rendering/SceneInvalidatedEventArgs.cs`
- `public class SceneInvalidatedEventArgs : EventArgs`
- `public SceneInvalidatedEventArgs( IRenderRoot root, Rect dirtyRect) {`
- `public Rect DirtyRect { get; }`
- `public IRenderRoot RenderRoot { get; }`

### `src/Avalonia.Base/Rendering/SleepLoopRenderTimer.cs`
- `public class SleepLoopRenderTimer : IRenderTimer`
- `public SleepLoopRenderTimer(int fps) {`
- `public bool RunsInBackground => true;`

### `src/Avalonia.Base/Rendering/ThreadProxyRenderTimer.cs`
- `public sealed class ThreadProxyRenderTimer : IRenderTimer`
- `public ThreadProxyRenderTimer(IRenderTimer inner, int maxStackSize = 1 * 1024 * 1024) {`
- `public bool RunsInBackground => true;`

### `src/Avalonia.Base/Rendering/UiThreadRenderTimer.cs`
- `public class UiThreadRenderTimer : DefaultRenderTimer`
- `public UiThreadRenderTimer(int framesPerSecond) : base(framesPerSecond) {`
- `public override bool RunsInBackground => false;`

### `src/Avalonia.Base/Rotate3DTransform.cs`
- `public sealed class Rotate3DTransform : Transform`
- `public static readonly StyledProperty<double> AngleXProperty = AvaloniaProperty.Register<Rotate3DTransform, double>(nameof(AngleX));`
- `public static readonly StyledProperty<double> AngleYProperty = AvaloniaProperty.Register<Rotate3DTransform, double>(nameof(AngleY));`
- `public static readonly StyledProperty<double> AngleZProperty = AvaloniaProperty.Register<Rotate3DTransform, double>(nameof(AngleZ));`
- `public static readonly StyledProperty<double> CenterXProperty = AvaloniaProperty.Register<Rotate3DTransform, double>(nameof(CenterX));`
- `public static readonly StyledProperty<double> CenterYProperty = AvaloniaProperty.Register<Rotate3DTransform, double>(nameof(CenterY));`
- `public static readonly StyledProperty<double> CenterZProperty = AvaloniaProperty.Register<Rotate3DTransform, double>(nameof(CenterZ));`
- `public static readonly StyledProperty<double> DepthProperty = AvaloniaProperty.Register<Rotate3DTransform, double>(nameof(Depth));`
- `public Rotate3DTransform() { }`
- `public Rotate3DTransform( double angleX, double angleY, double angleZ, double centerX, double centerY, double centerZ, double depth) : this() {`
- `public double AngleX {`
- `public double AngleY {`
- `public double AngleZ {`
- `public double CenterX {`
- `public double CenterY {`
- `public double CenterZ {`
- `public double Depth {`

### `src/Avalonia.Base/RoundedRect.cs`
- `public struct RoundedRect`
- `public Rect Rect { get; }`
- `public Vector RadiiTopLeft { get; }`
- `public Vector RadiiTopRight { get; }`
- `public Vector RadiiBottomLeft { get; }`
- `public Vector RadiiBottomRight { get; }`
- `public RoundedRect( Rect rect, Vector radiiTopLeft, Vector radiiTopRight, Vector radiiBottomRight, Vector radiiBottomLeft) {`
- `public RoundedRect( Rect rect, double radiusTopLeft, double radiusTopRight, double radiusBottomRight, double radiusBottomLeft) : this(rect, new Vector(radiusTopLeft, radiusTopLeft), new Vector(radiusTopRight, radiusTopRight), new Vector(radiusBottomRight, radiusBottomRight), new Vector(radiusBottomLeft, radiusBottomLeft) ) {`
- `public RoundedRect(Rect rect, Vector radii) : this(rect, radii, radii, radii, radii) {`
- `public RoundedRect(Rect rect, double radiusX, double radiusY) : this(rect, new Vector(radiusX, radiusY)) {`
- `public RoundedRect(Rect rect, double radius) : this(rect, radius, radius) {`
- `public RoundedRect(Rect rect) : this(rect, 0) {`
- `public RoundedRect(in Rect bounds, in CornerRadius radius) : this(bounds, radius.TopLeft, radius.TopRight, radius.BottomRight, radius.BottomLeft) {`
- `public static implicit operator RoundedRect(Rect r) => new RoundedRect(r);`
- `public bool IsRounded => RadiiTopLeft != default || RadiiTopRight != default || RadiiBottomRight != default ||`
- `public bool IsUniform =>`
- `public RoundedRect Inflate(double dx, double dy) {`
- `public unsafe RoundedRect Deflate(double dx, double dy) {`
- `public bool ContainsExclusive(Point p) {`

### `src/Avalonia.Base/StyledElement.cs`
- `public static readonly DirectProperty<StyledElement, StyledElement?> ParentProperty = AvaloniaProperty.RegisterDirect<StyledElement, StyledElement?>(nameof(Parent), o => o.Parent);`
- `public static readonly DirectProperty<StyledElement, AvaloniaObject?> TemplatedParentProperty = AvaloniaProperty.RegisterDirect<StyledElement, AvaloniaObject?>( nameof(TemplatedParent), o => o.TemplatedParent);`
- `public StyledElement() {`
- `public event EventHandler? DataContextChanged;`
- `public event EventHandler? Initialized;`
- `public bool IsInitialized { get; private set; }`
- `public Type StyleKey => StyleKeyOverride;`
- `public StyledElement? Parent { get; private set; }`
- `public virtual void BeginInit() {`
- `public virtual void EndInit() {`
- `public bool ApplyStyling() {`

### `src/Avalonia.Base/StyledElementExtensions.cs`
- `public static IDisposable BindClass(this StyledElement target, string className, IBinding source, object anchor) =>`
- `public static AvaloniaProperty GetClassProperty(string className) =>`

### `src/Avalonia.Base/StyledProperty.cs`
- `public class StyledPropertyMetadata<TValue> : AvaloniaPropertyMetadata, IStyledPropertyMetadata`
- `public StyledPropertyMetadata( Optional<TValue> defaultValue = default, BindingMode defaultBindingMode = BindingMode.Default, Func<AvaloniaObject, TValue, TValue>? coerce = null, bool enableDataValidation = false) : base(defaultBindingMode, enableDataValidation) {`
- `public TValue DefaultValue {`

### `src/Avalonia.Base/Threading/AvaloniaSynchronizationContext.cs`
- `public class AvaloniaSynchronizationContext : SynchronizationContext`
- `public AvaloniaSynchronizationContext() : this(Dispatcher.UIThread, DispatcherPriority.Default, Thread.CurrentThread.GetApartmentState() == ApartmentState.STA) {`
- `public AvaloniaSynchronizationContext(DispatcherPriority priority) : this(Dispatcher.UIThread, priority, false) {`
- `public AvaloniaSynchronizationContext(Dispatcher dispatcher, DispatcherPriority priority) : this(dispatcher, priority, false) {`
- `public static bool AutoInstall { get; set; } = true;`
- `public static void InstallIfNeeded() {`
- `public record struct RestoreContext : IDisposable`
- `public static RestoreContext Ensure(DispatcherPriority priority) => Ensure(Dispatcher.UIThread, priority);`
- `public static RestoreContext Ensure(Dispatcher dispatcher, DispatcherPriority priority) {`

### `src/Avalonia.Base/Threading/IDispatcher.cs`
- `public interface IDispatcher`

### `src/Avalonia.Base/Threading/IDispatcherImpl.cs`
- `public interface IDispatcherImpl`
- `public interface IDispatcherImplWithPendingInput : IDispatcherImpl`
- `public interface IDispatcherImplWithExplicitBackgroundProcessing : IDispatcherImpl`
- `public interface IControlledDispatcherImpl : IDispatcherImplWithPendingInput`

### `src/Avalonia.Base/Utilities/IWeakEventSubscriber.cs`
- `public interface IWeakEventSubscriber<in TEventArgs>`
- `public sealed class WeakEventSubscriber<TEventArgs> : IWeakEventSubscriber<TEventArgs>`
- `public event Action<object?, WeakEvent, TEventArgs>? Event;`
- `public sealed class TargetWeakEventSubscriber<TTarget, TEventArgs> : IWeakEventSubscriber<TEventArgs>`
- `public TargetWeakEventSubscriber(TTarget target, Action<TTarget, object?, WeakEvent, TEventArgs> dispatchFunc) {`

### `src/Avalonia.Base/Utilities/ImmutableReadOnlyListStructEnumerator.cs`
- `public struct ImmutableReadOnlyListStructEnumerator<T> : IEnumerator<T>`
- `public ImmutableReadOnlyListStructEnumerator(IReadOnlyList<T> readOnlyList) {`
- `public T Current => _current!;`
- `public bool MoveNext() {`
- `public void Reset() {`

### `src/Avalonia.Base/Utilities/SynchronousCompletionAsyncResult.cs`
- `public record struct SynchronousCompletionAsyncResult<T> : INotifyCompletion`
- `public SynchronousCompletionAsyncResult(T result) {`
- `public class SynchronousCompletionAsyncResultSource<T>`
- `public SynchronousCompletionAsyncResult<T> AsyncResult => new SynchronousCompletionAsyncResult<T>(this);`
- `public void SetResult(T result) {`
- `public void TrySetResult(T result) {`

### `src/Avalonia.Base/Utilities/TypeUtilities.cs`
- `public static class TypeUtilities`
- `public static bool AcceptsNull(Type type) {`
- `public static bool AcceptsNull<T>() {`
- `public static bool CanCast<T>(object? value) {`
- `public static bool TryConvert(Type to, object? value, CultureInfo? culture, out object? result) {`
- `public static bool TryConvertImplicit(Type to, object? value, out object? result) {`
- `public static object? ConvertOrDefault(object? value, Type type, CultureInfo culture) {`
- `public static object? ConvertImplicitOrDefault(object? value, Type type) {`
- `public static T ConvertImplicit<T>(object? value) {`
- `public static bool IsNumeric(Type type) {`

### `src/Avalonia.Base/Utilities/ValueSpan.cs`
- `public readonly record struct ValueSpan<T>`
- `public ValueSpan(int start, int length, T value) {`
- `public int Length { get; }`

### `src/Avalonia.Base/Utilities/WeakEvent.cs`
- `public sealed class WeakEvent<TSender, TEventArgs> : WeakEvent where TSender : class`
- `public void Unsubscribe(TSender target, IWeakEventSubscriber<TEventArgs> subscriber) {`
- `public class WeakEvent`

### `src/Avalonia.Base/Utilities/WeakEventHandlerManager.cs`
- `public static class WeakEventHandlerManager`
- `public static void Unsubscribe<TEventArgs, TSubscriber>(object target, string eventName, EventHandler<TEventArgs> subscriber) where TEventArgs : EventArgs where TSubscriber : class {`

### `src/Avalonia.Base/Utilities/WeakEvents.cs`
- `public class WeakEvents`
- `public static readonly WeakEvent<INotifyPropertyChanged, PropertyChangedEventArgs> ThreadSafePropertyChanged = WeakEvent.Register<INotifyPropertyChanged, PropertyChangedEventArgs>( (s, h) =>`
- `public static readonly WeakEvent<AvaloniaObject, AvaloniaPropertyChangedEventArgs> AvaloniaPropertyChanged = WeakEvent.Register<AvaloniaObject, AvaloniaPropertyChangedEventArgs>( (s, h) =>`
- `public static readonly WeakEvent<ICommand, EventArgs> CommandCanExecuteChanged = WeakEvent.Register<ICommand>((s, h) => s.CanExecuteChanged += h,`

### `src/Avalonia.Base/Vector3D.cs`
- `public readonly record struct Vector3D(double X, double Y, double Z)`
- `public static implicit operator Vector3D(Vector3 vector) => new(vector);`
- `public static double Dot(Vector3D vector1, Vector3D vector2) =>`
- `public static Vector3D operator +(Vector3D left, Vector3D right) => Add(left, right);`
- `public static Vector3D Substract(Vector3D left, Vector3D right) =>`
- `public static Vector3D operator -(Vector3D left, Vector3D right) => Substract(left, right);`
- `public static Vector3D operator -(Vector3D v) => new(-v.X, -v.Y, -v.Z);`
- `public static Vector3D Multiply(Vector3D left, Vector3D right) =>`
- `public static Vector3D Multiply(Vector3D left, double right) =>`
- `public static Vector3D operator *(Vector3D left, double right) => Multiply(left, right);`
- `public static Vector3D Divide(Vector3D left, Vector3D right) =>`
- `public static Vector3D Divide(Vector3D left, double right) =>`
- `public Vector3D Abs() => new(Math.Abs(X), Math.Abs(Y), Math.Abs(Z));`
- `public double Length => Math.Sqrt(Dot(this, this));`
- `public static Vector3D Normalize(Vector3D value) => Divide(value, value.Length);`
- `public static double DistanceSquared(Vector3D value1, Vector3D value2) {`
- `public static double Distance(Vector3D value1, Vector3D value2) => Math.Sqrt(DistanceSquared(value1, value2));`

### `src/Avalonia.Base/Visual.cs`
- `public static readonly StyledProperty<bool> ClipToBoundsProperty = AvaloniaProperty.Register<Visual, bool>(nameof(ClipToBounds));`
- `public static readonly StyledProperty<Geometry?> ClipProperty = AvaloniaProperty.Register<Visual, Geometry?>(nameof(Clip));`
- `public static readonly StyledProperty<IBrush?> OpacityMaskProperty = AvaloniaProperty.Register<Visual, IBrush?>(nameof(OpacityMask));`
- `public static readonly StyledProperty<IEffect?> EffectProperty = AvaloniaProperty.Register<Visual, IEffect?>(nameof(Effect));`
- `public static readonly DirectProperty<Visual, bool> HasMirrorTransformProperty = AvaloniaProperty.RegisterDirect<Visual, bool>(nameof(HasMirrorTransform), o => o.HasMirrorTransform);`
- `public static readonly StyledProperty<RelativePoint> RenderTransformOriginProperty = AvaloniaProperty.Register<Visual, RelativePoint>(nameof(RenderTransformOrigin), defaultValue: RelativePoint.Center);`
- `public static readonly AttachedProperty<FlowDirection> FlowDirectionProperty = AvaloniaProperty.RegisterAttached<Visual, Visual, FlowDirection>( nameof(FlowDirection), inherits: true);`
- `public static readonly DirectProperty<Visual, Visual?> VisualParentProperty = AvaloniaProperty.RegisterDirect<Visual, Visual?>(nameof(VisualParent), o => o._visualParent);`
- `public static readonly StyledProperty<int> ZIndexProperty = AvaloniaProperty.Register<Visual, int>(nameof(ZIndex));`
- `public Geometry? Clip {`
- `public bool IsEffectivelyVisible { get; private set; } = true;`
- `public double Opacity {`
- `public IBrush? OpacityMask {`
- `public IEffect? Effect {`
- `public bool HasMirrorTransform {`
- `public RelativePoint RenderTransformOrigin {`
- `public static FlowDirection GetFlowDirection(Visual visual) {`
- `public static void SetFlowDirection(Visual visual, FlowDirection value) {`

### `src/Avalonia.Base/VisualExtensions.cs`
- `public static Point PointToClient(this Visual visual, PixelPoint point) {`
- `public static PixelPoint PointToScreen(this Visual visual, Point point) {`
- `public static Matrix? TransformToVisual(this Visual from, Visual to) {`
- `public static Point? TranslatePoint(this Visual visual, Point point, Visual relativeTo) {`

### `src/Avalonia.Base/VisualTree/TransformedBounds.cs`
- `public readonly struct TransformedBounds : IEquatable<TransformedBounds>`
- `public TransformedBounds(Rect bounds, Rect clip, Matrix transform) {`
- `public Rect Clip { get; }`

### `src/Avalonia.Base/VisualTree/VisualExtensions.cs`
- `public static int CalculateDistanceFromAncestor(this Visual visual, Visual? ancestor) {`
- `public static int CalculateDistanceFromRoot(Visual visual) {`
- `public static Visual? FindCommonVisualAncestor(this Visual? visual, Visual? target) {`
- `public static IEnumerable<Visual> SortByZIndex(this IEnumerable<Visual> elements) {`

### `src/Avalonia.Base/VisualTree/VisualLocator.cs`
- `public class VisualLocator`

### `src/Avalonia.Base/VisualTreeAttachmentEventArgs.cs`
- `public Visual Parent { get; }`
- `public IRenderRoot Root { get; }`

### `src/Avalonia.Build.Tasks/CompileAvaloniaXamlTask.cs`
- `public const string AvaloniaCompileOutputMetadataName = "AvaloniaCompileOutput";`
- `public string ProjectDirectory { get; set; }`
- `public ITaskItem AssemblyFile { get; set; }`
- `public ITaskItem? RefAssemblyFile { get; set; }`
- `public bool VerifyIl { get; set; }`
- `public bool DefaultCompileBindings { get; set; }`
- `public bool SkipXamlCompilation { get; set; }`
- `public string AssemblyOriginatorKeyFile { get; set; }`
- `public bool SignAssembly { get; set; }`
- `public bool DelaySign { get; set; }`
- `public string ReportImportance { get; set; }`
- `public IBuildEngine BuildEngine { get; set; }`
- `public ITaskHost HostObject { get; set; }`
- `public bool DebuggerLaunch { get; set; }`
- `public bool VerboseExceptions { get; set; }`
- `public ITaskItem[] AnalyzerConfigFiles { get; set; }`

### `src/Avalonia.Build.Tasks/DeterministicIdGenerator.cs`
- `public class DeterministicIdGenerator : IXamlIdentifierGenerator`
- `public string GenerateIdentifierPart() => (_nextId++).ToString();`

### `src/Avalonia.Build.Tasks/GenerateAvaloniaResourcesTask.cs`
- `public string Root { get; set; }`
- `public string Output { get; set; }`
- `public string ReportImportance { get; set; }`
- `public IBuildEngine BuildEngine { get; set; }`
- `public ITaskHost HostObject { get; set; }`

### `src/Avalonia.Build.Tasks/XamlCompilerDiagnosticsFilter.cs`
- `public class XamlCompilerDiagnosticsFilter`
- `public XamlCompilerDiagnosticsFilter( ITaskItem[]? analyzerConfigFiles) {`

### `src/Avalonia.Build.Tasks/XamlCompilerTaskExecutor.cs`
- `public class CompileResult`
- `public bool WrittenFile { get; }`
- `public CompileResult(bool success, bool writtenFile = false) {`

### `src/Avalonia.Build.Tasks/XamlFileInfo.cs`
- `public class XamlFileInfo`
- `public string XClass { get; set; }`

### `src/Avalonia.Controls.ColorPicker/ColorChangedEventArgs.cs`
- `public ColorChangedEventArgs(Color oldColor, Color newColor) {`
- `public Color OldColor { get; private set; }`

### `src/Avalonia.Controls.ColorPicker/ColorPalettes/FlatColorPalette.cs`
- `public class FlatColorPalette : IColorPalette`
- `public enum FlatColor : uint`
- `public int ColorCount {`
- `public int ShadeCount {`
- `public Color GetColor(int colorIndex, int shadeIndex) {`

### `src/Avalonia.Controls.ColorPicker/ColorPalettes/FlatHalfColorPalette.cs`
- `public class FlatHalfColorPalette : IColorPalette`
- `public int ColorCount {`
- `public int ShadeCount {`
- `public Color GetColor(int colorIndex, int shadeIndex) {`

### `src/Avalonia.Controls.ColorPicker/ColorPalettes/FluentColorPalette.cs`
- `public class FluentColorPalette : IColorPalette`
- `public int ColorCount {`
- `public int ShadeCount {`
- `public Color GetColor(int colorIndex, int shadeIndex) {`

### `src/Avalonia.Controls.ColorPicker/ColorPalettes/IColorPalette.cs`
- `public interface IColorPalette`

### `src/Avalonia.Controls.ColorPicker/ColorPalettes/MaterialColorPalette.cs`
- `public class MaterialColorPalette : IColorPalette`
- `public enum MaterialColor : uint`
- `public int ColorCount {`
- `public int ShadeCount {`
- `public Color GetColor(int colorIndex, int shadeIndex) {`

### `src/Avalonia.Controls.ColorPicker/ColorPalettes/MaterialHalfColorPalette.cs`
- `public class MaterialHalfColorPalette : IColorPalette`
- `public int ColorCount {`
- `public int ShadeCount {`
- `public Color GetColor(int colorIndex, int shadeIndex) {`

### `src/Avalonia.Controls.ColorPicker/ColorPalettes/SixteenColorPalette.cs`
- `public class SixteenColorPalette : IColorPalette`
- `public int ColorCount {`
- `public int ShadeCount {`
- `public Color GetColor(int colorIndex, int shadeIndex) {`

### `src/Avalonia.Controls.ColorPicker/ColorSpectrum/ColorSpectrum.Properties.cs`
- `public int MaxHue {`
- `public int MinHue {`

### `src/Avalonia.Controls.ColorPicker/ColorSpectrum/ColorSpectrum.cs`
- `public void RaiseColorChanged() {`

### `src/Avalonia.Controls.ColorPicker/ColorView/ColorView.Properties.cs`
- `public static readonly StyledProperty<bool> IsComponentTextInputVisibleProperty = AvaloniaProperty.Register<ColorView, bool>( nameof(IsComponentTextInputVisible), true);`
- `public static readonly StyledProperty<bool> IsHexInputVisibleProperty = AvaloniaProperty.Register<ColorView, bool>( nameof(IsHexInputVisible), true);`
- `public static readonly StyledProperty<IEnumerable<Color>?> PaletteColorsProperty = AvaloniaProperty.Register<ColorView, IEnumerable<Color>?>( nameof(PaletteColors), null);`
- `public static readonly StyledProperty<int> PaletteColumnCountProperty = AvaloniaProperty.Register<ColorView, int>( nameof(PaletteColumnCount), 4);`
- `public static readonly StyledProperty<IColorPalette?> PaletteProperty = AvaloniaProperty.Register<ColorView, IColorPalette?>( nameof(Palette), null);`
- `public bool IsComponentTextInputVisible {`
- `public bool IsHexInputVisible {`
- `public int MaxHue {`
- `public int MinHue {`
- `public IEnumerable<Color>? PaletteColors {`
- `public int PaletteColumnCount {`
- `public IColorPalette? Palette {`

### `src/Avalonia.Controls.ColorPicker/ColorView/ColorViewTab.cs`
- `public enum ColorViewTab`

### `src/Avalonia.Controls.ColorPicker/Converters/AccentColorConverter.cs`
- `public class AccentColorConverter : IValueConverter`
- `public const double ValueDelta = 0.1;`
- `public static HsvColor GetAccent(HsvColor hsvColor, int accentStep) {`

### `src/Avalonia.Controls.ColorPicker/Converters/ColorToDisplayNameConverter.cs`
- `public class ColorToDisplayNameConverter : IValueConverter`

### `src/Avalonia.Controls.ColorPicker/Converters/ColorToHexConverter.cs`
- `public class ColorToHexConverter : IValueConverter`
- `public AlphaComponentPosition AlphaPosition { get; set; } = AlphaComponentPosition.Leading;`
- `public static string ToHexString( Color color, AlphaComponentPosition alphaPosition, bool includeAlpha = true, bool includeSymbol = false) {`
- `public static Color? ParseHexString( string hexColor, AlphaComponentPosition alphaPosition) {`

### `src/Avalonia.Controls.ColorPicker/Converters/ContrastBrushConverter.cs`
- `public class ContrastBrushConverter : IValueConverter`
- `public byte AlphaThreshold { get; set; } = 128;`

### `src/Avalonia.Controls.ColorPicker/Converters/DoNothingForNullConverter.cs`
- `public class DoNothingForNullConverter : IValueConverter`

### `src/Avalonia.Controls.ColorPicker/Converters/ToBrushConverter.cs`
- `public class ToBrushConverter : IValueConverter`

### `src/Avalonia.Controls.ColorPicker/Converters/ToColorConverter.cs`
- `public class ToColorConverter : IValueConverter`

### `src/Avalonia.Controls.ColorPicker/Helpers/ColorHelper.cs`
- `public static class ColorHelper`
- `public static double GetRelativeLuminance(Color color) {`
- `public static bool ToDisplayNameExists {`
- `public static string ToDisplayName(Color color) {`

### `src/Avalonia.Controls.ColorPicker/HsvComponent.cs`
- `public enum HsvComponent`

### `src/Avalonia.Controls.ColorPicker/RgbComponent.cs`
- `public enum RgbComponent`

### `src/Avalonia.Controls/AcrylicPlatformCompensationLevels.cs`
- `public record struct AcrylicPlatformCompensationLevels`
- `public AcrylicPlatformCompensationLevels(double transparent, double blurred, double acrylic) {`
- `public double TransparentLevel { get; }`
- `public double BlurLevel { get; }`
- `public double AcrylicBlurLevel { get; }`

### `src/Avalonia.Controls/AutoCompleteBox/AutoCompleteBox.Properties.cs`
- `public static readonly StyledProperty<AutoCompleteSelector<string?>?> TextSelectorProperty = AvaloniaProperty.Register<AutoCompleteBox, AutoCompleteSelector<string?>?>( nameof(TextSelector));`
- `public static readonly StyledProperty<Func<string?, CancellationToken, Task<IEnumerable<object>>>?> AsyncPopulatorProperty = AvaloniaProperty.Register<AutoCompleteBox, Func<string?, CancellationToken, Task<IEnumerable<object>>>?>( nameof(AsyncPopulator));`
- `public static readonly StyledProperty<int> MaxLengthProperty = TextBox.MaxLengthProperty.AddOwner<AutoCompleteBox>();`
- `public static readonly StyledProperty<object?> InnerLeftContentProperty = TextBox.InnerLeftContentProperty.AddOwner<AutoCompleteBox>();`
- `public static readonly StyledProperty<object?> InnerRightContentProperty = TextBox.InnerRightContentProperty.AddOwner<AutoCompleteBox>();`
- `public IBinding? ValueMemberBinding {`
- `public AutoCompleteSelector<string?>? TextSelector {`
- `public object? InnerLeftContent {`
- `public object? InnerRightContent {`

### `src/Avalonia.Controls/AutoCompleteBox/AutoCompleteBox.cs`
- `public static readonly RoutedEvent<TextChangedEventArgs> TextChangedEvent = RoutedEvent.Register<AutoCompleteBox, TextChangedEventArgs>( nameof(TextChanged), RoutingStrategies.Bubble);`
- `public event EventHandler<PopulatingEventArgs>? Populating;`
- `public event EventHandler<PopulatedEventArgs>? Populated;`
- `public event EventHandler<CancelEventArgs>? DropDownOpening;`
- `public event EventHandler<CancelEventArgs>? DropDownClosing;`
- `public void PopulateComplete() {`

### `src/Avalonia.Controls/AutoCompleteBox/PopulatedEventArgs.cs`
- `public class PopulatedEventArgs : EventArgs`
- `public PopulatedEventArgs(IEnumerable data) {`

### `src/Avalonia.Controls/AutoCompleteBox/PopulatingEventArgs.cs`
- `public class PopulatingEventArgs : CancelEventArgs`
- `public PopulatingEventArgs(string? parameter) {`

### `src/Avalonia.Controls/Automation/AutomationElementIdentifiers.cs`
- `public static class AutomationElementIdentifiers`
- `public static AutomationProperty BoundingRectangleProperty { get; } = new AutomationProperty();`
- `public static AutomationProperty ClassNameProperty { get; } = new AutomationProperty();`
- `public static AutomationProperty HelpTextProperty { get; } = new AutomationProperty();`
- `public static AutomationProperty ItemStatusProperty { get; } = new AutomationProperty();`
- `public static AutomationProperty LandmarkTypeProperty { get; } = new AutomationProperty();`
- `public static AutomationProperty HeadingLevelProperty { get; } = new AutomationProperty();`

### `src/Avalonia.Controls/Automation/AutomationProperties.cs`
- `public static readonly AttachedProperty<string?> AcceleratorKeyProperty = AvaloniaProperty.RegisterAttached<StyledElement, string?>( "AcceleratorKey", typeof(AutomationProperties));`
- `public static readonly AttachedProperty<AccessibilityView> AccessibilityViewProperty = AvaloniaProperty.RegisterAttached<StyledElement, AccessibilityView>( "AccessibilityView", typeof(AutomationProperties));`
- `public static readonly AttachedProperty<string?> AccessKeyProperty = AvaloniaProperty.RegisterAttached<StyledElement, string?>( "AccessKey", typeof(AutomationProperties));`
- `public static readonly AttachedProperty<string?> AutomationIdProperty = AvaloniaProperty.RegisterAttached<StyledElement, string?>( "AutomationId", typeof(AutomationProperties));`
- `public static readonly AttachedProperty<AutomationControlType?> ControlTypeOverrideProperty = AvaloniaProperty.RegisterAttached<StyledElement, AutomationControlType?>( "ControlTypeOverride", typeof(AutomationProperties));`
- `public static readonly AttachedProperty<string?> HelpTextProperty = AvaloniaProperty.RegisterAttached<StyledElement, string?>( "HelpText", typeof(AutomationProperties));`
- `public static readonly AttachedProperty<AutomationLandmarkType?> LandmarkTypeProperty = AvaloniaProperty.RegisterAttached<StyledElement, AutomationLandmarkType?>( "LandmarkType", typeof(AutomationProperties));`
- `public static readonly AttachedProperty<int> HeadingLevelProperty = AvaloniaProperty.RegisterAttached<StyledElement, int>( "HeadingLevel", typeof(AutomationProperties));`
- `public static readonly AttachedProperty<bool> IsColumnHeaderProperty = AvaloniaProperty.RegisterAttached<StyledElement, bool>( "IsColumnHeader", typeof(AutomationProperties), false);`
- `public static readonly AttachedProperty<bool> IsRequiredForFormProperty = AvaloniaProperty.RegisterAttached<StyledElement, bool>( "IsRequiredForForm", typeof(AutomationProperties), false);`
- `public static readonly AttachedProperty<bool> IsRowHeaderProperty = AvaloniaProperty.RegisterAttached<StyledElement, bool>( "IsRowHeader", typeof(AutomationProperties), false);`
- `public static readonly AttachedProperty<IsOffscreenBehavior> IsOffscreenBehaviorProperty = AvaloniaProperty.RegisterAttached<StyledElement, IsOffscreenBehavior>( "IsOffscreenBehavior", typeof(AutomationProperties), IsOffscreenBehavior.Default);`
- `public static readonly AttachedProperty<string?> ItemStatusProperty = AvaloniaProperty.RegisterAttached<StyledElement, string?>( "ItemStatus", typeof(AutomationProperties));`
- `public static readonly AttachedProperty<string?> ItemTypeProperty = AvaloniaProperty.RegisterAttached<StyledElement, string?>( "ItemType", typeof(AutomationProperties));`
- `public static readonly AttachedProperty<Control> LabeledByProperty = AvaloniaProperty.RegisterAttached<StyledElement, Control>( "LabeledBy", typeof(AutomationProperties));`
- `public static readonly AttachedProperty<AutomationLiveSetting> LiveSettingProperty = AvaloniaProperty.RegisterAttached<StyledElement, AutomationLiveSetting>( "LiveSetting", typeof(AutomationProperties), AutomationLiveSetting.Off);`
- `public static readonly AttachedProperty<int> PositionInSetProperty = AvaloniaProperty.RegisterAttached<StyledElement, int>( "PositionInSet", typeof(AutomationProperties), AutomationPositionInSetDefault);`
- `public static readonly AttachedProperty<int> SizeOfSetProperty = AvaloniaProperty.RegisterAttached<StyledElement, int>( "SizeOfSet", typeof(AutomationProperties), AutomationSizeOfSetDefault);`
- `public static void SetAcceleratorKey(StyledElement element, string value) {`
- `public static string? GetAcceleratorKey(StyledElement element) {`
- `public static void SetAccessibilityView(StyledElement element, AccessibilityView value) {`
- `public static AccessibilityView GetAccessibilityView(StyledElement element) {`
- `public static string? GetAccessKey(StyledElement element) {`
- `public static AutomationControlType? GetControlTypeOverride(StyledElement element) {`
- `public static void SetLandmarkType(StyledElement element, AutomationLandmarkType? value) {`
- `public static AutomationLandmarkType? GetLandmarkType(StyledElement element) {`
- `public static void SetHeadingLevel(StyledElement element, int value) {`
- `public static int GetHeadingLevel(StyledElement element) {`
- `public static void SetIsColumnHeader(StyledElement element, bool value) {`
- `public static bool GetIsColumnHeader(StyledElement element) {`
- `public static bool GetIsRequiredForForm(StyledElement element) {`
- `public static bool GetIsRowHeader(StyledElement element) {`
- `public static void SetIsRowHeader(StyledElement element, bool value) {`
- `public static void SetIsOffscreenBehavior(StyledElement element, IsOffscreenBehavior value) {`
- `public static IsOffscreenBehavior GetIsOffscreenBehavior(StyledElement element) {`
- `public static void SetItemStatus(StyledElement element, string? value) {`
- `public static string? GetItemStatus(StyledElement element) {`
- `public static void SetItemType(StyledElement element, string? value) {`
- `public static string? GetItemType(StyledElement element) {`
- `public static void SetPositionInSet(StyledElement element, int value) {`
- `public static int GetPositionInSet(StyledElement element) {`
- `public static void SetSizeOfSet(StyledElement element, int value) {`
- `public static int GetSizeOfSet(StyledElement element) {`

### `src/Avalonia.Controls/Automation/AutomationProperty.cs`
- `public sealed class AutomationProperty`

### `src/Avalonia.Controls/Automation/AutomationPropertyChangedEventArgs.cs`
- `public class AutomationPropertyChangedEventArgs : EventArgs`
- `public AutomationPropertyChangedEventArgs( AutomationProperty property, object? oldValue, object? newValue) {`

### `src/Avalonia.Controls/Automation/ElementNotEnabledException.cs`
- `public class ElementNotEnabledException : Exception`
- `public ElementNotEnabledException() : base("Element not enabled.") { }`
- `public ElementNotEnabledException(string message) : base(message) { }`

### `src/Avalonia.Controls/Automation/ExpandCollapsePatternIdentifiers.cs`
- `public static class ExpandCollapsePatternIdentifiers`
- `public static AutomationProperty ExpandCollapseStateProperty { get; } = new AutomationProperty();`

### `src/Avalonia.Controls/Automation/ExpandCollapseState.cs`
- `public enum ExpandCollapseState`

### `src/Avalonia.Controls/Automation/Peers/AutomationPeer.cs`
- `public string? GetAcceleratorKey() => GetAcceleratorKeyCore();`
- `public string? GetAccessKey() => GetAccessKeyCore();`
- `public Rect GetBoundingRectangle() => GetBoundingRectangleCore();`
- `public IReadOnlyList<AutomationPeer> GetChildren() => GetOrCreateChildrenCore();`
- `public string GetClassName() => GetClassNameCore() ?? string.Empty;`
- `public string GetLocalizedControlType() => GetLocalizedControlTypeCore();`
- `public AutomationLandmarkType? GetLandmarkType() => GetLandmarkTypeCore();`
- `public int GetHeadingLevel() => GetHeadingLevelCore();`
- `public string? GetItemType() => GetItemTypeCore();`
- `public string? GetItemStatus() => GetItemStatusCore();`
- `public bool HasKeyboardFocus() => HasKeyboardFocusCore();`
- `public bool IsContentElement() => IsContentElementOverrideCore();`
- `public bool IsControlElement() => IsControlElementOverrideCore();`
- `public bool IsKeyboardFocusable() => IsKeyboardFocusableCore();`
- `public bool IsOffscreen() => IsOffscreenCore();`
- `public void SetFocus() => SetFocusCore();`
- `public bool ShowContextMenu() => ShowContextMenuCore();`
- `public T? GetProvider<T>() => (T?)GetProviderCore(typeof(T));`
- `public event EventHandler? ChildrenChanged;`
- `public void RaisePropertyChangedEvent( AutomationProperty property, object? oldValue, object? newValue) {`

### `src/Avalonia.Controls/Automation/Peers/ButtonAutomationPeer.cs`
- `public class ButtonAutomationPeer : ContentControlAutomationPeer,`
- `public ButtonAutomationPeer(Button owner) : base(owner) {`

### `src/Avalonia.Controls/Automation/Peers/ComboBoxAutomationPeer.cs`
- `public class ComboBoxAutomationPeer : SelectingItemsControlAutomationPeer,`
- `public ComboBoxAutomationPeer(ComboBox owner) : base(owner) {`
- `public ExpandCollapseState ExpandCollapseState => ToState(Owner.IsDropDownOpen);`
- `public bool ShowsMenu => true;`
- `public void Collapse() => Owner.IsDropDownOpen = false;`
- `public void Expand() => Owner.IsDropDownOpen = true;`

### `src/Avalonia.Controls/Automation/Peers/ContentControlAutomationPeer.cs`
- `public class ContentControlAutomationPeer : ControlAutomationPeer`

### `src/Avalonia.Controls/Automation/Peers/ControlAutomationPeer.cs`
- `public AutomationPeer GetOrCreate(Control element) {`
- `public static AutomationPeer? FromElement(Control element) => element.GetAutomationPeer();`

### `src/Avalonia.Controls/Automation/Peers/DatePickerAutomationPeer.cs`
- `public class DatePickerAutomationPeer : ControlAutomationPeer, IValueProvider`
- `public DatePickerAutomationPeer(DatePicker owner) : base(owner) {`

### `src/Avalonia.Controls/Automation/Peers/EmbeddableControlRootAutomationPeer.cs`
- `public class EmbeddableControlRootAutomationPeer : ContentControlAutomationPeer, IEmbeddedRootProvider`
- `public EmbeddableControlRootAutomationPeer(EmbeddableControlRoot owner) : base(owner) {`
- `public event EventHandler? FocusChanged;`
- `public AutomationPeer? GetFocus() => _focus is object ? GetOrCreate(_focus) : null;`
- `public AutomationPeer? GetPeerFromPoint(Point p) {`

### `src/Avalonia.Controls/Automation/Peers/ExpanderAutomationPeer.cs`
- `public class ExpanderAutomationPeer : ControlAutomationPeer,`
- `public ExpanderAutomationPeer(Control owner) : base(owner) {`
- `public ExpandCollapseState ExpandCollapseState => ToState(Owner.IsExpanded);`
- `public bool ShowsMenu => false;`
- `public void Collapse() => Owner.IsExpanded = false;`
- `public void Expand() => Owner.IsExpanded = true;`

### `src/Avalonia.Controls/Automation/Peers/ImageAutomationPeer.cs`
- `public class ImageAutomationPeer : ControlAutomationPeer`
- `public ImageAutomationPeer(Control owner) : base(owner) {`

### `src/Avalonia.Controls/Automation/Peers/ItemsControlAutomationPeer.cs`
- `public class ItemsControlAutomationPeer : ControlAutomationPeer, IScrollProvider`
- `public ItemsControlAutomationPeer(ItemsControl owner) : base(owner) {`
- `public bool HorizontallyScrollable => _scroller?.HorizontallyScrollable ?? false;`
- `public double HorizontalScrollPercent => _scroller?.HorizontalScrollPercent ?? -1;`
- `public double HorizontalViewSize => _scroller?.HorizontalViewSize ?? 0;`
- `public bool VerticallyScrollable => _scroller?.VerticallyScrollable ?? false;`
- `public double VerticalScrollPercent => _scroller?.VerticalScrollPercent ?? -1;`
- `public double VerticalViewSize => _scroller?.VerticalViewSize ?? 0;`
- `public void Scroll(ScrollAmount horizontalAmount, ScrollAmount verticalAmount) {`
- `public void SetScrollPercent(double horizontalPercent, double verticalPercent) {`

### `src/Avalonia.Controls/Automation/Peers/LabelAutomationPeer.cs`
- `public class LabelAutomationPeer : ControlAutomationPeer`
- `public LabelAutomationPeer(Label owner) : base(owner) {`

### `src/Avalonia.Controls/Automation/Peers/ListItemAutomationPeer.cs`
- `public class ListItemAutomationPeer : ContentControlAutomationPeer,`
- `public ListItemAutomationPeer(ContentControl owner) : base(owner) {`
- `public ISelectionProvider? SelectionContainer {`

### `src/Avalonia.Controls/Automation/Peers/MenuItemAutomationPeer.cs`
- `public class MenuItemAutomationPeer : ControlAutomationPeer`
- `public MenuItemAutomationPeer(MenuItem owner) : base(owner) {`

### `src/Avalonia.Controls/Automation/Peers/NoneAutomationPeer.cs`
- `public class NoneAutomationPeer : ControlAutomationPeer`
- `public NoneAutomationPeer(Control owner) : base(owner) {`

### `src/Avalonia.Controls/Automation/Peers/PopupAutomationPeer.cs`
- `public class PopupAutomationPeer : ControlAutomationPeer`
- `public PopupAutomationPeer(Popup owner) : base(owner) {`

### `src/Avalonia.Controls/Automation/Peers/PopupRootAutomationPeer.cs`
- `public class PopupRootAutomationPeer : WindowBaseAutomationPeer`
- `public PopupRootAutomationPeer(PopupRoot owner) : base(owner) {`

### `src/Avalonia.Controls/Automation/Peers/ProgressBarAutomationPeer.cs`
- `public class ProgressBarAutomationPeer : RangeBaseAutomationPeer, IRangeValueProvider`
- `public ProgressBarAutomationPeer(RangeBase owner) : base(owner) {`

### `src/Avalonia.Controls/Automation/Peers/RadioButtonAutomationPeer.cs`
- `public class RadioButtonAutomationPeer : ToggleButtonAutomationPeer, ISelectionItemProvider`
- `public RadioButtonAutomationPeer(RadioButton owner) : base(owner) {`
- `public ISelectionProvider? SelectionContainer => null;`
- `public void AddToSelection() {`
- `public void RemoveFromSelection() {`

### `src/Avalonia.Controls/Automation/Peers/RangeBaseAutomationPeer.cs`
- `public abstract class RangeBaseAutomationPeer : ControlAutomationPeer, IRangeValueProvider`
- `public RangeBaseAutomationPeer(RangeBase owner) : base(owner) {`

### `src/Avalonia.Controls/Automation/Peers/ScrollBarAutomationPeer.cs`
- `public class ScrollBarAutomationPeer : RangeBaseAutomationPeer`
- `public ScrollBarAutomationPeer(ScrollBar owner) : base(owner) {`

### `src/Avalonia.Controls/Automation/Peers/ScrollViewerAutomationPeer.cs`
- `public class ScrollViewerAutomationPeer : ControlAutomationPeer, IScrollProvider`
- `public ScrollViewerAutomationPeer(ScrollViewer owner) : base(owner) {`
- `public bool HorizontallyScrollable {`
- `public double HorizontalScrollPercent {`
- `public double HorizontalViewSize {`
- `public bool VerticallyScrollable {`
- `public double VerticalScrollPercent {`
- `public double VerticalViewSize {`
- `public void Scroll(ScrollAmount horizontalAmount, ScrollAmount verticalAmount) {`
- `public void SetScrollPercent(double horizontalPercent, double verticalPercent) {`

### `src/Avalonia.Controls/Automation/Peers/SelectingItemsControlAutomationPeer.cs`
- `public abstract class SelectingItemsControlAutomationPeer : ItemsControlAutomationPeer,`
- `public bool CanSelectMultiple => GetSelectionModeCore().HasAllFlags(SelectionMode.Multiple);`
- `public bool IsSelectionRequired => GetSelectionModeCore().HasAllFlags(SelectionMode.AlwaysSelected);`
- `public IReadOnlyList<AutomationPeer> GetSelection() => GetSelectionCore() ?? Array.Empty<AutomationPeer>();`

### `src/Avalonia.Controls/Automation/Peers/SliderAutomationPeer.cs`
- `public class SliderAutomationPeer : RangeBaseAutomationPeer`
- `public SliderAutomationPeer(Slider owner) : base(owner) {`

### `src/Avalonia.Controls/Automation/Peers/TextBlockAutomationPeer.cs`
- `public class TextBlockAutomationPeer : ControlAutomationPeer`
- `public TextBlockAutomationPeer(TextBlock owner) : base(owner) {`

### `src/Avalonia.Controls/Automation/Peers/TextBoxAutomationPeer.cs`
- `public class TextBoxAutomationPeer : ControlAutomationPeer, IValueProvider`
- `public TextBoxAutomationPeer(TextBox owner) : base(owner) {`

### `src/Avalonia.Controls/Automation/Peers/ThumbAutomationPeer.cs`
- `public class ThumbAutomationPeer : ControlAutomationPeer`
- `public ThumbAutomationPeer(Thumb owner) : base(owner) { }`

### `src/Avalonia.Controls/Automation/Peers/TimePickerAutomationPeer.cs`
- `public class TimePickerAutomationPeer : ControlAutomationPeer, IValueProvider`
- `public TimePickerAutomationPeer(TimePicker owner) : base(owner) {`

### `src/Avalonia.Controls/Automation/Peers/ToggleButtonAutomationPeer.cs`
- `public class ToggleButtonAutomationPeer : ContentControlAutomationPeer, IToggleProvider`
- `public ToggleButtonAutomationPeer(ToggleButton owner) : base(owner) {`

### `src/Avalonia.Controls/Automation/Peers/TreeViewAutomationPeer.cs`
- `public class TreeViewAutomationPeer : ItemsControlAutomationPeer`
- `public TreeViewAutomationPeer(TreeView owner) : base(owner) {`

### `src/Avalonia.Controls/Automation/Peers/TreeViewItemAutomationPeer.cs`
- `public class TreeViewItemAutomationPeer : ItemsControlAutomationPeer`
- `public TreeViewItemAutomationPeer(TreeViewItem owner) : base(owner) {`

### `src/Avalonia.Controls/Automation/Peers/UnrealizedElementAutomationPeer.cs`
- `public abstract class UnrealizedElementAutomationPeer : AutomationPeer`
- `public void SetParent(AutomationPeer? parent) => TrySetParent(parent);`

### `src/Avalonia.Controls/Automation/Peers/UserControlAutomationPeer.cs`
- `public class UserControlAutomationPeer : ControlAutomationPeer`
- `public UserControlAutomationPeer(UserControl owner) : base(owner) {`

### `src/Avalonia.Controls/Automation/Peers/WindowAutomationPeer.cs`
- `public class WindowAutomationPeer : WindowBaseAutomationPeer`
- `public WindowAutomationPeer(Window owner) : base(owner) {`

### `src/Avalonia.Controls/Automation/Peers/WindowBaseAutomationPeer.cs`
- `public class WindowBaseAutomationPeer : ControlAutomationPeer, IRootProvider`
- `public WindowBaseAutomationPeer(WindowBase owner) : base(owner) {`
- `public event EventHandler? FocusChanged;`
- `public AutomationPeer? GetFocus() => _focus is object ? GetOrCreate(_focus) : null;`
- `public AutomationPeer? GetPeerFromPoint(Point p) {`

### `src/Avalonia.Controls/Automation/Provider/IEmbeddedRootProvider.cs`
- `public interface IEmbeddedRootProvider`

### `src/Avalonia.Controls/Automation/Provider/IExpandCollapseProvider.cs`
- `public interface IExpandCollapseProvider`

### `src/Avalonia.Controls/Automation/Provider/IInvokeProvider.cs`
- `public interface IInvokeProvider`

### `src/Avalonia.Controls/Automation/Provider/IRangeValueProvider.cs`
- `public interface IRangeValueProvider`

### `src/Avalonia.Controls/Automation/Provider/IRootProvider.cs`
- `public interface IRootProvider`

### `src/Avalonia.Controls/Automation/Provider/IScrollProvider.cs`
- `public enum ScrollAmount`
- `public interface IScrollProvider`

### `src/Avalonia.Controls/Automation/Provider/ISelectionItemProvider .cs`
- `public interface ISelectionItemProvider`

### `src/Avalonia.Controls/Automation/Provider/ISelectionProvider.cs`
- `public interface ISelectionProvider`

### `src/Avalonia.Controls/Automation/Provider/IToggleProvider.cs`
- `public enum ToggleState`
- `public interface IToggleProvider`

### `src/Avalonia.Controls/Automation/Provider/IValueProvider.cs`
- `public interface IValueProvider`

### `src/Avalonia.Controls/Automation/RangeValuePatternIdentifiers.cs`
- `public static class RangeValuePatternIdentifiers`

### `src/Avalonia.Controls/Automation/ScrollPatternIdentifiers.cs`
- `public static class ScrollPatternIdentifiers`
- `public const double NoScroll = -1;`
- `public static AutomationProperty HorizontallyScrollableProperty { get; } = new AutomationProperty();`
- `public static AutomationProperty HorizontalScrollPercentProperty { get; } = new AutomationProperty();`
- `public static AutomationProperty HorizontalViewSizeProperty { get; } = new AutomationProperty();`
- `public static AutomationProperty VerticallyScrollableProperty { get; } = new AutomationProperty();`
- `public static AutomationProperty VerticalScrollPercentProperty { get; } = new AutomationProperty();`
- `public static AutomationProperty VerticalViewSizeProperty { get; } = new AutomationProperty();`

### `src/Avalonia.Controls/Automation/SelectionItemPatternIdentifiers.cs`
- `public static class SelectionItemPatternIdentifiers`
- `public static AutomationProperty SelectionContainerProperty { get; } = new AutomationProperty();`

### `src/Avalonia.Controls/Automation/SelectionPatternIdentifiers.cs`
- `public static class SelectionPatternIdentifiers`
- `public static AutomationProperty CanSelectMultipleProperty { get; } = new AutomationProperty();`
- `public static AutomationProperty IsSelectionRequiredProperty { get; } = new AutomationProperty();`

### `src/Avalonia.Controls/Automation/TogglePatternIdentifiers.cs`
- `public static class TogglePatternIdentifiers`
- `public static AutomationProperty ToggleStateProperty { get; } = new AutomationProperty();`

### `src/Avalonia.Controls/Automation/ValuePatternIdentifiers.cs`
- `public static class ValuePatternIdentifiers`

### `src/Avalonia.Controls/Calendar/Calendar.cs`
- `public class CalendarDateChangedEventArgs : RoutedEventArgs`
- `public DateTime? RemovedDate { get; private set; }`
- `public DateTime? AddedDate { get; private set; }`
- `public class CalendarModeChangedEventArgs : RoutedEventArgs`
- `public CalendarMode OldMode { get; private set; }`
- `public CalendarMode NewMode { get; private set; }`
- `public CalendarModeChangedEventArgs(CalendarMode oldMode, CalendarMode newMode) {`
- `public event EventHandler<SelectionChangedEventArgs>? SelectedDatesChanged;`
- `public event EventHandler<CalendarDateChangedEventArgs>? DisplayDateChanged;`
- `public event EventHandler<CalendarModeChangedEventArgs>? DisplayModeChanged;`

### `src/Avalonia.Controls/Calendar/CalendarBlackoutDatesCollection.cs`
- `public CalendarBlackoutDatesCollection(Calendar owner) {`
- `public void AddDatesInPast() {`
- `public bool ContainsAny(CalendarDateRange range) {`

### `src/Avalonia.Controls/Calendar/CalendarDateRange.cs`
- `public sealed class CalendarDateRange`
- `public CalendarDateRange(DateTime day) {`
- `public CalendarDateRange(DateTime start, DateTime end) {`

### `src/Avalonia.Controls/Calendar/SelectedDatesCollection.cs`
- `public SelectedDatesCollection(Calendar owner) {`

### `src/Avalonia.Controls/CalendarDatePicker/CalendarDatePicker.Properties.cs`
- `public bool UseFloatingWatermark {`

### `src/Avalonia.Controls/CalendarDatePicker/CalendarDatePicker.cs`
- `public event EventHandler? CalendarClosed;`
- `public event EventHandler? CalendarOpened;`
- `public event EventHandler<CalendarDatePickerDateValidationErrorEventArgs>? DateValidationError;`
- `public event EventHandler<SelectionChangedEventArgs>? SelectedDateChanged;`

### `src/Avalonia.Controls/CalendarDatePicker/CalendarDatePickerDateValidationErrorEventArgs.cs`
- `public class CalendarDatePickerDateValidationErrorEventArgs : EventArgs`
- `public CalendarDatePickerDateValidationErrorEventArgs(Exception exception, string text) {`
- `public bool ThrowException {`

### `src/Avalonia.Controls/ColumnDefinition.cs`
- `public static readonly StyledProperty<double> MaxWidthProperty = AvaloniaProperty.Register<ColumnDefinition, double>(nameof(MaxWidth), double.PositiveInfinity);`
- `public static readonly StyledProperty<double> MinWidthProperty = AvaloniaProperty.Register<ColumnDefinition, double>(nameof(MinWidth));`
- `public static readonly StyledProperty<GridLength> WidthProperty = AvaloniaProperty.Register<ColumnDefinition, GridLength>(nameof(Width), new GridLength(1, GridUnitType.Star));`

### `src/Avalonia.Controls/ContainerClearingEventArgs.cs`
- `public class ContainerClearingEventArgs : EventArgs`
- `public ContainerClearingEventArgs(Control container) {`

### `src/Avalonia.Controls/ContainerIndexChangedEventArgs.cs`
- `public class ContainerIndexChangedEventArgs : EventArgs`
- `public ContainerIndexChangedEventArgs(Control container, int oldIndex, int newIndex) {`
- `public int NewIndex { get; }`
- `public int OldIndex { get; }`

### `src/Avalonia.Controls/ContainerPreparedEventArgs.cs`
- `public class ContainerPreparedEventArgs : EventArgs`
- `public ContainerPreparedEventArgs(Control container, int index) {`
- `public int Index { get; }`

### `src/Avalonia.Controls/ContextRequestedEventArgs.cs`
- `public ContextRequestedEventArgs() : base(Control.ContextRequestedEvent) {`
- `public ContextRequestedEventArgs(PointerEventArgs pointerEventArgs) : this() {`
- `public ContextRequestedEventArgs(ContextRequestedEventArgs contextRequestedEventArgs) : this() {`
- `public bool TryGetPosition(Control? relativeTo, out Point point) {`

### `src/Avalonia.Controls/ControlExtensions.cs`
- `public static class ControlExtensions`
- `public static T GetControl<T>(this Control control, string name) where T : Control {`

### `src/Avalonia.Controls/Converters/CornerRadiusFilterConverter.cs`
- `public class CornerRadiusFilterConverter : IValueConverter`
- `public Corners Filter { get; set; }`
- `public double Scale { get; set; } = 1;`

### `src/Avalonia.Controls/Converters/CornerRadiusToDoubleConverter.cs`
- `public class CornerRadiusToDoubleConverter : IValueConverter`
- `public Corners Corner { get; set; }`

### `src/Avalonia.Controls/Converters/Corners.cs`
- `public enum Corners`

### `src/Avalonia.Controls/Converters/EnumToBoolConverter.cs`
- `public class EnumToBoolConverter : IValueConverter`

### `src/Avalonia.Controls/Converters/MarginMultiplierConverter.cs`
- `public class MarginMultiplierConverter : IValueConverter`
- `public double Indent { get; set; }`
- `public bool Top { get; set; } = false;`

### `src/Avalonia.Controls/Converters/MenuScrollingVisibilityConverter.cs`
- `public class MenuScrollingVisibilityConverter : IMultiValueConverter`

### `src/Avalonia.Controls/Converters/PlatformKeyGestureConverter.cs`
- `public class PlatformKeyGestureConverter : IValueConverter`
- `public static string ToPlatformString(KeyGesture gesture) => gesture.ToString("p", null);`

### `src/Avalonia.Controls/Converters/StringFormatConverter.cs`
- `public class StringFormatConverter : IMultiValueConverter`

### `src/Avalonia.Controls/DateTimePickers/DatePicker.cs`
- `public event EventHandler<DatePickerSelectedValueChangedEventArgs>? SelectedDateChanged;`

### `src/Avalonia.Controls/DateTimePickers/DatePickerPresenter.cs`
- `public DateTimeOffset Date {`

### `src/Avalonia.Controls/DateTimePickers/DatePickerSelectedValueChangedEventArgs.cs`
- `public class DatePickerSelectedValueChangedEventArgs`
- `public DateTimeOffset? NewDate { get; }`
- `public DateTimeOffset? OldDate { get; }`
- `public DatePickerSelectedValueChangedEventArgs(DateTimeOffset? oldDate, DateTimeOffset? newDate) {`

### `src/Avalonia.Controls/DateTimePickers/DateTimePickerPanel.cs`
- `public bool IsLogicalScrollEnabled => true;`
- `public Size ScrollSize => new Size(0, ItemHeight);`
- `public Size PageScrollSize => new Size(0, ItemHeight * 4);`
- `public event EventHandler? ScrollInvalidated;`
- `public void RefreshItems() {`
- `public void ScrollUp(int numItems = 1) {`
- `public void ScrollDown(int numItems = 1) {`
- `public Control? GetControlInDirection(NavigationDirection direction, Control? from) { return null; }`
- `public void RaiseScrollInvalidated(EventArgs e) {`

### `src/Avalonia.Controls/DateTimePickers/TimePickerPresenter.cs`
- `public TimeSpan Time {`

### `src/Avalonia.Controls/DateTimePickers/TimePickerSelectedValueChangedEventArgs.cs`
- `public TimeSpan? OldTime { get; }`
- `public TimeSpan? NewTime { get; }`
- `public TimePickerSelectedValueChangedEventArgs(TimeSpan? old, TimeSpan? newT) {`

### `src/Avalonia.Controls/DefinitionBase.cs`
- `public abstract class DefinitionBase : AvaloniaObject`
- `public static readonly AttachedProperty<string?> SharedSizeGroupProperty = AvaloniaProperty.RegisterAttached<DefinitionBase, Control, string?>( "SharedSizeGroup", validate: SharedSizeGroupPropertyValueValid);`

### `src/Avalonia.Controls/DefinitionList.cs`
- `public abstract class DefinitionList<T> : AvaloniaList<T> where T : DefinitionBase`
- `public DefinitionList() {`

### `src/Avalonia.Controls/Design.cs`
- `public static bool IsDesignMode { get; internal set; }`
- `public static readonly AttachedProperty<double> HeightProperty = AvaloniaProperty .RegisterAttached<Control, double>("Height", typeof (Design));`
- `public static void SetHeight(Control control, double value) {`
- `public static double GetHeight(Control control) {`
- `public static readonly AttachedProperty<double> WidthProperty = AvaloniaProperty .RegisterAttached<Control, double>("Width", typeof(Design));`
- `public static void SetWidth(Control control, double value) {`
- `public static double GetWidth(Control control) {`
- `public static void SetDataContext(Control control, object value) {`
- `public static object GetDataContext(Control control) {`
- `public static readonly AttachedProperty<Control?> PreviewWithProperty = AvaloniaProperty .RegisterAttached<AvaloniaObject, Control?>("PreviewWith", typeof (Design));`
- `public static void SetPreviewWith(AvaloniaObject target, Control? control) {`
- `public static void SetPreviewWith(ResourceDictionary target, Control? control) {`
- `public static Control? GetPreviewWith(AvaloniaObject target) {`
- `public static Control? GetPreviewWith(ResourceDictionary target) {`
- `public static readonly AttachedProperty<IStyle> DesignStyleProperty = AvaloniaProperty .RegisterAttached<Control, IStyle>("DesignStyle", typeof(Design));`
- `public static void SetDesignStyle(Control control, IStyle value) {`
- `public static IStyle GetDesignStyle(Control control) {`
- `public static void ApplyDesignModeProperties(Control target, Control source) {`

### `src/Avalonia.Controls/Diagnostics/ToolTipDiagnostics.cs`
- `public static class ToolTipDiagnostics`
- `public static readonly AvaloniaProperty<ToolTip?> ToolTipProperty = ToolTip.ToolTipProperty;`

### `src/Avalonia.Controls/Documents/Inline.cs`
- `public static readonly StyledProperty<TextDecorationCollection?> TextDecorationsProperty = AvaloniaProperty.RegisterAttached<Inline, Inline, TextDecorationCollection?>( nameof(TextDecorations), inherits: true);`
- `public static readonly StyledProperty<BaselineAlignment> BaselineAlignmentProperty = AvaloniaProperty.Register<Inline, BaselineAlignment>( nameof(BaselineAlignment), BaselineAlignment.Baseline);`
- `public BaselineAlignment BaselineAlignment {`
- `public static TextDecorationCollection? GetTextDecorations(Control control) {`

### `src/Avalonia.Controls/Documents/InlineCollection.cs`
- `public class InlineCollection : AvaloniaList<Inline>`
- `public InlineCollection() {`
- `public event EventHandler? Invalidated;`

### `src/Avalonia.Controls/Documents/InlineUIContainer.cs`
- `public class InlineUIContainer : Inline`
- `public InlineUIContainer() {`
- `public InlineUIContainer(Control child) {`

### `src/Avalonia.Controls/Documents/LineBreak.cs`
- `public class LineBreak : Inline`
- `public LineBreak() {`

### `src/Avalonia.Controls/Documents/Span.cs`
- `public static readonly StyledProperty<InlineCollection> InlinesProperty = AvaloniaProperty.Register<Span, InlineCollection>( nameof(Inlines));`

### `src/Avalonia.Controls/Documents/TextElement.cs`
- `public FontFeatureCollection? FontFeatures {`
- `public static FontFamily GetFontFamily(Control control) {`
- `public static FontFeatureCollection? GetFontFeatures(Control control) {`
- `public static double GetFontSize(Control control) {`
- `public static FontStyle GetFontStyle(Control control) {`
- `public static FontWeight GetFontWeight(Control control) {`
- `public static FontStretch GetFontStretch(Control control) {`
- `public static void SetFontStretch(Control control, FontStretch value) {`
- `public static IBrush? GetForeground(Control control) {`
- `public static void SetForeground(Control control, IBrush? value) {`

### `src/Avalonia.Controls/Embedding/Offscreen/OffscreenTopLevelImpl.cs`
- `public abstract class OffscreenTopLevelImplBase : ITopLevelImpl`
- `public IInputRoot? InputRoot { get; private set; }`
- `public OffscreenTopLevelImplBase() => Compositor = new Compositor(null);`
- `public IPlatformHandle? Handle { get; }`
- `public Action<WindowTransparencyLevel>? TransparencyLevelChanged { get; set; }`
- `public void SetFrameThemeVariant(PlatformThemeVariant themeVariant) { }`
- `public AcrylicPlatformCompensationLevels AcrylicCompensationLevels { get; } = new AcrylicPlatformCompensationLevels(1, 1, 1);`
- `public void SetInputRoot(IInputRoot inputRoot) => InputRoot = inputRoot;`
- `public virtual Point PointToClient(PixelPoint point) => point.ToPoint(1);`
- `public virtual PixelPoint PointToScreen(Point point) => PixelPoint.FromPoint(point, 1);`
- `public virtual void SetCursor(ICursorImpl? cursor) {`
- `public abstract IMouseDevice MouseDevice { get; }`
- `public void SetTransparencyLevelHint(IReadOnlyList<WindowTransparencyLevel> transparencyLevel) { }`
- `public WindowTransparencyLevel TransparencyLevel => WindowTransparencyLevel.None;`
- `public IPopupImpl? CreatePopup() => null;`

### `src/Avalonia.Controls/Flyouts/FlyoutBase.cs`
- `public static FlyoutBase? GetAttachedFlyout(Control element) {`
- `public static void SetAttachedFlyout(Control element, FlyoutBase? value) {`

### `src/Avalonia.Controls/Flyouts/FlyoutShowMode.cs`
- `public enum FlyoutShowMode`

### `src/Avalonia.Controls/Flyouts/PopupFlyoutBase.cs`
- `public static readonly StyledProperty<FlyoutShowMode> ShowModeProperty = AvaloniaProperty.Register<PopupFlyoutBase, FlyoutShowMode>(nameof(ShowMode));`

### `src/Avalonia.Controls/Generators/ItemContainerGenerator.cs`
- `public void ItemContainerIndexChanged(Control container, int oldIndex, int newIndex) =>`
- `public int IndexFromContainer(Control container) => _owner.IndexFromContainer(container);`

### `src/Avalonia.Controls/Generators/TreeItemContainerGenerator.cs`
- `public TreeContainerIndex Index { get; }`
- `public class TreeContainerIndex`
- `public Control? ContainerFromItem(object item) => _owner.TreeContainerFromItem(item);`
- `public object? ItemFromContainer(Control container) => _owner.TreeItemFromContainer(container);`

### `src/Avalonia.Controls/Grid.cs`
- `public static readonly StyledProperty<bool> ShowGridLinesProperty = AvaloniaProperty.Register<Grid, bool>(nameof(ShowGridLines));`
- `public static readonly AttachedProperty<int> ColumnProperty = AvaloniaProperty.RegisterAttached<Grid, Control, int>( "Column", defaultValue: 0, validate: v => v >= 0);`
- `public static readonly AttachedProperty<int> ColumnSpanProperty = AvaloniaProperty.RegisterAttached<Grid, Control, int>( "ColumnSpan", defaultValue: 1, validate: v => v > 0);`
- `public static readonly AttachedProperty<int> RowSpanProperty = AvaloniaProperty.RegisterAttached<Grid, Control, int>( "RowSpan", defaultValue: 1, validate: v => v > 0);`
- `public static readonly AttachedProperty<bool> IsSharedSizeScopeProperty = AvaloniaProperty.RegisterAttached<Grid, Control, bool>( "IsSharedSizeScope");`

### `src/Avalonia.Controls/INativeMenuExporterEventsImplBridge.cs`
- `public interface INativeMenuExporterEventsImplBridge`

### `src/Avalonia.Controls/INativeMenuItemExporterEventsImplBridge.cs`
- `public interface INativeMenuItemExporterEventsImplBridge`

### `src/Avalonia.Controls/ItemsControl.cs`
- `public Panel? ItemsPanelRoot => Presenter?.Panel;`
- `public event EventHandler<ContainerPreparedEventArgs>? PreparingContainer;`
- `public event EventHandler<ContainerPreparedEventArgs>? ContainerPrepared;`
- `public event EventHandler<ContainerIndexChangedEventArgs>? ContainerIndexChanged;`
- `public event EventHandler<ContainerClearingEventArgs>? ContainerClearing;`
- `public Control? ContainerFromItem(object item) {`
- `public int IndexFromContainer(Control container) => Presenter?.IndexFromContainer(container) ?? -1;`
- `public object? ItemFromContainer(Control container) {`
- `public static ItemsControl? ItemsControlFromItemContaner(Control container) =>`
- `public static ItemsControl? ItemsControlFromItemContainer(Control container) {`

### `src/Avalonia.Controls/ItemsSourceView.cs`
- `public class ItemsSourceView : IReadOnlyList<object?>,`
- `public object? GetAt(int index) => Source[index];`
- `public static ItemsSourceView GetOrCreate(IEnumerable? items) {`
- `public static ItemsSourceView<T> GetOrCreate<T>(IEnumerable? items) {`
- `public static ItemsSourceView<T> GetOrCreate<T>(IEnumerable<T>? items) {`
- `public sealed class ItemsSourceView<T> : ItemsSourceView, IReadOnlyList<T>`
- `public new T GetAt(int index) => (T)Source[index]!;`

### `src/Avalonia.Controls/ListBox.cs`
- `public IScrollable? Scroll {`

### `src/Avalonia.Controls/MaskedTextBox.cs`
- `public CultureInfo? Culture {`
- `public MaskedTextProvider? MaskProvider { get; private set; }`

### `src/Avalonia.Controls/MenuItem.cs`
- `public bool HasSubMenu => !Classes.Contains(":empty");`
- `public bool IsTopLevel => Parent is Menu;`

### `src/Avalonia.Controls/Mixins/PressedMixin.cs`
- `public static class PressedMixin`

### `src/Avalonia.Controls/Mixins/SelectableMixin.cs`
- `public static class SelectableMixin`

### `src/Avalonia.Controls/NativeMenu.cs`
- `public static readonly DirectProperty<NativeMenu, NativeMenuItem?> ParentProperty = AvaloniaProperty.RegisterDirect<NativeMenu, NativeMenuItem?>(nameof(Parent), o => o.Parent);`
- `public NativeMenuItem? Parent {`

### `src/Avalonia.Controls/NativeMenuItem.cs`
- `public static readonly StyledProperty<string?> ToolTipProperty = AvaloniaProperty.Register<NativeMenuItem, string?>(nameof(ToolTip));`
- `public static readonly StyledProperty<bool> IsEnabledProperty = AvaloniaProperty.Register<NativeMenuItem, bool>(nameof(IsEnabled), true);`
- `public bool HasClickHandlers => Click != null;`
- `public enum NativeMenuItemToggleType`

### `src/Avalonia.Controls/NativeMenuItemBase.cs`
- `public static readonly DirectProperty<NativeMenuItemBase, NativeMenu?> ParentProperty = AvaloniaProperty.RegisterDirect<NativeMenuItemBase, NativeMenu?>(nameof(Parent), o => o.Parent);`
- `public NativeMenu? Parent {`

### `src/Avalonia.Controls/NumericUpDown/NumericUpDown.cs`
- `public static readonly StyledProperty<object?> InnerLeftContentProperty = TextBox.InnerLeftContentProperty.AddOwner<NumericUpDown>();`
- `public static readonly StyledProperty<object?> InnerRightContentProperty = TextBox.InnerRightContentProperty.AddOwner<NumericUpDown>();`
- `public object? InnerLeftContent {`
- `public object? InnerRightContent {`
- `public event EventHandler<SpinEventArgs>? Spinned;`

### `src/Avalonia.Controls/NumericUpDown/NumericUpDownValueChangedEventArgs.cs`
- `public class NumericUpDownValueChangedEventArgs : RoutedEventArgs`
- `public NumericUpDownValueChangedEventArgs(RoutedEvent routedEvent, decimal? oldValue, decimal? newValue) : base(routedEvent) {`

### `src/Avalonia.Controls/PixelPointEventArgs.cs`
- `public PixelPointEventArgs(PixelPoint point) {`
- `public PixelPoint Point { get; }`

### `src/Avalonia.Controls/Platform/DefaultMenuInteractionHandler.cs`
- `public static TimeSpan MenuShowDelay { get; set;} = TimeSpan.FromMilliseconds(400);`

### `src/Avalonia.Controls/Platform/Dialogs/IMountedVolumeInfoProvider.cs`
- `public interface IMountedVolumeInfoProvider`

### `src/Avalonia.Controls/Platform/Dialogs/IStorageProviderFactory.cs`
- `public interface IStorageProviderFactory`

### `src/Avalonia.Controls/Platform/Dialogs/ISystemDialogImpl.cs`
- `public interface ISystemDialogImpl`

### `src/Avalonia.Controls/Platform/Dialogs/MountedDriveInfo.cs`
- `public class MountedVolumeInfo : IEquatable<MountedVolumeInfo>`
- `public string? VolumeLabel { get; set; }`
- `public string? VolumePath { get; set; }`
- `public ulong VolumeSizeBytes { get; set; }`

### `src/Avalonia.Controls/Platform/IApplicationPlatformEvents.cs`
- `public interface IApplicationPlatformEvents`

### `src/Avalonia.Controls/Platform/IInputPane.cs`
- `public interface IInputPane`
- `public abstract class InputPaneBase : IInputPane`
- `public virtual InputPaneState State { get; protected set; }`
- `public virtual Rect OccludedRect { get; protected set; }`
- `public event EventHandler<InputPaneStateEventArgs>? StateChanged;`
- `public enum InputPaneState`
- `public sealed class InputPaneStateEventArgs : EventArgs`
- `public InputPaneState NewState { get; }`
- `public Rect? StartRect { get; }`
- `public Rect EndRect { get; }`
- `public TimeSpan AnimationDuration { get; }`
- `public IEasing? Easing { get; }`
- `public InputPaneStateEventArgs(InputPaneState newState, Rect? startRect, Rect endRect, TimeSpan animationDuration, IEasing? easing) {`
- `public InputPaneStateEventArgs(InputPaneState newState, Rect? startRect, Rect endRect) : this(newState, startRect, endRect, default, null) {`

### `src/Avalonia.Controls/Platform/IInsetsManager.cs`
- `public interface IInsetsManager`
- `public abstract class InsetsManagerBase : IInsetsManager`
- `public virtual bool? IsSystemBarVisible { get; set; }`
- `public virtual bool DisplayEdgeToEdgePreference { get; set; }`
- `public virtual bool DisplayEdgeToEdge { get => DisplaysEdgeToEdge; set => DisplayEdgeToEdgePreference = value; }`
- `public virtual Thickness SafeAreaPadding { get; protected set; }`
- `public virtual bool DisplaysEdgeToEdge => DisplayEdgeToEdgePreference;`
- `public event EventHandler<SafeAreaChangedArgs>? SafeAreaChanged;`
- `public class SafeAreaChangedArgs : EventArgs`
- `public SafeAreaChangedArgs(Thickness safeArePadding) {`
- `public Thickness SafeAreaPadding { get; }`
- `public enum SystemBarTheme`

### `src/Avalonia.Controls/Platform/INativeControlHostImpl.cs`
- `public interface INativeControlHostImpl`
- `public interface INativeControlHostDestroyableControlHandle : IPlatformHandle`
- `public interface INativeControlHostControlTopLevelAttachment : IDisposable`

### `src/Avalonia.Controls/Platform/IPlatformIconLoader.cs`
- `public interface IPlatformIconLoader`

### `src/Avalonia.Controls/Platform/IPlatformLifetimeEventsImpl.cs`
- `public interface IPlatformLifetimeEventsImpl`

### `src/Avalonia.Controls/Platform/IPlatformNativeSurfaceHandle.cs`
- `public interface INativePlatformHandleSurface : IPlatformHandle`

### `src/Avalonia.Controls/Platform/IScreenImpl.cs`
- `public interface IScreenImpl`
- `public class PlatformScreen(IPlatformHandle platformHandle) : Screen`
- `public abstract class ScreensBase<TKey, TScreen>(IEqualityComparer<TKey>? screenKeyComparer) : IScreenImpl`
- `public IReadOnlyList<Screen> AllScreens {`
- `public Action? Changed { get; set; }`
- `public Screen? ScreenFromWindow(IWindowBaseImpl window) => ScreenFromTopLevel(window);`
- `public Screen? ScreenFromRect(PixelRect rect) => ScreenFromRectCore(rect);`
- `public void OnChanged() {`

### `src/Avalonia.Controls/Platform/IWin32OptionsTopLevelImpl.cs`
- `public interface IWin32OptionsTopLevelImpl : ITopLevelImpl`
- `public CustomWindowStylesCallback? WindowStylesCallback { get; set; }`
- `public CustomWndProcHookCallback? WndProcHookCallback { get; set; }`

### `src/Avalonia.Controls/Platform/IWindowIconImpl.cs`
- `public interface IWindowIconImpl`

### `src/Avalonia.Controls/Platform/IX11OptionsToplevelImplFeature.cs`
- `public enum X11NetWmWindowType`
- `public interface IX11OptionsToplevelImplFeature`

### `src/Avalonia.Controls/Platform/ManagedDispatcherImpl.cs`
- `public class ManagedDispatcherImpl : IControlledDispatcherImpl`
- `public interface IManagedDispatcherInputProvider`
- `public ManagedDispatcherImpl(IManagedDispatcherInputProvider? inputProvider) {`
- `public bool CurrentThreadIsLoopThread => _loopThread == Thread.CurrentThread;`
- `public void Signal() {`
- `public event Action? Signaled;`
- `public long Now => _clock.ElapsedMilliseconds;`
- `public void UpdateTimer(long? dueTimeInMs) {`
- `public bool CanQueryPendingInput => _inputProvider != null;`
- `public bool HasPendingInput => _inputProvider?.HasInput ?? false;`
- `public void RunLoop(CancellationToken token) {`

### `src/Avalonia.Controls/Platform/PlatformManager.cs`
- `public static IDisposable DesignerMode() {`
- `public static void SetDesignerScalingFactor(double factor) {`
- `public static IWindowImpl CreateWindow() {`
- `public static IWindowImpl CreateEmbeddableWindow() {`

### `src/Avalonia.Controls/Platform/Screen.cs`
- `public enum ScreenOrientation`
- `public double PixelDensity => Scaling;`
- `public bool Primary => IsPrimary;`

### `src/Avalonia.Controls/Platform/Surfaces/IFramebufferPlatformSurface.cs`
- `public interface IFramebufferPlatformSurface`
- `public interface IFramebufferRenderTarget : IDisposable`
- `public interface IFramebufferRenderTargetWithProperties : IFramebufferRenderTarget`
- `public record struct FramebufferLockProperties(bool PreviousFrameIsRetained);`
- `public class FuncFramebufferRenderTarget : IFramebufferRenderTarget`
- `public FuncFramebufferRenderTarget(Func<ILockedFramebuffer> lockFramebuffer) {`
- `public ILockedFramebuffer Lock() => _lockFramebuffer();`

### `src/Avalonia.Controls/Platform/Win32Properties.cs`
- `public delegate (uint style, uint exStyle) CustomWindowStylesCallback(uint style, uint exStyle);`
- `public delegate IntPtr CustomWndProcHookCallback(IntPtr hWnd, uint msg, IntPtr wParam, IntPtr lParam, ref bool handled);`
- `public static void RemoveWindowStylesCallback(TopLevel topLevel, CustomWindowStylesCallback? callback) {`
- `public static void RemoveWndProcHookCallback(TopLevel topLevel, CustomWndProcHookCallback? callback) {`
- `public static void SetNonClientHitTestResult(Visual obj, Win32HitTestValue value) => obj.SetValue(NonClientHitTestResultProperty, value);`
- `public static Win32HitTestValue GetNonClientHitTestResult(Visual obj) => obj.GetValue(NonClientHitTestResultProperty);`
- `public enum Win32HitTestValue`

### `src/Avalonia.Controls/Platform/X11Properties.cs`
- `public static void SetNetWmWindowType(Window obj, X11NetWmWindowType value) => obj.SetValue(NetWmWindowTypeProperty, value);`
- `public static X11NetWmWindowType GetNetWmWindowType(Window obj) => obj.GetValue(NetWmWindowTypeProperty);`
- `public static void SetWmClass(Window obj, string? value) => obj.SetValue(WmClassProperty, value);`
- `public static string? GetWmClass(Window obj) => obj.GetValue(WmClassProperty);`

### `src/Avalonia.Controls/Presenters/ContentPresenter.cs`
- `public static readonly StyledProperty<bool> RecognizesAccessKeyProperty = AvaloniaProperty.Register<ContentPresenter, bool>(nameof(RecognizesAccessKey));`
- `public bool RecognizesAccessKey {`
- `public void UpdateChild() {`

### `src/Avalonia.Controls/Presenters/ScrollContentPresenter.cs`
- `public bool BringDescendantIntoView(Visual target, Rect targetRect) {`

### `src/Avalonia.Controls/Presenters/TextPresenter.cs`
- `public event EventHandler? CaretBoundsChanged;`
- `public FontFeatureCollection? FontFeatures {`
- `public void ShowCaret() {`
- `public void HideCaret() {`
- `public void MoveCaretToTextPosition(int textPosition, bool trailingEdge = false) {`
- `public void MoveCaretToPoint(Point point) {`
- `public void MoveCaretVertical(LogicalDirection direction = LogicalDirection.Forward) {`
- `public CharacterHit GetNextCharacterHit(LogicalDirection direction = LogicalDirection.Forward) {`
- `public void MoveCaretHorizontal(LogicalDirection direction = LogicalDirection.Forward) {`

### `src/Avalonia.Controls/Primitives/Popup.cs`
- `public static readonly AttachedProperty<bool> TakesFocusFromNativeControlProperty = AvaloniaProperty.RegisterAttached<Popup, Control, bool>(nameof(TakesFocusFromNativeControl), true);`
- `public static readonly StyledProperty<bool> ShouldUseOverlayLayerProperty = AvaloniaProperty.Register<Popup, bool>(nameof(ShouldUseOverlayLayer));`
- `public static readonly DirectProperty<Popup, bool> IsUsingOverlayLayerProperty = AvaloniaProperty.RegisterDirect<Popup, bool>( nameof(IsUsingOverlayLayer), o => o.IsUsingOverlayLayer);`
- `public IPopupHost? Host => _openState?.PopupHost;`
- `public IAvaloniaDependencyResolver? DependencyResolver {`
- `public bool TakesFocusFromNativeControl {`
- `public static bool GetTakesFocusFromNativeControl(Control control) {`
- `public static void SetTakesFocusFromNativeControl(Control control, bool value) {`
- `public bool IsInsidePopup(Visual visual) {`
- `public bool IsPointerOverPopup => ((IInputElement?)_openState?.PopupHost)?.IsPointerOver ?? false;`

### `src/Avalonia.Controls/Primitives/PopupPositioning/CustomPopupPlacement.cs`
- `public Size PopupSize { get; }`
- `public Rect AnchorRectangle { get; set; }`
- `public PopupGravity Gravity {`
- `public PopupPositionerConstraintAdjustment ConstraintAdjustment { get; set; }`

### `src/Avalonia.Controls/Primitives/PopupPositioning/IPopupPositioner.cs`
- `public record struct PopupPositionerParameters`
- `public Rect AnchorRectangle { get; set; }`
- `public PopupGravity Gravity {`
- `public PopupPositionerConstraintAdjustment ConstraintAdjustment { get; set; }`

### `src/Avalonia.Controls/Primitives/PopupPositioning/ManagedPopupPositioner.cs`
- `public class ManagedPopupPositionerScreenInfo`
- `public ManagedPopupPositionerScreenInfo(Rect bounds, Rect workingArea) {`
- `public class ManagedPopupPositioner : IPopupPositioner`
- `public ManagedPopupPositioner(IManagedPopupPositionerPopup popup) {`

### `src/Avalonia.Controls/Primitives/PopupPositioning/ManagedPopupPositionerPopupImplHelper.cs`
- `public class ManagedPopupPositionerPopupImplHelper : IManagedPopupPositionerPopup`
- `public delegate void MoveResizeDelegate(PixelPoint position, Size size, double scaling);`
- `public ManagedPopupPositionerPopupImplHelper(ITopLevelImpl parent, MoveResizeDelegate moveResize) {`
- `public Rect ParentClientAreaScreenGeometry {`
- `public void MoveAndResize(Point devicePoint, Size virtualSize) {`

### `src/Avalonia.Controls/Primitives/PopupPositioning/PopupPositionRequest.cs`
- `public class PopupPositionRequest`
- `public PopupGravity Gravity {get;}`
- `public PopupPositionerConstraintAdjustment ConstraintAdjustment {get;}`
- `public Rect? AnchorRect {get;}`
- `public CustomPopupPlacementCallback? PlacementCallback {get;}`

### `src/Avalonia.Controls/Primitives/RangeBaseValueChangedEventArgs.cs`
- `public RangeBaseValueChangedEventArgs(double oldValue, double newValue, RoutedEvent? routedEvent) : base(routedEvent) {`
- `public RangeBaseValueChangedEventArgs(double oldValue, double newValue, RoutedEvent? routedEvent, object? source) : base(routedEvent, source) {`

### `src/Avalonia.Controls/Primitives/ScrollBar.cs`
- `public ScrollEventArgs(ScrollEventType eventType, double newValue) {`
- `public ScrollEventType ScrollEventType { get; private set; }`
- `public event EventHandler<ScrollEventArgs>? Scroll;`

### `src/Avalonia.Controls/Primitives/ScrollEventType.cs`
- `public enum ScrollEventType`

### `src/Avalonia.Controls/Primitives/SelectingItemsControl.cs`
- `public override void BeginInit() {`
- `public override void EndInit() {`
- `public static bool GetIsSelected(Control control) => control.GetValue(IsSelectedProperty);`
- `public static void SetIsSelected(Control control, bool value) => control.SetValue(IsSelectedProperty, value);`

### `src/Avalonia.Controls/Primitives/SelectionHandleType.cs`
- `public enum SelectionHandleType`

### `src/Avalonia.Controls/Primitives/TemplatedControl.cs`
- `public FontFeatureCollection? FontFeatures {`
- `public static bool GetIsTemplateFocusTarget(Control control) {`
- `public static void SetIsTemplateFocusTarget(Control control, bool value) {`

### `src/Avalonia.Controls/Primitives/TextSearch.cs`
- `public static class TextSearch`
- `public static readonly AttachedProperty<IBinding?> TextBindingProperty = AvaloniaProperty.RegisterAttached<Interactive, IBinding?>("TextBinding", typeof(TextSearch));`
- `public static string? GetText(Control control) => control.GetValue(TextProperty);`
- `public static void SetTextBinding(Interactive interactive, IBinding? value) => interactive.SetValue(TextBindingProperty, value);`
- `public static IBinding? GetTextBinding(Interactive interactive) => interactive.GetValue(TextBindingProperty);`

### `src/Avalonia.Controls/Primitives/ToggleButton.cs`
- `public event EventHandler<RoutedEventArgs>? Checked {`

### `src/Avalonia.Controls/Primitives/Track.cs`
- `public virtual double ValueFromPoint(Point point) {`
- `public virtual double ValueFromDistance(double horizontal, double vertical) {`

### `src/Avalonia.Controls/Primitives/VisualLayerManager.cs`
- `public bool IsPopup { get; set; }`

### `src/Avalonia.Controls/ProgressBar.cs`
- `public class ProgressBarTemplateSettings : AvaloniaObject`
- `public static readonly DirectProperty<ProgressBarTemplateSettings, double> ContainerAnimationStartPositionProperty = AvaloniaProperty.RegisterDirect<ProgressBarTemplateSettings, double>( nameof(ContainerAnimationStartPosition), p => p.ContainerAnimationStartPosition,`
- `public static readonly DirectProperty<ProgressBarTemplateSettings, double> ContainerAnimationEndPositionProperty = AvaloniaProperty.RegisterDirect<ProgressBarTemplateSettings, double>( nameof(ContainerAnimationEndPosition), p => p.ContainerAnimationEndPosition,`
- `public static readonly DirectProperty<ProgressBarTemplateSettings, double> Container2AnimationStartPositionProperty = AvaloniaProperty.RegisterDirect<ProgressBarTemplateSettings, double>( nameof(Container2AnimationStartPosition), p => p.Container2AnimationStartPosition,`
- `public static readonly DirectProperty<ProgressBarTemplateSettings, double> Container2AnimationEndPositionProperty = AvaloniaProperty.RegisterDirect<ProgressBarTemplateSettings, double>( nameof(Container2AnimationEndPosition), p => p.Container2AnimationEndPosition,`
- `public static readonly DirectProperty<ProgressBarTemplateSettings, double> Container2WidthProperty = AvaloniaProperty.RegisterDirect<ProgressBarTemplateSettings, double>( nameof(Container2Width), p => p.Container2Width,`
- `public static readonly DirectProperty<ProgressBarTemplateSettings, double> ContainerWidthProperty = AvaloniaProperty.RegisterDirect<ProgressBarTemplateSettings, double>( nameof(ContainerWidth), p => p.ContainerWidth,`
- `public static readonly DirectProperty<ProgressBarTemplateSettings, double> IndeterminateStartingOffsetProperty = AvaloniaProperty.RegisterDirect<ProgressBarTemplateSettings, double>( nameof(IndeterminateStartingOffset), p => p.IndeterminateStartingOffset,`
- `public static readonly DirectProperty<ProgressBarTemplateSettings, double> IndeterminateEndingOffsetProperty = AvaloniaProperty.RegisterDirect<ProgressBarTemplateSettings, double>( nameof(IndeterminateEndingOffset), p => p.IndeterminateEndingOffset,`
- `public double ContainerWidth {`
- `public double Container2Width {`
- `public double ContainerAnimationStartPosition {`
- `public double ContainerAnimationEndPosition {`
- `public double Container2AnimationStartPosition {`
- `public double Container2AnimationEndPosition {`
- `public double IndeterminateStartingOffset {`
- `public double IndeterminateEndingOffset {`
- `public static readonly StyledProperty<bool> ShowProgressTextProperty = AvaloniaProperty.Register<ProgressBar, bool>(nameof(ShowProgressText));`
- `public static readonly StyledProperty<string> ProgressTextFormatProperty = AvaloniaProperty.Register<ProgressBar, string>(nameof(ProgressTextFormat), "{1:0}%");`
- `public static readonly DirectProperty<ProgressBar, double> PercentageProperty = AvaloniaProperty.RegisterDirect<ProgressBar, double>( nameof(Percentage), o => o.Percentage);`
- `public double Percentage {`
- `public bool ShowProgressText {`
- `public string ProgressTextFormat {`

### `src/Avalonia.Controls/PullToRefresh/RefreshCompletionDeferral.cs`
- `public RefreshCompletionDeferral(Action deferredAction) {`
- `public RefreshCompletionDeferral Get() {`

### `src/Avalonia.Controls/PullToRefresh/RefreshRequestedEventArgs.cs`
- `public RefreshRequestedEventArgs(Action deferredAction, RoutedEvent? routedEvent) : base(routedEvent) {`
- `public RefreshRequestedEventArgs(RefreshCompletionDeferral completionDeferral, RoutedEvent? routedEvent) : base(routedEvent) {`

### `src/Avalonia.Controls/RelativePanel.AttachedProperties.cs`
- `public static void SetAlignLeftWithPanel(AvaloniaObject obj, bool value) {`
- `public static readonly AttachedProperty<bool> AlignLeftWithPanelProperty = AvaloniaProperty.RegisterAttached<Layoutable, bool>("AlignLeftWithPanel", typeof(RelativePanel), false);`
- `public static object GetAlignLeftWith(AvaloniaObject obj) {`
- `public static void SetAlignLeftWith(AvaloniaObject obj, object value) {`
- `public static readonly AttachedProperty<object> AlignLeftWithProperty = AvaloniaProperty.RegisterAttached<RelativePanel, Layoutable, object>("AlignLeftWith");`
- `public static bool GetAlignRightWithPanel(AvaloniaObject obj) {`
- `public static void SetAlignRightWithPanel(AvaloniaObject obj, bool value) {`
- `public static readonly AttachedProperty<bool> AlignRightWithPanelProperty = AvaloniaProperty.RegisterAttached<RelativePanel, Layoutable, bool>("AlignRightWithPanel", false);`
- `public static object GetAlignRightWith(AvaloniaObject obj) {`
- `public static void SetAlignRightWith(AvaloniaObject obj, object value) {`
- `public static readonly AttachedProperty<object> AlignRightWithProperty = AvaloniaProperty.RegisterAttached<RelativePanel, Layoutable, object>("AlignRightWith");`
- `public static bool GetAlignTopWithPanel(AvaloniaObject obj) {`
- `public static void SetAlignTopWithPanel(AvaloniaObject obj, bool value) {`
- `public static readonly AttachedProperty<bool> AlignTopWithPanelProperty = AvaloniaProperty.RegisterAttached<RelativePanel, Layoutable, bool>("AlignTopWithPanel", false);`
- `public static object GetAlignTopWith(AvaloniaObject obj) {`
- `public static void SetAlignTopWith(AvaloniaObject obj, object value) {`
- `public static readonly AttachedProperty<object> AlignTopWithProperty = AvaloniaProperty.RegisterAttached<RelativePanel, Layoutable, object>("AlignTopWith");`
- `public static bool GetAlignVerticalCenterWithPanel(AvaloniaObject obj) {`
- `public static void SetAlignVerticalCenterWithPanel(AvaloniaObject obj, bool value) {`
- `public static readonly AttachedProperty<bool> AlignVerticalCenterWithPanelProperty = AvaloniaProperty.RegisterAttached<RelativePanel, Layoutable, bool>("AlignVerticalCenterWithPanel", false);`
- `public static object GetAlignVerticalCenterWith(AvaloniaObject obj) {`
- `public static void SetAlignVerticalCenterWith(AvaloniaObject obj, object value) {`
- `public static readonly AttachedProperty<object> AlignVerticalCenterWithProperty = AvaloniaProperty.RegisterAttached<RelativePanel, Layoutable, object>("AlignVerticalCenterWith");`
- `public static object GetBelow(AvaloniaObject obj) {`
- `public static void SetBelow(AvaloniaObject obj, object value) {`
- `public static readonly AttachedProperty<object> BelowProperty = AvaloniaProperty.RegisterAttached<RelativePanel, Layoutable, object>("Below");`
- `public static object GetLeftOf(AvaloniaObject obj) {`
- `public static void SetLeftOf(AvaloniaObject obj, object value) {`
- `public static readonly AttachedProperty<object> LeftOfProperty = AvaloniaProperty.RegisterAttached<RelativePanel, Layoutable, object>("LeftOf");`
- `public static object GetRightOf(AvaloniaObject obj) {`
- `public static void SetRightOf(AvaloniaObject obj, object value) {`
- `public static readonly AttachedProperty<object> RightOfProperty = AvaloniaProperty.RegisterAttached<RelativePanel, Layoutable, object>("RightOf");`

### `src/Avalonia.Controls/Remote/RemoteServer.cs`
- `public class RemoteServer : IDisposable`
- `public RemoteServer(IAvaloniaRemoteTransportConnection transport) {`

### `src/Avalonia.Controls/Remote/RemoteWidget.cs`
- `public enum SizingMode`

### `src/Avalonia.Controls/RequestBringIntoViewEventArgs.cs`
- `public Rect TargetRect { get; set; }`

### `src/Avalonia.Controls/ResolveByNameAttribute.cs`
- `public sealed class ResolveByNameAttribute : Attribute`

### `src/Avalonia.Controls/RowDefinition.cs`
- `public static readonly StyledProperty<double> MaxHeightProperty = AvaloniaProperty.Register<RowDefinition, double>(nameof(MaxHeight), double.PositiveInfinity);`
- `public static readonly StyledProperty<double> MinHeightProperty = AvaloniaProperty.Register<RowDefinition, double>(nameof(MinHeight));`
- `public static readonly StyledProperty<GridLength> HeightProperty = AvaloniaProperty.Register<RowDefinition, GridLength>(nameof(Height), new GridLength(1, GridUnitType.Star));`
- `public RowDefinition() {`
- `public RowDefinition(double value, GridUnitType type) : this(new GridLength(value, type)) {`
- `public RowDefinition(GridLength height) {`

### `src/Avalonia.Controls/Screens.cs`
- `public Screen? ScreenFromWindow(WindowBase window) {`
- `public Screen? ScreenFromWindow(IWindowBaseImpl window) {`

### `src/Avalonia.Controls/ScrollViewer.cs`
- `public static readonly AttachedProperty<bool> IsScrollInertiaEnabledProperty = AvaloniaProperty.RegisterAttached<ScrollViewer, Control, bool>( nameof(IsScrollInertiaEnabled), defaultValue: true);`
- `public static readonly AttachedProperty<bool> IsDeferredScrollingEnabledProperty = AvaloniaProperty.RegisterAttached<ScrollViewer, Control, bool>( nameof(IsDeferredScrollingEnabled));`
- `public static readonly RoutedEvent<ScrollChangedEventArgs> ScrollChangedEvent = RoutedEvent.Register<ScrollViewer, ScrollChangedEventArgs>( nameof(ScrollChanged), RoutingStrategies.Bubble);`
- `public static bool GetBringIntoViewOnFocusChange(Control control) {`
- `public static void SetBringIntoViewOnFocusChange(Control control, bool value) {`
- `public static ScrollBarVisibility GetHorizontalScrollBarVisibility(Control control) {`
- `public static void SetHorizontalScrollBarVisibility(Control control, ScrollBarVisibility value) {`
- `public static SnapPointsType GetHorizontalSnapPointsType(Control control) {`
- `public static void SetHorizontalSnapPointsType(Control control, SnapPointsType value) {`
- `public static SnapPointsType GetVerticalSnapPointsType(Control control) {`
- `public static void SetVerticalSnapPointsType(Control control, SnapPointsType value) {`
- `public static SnapPointsAlignment GetHorizontalSnapPointsAlignment(Control control) {`
- `public static void SetHorizontalSnapPointsAlignment(Control control, SnapPointsAlignment value) {`
- `public static SnapPointsAlignment GetVerticalSnapPointsAlignment(Control control) {`
- `public static void SetVerticalSnapPointsAlignment(Control control, SnapPointsAlignment value) {`
- `public static ScrollBarVisibility GetVerticalScrollBarVisibility(Control control) {`
- `public static void SetAllowAutoHide(Control control, bool value) {`
- `public static bool GetAllowAutoHide(Control control) {`
- `public static void SetIsScrollChainingEnabled(Control control, bool value) {`
- `public static bool GetIsScrollChainingEnabled(Control control) {`
- `public static void SetVerticalScrollBarVisibility(Control control, ScrollBarVisibility value) {`
- `public static bool GetIsScrollInertiaEnabled(Control control) {`
- `public static void SetIsScrollInertiaEnabled(Control control, bool value) {`
- `public static bool GetIsDeferredScrollingEnabled(Control control) => control.GetValue(IsDeferredScrollingEnabledProperty);`
- `public static void SetIsDeferredScrollingEnabled(Control control, bool value) => control.SetValue(IsDeferredScrollingEnabledProperty, value);`

### `src/Avalonia.Controls/Selection/ISelectionModel.cs`
- `public event EventHandler<SelectionModelIndexesChangedEventArgs>? IndexesChanged;`
- `public event EventHandler? LostSelection;`
- `public event EventHandler? SourceReset;`
- `public void BeginBatchUpdate();`
- `public void EndBatchUpdate();`
- `public static class SelectionModelExtensions`
- `public static IDisposable BatchUpdate(this ISelectionModel model) {`
- `public record struct BatchUpdateOperation : IDisposable`
- `public BatchUpdateOperation(ISelectionModel owner) {`

### `src/Avalonia.Controls/Selection/SelectionModel.cs`
- `public SelectionModel() {`
- `public SelectionModel(IEnumerable<T>? source) {`
- `public bool SingleSelect {`
- `public IReadOnlyList<int> SelectedIndexes => _selectedIndexes ??= new SelectedIndexes<T>(this);`
- `public int AnchorIndex {`
- `public event EventHandler<SelectionModelIndexesChangedEventArgs>? IndexesChanged;`
- `public event EventHandler? LostSelection;`
- `public event EventHandler? SourceReset;`
- `public BatchUpdateOperation BatchUpdate() => new BatchUpdateOperation(this);`
- `public void BeginBatchUpdate() {`
- `public void EndBatchUpdate() {`
- `public bool IsSelected(int index) {`
- `public void SelectRange(int start, int end) => SelectRange(start, end, false, false);`
- `public void DeselectRange(int start, int end) {`
- `public record struct BatchUpdateOperation : IDisposable`
- `public BatchUpdateOperation(SelectionModel<T> owner) {`

### `src/Avalonia.Controls/Selection/SelectionModelIndexesChangedEventArgs.cs`
- `public class SelectionModelIndexesChangedEventArgs : EventArgs`
- `public SelectionModelIndexesChangedEventArgs(int startIndex, int delta) {`
- `public int StartIndex { get; }`

### `src/Avalonia.Controls/Selection/SelectionModelSelectionChangedEventArgs.cs`
- `public abstract class SelectionModelSelectionChangedEventArgs : EventArgs`
- `public abstract IReadOnlyList<int> DeselectedIndexes { get; }`
- `public abstract IReadOnlyList<int> SelectedIndexes { get; }`
- `public IReadOnlyList<object?> DeselectedItems => GetUntypedDeselectedItems();`
- `public class SelectionModelSelectionChangedEventArgs<T> : SelectionModelSelectionChangedEventArgs`
- `public SelectionModelSelectionChangedEventArgs( IReadOnlyList<int>? deselectedIndices = null, IReadOnlyList<int>? selectedIndices = null, IReadOnlyList<T?>? deselectedItems = null, IReadOnlyList<T?>? selectedItems = null) {`
- `public override IReadOnlyList<int> DeselectedIndexes { get; }`
- `public override IReadOnlyList<int> SelectedIndexes { get; }`
- `public new IReadOnlyList<T?> DeselectedItems { get; }`

### `src/Avalonia.Controls/Selection/SelectionNodeBase.cs`
- `public abstract class SelectionNodeBase<T>`

### `src/Avalonia.Controls/SelectionChangedEventArgs.cs`
- `public SelectionChangedEventArgs(RoutedEvent routedEvent, IList removedItems, IList addedItems) : base(routedEvent) {`
- `public IList AddedItems { get; }`
- `public IList RemovedItems { get; }`

### `src/Avalonia.Controls/SizeChangedEventArgs.cs`
- `public SizeChangedEventArgs(RoutedEvent? routedEvent) : base (routedEvent) {`
- `public SizeChangedEventArgs(RoutedEvent? routedEvent, object? source) : base(routedEvent, source) {`
- `public SizeChangedEventArgs( RoutedEvent? routedEvent, object? source, Size previousSize, Size newSize) : base(routedEvent, source) {`
- `public bool HeightChanged => !MathUtilities.AreClose(NewSize.Height, PreviousSize.Height, LayoutHelper.LayoutEpsilon);`
- `public Size NewSize { get; init; }`
- `public Size PreviousSize { get; init; }`
- `public bool WidthChanged => !MathUtilities.AreClose(NewSize.Width, PreviousSize.Width, LayoutHelper.LayoutEpsilon);`

### `src/Avalonia.Controls/Slider.cs`
- `public AvaloniaList<double>? Ticks {`

### `src/Avalonia.Controls/Spinner.cs`
- `public enum SpinDirection`
- `public bool UsingMouseWheel{ get; }`
- `public SpinEventArgs(SpinDirection direction) {`
- `public SpinEventArgs(RoutedEvent routedEvent, SpinDirection direction) : base(routedEvent) {`
- `public SpinEventArgs(SpinDirection direction, bool usingMouseWheel) {`
- `public SpinEventArgs(RoutedEvent routedEvent, SpinDirection direction, bool usingMouseWheel) : base(routedEvent) {`
- `public event EventHandler<SpinEventArgs>? Spin {`

### `src/Avalonia.Controls/SplitView/SplitViewTemplateSettings.cs`
- `public static readonly StyledProperty<double> ClosedPaneWidthProperty = AvaloniaProperty.Register<SplitViewTemplateSettings, double>(nameof(ClosedPaneWidth), 0d);`
- `public static readonly StyledProperty<GridLength> PaneColumnGridLengthProperty = AvaloniaProperty.Register<SplitViewTemplateSettings, GridLength>( nameof(PaneColumnGridLength));`
- `public static readonly StyledProperty<double> ClosedPaneHeightProperty = AvaloniaProperty.Register<SplitViewTemplateSettings, double>(nameof(ClosedPaneHeight), 0d);`
- `public static readonly StyledProperty<GridLength> PaneRowGridLengthProperty = AvaloniaProperty.Register<SplitViewTemplateSettings, GridLength>( nameof(PaneRowGridLength));`
- `public double ClosedPaneWidth {`
- `public GridLength PaneColumnGridLength {`
- `public double ClosedPaneHeight {`
- `public GridLength PaneRowGridLength {`

### `src/Avalonia.Controls/SystemDialog.cs`
- `public abstract class FileDialog : FileSystemDialog`
- `public List<FileDialogFilter> Filters { get; set; } = new List<FileDialogFilter>();`
- `public string? InitialFileName { get; set; }`
- `public abstract class FileSystemDialog : SystemDialog`
- `public string? Directory { get; set; }`
- `public FilePickerSaveOptions ToFilePickerSaveOptions() {`
- `public FilePickerOpenOptions ToFilePickerOpenOptions() {`
- `public FolderPickerOpenOptions ToFolderPickerOpenOptions() {`
- `public abstract class SystemDialog`
- `public class FileDialogFilter`

### `src/Avalonia.Controls/SystemFontAppBuilderExtension.cs`
- `public static class SystemFontAppBuilderExtension`
- `public static AppBuilder WithSystemFontSource(this AppBuilder appBuilder, Uri fontSource) {`

### `src/Avalonia.Controls/TextBlock.cs`
- `public static readonly StyledProperty<TextDecorationCollection?> TextDecorationsProperty = Inline.TextDecorationsProperty.AddOwner<TextBlock>();`
- `public static readonly DirectProperty<TextBlock, InlineCollection?> InlinesProperty = AvaloniaProperty.RegisterDirect<TextBlock, InlineCollection?>( nameof(Inlines), t => t.Inlines, (t, v) => t.Inlines = v);`
- `public FontFeatureCollection? FontFeatures {`
- `public static double GetBaselineOffset(Control control) {`
- `public static void SetBaselineOffset(Control control, double value) {`
- `public static TextAlignment GetTextAlignment(Control control) {`
- `public static void SetTextAlignment(Control control, TextAlignment alignment) {`
- `public static TextWrapping GetTextWrapping(Control control) {`
- `public static void SetTextWrapping(Control control, TextWrapping wrapping) {`
- `public static TextTrimming GetTextTrimming(Control control) {`
- `public static void SetTextTrimming(Control control, TextTrimming trimming) {`
- `public static double GetLineHeight(Control control) {`
- `public static void SetLineHeight(Control control, double height) {`
- `public static double GetLetterSpacing(Control control) {`
- `public static void SetLetterSpacing(Control control, double letterSpacing) {`
- `public static int GetMaxLines(Control control) {`
- `public static void SetMaxLines(Control control, int maxLines) {`

### `src/Avalonia.Controls/TextBox.cs`
- `public static readonly StyledProperty<int> MaxLengthProperty = AvaloniaProperty.Register<TextBox, int>(nameof(MaxLength));`
- `public static readonly StyledProperty<int> MinLinesProperty = AvaloniaProperty.Register<TextBox, int>(nameof(MinLines));`
- `public static readonly StyledProperty<string> NewLineProperty = AvaloniaProperty.Register<TextBox, string>(nameof(NewLine), Environment.NewLine);`
- `public static readonly StyledProperty<object?> InnerLeftContentProperty = AvaloniaProperty.Register<TextBox, object?>(nameof(InnerLeftContent));`
- `public static readonly StyledProperty<object?> InnerRightContentProperty = AvaloniaProperty.Register<TextBox, object?>(nameof(InnerRightContent));`
- `public static readonly DirectProperty<TextBox, bool> CanCutProperty = AvaloniaProperty.RegisterDirect<TextBox, bool>( nameof(CanCut), o => o.CanCut);`
- `public static readonly DirectProperty<TextBox, bool> CanPasteProperty = AvaloniaProperty.RegisterDirect<TextBox, bool>( nameof(CanPaste), o => o.CanPaste);`
- `public static readonly StyledProperty<bool> IsUndoEnabledProperty = AvaloniaProperty.Register<TextBox, bool>( nameof(IsUndoEnabled), defaultValue: true);`
- `public static readonly StyledProperty<int> UndoLimitProperty = AvaloniaProperty.Register<TextBox, int>(nameof(UndoLimit), UndoRedoHelper<UndoRedoState>.DefaultUndoLimit);`
- `public static readonly DirectProperty<TextBox, bool> CanUndoProperty = AvaloniaProperty.RegisterDirect<TextBox, bool>(nameof(CanUndo), x => x.CanUndo);`
- `public static readonly DirectProperty<TextBox, bool> CanRedoProperty = AvaloniaProperty.RegisterDirect<TextBox, bool>(nameof(CanRedo), x => x.CanRedo);`
- `public static readonly RoutedEvent<RoutedEventArgs> CuttingToClipboardEvent = RoutedEvent.Register<TextBox, RoutedEventArgs>( nameof(CuttingToClipboard), RoutingStrategies.Bubble);`
- `public static readonly RoutedEvent<RoutedEventArgs> PastingFromClipboardEvent = RoutedEvent.Register<TextBox, RoutedEventArgs>( nameof(PastingFromClipboard), RoutingStrategies.Bubble);`
- `public static readonly RoutedEvent<TextChangedEventArgs> TextChangedEvent = RoutedEvent.Register<TextBox, TextChangedEventArgs>( nameof(TextChanged), RoutingStrategies.Bubble);`
- `public static readonly RoutedEvent<TextChangingEventArgs> TextChangingEvent = RoutedEvent.Register<TextBox, TextChangingEventArgs>( nameof(TextChanging), RoutingStrategies.Bubble);`
- `public bool UseFloatingWatermark {`
- `public object? InnerLeftContent {`
- `public object? InnerRightContent {`
- `public string NewLine {`
- `public int GetLineCount() {`

### `src/Avalonia.Controls/TextChangedEventArgs.cs`
- `public class TextChangedEventArgs : RoutedEventArgs`
- `public TextChangedEventArgs(RoutedEvent? routedEvent) : base (routedEvent) {`
- `public TextChangedEventArgs(RoutedEvent? routedEvent, Interactive? source) : base(routedEvent, source) {`

### `src/Avalonia.Controls/TextChangingEventArgs.cs`
- `public class TextChangingEventArgs : RoutedEventArgs`
- `public TextChangingEventArgs(RoutedEvent? routedEvent) : base (routedEvent) {`
- `public TextChangingEventArgs(RoutedEvent? routedEvent, Interactive? source) : base(routedEvent, source) {`

### `src/Avalonia.Controls/TickBar.cs`
- `public AvaloniaList<double>? Ticks {`
- `public static readonly StyledProperty<Rect> ReservedSpaceProperty = AvaloniaProperty.Register<TickBar, Rect>(nameof(ReservedSpace));`
- `public Rect ReservedSpace {`

### `src/Avalonia.Controls/ToolTip.cs`
- `public static PlacementMode GetPlacement(Control element) {`
- `public static void SetPlacement(Control element, PlacementMode value) {`
- `public static double GetHorizontalOffset(Control element) {`
- `public static void SetHorizontalOffset(Control element, double value) {`
- `public static double GetVerticalOffset(Control element) {`
- `public static void SetVerticalOffset(Control element, double value) {`
- `public static int GetShowDelay(Control element) {`
- `public static int GetBetweenShowDelay(Control element) => element.GetValue(BetweenShowDelayProperty);`
- `public static void SetBetweenShowDelay(Control element, int value) => element.SetValue(BetweenShowDelayProperty, value);`
- `public static bool GetShowOnDisabled(Control element) =>`
- `public static void SetShowOnDisabled(Control element, bool value) =>`
- `public static bool GetServiceEnabled(Control element) =>`
- `public static void SetServiceEnabled(Control element, bool value) =>`
- `public static void AddToolTipOpeningHandler(Control element, EventHandler<CancelRoutedEventArgs> handler) =>`
- `public static void RemoveToolTipOpeningHandler(Control element, EventHandler<CancelRoutedEventArgs> handler) =>`
- `public static void AddToolTipClosingHandler(Control element, EventHandler<RoutedEventArgs> handler) =>`
- `public static void RemoveToolTipClosingHandler(Control element, EventHandler<RoutedEventArgs> handler) =>`
- `public static CustomPopupPlacementCallback? GetCustomPopupPlacementCallback(Control element) {`
- `public static void SetCustomPopupPlacementCallback(Control element, CustomPopupPlacementCallback? value) {`

### `src/Avalonia.Controls/TransitionCompletedEventArgs.cs`
- `public TransitionCompletedEventArgs(object? from, object? to, bool hasRunToCompletion) : base(TransitioningContentControl.TransitionCompletedEvent) {`
- `public object? From { get; }`
- `public object? To { get; }`
- `public bool HasRunToCompletion { get; }`

### `src/Avalonia.Controls/TreeView.cs`
- `public object? TreeItemFromContainer(Control container) {`

### `src/Avalonia.Controls/TreeViewItem.cs`
- `public int Level {`

### `src/Avalonia.Controls/UrlOpenedEventArgs.cs`
- `public class UrlOpenedEventArgs : EventArgs`
- `public UrlOpenedEventArgs(string[] urls) {`
- `public string[] Urls { get; }`

### `src/Avalonia.Controls/Utils/AncestorFinder.cs`
- `public static class AncestorFinder`

### `src/Avalonia.Controls/Utils/ISelectionAdapter.cs`
- `public interface ISelectionAdapter`

### `src/Avalonia.Controls/Utils/SelectingItemsControlSelectionAdapter.cs`
- `public class SelectingItemsControlSelectionAdapter : ISelectionAdapter`
- `public SelectingItemsControl? SelectorControl {`
- `public event EventHandler<RoutedEventArgs>? Commit;`
- `public SelectingItemsControlSelectionAdapter() {`
- `public SelectingItemsControlSelectionAdapter(SelectingItemsControl selector) {`
- `public void HandleKeyDown(KeyEventArgs e) {`

### `src/Avalonia.DesignerSupport/DesignWindowLoader.cs`
- `public class DesignWindowLoader`
- `public static Window LoadDesignerWindow(string xaml, string assemblyPath, string xamlFileProjectPath) => LoadDesignerWindow(xaml, assemblyPath, xamlFileProjectPath, 1.0);`
- `public static Window LoadDesignerWindow(string xaml, string assemblyPath, string xamlFileProjectPath, double renderScaling) {`

### `src/Avalonia.DesignerSupport/Remote/HtmlTransport/HtmlTransport.cs`
- `public class HtmlWebSocketTransport : IAvaloniaRemoteTransportConnection`
- `public HtmlWebSocketTransport(IAvaloniaRemoteTransportConnection signalTransport, Uri listenUri) {`

### `src/Avalonia.DesignerSupport/Remote/HtmlTransport/SimpleWebSocketHttpServer.cs`
- `public class SimpleWebSocketHttpServer : IDisposable`
- `public async Task<SimpleWebSocketHttpRequest> AcceptAsync() {`
- `public void Listen() {`
- `public SimpleWebSocketHttpServer(IPAddress address, int port) {`
- `public class SimpleWebSocketHttpRequest : IDisposable`
- `public Dictionary<string, string> Headers { get; }`
- `public bool IsWebsocketRequest { get; }`
- `public IReadOnlyList<string> WebSocketProtocols { get; }`
- `public SimpleWebSocketHttpRequest(NetworkStream stream, string path, Dictionary<string, string> headers) {`
- `public async Task RespondAsync(int code, byte[] data, string contentType) {`
- `public async Task<SimpleWebSocket> AcceptWebSocket(string protocol = null) {`
- `public class SimpleWebSocket : IDisposable`
- `public Task SendMessage(string text) {`
- `public Task SendMessage(bool isText, byte[] data) => SendMessage(isText, data, 0, data.Length);`
- `public Task SendMessage(bool isText, byte[] data, int offset, int length) => SendFrame(isText ? FrameType.Text : FrameType.Binary, data, offset, length);`
- `public async Task<SimpleWebSocketMessage> ReceiveMessage() {`
- `public class SimpleWebSocketMessage`
- `public bool IsText { get; set; }`
- `public string AsString() {`

### `src/Avalonia.DesignerSupport/Remote/RemoteDesignerEntryPoint.cs`
- `public class RemoteDesignerEntryPoint`

### `src/Avalonia.Diagnostics/DevToolsExtensions.cs`
- `public static class DevToolsExtensions`

### `src/Avalonia.Diagnostics/Diagnostics/DevToolsDataFormats.cs`
- `public static class DevToolsDataFormats`

### `src/Avalonia.Diagnostics/Diagnostics/DevToolsOptions.cs`
- `public class DevToolsOptions`
- `public bool ShowAsChildWindow { get; set; } = true;`
- `public int? StartupScreenIndex { get; set; }`
- `public bool ShowImplementedInterfaces { get; set; } = true;`
- `public IScreenshotHandler ScreenshotHandler { get; set; }`
- `public IBrush? FocusHighlighterBrush { get; set; }`
- `public DevToolsViewKind LaunchView { get; init; }`
- `public HotKeyConfiguration HotKeys { get; init; } = new();`

### `src/Avalonia.Diagnostics/Diagnostics/DevToolsViewKind.cs`
- `public enum DevToolsViewKind`

### `src/Avalonia.Diagnostics/Diagnostics/HotKeyConfiguration.cs`
- `public class HotKeyConfiguration`
- `public KeyGesture ValueFramesFreeze { get; init; } = new(Key.S, KeyModifiers.Alt);`
- `public KeyGesture ValueFramesUnfreeze { get; init; } = new(Key.D, KeyModifiers.Alt);`
- `public KeyGesture InspectHoveredControl { get; init; } = new(Key.None, KeyModifiers.Shift | KeyModifiers.Control);`
- `public KeyGesture TogglePopupFreeze { get; init; } = new(Key.F, KeyModifiers.Alt | KeyModifiers.Control);`
- `public KeyGesture ScreenshotSelectedControl { get; init; } = new(Key.F8);`

### `src/Avalonia.Diagnostics/Diagnostics/IScreenshotHandler.cs`
- `public interface IScreenshotHandler`

### `src/Avalonia.Diagnostics/Diagnostics/Screenshots/BaseRenderToStreamHandler.cs`
- `public abstract class BaseRenderToStreamHandler : IScreenshotHandler`
- `public async Task Take(Control control) {`

### `src/Avalonia.Diagnostics/Diagnostics/Screenshots/FilePickerHandler.cs`
- `public sealed class FilePickerHandler : BaseRenderToStreamHandler`
- `public FilePickerHandler() : this(null, null) {`
- `public FilePickerHandler( string? title, string? screenshotRoot = default) {`

### `src/Avalonia.Diagnostics/Diagnostics/VisualTreeDebug.cs`
- `public static class VisualTreeDebug`
- `public static string PrintVisualTree(Visual visual) {`

### `src/Avalonia.Dialogs/AboutAvaloniaDialog.xaml.cs`
- `public class AboutAvaloniaDialog : Window`
- `public static bool IsDevelopmentBuild { get; } = s_version.Revision == 999;`
- `public static string Copyright { get; } = $"© {DateTime.Now.Year} The Avalonia Project";`
- `public AboutAvaloniaDialog() {`

### `src/Avalonia.Dialogs/Internal/AvaloniaDialogsInternalViewModelBase.cs`
- `public class AvaloniaDialogsInternalViewModelBase : INotifyPropertyChanged`

### `src/Avalonia.Dialogs/Internal/ChildFitter.cs`
- `public class ChildFitter : Decorator`

### `src/Avalonia.Dialogs/Internal/FileSizeStringConverter.cs`
- `public class FileSizeStringConverter : IValueConverter`

### `src/Avalonia.Dialogs/Internal/ManagedFileChooserFilterViewModel.cs`
- `public class ManagedFileChooserFilterViewModel : AvaloniaDialogsInternalViewModelBase`
- `public ManagedFileChooserFilterViewModel(FilePickerFileType filter) : this(filter, 0) {`
- `public ManagedFileChooserFilterViewModel(FilePickerFileType filter, int index) {`

### `src/Avalonia.Dialogs/Internal/ManagedFileChooserItemType.cs`
- `public enum ManagedFileChooserItemType`

### `src/Avalonia.Dialogs/Internal/ManagedFileChooserItemViewModel.cs`
- `public class ManagedFileChooserItemViewModel : AvaloniaDialogsInternalViewModelBase`
- `public string IconKey {`
- `public ManagedFileChooserItemViewModel() {`
- `public ManagedFileChooserItemViewModel(ManagedFileChooserNavigationItem item) {`

### `src/Avalonia.Dialogs/Internal/ManagedFileChooserNavigationItem.cs`
- `public class ManagedFileChooserNavigationItem`

### `src/Avalonia.Dialogs/Internal/ManagedFileChooserViewModel.cs`
- `public class ManagedFileChooserViewModel : AvaloniaDialogsInternalViewModelBase`
- `public event Action? CancelRequested;`
- `public event Action<string[]>? CompleteRequested;`
- `public event Action<string>? OverwritePrompt;`
- `public AvaloniaList<ManagedFileChooserItemViewModel> QuickLinks { get; } =`
- `public AvaloniaList<ManagedFileChooserFilterViewModel> Filters { get; } =`
- `public bool SelectingFolder => _selectingDirectory;`
- `public bool ShowFilters { get; }`
- `public int QuickLinksSelectedIndex {`
- `public ManagedFileChooserFilterViewModel? SelectedFilter {`
- `public bool ShowHiddenFiles {`
- `public ManagedFileChooserViewModel(ManagedFileDialogOptions options) {`
- `public ManagedFileChooserViewModel(FilePickerOpenOptions filePickerOpen, ManagedFileDialogOptions options) : this(options) {`
- `public ManagedFileChooserViewModel(FilePickerSaveOptions filePickerSave, ManagedFileDialogOptions options) : this(options) {`
- `public ManagedFileChooserViewModel(FolderPickerOpenOptions folderPickerOpen, ManagedFileDialogOptions options) : this(options) {`
- `public void EnterPressed() {`
- `public void GoUp() {`
- `public bool CanOk(object _) =>`
- `public void Ok() {`
- `public void SelectSingleFile(ManagedFileChooserItemViewModel item) {`

### `src/Avalonia.Dialogs/Internal/ResourceSelectorConverter.cs`
- `public class ResourceSelectorConverter : ResourceDictionary, IValueConverter`

### `src/Avalonia.Dialogs/ManagedFileChooser.cs`
- `public class ManagedFileChooser : TemplatedControl`
- `public ManagedFileChooser() {`

### `src/Avalonia.Dialogs/ManagedFileChooserOverwritePrompt.cs`
- `public class ManagedFileChooserOverwritePrompt : TemplatedControl`
- `public static readonly DirectProperty<ManagedFileChooserOverwritePrompt, string> FileNameProperty = AvaloniaProperty.RegisterDirect<ManagedFileChooserOverwritePrompt, string>( "FileName", o => o.FileName, (o, v) => o.FileName = v);`

### `src/Avalonia.Dialogs/ManagedFileDialogOptions.cs`
- `public bool AllowDirectorySelection { get; set; }`
- `public IMountedVolumeInfoProvider? CustomVolumeInfoProvider { get; set; }`
- `public Func<ContentControl>? ContentRootFactory { get; set; }`

### `src/Avalonia.Fonts.Inter/InterFontCollection.cs`
- `public sealed class InterFontCollection : EmbeddedFontCollection`
- `public InterFontCollection() : base( new Uri("fonts:Inter", UriKind.Absolute), new Uri("avares: {`

### `src/Avalonia.Metal/IMetalDevice.cs`
- `public interface IMetalDevice : IPlatformGraphicsContext`
- `public interface IMetalPlatformSurface`
- `public interface IMetalPlatformSurfaceRenderTarget : IDisposable`
- `public interface IMetalPlatformSurfaceRenderingSession : IDisposable`

### `src/Avalonia.Metal/IMetalExternalObjectsFeature.cs`
- `public interface IMetalExternalObjectsFeature`
- `public interface IMetalExternalTexture : IDisposable`
- `public interface IMetalSharedEvent : IDisposable`

### `src/Avalonia.MicroCom/CallbackBase.cs`
- `public abstract class CallbackBase : IUnknown, IMicroComShadowContainer`
- `public bool IsDestroyed => _destroyed;`
- `public MicroComShadow? Shadow { get; set; }`
- `public void OnReferencedFromNative() {`
- `public void OnUnreferencedFromNative() {`

### `src/Avalonia.OpenGL/Controls/OpenGlControlBase.cs`
- `public abstract class OpenGlControlBase : Control`
- `public OpenGlControlBase() {`
- `public void RequestNextFrameRendering() {`

### `src/Avalonia.OpenGL/Egl/EglConsts.cs`
- `public static class EglConsts`
- `public const int EGL_ALPHA_SIZE = 0x3021;`
- `public const int EGL_BAD_ACCESS = 0x3002;`
- `public const int EGL_BAD_ALLOC = 0x3003;`
- `public const int EGL_BAD_ATTRIBUTE = 0x3004;`
- `public const int EGL_BAD_CONFIG = 0x3005;`
- `public const int EGL_BAD_CONTEXT = 0x3006;`
- `public const int EGL_BAD_CURRENT_SURFACE = 0x3007;`
- `public const int EGL_BAD_DISPLAY = 0x3008;`
- `public const int EGL_BAD_MATCH = 0x3009;`
- `public const int EGL_BAD_NATIVE_PIXMAP = 0x300A;`
- `public const int EGL_BAD_NATIVE_WINDOW = 0x300B;`
- `public const int EGL_BAD_PARAMETER = 0x300C;`
- `public const int EGL_BAD_SURFACE = 0x300D;`
- `public const int EGL_BLUE_SIZE = 0x3022;`
- `public const int EGL_CORE_NATIVE_ENGINE = 0x305B;`
- `public const int EGL_DEPTH_SIZE = 0x3025;`
- `public const int EGL_DRAW = 0x3059;`
- `public const int EGL_EXTENSIONS = 0x3055;`
- `public const int EGL_FALSE = 0;`
- `public const int EGL_GREEN_SIZE = 0x3023;`
- `public const int EGL_HEIGHT = 0x3056;`
- `public const int EGL_NONE = 0x3038;`
- `public const int EGL_NOT_INITIALIZED = 0x3001;`
- `public const int EGL_NO_CONTEXT = 0;`
- `public const int EGL_NO_DISPLAY = 0;`
- `public const int EGL_NO_SURFACE = 0;`
- `public const int EGL_PBUFFER_BIT = 0x0001;`
- `public const int EGL_READ = 0x305A;`
- `public const int EGL_RED_SIZE = 0x3024;`
- `public const int EGL_SAMPLES = 0x3031;`
- `public const int EGL_STENCIL_SIZE = 0x3026;`
- `public const int EGL_SUCCESS = 0x3000;`
- `public const int EGL_SURFACE_TYPE = 0x3033;`
- `public const int EGL_TRUE = 1;`
- `public const int EGL_WIDTH = 0x3057;`
- `public const int EGL_WINDOW_BIT = 0x0004;`
- `public const int EGL_BACK_BUFFER = 0x3084;`
- `public const int EGL_CONTEXT_LOST = 0x300E;`
- `public const int EGL_TEXTURE_2D = 0x305F;`
- `public const int EGL_TEXTURE_FORMAT = 0x3080;`
- `public const int EGL_TEXTURE_RGBA = 0x305E;`
- `public const int EGL_TEXTURE_TARGET = 0x3081;`
- `public const int EGL_OPENGL_ES_BIT = 0x0001;`
- `public const int EGL_OPENGL_ES_API = 0x30A0;`
- `public const int EGL_RENDERABLE_TYPE = 0x3040;`
- `public const int EGL_OPENGL_ES2_BIT = 0x0004;`
- `public const int EGL_CONTEXT_MAJOR_VERSION = 0x3098;`
- `public const int EGL_CONTEXT_MINOR_VERSION = 0x30FB;`
- `public const int EGL_OPENGL_ES3_BIT = 0x00000040;`
- `public const int EGL_PLATFORM_ANGLE_TYPE_D3D9_ANGLE = 0x3207;`
- `public const int EGL_PLATFORM_ANGLE_TYPE_D3D11_ANGLE = 0x3208;`
- `public const int EGL_PLATFORM_ANGLE_ANGLE = 0x3202;`
- `public const int EGL_PLATFORM_ANGLE_TYPE_ANGLE = 0x3203;`
- `public const int EGL_PLATFORM_DEVICE_EXT = 0x313F;`
- `public const int EGL_DEVICE_EXT = 0x322C;`
- `public const int EGL_D3D9_DEVICE_ANGLE = 0x33A0;`
- `public const int EGL_D3D11_DEVICE_ANGLE = 0x33A1;`
- `public const int EGL_D3D_TEXTURE_2D_SHARE_HANDLE_ANGLE = 0x3200;`
- `public const int EGL_D3D_TEXTURE_ANGLE = 0x33A3;`
- `public const int EGL_TEXTURE_OFFSET_X_ANGLE = 0x3490;`
- `public const int EGL_TEXTURE_OFFSET_Y_ANGLE = 0x3491;`
- `public const int EGL_FLEXIBLE_SURFACE_COMPATIBILITY_SUPPORTED_ANGLE = 0x33A6;`
- `public const int EGL_TEXTURE_INTERNAL_FORMAT_ANGLE = 0x345D;`

### `src/Avalonia.OpenGL/Egl/EglContext.cs`
- `public class EglContext : IGlContext`
- `public IntPtr Context =>`
- `public EglSurface? OffscreenSurface { get; }`
- `public EglDisplay Display => _disp;`
- `public EglInterface EglInterface => _egl;`
- `public void NotifyContextLost() {`
- `public IDisposable EnsureLocked() {`
- `public bool CanCreateSharedContext => _disp.SupportsSharing;`
- `public bool IsCurrent => _context != default && _egl.GetCurrentDisplay() == _disp.Handle && _egl.GetCurrentContext() == _context;`

### `src/Avalonia.OpenGL/Egl/EglDisplay.cs`
- `public class EglDisplay : IDisposable`
- `public bool SupportsSharing { get; }`
- `public IntPtr Handle => _display;`
- `public IntPtr Config => _config.Config;`
- `public EglDisplay() : this(new EglDisplayCreationOptions {`
- `public EglDisplay(EglDisplayCreationOptions options) : this(EglDisplayUtils.CreateDisplay(options), options) {`
- `public EglDisplay(IntPtr display, EglDisplayOptions options) {`
- `public EglInterface EglInterface => _egl;`
- `public EglContext CreateContext(EglContextOptions? options) {`
- `public EglSurface CreateWindowSurface(IntPtr window) {`
- `public unsafe EglSurface CreatePBufferFromClientBuffer(int bufferType, IntPtr handle, int[] attribs) {`
- `public unsafe EglSurface CreatePBufferFromClientBuffer (int bufferType, IntPtr handle, int* attribs) {`
- `public IDisposable Lock() {`

### `src/Avalonia.OpenGL/Egl/EglDisplayOptions.cs`
- `public class EglDisplayOptions`
- `public EglInterface? Egl { get; set; }`
- `public bool SupportsContextSharing { get; set; }`
- `public bool SupportsMultipleContexts { get; set; }`
- `public bool ContextLossIsDisplayLoss { get; set; }`
- `public Func<bool>? DeviceLostCheckCallback { get; set; }`
- `public Action? DisposeCallback { get; set; }`
- `public IEnumerable<GlVersion>? GlVersions { get; set; }`
- `public class EglContextOptions`
- `public EglContext? ShareWith { get; set; }`
- `public EglSurface? OffscreenSurface { get; set; }`
- `public Dictionary<Type, Func<EglContext, object>>? ExtraFeatures { get; set; }`
- `public class EglDisplayCreationOptions : EglDisplayOptions`
- `public int? PlatformType { get; set; }`
- `public IntPtr PlatformDisplay { get; set; }`
- `public int[]? PlatformDisplayAttrs { get; set; }`

### `src/Avalonia.OpenGL/Egl/EglErrors.cs`
- `public enum EglErrors`

### `src/Avalonia.OpenGL/Egl/EglGlPlatformSurface.cs`
- `public class EglGlPlatformSurface : EglGlPlatformSurfaceBase`
- `public interface IEglWindowGlPlatformSurfaceInfo`
- `public EglGlPlatformSurface(IEglWindowGlPlatformSurfaceInfo info) {`
- `public override IGlPlatformSurfaceRenderTarget CreateGlRenderTarget(IGlContext context) {`

### `src/Avalonia.OpenGL/Egl/EglGlPlatformSurfaceBase.cs`
- `public abstract class EglGlPlatformSurfaceBase : IGlPlatformSurface`
- `public abstract IGlPlatformSurfaceRenderTarget CreateGlRenderTarget(IGlContext context);`
- `public abstract class EglPlatformSurfaceRenderTargetBase : IGlPlatformSurfaceRenderTargetWithCorruptionInfo`
- `public abstract IGlPlatformSurfaceRenderingSession BeginDrawCore();`
- `public virtual bool IsCorrupted => Context.IsLost;`

### `src/Avalonia.OpenGL/Egl/EglInterface.cs`
- `public unsafe partial class EglInterface`
- `public EglInterface(Func<string, IntPtr> getProcAddress) {`
- `public EglInterface(string library) : this(Load(library)) {`
- `public EglInterface() : this(Load()) {`
- `public partial IntPtr GetDisplay(IntPtr nativeDisplay);`
- `public partial IntPtr GetPlatformDisplayExt(int platform, IntPtr nativeDisplay, int[]? attrs);`
- `public partial void Terminate(IntPtr display);`
- `public partial bool BindApi(int api);`
- `public partial bool ChooseConfig(IntPtr display, int[] attribs, out IntPtr surfaceConfig, int numConfigs, out int choosenConfig);`
- `public partial IntPtr CreateContext(IntPtr display, IntPtr config, IntPtr share, int[] attrs);`
- `public partial bool DestroyContext(IntPtr display, IntPtr context);`
- `public partial IntPtr CreatePBufferSurface(IntPtr display, IntPtr config, int[]? attrs);`
- `public partial IntPtr GetCurrentContext();`
- `public partial IntPtr GetCurrentDisplay();`
- `public partial IntPtr GetCurrentSurface(int readDraw);`
- `public partial void DestroySurface(IntPtr display, IntPtr surface);`
- `public partial void SwapBuffers(IntPtr display, IntPtr surface);`
- `public partial IntPtr CreateWindowSurface(IntPtr display, IntPtr config, IntPtr window, int[]? attrs);`
- `public partial int BindTexImage(IntPtr display, IntPtr surface, int buffer);`
- `public partial bool GetConfigAttrib(IntPtr display, IntPtr config, int attr, out int rv);`
- `public partial bool WaitGL();`
- `public partial bool WaitClient();`
- `public partial bool WaitNative(int engine);`
- `public partial IntPtr QueryStringNative(IntPtr display, int i);`
- `public string? QueryString(IntPtr display, int i) {`
- `public partial IntPtr CreatePbufferFromClientBuffer(IntPtr display, int buftype, IntPtr buffer, IntPtr config, int[]? attrib_list);`
- `public partial IntPtr CreatePbufferFromClientBufferPtr(IntPtr display, int buftype, IntPtr buffer, IntPtr config, int* attrib_list);`
- `public partial bool QueryDisplayAttribExt(IntPtr display, int attr, out IntPtr res);`
- `public partial bool QueryDeviceAttribExt(IntPtr display, int attr, out IntPtr res);`

### `src/Avalonia.OpenGL/Egl/EglPlatformGraphics.cs`
- `public sealed class EglPlatformGraphics : IPlatformGraphics`
- `public bool UsesSharedContext => false;`
- `public IPlatformGraphicsContext CreateContext() => _display.CreateContext(null);`
- `public IPlatformGraphicsContext GetSharedContext() => throw new NotSupportedException();`
- `public EglPlatformGraphics(EglDisplay display) {`
- `public static EglPlatformGraphics? TryCreate() => TryCreate(() => new EglDisplay(new EglDisplayCreationOptions`
- `public static EglPlatformGraphics? TryCreate(Func<EglDisplay> displayFactory) {`

### `src/Avalonia.OpenGL/Egl/EglSurface.cs`
- `public class EglSurface : SafeHandle`
- `public EglSurface(EglDisplay display, IntPtr surface) : base(surface, true) {`
- `public override bool IsInvalid => handle == IntPtr.Zero;`
- `public void SwapBuffers() => _egl.SwapBuffers(_display.Handle, handle);`

### `src/Avalonia.OpenGL/Features/ExternalObjectsOpenGlExtensionFeature.cs`
- `public class ExternalObjectsOpenGlExtensionFeature : IGlContextExternalObjectsFeature`
- `public static ExternalObjectsOpenGlExtensionFeature? TryCreate(IGlContext context) {`
- `public IReadOnlyList<string> SupportedImportableExternalImageTypes => _imageTypes;`
- `public IReadOnlyList<string> SupportedExportableExternalImageTypes { get; } = Array.Empty<string>();`
- `public IReadOnlyList<string> SupportedImportableExternalSemaphoreTypes => _semaphoreTypes;`
- `public IReadOnlyList<string> SupportedExportableExternalSemaphoreTypes { get; } = Array.Empty<string>();`
- `public IReadOnlyList<PlatformGraphicsExternalImageFormat> GetSupportedFormatsForExternalMemoryType(string type) {`
- `public IGlExportableExternalImageTexture CreateImage(string type, PixelSize size, PlatformGraphicsExternalImageFormat format) =>`
- `public IGlExportableExternalImageTexture CreateSemaphore(string type) => throw new NotSupportedException();`
- `public IGlExternalImageTexture ImportImage(IPlatformHandle handle, PlatformGraphicsExternalImageProperties properties) {`
- `public IGlExternalSemaphore ImportSemaphore(IPlatformHandle handle) {`
- `public CompositionGpuImportedImageSynchronizationCapabilities GetSynchronizationCapabilities(string imageHandleType) {`
- `public byte[]? DeviceLuid { get; }`
- `public byte[]? DeviceUuid { get; }`

### `src/Avalonia.OpenGL/GlBasicInfoInterface.cs`
- `public unsafe partial class GlBasicInfoInterface`
- `public GlBasicInfoInterface(Func<string, IntPtr> getProcAddress) {`
- `public partial void GetIntegerv(int name, out int rv);`
- `public partial void GetFloatv(int name, out float rv);`
- `public partial IntPtr GetStringNative(int v);`
- `public partial IntPtr GetStringiNative(int v, int v1);`
- `public string? GetString(int v) {`
- `public string? GetString(int v, int index) {`
- `public List<string> GetExtensions() {`

### `src/Avalonia.OpenGL/GlConsts.cs`
- `public static class GlConsts`
- `public const int GL_UNSIGNED_BYTE = 0x1401;`
- `public const int GL_UNSIGNED_SHORT = 0x1403;`
- `public const int GL_FLOAT = 0x1406;`
- `public const int GL_TRIANGLES = 0x0004;`
- `public const int GL_CULL_FACE = 0x0B44;`
- `public const int GL_LESS = 0x0201;`
- `public const int GL_GREATER = 0x0204;`
- `public const int GL_DEPTH_TEST = 0x0B71;`
- `public const int GL_DEPTH_COMPONENT = 0x1902;`
- `public const int GL_LINEAR = 0x2601;`
- `public const int GL_STENCIL_BITS = 0x0D57;`
- `public const int GL_RGBA = 0x1908;`
- `public const int GL_SCISSOR_TEST = 0x0C11;`
- `public const int GL_TEXTURE_2D = 0x0DE1;`
- `public const int GL_TEXTURE_MAG_FILTER = 0x2800;`
- `public const int GL_TEXTURE_MIN_FILTER = 0x2801;`
- `public const int GL_NEAREST = 0x2600;`
- `public const int GL_VENDOR = 0x1F00;`
- `public const int GL_RENDERER = 0x1F01;`
- `public const int GL_VERSION = 0x1F02;`
- `public const int GL_EXTENSIONS = 0x1F03;`
- `public const int GL_NO_ERROR = 0;`
- `public const int GL_INVALID_ENUM = 0x0500;`
- `public const int GL_INVALID_VALUE = 0x0501;`
- `public const int GL_INVALID_OPERATION = 0x0502;`
- `public const int GL_STACK_OVERFLOW = 0x0503;`
- `public const int GL_STACK_UNDERFLOW = 0x0504;`
- `public const int GL_OUT_OF_MEMORY = 0x0505;`
- `public const int GL_INVALID_FRAMEBUFFER_OPERATION = 0x0506;`
- `public const int GL_CONTEXT_LOST = 0x0507;`
- `public const int GL_DEPTH_BUFFER_BIT = 0x00000100;`
- `public const int GL_STENCIL_BUFFER_BIT = 0x00000400;`
- `public const int GL_COLOR_BUFFER_BIT = 0x00004000;`
- `public const int GL_TEXTURE_BINDING_2D = 0x8069;`
- `public const int GL_RGBA8 = 0x8058;`
- `public const int GL_BGRA = 0x80E1;`
- `public const int GL_UNSIGNED_INT_8_8_8_8_REV = 0x8367;`
- `public const int GL_TEXTURE0 = 0x84C0;`
- `public const int GL_ACTIVE_TEXTURE = 0x84E0;`
- `public const int GL_SAMPLES = 0x80A9;`
- `public const int GL_DEPTH_COMPONENT16 = 0x81A5;`
- `public const int GL_ARRAY_BUFFER = 0x8892;`
- `public const int GL_ELEMENT_ARRAY_BUFFER = 0x8893;`
- `public const int GL_STATIC_DRAW = 0x88E4;`
- `public const int GL_FRAGMENT_SHADER = 0x8B30;`
- `public const int GL_VERTEX_SHADER = 0x8B31;`
- `public const int GL_COMPILE_STATUS = 0x8B81;`
- `public const int GL_LINK_STATUS = 0x8B82;`
- `public const int GL_INFO_LOG_LENGTH = 0x8B84;`
- `public const int GL_MAJOR_VERSION = 0x821B;`
- `public const int GL_MINOR_VERSION = 0x821C;`
- `public const int GL_NUM_EXTENSIONS = 0x821D;`
- `public const int GL_DEPTH_STENCIL = 0x84F9;`
- `public const int GL_DEPTH24_STENCIL8 = 0x88F0;`
- `public const int GL_FRAMEBUFFER_BINDING = 0x8CA6;`
- `public const int GL_RENDERBUFFER_BINDING = 0x8CA7;`
- `public const int GL_READ_FRAMEBUFFER = 0x8CA8;`
- `public const int GL_DRAW_FRAMEBUFFER = 0x8CA9;`
- `public const int GL_READ_FRAMEBUFFER_BINDING = 0x8CAA;`
- `public const int GL_FRAMEBUFFER_COMPLETE = 0x8CD5;`
- `public const int GL_COLOR_ATTACHMENT0 = 0x8CE0;`
- `public const int GL_DEPTH_ATTACHMENT = 0x8D00;`
- `public const int GL_STENCIL_ATTACHMENT = 0x8D20;`
- `public const int GL_FRAMEBUFFER = 0x8D40;`
- `public const int GL_RENDERBUFFER = 0x8D41;`
- `public const int GL_RENDERBUFFER_WIDTH = 0x8D42;`
- `public const int GL_RENDERBUFFER_HEIGHT = 0x8D43;`
- `public const int GL_STENCIL_INDEX8 = 0x8D48;`
- `public const int GL_TEXTURE_RECTANGLE = 0x84F5;`
- `public const int GL_TEXTURE_BINDING_RECTANGLE = 0x84F6;`
- `public const int GL_CONTEXT_CORE_PROFILE_BIT = 0x00000001;`
- `public const int GL_CONTEXT_COMPATIBILITY_PROFILE_BIT = 0x00000002;`
- `public const int GL_CONTEXT_PROFILE_MASK = 0x9126;`
- `public const int GL_DEVICE_LUID_EXT = 0x9599;`

### `src/Avalonia.OpenGL/GlErrors.cs`
- `public enum GlErrors`

### `src/Avalonia.OpenGL/GlInterface.cs`
- `public string? Vendor { get; }`
- `public GlContextInfo ContextInfo { get; }`
- `public class GlContextInfo`
- `public GlContextInfo(GlVersion version, HashSet<string> extensions) {`
- `public partial void ClearStencil(int s);`
- `public partial void ClearColor(float r, float g, float b, float a);`
- `public void ClearDepth(float value) {`
- `public partial void DepthFunc(int value);`
- `public partial void DepthMask(int value);`
- `public partial void Flush();`
- `public partial void Finish();`
- `public partial void GenFramebuffers(int count, int* res);`
- `public int GenFramebuffer() {`
- `public partial void DeleteFramebuffers(int count, int* framebuffers);`
- `public void DeleteFramebuffer(int fb) {`
- `public partial void BindFramebuffer(int target, int fb);`
- `public partial int CheckFramebufferStatus(int target);`
- `public partial void BlitFramebuffer(int srcX0, int srcY0, int srcX1, int srcY1, int dstX0, int dstY0, int dstX1, int dstY1, int mask, int filter);`
- `public partial void GenRenderbuffers(int count, int* res);`
- `public int GenRenderbuffer() {`
- `public partial void DeleteRenderbuffers(int count, int* renderbuffers);`
- `public void DeleteRenderbuffer(int renderbuffer) {`
- `public partial void BindRenderbuffer(int target, int fb);`
- `public partial void RenderbufferStorage(int target, int internalFormat, int width, int height);`
- `public partial void FramebufferRenderbuffer(int target, int attachment, int renderbufferTarget, int renderbuffer);`
- `public partial void GenTextures(int count, int* res);`
- `public int GenTexture() {`
- `public partial void BindTexture(int target, int fb);`
- `public partial void ActiveTexture(int texture);`
- `public partial void DeleteTextures(int count, int* textures);`
- `public void DeleteTexture(int texture) => DeleteTextures(1, &texture);`
- `public partial void TexImage2D(int target, int level, int internalFormat, int width, int height, int border, int format, int type, IntPtr data);`
- `public partial void CopyTexSubImage2D(int target, int level, int xoffset, int yoffset, int x, int y, int width, int height);`
- `public partial void TexParameteri(int target, int name, int value);`
- `public partial void FramebufferTexture2D(int target, int attachment, int texTarget, int texture, int level);`
- `public partial int CreateShader(int shaderType);`
- `public partial void ShaderSource(int shader, int count, IntPtr strings, IntPtr lengths);`
- `public void ShaderSourceString(int shader, string source) {`
- `public partial void CompileShader(int shader);`
- `public partial void GetShaderiv(int shader, int name, int* parameters);`
- `public partial void GetShaderInfoLog(int shader, int maxLength, out int length, void* infoLog);`
- `public unsafe string? CompileShaderAndGetError(int shader, string source) {`
- `public partial int CreateProgram();`
- `public partial void AttachShader(int program, int shader);`
- `public partial void LinkProgram(int program);`
- `public partial void GetProgramiv(int program, int name, int* parameters);`
- `public partial void GetProgramInfoLog(int program, int maxLength, out int len, void* infoLog);`
- `public unsafe string? LinkProgramAndGetError(int program) {`
- `public partial void BindAttribLocation(int program, int index, IntPtr name);`
- `public void BindAttribLocationString(int program, int index, string name) {`
- `public partial void GenBuffers(int len, int* rv);`
- `public int GenBuffer() {`
- `public partial void BindBuffer(int target, int buffer);`
- `public partial void BufferData(int target, IntPtr size, IntPtr data, int usage);`
- `public partial int GetAttribLocation(int program, IntPtr name);`
- `public int GetAttribLocationString(int program, string name) {`
- `public partial void VertexAttribPointer(int index, int size, int type, int normalized, int stride, IntPtr pointer);`
- `public partial void EnableVertexAttribArray(int index);`
- `public partial void UseProgram(int program);`
- `public partial void DrawArrays(int mode, int first, IntPtr count);`
- `public partial void DrawElements(int mode, int count, int type, IntPtr indices);`
- `public partial int GetUniformLocation(int program, IntPtr name);`
- `public int GetUniformLocationString(int program, string name) {`
- `public partial void Uniform1f(int location, float falue);`
- `public partial void UniformMatrix4fv(int location, int count, bool transpose, void* value);`
- `public partial void Enable(int what);`
- `public partial void Disable(int what);`
- `public partial void DeleteBuffers(int count, int* buffers);`
- `public void DeleteBuffer(int buffer) => DeleteBuffers(1, &buffer);`
- `public partial void DeleteProgram(int program);`
- `public partial void DeleteShader(int shader);`
- `public partial void GetRenderbufferParameteriv(int target, int name, out int value);`
- `public partial void DeleteVertexArrays(int count, int* arrays);`
- `public void DeleteVertexArray(int array) => DeleteVertexArrays(1, &array);`
- `public partial void BindVertexArray(int array);`
- `public partial void GenVertexArrays(int n, int* rv);`
- `public int GenVertexArray() {`
- `public static GlInterface FromNativeUtf8GetProcAddress(GlVersion version, Func<IntPtr, IntPtr> getProcAddress) {`

### `src/Avalonia.OpenGL/GlVersion.cs`
- `public enum GlProfileType`
- `public int Major { get; }`
- `public int Minor { get; }`
- `public bool IsCompatibilityProfile { get; }`

### `src/Avalonia.OpenGL/IGlContext.cs`
- `public interface IGlPlatformSurfaceRenderTargetFactory`

### `src/Avalonia.OpenGL/IGlContextExternalObjectsFeature.cs`
- `public interface IGlContextExternalObjectsFeature`
- `public byte[]? DeviceLuid { get; }`
- `public byte[]? DeviceUuid { get; }`
- `public interface IGlExternalSemaphore : IDisposable`
- `public interface IGlExportableExternalSemaphore : IGlExternalSemaphore`
- `public interface IGlExternalImageTexture : IDisposable`
- `public int TextureType { get; }`
- `public interface IGlExportableExternalImageTexture : IGlExternalImageTexture`

### `src/Avalonia.OpenGL/IOpenGlTextureSharingRenderInterfaceContextFeature.cs`
- `public interface IOpenGlTextureSharingRenderInterfaceContextFeature`
- `public interface ICompositionImportableOpenGlSharedTexture : ICompositionImportableSharedGpuContextImage`

### `src/Avalonia.OpenGL/IPlatformGraphicsOpenGlContextFactory.cs`
- `public interface IPlatformGraphicsOpenGlContextFactory`

### `src/Avalonia.OpenGL/OpenGlException.cs`
- `public class OpenGlException : Exception`
- `public int? ErrorCode { get; }`
- `public OpenGlException(string? message) : base(message) {`
- `public static OpenGlException GetFormattedException(string funcName, EglInterface egl) {`
- `public static OpenGlException GetFormattedException(string funcName, GlInterface gl) {`
- `public static OpenGlException GetFormattedException(string funcName, int errorCode) =>`
- `public static OpenGlException GetFormattedEglException(string funcName, int errorCode) =>`

### `src/Avalonia.OpenGL/Surfaces/IGlPlatformSurfaceRenderTarget.cs`
- `public interface IGlPlatformSurfaceRenderTargetWithCorruptionInfo : IGlPlatformSurfaceRenderTarget`
- `public interface IGlPlatformSurfaceRenderTarget2 : IGlPlatformSurfaceRenderTargetWithCorruptionInfo`

### `src/Avalonia.Remote.Protocol/AvaloniaRemoteMessageGuidAttribute.cs`
- `public sealed class AvaloniaRemoteMessageGuidAttribute : Attribute`
- `public Guid Guid { get; }`
- `public AvaloniaRemoteMessageGuidAttribute(string guid) {`

### `src/Avalonia.Remote.Protocol/BsonTcpTransport.cs`
- `public class BsonTcpTransport : TcpTransportBase`
- `public BsonTcpTransport(IMessageTypeResolver resolver) : base(resolver) {`
- `public BsonTcpTransport() : this(new DefaultMessageTypeResolver(typeof(BsonTcpTransport).GetTypeInfo().Assembly)) {`

### `src/Avalonia.Remote.Protocol/DefaultMessageTypeResolver.cs`
- `public class DefaultMessageTypeResolver : IMessageTypeResolver`
- `public DefaultMessageTypeResolver(params Assembly[] assemblies) {`
- `public Type GetByGuid(Guid id) => _guidsToTypes[id];`
- `public Guid GetGuid(Type type) => _typesToGuids[type];`

### `src/Avalonia.Remote.Protocol/DesignMessages.cs`
- `public class UpdateXamlMessage`
- `public string Xaml { get; set; }`
- `public string AssemblyPath { get; set; }`
- `public string XamlFileProjectPath { get; set; }`
- `public class UpdateXamlResultMessage`
- `public string Handle { get; set; }`
- `public class StartDesignerSessionMessage`
- `public string SessionId { get; set; }`
- `public class ExceptionDetails`
- `public ExceptionDetails() {`
- `public ExceptionDetails(Exception e) {`
- `public string ExceptionType { get; set; }`
- `public int? LineNumber { get; set; }`
- `public int? LinePosition { get; set; }`

### `src/Avalonia.Remote.Protocol/IMessageTypeResolver.cs`
- `public interface IMessageTypeResolver`

### `src/Avalonia.Remote.Protocol/ITransport.cs`
- `public interface IAvaloniaRemoteTransportConnection : IDisposable`

### `src/Avalonia.Remote.Protocol/InputMessages.cs`
- `public enum InputModifiers`
- `public abstract class InputEventMessageBase`
- `public abstract class PointerEventMessageBase : InputEventMessageBase`
- `public double X { get; set; }`
- `public double Y { get; set; }`
- `public class PointerMovedEventMessage : PointerEventMessageBase`
- `public class PointerPressedEventMessage : PointerEventMessageBase`
- `public class PointerReleasedEventMessage : PointerEventMessageBase`
- `public class ScrollEventMessage : PointerEventMessageBase`
- `public double DeltaX { get; set; }`
- `public double DeltaY { get; set; }`
- `public class KeyEventMessage : InputEventMessageBase`
- `public bool IsDown { get; set; }`
- `public string? KeySymbol { get; set; }`
- `public class TextInputEventMessage : InputEventMessageBase`

### `src/Avalonia.Remote.Protocol/MetsysBson.cs`
- `public interface IExpando`
- `public static class Helper`
- `public static readonly DateTime Epoch = new DateTime(1970, 1, 1, 0, 0, 0, DateTimeKind.Utc);`
- `public interface ITypeConfiguration<T>`
- `public static class ExpressionHelper`
- `public static MemberExpression GetMemberExpression<T, TValue>(this Expression<Func<T, TValue>> expression) {`

### `src/Avalonia.Remote.Protocol/TcpTransportBase.cs`
- `public abstract class TcpTransportBase`
- `public TcpTransportBase(IMessageTypeResolver resolver) {`
- `public IDisposable Listen(IPAddress address, int port, Action<IAvaloniaRemoteTransportConnection> cb) {`
- `public async Task<IAvaloniaRemoteTransportConnection> Connect(IPAddress address, int port) {`

### `src/Avalonia.Remote.Protocol/TransportConnectionWrapper.cs`
- `public class TransportConnectionWrapper : IAvaloniaRemoteTransportConnection`
- `public TransportConnectionWrapper(IAvaloniaRemoteTransportConnection conn) {`
- `public event Action<IAvaloniaRemoteTransportConnection, Exception> OnException {`

### `src/Avalonia.Remote.Protocol/TransportMessages.cs`
- `public class HtmlTransportStartedMessage`

### `src/Avalonia.Remote.Protocol/ViewportMessages.cs`
- `public enum PixelFormat`
- `public class MeasureViewportMessage`
- `public class ClientViewportAllocatedMessage`
- `public double DpiX { get; set; }`
- `public double DpiY { get; set; }`
- `public class RequestViewportResizeMessage`
- `public class ClientSupportedPixelFormatsMessage`
- `public PixelFormat[] Formats { get; set; }`
- `public class ClientRenderInfoMessage`
- `public class FrameReceivedMessage`
- `public long SequenceId { get; set; }`
- `public class FrameMessage`
- `public PixelFormat Format { get; set; }`
- `public int Stride { get; set; }`

### `src/Avalonia.Themes.Simple/SimpleTheme.xaml.cs`
- `public class SimpleTheme : Styles`
- `public SimpleTheme(IServiceProvider? sp = null) {`

### `src/Avalonia.Vulkan/IVulkanContextExternalObjectsFeature.cs`
- `public interface IVulkanContextExternalObjectsFeature`
- `public interface IVulkanExternalSemaphore : IDisposable`
- `public interface IVulkanExternalImage : IDisposable`

### `src/Avalonia.Vulkan/IVulkanDevice.cs`
- `public IntPtr Handle { get; }`
- `public IntPtr PhysicalDeviceHandle { get; }`
- `public IntPtr MainQueueHandle { get; }`
- `public uint GraphicsQueueFamilyIndex { get; }`
- `public IDisposable Lock();`
- `public IEnumerable<string> EnabledExtensions { get; }`
- `public IntPtr GetInstanceProcAddress(IntPtr instance, string name);`
- `public IntPtr GetDeviceProcAddress(IntPtr device, string name);`

### `src/Avalonia.Vulkan/IVulkanPlatformSurface.cs`
- `public interface IVulkanKhrSurfacePlatformSurface : IDisposable`
- `public interface IVulkanKhrSurfacePlatformSurfaceFactory`

### `src/Avalonia.Vulkan/UnmanagedInterop/VulkanStructs.cs`
- `public struct VkMemoryTypesBuffer`
- `public VkMemoryType Element0;`
- `public VkMemoryType Element1;`
- `public VkMemoryType Element2;`
- `public VkMemoryType Element3;`
- `public VkMemoryType Element4;`
- `public VkMemoryType Element5;`
- `public VkMemoryType Element6;`
- `public VkMemoryType Element7;`
- `public VkMemoryType Element8;`
- `public VkMemoryType Element9;`
- `public VkMemoryType Element10;`
- `public VkMemoryType Element11;`
- `public VkMemoryType Element12;`
- `public VkMemoryType Element13;`
- `public VkMemoryType Element14;`
- `public VkMemoryType Element15;`
- `public VkMemoryType Element16;`
- `public VkMemoryType Element17;`
- `public VkMemoryType Element18;`
- `public VkMemoryType Element19;`
- `public VkMemoryType Element20;`
- `public VkMemoryType Element21;`
- `public VkMemoryType Element22;`
- `public VkMemoryType Element23;`
- `public VkMemoryType Element24;`
- `public VkMemoryType Element25;`
- `public VkMemoryType Element26;`
- `public VkMemoryType Element27;`
- `public VkMemoryType Element28;`
- `public VkMemoryType Element29;`
- `public VkMemoryType Element30;`
- `public VkMemoryType Element31;`
- `public struct VkMemoryHeapsBuffer`
- `public VkMemoryHeap Element0;`
- `public VkMemoryHeap Element1;`
- `public VkMemoryHeap Element2;`
- `public VkMemoryHeap Element3;`
- `public VkMemoryHeap Element4;`
- `public VkMemoryHeap Element5;`
- `public VkMemoryHeap Element6;`
- `public VkMemoryHeap Element7;`
- `public VkMemoryHeap Element8;`
- `public VkMemoryHeap Element9;`
- `public VkMemoryHeap Element10;`
- `public VkMemoryHeap Element11;`
- `public VkMemoryHeap Element12;`
- `public VkMemoryHeap Element13;`
- `public VkMemoryHeap Element14;`
- `public VkMemoryHeap Element15;`

### `src/Avalonia.Vulkan/VulkanException.cs`
- `public class VulkanException : Exception`
- `public VulkanException(string message) : base(message) {`
- `public VulkanException(string funcName, int res) : this(funcName, (VkResult)res) {`
- `public static void ThrowOnError(string funcName, int res) => ((VkResult)res).ThrowOnError(funcName);`

### `src/Avalonia.Vulkan/VulkanImageInfo.cs`
- `public record struct VulkanImageInfo`
- `public uint Format { get; set; }`
- `public PixelSize PixelSize { get; set; }`
- `public ulong Handle { get; set; }`
- `public uint Tiling { get; set; }`
- `public uint UsageFlags { get; set; }`
- `public uint LevelCount { get; set; }`
- `public ulong MemoryHandle { get; set; }`
- `public ulong ViewHandle { get; set; }`
- `public ulong MemorySize { get; set; }`
- `public bool IsProtected { get; set; }`

### `src/Avalonia.Vulkan/VulkanOptions.cs`
- `public VkGetInstanceProcAddressDelegate? CustomGetProcAddressDelegate { get; set; }`
- `public class VulkanPlatformSpecificOptions`
- `public IList<string> RequiredInstanceExtensions { get; set; } = new List<string>();`
- `public VkGetInstanceProcAddressDelegate? GetProcAddressDelegate { get; set; }`
- `public Func<IVulkanInstance, ulong>? DeviceCheckSurfaceFactory { get; set; }`
- `public Dictionary<Type, object> PlatformFeatures { get; set; } = new();`

### `src/Avalonia.Vulkan/VulkanPlatformGraphics.cs`
- `public class VulkanPlatformGraphics : IPlatformGraphics`
- `public VulkanPlatformGraphics(IVulkanDeviceFactory factory, VulkanPlatformSpecificOptions platformOptions) {`
- `public IPlatformGraphicsContext CreateContext() =>`
- `public IPlatformGraphicsContext GetSharedContext() {`
- `public bool UsesSharedContext => _factory.UsesShadedDevice;`
- `public interface IVulkanDeviceFactory`
- `public static VulkanPlatformGraphics? TryCreate(VulkanOptions options, VulkanPlatformSpecificOptions platformOptions) {`

### `src/Avalonia.X11/Clipboard/ClipboardReadSession.cs`
- `public class GetDataResult(byte[]? data, MemoryStream? stream, IntPtr actualTypeAtom)`
- `public IntPtr TypeAtom => actualTypeAtom;`
- `public byte[] AsBytes() => data ?? stream!.ToArray();`
- `public MemoryStream AsStream() => stream ?? new MemoryStream(data!);`

### `src/Avalonia.X11/Interop/GtkInteropHelper.cs`
- `public class GtkInteropHelper`
- `public static async Task<T> RunOnGlibThread<T>(Func<T> cb) {`

### `src/Avalonia.X11/X11WindowModes/DefaultWindowMode.cs`
- `public class DefaultTopLevelWindowMode : X11WindowMode`
- `public override Point PointToClient(PixelPoint point) => new Point(`
- `public override PixelPoint PointToScreen(Point point) => new PixelPoint(`

### `src/Avalonia.X11/X11WindowModes/InputProxyWindowMode.cs`
- `public class InputProxyWindowMode : DefaultTopLevelWindowMode`
- `public override void OnHandleCreated(IntPtr handle) {`
- `public override bool OnEvent(ref XEvent ev) {`
- `public override void OnDestroyNotify() {`
- `public override void AppendWmProtocols(List<IntPtr> data) {`

### `src/Avalonia.X11/X11WindowModes/WindowMode.cs`
- `public abstract class X11WindowMode`
- `public virtual bool BlockInput => false;`
- `public void Init(X11Window window) {`
- `public virtual bool OnEvent(ref XEvent ev) {`
- `public virtual void OnHandleCreated(IntPtr handle) {`
- `public virtual void OnDestroyNotify() {`
- `public virtual void AppendWmProtocols(List<IntPtr> data) {`
- `public abstract PixelPoint PointToScreen(Point pt);`
- `public abstract Point PointToClient(PixelPoint pt);`

### `src/Avalonia.X11/X11WindowModes/XEmbedClientWindowMode.cs`
- `public class XEmbedClientWindowMode : X11WindowMode`
- `public override bool BlockInput => _disabled;`
- `public override void OnHandleCreated(IntPtr handle) {`
- `public override bool OnEvent(ref XEvent ev) {`
- `public void ProcessInteractiveResize(PixelSize size) {`
- `public override Point PointToClient(PixelPoint point) {`
- `public override PixelPoint PointToScreen(Point point) =>`

### `src/Avalonia.X11/XEmbedPlug.cs`
- `public class XEmbedPlug : IDisposable`
- `public IntPtr Handle =>`
- `public Color BackgroundColor {`
- `public double ScaleFactor {`
- `public void ProcessInteractiveResize(PixelSize size) {`

### `src/Browser/Avalonia.Browser.Blazor/BlazorSingleViewLifetime.cs`
- `public static class BlazorAppBuilder`
- `public static async Task StartBlazorAppAsync(this AppBuilder builder, BrowserPlatformOptions? options = null) {`

### `src/Browser/Avalonia.Browser/JSObjectControlHandle.cs`
- `public class JSObjectPlatformHandle : PlatformHandle`
- `public JSObject Object { get; }`
- `public class JSObjectControlHandle : JSObjectPlatformHandle, INativeControlHostDestroyableControlHandle`
- `public JSObjectControlHandle(JSObject reference) : base(reference) {`
- `public void Destroy() {`

### `src/Headless/Avalonia.Headless.NUnit/AvaloniaTest.cs`
- `public TestCommand Wrap(TestCommand command) {`

### `src/Headless/Avalonia.Headless.NUnit/AvaloniaTheory.cs`
- `public TestCommand Wrap(TestCommand command) {`

### `src/Headless/Avalonia.Headless.Vnc/HeadlessVncFramebufferSource.cs`
- `public class HeadlessVncFramebufferSource : IVncFramebufferSource`
- `public VncFramebuffer _framebuffer = new VncFramebuffer("Avalonia", 1, 1, VncPixelFormat.RGB32);`
- `public HeadlessVncFramebufferSource(VncServerSession session, Window window) {`
- `public unsafe VncFramebuffer Capture() {`
- `public ExtendedDesktopSizeStatus SetDesktopSize(int width, int height) {`
- `public bool SupportsResizing => true;`

### `src/Headless/Avalonia.Headless.Vnc/HeadlessVncPlatformExtensions.cs`
- `public static class HeadlessVncPlatformExtensions`
- `public static int StartWithHeadlessVncPlatform( this AppBuilder builder, string host, int port, string[] args, ShutdownMode shutdownMode = ShutdownMode.OnLastWindowClose) {`
- `public static int StartWithHeadlessVncPlatform( this AppBuilder builder, string host, int port, string? password, string[] args, ShutdownMode shutdownMode = ShutdownMode.OnLastWindowClose) {`

### `src/Headless/Avalonia.Headless.XUnit/AvaloniaFact.cs`
- `public class AvaloniaUIFactDiscoverer : FactDiscoverer`
- `public AvaloniaUIFactDiscoverer(IMessageSink diagnosticMessageSink) : base(diagnosticMessageSink) {`

### `src/Headless/Avalonia.Headless.XUnit/AvaloniaTestFrameworkAttribute.cs`
- `public sealed class AvaloniaTestFrameworkAttribute : Attribute, ITestFrameworkAttribute`
- `public class AvaloniaTestFrameworkTypeDiscoverer : ITestFrameworkTypeDiscoverer`
- `public AvaloniaTestFrameworkTypeDiscoverer(IMessageSink _) {`
- `public Type GetTestFrameworkType(IAttributeInfo attribute) {`

### `src/Headless/Avalonia.Headless.XUnit/AvaloniaTheoryAttribute.cs`
- `public class AvaloniaTheoryDiscoverer : TheoryDiscoverer`
- `public AvaloniaTheoryDiscoverer(IMessageSink diagnosticMessageSink) : base(diagnosticMessageSink) {`

### `src/Headless/Avalonia.Headless/AvaloniaTestApplicationAttribute.cs`
- `public Type AppBuilderEntryPointType { get; }`

### `src/Headless/Avalonia.Headless/HeadlessUnitTestIsolationAttribute.cs`
- `public AvaloniaTestIsolationLevel IsolationLevel { get; } = isolationLevel;`

### `src/Headless/Avalonia.Headless/HeadlessWindowExtensions.cs`
- `public static void KeyPressQwerty(this TopLevel topLevel, PhysicalKey physicalKey, RawInputModifiers modifiers) =>`
- `public static void KeyReleaseQwerty(this TopLevel topLevel, PhysicalKey physicalKey, RawInputModifiers modifiers) =>`

### `src/Linux/Avalonia.LinuxFramebuffer/DrmConnectorType.cs`
- `public enum DrmConnectorType : uint`

### `src/Linux/Avalonia.LinuxFramebuffer/DrmOutputOptions.cs`
- `public bool EnableInitialBufferSwapping { get; set; } = true;`
- `public Color InitialBufferSwappingColor { get; set; } = new Color(0, 0, 0, 0);`
- `public DrmConnectorType? ConnectorType { get; set; }`
- `public uint? ConnectorTypeId { get; set; }`

### `src/Linux/Avalonia.LinuxFramebuffer/Input/EvDev/EvDevBackend.cs`
- `public class EvDevBackend : IInputBackend`
- `public EvDevBackend(EvDevDeviceDescription[] devices) {`
- `public void SetInputRoot(IInputRoot root) {`
- `public static EvDevBackend CreateFromEnvironment() {`

### `src/Linux/Avalonia.LinuxFramebuffer/Input/EvDev/EvDevDeviceDescription.cs`
- `public abstract class EvDevDeviceDescription`

### `src/Linux/Avalonia.LinuxFramebuffer/Input/EvDev/EvDevTouchScreenDeviceDescription.cs`
- `public sealed class EvDevTouchScreenDeviceDescription : EvDevDeviceDescription`
- `public Matrix CalibrationMatrix { get; set; } = Matrix.Identity;`

### `src/Linux/Avalonia.LinuxFramebuffer/Input/IInputBackend.cs`
- `public interface IInputBackend`

### `src/Linux/Avalonia.LinuxFramebuffer/Input/IScreenInfoProvider.cs`
- `public interface IScreenInfoProvider`

### `src/Linux/Avalonia.LinuxFramebuffer/Input/LibInput/LibInputBackend.Pointer.cs`
- `public partial class LibInputBackend`

### `src/Linux/Avalonia.LinuxFramebuffer/Input/LibInput/LibInputBackend.Touch.cs`
- `public partial class LibInputBackend`

### `src/Linux/Avalonia.LinuxFramebuffer/Input/LibInput/LibInputBackend.cs`
- `public partial class LibInputBackend : IInputBackend`
- `public LibInputBackend() {`
- `public LibInputBackend(LibInputBackendOptions options) {`
- `public void SetInputRoot(IInputRoot root) {`

### `src/Linux/Avalonia.LinuxFramebuffer/Input/LibInput/LibInputBackendOptions.cs`
- `public sealed record class LibInputBackendOptions`
- `public IReadOnlyList<string>? Events { get; init; } = null;`

### `src/Linux/Avalonia.LinuxFramebuffer/Input/LibInput/LibInputNativeUnsafeMethods.cs`
- `public enum LibInputEventType`
- `public enum LibInputPointerAxisSource`
- `public enum LibInputPointerAxis`

### `src/Linux/Avalonia.LinuxFramebuffer/Input/NullInput/NullInputBackend.cs`
- `public class NullInputBackend : IInputBackend`
- `public void SetInputRoot(IInputRoot root) {`

### `src/Linux/Avalonia.LinuxFramebuffer/Output/Drm.cs`
- `public enum DrmModeConnection`
- `public enum DrmModeSubPixel{`
- `public struct DrmEventContext`
- `public int version;`
- `public IntPtr vblank_handler;`
- `public IntPtr page_flip_handler;`
- `public IntPtr page_flip_handler2;`
- `public IntPtr sequence_handler;`
- `public struct drmModeRes {`
- `public int count_fbs;`
- `public uint *fbs;`
- `public int count_crtcs;`
- `public uint *crtcs;`
- `public int count_connectors;`
- `public uint *connectors;`
- `public int count_encoders;`
- `public uint *encoders;`
- `public enum DrmModeType`
- `public struct drmModeModeInfo`
- `public uint clock;`
- `public ushort hdisplay, hsync_start, hsync_end, htotal, hskew;`
- `public ushort vdisplay, vsync_start, vsync_end, vtotal, vscan;`
- `public uint vrefresh;`
- `public uint flags;`
- `public DrmModeType type;`
- `public fixed byte name[32];`
- `public struct drmModeConnector {`
- `public uint connector_id;`
- `public uint encoder_id;`
- `public uint connector_type;`
- `public uint connector_type_id;`
- `public DrmModeConnection connection;`
- `public uint mmWidth, mmHeight;`
- `public DrmModeSubPixel subpixel;`
- `public int count_modes;`
- `public drmModeModeInfo* modes;`
- `public int count_props;`
- `public uint *props;`
- `public ulong *prop_values;`
- `public struct drmModeEncoder {`
- `public uint encoder_type;`
- `public uint crtc_id;`
- `public uint possible_crtcs;`
- `public uint possible_clones;`
- `public struct drmModeCrtc {`
- `public uint buffer_id;`
- `public uint x, y;`
- `public int mode_valid;`
- `public drmModeModeInfo mode;`
- `public int gamma_size;`
- `public enum DrmModePageFlip`
- `public enum GbmBoFlags {`
- `public struct GbmBoHandle`
- `public void *ptr;`
- `public int s32;`
- `public uint u32;`
- `public long s64;`
- `public ulong u64;`
- `public static class GbmColorFormats`
- `public static uint FourCC(char a, char b, char c, char d) =>`
- `public static uint GBM_FORMAT_XRGB8888 { get; } = FourCC('X', 'R', '2', '4');`

### `src/Linux/Avalonia.LinuxFramebuffer/Output/DrmBindings.cs`
- `public uint Id { get; }`
- `public Size SizeMm { get; }`
- `public DrmModeSubPixel SubPixel { get; }`
- `public List<DrmModeInfo> Modes { get; } = new List<DrmModeInfo>();`
- `public DrmConnectorType ConnectorType { get; }`
- `public uint ConnectorTypeId { get; }`
- `public bool IsPreferred => Mode.type.HasAllFlags(DrmModeType.DRM_MODE_TYPE_PREFERRED);`
- `public List<DrmConnector> Connectors { get; } = new List<DrmConnector>();`
- `public int Fd { get; private set; }`
- `public DrmResources GetResources(bool connectorsForceProbe = false) => new DrmResources(Fd, connectorsForceProbe);`

### `src/Linux/Avalonia.LinuxFramebuffer/Output/DrmOutput.cs`
- `public unsafe class DrmOutput : IGlOutputBackend, IGlPlatformSurface`
- `public PixelSize PixelSize => _mode.Resolution;`
- `public IPlatformGraphics PlatformGraphics { get; private set; }`
- `public DrmOutput(DrmCard card, DrmResources resources, DrmConnector connector, DrmModeInfo modeInfo, DrmOutputOptions? options = null) {`
- `public DrmOutput(string? path = null, bool connectorsForceProbe = false, DrmOutputOptions? options = null) :this(new DrmCard(path), connectorsForceProbe, options) {`
- `public DrmOutput(DrmCard card, bool connectorsForceProbe = false, DrmOutputOptions? options = null) {`
- `public DrmOutput(DrmCard card, DrmResources resources, DrmConnector connector, DrmModeInfo modeInfo) {`
- `public IGlPlatformSurfaceRenderTarget CreateGlRenderTarget() => new RenderTarget(this);`
- `public IGlPlatformSurfaceRenderTarget CreateGlRenderTarget(IGlContext context) {`
- `public IGlContext CreateContext() {`

### `src/Linux/Avalonia.LinuxFramebuffer/Output/FbDevOutputOptions.cs`
- `public class FbDevOutputOptions`
- `public PixelFormat? PixelFormat { get; set; }`
- `public bool RenderDirectlyToMappedMemory { get; set; }`
- `public bool? UseAsyncFrontBufferBlit { get; set; }`

### `src/Linux/Avalonia.LinuxFramebuffer/Output/FbdevOutput.cs`
- `public string Id { get; private set; }`
- `public PixelSize PixelSize {`
- `public ILockedFramebuffer Lock() => Lock(out _);`
- `public IFramebufferRenderTarget CreateFramebufferRenderTarget() => new FuncRetainedFramebufferRenderTarget(Lock);`

### `src/Linux/Avalonia.LinuxFramebuffer/Output/IGlOutputBackend.cs`
- `public interface IGlOutputBackend : IOutputBackend`
- `public IPlatformGraphics PlatformGraphics { get; }`

### `src/Linux/Avalonia.LinuxFramebuffer/Output/IOutputBackend.cs`
- `public interface IOutputBackend`

### `src/Markup/Avalonia.Markup.Xaml.Loader/CompilerExtensions/Transformers/AvaloniaXamlIlControlTemplateTargetTypeMetadataTransformer.cs`
- `public enum ScopeTypes`

### `src/Markup/Avalonia.Markup.Xaml.Loader/CompilerExtensions/Transformers/AvaloniaXamlIlQueryTransformer.cs`
- `public enum QueryType`
- `public enum CombinatorQueryType`

### `src/Markup/Avalonia.Markup.Xaml.Loader/CompilerExtensions/Transformers/AvaloniaXamlIlSelectorTransformer.cs`
- `public enum SelectorType`
- `public enum CombinatorSelectorType`

### `src/Markup/Avalonia.Markup.Xaml/Converters/AvaloniaPropertyTypeConverter.cs`
- `public class AvaloniaPropertyTypeConverter : TypeConverter`

### `src/Markup/Avalonia.Markup.Xaml/Converters/AvaloniaUriTypeConverter.cs`
- `public class AvaloniaUriTypeConverter : TypeConverter`

### `src/Markup/Avalonia.Markup.Xaml/Converters/BitmapTypeConverter.cs`
- `public class BitmapTypeConverter : TypeConverter`

### `src/Markup/Avalonia.Markup.Xaml/Converters/ColorToBrushConverter.cs`
- `public class ColorToBrushConverter : IValueConverter`

### `src/Markup/Avalonia.Markup.Xaml/Converters/FontFamilyTypeConverter.cs`
- `public class FontFamilyTypeConverter : TypeConverter`

### `src/Markup/Avalonia.Markup.Xaml/Converters/IconTypeConverter.cs`
- `public class IconTypeConverter : TypeConverter`

### `src/Markup/Avalonia.Markup.Xaml/Converters/PointsListTypeConverter.cs`
- `public class PointsListTypeConverter : TypeConverter`

### `src/Markup/Avalonia.Markup.Xaml/Converters/TimeSpanTypeConverter.cs`
- `public class TimeSpanTypeConverter : TimeSpanConverter`

### `src/Markup/Avalonia.Markup.Xaml/Diagnostics/XamlSourceInfo.cs`
- `public Uri? SourceUri { get; }`
- `public int LineNumber { get; }`
- `public int LinePosition { get; }`
- `public static void SetXamlSourceInfo(object obj, XamlSourceInfo? info) {`
- `public static void SetXamlSourceInfo(IResourceDictionary dictionary, object key, XamlSourceInfo? info) {`

### `src/Markup/Avalonia.Markup.Xaml/MarkupExtension.cs`
- `public abstract class MarkupExtension`

### `src/Markup/Avalonia.Markup.Xaml/MarkupExtensions/CompiledBindings/CompiledBindingPath.cs`
- `public CompiledBindingPathBuilder ArrayElement(int[] indices, Type elementType) {`
- `public CompiledBindingPathBuilder TypeCast<T>() {`
- `public CompiledBindingPathBuilder SetRawSource(object? rawSource) {`

### `src/Markup/Avalonia.Markup.Xaml/MarkupExtensions/CompiledBindings/PropertyInfoAccessorFactory.cs`
- `public static class PropertyInfoAccessorFactory`
- `public static IPropertyAccessor CreateInpcPropertyAccessor(WeakReference<object?> target, IPropertyInfo property) => new InpcPropertyAccessor(target, property);`
- `public static IPropertyAccessor CreateAvaloniaPropertyAccessor(WeakReference<object?> target, IPropertyInfo property) => new AvaloniaPropertyAccessor(new WeakReference<AvaloniaObject?>((AvaloniaObject?)(target.TryGetTarget(out var o) ? o : null)), (AvaloniaProperty)property);`
- `public static IPropertyAccessor CreateIndexerPropertyAccessor(WeakReference<object?> target, IPropertyInfo property, int argument) => new IndexerAccessor(target, property, argument);`

### `src/Markup/Avalonia.Markup.Xaml/RuntimeXamlLoaderConfiguration.cs`
- `public delegate RuntimeXamlDiagnosticSeverity XamlDiagnosticFunc(RuntimeXamlDiagnostic diagnostic);`

### `src/Markup/Avalonia.Markup.Xaml/XamlIl/Runtime/IAvaloniaXamlIlControlTemplateProvider.cs`
- `public interface IAvaloniaXamlIlControlTemplateProvider`

### `src/Markup/Avalonia.Markup.Xaml/XamlIl/Runtime/IAvaloniaXamlIlXmlNamespaceInfoProviderV1.cs`
- `public interface IAvaloniaXamlIlXmlNamespaceInfoProvider`
- `public class AvaloniaXamlIlXmlNamespaceInfo`
- `public string ClrNamespace { get; set; } = string.Empty;`
- `public string ClrAssemblyName { get; set; } = string.Empty;`

### `src/Markup/Avalonia.Markup.Xaml/XamlIl/Runtime/XamlIlRuntimeHelpers.cs`
- `public static Func<IServiceProvider, object> DeferredTransformationFactoryV1(Func<IServiceProvider, object> builder, IServiceProvider provider) {`
- `public static Func<IServiceProvider, object> DeferredTransformationFactoryV2<T>(Func<IServiceProvider, object> builder, IServiceProvider provider) {`
- `public static unsafe IDeferredContent DeferredTransformationFactoryV3<T>( IntPtr builder, IServiceProvider provider) {`
- `public static IAvaloniaXamlIlEagerParentStackProvider AsEagerParentStackProvider( this IAvaloniaXamlIlParentStackProvider provider) => provider as IAvaloniaXamlIlEagerParentStackProvider ?? new XamlIlParentStackProviderWrapper(provider);`
- `public static void ApplyNonMatchingMarkupExtensionV1(object target, object property, IServiceProvider prov, object value) {`
- `public static IServiceProvider CreateInnerServiceProviderV1(IServiceProvider compiled) => new InnerServiceProvider(compiled);`

### `src/Markup/Avalonia.Markup.Xaml/XamlTypes.cs`
- `public sealed class ConstructorArgumentAttribute : Attribute`
- `public ConstructorArgumentAttribute(string name) {`

### `src/Markup/Avalonia.Markup/Data/BindingBase.cs`
- `public WeakReference? DefaultAnchor { get; set; }`

### `src/Skia/Avalonia.Skia/Gpu/ISkiaGpu.cs`
- `public interface ISkiaGpu : IPlatformGraphicsContext`
- `public interface ISkiaGpuWithPlatformGraphicsContext : ISkiaGpu`
- `public interface ISkiaSurface : IDisposable`

### `src/Skia/Avalonia.Skia/Gpu/ISkiaGpuRenderSession.cs`
- `public interface ISkiaGpuRenderSession : IDisposable`

### `src/Skia/Avalonia.Skia/Gpu/ISkiaGpuRenderTarget.cs`
- `public interface ISkiaGpuRenderTarget : IDisposable`
- `public interface ISkiaGpuRenderTarget2 : ISkiaGpuRenderTarget`

### `src/Skia/Avalonia.Skia/Gpu/OpenGl/IGlSkiaSpecificOptionsFeature.cs`
- `public interface IGlSkiaSpecificOptionsFeature`
- `public bool UseNativeSkiaGrGlInterface { get; }`

### `src/Skia/Avalonia.Skia/Helpers/DrawingContextHelper.cs`
- `public static IDrawingContextImpl WrapSkiaCanvas(SKCanvas canvas, Vector dpi) {`
- `public static bool TryCreateDashEffect(IPen? pen, [NotNullWhen(true)] out SKPathEffect? effect) {`

### `src/Skia/Avalonia.Skia/Helpers/ImageSavingHelper.cs`
- `public static class ImageSavingHelper`
- `public static void SaveImage(SKImage image, string fileName, int? quality = null) {`
- `public static void SaveImage(SKImage image, Stream stream, int? quality = null) {`

### `src/Skia/Avalonia.Skia/Helpers/PixelFormatHelper.cs`
- `public static class PixelFormatHelper`
- `public static SKColorType ResolveColorType(PixelFormat? format) {`

### `src/Skia/Avalonia.Skia/ISkiaSharpApiLeaseFeature.cs`
- `public interface ISkiaSharpApiLease : IDisposable`
- `public interface ISkiaSharpPlatformGraphicsApiLease : IDisposable`

### `src/Skia/Avalonia.Skia/SkiaPlatform.cs`
- `public static class SkiaPlatform`
- `public static Vector DefaultDpi => new Vector(96.0f, 96.0f);`

### `src/Skia/Avalonia.Skia/SkiaSharpExtensions.cs`
- `public static class SkiaSharpExtensions`
- `public static SKFilterQuality ToSKFilterQuality(this BitmapInterpolationMode interpolationMode) {`
- `public static SKBlendMode ToSKBlendMode(this BitmapBlendingMode blendingMode) {`
- `public static SKPoint ToSKPoint(this Point p) {`
- `public static SKPoint ToSKPoint(this Vector p) {`
- `public static SKRect ToSKRect(this Rect r) {`
- `public static SKRectI ToSKRectI(this PixelRect r) {`
- `public static SKRoundRect ToSKRoundRect(this RoundedRect r) {`
- `public static Rect ToAvaloniaRect(this SKRect r) {`
- `public static PixelRect ToAvaloniaPixelRect(this SKRectI r) {`
- `public static SKMatrix ToSKMatrix(this Matrix m) {`
- `public static SKColor ToSKColor(this Color c) {`
- `public static SKColorType ToSkColorType(this PixelFormat fmt) {`
- `public static PixelFormat? ToAvalonia(this SKColorType colorType) {`
- `public static PixelFormat ToPixelFormat(this SKColorType fmt) {`
- `public static SKAlphaType ToSkAlphaType(this AlphaFormat fmt) {`
- `public static AlphaFormat ToAlphaFormat(this SKAlphaType fmt) {`
- `public static SKShaderTileMode ToSKShaderTileMode(this GradientSpreadMethod m) {`
- `public static SKTextAlign ToSKTextAlign(this TextAlignment a) {`
- `public static SKStrokeCap ToSKStrokeCap(this PenLineCap cap) {`
- `public static SKStrokeJoin ToSKStrokeJoin(this PenLineJoin join) {`
- `public static TextAlignment ToAvalonia(this SKTextAlign a) {`
- `public static FontStyle ToAvalonia(this SKFontStyleSlant slant) {`
- `public static SKFontStyleSlant ToSkia(this FontStyle style) {`
- `public static SKPath? Clone(this SKPath? src) {`

### `src/Tizen/Avalonia.Tizen/NuiAvaloniaView.cs`
- `public class NuiAvaloniaView : GLView, ITizenView, ITextInputMethodImpl`
- `public IInputRoot InputRoot {`
- `public event Action? OnSurfaceInit;`
- `public NuiAvaloniaView() : base(ColorFormat.RGBA8888) {`
- `public void SetClient(TextInputMethodClient? client) {`
- `public void SetCursorRect(Rect rect) {`
- `public void SetOptions(TextInputOptions options) =>`

### `src/Tizen/Avalonia.Tizen/NuiAvaloniaViewTextEditable.cs`
- `public class NuiMultiLineTextInput : TextEditor, INuiTextInput`
- `public class NuiSingleLineTextInput : TextField, INuiTextInput`

### `src/Tizen/Avalonia.Tizen/NuiTizenApplication.cs`
- `public class NuiTizenApplication<TApp> : NUIApplication`

### `src/Tizen/Avalonia.Tizen/NuiViewControlHandle.cs`
- `public class NuiViewControlHandle : INativeControlHostDestroyableControlHandle`
- `public NuiViewControlHandle(View view) {`
- `public View View { get; set; }`
- `public IntPtr Handle => throw new NotSupportedException();`
- `public string? HandleDescriptor => ViewDescriptor;`
- `public void Destroy() => View.Dispose();`

### `src/Tizen/Avalonia.Tizen/TizenApplicationExtensions.cs`
- `public static class TizenApplicationExtensions`
- `public static AppBuilder UseTizen(this AppBuilder builder) {`

### `src/Windows/Avalonia.Direct2D1/Direct2D1Platform.cs`
- `public static class Direct2DApplicationExtensions`
- `public static AppBuilder UseDirect2D1(this AppBuilder builder) {`

### `src/Windows/Avalonia.Direct2D1/IExternalDirect2DRenderTargetSurface.cs`
- `public interface IExternalDirect2DRenderTargetSurface`

### `src/Windows/Avalonia.Win32.Interoperability/WinForms/WinFormsAvaloniaControlHost.cs`
- `public class WinFormsAvaloniaControlHost : WinFormsControl, IMessageFilter`
- `public WinFormsAvaloniaControlHost() {`
- `public bool PreFilterMessage(ref Message m) {`

### `src/Windows/Avalonia.Win32/AngleOptions.cs`
- `public class AngleOptions`
- `public enum PlatformApi`
- `public IList<PlatformApi>? AllowedPlatformApis { get; set; } = null;`

### `src/Windows/Avalonia.Win32/DirectX/IDirect3D11TexturePlatformSurface.cs`
- `public interface IDirect3D11TexturePlatformSurface`
- `public interface IDirect3D11TextureRenderTarget : IDisposable`
- `public interface IDirect3D11TextureRenderTargetRenderSession : IDisposable`
- `public IntPtr D3D11Texture2D { get; }`

### `src/Windows/Avalonia.Win32/Input/KeyInterop.cs`
- `public static class KeyInterop`
- `public static Key KeyFromVirtualKey(int virtualKey, int keyData) {`
- `public static int VirtualKeyFromKey(Key key) {`
- `public static PhysicalKey PhysicalKeyFromVirtualKey(int virtualKey, int keyData) {`
- `public static unsafe string? GetKeySymbol(int virtualKey, int keyData) {`

### `src/iOS/Avalonia.iOS/AvaloniaAppDelegate.cs`
- `public AvaloniaAppDelegate() {`
- `public bool FinishedLaunching(UIApplication application, NSDictionary launchOptions) {`
- `public bool OpenUrl(UIApplication app, NSUrl url, NSDictionary options) {`
- `public bool ContinueUserActivity(UIApplication application, NSUserActivity userActivity, UIApplicationRestorationHandler completionHandler) {`

### `src/iOS/Avalonia.iOS/AvaloniaView.Text.cs`
- `public override bool BecomeFirstResponder() {`
- `public override bool ResignFirstResponder() {`

### `src/iOS/Avalonia.iOS/AvaloniaView.cs`
- `public override bool CanBecomeFirstResponder => true;`
- `public override bool CanResignFirstResponder => true;`
- `public override void TraitCollectionDidChange(UITraitCollection? previousTraitCollection) {`
- `public override void TintColorDidChange() {`
- `public void InitWithController<TController>(TController controller) where TController : UIViewController, IAvaloniaViewController {`
- `public static Class LayerClass() {`
- `public override void TouchesBegan(NSSet touches, UIEvent? evt) => _input.Handle(touches, evt);`
- `public override void TouchesMoved(NSSet touches, UIEvent? evt) => _input.Handle(touches, evt);`
- `public override void TouchesEnded(NSSet touches, UIEvent? evt) => _input.Handle(touches, evt);`
- `public override void TouchesCancelled(NSSet touches, UIEvent? evt) => _input.Handle(touches, evt);`
- `public override void PressesBegan(NSSet<UIPress> presses, UIPressesEvent evt) {`
- `public override void PressesChanged(NSSet<UIPress> presses, UIPressesEvent evt) {`
- `public override void PressesEnded(NSSet<UIPress> presses, UIPressesEvent evt) {`
- `public override void PressesCancelled(NSSet<UIPress> presses, UIPressesEvent evt) {`
- `public override void LayoutSubviews() {`

### `src/iOS/Avalonia.iOS/NativeControlHostImpl.cs`
- `public class UIViewControlHandle : PlatformHandle, INativeControlHostDestroyableControlHandle`
- `public UIViewControlHandle(UIView view) : base(view.Handle.Handle, UIViewDescriptor) {`
- `public UIView View { get; }`
- `public void Destroy() {`

### `src/iOS/Avalonia.iOS/ViewController.cs`
- `public interface IAvaloniaViewController`
- `public class DefaultAvaloniaViewController : UIViewController, IAvaloniaViewController`
- `public override void ViewDidLayoutSubviews() {`
- `public override bool PrefersStatusBarHidden() {`
- `public override UIStatusBarStyle PreferredStatusBarStyle() {`
- `public Thickness SafeAreaPadding { get; private set; }`
- `public event EventHandler? SafeAreaPaddingChanged;`

### `src/tools/Avalonia.Analyzers/AvaloniaPropertyAnalyzer.CompileAnalyzer.cs`
- `public partial class AvaloniaPropertyAnalyzer`
- `public class CompileAnalyzer`
- `public CompileAnalyzer(CompilationStartAnalysisContext context, INamedTypeSymbol avaloniaObjectType) {`

### `src/tools/Avalonia.Analyzers/AvaloniaPropertyAnalyzer.cs`
- `public partial class AvaloniaPropertyAnalyzer : DiagnosticAnalyzer`
- `public override ImmutableArray<DiagnosticDescriptor> SupportedDiagnostics { get; } = ImmutableArray.Create(`
- `public class AvaloniaAnalysisException : Exception`
- `public AvaloniaAnalysisException(string message, Exception? innerException = null) : base(message, innerException) {`

### `src/tools/Avalonia.Analyzers/BitmapAnalyzer.cs`
- `public class BitmapAnalyzer: DiagnosticAnalyzer`
- `public const string DiagnosticId = "AVA2002";`
- `public override ImmutableArray<DiagnosticDescriptor> SupportedDiagnostics { get { return ImmutableArray.Create(_rule); } }`

### `src/tools/Avalonia.Analyzers/BitmapAnalyzerCSCodeFixProvider.cs`
- `public class BitmapAnalyzerCSCodeFixProvider : CodeFixProvider`
- `public override ImmutableArray<string> FixableDiagnosticIds { get; } =`
- `public override FixAllProvider? GetFixAllProvider() {`
- `public sealed override async Task RegisterCodeFixesAsync(CodeFixContext context) {`

### `src/tools/Avalonia.Analyzers/OnPropertyChangedOverrideAnalyzer.cs`
- `public class OnPropertyChangedOverrideAnalyzer : DiagnosticAnalyzer`
- `public const string DiagnosticId = "AVA2001";`
- `public override ImmutableArray<DiagnosticDescriptor> SupportedDiagnostics => ImmutableArray.Create(Rule);`

### `src/tools/Avalonia.Generators/NameGenerator/AvaloniaNameSourceGenerator.cs`
- `public class AvaloniaNameSourceGenerator : ISourceGenerator`

### `src/tools/DevAnalyzers/GenericVirtualAnalyzer.cs`
- `public class GenericVirtualAnalyzer : DiagnosticAnalyzer`
- `public const string DiagnosticId = "AVADEV1001";`
- `public override ImmutableArray<DiagnosticDescriptor> SupportedDiagnostics => ImmutableArray.Create(Rule);`

### `src/tools/DevAnalyzers/OnPropertyChangedOverrideAnalyzer.cs`
- `public class OnPropertyChangedOverrideAnalyzer : DiagnosticAnalyzer`
- `public const string DiagnosticId = "AVADEV2001";`
- `public override ImmutableArray<DiagnosticDescriptor> SupportedDiagnostics => ImmutableArray.Create(Rule);`

### `src/tools/DevGenerators/CompilerDynamicDependenciesGenerator.cs`
- `public class CompilerDynamicDependenciesGenerator : IIncrementalGenerator`

### `src/tools/DevGenerators/CompositionGenerator/CompositionRoslynGenerator.cs`
- `public class CompositionRoslynGenerator : IIncrementalGenerator`

### `src/tools/DevGenerators/CompositionGenerator/Config.cs`
- `public class GConfig`
- `public List<GUsing> Usings { get; set; } = new List<GUsing>();`
- `public List<GManualClass> ManualClasses { get; set; } = new List<GManualClass>();`
- `public List<GAnimationType> KeyFrameAnimations { get; set; } = new List<GAnimationType>();`
- `public class GUsing`
- `public class GManualClass`
- `public bool Passthrough { get; set; }`
- `public string ServerName { get; set; }`
- `public class GImplements`
- `public class GClass`
- `public string ChangesBase { get; set; }`
- `public string ServerBase { get; set; }`
- `public bool CustomCtor { get; set; }`
- `public bool CustomServerCtor { get; set; }`
- `public bool ServerOnly { get; set; }`
- `public List<GImplements> Implements { get; set; } = new List<GImplements>();`
- `public class GBrush : GClass`
- `public bool CustomUpdate { get; set; }`
- `public GBrush() {`
- `public class GList : GClass`
- `public class GProperty`
- `public string ClientName { get; set; }`
- `public string DefaultValue { get; set; }`
- `public bool Animated { get; set; }`
- `public bool InternalSet { get; set; }`
- `public bool Private { get; set; }`
- `public class GAnimationType`

### `src/tools/DevGenerators/CompositionGenerator/Extensions.cs`
- `public static ClassDeclarationSyntax AddModifiers(this ClassDeclarationSyntax cl, params SyntaxKind[]? modifiers) {`
- `public static MethodDeclarationSyntax AddModifiers(this MethodDeclarationSyntax cl, params SyntaxKind[]? modifiers) {`
- `public static PropertyDeclarationSyntax AddModifiers(this PropertyDeclarationSyntax cl, params SyntaxKind[]? modifiers) {`
- `public static ConstructorDeclarationSyntax AddModifiers(this ConstructorDeclarationSyntax cl, params SyntaxKind[]? modifiers) {`
- `public static AccessorDeclarationSyntax AddModifiers(this AccessorDeclarationSyntax cl, params SyntaxKind[]? modifiers) {`
- `public static EnumDeclarationSyntax AddModifiers(this EnumDeclarationSyntax cl, params SyntaxKind[]? modifiers) {`
- `public static string WithLowerFirst(this string s) {`
- `public static ExpressionSyntax MemberAccess(params string[]? identifiers) {`
- `public static ExpressionSyntax MemberAccess(ExpressionSyntax expr, params string[] identifiers) {`
- `public static MemberAccessExpressionSyntax MemberAccess(ExpressionSyntax expr, string identifier) =>`
- `public static ExpressionSyntax ConditionalMemberAccess(ExpressionSyntax expr, string member, bool checkNull) {`
- `public static ClassDeclarationSyntax WithBaseType(this ClassDeclarationSyntax cl, string bt) {`
- `public static string StripPrefix(this string s, string prefix) => string.IsNullOrEmpty(s)`

### `src/tools/DevGenerators/CompositionGenerator/Generator.cs`
- `public Generator(ICompositionGeneratorSink output, GConfig config) {`
- `public void Generate() {`

### `src/tools/DevGenerators/CompositionGenerator/ICompositionGeneratorSink.cs`
- `public interface ICompositionGeneratorSink`

### `src/tools/DevGenerators/EnumMemberDictionaryGenerator.cs`
- `public class EnumMemberDictionaryGenerator : IIncrementalGenerator`

### `src/tools/DevGenerators/GetProcAddressInitialization.cs`
- `public class GetProcAddressInitializationGenerator : IIncrementalGenerator`

### `src/tools/DevGenerators/SubtypesFactoryGenerator.cs`
- `public class SubtypesFactoryGenerator : IIncrementalGenerator`

### `src/tools/DevGenerators/X11AtomsGenerator.cs`
- `public class X11AtomsGenerator : IIncrementalGenerator`
