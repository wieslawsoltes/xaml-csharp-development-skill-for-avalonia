# WinUI Binding, x:Bind, RelativeSource, and Update Flow to Avalonia

## Table of Contents
1. Scope and APIs
2. Concept Mapping
3. Conversion Example
4. Migration Notes

## Scope and APIs

Primary WinUI APIs:

- {Binding}, {x:Bind}, Mode, ElementName, RelativeSource, UpdateSourceTrigger

Primary Avalonia APIs:

- {Binding}, {CompiledBinding}, RelativeSource, ElementName, BindingPriority

## Concept Mapping

| WinUI idiom | Avalonia idiom |
|---|---|
| WinUI control/template/state pipeline | Avalonia control theme/style/selector pipeline |
| `x:Bind` or `{Binding}` data flow | `{CompiledBinding ...}` and typed `x:DataType` flow |
| WinUI layout/render invalidation model | Avalonia `InvalidateMeasure`/`InvalidateArrange`/`InvalidateVisual` model |

## Conversion Example

WinUI XAML:

```xaml
<Page
    x:Class="MyApp.Views.SamplePage"
    xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
    xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
    xmlns:local="using:MyApp.Controls">
  <TextBox Text="{x:Bind ViewModel.Query, Mode=TwoWay}" />
</Page>
```

WinUI C#:

```csharp
var view = new TextBox();
```

Avalonia XAML:

```xaml
<UserControl xmlns="https://github.com/avaloniaui"
             xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
             xmlns:vm="using:MyApp.ViewModels"
             xmlns:local="using:MyApp.Controls"
             x:DataType="vm:SampleViewModel">
  <TextBox Text="{CompiledBinding Query, Mode=TwoWay}" />
</UserControl>
```

Avalonia C#:

```csharp
var box = new TextBox(); box.Bind(TextBox.TextProperty, new Binding("Query") { Mode = BindingMode.TwoWay });
```

## Migration Notes

1. Start by porting behavior and state contracts first, then restyle and retune visuals.
2. Prefer typed compiled bindings and avoid reflection-heavy dynamic binding paths.
3. Keep UI-thread updates explicit when porting WinUI async/event flows.
