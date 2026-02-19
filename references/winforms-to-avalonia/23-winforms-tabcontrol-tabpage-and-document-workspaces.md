# WinForms TabControl/TabPage and Document Workspaces to Avalonia

## Table of Contents
1. Scope and APIs
2. Tab Workspace Mapping
3. Conversion Example
4. C# Equivalent
5. Troubleshooting

## Scope and APIs

Primary WinForms APIs:

- `TabControl`
- `TabPage`

Primary Avalonia APIs:

- `TabControl`
- item/content templates for tab headers and content
- view-model-driven document collections

## Tab Workspace Mapping

| WinForms | Avalonia |
|---|---|
| `TabControl.TabPages` | `TabControl.ItemsSource` |
| `TabPage.Text` | `ItemTemplate` header binding |
| active tab by index/object | `SelectedIndex`/`SelectedItem` binding |

## Conversion Example

WinForms C#:

```csharp
var tabs = new TabControl();
tabs.TabPages.Add(new TabPage("Customers") { Controls = { new TextBox { Dock = DockStyle.Fill } } });
tabs.TabPages.Add(new TabPage("Orders") { Controls = { new DataGridView { Dock = DockStyle.Fill } } });
```

Avalonia XAML:

```xaml
<UserControl xmlns="https://github.com/avaloniaui"
             xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
             xmlns:vm="using:MyApp.ViewModels"
             x:DataType="vm:WorkspaceViewModel">
  <TabControl ItemsSource="{CompiledBinding Documents}"
              SelectedItem="{CompiledBinding ActiveDocument}">
    <TabControl.ItemTemplate>
      <DataTemplate x:DataType="vm:DocumentViewModel">
        <TextBlock Text="{CompiledBinding Title}" />
      </DataTemplate>
    </TabControl.ItemTemplate>

    <TabControl.ContentTemplate>
      <DataTemplate x:DataType="vm:DocumentViewModel">
        <ContentControl Content="{CompiledBinding ContentViewModel}" />
      </DataTemplate>
    </TabControl.ContentTemplate>
  </TabControl>
</UserControl>
```

## C# Equivalent

```csharp
using Avalonia.Controls;

var tabs = new TabControl
{
    ItemsSource = viewModel.Documents,
    SelectedItem = viewModel.ActiveDocument
};
```

## Troubleshooting

1. Tab content is recreated too often.
- keep stable document view-model instances and avoid rebuilding item collections.

2. Header text updates lag behind state.
- ensure document title properties raise `PropertyChanged`.

3. Complex MDI behavior is still expected.
- model workspace/document actions explicitly instead of emulating WinForms internals.
