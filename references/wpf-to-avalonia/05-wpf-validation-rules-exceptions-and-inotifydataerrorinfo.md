# WPF Validation Rules, Exceptions, and INotifyDataErrorInfo to Avalonia

## Table of Contents
1. Scope and APIs
2. Validation Mapping
3. Conversion Example
4. Avalonia C# Equivalent
5. Troubleshooting

## Scope and APIs

Primary WPF APIs:

- `ValidationRule`
- `ExceptionValidationRule`, `DataErrorValidationRule`
- `INotifyDataErrorInfo`

Primary Avalonia APIs:

- binding validation pipeline
- `INotifyDataErrorInfo`
- `DataValidationErrors` attached properties and templates

## Validation Mapping

| WPF | Avalonia |
|---|---|
| `ValidationRule` in binding | view-model validation + `INotifyDataErrorInfo` |
| `Validation.HasError` | `DataValidationErrors.HasErrors` |
| bound error list | `DataValidationErrors.Errors` |

## Conversion Example

WPF XAML:

```xaml
<TextBox>
  <TextBox.Text>
    <Binding Path="Email" UpdateSourceTrigger="PropertyChanged">
      <Binding.ValidationRules>
        <local:EmailRule />
      </Binding.ValidationRules>
    </Binding>
  </TextBox.Text>
</TextBox>
```

Avalonia XAML:

```xaml
<UserControl xmlns="https://github.com/avaloniaui"
             xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
             xmlns:vm="using:MyApp.ViewModels"
             x:DataType="vm:ProfileViewModel">
  <StackPanel Spacing="6">
    <TextBox x:Name="EmailBox"
             Text="{CompiledBinding Email, Mode=TwoWay, UpdateSourceTrigger=PropertyChanged}" />
    <TextBlock Classes="error"
               IsVisible="{Binding (DataValidationErrors.HasErrors), ElementName=EmailBox}"
               Text="Invalid email address" />
  </StackPanel>
</UserControl>
```

## Avalonia C# Equivalent

```csharp
using System;
using System.Collections;
using System.Collections.Generic;
using System.ComponentModel;

public sealed class ProfileViewModel : INotifyPropertyChanged, INotifyDataErrorInfo
{
    private readonly Dictionary<string, List<string>> _errors = new();
    private string _email = string.Empty;

    public string Email
    {
        get => _email;
        set
        {
            if (_email == value)
                return;

            _email = value;
            ValidateEmail();
            PropertyChanged?.Invoke(this, new PropertyChangedEventArgs(nameof(Email)));
        }
    }

    public bool HasErrors => _errors.Count > 0;
    public event PropertyChangedEventHandler? PropertyChanged;
    public event EventHandler<DataErrorsChangedEventArgs>? ErrorsChanged;

    public IEnumerable GetErrors(string? propertyName)
        => propertyName is not null && _errors.TryGetValue(propertyName, out var e) ? e : new List<string>();

    private void ValidateEmail()
    {
        _errors.Remove(nameof(Email));
        if (!_email.Contains("@"))
            _errors[nameof(Email)] = new List<string> { "Invalid email address" };

        ErrorsChanged?.Invoke(this, new DataErrorsChangedEventArgs(nameof(Email)));
    }
}
```

## Troubleshooting

1. Errors do not appear in UI.
- verify `INotifyDataErrorInfo` is implemented and `ErrorsChanged` is raised.

2. Validation runs only on focus loss.
- use `UpdateSourceTrigger=PropertyChanged` where immediate feedback is required.

3. exceptions escape binding updates.
- move validation into model/view-model and avoid relying on exception flow for normal validation.
