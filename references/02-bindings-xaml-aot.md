# Bindings, XAML, and AOT Compatibility

## Core Rule

Default to precompiled XAML + compiled bindings. Treat reflection-based or runtime-loaded paths as explicit exceptions.

## XAML Loading Modes

### Production path

- Use precompiled XAML with generated `InitializeComponent()`.
- `AvaloniaXamlLoader.Load(this)` is expected through generated initialization wiring.

### Dynamic/runtime path

- `AvaloniaXamlLoader.Load(Uri, ...)` and runtime loaders (`AvaloniaRuntimeXamlLoader`) are dynamic paths.
- These paths are annotated with `RequiresUnreferencedCode` and are not default-safe for trim/AOT workflows.

Use runtime loaders only when the feature explicitly requires dynamic XAML (plugin/theme editor-like scenarios).

## Binding Families

For detailed converter guidance (single-value/multi-value, XAML resources, function-based converters, and binding wiring), see:
- [`45-value-converters-single-multi-and-binding-wiring.md`](45-value-converters-single-multi-and-binding-wiring)

For advanced typed/untyped binding value semantics (`BindingValue<T>`, `BindingNotification`, `InstancedBinding`, `IndexerDescriptor`), see:
- [`46-binding-value-notification-and-instanced-binding-semantics.md`](46-binding-value-notification-and-instanced-binding-semantics)

For `RelativeSource`, `StaticResource`, and name-scope resolution markup (`ResolveByNameExtension`), see:
- [`50-relative-static-resource-and-name-resolution-markup.md`](50-relative-static-resource-and-name-resolution-markup)

Advanced binding-assignment contract:
- `AssignBindingAttribute` marks members where a binding object should be assigned instead of initiating a live binding.

### Compiled bindings (preferred)

Primary APIs:
- XAML: `{CompiledBinding ...}` with `x:DataType`
- C#: `CompiledBinding`, `CompiledBindingPath`, `CompiledBindingPathBuilder`

Benefits:
- Better performance and type safety.
- Better compatibility posture than reflection-based binding paths.

### Reflection bindings (fallback)

Primary APIs:
- `{Binding ...}` from `Avalonia.Markup.Data.Binding` (inherits reflection binding behavior)
- `{ReflectionBinding ...}` explicit extension
- `ReflectionBinding`

Tradeoffs:
- Annotated for unreferenced/dynamic code usage.
- More fragile for aggressive trimming and NativeAOT.

## Required XAML Patterns for Typed/Compiled Binding

1. Set `x:DataType` on root views and templates.
2. Use `{CompiledBinding ...}` where practical.
3. Keep property and command names strongly aligned with viewmodel contracts.

Example:

```xml
<UserControl xmlns="https://github.com/avaloniaui"
             xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
             xmlns:vm="using:MyApp.ViewModels"
             x:Class="MyApp.Views.MainView"
             x:DataType="vm:MainViewModel">
  <StackPanel Spacing="8">
    <TextBox Text="{CompiledBinding Query, Mode=TwoWay}" />
    <Button Content="Search" Command="{CompiledBinding SearchCommand}" />
    <TextBlock Text="{CompiledBinding StatusText}" />
  </StackPanel>
</UserControl>
```

## Compiled Binding Features to Use Deliberately

Path capabilities (through grammar/builders):
- Property and nested property access.
- Indexers.
- Element/ancestor/self/templated-parent source selection.
- Stream/task projection (`^` operator in XAML path syntax).

Example stream binding in XAML:

```xml
<TextBlock Text="{CompiledBinding ClockObservable^, Mode=OneWay}" />
```

## C# Binding APIs

### Bind with a `BindingBase`

```csharp
textBlock.Bind(TextBlock.TextProperty,
    new CompiledBinding(new CompiledBindingPathBuilder()
        .Property(/* generated property info */)
        .Build()));
```

### Bind from observables directly

```csharp
IDisposable sub = textBlock.Bind(
    TextBlock.TextProperty,
    viewModel.StatusStream);
```

### Convert observable to binding object

```csharp
textBlock.Bind(TextBlock.TextProperty, viewModel.StatusStream.ToBinding());
```

## AOT Guidance for C#-Only UI

- Prefer direct property assignment and observable binding over runtime expression parsing.
- Be cautious with expression/lambda-based helper APIs that are annotated for dynamic code.
- Favor APIs that do not depend on runtime reflection discovery.

## `DataTemplate` and `DataType`

`DataTemplates` collections require typed templates in shared/global contexts.

Use:
- `DataTemplate x:DataType="..."`
- `TreeDataTemplate x:DataType="..."`
- `FuncDataTemplate` for C# template construction when needed.

## Name Generator and Typed `x:Name`

Generator options (from `Avalonia.Generators.props`):
- `AvaloniaNameGeneratorBehavior`
- `AvaloniaNameGeneratorDefaultFieldModifier`
- `AvaloniaNameGeneratorFilterByPath`
- `AvaloniaNameGeneratorFilterByNamespace`

Use:
- Keep views partial.
- Let generated component initialization and typed names eliminate repeated manual name lookups.

## Binding Error Hygiene

- Set fallback/null handling deliberately (`FallbackValue`, `TargetNullValue`, `StringFormat`).
- For form scenarios, pair binding mode/update trigger with UX requirements.
- Use explicit reflection binding only where compiled path is not feasible.

## Advanced Binding Result Semantics

When debugging or building advanced binding flows, use these APIs deliberately:
- typed path: `BindingValue<T>` + `BindingValueType`,
- untyped path: `BindingNotification` + `BindingErrorType`,
- state bridging: `BindingValue<T>.FromUntyped(...)`, `ToUntyped()`, `ToOptional()`,
- expression inspection: `BindingOperations.GetBindingExpressionBase(...)`.

State mapping you should rely on:
- `BindingValue<T>.Unset` maps to `AvaloniaProperty.UnsetValue`,
- `BindingValue<T>.DoNothing` maps to `BindingOperations.DoNothing`,
- `BindingError` / `DataValidationError` can carry fallback values,
- `BindingNotification` can carry both error metadata and a fallback/passthrough value.

Example: inspect typed binding stream safely.

```csharp
using Avalonia;
using Avalonia.Data;

IDisposable sub = textBox
    .GetBindingObservable(TextBox.TextProperty)
    .Subscribe(v =>
    {
        switch (v.Type)
        {
            case BindingValueType.Value:
                viewModel.LastValidText = v.GetValueOrDefault() ?? string.Empty;
                break;
            case BindingValueType.DataValidationError:
            case BindingValueType.BindingError:
                viewModel.LastBindingError = v.Error?.Message;
                break;
            case BindingValueType.UnsetValue:
                // Target will fall back to the property's unbound/default behavior.
                break;
            case BindingValueType.DoNothing:
                // Preserve current target state.
                break;
        }
    });
```

Example: explicit source update for `UpdateSourceTrigger=Explicit`.

```csharp
var expr = BindingOperations.GetBindingExpressionBase(textBox, TextBox.TextProperty);
expr?.UpdateSource();
```

## Instanced and Indexer Binding APIs (Advanced)

Advanced app code occasionally needs:
- `InstancedBinding` factory helpers (`OneWay`, `TwoWay`, `OneTime`, `OneWayToSource`),
- `IndexerDescriptor` (`!property` / `~property` operator paths) for concise property-indexer binding wiring.

Compatibility note:
- `IBinding.Initiate(...)` and `BindingOperations.Apply(...)` are obsolete compatibility paths in Avalonia 11.3.12 and are not recommended for new app code.

These APIs are useful for dynamic binding infrastructure and diagnostics tooling, not as default app authoring style. Prefer normal XAML binding syntax unless you need dynamic composition.

## Anti-Patterns

1. Global use of `{Binding ...}` without `x:DataType` in large apps.
2. Runtime XAML loading for normal app startup.
3. Mixed implicit/explicit DataContext contracts with no typed binding boundary.
4. Repeatedly switching between compiled and reflection binding styles in one view tree.

## XAML-First and Code-Only Usage

Default mode:
- Use compiled XAML + compiled bindings first.
- Provide code-only binding trees only when requested.

XAML-first complete example:

```xml
<UserControl xmlns="https://github.com/avaloniaui"
             xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
             xmlns:vm="using:MyApp.ViewModels"
             x:Class="MyApp.Views.SearchView"
             x:DataType="vm:SearchViewModel">
  <StackPanel Margin="16" Spacing="8">
    <TextBox Watermark="Query"
             Text="{CompiledBinding Query, Mode=TwoWay, UpdateSourceTrigger=PropertyChanged}" />
    <Button Content="Search" Command="{CompiledBinding SearchCommand}" />
    <TextBlock Text="{CompiledBinding StatusText}" />
  </StackPanel>
</UserControl>
```

```csharp
using Avalonia.Controls;
using Avalonia.Markup.Xaml;

namespace MyApp.Views;

public partial class SearchView : UserControl
{
    public SearchView() => InitializeComponent();

    private void InitializeComponent() => AvaloniaXamlLoader.Load(this);
}
```

Code-only alternative (on request):

```csharp
using Avalonia;
using Avalonia.Controls;
using Avalonia.Data;

var panel = new StackPanel { Margin = new Thickness(16), Spacing = 8 };
var input = new TextBox { Watermark = "Query" };
input.Bind(TextBox.TextProperty, new Binding(nameof(SearchViewModel.Query))
{
    Mode = BindingMode.TwoWay,
    UpdateSourceTrigger = UpdateSourceTrigger.PropertyChanged
});

var run = new Button { Content = "Search" };
run.Bind(Button.CommandProperty, new Binding(nameof(SearchViewModel.SearchCommand)));

var status = new TextBlock();
status.Bind(TextBlock.TextProperty, new Binding(nameof(SearchViewModel.StatusText)));

panel.Children.Add(input);
panel.Children.Add(run);
panel.Children.Add(status);
```
