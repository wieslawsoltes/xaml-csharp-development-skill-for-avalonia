# WPF Routed Events, Commands, and InputBindings to Avalonia

## Table of Contents
1. Scope and APIs
2. Event and Command Mapping
3. Input Gesture Mapping
4. Conversion Example
5. Avalonia C# Equivalent
6. Troubleshooting

## Scope and APIs

Primary WPF APIs:

- `RoutedEvent`, bubbling/tunneling handlers
- `RoutedCommand`, `CommandBinding`, `InputBinding`, `KeyBinding`

Primary Avalonia APIs:

- `RoutedEvent` and routed event handlers
- `ICommand` command sources (`Button`, `MenuItem`, etc.)
- `KeyBinding`, `KeyGesture`, `HotKey`

## Event and Command Mapping

| WPF | Avalonia |
|---|---|
| `RoutedCommand` + `CommandBinding` | `ICommand` on command sources + explicit handlers |
| `CanExecute` routing | command `CanExecute` + view-model state |
| routed events (`Preview*`, `*`) | routed input events with tunnel/bubble semantics |

## Input Gesture Mapping

| WPF | Avalonia |
|---|---|
| `<Window.InputBindings>` | root `KeyBindings` on `Window`/`UserControl` |
| `InputGestureText` in menu | `InputGesture` display hint on `MenuItem` |
| shortcut execution | `HotKey` or `KeyBinding` |

## Conversion Example

WPF XAML:

```xaml
<Window.InputBindings>
  <KeyBinding Gesture="Ctrl+S" Command="{Binding SaveCommand}" />
</Window.InputBindings>

<MenuItem Header="_Save" Command="{Binding SaveCommand}" InputGestureText="Ctrl+S" />
```

Avalonia XAML:

```xaml
<UserControl xmlns="https://github.com/avaloniaui"
             xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
             xmlns:vm="using:MyApp.ViewModels"
             x:DataType="vm:EditorViewModel">
  <UserControl.KeyBindings>
    <KeyBinding Gesture="Ctrl+S" Command="{CompiledBinding SaveCommand}" />
  </UserControl.KeyBindings>

  <Menu>
    <MenuItem Header="_File">
      <MenuItem Header="_Save"
                Command="{CompiledBinding SaveCommand}"
                InputGesture="Ctrl+S"
                HotKey="Ctrl+S" />
    </MenuItem>
  </Menu>
</UserControl>
```

## Avalonia C# Equivalent

```csharp
using Avalonia.Controls;
using Avalonia.Input;

var root = new UserControl();
root.KeyBindings.Add(new KeyBinding
{
    Gesture = KeyGesture.Parse("Ctrl+S"),
    Command = viewModel.SaveCommand
});
```

## Troubleshooting

1. Shortcut text shows but command never runs.
- `InputGesture` is only hint text; wire `HotKey` or `KeyBinding` for execution.

2. command executes twice.
- remove duplicate bindings at nested roots.

3. routed handler order changed.
- verify tunnel vs bubble registration points after port.
