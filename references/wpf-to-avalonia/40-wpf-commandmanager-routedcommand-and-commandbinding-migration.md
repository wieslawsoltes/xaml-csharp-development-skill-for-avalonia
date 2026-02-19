# WPF CommandManager, RoutedCommand, and CommandBinding Migration to Avalonia

## Table of Contents
1. Scope and APIs
2. Command Infrastructure Mapping
3. Conversion Example
4. Avalonia C# Equivalent
5. Troubleshooting

## Scope and APIs

Primary WPF APIs:

- `RoutedCommand`, `RoutedUICommand`
- `CommandBinding`
- `CommandManager.RequerySuggested` / `InvalidateRequerySuggested()`

Primary Avalonia APIs:

- `ICommand` command sources (`Button`, `MenuItem`, `ToggleButton`)
- `KeyBinding` and `HotKey` for keyboard activation
- explicit command-state invalidation by raising `CanExecuteChanged`

Avalonia `11.3.12` does not provide WPF `CommandManager`/`CommandBinding` routing primitives.

## Command Infrastructure Mapping

| WPF | Avalonia |
|---|---|
| `RoutedCommand` + `CommandBinding` | `ICommand` on control + view-model command handlers |
| `CommandManager.RequerySuggested` | explicit `CanExecuteChanged` raise from command implementation |
| `Window.InputBindings` | `KeyBindings` on `Window`/`UserControl` |

## Conversion Example

WPF XAML:

```xaml
<Window.CommandBindings>
  <CommandBinding Command="{x:Static ApplicationCommands.Save}"
                  Executed="SaveExecuted"
                  CanExecute="SaveCanExecute" />
</Window.CommandBindings>

<Window.InputBindings>
  <KeyBinding Command="{x:Static ApplicationCommands.Save}" Gesture="Ctrl+S" />
</Window.InputBindings>
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
            Command="{CompiledBinding SaveCommand}" />
    <TextBlock Text="{CompiledBinding SaveStatus}" />
  </StackPanel>
</UserControl>
```

## Avalonia C# Equivalent

```csharp
using System;
using System.Windows.Input;
using Avalonia.Controls;
using Avalonia.Input;

public sealed class RelayCommand : ICommand
{
    private readonly Action _execute;
    private readonly Func<bool> _canExecute;

    public RelayCommand(Action execute, Func<bool> canExecute)
    {
        _execute = execute;
        _canExecute = canExecute;
    }

    public event EventHandler? CanExecuteChanged;

    public bool CanExecute(object? parameter) => _canExecute();

    public void Execute(object? parameter) => _execute();

    public void RaiseCanExecuteChanged() => CanExecuteChanged?.Invoke(this, EventArgs.Empty);
}

var saveCommand = new RelayCommand(
    execute: () => viewModel.Save(),
    canExecute: () => viewModel.CanSave);

var root = new UserControl();
root.KeyBindings.Add(new KeyBinding
{
    Gesture = KeyGesture.Parse("Ctrl+S"),
    Command = saveCommand
});

// Replace CommandManager.InvalidateRequerySuggested():
viewModel.CanSave = false;
saveCommand.RaiseCanExecuteChanged();
```

## Troubleshooting

1. `CanExecute` does not refresh automatically after state changes.
- Raise `CanExecuteChanged` explicitly when relevant state changes.

2. Shortcut displays in menu but command does not run.
- Add `KeyBinding`/`HotKey`; gesture text alone is only visual metadata.

3. Migrated command logic is too coupled to views.
- Move command state and execution logic into view models/services.
