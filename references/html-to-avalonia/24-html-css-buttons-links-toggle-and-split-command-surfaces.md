# HTML/CSS Buttons, Links, Toggle, and Split Command Surfaces in Avalonia

## Table of Contents
1. Scope and APIs
2. Element-to-Control Mapping
3. Toggle and Segmented Patterns
4. DropDown and Split Command Patterns
5. Hold-to-Repeat Interaction Pattern
6. Conversion Example: Command Toolbar
7. C# Equivalent: Command Toolbar
8. AOT/Threading Notes
9. Troubleshooting

## Scope and APIs

Primary APIs:

- `Button`, `HyperlinkButton`
- `ToggleButton`, `ToggleSplitButton`
- `DropDownButton`, `SplitButton`, `RepeatButton`
- `MenuFlyout`, `MenuItem`, `Separator`
- `ICommand`, `HotKeyManager`

Reference docs:

- [`04-html-forms-input-and-validation-to-avalonia-controls.md`](04-html-forms-input-and-validation-to-avalonia-controls)
- [`05-html-shell-navigation-popups-and-layering-patterns.md`](05-html-shell-navigation-popups-and-layering-patterns)
- [`12-html-css-interaction-states-focus-gestures-and-input-ux.md`](12-html-css-interaction-states-focus-gestures-and-input-ux)
- [`24-commands-hotkeys-and-gestures.md`](../24-commands-hotkeys-and-gestures)

## Element-to-Control Mapping

| HTML/CSS idiom | Avalonia mapping |
|---|---|
| `<button>` | `Button` |
| `<a href="...">` styled as button/link | `HyperlinkButton NavigateUri` (or `Button` + launcher command) |
| split button (primary action + menu) | `SplitButton` + `Flyout` |
| menu-only trigger button | `DropDownButton` + `Flyout` |
| toggle/pressed state (`aria-pressed`) | `ToggleButton IsChecked` |
| long-press increment button | `RepeatButton Delay` + `Interval` |

## Toggle and Segmented Patterns

HTML/CSS segmented toggle pattern:

```html
<div class="segment" role="group" aria-label="View mode">
  <button aria-pressed="true">Preview</button>
  <button aria-pressed="false">Code</button>
</div>
```

```css
.segment { display: inline-flex; gap: 6px; }
.segment button[aria-pressed="true"] { background: #2f6fed; color: #fff; }
```

Avalonia pattern:

```xaml
<StackPanel Orientation="Horizontal" Spacing="6">
  <ToggleButton Content="Preview" IsChecked="{CompiledBinding IsPreview}" />
  <ToggleButton Content="Code" IsChecked="{CompiledBinding IsCodeView}" />
</StackPanel>
```

## DropDown and Split Command Patterns

HTML/CSS intent:

```html
<div class="toolbar">
  <button>Publish</button>
  <button aria-haspopup="menu">More</button>
</div>
```

```xaml
<StackPanel Orientation="Horizontal" Spacing="8">
  <SplitButton Content="Publish" Command="{CompiledBinding PublishNowCommand}">
    <SplitButton.Flyout>
      <MenuFlyout>
        <MenuItem Header="Publish now" Command="{CompiledBinding PublishNowCommand}" />
        <MenuItem Header="Schedule..." Command="{CompiledBinding SchedulePublishCommand}" />
      </MenuFlyout>
    </SplitButton.Flyout>
  </SplitButton>

  <DropDownButton Content="More">
    <DropDownButton.Flyout>
      <MenuFlyout>
        <MenuItem Header="Duplicate" Command="{CompiledBinding DuplicateCommand}" />
        <Separator />
        <MenuItem Header="Archive" Command="{CompiledBinding ArchiveCommand}" />
      </MenuFlyout>
    </DropDownButton.Flyout>
  </DropDownButton>
</StackPanel>
```

## Hold-to-Repeat Interaction Pattern

HTML/CSS spinner arrows map to `RepeatButton` with interval tuning.

```xaml
<StackPanel Orientation="Horizontal" Spacing="6">
  <RepeatButton Content="-" Delay="300" Interval="80" Command="{CompiledBinding DecrementCommand}" />
  <TextBlock Text="{CompiledBinding QuantityText}" VerticalAlignment="Center" />
  <RepeatButton Content="+" Delay="300" Interval="80" Command="{CompiledBinding IncrementCommand}" />
</StackPanel>
```

## Conversion Example: Command Toolbar

```html
<div class="cmd-toolbar">
  <button class="primary">Save</button>
  <button class="split">Publish</button>
  <button class="menu">More</button>
  <a class="docs" href="/docs">Docs</a>
  <button aria-pressed="true" class="toggle">Preview</button>
</div>
```

```css
.cmd-toolbar { display: flex; gap: 8px; align-items: center; }
.cmd-toolbar .primary { background: #2f6fed; color: #fff; }
.cmd-toolbar .toggle[aria-pressed="true"] { border-color: #2f6fed; }
```

```xaml
<StackPanel Orientation="Horizontal" Spacing="8">
  <Button Content="Save" Classes="primary" Command="{CompiledBinding SaveCommand}" />

  <SplitButton Content="Publish" Command="{CompiledBinding PublishNowCommand}">
    <SplitButton.Flyout>
      <MenuFlyout>
        <MenuItem Header="Publish now" Command="{CompiledBinding PublishNowCommand}" />
        <MenuItem Header="Schedule..." Command="{CompiledBinding SchedulePublishCommand}" />
      </MenuFlyout>
    </SplitButton.Flyout>
  </SplitButton>

  <DropDownButton Content="More">
    <DropDownButton.Flyout>
      <MenuFlyout>
        <MenuItem Header="Duplicate" Command="{CompiledBinding DuplicateCommand}" />
        <MenuItem Header="Archive" Command="{CompiledBinding ArchiveCommand}" />
      </MenuFlyout>
    </DropDownButton.Flyout>
  </DropDownButton>

  <HyperlinkButton Content="Docs" NavigateUri="https://example.com/docs" />
  <ToggleButton Content="Preview" IsChecked="{CompiledBinding IsPreview}" />
</StackPanel>
```

## C# Equivalent: Command Toolbar

```csharp
using System;
using Avalonia.Controls;
using Avalonia.Controls.Primitives;
using Avalonia.Input;

var toolbar = new StackPanel
{
    Orientation = Avalonia.Layout.Orientation.Horizontal,
    Spacing = 8
};

var saveButton = new Button { Content = "Save" };
HotKeyManager.SetHotKey(saveButton, new KeyGesture(Key.S, KeyModifiers.Control));

var publishMenu = new MenuFlyout();
publishMenu.Items.Add(new MenuItem { Header = "Publish now" });
publishMenu.Items.Add(new MenuItem { Header = "Schedule..." });

var publishSplit = new SplitButton
{
    Content = "Publish",
    Flyout = publishMenu
};

var moreMenu = new MenuFlyout();
moreMenu.Items.Add(new MenuItem { Header = "Duplicate" });
moreMenu.Items.Add(new Separator());
moreMenu.Items.Add(new MenuItem { Header = "Archive" });

var moreButton = new DropDownButton
{
    Content = "More",
    Flyout = moreMenu
};

var docsLink = new HyperlinkButton
{
    Content = "Docs",
    NavigateUri = new Uri("https://example.com/docs")
};

var previewToggle = new ToggleButton
{
    Content = "Preview",
    IsChecked = true
};

toolbar.Children.Add(saveButton);
toolbar.Children.Add(publishSplit);
toolbar.Children.Add(moreButton);
toolbar.Children.Add(docsLink);
toolbar.Children.Add(previewToggle);
```

## AOT/Threading Notes

- Keep command handlers strongly typed; avoid runtime reflection command routing.
- Update command state (`CanExecute` and related VM flags) on `Dispatcher.UIThread` when triggered from background work.

## Troubleshooting

1. Split/DropDown menu does not open.
- Confirm `Flyout` is set and the control is attached to visual tree.

2. Toggle visuals do not reflect state.
- Ensure `IsChecked` binding mode is TwoWay and not overwritten by local setters.

3. Repeat action is too aggressive.
- Increase `Delay` and `Interval` to reduce accidental rapid changes.
