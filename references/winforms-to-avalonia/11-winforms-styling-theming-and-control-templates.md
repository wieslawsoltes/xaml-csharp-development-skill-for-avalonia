# WinForms Styling, Theming, and Control Templates to Avalonia

## Table of Contents
1. Scope and APIs
2. Styling Model Mapping
3. Conversion Example
4. C# Equivalent
5. Troubleshooting

## Scope and APIs

Primary WinForms APIs:

- per-control styling (`BackColor`, `ForeColor`, `Font`)
- custom visual tweaks in designer/code

Primary Avalonia APIs:

- `Style` selectors and classes
- `ControlTheme`
- resources (`StaticResource`, dynamic resource patterns)
- pseudo-classes (`:pointerover`, `:pressed`, `:focus`)

## Styling Model Mapping

| WinForms | Avalonia |
|---|---|
| set color/font on each control | reusable styles and resource dictionaries |
| designer theme drift | centralized theme resources |
| owner-draw for simple states | pseudo-class selectors and templates |

## Conversion Example

WinForms C#:

```csharp
saveButton.BackColor = Color.FromArgb(20, 120, 200);
saveButton.ForeColor = Color.White;
saveButton.FlatStyle = FlatStyle.Flat;
```

Avalonia XAML:

```xaml
<Styles xmlns="https://github.com/avaloniaui"
        xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml">
  <Styles.Resources>
    <Color x:Key="AccentColor">#1478C8</Color>
    <SolidColorBrush x:Key="AccentBrush" Color="{StaticResource AccentColor}" />
  </Styles.Resources>

  <Style Selector="Button.accent">
    <Setter Property="Background" Value="{StaticResource AccentBrush}" />
    <Setter Property="Foreground" Value="White" />
    <Setter Property="Padding" Value="12,6" />
  </Style>

  <Style Selector="Button.accent:pointerover">
    <Setter Property="Opacity" Value="0.9" />
  </Style>
</Styles>

<Button Classes="accent" Content="Save" />
```

## C# Equivalent

```csharp
using Avalonia.Controls;
using Avalonia.Media;

var save = new Button
{
    Content = "Save",
    Background = new SolidColorBrush(Color.Parse("#1478C8")),
    Foreground = Brushes.White,
    Padding = new Avalonia.Thickness(12, 6)
};
save.Classes.Add("accent");
```

## Troubleshooting

1. Styling logic copied per control from WinForms.
- move recurring values to resources and styles.

2. Hover/pressed visuals regress.
- use pseudo-class selectors instead of event-based color toggling.

3. Template overrides break accessibility or behavior.
- keep control contracts intact and modify visuals through theme parts only.
