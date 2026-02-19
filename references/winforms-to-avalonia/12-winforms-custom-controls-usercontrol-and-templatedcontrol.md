# WinForms Custom Controls, UserControl, and TemplatedControl to Avalonia

## Table of Contents
1. Scope and APIs
2. Custom Control Mapping
3. Conversion Example
4. C# Equivalent
5. Troubleshooting

## Scope and APIs

Primary WinForms APIs:

- `UserControl`
- custom `Control` subclasses with custom properties and painting

Primary Avalonia APIs:

- `UserControl` for composition-first controls
- `TemplatedControl` for skinnable reusable controls
- Avalonia property system (`StyledProperty`, `DirectProperty`)

## Custom Control Mapping

| WinForms | Avalonia |
|---|---|
| `UserControl` with child controls | `UserControl` with XAML composition |
| custom `Control` + `OnPaint` | `TemplatedControl` + template + optional `Render` |
| CLR properties only | register Avalonia properties for styling/binding |

## Conversion Example

WinForms C#:

```csharp
public partial class HeaderPanel : UserControl
{
    public string TitleText
    {
        get => titleLabel.Text;
        set => titleLabel.Text = value;
    }
}
```

Avalonia XAML (`HeaderPanel.axaml`):

```xaml
<UserControl xmlns="https://github.com/avaloniaui"
             xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
             xmlns:local="using:MyApp.Controls"
             x:Class="MyApp.Controls.HeaderPanel">
  <Border Padding="8" Classes="header-panel">
    <TextBlock Text="{Binding TitleText, RelativeSource={RelativeSource AncestorType=local:HeaderPanel}}" />
  </Border>
</UserControl>
```

## C# Equivalent

```csharp
using Avalonia;
using Avalonia.Controls.Primitives;

public class HeaderPanel : TemplatedControl
{
    public static readonly StyledProperty<string> TitleTextProperty =
        AvaloniaProperty.Register<HeaderPanel, string>(nameof(TitleText), string.Empty);

    public string TitleText
    {
        get => GetValue(TitleTextProperty);
        set => SetValue(TitleTextProperty, value);
    }
}
```

A template for `HeaderPanel` can then be provided via `ControlTheme` in app styles.

## Troubleshooting

1. Custom property changes do not update UI.
- ensure values are Avalonia properties, not plain fields.

2. Reusable control cannot be restyled.
- migrate from composition-only control to `TemplatedControl` where needed.

3. Too much code-behind in custom user controls.
- move state and behavior to bindable properties and commands.
