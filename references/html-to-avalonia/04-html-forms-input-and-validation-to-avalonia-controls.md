# HTML Forms, Input, and Validation to Avalonia Controls

## Table of Contents
1. Scope and APIs
2. HTML Form Element Mapping
3. Validation Model Mapping
4. Accessibility/Semantics Mapping
5. Styled Form Comparison Example
6. End-to-End Form Conversion
7. C# Equivalent: End-to-End Form Conversion
8. Async Command and UI Thread Notes
9. Troubleshooting

## Scope and APIs

Primary APIs:

- input controls: `TextBox`, `MaskedTextBox`, `NumericUpDown`, `DatePicker`, `TimePicker`, `CheckBox`, `RadioButton`, `ComboBox`, `Slider`, `ToggleSwitch`
- command wiring: `ICommand`, `Button.Command`, hotkeys/gestures
- validation pipeline: `DataValidationErrors`, binding validation hooks
- accessibility: `AutomationProperties`

Reference docs:

- [`22-validation-pipeline-and-data-errors.md`](../22-validation-pipeline-and-data-errors)
- [`58-textbox-editing-clipboard-undo-and-input-options.md`](../58-textbox-editing-clipboard-undo-and-input-options)
- [`23-accessibility-and-automation.md`](../23-accessibility-and-automation)
- [`60-automation-properties-and-attached-behavior-patterns.md`](../60-automation-properties-and-attached-behavior-patterns)

## HTML Form Element Mapping

| HTML element/idiom | Avalonia control/pattern |
|---|---|
| `<input type="text">` | `TextBox Text` |
| `<input type="password">` | `TextBox PasswordChar` / `RevealPassword` |
| `<input type="number">` | `NumericUpDown` |
| `<input type="date">` | `DatePicker` |
| `<input type="time">` | `TimePicker` |
| `<input type="checkbox">` | `CheckBox` |
| `<input type="radio">` | `RadioButton` |
| `<select>` | `ComboBox` |
| `<textarea>` | `TextBox AcceptsReturn="True" TextWrapping="Wrap"` |
| `<label for="...">` | `Label Target="{Binding ElementName=...}"` or adjacent semantic labeling |

## Validation Model Mapping

| HTML validation idiom | Avalonia mapping |
|---|---|
| `required`, `minlength`, `pattern` | viewmodel/domain validation + binding validation |
| `:invalid` pseudo-state | `DataValidationErrors` template/styles |
| form submit prevention | command `CanExecute` and validation state |

Pattern:

1. keep authoritative rules in viewmodel/domain,
2. surface errors through validation interfaces,
3. style invalid controls with validation templates or classes.

## Accessibility/Semantics Mapping

| Web accessibility idiom | Avalonia mapping |
|---|---|
| `aria-label` | `AutomationProperties.Name` |
| `aria-describedby` | `AutomationProperties.HelpText` |
| `id` for automation | `AutomationProperties.AutomationId` |
| landmark role intent | logical layout + explicit control semantics and automation metadata |

## Styled Form Comparison Example

HTML/CSS:

```html
<form class="settings">
  <label for="displayName">Display Name</label>
  <input id="displayName" type="text" placeholder="Jane Doe">

  <label for="role">Role</label>
  <select id="role">
    <option>Admin</option>
    <option>Editor</option>
  </select>

  <button class="primary">Save</button>
</form>
```

```css
.settings {
  display: grid;
  grid-template-columns: 180px 1fr;
  gap: 10px 12px;
}
.settings input, .settings select {
  border: 1px solid #2a3348;
  border-radius: 8px;
  padding: 10px 12px;
}
.settings button.primary {
  grid-column: 2;
  justify-self: start;
}
```

Avalonia:

```xaml
<Grid ColumnDefinitions="180,*"
      RowDefinitions="Auto,Auto,Auto"
      ColumnSpacing="12"
      RowSpacing="10">
  <TextBlock Grid.Row="0" Grid.Column="0" Text="Display Name" VerticalAlignment="Center" />
  <TextBox Grid.Row="0" Grid.Column="1"
           Text="{CompiledBinding DisplayName}"
           Watermark="Jane Doe" />

  <TextBlock Grid.Row="1" Grid.Column="0" Text="Role" VerticalAlignment="Center" />
  <ComboBox Grid.Row="1" Grid.Column="1"
            ItemsSource="{CompiledBinding Roles}"
            SelectedItem="{CompiledBinding SelectedRole}" />

  <Button Grid.Row="2" Grid.Column="1"
          HorizontalAlignment="Left"
          Classes="primary"
          Content="Save"
          Command="{CompiledBinding SaveCommand}" />
</Grid>
```

## End-to-End Form Conversion

HTML:

```html
<form class="profile" novalidate>
  <label>Email</label>
  <input type="email" required>
  <label>Age</label>
  <input type="number" min="0" max="120">
  <button type="submit">Save</button>
</form>
```

Avalonia XAML:

```xaml
<StackPanel Spacing="10" x:DataType="vm:ProfileViewModel">
  <TextBlock Text="Email" />
  <TextBox Text="{CompiledBinding Email}" Watermark="name@example.com" />

  <TextBlock Text="Age" />
  <NumericUpDown Value="{CompiledBinding Age}" Minimum="0" Maximum="120" />

  <CheckBox IsChecked="{CompiledBinding AcceptTerms}" Content="Accept terms" />

  <Button Content="Save"
          Command="{CompiledBinding SaveCommand}"
          IsEnabled="{CompiledBinding CanSave}" />
</StackPanel>
```

Minimal viewmodel sketch:

```csharp
public sealed class ProfileViewModel
{
    public string? Email { get; set; }
    public decimal Age { get; set; }
    public bool AcceptTerms { get; set; }

    public bool CanSave =>
        !string.IsNullOrWhiteSpace(Email) &&
        Age is >= 0 and <= 120 &&
        AcceptTerms;
}
```

## C# Equivalent: End-to-End Form Conversion

```csharp
using Avalonia.Controls;

var profileForm = new StackPanel
{
    Spacing = 10
};

profileForm.Children.Add(new TextBlock { Text = "Email" });
profileForm.Children.Add(new TextBox { Watermark = "name@example.com" });

profileForm.Children.Add(new TextBlock { Text = "Age" });
profileForm.Children.Add(new NumericUpDown
{
    Minimum = 0,
    Maximum = 120
});

profileForm.Children.Add(new CheckBox { Content = "Accept terms" });
profileForm.Children.Add(new Button { Content = "Save" });
```

## Async Command and UI Thread Notes

- Execute network/storage work off UI thread.
- When mutating control-bound state from background operations, marshal back with `Dispatcher.UIThread`.
- Keep validation state deterministic to avoid flicker while async operations complete.

## Troubleshooting

1. `TextBox` password behavior differs from web field.
- Set `PasswordChar` and optional `RevealPassword`; do not bind plaintext mirrors unless required.

2. Validation visuals never appear.
- Confirm validation interfaces are implemented and binding enables validation.

3. Keyboard navigation feels inconsistent.
- Verify tab order, focusable elements, and command gesture conflicts.
