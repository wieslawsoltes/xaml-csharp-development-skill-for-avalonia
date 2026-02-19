# HTML/CSS Modal, Drawer, Toast, and Overlay System Patterns in Avalonia

## Table of Contents
1. Scope and APIs
2. Modal/Dialog Mapping
3. Drawer/Sheet Mapping
4. Popover/Context/Tooltip Mapping
5. Toast/Notification Mapping
6. Conversion Example: Confirm + Toast Flow
7. C# Equivalent: Confirm + Toast Flow
8. Troubleshooting

## Scope and APIs

Primary APIs:

- `Window` dialog patterns
- `Popup`, `Flyout`, `ContextMenu`, `ToolTip`
- `SplitView` for drawer/sheet patterns
- `WindowNotificationManager` and notification contracts

Reference docs:

- [`25-popups-flyouts-tooltips-and-overlays.md`](../25-popups-flyouts-tooltips-and-overlays)
- [`53-menu-controls-contextmenu-and-menuflyout-patterns.md`](../53-menu-controls-contextmenu-and-menuflyout-patterns)
- [`56-managed-notifications-and-window-notification-manager.md`](../56-managed-notifications-and-window-notification-manager)

## Modal/Dialog Mapping

HTML/CSS modal idiom:

```html
<div class="backdrop"></div>
<div class="modal">Are you sure?</div>
```

Avalonia pattern:

- use a dialog `Window` owned by the parent window,
- keep focus trapped in dialog until close,
- return typed result where possible.

```csharp
var confirmed = await new ConfirmDeleteWindow().ShowDialog<bool>(owner);
```

## Drawer/Sheet Mapping

HTML/CSS:

```css
.drawer { position: fixed; right: 0; width: 380px; height: 100vh; }
```

Avalonia patterns:

1. right pane with `SplitView` + overlay mode,
2. popup-hosted panel anchored to edge.

```xaml
<SplitView DisplayMode="Overlay"
           IsPaneOpen="{CompiledBinding IsInspectorOpen}"
           OpenPaneLength="380"
           PanePlacement="Right" />
```

## Popover/Context/Tooltip Mapping

| Web pattern | Avalonia |
|---|---|
| popover | `Flyout` / `Popup` |
| context menu | `ContextMenu` |
| tooltip | `ToolTip.Tip` |

```xaml
<Button Content="Options">
  <Button.Flyout>
    <MenuFlyout>
      <MenuItem Header="Rename" />
      <MenuItem Header="Duplicate" />
    </MenuFlyout>
  </Button.Flyout>
</Button>
```

## Toast/Notification Mapping

HTML/CSS toasts are mapped to notification manager APIs:

```csharp
var manager = new WindowNotificationManager(owner)
{
    Position = NotificationPosition.TopRight
};
manager.Show(new Notification("Saved", "Project settings updated.", NotificationType.Success));
```

## Conversion Example: Confirm + Toast Flow

```html
<button class="danger">Delete</button>
<div class="modal-backdrop"></div>
<dialog class="confirm">Are you sure?</dialog>
<div class="toast success">Item removed.</div>
```

```css
.modal-backdrop { position: fixed; inset: 0; background: rgba(0,0,0,.45); }
.confirm { border: none; border-radius: 12px; padding: 20px; }
.toast.success { position: fixed; top: 16px; right: 16px; }
```

```xaml
<StackPanel Spacing="10">
  <Button Content="Delete"
          Classes="destructive"
          Command="{CompiledBinding ConfirmDeleteCommand}" />
</StackPanel>
```

1. user clicks Delete,
2. show confirm dialog,
3. if confirmed, execute delete command,
4. show success/error notification.

## C# Equivalent: Confirm + Toast Flow

```csharp
if (await new ConfirmDeleteWindow().ShowDialog<bool>(owner))
{
    await vm.DeleteAsync();
    _notifications.Show(new Notification("Deleted", "Item removed.", NotificationType.Information));
}
```

## Troubleshooting

1. Overlay blocks input unexpectedly.
- Ensure popup light-dismiss and hit-testing behavior match UX intent.

2. Dialog appears behind owner.
- Always pass explicit owner window when showing dialogs.

3. Toasts never appear.
- Verify notification manager is attached to active window and not disposed.
