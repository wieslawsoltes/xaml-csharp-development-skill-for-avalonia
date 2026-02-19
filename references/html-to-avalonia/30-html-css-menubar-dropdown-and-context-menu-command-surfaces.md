# HTML/CSS Menubar, Dropdown Menu, and Context Menu Patterns to Avalonia

## Table of Contents
1. Scope and APIs
2. Mapping Table
3. Menubar Pattern
4. Dropdown/Submenu Pattern
5. Context Menu Pattern
6. Conversion Example: File Workspace Commands
7. C# Equivalent: File Workspace Commands
8. AOT/Threading Notes
9. Troubleshooting

## Scope and APIs

Primary APIs:

- `Menu`, `MenuItem`, `Separator`
- `ContextMenu`
- `Control.ContextFlyout`, `FlyoutBase.ShowAttachedFlyout`
- command metadata: `ICommand`, `MenuItem.InputGesture`, `MenuItem.Icon`

Reference docs:

- [`24-html-css-buttons-links-toggle-and-split-command-surfaces.md`](24-html-css-buttons-links-toggle-and-split-command-surfaces)
- [`53-menu-controls-contextmenu-and-menuflyout-patterns.md`](../53-menu-controls-contextmenu-and-menuflyout-patterns)
- [`54-native-menu-and-native-menubar-integration.md`](../54-native-menu-and-native-menubar-integration)

## Mapping Table

| HTML/CSS idiom | Avalonia mapping |
|---|---|
| top app menubar (`<nav class="menubar">`) | `Menu` + top-level `MenuItem` |
| nested dropdown (`ul > li > ul`) | nested `MenuItem` hierarchy |
| menu separator (`<hr>`) | `Separator` |
| right-click context actions | `ContextMenu` on target control |
| shortcut label (`Ctrl+S`) | `MenuItem InputGesture` |

## Menubar Pattern

HTML/CSS:

```html
<nav class="menubar">
  <button>File</button>
  <button>Edit</button>
  <button>View</button>
</nav>
```

```xaml
<Menu>
  <MenuItem Header="_File" />
  <MenuItem Header="_Edit" />
  <MenuItem Header="_View" />
</Menu>
```

## Dropdown/Submenu Pattern

```html
<ul class="menu">
  <li>File
    <ul>
      <li>New</li>
      <li>Open</li>
      <li>Recent
        <ul>
          <li>project-a.sln</li>
          <li>project-b.sln</li>
        </ul>
      </li>
    </ul>
  </li>
</ul>
```

```xaml
<Menu>
  <MenuItem Header="_File">
    <MenuItem Header="New" Command="{CompiledBinding NewCommand}" />
    <MenuItem Header="Open" Command="{CompiledBinding OpenCommand}" />
    <Separator />
    <MenuItem Header="Recent">
      <MenuItem Header="project-a.sln" Command="{CompiledBinding OpenRecentACommand}" />
      <MenuItem Header="project-b.sln" Command="{CompiledBinding OpenRecentBCommand}" />
    </MenuItem>
  </MenuItem>
</Menu>
```

## Context Menu Pattern

HTML/CSS intent:

```html
<div class="file-row" role="button">Report.csv</div>
```

```css
.file-row {
  user-select: none;
}
```

Avalonia:

```xaml
<Border Padding="8" Background="#121821">
  <TextBlock Text="Report.csv" />
  <Border.ContextMenu>
    <ContextMenu>
      <MenuItem Header="Open" Command="{CompiledBinding OpenFileCommand}" />
      <MenuItem Header="Rename" Command="{CompiledBinding RenameFileCommand}" />
      <Separator />
      <MenuItem Header="Delete" Command="{CompiledBinding DeleteFileCommand}" />
    </ContextMenu>
  </Border.ContextMenu>
</Border>
```

## Conversion Example: File Workspace Commands

```html
<header class="workspace-header">
  <nav class="menubar">...</nav>
</header>
<main>
  <div class="file-row">Report.csv</div>
</main>
```

```css
.workspace-header {
  border-block-end: 1px solid #2a3240;
  padding: 8px 12px;
}
```

```xaml
<DockPanel>
  <Menu DockPanel.Dock="Top">
    <MenuItem Header="_File">
      <MenuItem Header="New" Command="{CompiledBinding NewCommand}" InputGesture="Ctrl+N" />
      <MenuItem Header="Open" Command="{CompiledBinding OpenCommand}" InputGesture="Ctrl+O" />
      <MenuItem Header="Save" Command="{CompiledBinding SaveCommand}" InputGesture="Ctrl+S" />
      <Separator />
      <MenuItem Header="Exit" Command="{CompiledBinding ExitCommand}" />
    </MenuItem>
    <MenuItem Header="_Edit">
      <MenuItem Header="Copy" Command="{CompiledBinding CopyCommand}" InputGesture="Ctrl+C" />
      <MenuItem Header="Paste" Command="{CompiledBinding PasteCommand}" InputGesture="Ctrl+V" />
    </MenuItem>
  </Menu>

  <StackPanel Margin="12" Spacing="6">
    <Border Padding="8" Background="#121821">
      <TextBlock Text="Report.csv" />
      <Border.ContextMenu>
        <ContextMenu>
          <MenuItem Header="Open" Command="{CompiledBinding OpenFileCommand}" />
          <MenuItem Header="Rename" Command="{CompiledBinding RenameFileCommand}" />
          <Separator />
          <MenuItem Header="Delete" Command="{CompiledBinding DeleteFileCommand}" />
        </ContextMenu>
      </Border.ContextMenu>
    </Border>
  </StackPanel>
</DockPanel>
```

## C# Equivalent: File Workspace Commands

```csharp
using Avalonia.Controls;
using Avalonia.Input;

var menu = new Menu();

var file = new MenuItem { Header = "_File" };
file.Items.Add(new MenuItem { Header = "New", InputGesture = KeyGesture.Parse("Ctrl+N") });
file.Items.Add(new MenuItem { Header = "Open", InputGesture = KeyGesture.Parse("Ctrl+O") });
file.Items.Add(new MenuItem { Header = "Save", InputGesture = KeyGesture.Parse("Ctrl+S") });
file.Items.Add(new Separator());
file.Items.Add(new MenuItem { Header = "Exit" });

var edit = new MenuItem { Header = "_Edit" };
edit.Items.Add(new MenuItem { Header = "Copy", InputGesture = KeyGesture.Parse("Ctrl+C") });
edit.Items.Add(new MenuItem { Header = "Paste", InputGesture = KeyGesture.Parse("Ctrl+V") });

menu.Items.Add(file);
menu.Items.Add(edit);

var row = new Border
{
    Padding = new Avalonia.Thickness(8),
    Background = new Avalonia.Media.SolidColorBrush(Avalonia.Media.Color.Parse("#121821")),
    Child = new TextBlock { Text = "Report.csv" }
};

row.ContextMenu = new ContextMenu();
row.ContextMenu.Items.Add(new MenuItem { Header = "Open" });
row.ContextMenu.Items.Add(new MenuItem { Header = "Rename" });
row.ContextMenu.Items.Add(new Separator());
row.ContextMenu.Items.Add(new MenuItem { Header = "Delete" });

var layout = new DockPanel();
DockPanel.SetDock(menu, Dock.Top);
layout.Children.Add(menu);
layout.Children.Add(new StackPanel { Margin = new Avalonia.Thickness(12), Children = { row } });
```

## AOT/Threading Notes

- Keep command routing strongly typed (`ICommand` on VM) instead of reflection-based lookup.
- Build/update dynamic menu items on `Dispatcher.UIThread` if source data arrives asynchronously.

## Troubleshooting

1. Menu shortcuts do not appear or trigger.
- Verify `InputGesture` format and command binding target scope.

2. Context menu does not show on right-click.
- Ensure the control is enabled, visible, and has a non-null `ContextMenu`.

3. Nested submenus close unexpectedly.
- Check focus handling and avoid rebuilding menu item collections during pointer navigation.
