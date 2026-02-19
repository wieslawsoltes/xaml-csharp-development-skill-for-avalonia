# WinForms TreeView (Lazy Loading, Selection, Check State) to Avalonia

## Table of Contents
1. Scope and APIs
2. Tree Mapping
3. Conversion Example
4. C# Equivalent
5. Troubleshooting

## Scope and APIs

Primary WinForms APIs:

- `TreeView`, `TreeNode`
- `BeforeExpand` / `AfterSelect`
- `CheckBoxes` and node check state updates

Primary Avalonia APIs:

- `TreeView` + `TreeDataTemplate`
- `TreeView.SelectedItem`, `TreeView.AutoScrollToSelectedItem`
- `TreeViewItem.Expanded` event for lazy-load triggers

## Tree Mapping

| WinForms | Avalonia |
|---|---|
| `TreeNode` hierarchy | hierarchical view-model with `Children` |
| `BeforeExpand` async population | `TreeViewItem.Expanded` handler + `EnsureChildrenLoadedAsync()` |
| `AfterSelect` | `SelectedItem` binding + command/view-model state updates |
| built-in check boxes | `CheckBox` inside `TreeDataTemplate` for two-state or three-state logic |

## Conversion Example

WinForms C#:

```csharp
treeView1.CheckBoxes = true;
treeView1.BeforeExpand += (_, e) => LoadChildrenIfNeeded(e.Node);
treeView1.AfterSelect += (_, e) => detailsPanel.Bind(e.Node.Tag);
```

Avalonia XAML:

```xaml
<UserControl xmlns="https://github.com/avaloniaui"
             xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
             xmlns:vm="using:MyApp.ViewModels"
             x:DataType="vm:ExplorerTreeViewModel">
  <TreeView ItemsSource="{CompiledBinding Roots}"
            AutoScrollToSelectedItem="True"
            SelectedItem="{CompiledBinding SelectedNode, Mode=TwoWay}">
    <TreeView.ItemTemplate>
      <TreeDataTemplate x:DataType="vm:TreeNodeViewModel"
                        ItemsSource="{CompiledBinding Children}">
        <StackPanel Orientation="Horizontal" Spacing="6">
          <CheckBox IsThreeState="True"
                    IsChecked="{CompiledBinding IsChecked, Mode=TwoWay}" />
          <TextBlock Text="{CompiledBinding Name}" />
        </StackPanel>
      </TreeDataTemplate>
    </TreeView.ItemTemplate>
  </TreeView>
</UserControl>
```

## C# Equivalent

```csharp
using Avalonia.Controls;
using Avalonia.Interactivity;

var tree = new TreeView
{
    ItemsSource = viewModel.Roots,
    AutoScrollToSelectedItem = true
};

tree.AddHandler(TreeViewItem.ExpandedEvent, (sender, e) =>
{
    if (e.Source is TreeViewItem { DataContext: TreeNodeViewModel node })
    {
        _ = node.EnsureChildrenLoadedAsync();
    }
}, RoutingStrategies.Bubble);
```

## Troubleshooting

1. Expanded nodes lose state after refresh.
- use stable node identities and update existing child collections in place.

2. Lazy loading causes duplicate children.
- guard `EnsureChildrenLoadedAsync()` with an idempotent `IsLoaded` flag.

3. Check-state propagation is inconsistent.
- keep parent/child check computation in view model, not per-control event handlers.
