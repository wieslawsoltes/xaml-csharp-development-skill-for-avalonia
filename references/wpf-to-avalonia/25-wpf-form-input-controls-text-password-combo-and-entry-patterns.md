# WPF Form Input Controls (Text, Password, Combo, Entry Patterns) to Avalonia

## Table of Contents
1. Scope and APIs
2. Input Control Mapping
3. Conversion Example
4. Avalonia C# Equivalent
5. Troubleshooting

## Scope and APIs

Primary WPF APIs:

- `TextBox`, `PasswordBox`
- `ComboBox` (`IsEditable`, `IsTextSearchEnabled`)

Primary Avalonia APIs:

- `TextBox` (`PasswordChar` for masked entry)
- `ComboBox`
- optional `AutoCompleteBox` for suggestion-heavy entry

## Input Control Mapping

| WPF | Avalonia |
|---|---|
| `TextBox.Text` | `TextBox.Text` |
| `PasswordBox.Password` | `TextBox PasswordChar="*"` or custom secure-entry pattern |
| `ComboBox IsEditable="True"` | `ComboBox IsEditable="True"` |
| `ComboBox IsTextSearchEnabled="True"` | `ComboBox IsTextSearchEnabled="True"` |
| watermark via style/template | `Watermark` properties on text entry controls |

## Conversion Example

WPF XAML:

```xaml
<StackPanel>
  <TextBox Text="{Binding UserName, Mode=TwoWay}" />
  <PasswordBox />
  <ComboBox ItemsSource="{Binding Roles}"
            SelectedItem="{Binding SelectedRole, Mode=TwoWay}"
            IsEditable="True"
            IsTextSearchEnabled="True" />
</StackPanel>
```

Avalonia XAML:

```xaml
<UserControl xmlns="https://github.com/avaloniaui"
             xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
             xmlns:vm="using:MyApp.ViewModels"
             x:DataType="vm:LoginViewModel">
  <StackPanel Spacing="8">
    <TextBox Watermark="User name"
             Text="{CompiledBinding UserName, Mode=TwoWay}" />

    <TextBox Watermark="Password"
             PasswordChar="*"
             Text="{CompiledBinding Password, Mode=TwoWay}" />

    <ComboBox ItemsSource="{CompiledBinding Roles}"
              SelectedItem="{CompiledBinding SelectedRole, Mode=TwoWay}"
              IsEditable="True"
              IsTextSearchEnabled="True" />

    <AutoCompleteBox ItemsSource="{CompiledBinding Roles}"
                     MinimumPrefixLength="1"
                     Text="{CompiledBinding RoleSearch, Mode=TwoWay}"
                     SelectedItem="{CompiledBinding SelectedRole, Mode=TwoWay}" />
  </StackPanel>
</UserControl>
```

## Avalonia C# Equivalent

```csharp
using Avalonia.Controls;

var user = new TextBox { Watermark = "User name", Text = viewModel.UserName };

var password = new TextBox
{
    Watermark = "Password",
    PasswordChar = '*',
    Text = viewModel.Password
};

var role = new ComboBox
{
    ItemsSource = viewModel.Roles,
    SelectedItem = viewModel.SelectedRole,
    IsEditable = true,
    IsTextSearchEnabled = true
};

var roleSearch = new AutoCompleteBox
{
    ItemsSource = viewModel.Roles,
    MinimumPrefixLength = 1,
    Text = viewModel.RoleSearch,
    SelectedItem = viewModel.SelectedRole
};
```

## Troubleshooting

1. Migrated password flow is less secure than expected.
- keep sensitive values out of long-lived strings and centralize secure-entry handling.

2. Editable combo behavior differs.
- start with `ComboBox IsEditable`/`IsTextSearchEnabled`; use `AutoCompleteBox` when custom filtering/population behavior is required.

3. Form entry lags during validation.
- debounce expensive validation and keep UI-thread work minimal.
