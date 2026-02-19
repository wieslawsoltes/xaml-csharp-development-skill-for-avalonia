# WPF Choice Controls (CheckBox, RadioButton, Toggle) and State Modeling to Avalonia

## Table of Contents
1. Scope and APIs
2. Choice Control Mapping
3. Conversion Example
4. Avalonia C# Equivalent
5. Troubleshooting

## Scope and APIs

Primary WPF APIs:

- `CheckBox` (`IsThreeState`, `IsChecked`)
- `RadioButton` grouping
- `ToggleButton`

Primary Avalonia APIs:

- `CheckBox` (`IsThreeState`, `IsChecked`)
- `RadioButton` (`GroupName`)
- `ToggleButton` and `ToggleSwitch`

## Choice Control Mapping

| WPF | Avalonia |
|---|---|
| tri-state checkbox | same concept (`IsThreeState`, nullable `IsChecked`) |
| radio groups by container/name | explicit `GroupName` for predictable grouping |
| toggle semantics | `ToggleButton`/`ToggleSwitch` |

## Conversion Example

WPF XAML:

```xaml
<StackPanel>
  <CheckBox Content="Archive"
            IsThreeState="True"
            IsChecked="{Binding ArchiveState, Mode=TwoWay}" />

  <StackPanel Orientation="Horizontal">
    <RadioButton GroupName="Priority" Content="High" IsChecked="{Binding IsHigh}" />
    <RadioButton GroupName="Priority" Content="Low" IsChecked="{Binding IsLow}" />
  </StackPanel>
</StackPanel>
```

Avalonia XAML:

```xaml
<UserControl xmlns="https://github.com/avaloniaui"
             xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
             xmlns:vm="using:MyApp.ViewModels"
             x:DataType="vm:PreferencesViewModel">
  <StackPanel Spacing="8">
    <CheckBox Content="Archive"
              IsThreeState="True"
              IsChecked="{CompiledBinding ArchiveState, Mode=TwoWay}" />

    <StackPanel Orientation="Horizontal" Spacing="8">
      <RadioButton GroupName="Priority"
                   Content="High"
                   IsChecked="{CompiledBinding IsHigh, Mode=TwoWay}" />
      <RadioButton GroupName="Priority"
                   Content="Low"
                   IsChecked="{CompiledBinding IsLow, Mode=TwoWay}" />
    </StackPanel>

    <ToggleSwitch Content="Enable sync"
                  IsChecked="{CompiledBinding SyncEnabled, Mode=TwoWay}" />
  </StackPanel>
</UserControl>
```

## Avalonia C# Equivalent

```csharp
using Avalonia.Controls;

var archive = new CheckBox
{
    Content = "Archive",
    IsThreeState = true,
    IsChecked = null
};

var high = new RadioButton { GroupName = "Priority", Content = "High" };
var low = new RadioButton { GroupName = "Priority", Content = "Low" };
var sync = new ToggleSwitch { Content = "Enable sync", IsChecked = true };
```

## Troubleshooting

1. Tri-state values collapse to true/false.
- use `bool?` in the view model for indeterminate state.

2. Radio groups interfere across UI regions.
- set explicit `GroupName` values and avoid accidental cross-grouping.

3. Toggle UX becomes ambiguous.
- reserve `ToggleSwitch` for setting-like states and keep labels explicit.
