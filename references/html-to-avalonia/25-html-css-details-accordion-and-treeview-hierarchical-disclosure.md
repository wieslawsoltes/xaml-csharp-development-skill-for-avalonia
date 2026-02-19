# HTML/CSS `details`/Accordion and Tree Disclosure to Avalonia `Expander` and `TreeView`

## Table of Contents
1. Scope and APIs
2. Mapping Table
3. Disclosure Pattern (`<details>` to `Expander`)
4. Accordion Pattern
5. Hierarchical Tree Pattern
6. Conversion Example: Settings + Navigation Tree
7. C# Equivalent: Settings + Navigation Tree
8. AOT/Threading Notes
9. Troubleshooting

## Scope and APIs

Primary APIs:

- `Expander` (`Header`, `IsExpanded`, `ExpandDirection`, `ContentTransition`)
- `TreeView`, `TreeViewItem`
- selection APIs: `SelectionMode`, `SelectedItem`, `SelectionChanged`

Reference docs:

- [`13-html-css-navigation-tabs-sidebars-breadcrumbs-and-routing-patterns.md`](13-html-css-navigation-tabs-sidebars-breadcrumbs-and-routing-patterns)
- [`16-html-css-accessibility-semantics-and-motion-preference-mapping.md`](16-html-css-accessibility-semantics-and-motion-preference-mapping)
- [`controls/expander.md`](../controls/expander)
- [`controls/tree-view.md`](../controls/tree-view)

## Mapping Table

| HTML/CSS idiom | Avalonia mapping |
|---|---|
| `<details open>` | `Expander IsExpanded="True"` |
| `<summary>` | `Expander Header` |
| accordion with one panel open | coordinated `Expander IsExpanded` view-model state |
| `<ul role="tree">` + nested `<li>` | `TreeView` with nested `TreeViewItem` or hierarchical templates |
| `aria-expanded` node state | `TreeViewItem IsExpanded` |

## Disclosure Pattern (`<details>` to `Expander`)

HTML/CSS:

```html
<details open class="section">
  <summary>Project Settings</summary>
  <div class="body">Build, signing, and deployment options.</div>
</details>
```

```css
.section {
  border: 1px solid #d8deea;
  border-radius: 10px;
  padding: 8px 12px;
}
.section > summary {
  cursor: pointer;
  font-weight: 600;
}
```

Avalonia:

```xaml
<Expander Header="Project Settings"
          IsExpanded="True"
          ExpandDirection="Down">
  <Border Padding="8" Classes="panel-body">
    <TextBlock Text="Build, signing, and deployment options." />
  </Border>
</Expander>
```

## Accordion Pattern

HTML/CSS accordion behavior is typically JS-controlled. In Avalonia, drive each `Expander.IsExpanded` from a single selected key.

```xaml
<StackPanel Spacing="8">
  <Expander Header="General"
            IsExpanded="{CompiledBinding IsGeneralOpen}">
    <TextBlock Text="General project settings." />
  </Expander>
  <Expander Header="Security"
            IsExpanded="{CompiledBinding IsSecurityOpen}">
    <TextBlock Text="Certificates and secrets." />
  </Expander>
  <Expander Header="Deploy"
            IsExpanded="{CompiledBinding IsDeployOpen}">
    <TextBlock Text="Publishing channels." />
  </Expander>
</StackPanel>
```

## Hierarchical Tree Pattern

HTML/CSS tree baseline:

```html
<ul role="tree" class="nav-tree">
  <li role="treeitem" aria-expanded="true">
    Docs
    <ul role="group">
      <li role="treeitem">Getting Started</li>
      <li role="treeitem">API</li>
    </ul>
  </li>
  <li role="treeitem">Samples</li>
</ul>
```

Avalonia tree equivalent:

```xaml
<TreeView SelectionMode="Single"
          SelectedItem="{CompiledBinding SelectedNode, Mode=TwoWay}">
  <TreeViewItem Header="Docs" IsExpanded="True">
    <TreeViewItem Header="Getting Started" />
    <TreeViewItem Header="API" />
  </TreeViewItem>
  <TreeViewItem Header="Samples" />
</TreeView>
```

## Conversion Example: Settings + Navigation Tree

```html
<section class="workspace">
  <aside>
    <ul role="tree" class="nav-tree">
      <li role="treeitem" aria-expanded="true">Settings
        <ul role="group">
          <li role="treeitem">General</li>
          <li role="treeitem">Security</li>
        </ul>
      </li>
      <li role="treeitem">Logs</li>
    </ul>
  </aside>
  <main>
    <details open>
      <summary>General</summary>
      <div>General options panel...</div>
    </details>
  </main>
</section>
```

```css
.workspace {
  display: grid;
  grid-template-columns: 260px 1fr;
  gap: 12px;
}
.nav-tree { list-style: none; padding-inline-start: 12px; }
```

```xaml
<Grid ColumnDefinitions="260,*" ColumnSpacing="12">
  <TreeView Grid.Column="0"
            SelectionMode="Single"
            SelectedItem="{CompiledBinding SelectedNode, Mode=TwoWay}">
    <TreeViewItem Header="Settings" IsExpanded="True">
      <TreeViewItem Header="General" />
      <TreeViewItem Header="Security" />
    </TreeViewItem>
    <TreeViewItem Header="Logs" />
  </TreeView>

  <StackPanel Grid.Column="1" Spacing="8">
    <Expander Header="General"
              IsExpanded="{CompiledBinding IsGeneralOpen}">
      <Border Padding="8">
        <TextBlock Text="General options panel..." />
      </Border>
    </Expander>
  </StackPanel>
</Grid>
```

## C# Equivalent: Settings + Navigation Tree

```csharp
using Avalonia.Controls;

var root = new Grid
{
    ColumnDefinitions = ColumnDefinitions.Parse("260,*"),
    ColumnSpacing = 12
};

var tree = new TreeView
{
    SelectionMode = SelectionMode.Single
};

var settings = new TreeViewItem { Header = "Settings", IsExpanded = true };
settings.Items.Add(new TreeViewItem { Header = "General" });
settings.Items.Add(new TreeViewItem { Header = "Security" });

tree.Items.Add(settings);
tree.Items.Add(new TreeViewItem { Header = "Logs" });

var generalExpander = new Expander
{
    Header = "General",
    IsExpanded = true,
    Content = new Border
    {
        Padding = new Avalonia.Thickness(8),
        Child = new TextBlock { Text = "General options panel..." }
    }
};

var content = new StackPanel { Spacing = 8 };
content.Children.Add(generalExpander);

Grid.SetColumn(tree, 0);
Grid.SetColumn(content, 1);

root.Children.Add(tree);
root.Children.Add(content);
```

## AOT/Threading Notes

- Keep expansion/selection state in typed view-model properties; avoid stringly-typed node routing.
- If node data is loaded asynchronously, add or update tree items on `Dispatcher.UIThread`.

## Troubleshooting

1. Tree nodes do not expand.
- Ensure child items exist for each expandable node and `IsExpanded` is not reset by state sync code.

2. Accordion opens multiple sections unexpectedly.
- Use one source of truth (`SelectedSection`) and derive each `IsExpanded` from it.

3. Selection binding does not update.
- Confirm `SelectedItem` binding is `TwoWay` and `SelectionMode` matches expected interaction.
