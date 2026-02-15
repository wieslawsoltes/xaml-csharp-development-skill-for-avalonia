# Runtime XAML Manipulation and Service Provider Patterns

## Table of Contents
1. Scope and APIs
2. Manipulation Layers in Avalonia
3. Pre-Load XAML Mutation
4. Load into Existing Objects
5. Runtime Graph Updates After Load
6. `IServiceProvider` Patterns in Markup Extensions
7. Source Mapping and Diagnostics Metadata
8. Limits and Non-Public Internals
9. Troubleshooting

## Scope and APIs

Primary APIs:
- `AvaloniaRuntimeXamlLoader.Load(...)`
- `AvaloniaRuntimeXamlLoader.LoadGroup(...)`
- `RuntimeXamlLoaderDocument`
- `RuntimeXamlLoaderConfiguration`
- `IProvideValueTarget`
- `IRootObjectProvider`
- `IUriContext`
- `IXamlTypeResolver`
- `IAvaloniaXamlIlParentStackProvider`
- `IAvaloniaXamlIlEagerParentStackProvider`
- `XamlSourceInfo`

Reference source files:
- `src/Markup/Avalonia.Markup.Xaml/RuntimeXamlLoaderDocument.cs`
- `src/Markup/Avalonia.Markup.Xaml/RuntimeXamlLoaderConfiguration.cs`
- `src/Markup/Avalonia.Markup.Xaml.Loader/AvaloniaRuntimeXamlLoader.cs`
- `src/Markup/Avalonia.Markup.Xaml/XamlTypes.cs`
- `src/Markup/Avalonia.Markup.Xaml/XamlIl/Runtime/IAvaloniaXamlIlParentStackProvider.cs`
- `src/Markup/Avalonia.Markup.Xaml/XamlIl/Runtime/XamlIlRuntimeHelpers.cs`
- `src/Markup/Avalonia.Markup.Xaml/Diagnostics/XamlSourceInfo.cs`
- `tests/Avalonia.Markup.Xaml.UnitTests/Xaml/XamlSourceInfoTests.cs`

## Manipulation Layers in Avalonia

Use three explicit layers:
1. Pre-load text/XML mutation.
2. Load-time behavior (`RootInstance`, `BaseUri`, diagnostics config).
3. Post-load object graph updates (controls, resources, bindings).

There is no supported public API for injecting custom XamlIl AST transformers from application code.

## Pre-Load XAML Mutation

For dynamic scenarios, mutate XAML text before calling runtime loader.

```csharp
using System.Xml.Linq;
using Avalonia.Markup.Xaml;

var doc = XDocument.Parse(rawXaml);

// Example: mutate root attributes based on plugin settings.
doc.Root?.SetAttributeValue("Opacity", "0.8");

var loaded = AvaloniaRuntimeXamlLoader.Load(doc.ToString());
```

Use this when plugin metadata or feature flags must alter markup before load.

## Load into Existing Objects

`RootInstance` lets you populate an existing object instead of constructing a new one.

```csharp
using Avalonia.Markup.Xaml;

var existing = new MyControl();

var runtimeDoc = new RuntimeXamlLoaderDocument(
    baseUri: new Uri("avares://MyPlugin/Views/MyControl.axaml"),
    rootInstance: existing,
    xaml: xamlText)
{
    Document = "/plugins/MyControl.axaml"
};

AvaloniaRuntimeXamlLoader.Load(runtimeDoc, new RuntimeXamlLoaderConfiguration
{
    LocalAssembly = typeof(MyControl).Assembly,
    UseCompiledBindingsByDefault = true
});
```

This pattern is useful for hot-reload-like replacement without replacing the outer object identity.

## Runtime Graph Updates After Load

After load, manipulate standard Avalonia object graph APIs:
- replace resources in `ResourceDictionary`,
- update styles/templates at root/theme scope,
- apply state values on loaded controls.

For include-heavy runtime sets, prefer `LoadGroup` so cross-document references resolve consistently in one pass.

## `IServiceProvider` Patterns in Markup Extensions

Custom markup extensions can inspect loader context through public services.

```csharp
using System;
using Avalonia.Markup.Xaml;

public sealed class DebugContextExtension
{
    public object? ProvideValue(IServiceProvider serviceProvider)
    {
        var target = (IProvideValueTarget?)serviceProvider.GetService(typeof(IProvideValueTarget));
        var root = (IRootObjectProvider?)serviceProvider.GetService(typeof(IRootObjectProvider));
        var uri = (IUriContext?)serviceProvider.GetService(typeof(IUriContext));

        return $"Target={target?.TargetObject?.GetType().Name}; " +
               $"Root={root?.RootObject?.GetType().Name}; " +
               $"BaseUri={uri?.BaseUri}";
    }
}
```

Context services are particularly useful when extension behavior depends on target property or root scope.

## Source Mapping and Diagnostics Metadata

For runtime tooling/debugging:
- set `RuntimeXamlLoaderDocument.Document`,
- set `RuntimeXamlLoaderConfiguration.CreateSourceInfo = true`.

Then inspect `XamlSourceInfo` on loaded objects for file/line mapping.

```csharp
using Avalonia.Markup.Xaml.Diagnostics;

var info = XamlSourceInfo.GetXamlSourceInfo(loadedControl);
```

## Limits and Non-Public Internals

Not intended as app-level extension points:
- `AvaloniaXamlIlCompiler` and transformer pipeline classes,
- internal helper extension methods in `Avalonia.Markup.Xaml.Extensions`,
- internal runtime compiler backend types.

For app/library code, stay on public runtime loader, markup extension interfaces, and standard control/resource APIs.

## Troubleshooting

1. Custom markup extension cannot find context service
- Service may be unavailable for that target phase; handle null and provide fallback.

2. Relative include paths fail in runtime documents
- Ensure `RuntimeXamlLoaderDocument.BaseUri` is set.

3. Source info missing
- Set `CreateSourceInfo=true` and provide `Document` path.

4. Runtime manipulations break bindings/styles
- Apply changes at correct scope (control vs style/resource root) and avoid replacing objects blindly.

5. Need deep compile pipeline customization
- Public API does not expose AST transformer injection; preprocess XAML text or build custom tooling pipeline externally.
