# WPF Access Keys, Label Target, Focus Scope, and Tab Navigation to Avalonia

## Table of Contents
1. Scope and APIs
2. Keyboard UX Mapping
3. Conversion Example
4. Avalonia C# Equivalent
5. Troubleshooting

## Scope and APIs

Primary WPF APIs:

- access-key markup (`_File`, `AccessText`)
- `Label.Target`
- `KeyboardNavigation.TabNavigation`, `TabIndex`
- `FocusManager.IsFocusScope`

Primary Avalonia APIs:

- access-key marker in content (`_`) + `AccessText` behavior in templates
- `Label.Target`
- `KeyboardNavigation.TabNavigation`, `KeyboardNavigation.TabIndex`, `KeyboardNavigation.IsTabStop`
- `FocusManager` usage through `TopLevel.FocusManager`

In Avalonia, focus scopes are defined by controls implementing `IFocusScope` (for example top-level roots), not by setting a public `IsFocusScope` attached property.

## Keyboard UX Mapping

| WPF | Avalonia |
|---|---|
| `_Save` / `AccessText` | `_Save` marker works on common controls; template `ContentPresenter` can opt into access-key parsing |
| `Label Target="{Binding ElementName=...}"` | `Label Target="{Binding #...}"` |
| `KeyboardNavigation.TabNavigation` | `KeyboardNavigation.TabNavigation` |
| `KeyboardNavigation.TabIndex` | `KeyboardNavigation.TabIndex` |

## Conversion Example

WPF XAML:

```xaml
<StackPanel KeyboardNavigation.TabNavigation="Cycle">
  <Label Content="_Name" Target="{Binding ElementName=NameBox}" />
  <TextBox x:Name="NameBox" TabIndex="0" />
  <Button Content="_Save" TabIndex="1" />
</StackPanel>
```

Avalonia XAML:

```xaml
<UserControl xmlns="https://github.com/avaloniaui"
             xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
             xmlns:vm="using:MyApp.ViewModels"
             x:DataType="vm:ProfileViewModel">
  <StackPanel KeyboardNavigation.TabNavigation="Cycle" Spacing="8">
    <Label Content="_Name" Target="{Binding #NameBox}" />
    <TextBox x:Name="NameBox"
             KeyboardNavigation.TabIndex="0"
             Text="{CompiledBinding Name, Mode=TwoWay}" />

    <Label Content="_Email" Target="{Binding #EmailBox}" />
    <TextBox x:Name="EmailBox"
             KeyboardNavigation.TabIndex="1"
             Text="{CompiledBinding Email, Mode=TwoWay}" />

    <Button Content="_Save"
            KeyboardNavigation.TabIndex="2"
            Command="{CompiledBinding SaveCommand}" />
  </StackPanel>
</UserControl>
```

## Avalonia C# Equivalent

```csharp
using Avalonia.Controls;
using Avalonia.Input;

var panel = new StackPanel { Spacing = 8 };
KeyboardNavigation.SetTabNavigation(panel, KeyboardNavigationMode.Cycle);

var nameBox = new TextBox();
KeyboardNavigation.SetTabIndex(nameBox, 0);

var emailBox = new TextBox();
KeyboardNavigation.SetTabIndex(emailBox, 1);

var save = new Button { Content = "_Save", Command = viewModel.SaveCommand };
KeyboardNavigation.SetTabIndex(save, 2);

var nameLabel = new Label { Content = "_Name", Target = nameBox };
var emailLabel = new Label { Content = "_Email", Target = emailBox };

panel.Children.Add(nameLabel);
panel.Children.Add(nameBox);
panel.Children.Add(emailLabel);
panel.Children.Add(emailBox);
panel.Children.Add(save);
```

## Troubleshooting

1. Access keys are shown but do not activate target controls.
- Ensure `Label.Target` points to a focusable input element.

2. Tab order is inconsistent after migration.
- Set `KeyboardNavigation.TabIndex` explicitly on critical form fields.

3. Focus gets trapped or skipped in composite surfaces.
- Set `KeyboardNavigation.TabNavigation` intentionally on container roots (`Cycle`, `Local`, etc.).
