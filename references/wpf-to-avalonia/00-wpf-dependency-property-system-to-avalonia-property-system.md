# WPF Dependency Property System to Avalonia Property System

## Table of Contents
1. Scope and APIs
2. Property System Mapping
3. Conversion Example
4. Avalonia C# Equivalent
5. AOT Notes
6. Troubleshooting

## Scope and APIs

Primary WPF APIs:

- `DependencyObject`, `DependencyProperty`
- `DependencyProperty.Register`, `RegisterAttached`, `RegisterReadOnly`
- `FrameworkPropertyMetadata`

Primary Avalonia APIs:

- `AvaloniaObject`, `AvaloniaProperty`
- `AvaloniaProperty.Register`, `RegisterAttached`, `RegisterDirect`
- `StyledProperty<T>`, `DirectProperty<TOwner, TValue>`

## Property System Mapping

| WPF | Avalonia |
|---|---|
| `DependencyProperty` | `AvaloniaProperty` |
| `FrameworkPropertyMetadata` | property registration options + changed callbacks |
| `RegisterReadOnly` | `DirectProperty` with private setter backing field |
| attached property via `RegisterAttached` | attached property via `AvaloniaProperty.RegisterAttached` |

## Conversion Example

WPF C#:

```csharp
public class HeaderCard : Control
{
    public static readonly DependencyProperty TitleProperty =
        DependencyProperty.Register(
            nameof(Title),
            typeof(string),
            typeof(HeaderCard),
            new FrameworkPropertyMetadata(string.Empty));

    public string Title
    {
        get => (string)GetValue(TitleProperty);
        set => SetValue(TitleProperty, value);
    }
}
```

Avalonia XAML usage:

```xaml
<local:HeaderCard xmlns="https://github.com/avaloniaui"
                  xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
                  xmlns:local="using:MyApp.Controls"
                  Title="Revenue" />
```

## Avalonia C# Equivalent

```csharp
using Avalonia;
using Avalonia.Controls;

public class HeaderCard : Control
{
    public static readonly StyledProperty<string> TitleProperty =
        AvaloniaProperty.Register<HeaderCard, string>(nameof(Title), string.Empty);

    public string Title
    {
        get => GetValue(TitleProperty);
        set => SetValue(TitleProperty, value);
    }
}
```

Attached property pattern:

```csharp
public static readonly AttachedProperty<bool> IsHighlightedProperty =
    AvaloniaProperty.RegisterAttached<HeaderCard, Control, bool>("IsHighlighted");
```

## AOT Notes

- keep property registrations strongly typed and static.
- avoid reflection-based property lookup when typed APIs are available.

## Troubleshooting

1. Property changes do not update style/template.
- ensure property is registered as `StyledProperty` and used in style selectors/setters.

2. read-only property migration fails.
- use `RegisterDirect` with explicit getter/setter backing field pattern.

3. attached property set/get methods missing.
- expose static helper methods for ergonomics where needed.
