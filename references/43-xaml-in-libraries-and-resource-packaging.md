# XAML in Libraries and Resource Packaging

## Table of Contents
1. Scope and APIs
2. Packaging Rules for Library XAML
3. URI Rules and Path Resolution
4. Include Semantics (`StyleInclude`, `ResourceInclude`, `MergeResourceInclude`)
5. Cross-Assembly Include Resolution
6. XML Namespace Mapping for Library Controls
7. Visibility and Reachability
8. Recommended Library Layout
9. Troubleshooting

## Scope and APIs

Primary APIs and build parts:
- `AvaloniaXaml` / `AvaloniaResource` item groups
- `GenerateAvaloniaResourcesTask`
- `AvaloniaXamlLoader.Load(Uri, ...)`
- `StyleInclude`
- `ResourceInclude`
- `MergeResourceInclude`
- `XmlnsDefinitionAttribute`
- `XmlnsPrefixAttribute`

Reference source files:
- `packages/Avalonia/AvaloniaBuildTasks.props`
- `packages/Avalonia/AvaloniaBuildTasks.targets`
- `src/Avalonia.Build.Tasks/GenerateAvaloniaResourcesTask.cs`
- `src/Avalonia.Build.Tasks/XamlCompilerTaskExecutor.Helpers.cs`
- `src/Markup/Avalonia.Markup.Xaml/Styling/StyleInclude.cs`
- `src/Markup/Avalonia.Markup.Xaml/Styling/ResourceInclude.cs`
- `src/Markup/Avalonia.Markup.Xaml/Styling/MergeResourceInclude.cs`
- `src/Markup/Avalonia.Markup.Xaml.Loader/CompilerExtensions/GroupTransformers/XamlIncludeGroupTransformer.cs`
- `src/Markup/Avalonia.Markup.Xaml.Loader/CompilerExtensions/GroupTransformers/XamlMergeResourceGroupTransformer.cs`
- `src/Avalonia.Base/Metadata/XmlnsDefinitionAttribute.cs`
- `src/Avalonia.Base/Metadata/XmlnsPrefixAttribute.cs`

## Packaging Rules for Library XAML

Library baseline:
- Keep reusable views/themes as `AvaloniaXaml`.
- Keep non-XAML assets as `AvaloniaResource`.

By default, `*.axaml` and `*.paml` are discovered as `AvaloniaXaml` when default items are enabled.

During build:
- resources are packed into embedded `!AvaloniaResources`,
- each resource gets an `avares://AssemblyName/path` URI.

## URI Rules and Path Resolution

Canonical absolute form:
- `avares://MyLibrary/Themes/Colors.axaml`

Supported relative include forms (resolved from current document URI):
- `Style.xaml`
- `./Style.xaml`
- `../Style.xaml`
- `/Style.xaml`

In grouped runtime documents (`LoadGroup`), relative resolution depends on each document `BaseUri`.

## Include Semantics (`StyleInclude`, `ResourceInclude`, `MergeResourceInclude`)

### `StyleInclude` / `ResourceInclude`

When source is compile-resolvable (`avares://` or relative URI), compiler group transforms replace include nodes with direct compiled references.

At runtime (dynamic path), includes can still load via `AvaloniaXamlLoader.Load(...)`.

### `MergeResourceInclude`

Special behavior:
- merged at compile time into parent `ResourceDictionary`,
- source must resolve to another `ResourceDictionary`,
- when mixed with other `MergedDictionaries`, `MergeResourceInclude` should be last in declaration order.

If include shape/source is invalid, compiler reports transform diagnostics.

## Cross-Assembly Include Resolution

For external assembly includes, compiler attempts:
1. `CompiledAvaloniaXaml.!AvaloniaResources` public `Build:<path>` method,
2. public type fallback (usually `x:Class` type) matching expected loaded type.

If neither exists or types mismatch, compile-time transform error is produced.

Implication for library authors:
- include targets must be publicly reachable if they are consumed cross-assembly through include transforms.

## XML Namespace Mapping for Library Controls

Expose controls with assembly attributes:

```csharp
using Avalonia.Metadata;

[assembly: XmlnsDefinition("https://github.com/avaloniaui", "MyLibrary.Controls")]
[assembly: XmlnsPrefix("https://github.com/avaloniaui", "mylib")]
```

Then consumers can use:

```xml
xmlns:mylib="https://github.com/avaloniaui"
```

## Visibility and Reachability

`x:ClassModifier` and CLR visibility matter:
- public class/build paths are reachable by dispatcher-based URI loading,
- non-public types can become unreachable for runtime URI dispatch (`AVLN3001` warning path).

Use non-public XAML classes only when you do not need runtime URI-based construction from other assemblies.

## Recommended Library Layout

```xml
<Project Sdk="Microsoft.NET.Sdk">
  <PropertyGroup>
    <EnableAvaloniaXamlCompilation>true</EnableAvaloniaXamlCompilation>
    <AvaloniaUseCompiledBindingsByDefault>true</AvaloniaUseCompiledBindingsByDefault>
  </PropertyGroup>

  <ItemGroup>
    <AvaloniaXaml Include="Themes/**/*.axaml" />
    <AvaloniaResource Include="Assets/**" />
  </ItemGroup>
</Project>
```

Example consumer usage:

```xml
<Application.Styles>
  <StyleInclude Source="avares://MyLibrary/Themes/LibraryTheme.axaml" />
</Application.Styles>
```

## Troubleshooting

1. Include cannot resolve external file
- Wrong assembly name/path in `avares://...` URI.

2. Relative include fails in runtime grouping
- Missing `BaseUri` on documents.

3. Merge include errors
- Target is not a `ResourceDictionary`, or order/source is invalid.

4. Library controls not visible in XAML
- Missing `XmlnsDefinition` mapping or incorrect CLR namespace.

5. URI runtime loading cannot construct type
- Resource/type not publicly reachable for dispatcher path.
