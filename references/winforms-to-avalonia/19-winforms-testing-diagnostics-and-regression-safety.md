# WinForms to Avalonia Testing, Diagnostics, and Regression Safety

## Table of Contents
1. Scope
2. Test Strategy Mapping
3. Diagnostics Mapping
4. Conversion Example
5. C# Equivalent
6. Troubleshooting

## Scope

This reference defines a pragmatic migration verification model so WinForms-to-Avalonia conversion does not trade feature parity for unstable behavior.

## Test Strategy Mapping

| WinForms migration risk | Avalonia validation approach |
|---|---|
| event-driven behavior drift | command- and binding-level tests on view models |
| layout regressions | visual/snapshot checks and deterministic layout scenarios |
| threading regressions | tests around dispatcher marshaling and async workflows |
| platform service breakage | integration checks for storage, clipboard, tray, menu paths |

## Diagnostics Mapping

- WinForms control-tree/debugging habits map to Avalonia visual/logical tree inspection.
- validate input/focus routing with focused control-tree scenarios.
- use existing diagnostics references:
  - [`../26-testing-stack-headless-render-and-ui-tests.md`](../26-testing-stack-headless-render-and-ui-tests)
  - [`../27-diagnostics-profiling-and-devtools.md`](../27-diagnostics-profiling-and-devtools)

## Conversion Example

WinForms baseline behavior definition:

```csharp
var saveShortcut = new ToolStripMenuItem("Save")
{
    ShortcutKeys = Keys.Control | Keys.S
};

saveShortcut.Click += (_, _) =>
{
    SaveDocument();
    editorTextBox.Focus();
};

menuStrip.Items.Add(saveShortcut);
```

Avalonia XAML test target shape:

```xaml
<UserControl xmlns="https://github.com/avaloniaui"
             xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
             xmlns:vm="using:MyApp.ViewModels"
             x:DataType="vm:EditorViewModel">
  <UserControl.KeyBindings>
    <KeyBinding Gesture="Ctrl+S" Command="{CompiledBinding SaveCommand}" />
  </UserControl.KeyBindings>
  <TextBox Text="{CompiledBinding DocumentText, Mode=TwoWay}" />
</UserControl>
```

## C# Equivalent

```csharp
using System;
using Avalonia.Threading;

public static class RegressionChecks
{
    public static void AssertCanSave(EditorViewModel vm)
    {
        if (!vm.SaveCommand.CanExecute(null))
            throw new InvalidOperationException("Save command should be executable.");
    }

    public static void AssertNoUiThreadViolation()
    {
        if (!Dispatcher.UIThread.CheckAccess())
            throw new InvalidOperationException("UI mutation attempted from a non-UI thread.");
    }
}
```

## Troubleshooting

1. Migration appears functionally correct but unstable under load.
- add explicit async/dispatcher test coverage around heavy operations.

2. Keyboard and focus behavior differs from WinForms.
- add deterministic key/focus scenarios with rooted key bindings.

3. Large feature slices are hard to verify.
- split migration into smaller vertical slices and gate each with parity checks.
