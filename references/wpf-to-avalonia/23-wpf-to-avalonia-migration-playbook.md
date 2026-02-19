# WPF to Avalonia Migration Playbook

## Table of Contents
1. Scope
2. Phase Plan
3. Practical Checkpoints
4. Example Vertical Slice
5. Avalonia C# Planning Skeleton
6. Exit Criteria

## Scope

This playbook provides a production-focused sequencing model for migrating WPF applications to Avalonia with controlled risk.

## Phase Plan

1. baseline inventory:
- catalog windows, custom controls, templates, commands, and interop surfaces.

2. shell and lifetime:
- port startup, main window, and platform service boundaries.

3. property/layout/binding:
- port dependency properties, layout containers, and binding surfaces.

4. styling/templates/state:
- port resources, control themes, and trigger/state behaviors.

5. advanced flows:
- dialogs/navigation/background work/custom rendering/interop.

6. hardening:
- accessibility, diagnostics, and performance validation.

## Practical Checkpoints

- all new views use compiled bindings with `x:DataType` when feasible.
- no blocking UI-thread calls remain from WPF-era sync flows.
- custom controls expose clear Avalonia property contracts.
- platform integrations isolated behind abstractions.

## Example Vertical Slice

WPF slice candidate:

```csharp
// Customer editor window: validation + command bar + async save.
```

Avalonia XAML target:

```xaml
<Grid xmlns="https://github.com/avaloniaui"
      xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
      xmlns:vm="using:MyApp.ViewModels"
      x:DataType="vm:CustomerEditorViewModel"
      RowDefinitions="Auto,*"
      RowSpacing="8">
  <StackPanel Orientation="Horizontal" Spacing="8">
    <Button Content="Save" Command="{CompiledBinding SaveCommand}" />
    <Button Content="Cancel" Command="{CompiledBinding CancelCommand}" />
  </StackPanel>

  <TextBox Grid.Row="1" Text="{CompiledBinding CustomerName, Mode=TwoWay}" />
</Grid>
```

## Avalonia C# Planning Skeleton

```csharp
public sealed class MigrationSlice
{
    public string Name { get; init; } = string.Empty;
    public bool PropertySystemPorted { get; set; }
    public bool LayoutPorted { get; set; }
    public bool StylingPorted { get; set; }
    public bool CommandsPorted { get; set; }
    public bool Verified { get; set; }
}

public static bool ReadyForCutover(MigrationSlice slice)
    => slice.PropertySystemPorted
    && slice.LayoutPorted
    && slice.StylingPorted
    && slice.CommandsPorted
    && slice.Verified;
```

## Exit Criteria

- parity-critical workflows validated across target platforms.
- no known blocking accessibility or threading regressions.
- style/template system fully under Avalonia theme/resource ownership.
- unresolved gaps documented with explicit mitigation and ownership.
