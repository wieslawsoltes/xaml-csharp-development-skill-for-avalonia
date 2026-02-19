# WPF Binding Modes, RelativeSource, ElementName, and UpdateSource to Avalonia

## Table of Contents
1. Scope and APIs
2. Binding Feature Mapping
3. Conversion Example
4. Avalonia C# Equivalent
5. Troubleshooting

## Scope and APIs

Primary WPF APIs:

- `Binding` (`Mode`, `UpdateSourceTrigger`, `RelativeSource`, `ElementName`)
- `INotifyPropertyChanged`

Primary Avalonia APIs:

- `{CompiledBinding ...}` and `{Binding ...}`
- binding mode support (`OneWay`, `TwoWay`, etc.)
- `RelativeSource`, `ElementName`

## Binding Feature Mapping

| WPF | Avalonia |
|---|---|
| `Mode=TwoWay` | same concept |
| `UpdateSourceTrigger=PropertyChanged` | same intent for editable controls |
| `RelativeSource AncestorType=...` | same concept |
| `ElementName=...` | same concept |

Recommended default in migrated views:

- use compiled bindings for view-model paths,
- use standard binding form for name/ancestor-based element bindings when clearer.

## Conversion Example

WPF XAML:

```xaml
<TextBox x:Name="QueryBox"
         Text="{Binding Query, Mode=TwoWay, UpdateSourceTrigger=PropertyChanged}" />
<TextBlock Text="{Binding Text, ElementName=QueryBox}" />
```

Avalonia XAML:

```xaml
<UserControl xmlns="https://github.com/avaloniaui"
             xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
             xmlns:vm="using:MyApp.ViewModels"
             x:DataType="vm:SearchViewModel">
  <StackPanel Spacing="6">
    <TextBox x:Name="QueryBox"
             Text="{CompiledBinding Query, Mode=TwoWay, UpdateSourceTrigger=PropertyChanged}" />
    <TextBlock Text="{Binding Text, ElementName=QueryBox}" />
  </StackPanel>
</UserControl>
```

## Avalonia C# Equivalent

```csharp
using Avalonia.Controls;
using Avalonia.Data;

var query = new TextBox();
query.Bind(TextBox.TextProperty, new Binding("Query")
{
    Mode = BindingMode.TwoWay,
    UpdateSourceTrigger = UpdateSourceTrigger.PropertyChanged
});
```

## Troubleshooting

1. Binding compiles but does not update.
- confirm view-model raises `PropertyChanged` for the bound property.

2. Element-name binding fails.
- ensure the target element name is in scope and loaded in the same name scope.

3. runtime-only binding errors remain.
- migrate view-model bindings to compiled bindings with `x:DataType`.
