# WinForms Choice Controls (CheckBox, RadioButton, CheckedListBox) to Avalonia

## Table of Contents
1. Scope and APIs
2. Choice Control Mapping
3. Conversion Example
4. C# Equivalent
5. Troubleshooting

## Scope and APIs

Primary WinForms APIs:

- `CheckBox` (`ThreeState`)
- `RadioButton`
- `CheckedListBox`

Primary Avalonia APIs:

- `CheckBox` (`IsThreeState`)
- `RadioButton` (`GroupName`)
- `ListBox` + checkbox item template
- optional `ToggleSwitch` for binary settings UX

## Choice Control Mapping

| WinForms | Avalonia |
|---|---|
| `CheckBox.Checked`/`CheckState` | `CheckBox.IsChecked` (`bool?`) |
| `ThreeState` | `IsThreeState="True"` |
| `RadioButton` groups by container | `RadioButton GroupName` for explicit grouping |
| `CheckedListBox` | `ListBox` with `CheckBox` in `ItemTemplate` |

## Conversion Example

WinForms C#:

```csharp
var archive = new CheckBox { ThreeState = true, CheckState = CheckState.Indeterminate };

var high = new RadioButton { Text = "High" };
var low = new RadioButton { Text = "Low" };

var tags = new CheckedListBox();
tags.Items.Add("UI", true);
tags.Items.Add("Data", false);
```

Avalonia XAML:

```xaml
<UserControl xmlns="https://github.com/avaloniaui"
             xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
             xmlns:vm="using:MyApp.ViewModels"
             x:DataType="vm:SettingsViewModel">
  <StackPanel Spacing="8">
    <CheckBox Content="Archive after export"
              IsThreeState="True"
              IsChecked="{CompiledBinding ArchiveState, Mode=TwoWay}" />

    <StackPanel Orientation="Horizontal" Spacing="8">
      <RadioButton GroupName="Priority"
                   Content="High"
                   IsChecked="{CompiledBinding IsHighPriority, Mode=TwoWay}" />
      <RadioButton GroupName="Priority"
                   Content="Low"
                   IsChecked="{CompiledBinding IsLowPriority, Mode=TwoWay}" />
    </StackPanel>

    <ListBox ItemsSource="{CompiledBinding Tags}">
      <ListBox.ItemTemplate>
        <DataTemplate x:DataType="vm:TagOptionViewModel">
          <CheckBox Content="{CompiledBinding Name}"
                    IsChecked="{CompiledBinding IsChecked, Mode=TwoWay}" />
        </DataTemplate>
      </ListBox.ItemTemplate>
    </ListBox>
  </StackPanel>
</UserControl>
```

## C# Equivalent

```csharp
using Avalonia.Controls;

var archive = new CheckBox
{
    Content = "Archive after export",
    IsThreeState = true,
    IsChecked = null
};

var high = new RadioButton { GroupName = "Priority", Content = "High" };
var low = new RadioButton { GroupName = "Priority", Content = "Low" };
```

## Troubleshooting

1. Radio buttons in different regions interfere.
- set explicit `GroupName` values instead of relying on implicit container grouping.

2. Checked-list behavior is hard to bind.
- represent checked-state in item view-models and bind each item checkbox.

3. Tri-state check values collapse to true/false.
- use nullable bool model properties (`bool?`) for indeterminate state.
