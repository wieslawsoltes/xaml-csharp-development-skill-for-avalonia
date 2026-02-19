# WinUI Layout Panels, Measure/Arrange, and Effective Pixels to Avalonia

## Table of Contents
1. Scope and APIs
2. Concept Mapping
3. Conversion Example
4. Migration Notes

## Scope and APIs

Primary WinUI APIs:

- Grid, StackPanel, RelativePanel, Canvas, MeasureOverride, ArrangeOverride

Primary Avalonia APIs:

- Grid, StackPanel, RelativePanel, Canvas, MeasureOverride, ArrangeOverride

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
  <Grid RowDefinitions="Auto,*" ColumnDefinitions="220,*"><TextBlock Text="Name" /><TextBox Grid.Column="1" /></Grid>
</Page>
```

WinUI C#:

```csharp
var view = new Grid();
```

Avalonia XAML:

```xaml
<UserControl xmlns="https://github.com/avaloniaui"
             xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
             xmlns:vm="using:MyApp.ViewModels"
             xmlns:local="using:MyApp.Controls"
             x:DataType="vm:SampleViewModel">
  <Grid RowDefinitions="Auto,*" ColumnDefinitions="220,*"><TextBlock Text="Name" /><TextBox Grid.Column="1" /></Grid>
</UserControl>
```

Avalonia C#:

```csharp
var form = new Grid { RowDefinitions = RowDefinitions.Parse("Auto,*"), ColumnDefinitions = ColumnDefinitions.Parse("220,*") };
```

## Migration Notes

1. Start by porting behavior and state contracts first, then restyle and retune visuals.
2. Prefer typed compiled bindings and avoid reflection-heavy dynamic binding paths.
3. Keep UI-thread updates explicit when porting WinUI async/event flows.
