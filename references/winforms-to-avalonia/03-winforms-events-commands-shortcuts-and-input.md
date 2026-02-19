# WinForms Events, Commands, Shortcuts, and Input to Avalonia

## Table of Contents
1. Scope and APIs
2. Event-to-Command Mapping
3. Keyboard Shortcut Mapping
4. Conversion Example
5. C# Equivalent
6. Troubleshooting

## Scope and APIs

Primary WinForms APIs:

- control events (`Click`, `TextChanged`, `KeyDown`)
- form-level key handling (`KeyPreview`, `ProcessCmdKey`)

Primary Avalonia APIs:

- `ICommand` on command sources (`Button`, `MenuItem`)
- `KeyBinding`, `KeyGesture`, `HotKey`
- input events (`PointerPressed`, `KeyDown`)

## Event-to-Command Mapping

| WinForms | Avalonia |
|---|---|
| `button.Click += ...` | `Button Command="{CompiledBinding ...}"` |
| `TextBox.TextChanged` handler | bind `Text` to view-model property and react in model layer |
| imperative `Enabled` toggling | bind `IsEnabled` to state or command `CanExecute` |

## Keyboard Shortcut Mapping

| WinForms | Avalonia |
|---|---|
| `KeyPreview = true` + `KeyDown` | root-level `KeyBindings` |
| `ProcessCmdKey` | `KeyBinding` with `Gesture` + command |
| menu shortcut text | `InputGesture` on `MenuItem` |
| shortcut execution | `HotKey` or `KeyBinding` |

## Conversion Example

WinForms C#:

```csharp
public MainForm()
{
    InitializeComponent();
    KeyPreview = true;

    saveButton.Click += (_, _) => Save();
    KeyDown += (_, e) =>
    {
        if (e.Control && e.KeyCode == Keys.S)
        {
            Save();
            e.Handled = true;
        }
    };
}
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

  <StackPanel Spacing="8">
    <Button Content="Save"
            Command="{CompiledBinding SaveCommand}"
            HotKey="Ctrl+S" />
  </StackPanel>
</UserControl>
```

## C# Equivalent

```csharp
using Avalonia.Controls;
using Avalonia.Input;

var view = new UserControl();
view.KeyBindings.Add(new KeyBinding
{
    Gesture = KeyGesture.Parse("Ctrl+S"),
    Command = viewModel.SaveCommand
});

var saveButton = new Button
{
    Content = "Save",
    Command = viewModel.SaveCommand,
    HotKey = KeyGesture.Parse("Ctrl+S")
};
```

## Troubleshooting

1. Shortcut text appears but key does nothing.
- `InputGesture` is display-only; wire `HotKey` or `KeyBinding` for execution.

2. Command executes twice.
- remove duplicate shortcut registrations at nested scopes.

3. Large code-behind event graph remains after migration.
- move side effects into view-model commands and observable state.
