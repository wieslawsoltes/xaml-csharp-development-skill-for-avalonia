# WPF MultiBinding, StringFormat, and PriorityBinding Fallback Patterns to Avalonia

## Table of Contents
1. Scope and APIs
2. Binding Aggregation Mapping
3. Conversion Example
4. Avalonia C# Equivalent
5. Troubleshooting

## Scope and APIs

Primary WPF APIs:

- `MultiBinding`
- `IMultiValueConverter`
- `PriorityBinding`

Primary Avalonia APIs:

- `MultiBinding`
- `IMultiValueConverter`
- `MultiBinding.StringFormat`, `FallbackValue`, `TargetNullValue`

`PriorityBinding` does not have a direct built-in equivalent in Avalonia `11.3.12`.

## Binding Aggregation Mapping

| WPF | Avalonia |
|---|---|
| `MultiBinding` + converter | `MultiBinding` + `IMultiValueConverter` |
| `MultiBinding StringFormat` | `MultiBinding StringFormat` |
| `PriorityBinding` fallback chain | computed VM property or `MultiBinding` first-value converter |

## Conversion Example

WPF XAML:

```xaml
<TextBlock>
  <TextBlock.Text>
    <PriorityBinding>
      <Binding Path="PreferredDisplayName" />
      <Binding Path="UserName" />
      <Binding Path="Email" />
    </PriorityBinding>
  </TextBlock.Text>
</TextBlock>
```

Avalonia XAML:

```xaml
<UserControl xmlns="https://github.com/avaloniaui"
             xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
             xmlns:vm="using:MyApp.ViewModels"
             xmlns:conv="using:MyApp.Converters"
             x:DataType="vm:UserBadgeViewModel">
  <UserControl.Resources>
    <conv:FirstNonEmptyConverter x:Key="FirstNonEmptyConverter" />
  </UserControl.Resources>

  <StackPanel Spacing="6">
    <TextBlock>
      <TextBlock.Text>
        <MultiBinding StringFormat="{}{0} {1}" FallbackValue="(unknown)">
          <Binding Path="FirstName" />
          <Binding Path="LastName" />
        </MultiBinding>
      </TextBlock.Text>
    </TextBlock>

    <TextBlock>
      <TextBlock.Text>
        <MultiBinding Converter="{StaticResource FirstNonEmptyConverter}" FallbackValue="(unknown)">
          <Binding Path="PreferredDisplayName" />
          <Binding Path="UserName" />
          <Binding Path="Email" />
        </MultiBinding>
      </TextBlock.Text>
    </TextBlock>
  </StackPanel>
</UserControl>
```

## Avalonia C# Equivalent

```csharp
using System;
using System.Collections.Generic;
using System.Globalization;
using Avalonia;
using Avalonia.Controls;
using Avalonia.Data;
using Avalonia.Data.Converters;

public sealed class FirstNonEmptyConverter : IMultiValueConverter
{
    public object? Convert(IList<object?> values, Type targetType, object? parameter, CultureInfo culture)
    {
        foreach (var value in values)
        {
            if (value is string s && !string.IsNullOrWhiteSpace(s))
                return s;
        }

        return AvaloniaProperty.UnsetValue;
    }
}

var nameText = new TextBlock();
nameText.Bind(TextBlock.TextProperty, new MultiBinding
{
    StringFormat = "{0} {1}",
    Bindings = { new Binding("FirstName"), new Binding("LastName") }
});

var displayText = new TextBlock();
displayText.Bind(TextBlock.TextProperty, new MultiBinding
{
    Converter = new FirstNonEmptyConverter(),
    Bindings =
    {
        new Binding("PreferredDisplayName"),
        new Binding("UserName"),
        new Binding("Email")
    }
});
```

## Troubleshooting

1. Expected `PriorityBinding` behavior is missing.
- Replace with a VM-computed property or `MultiBinding` + first-non-empty converter.

2. MultiBinding never updates.
- Check each child binding path and ensure the sources raise property notifications.

3. Converter throws at runtime.
- Return `AvaloniaProperty.UnsetValue` for unsupported combinations instead of throwing.
