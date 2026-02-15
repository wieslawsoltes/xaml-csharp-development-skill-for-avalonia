# Validation Pipeline and Data Errors

## Table of Contents
1. Scope and APIs
2. Validation Pipeline
3. Authoring Patterns
4. AOT and Trimming Guidance
5. Troubleshooting

## Scope and APIs

Primary APIs:
- `AvaloniaPropertyMetadata.EnableDataValidation`
- `AvaloniaProperty.Register(..., enableDataValidation: true)`
- `DataValidationErrors`
- `BindingNotification`
- `BindingErrorType`
- `DataValidationException`
- `BindingPlugins.DataValidators`

Important members:
- `DataValidationErrors.ErrorsProperty`, `HasErrorsProperty`, `ErrorConverterProperty`
- `DataValidationErrors.GetErrors(...)`, `SetErrors(...)`, `SetError(...)`, `ClearErrors(...)`
- `BindingNotification.Error`, `ErrorType`, `Value`, `HasValue`
- `BindingNotification.ExtractValue(...)`, `ExtractError(...)`, `UpdateValue(...)`
- `DataValidationException.ErrorData`

Reference source files:
- `src/Avalonia.Base/AvaloniaPropertyMetadata.cs`
- `src/Avalonia.Controls/DataValidationErrors.cs`
- `src/Avalonia.Base/Data/BindingNotification.cs`
- `src/Avalonia.Base/Data/DataValidationException.cs`
- `src/Avalonia.Base/Data/Core/Plugins/BindingPlugins.cs`
- `src/Avalonia.Base/Data/Core/Plugins/DataAnnotationsValidationPlugin.cs`

## Validation Pipeline

Practical flow for control-bound validation:
1. Target property opts into validation (`enableDataValidation: true`).
2. Binding emits value or validation error (`BindingNotification` / exceptions).
3. Control receives validation state update.
4. `DataValidationErrors` attached state is updated (`Errors`, `HasErrors`).
5. Templates/styles use `:error` state and error collections for UX.

## Authoring Patterns

### Enable validation on a custom property

```csharp
using Avalonia;
using Avalonia.Data;

public class EmailEditor : Avalonia.Controls.TemplatedControl
{
    public static readonly StyledProperty<string?> EmailProperty =
        AvaloniaProperty.Register<EmailEditor, string?>(
            nameof(Email),
            defaultBindingMode: BindingMode.TwoWay,
            enableDataValidation: true);

    public string? Email
    {
        get => GetValue(EmailProperty);
        set => SetValue(EmailProperty, value);
    }
}
```

### Data annotations plugin registration (11.3.12)

`DataAnnotationsValidationPlugin` is registered by default in `BindingPlugins.DataValidators`, so no `AppBuilder` extension call is required.

```csharp
AppBuilder.Configure<App>()
    .UsePlatformDetect()
    .StartWithClassicDesktopLifetime(args);
```

### Surface errors with `DataValidationErrors`

```csharp
if (DataValidationErrors.GetHasErrors(textBox))
{
    var errors = DataValidationErrors.GetErrors(textBox);
    // Render or log errors.
}
```

### Convert error payloads for UX

```csharp
DataValidationErrors.SetErrorConverter(textBox, error =>
{
    return error is Exception ex ? ex.Message : error;
});
```

## AOT and Trimming Guidance

- `DataAnnotationsValidationPlugin` relies on reflection and is trimming-sensitive.
- For NativeAOT-sensitive apps, prefer explicit validation via `INotifyDataErrorInfo` patterns and compiled bindings.
- Keep validation logic in viewmodels/services, not UI code-behind.

## Troubleshooting

1. Validation never appears on UI:
- Target property does not enable validation metadata.
- Control template does not expose or style `DataValidationErrors` state.

2. Errors exist but message is unreadable:
- Error objects need conversion; set `ErrorConverter`.

3. DataAnnotations does not run:
- `DataAnnotationsValidationPlugin` was removed from `BindingPlugins.DataValidators`.
- Trimmed build removed needed metadata.

4. Error state does not clear:
- Binding never emits successful value after failure.
- Stale custom errors were set manually and not cleared.

## XAML-First and Code-Only Usage

Default mode:
- Surface validation states in XAML with bindings and styles first.
- Use code-only validation wiring only when requested.

XAML-first references:
- `TextBox`/input bindings with compiled binding
- `DataValidationErrors` styling and error templates

XAML-first usage example:

```xml
<TextBox xmlns="https://github.com/avaloniaui"
         xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
         Text="{CompiledBinding Email, Mode=TwoWay}" />
```

Code-only alternative (on request):

```csharp
textBox.Bind(TextBox.TextProperty, new Binding(nameof(EditUserViewModel.Email))
{
    Mode = BindingMode.TwoWay
});

if (DataValidationErrors.GetHasErrors(textBox))
    LogValidation(textBox, DataValidationErrors.GetErrors(textBox));
```
