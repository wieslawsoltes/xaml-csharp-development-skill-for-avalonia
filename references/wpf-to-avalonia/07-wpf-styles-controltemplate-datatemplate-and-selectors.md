# WPF Styles, ControlTemplate, DataTemplate, and Selectors to Avalonia

## Table of Contents
1. Scope and APIs
2. Template/Style Mapping
3. Conversion Example
4. Avalonia C# Equivalent
5. Troubleshooting

## Scope and APIs

Primary WPF APIs:

- `Style`, `BasedOn`
- `ControlTemplate`, `DataTemplate`
- `TemplateBinding`

Primary Avalonia APIs:

- `Style` with selectors
- `ControlTheme`
- `ControlTemplate`, `DataTemplate`
- `TemplateBinding`

## Template/Style Mapping

| WPF | Avalonia |
|---|---|
| `Style TargetType="Button"` | `Style Selector="Button"` |
| `BasedOn` style chains | style layering/ordering + theme composition |
| `ControlTemplate` | `ControlTemplate` |
| `DataTemplate` | `DataTemplate` |
| `TemplateBinding` | `TemplateBinding` |

## Conversion Example

WPF XAML:

```xaml
<Style TargetType="Button">
  <Setter Property="Padding" Value="12,6" />
  <Setter Property="Template">
    <Setter.Value>
      <ControlTemplate TargetType="Button">
        <Border Background="{TemplateBinding Background}" CornerRadius="6">
          <ContentPresenter HorizontalAlignment="Center" VerticalAlignment="Center" />
        </Border>
      </ControlTemplate>
    </Setter.Value>
  </Setter>
</Style>
```

Avalonia XAML:

```xaml
<Style xmlns="https://github.com/avaloniaui" Selector="Button.rounded">
  <Setter Property="Padding" Value="12,6" />
  <Setter Property="Template">
    <ControlTemplate>
      <Border Background="{TemplateBinding Background}" CornerRadius="6">
        <ContentPresenter HorizontalAlignment="Center"
                          VerticalAlignment="Center"
                          Content="{TemplateBinding Content}"
                          ContentTemplate="{TemplateBinding ContentTemplate}" />
      </Border>
    </ControlTemplate>
  </Setter>
</Style>
```

Data template sample:

```xaml
<ListBox xmlns="https://github.com/avaloniaui"
         xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
         xmlns:vm="using:MyApp.ViewModels"
         x:DataType="vm:UsersPageViewModel"
         ItemsSource="{CompiledBinding Users}">
  <ListBox.ItemTemplate>
    <DataTemplate x:DataType="vm:UserViewModel">
      <TextBlock Text="{CompiledBinding Name}" />
    </DataTemplate>
  </ListBox.ItemTemplate>
</ListBox>
```

## Avalonia C# Equivalent

```csharp
using Avalonia.Controls;
using Avalonia.Controls.Templates;

var list = new ListBox
{
    ItemsSource = viewModel.Users,
    ItemTemplate = new FuncDataTemplate<UserViewModel>((item, _) => new TextBlock { Text = item.Name })
};
```

## Troubleshooting

1. Template ports lose behavior.
- preserve required template parts and pseudo-class expectations.

2. Style applies too broadly.
- narrow with explicit selectors and classes.

3. Data templates recreate heavy visuals.
- simplify template tree and keep item visuals lightweight.
