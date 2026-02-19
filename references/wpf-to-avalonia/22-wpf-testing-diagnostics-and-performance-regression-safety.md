# WPF Testing, Diagnostics, and Performance Regression Safety to Avalonia

## Table of Contents
1. Scope
2. Validation Strategy Mapping
3. Diagnostics Mapping
4. Conversion Example
5. Avalonia C# Equivalent
6. Troubleshooting

## Scope

This reference defines regression-control patterns for WPF-to-Avalonia migration: behavior parity, rendering stability, input correctness, and performance limits.

## Validation Strategy Mapping

| WPF migration risk | Avalonia validation approach |
|---|---|
| routed-input differences | focused key/pointer routing tests |
| binding regressions | typed binding + view-model tests |
| rendering regressions | visual snapshots and deterministic render scenarios |
| performance drift | profiling and UI-thread workload checks |

## Diagnostics Mapping

Use repository references for test/diagnostic workflows:

- [`../26-testing-stack-headless-render-and-ui-tests.md`](../26-testing-stack-headless-render-and-ui-tests)
- [`../27-diagnostics-profiling-and-devtools.md`](../27-diagnostics-profiling-and-devtools)
- [`../08-performance-checklist.md`](../08-performance-checklist)

## Conversion Example

WPF behavior contract:

```csharp
// Ctrl+S saves current document and keeps editor focus.
```

Avalonia XAML target:

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

## Avalonia C# Equivalent

```csharp
using System;

public static class MigrationAssertions
{
    public static void AssertSaveIsExecutable(EditorViewModel vm)
    {
        if (!vm.SaveCommand.CanExecute(null))
            throw new InvalidOperationException("Save command must be executable.");
    }

    public static void AssertOnUiThread(bool isUiThread)
    {
        if (!isUiThread)
            throw new InvalidOperationException("UI mutation from non-UI thread.");
    }
}
```

## Troubleshooting

1. migrated features pass basic tests but fail under load.
- add dispatcher/async and large-data tests.

2. focus behavior diverges from WPF.
- add explicit focus and keyboard navigation scenario tests.

3. large migration slices are hard to verify.
- cut migration into smaller vertical slices with explicit parity gates.
