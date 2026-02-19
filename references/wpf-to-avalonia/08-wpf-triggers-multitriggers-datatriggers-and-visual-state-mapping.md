# WPF Triggers, MultiTriggers, DataTriggers, and Visual State Mapping to Avalonia

## Table of Contents
1. Scope and APIs
2. Trigger/State Mapping
3. Conversion Example
4. Avalonia C# Equivalent
5. Troubleshooting

## Scope and APIs

Primary WPF APIs:

- `Trigger`, `MultiTrigger`, `DataTrigger`
- `VisualStateManager` and storyboard-driven states

Primary Avalonia patterns:

- selector + pseudo-class styling (`:pointerover`, `:pressed`, `:checked`, `:disabled`)
- class-based state flags (`Classes.someState`)
- transitions/animations for state changes

## Trigger/State Mapping

| WPF | Avalonia |
|---|---|
| property trigger (`IsMouseOver`) | pseudo-class selector (`:pointerover`) |
| multi-trigger | combined selectors and explicit class-state modeling |
| data trigger | bind boolean to `Classes.<name>` then style by class |
| `VisualStateManager` groups | template state classes + transitions/animations |

## Conversion Example

WPF XAML:

```xaml
<Style TargetType="Button">
  <Style.Triggers>
    <Trigger Property="IsMouseOver" Value="True">
      <Setter Property="Opacity" Value="0.85" />
    </Trigger>
  </Style.Triggers>
</Style>
```

Avalonia XAML:

```xaml
<Style xmlns="https://github.com/avaloniaui" Selector="Button.primary">
  <Setter Property="Opacity" Value="1" />
</Style>

<Style xmlns="https://github.com/avaloniaui" Selector="Button.primary:pointerover">
  <Setter Property="Opacity" Value="0.85" />
</Style>

<TextBox xmlns="https://github.com/avaloniaui"
         xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
         xmlns:vm="using:MyApp.ViewModels"
         x:DataType="vm:StateViewModel"
         Classes.error="{CompiledBinding HasError}" />
<Style xmlns="https://github.com/avaloniaui" Selector="TextBox.error">
  <Setter Property="BorderBrush" Value="#D13438" />
</Style>
```

## Avalonia C# Equivalent

```csharp
using Avalonia.Controls;

var input = new TextBox();
input.Classes.Set("error", viewModel.HasError);
```

For animated state changes, add `Transitions` on the control and switch class/pseudo-class state.

## Troubleshooting

1. Expecting direct `DataTrigger`/`MultiTrigger` parity.
- model state with selectors and view-model boolean classes.

2. complex visual state logic becomes hard to read.
- split state styles by feature and keep class names explicit.

3. animation timing feels different from storyboard behavior.
- tune transitions and use keyframe animations for advanced states.
