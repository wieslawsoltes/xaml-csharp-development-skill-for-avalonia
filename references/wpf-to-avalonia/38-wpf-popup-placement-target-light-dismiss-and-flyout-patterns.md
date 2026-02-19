# WPF Popup Placement, Target, Light-Dismiss, and Flyout Patterns to Avalonia

## Table of Contents
1. Scope and APIs
2. Popup/Flyout Mapping
3. Conversion Example
4. Avalonia C# Equivalent
5. Troubleshooting

## Scope and APIs

Primary WPF APIs:

- `Popup` (`PlacementTarget`, `Placement`, `StaysOpen`)
- `ContextMenu`/transient surface patterns

Primary Avalonia APIs:

- `Popup` (`PlacementTarget`, `Placement`, `IsLightDismissEnabled`, offsets)
- `Flyout`/`FlyoutBase` (`ShowAt`, attached flyouts)
- `Button.Flyout`, `Control.ContextFlyout`

## Popup/Flyout Mapping

| WPF | Avalonia |
|---|---|
| `Popup StaysOpen="False"` | `Popup IsLightDismissEnabled="True"` |
| `PlacementTarget` + `Placement` | `PlacementTarget` + `Placement` + anchor/gravity options |
| ad-hoc popup menus | `Flyout`, `MenuFlyout`, `ContextFlyout` |

## Conversion Example

WPF XAML:

```xaml
<Grid>
  <Button x:Name="HelpButton" Content="Help" />
  <Popup IsOpen="{Binding IsHelpOpen}"
         PlacementTarget="{Binding ElementName=HelpButton}"
         Placement="Bottom"
         StaysOpen="False">
    <Border Padding="8">
      <TextBlock Text="Context help." />
    </Border>
  </Popup>
</Grid>
```

Avalonia XAML:

```xaml
<UserControl xmlns="https://github.com/avaloniaui"
             xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
             xmlns:vm="using:MyApp.ViewModels"
             x:DataType="vm:HelpSurfaceViewModel">
  <Grid RowDefinitions="Auto,Auto" RowSpacing="8">
    <Button x:Name="HelpButton"
            Grid.Row="0"
            Content="Help"
            Command="{CompiledBinding ToggleHelpCommand}" />

    <Popup Grid.Row="0"
           IsOpen="{CompiledBinding IsHelpOpen, Mode=TwoWay}"
           PlacementTarget="{Binding #HelpButton}"
           Placement="Bottom"
           HorizontalOffset="4"
           VerticalOffset="4"
           IsLightDismissEnabled="True">
      <Border Padding="8">
        <TextBlock Text="{CompiledBinding HelpText}" />
      </Border>
    </Popup>

    <Button Grid.Row="1" Content="Actions">
      <Button.Flyout>
        <Flyout Placement="Bottom">
          <StackPanel Spacing="6">
            <Button Content="Open" Command="{CompiledBinding OpenCommand}" />
            <Button Content="Delete" Command="{CompiledBinding DeleteCommand}" />
          </StackPanel>
        </Flyout>
      </Button.Flyout>
    </Button>
  </Grid>
</UserControl>
```

## Avalonia C# Equivalent

```csharp
using Avalonia;
using Avalonia.Controls;
using Avalonia.Controls.Primitives;

var anchor = new Button { Content = "Help" };

var popup = new Popup
{
    PlacementTarget = anchor,
    Placement = PlacementMode.Bottom,
    HorizontalOffset = 4,
    VerticalOffset = 4,
    IsLightDismissEnabled = true,
    Child = new Border
    {
        Padding = new Thickness(8),
        Child = new TextBlock { Text = "Context help." }
    }
};

var flyout = new Flyout
{
    Content = new StackPanel
    {
        Spacing = 6,
        Children =
        {
            new Button { Content = "Open", Command = viewModel.OpenCommand },
            new Button { Content = "Delete", Command = viewModel.DeleteCommand }
        }
    }
};

anchor.Flyout = flyout;
```

## Troubleshooting

1. Popup appears in wrong location.
- Verify `PlacementTarget` is in the visual tree before opening.

2. Popup never closes on outside click.
- Set `IsLightDismissEnabled="True"` when replacing `StaysOpen="False"` behavior.

3. Flyout command surface looks inconsistent.
- Prefer `Flyout`/`MenuFlyout` for command UX instead of custom popup trees.
