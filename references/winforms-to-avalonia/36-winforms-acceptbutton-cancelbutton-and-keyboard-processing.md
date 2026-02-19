# WinForms AcceptButton, CancelButton, and Keyboard Processing to Avalonia

## Table of Contents
1. Scope and APIs
2. Keyboard and Dialog Mapping
3. Conversion Example
4. C# Equivalent
5. Troubleshooting

## Scope and APIs

Primary WinForms APIs:

- `Form.AcceptButton`, `Form.CancelButton`
- `Form.KeyPreview`
- `ProcessCmdKey(...)`

Primary Avalonia APIs:

- `Button.IsDefault`, `Button.IsCancel`
- `Window.KeyBindings` + `KeyBinding`/`KeyGesture`
- routed key events (`InputElement.KeyDownEvent`) for custom fallback logic

## Keyboard and Dialog Mapping

| WinForms | Avalonia |
|---|---|
| `AcceptButton` | `Button IsDefault="True"` |
| `CancelButton` | `Button IsCancel="True"` |
| `KeyPreview` + form-level key interception | `Window.KeyBindings` and routed key handlers |
| `ProcessCmdKey` overrides | command routing + explicit `KeyDown` handling only for edge cases |

## Conversion Example

WinForms C#:

```csharp
AcceptButton = saveButton;
CancelButton = cancelButton;
KeyPreview = true;

protected override bool ProcessCmdKey(ref Message msg, Keys keyData)
{
    if (keyData == (Keys.Control | Keys.S))
    {
        Save();
        return true;
    }

    return base.ProcessCmdKey(ref msg, keyData);
}
```

Avalonia XAML:

```xaml
<Window xmlns="https://github.com/avaloniaui"
        xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
        xmlns:vm="using:MyApp.ViewModels"
        x:Class="MyApp.Views.EditCustomerWindow"
        x:DataType="vm:EditCustomerViewModel"
        Width="560"
        Height="360"
        Title="Edit Customer">
  <Window.KeyBindings>
    <KeyBinding Gesture="Ctrl+S"
                Command="{CompiledBinding SaveCommand}" />
  </Window.KeyBindings>

  <Grid RowDefinitions="*,Auto" Margin="12" RowSpacing="12">
    <TextBox AcceptsReturn="True"
             TextWrapping="Wrap"
             Text="{CompiledBinding Notes, Mode=TwoWay}" />

    <StackPanel Grid.Row="1"
                Orientation="Horizontal"
                HorizontalAlignment="Right"
                Spacing="8">
      <Button Content="Cancel"
              IsCancel="True"
              Command="{CompiledBinding CancelCommand}" />
      <Button Content="Save"
              IsDefault="True"
              Command="{CompiledBinding SaveCommand}" />
    </StackPanel>
  </Grid>
</Window>
```

## C# Equivalent

```csharp
using Avalonia.Controls;
using Avalonia.Input;
using Avalonia.Interactivity;

var dialog = new Window
{
    Width = 560,
    Height = 360,
    Title = "Edit Customer"
};

dialog.KeyBindings.Add(new KeyBinding
{
    Gesture = KeyGesture.Parse("Ctrl+S"),
    Command = viewModel.SaveCommand
});

dialog.AddHandler(InputElement.KeyDownEvent, (_, e) =>
{
    if (e.KeyModifiers == KeyModifiers.Control && e.Key == Key.S)
    {
        viewModel.SaveCommand.Execute(null);
        e.Handled = true;
    }
}, RoutingStrategies.Tunnel);

var cancel = new Button
{
    Content = "Cancel",
    IsCancel = true,
    Command = viewModel.CancelCommand
};

var save = new Button
{
    Content = "Save",
    IsDefault = true,
    Command = viewModel.SaveCommand
};
```

## Troubleshooting

1. Enter/Escape do not trigger expected actions.
- confirm `IsDefault`/`IsCancel` are set on buttons inside the active `Window`.

2. Keyboard shortcuts work in some controls but not others.
- prefer `Window.KeyBindings` for primary gestures and use routed key handlers only for exceptions.

3. Migrated `ProcessCmdKey` logic is too broad.
- move command logic to view model and keep key handling thin, explicit, and testable.
