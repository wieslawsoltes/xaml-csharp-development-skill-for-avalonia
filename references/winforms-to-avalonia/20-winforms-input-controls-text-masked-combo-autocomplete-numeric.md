# WinForms Input Controls (Text, Masked, Combo, AutoComplete, Numeric) to Avalonia

## Table of Contents
1. Scope and APIs
2. Input Control Mapping
3. Conversion Example
4. C# Equivalent
5. Troubleshooting

## Scope and APIs

Primary WinForms APIs:

- `TextBox`, `MaskedTextBox`
- `ComboBox` (`DropDownStyle`, autocomplete modes)
- `NumericUpDown`

Primary Avalonia APIs:

- `TextBox`, `MaskedTextBox`
- `ComboBox`, `AutoCompleteBox`
- `NumericUpDown`

## Input Control Mapping

| WinForms | Avalonia |
|---|---|
| `TextBox` | `TextBox` |
| `MaskedTextBox` | `MaskedTextBox` (`Mask`, prompt/mask properties) |
| `ComboBox` + autocomplete | `ComboBox` or `AutoCompleteBox` |
| `NumericUpDown` | `NumericUpDown` |

## Conversion Example

WinForms C#:

```csharp
var phone = new MaskedTextBox("(999) 000-0000");
phone.Text = customer.Phone;

var role = new ComboBox
{
    DropDownStyle = ComboBoxStyle.DropDownList,
    DataSource = roles
};

var priority = new NumericUpDown
{
    Minimum = 0,
    Maximum = 10,
    Increment = 1,
    Value = 3
};
```

Avalonia XAML:

```xaml
<UserControl xmlns="https://github.com/avaloniaui"
             xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
             xmlns:vm="using:MyApp.ViewModels"
             x:DataType="vm:OrderEditorViewModel">
  <Grid RowDefinitions="Auto,Auto,Auto,Auto" RowSpacing="8">
    <TextBox Grid.Row="0"
             Watermark="Customer name"
             Text="{CompiledBinding CustomerName, Mode=TwoWay}" />

    <MaskedTextBox Grid.Row="1"
                   Mask="(000) 000-0000"
                   Text="{CompiledBinding Phone, Mode=TwoWay}" />

    <AutoCompleteBox Grid.Row="2"
                     ItemsSource="{CompiledBinding CountrySuggestions}"
                     MinimumPrefixLength="1"
                     IsTextCompletionEnabled="True"
                     Text="{CompiledBinding Country, Mode=TwoWay}" />

    <NumericUpDown Grid.Row="3"
                   Minimum="0"
                   Maximum="10"
                   Increment="1"
                   Value="{CompiledBinding Priority, Mode=TwoWay}" />
  </Grid>
</UserControl>
```

## C# Equivalent

```csharp
using Avalonia.Controls;

var phone = new MaskedTextBox
{
    Mask = "(000) 000-0000",
    Text = viewModel.Phone
};

var country = new AutoCompleteBox
{
    ItemsSource = viewModel.CountrySuggestions,
    MinimumPrefixLength = 1,
    IsTextCompletionEnabled = true,
    Text = viewModel.Country
};

var priority = new NumericUpDown
{
    Minimum = 0,
    Maximum = 10,
    Increment = 1,
    Value = viewModel.Priority
};
```

## Troubleshooting

1. Masked input accepts unexpected characters.
- verify `Mask`, `AsciiOnly`, and prompt/reset settings on `MaskedTextBox`.

2. Combo/autocomplete behavior feels different.
- use `AutoCompleteBox` when free typing + suggestion filtering is required.

3. Numeric value does not update view-model.
- bind `Value` in `TwoWay` mode and keep model type compatible with decimal values.
