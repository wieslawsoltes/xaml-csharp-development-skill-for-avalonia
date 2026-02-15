# Runtime XAML Loader and Dynamic Loading

## Table of Contents
1. Scope and APIs
2. Loader Choices
3. `RuntimeXamlLoaderDocument` and Configuration
4. Loading Multiple Documents (`LoadGroup`)
5. Diagnostics and Severity Control
6. Trimming/AOT Tradeoffs
7. Practical Patterns
8. Troubleshooting

## Scope and APIs

Primary APIs:
- `AvaloniaXamlLoader.Load(object)`
- `AvaloniaXamlLoader.Load(IServiceProvider?, Uri, Uri?)`
- `AvaloniaRuntimeXamlLoader.Load(...)`
- `AvaloniaRuntimeXamlLoader.LoadGroup(...)`
- `AvaloniaRuntimeXamlLoader.Parse(...)`
- `RuntimeXamlLoaderDocument`
- `RuntimeXamlLoaderConfiguration`
- `RuntimeXamlDiagnostic`
- `RuntimeXamlDiagnosticSeverity`

Reference source files:
- `src/Markup/Avalonia.Markup.Xaml/AvaloniaXamlLoader.cs`
- `src/Markup/Avalonia.Markup.Xaml.Loader/AvaloniaRuntimeXamlLoader.cs`
- `src/Markup/Avalonia.Markup.Xaml/RuntimeXamlLoaderDocument.cs`
- `src/Markup/Avalonia.Markup.Xaml/RuntimeXamlLoaderConfiguration.cs`
- `src/Markup/Avalonia.Markup.Xaml.Loader/AvaloniaXamlIlRuntimeCompiler.cs`
- `src/Markup/Avalonia.Markup.Xaml.Loader/CompilerExtensions/AvaloniaXamlDiagnosticCodes.cs`

## Loader Choices

### Compiled app path (default)

- Use generated `InitializeComponent()` calling `AvaloniaXamlLoader.Load(this)`.
- This expects precompiled XAML.

If no compiled XAML exists for the type, `AvaloniaXamlLoader.Load(this)` throws `XamlLoadException`.

### URI-based dynamic path

`AvaloniaXamlLoader.Load(Uri, ...)` tries:
1. compiled dispatcher `CompiledAvaloniaXaml.!XamlLoader.TryLoad(...)`,
2. runtime loader fallback (`IRuntimeXamlLoader`) if registered.

The runtime fallback path is primarily intended for tests/infrastructure, not normal app startup.

### Explicit runtime compile/load path

`AvaloniaRuntimeXamlLoader` compiles and loads XAML at runtime from:
- string,
- stream,
- `RuntimeXamlLoaderDocument`,
- grouped documents (`LoadGroup`).

## `RuntimeXamlLoaderDocument` and Configuration

`RuntimeXamlLoaderDocument` supports:
- `BaseUri` for URI resolution,
- `Document` path for diagnostics/source info,
- `RootInstance` to populate an existing instance,
- `XamlStream`,
- `ServiceProvider` parent provider.

`RuntimeXamlLoaderConfiguration` controls:
- `LocalAssembly` for `clr-namespace:` lookup,
- `UseCompiledBindingsByDefault`,
- `DesignMode`,
- `CreateSourceInfo`,
- `DiagnosticHandler` severity override callback.

Example:

```csharp
using Avalonia.Markup.Xaml;

var doc = new RuntimeXamlLoaderDocument(
    new Uri("avares://MyPlugin/Views/EditorView.axaml"),
    xamlText)
{
    Document = "/plugins/editor/EditorView.axaml"
};

var view = (object)AvaloniaRuntimeXamlLoader.Load(
    doc,
    new RuntimeXamlLoaderConfiguration
    {
        LocalAssembly = typeof(MyPluginMarker).Assembly,
        UseCompiledBindingsByDefault = true,
        CreateSourceInfo = true
    });
```

## Loading Multiple Documents (`LoadGroup`)

`LoadGroup` resolves references among in-memory documents (including relative `Source` paths), which is useful for plugin packs or hot reload batches.

```csharp
using Avalonia.Markup.Xaml;

var docs = new[]
{
    new RuntimeXamlLoaderDocument(new Uri("avares://Plugin/Styles/Base.axaml"), styleXaml),
    new RuntimeXamlLoaderDocument(new Uri("avares://Plugin/Views/Main.axaml"), viewXaml)
};

var loaded = AvaloniaRuntimeXamlLoader.LoadGroup(docs);
// loaded[i] aligns with docs[i]
```

## Diagnostics and Severity Control

Runtime diagnostics are surfaced through `DiagnosticHandler`.

```csharp
var diagnostics = new List<RuntimeXamlDiagnostic>();

var cfg = new RuntimeXamlLoaderConfiguration
{
    DiagnosticHandler = d =>
    {
        diagnostics.Add(d);

        // Escalate warnings to errors in strict mode.
        if (d.Severity == RuntimeXamlDiagnosticSeverity.Warning)
            return RuntimeXamlDiagnosticSeverity.Error;

        return d.Severity;
    }
};
```

Diagnostic IDs map to Avalonia codes (`AVLNxxxx`) from compiler diagnostics.

## Trimming/AOT Tradeoffs

Dynamic loader APIs are annotated with `RequiresUnreferencedCode` and should be treated as opt-in runtime features.

Risky paths for trim/AOT:
- runtime XAML parsing/compilation,
- URI runtime loading when not resolved by compiled dispatcher,
- reflection-heavy binding paths.

Prefer compiled XAML + compiled bindings for startup and core UX surfaces.

## Practical Patterns

### Populate an existing instance

```csharp
var existing = new MyUserControl();
var doc = new RuntimeXamlLoaderDocument(rootInstance: existing, xaml: xamlText);
AvaloniaRuntimeXamlLoader.Load(doc);
```

### Parse strongly typed objects

```csharp
var style = AvaloniaRuntimeXamlLoader.Parse<Avalonia.Styling.Style>(xamlText);
```

### Resolve relative includes

Set `BaseUri` on each document when using relative `Source` in includes.

## Troubleshooting

1. `XamlLoadException` from `AvaloniaXamlLoader.Load(this)`
- Compiled XAML missing for that type/resource.

2. `clr-namespace` type not found
- Set `RuntimeXamlLoaderConfiguration.LocalAssembly`.

3. Relative include resolution fails
- Missing/incorrect `RuntimeXamlLoaderDocument.BaseUri`.

4. Runtime loader behaves differently from compiled startup
- Check `UseCompiledBindingsByDefault`, `DesignMode`, and document group context.

5. Trim/AOT warnings appear
- Move feature to compiled XAML path or isolate dynamic loading behind explicit runtime-only module boundaries.
