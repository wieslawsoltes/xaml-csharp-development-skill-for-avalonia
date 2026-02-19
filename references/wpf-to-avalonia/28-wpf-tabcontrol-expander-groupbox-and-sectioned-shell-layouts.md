# WPF TabControl, Expander, GroupBox, and Sectioned Shell Layouts to Avalonia

## Table of Contents
1. Scope and APIs
2. Sectioned Layout Mapping
3. Conversion Example
4. Avalonia C# Equivalent
5. Troubleshooting

## Scope and APIs

Primary WPF APIs:

- `TabControl`/`TabItem`
- `Expander`
- `GroupBox`

Primary Avalonia APIs:

- `TabControl`
- `Expander`
- `GroupBox`
- view-model-driven tab/document collections

## Sectioned Layout Mapping

| WPF | Avalonia |
|---|---|
| `TabControl.Items`/`SelectedItem` | same concept with `ItemsSource` + bindings |
| `TabItem Header` | header via `ItemTemplate` |
| `Expander` sections | same control and interaction pattern |
| `GroupBox` labeled blocks | same control |

## Conversion Example

WPF XAML:

```xaml
<TabControl SelectedItem="{Binding ActiveTab}">
  <TabItem Header="General">
    <GroupBox Header="Identity">
      <TextBox Text="{Binding Name}" />
    </GroupBox>
  </TabItem>
</TabControl>
```

Avalonia XAML:

```xaml
<UserControl xmlns="https://github.com/avaloniaui"
             xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
             xmlns:vm="using:MyApp.ViewModels"
             x:DataType="vm:SettingsShellViewModel">
  <TabControl ItemsSource="{CompiledBinding Tabs}"
              SelectedItem="{CompiledBinding ActiveTab}">
    <TabControl.ItemTemplate>
      <DataTemplate x:DataType="vm:SettingsTabViewModel">
        <TextBlock Text="{CompiledBinding Header}" />
      </DataTemplate>
    </TabControl.ItemTemplate>

    <TabControl.ContentTemplate>
      <DataTemplate x:DataType="vm:SettingsTabViewModel">
        <Expander Header="{CompiledBinding SectionTitle}" IsExpanded="True">
          <GroupBox Header="Identity">
            <TextBox Text="{CompiledBinding Name, Mode=TwoWay}" />
          </GroupBox>
        </Expander>
      </DataTemplate>
    </TabControl.ContentTemplate>
  </TabControl>
</UserControl>
```

## Avalonia C# Equivalent

```csharp
using Avalonia.Controls;

var tabs = new TabControl
{
    ItemsSource = viewModel.Tabs,
    SelectedItem = viewModel.ActiveTab
};

var group = new GroupBox { Header = "Identity", Content = new TextBox { Text = viewModel.Name } };
var section = new Expander { Header = "General", IsExpanded = true, Content = group };
```

## Troubleshooting

1. Tab content is recreated unexpectedly.
- keep stable tab view-model identities and avoid replacing entire collections.

2. Expander state resets on data refresh.
- persist section expansion state in the view model.

3. Group layouts become dense after migration.
- combine `GroupBox` with explicit spacing/margins instead of implicit defaults.
