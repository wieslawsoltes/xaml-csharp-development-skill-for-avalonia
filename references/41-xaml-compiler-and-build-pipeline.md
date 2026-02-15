# XAML Compiler and Build Pipeline

## Table of Contents
1. Scope and APIs
2. Build Inputs and Item Groups
3. Target Flow in Build
4. What the XAML Compiler Emits
5. Directives that Affect Compilation
6. Generated Runtime Dispatcher
7. Diagnostics and Source Info
8. Name Generator Integration
9. Recommended Project Baseline
10. Troubleshooting

## Scope and APIs

Primary APIs and build knobs:
- `EnableAvaloniaXamlCompilation`
- `AvaloniaUseCompiledBindingsByDefault`
- `AvaloniaXamlCreateSourceInfo`
- `AvaloniaXamlVerboseExceptions`
- `AvaloniaXamlIlVerifyIl`
- `CompileAvaloniaXamlTask`
- `XamlCompilerTaskExecutor`
- `AvaloniaXamlIlCompiler`

Reference source files:
- `packages/Avalonia/AvaloniaBuildTasks.props`
- `packages/Avalonia/AvaloniaBuildTasks.targets`
- `src/Avalonia.Build.Tasks/CompileAvaloniaXamlTask.cs`
- `src/Avalonia.Build.Tasks/XamlCompilerTaskExecutor.cs`
- `src/Avalonia.Build.Tasks/XamlCompilerTaskExecutor.Helpers.cs`
- `src/Avalonia.Build.Tasks/GenerateAvaloniaResourcesTask.cs`
- `src/Markup/Avalonia.Markup.Xaml.Loader/CompilerExtensions/AvaloniaXamlIlCompiler.cs`
- `src/Markup/Avalonia.Markup.Xaml.Loader/CompilerExtensions/AvaloniaXamlDiagnosticCodes.cs`
- `src/tools/Avalonia.Generators/Avalonia.Generators.props`
- `src/tools/Avalonia.Generators/NameGenerator/AvaloniaNameIncrementalGenerator.cs`

## Build Inputs and Item Groups

Avalonia package targets define two core item groups:
- `AvaloniaXaml` (`*.axaml`, `*.paml` by default)
- `AvaloniaResource`

Key behavior:
- `AvaloniaXaml` items are included as resources and compiled.
- `GenerateAvaloniaResourcesTask` packs resources into embedded `!AvaloniaResources`.
- A `ClassToResourcePathIndex` map is generated from `x:Class` declarations.

## Target Flow in Build

High-level order:
1. `AddAvaloniaResources` sets up embedded resource placeholder.
2. `GenerateAvaloniaResources` packs `AvaloniaResource` + `AvaloniaXaml`.
3. `AvaloniaPrepareCoreCompile` adds XAML/resources as compile inputs.
4. `CompileAvaloniaXaml` runs before final output, unless design-time build or explicitly disabled.

`CompileAvaloniaXaml` invokes `CompileAvaloniaXamlTask`, which calls `XamlCompilerTaskExecutor.Compile(...)`.

## What the XAML Compiler Emits

The compiler parses each XAML resource and emits:
- populate methods (`__AvaloniaXamlIlPopulate` or resource-specific populate methods),
- optional build methods (`__AvaloniaXamlIlBuild` / `Build:<resource>`),
- a dispatcher type `CompiledAvaloniaXaml.!XamlLoader` with `TryLoad(...)` overloads.

It also rewrites compiled code-behind calls:
- `AvaloniaXamlLoader.Load(this)`
- `AvaloniaXamlLoader.Load(sp, this)`

to generated trampoline methods that call compiled populate/build paths.

If no `AvaloniaXamlLoader.Load(this)` call exists and constructors are custom, compilation fails.

## Directives that Affect Compilation

### `x:Precompile`
- Literal `true`/`false` only.
- `false` skips compile for that file.

### `x:Class`
- Binds XAML root to a CLR type in target assembly.
- Type must exist.

### `x:ClassModifier`
- Supported values: `Public`, `NotPublic` (or `Internal`).
- Must match actual CLR type visibility when `x:Class` is used.

### `x:CompileBindings`
- Parsed by binding transformer.
- Controls whether `<Binding>` becomes `CompiledBinding` or `ReflectionBinding` in scope.

## Generated Runtime Dispatcher

The compiler builds `CompiledAvaloniaXaml.!XamlLoader.TryLoad(...)` lookup by URI.

Loader reachability rules:
- reachable if compiled build method exists,
- or if `x:Class` type has an accessible public constructor path.

If a resource cannot be instantiated by runtime dispatcher, warning `AVLN3001` is produced.

## Diagnostics and Source Info

`AvaloniaXamlDiagnosticCodes` maps parser/transform/emission issues (`AVLN1xxx`, `AVLN2xxx`, `AVLN3xxx`).

Useful build knobs:
- `AvaloniaXamlVerboseExceptions=true` for richer exceptions,
- `AvaloniaXamlCreateSourceInfo=true` to embed source location metadata,
- `AvaloniaXamlIlVerifyIl=true` for extra IL validation.

`AvaloniaXamlCreateSourceInfo` defaults to `true` in Debug and `false` in non-Debug configurations.

## Name Generator Integration

`Avalonia.Generators.props` injects `@(AvaloniaXaml)` into Roslyn `AdditionalFiles`.

Generator options:
- `AvaloniaNameGeneratorIsEnabled`
- `AvaloniaNameGeneratorBehavior`
- `AvaloniaNameGeneratorDefaultFieldModifier`
- `AvaloniaNameGeneratorFilterByPath`
- `AvaloniaNameGeneratorFilterByNamespace`
- `AvaloniaNameGeneratorViewFileNamingStrategy`
- `AvaloniaNameGeneratorAttachDevTools`

With `InitializeComponent` behavior, generated code calls `AvaloniaXamlLoader.Load(this)` and binds named controls.

## Recommended Project Baseline

```xml
<Project Sdk="Microsoft.NET.Sdk">
  <PropertyGroup>
    <EnableAvaloniaXamlCompilation>true</EnableAvaloniaXamlCompilation>
    <AvaloniaUseCompiledBindingsByDefault>true</AvaloniaUseCompiledBindingsByDefault>
    <AvaloniaXamlCreateSourceInfo>true</AvaloniaXamlCreateSourceInfo>
    <AvaloniaXamlVerboseExceptions>true</AvaloniaXamlVerboseExceptions>
  </PropertyGroup>
</Project>
```

Use `x:CompileBindings` and `x:DataType` intentionally in files where binding mode must differ.

## Troubleshooting

1. "No precompiled XAML found ..."
- XAML not in `AvaloniaXaml`/`AvaloniaResource`, or compilation disabled.

2. Duplicate `x:Class` error
- Multiple resources define same `x:Class`; fix file inclusion/duplicate resources.

3. Runtime loader cannot reach file by URI
- Resource not public/reachable for dispatcher (`AVLN3001`).

4. Unexpected reflection bindings
- Check `AvaloniaUseCompiledBindingsByDefault` and `x:CompileBindings` scope.

5. Weak diagnostics in release builds
- Enable `AvaloniaXamlCreateSourceInfo` and `AvaloniaXamlVerboseExceptions` when investigating.
