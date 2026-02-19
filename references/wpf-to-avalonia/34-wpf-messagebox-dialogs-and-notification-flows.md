# WPF MessageBox, Dialogs, and Notification Flows to Avalonia

## Table of Contents
1. Scope and APIs
2. Dialog/Notification Mapping
3. Conversion Example
4. Avalonia C# Equivalent
5. Troubleshooting

## Scope and APIs

Primary WPF APIs:

- `MessageBox.Show(...)`
- custom modal `Window` dialogs

Primary Avalonia patterns:

- async `Window.ShowDialog(owner)` flows
- in-app notifications via `WindowNotificationManager`
- tray notifications via `TrayIcon` where appropriate

## Dialog/Notification Mapping

| WPF | Avalonia |
|---|---|
| blocking `MessageBox.Show(...)` result | async modal dialog result pattern |
| modal `Window.ShowDialog()` | `await ShowDialog(owner)` |
| ad-hoc status messages | managed notification toasts (`WindowNotificationManager`) |

Avalonia core does not provide a built-in `MessageBox` control.

## Conversion Example

WPF C#:

```csharp
if (MessageBox.Show("Delete record?", "Confirm", MessageBoxButton.YesNo) == MessageBoxResult.Yes)
    Delete();
```

Avalonia XAML:

```xaml
<UserControl xmlns="https://github.com/avaloniaui"
             xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
             xmlns:vm="using:MyApp.ViewModels"
             x:DataType="vm:NotificationsViewModel">
  <StackPanel Spacing="8">
    <Button Content="Confirm Delete"
            Command="{CompiledBinding ConfirmDeleteCommand}" />
    <Button Content="Show Success Toast"
            Command="{CompiledBinding ShowToastCommand}" />
  </StackPanel>
</UserControl>
```

## Avalonia C# Equivalent

```csharp
using System;
using System.Threading.Tasks;
using Avalonia;
using Avalonia.Controls;
using Avalonia.Controls.Notifications;
using Avalonia.Layout;

public static class NotificationFlows
{
    public static void ShowSavedToast(Window owner)
    {
        var manager = new WindowNotificationManager(owner)
        {
            Position = NotificationPosition.TopRight,
            MaxItems = 3
        };

        manager.Show(new Notification("Saved", "Changes applied.", NotificationType.Success, TimeSpan.FromSeconds(3)));
    }

    public static async Task<bool> ConfirmDeleteAsync(Window owner)
    {
        var dialog = new Window
        {
            Width = 360,
            Height = 180,
            CanResize = false,
            Title = "Confirm Delete",
            WindowStartupLocation = WindowStartupLocation.CenterOwner
        };

        var delete = new Button { Content = "Delete" };
        var cancel = new Button { Content = "Cancel" };
        delete.Click += (_, _) => dialog.Close(true);
        cancel.Click += (_, _) => dialog.Close(false);

        dialog.Content = new StackPanel
        {
            Margin = new Thickness(16),
            Spacing = 12,
            Children =
            {
                new TextBlock { Text = "Delete record?" },
                new StackPanel
                {
                    Orientation = Orientation.Horizontal,
                    HorizontalAlignment = HorizontalAlignment.Right,
                    Spacing = 8,
                    Children = { cancel, delete }
                }
            }
        };

        return await dialog.ShowDialog<bool>(owner);
    }
}
```

## Troubleshooting

1. Legacy dialog flow blocks the app.
- convert to async command flows and propagate dialog results explicitly.

2. Toast notifications never appear.
- ensure manager is attached to a live `Window`/`TopLevel`.

3. Mixed tray and in-app messaging is inconsistent.
- centralize notification intent and route through one notification service.
