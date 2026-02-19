# WPF TreeView HierarchicalDataTemplate, Expansion, and Selection to Avalonia

## Table of Contents
1. Scope and APIs
2. Tree Mapping
3. Conversion Example
4. Avalonia C# Equivalent
5. Troubleshooting

## Scope and APIs

Primary WPF APIs:

- `TreeView`
- `HierarchicalDataTemplate`
- `TreeViewItem.IsExpanded`, selection behaviors

Primary Avalonia APIs:

- `TreeView`
- `TreeDataTemplate` / `FuncTreeDataTemplate<T>`
- `TreeViewItem.IsExpanded`, `Expanded`/`Collapsed` events
- `TreeView.SelectionMode`, `SelectedItem`, `AutoScrollToSelectedItem`

## Tree Mapping

| WPF | Avalonia |
|---|---|
| `HierarchicalDataTemplate ItemsSource=...` | `TreeDataTemplate ItemsSource=...` |
| `TreeViewItem.IsExpanded` two-way state | `TreeViewItem.IsExpanded` two-way state |
| selected node workflows | `SelectedItem` and `SelectionMode` on `TreeView` |
| lazy child load on expand | handle `TreeViewItem.Expanded` and load node children |

## Conversion Example

WPF XAML:

```xaml
<TreeView ItemsSource="{Binding RootNodes}"
          SelectedItemChanged="OnSelectedItemChanged">
  <TreeView.ItemTemplate>
    <HierarchicalDataTemplate DataType="{x:Type vm:NodeViewModel}"
                              ItemsSource="{Binding Children}">
      <TextBlock Text="{Binding Title}" />
    </HierarchicalDataTemplate>
  </TreeView.ItemTemplate>
</TreeView>
```

Avalonia XAML:

```xaml
<UserControl xmlns="https://github.com/avaloniaui"
             xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
             xmlns:vm="using:MyApp.ViewModels"
             x:DataType="vm:ExplorerViewModel">
  <TreeView ItemsSource="{CompiledBinding RootNodes}"
            SelectedItem="{CompiledBinding SelectedNode, Mode=TwoWay}"
            SelectionMode="Single"
            AutoScrollToSelectedItem="True">
    <TreeView.ItemTemplate>
      <TreeDataTemplate x:DataType="vm:NodeViewModel"
                        ItemsSource="{CompiledBinding Children}">
        <TextBlock Text="{CompiledBinding Title}" />
      </TreeDataTemplate>
    </TreeView.ItemTemplate>
  </TreeView>
</UserControl>
```

## Avalonia C# Equivalent

```csharp
using Avalonia.Controls;
using Avalonia.Controls.Templates;
using Avalonia.Interactivity;

var tree = new TreeView
{
    ItemsSource = viewModel.RootNodes,
    SelectionMode = SelectionMode.Single,
    AutoScrollToSelectedItem = true,
    ItemTemplate = new FuncTreeDataTemplate<NodeViewModel>(
        (node, _) => new TextBlock { Text = node.Title },
        node => node.Children)
};

tree.AddHandler(TreeViewItem.ExpandedEvent, (_, e) =>
{
    if (e.Source is TreeViewItem { DataContext: NodeViewModel node } && !node.ChildrenLoaded)
    {
        node.LoadChildren();
    }
}, RoutingStrategies.Bubble);
```

## Troubleshooting

1. Child nodes do not appear.
- Check `TreeDataTemplate.ItemsSource` binding and ensure children collection notifications are raised.

2. Selecting deep nodes fails.
- Ensure ancestor nodes are expanded before assigning deep selection.

3. Large trees become slow after port.
- Load child collections on demand and avoid eager full-tree expansion.
