# WinUI UserControl and CustomControl to Avalonia UserControl and TemplatedControl

## Table of Contents
1. Scope and APIs
2. Concept Mapping
3. Conversion Example
4. Migration Notes

## Scope and APIs

Primary WinUI APIs:

- UserControl, CustomControl, OnApplyTemplate, TemplatePart

Primary Avalonia APIs:

- UserControl, TemplatedControl, OnApplyTemplate, TemplatePartAttribute

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
  <local:MetricCard Value="{x:Bind ViewModel.Value}" />
</Page>
```

WinUI C#:

```csharp
var view = new MetricCard();
```

Avalonia XAML:

```xaml
<UserControl xmlns="https://github.com/avaloniaui"
             xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
             xmlns:vm="using:MyApp.ViewModels"
             xmlns:local="using:MyApp.Controls"
             x:DataType="vm:SampleViewModel">
  <local:MetricCard Value="{CompiledBinding Value}" />
</UserControl>
```

Avalonia C#:

```csharp
var metricCard = new MetricCard { Value = viewModel.Value };
```

## Migration Notes

1. Start by porting behavior and state contracts first, then restyle and retune visuals.
2. Prefer typed compiled bindings and avoid reflection-heavy dynamic binding paths.
3. Keep UI-thread updates explicit when porting WinUI async/event flows.
