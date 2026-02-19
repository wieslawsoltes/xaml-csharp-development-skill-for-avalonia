# WinForms Validation, ErrorProvider, and Data Errors to Avalonia

## Table of Contents
1. Scope and APIs
2. Validation Mapping
3. Conversion Example
4. C# Equivalent
5. Troubleshooting

## Scope and APIs

Primary WinForms APIs:

- `ErrorProvider` (`SetError`, `GetError`, `DataSource`, `DataMember`)
- `Validating` / `Validated` events

Primary Avalonia APIs:

- `INotifyDataErrorInfo`
- binding validation pipeline
- `DataValidationErrors` attached properties and error templates

## Validation Mapping

| WinForms | Avalonia |
|---|---|
| `ErrorProvider.SetError(control, message)` | validation errors from binding source (`INotifyDataErrorInfo`) |
| `Validating` event | validation in view-model setters/commands |
| per-control error glyph | style/template using `DataValidationErrors` |

## Conversion Example

WinForms C#:

```csharp
var errors = new ErrorProvider();

emailTextBox.Validating += (_, e) =>
{
    if (!emailTextBox.Text.Contains("@"))
    {
        errors.SetError(emailTextBox, "Invalid email address");
        e.Cancel = true;
    }
    else
    {
        errors.SetError(emailTextBox, string.Empty);
    }
};
```

Avalonia XAML:

```xaml
<UserControl xmlns="https://github.com/avaloniaui"
             xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
             xmlns:vm="using:MyApp.ViewModels"
             x:DataType="vm:ProfileViewModel">
  <StackPanel Spacing="6">
    <TextBlock Text="Email" />
    <TextBox x:Name="EmailBox" Text="{CompiledBinding Email, Mode=TwoWay}" />
    <TextBlock Classes="error"
               IsVisible="{Binding (DataValidationErrors.HasErrors), ElementName=EmailBox}"
               Text="Invalid email address" />
  </StackPanel>
</UserControl>
```

Avalonia C#:

```csharp
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
        => propertyName is not null && _errors.TryGetValue(propertyName, out var list) ? list : new List<string>();

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

1. No validation message appears.
- ensure bindings are two-way and model implements `INotifyDataErrorInfo` correctly.

2. Errors stay after valid input.
- clear previous errors and raise `ErrorsChanged` for the same property.

3. Validation logic still lives in code-behind events.
- move rules into view-model properties or command preconditions.
