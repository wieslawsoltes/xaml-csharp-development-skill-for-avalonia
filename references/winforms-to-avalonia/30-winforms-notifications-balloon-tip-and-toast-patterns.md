# WinForms Notifications (Balloon Tips, Message Dialogs) to Avalonia

## Table of Contents
1. Scope and APIs
2. Notification Mapping
3. Conversion Example
4. C# Equivalent
5. Troubleshooting

## Scope and APIs

Primary WinForms APIs:

- `NotifyIcon.ShowBalloonTip(...)`
- `MessageBox.Show(...)`
- `TaskDialog` patterns

Primary Avalonia APIs/patterns:

- `TrayIcon` for system-tray presence
- `WindowNotificationManager` + `Notification` for in-app toasts
- custom dialog windows (or package-based message box abstractions)

## Notification Mapping

| WinForms | Avalonia |
|---|---|
| tray balloon tip | tray integration + in-app toast notifications |
| `MessageBox.Show` blocking dialog | async `Window.ShowDialog(owner)` flow |
| task-oriented dialogs | custom dialog views with explicit commands |

## Conversion Example

WinForms C#:

```csharp
notifyIcon.ShowBalloonTip(3000, "Saved", "Customer updated.", ToolTipIcon.Info);

if (MessageBox.Show("Delete record?", "Confirm", MessageBoxButtons.YesNo) == DialogResult.Yes)
{
    Delete();
}
```

Avalonia XAML:

```xaml
<UserControl xmlns="https://github.com/avaloniaui"
             xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
             xmlns:vm="using:MyApp.ViewModels"
             x:DataType="vm:NotificationsViewModel">
  <StackPanel Spacing="8">
    <Button Content="Show Success Toast"
            Command="{CompiledBinding ShowSuccessCommand}" />
    <Button Content="Confirm Delete"
            Command="{CompiledBinding ConfirmDeleteCommand}" />
  </StackPanel>
</UserControl>
```

## C# Equivalent

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

        manager.Show(new Notification(
            "Saved",
            "Customer updated.",
            NotificationType.Success,
            TimeSpan.FromSeconds(3)));
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

        var confirm = new Button { Content = "Delete" };
        var cancel = new Button { Content = "Cancel" };
        confirm.Click += (_, _) => dialog.Close(true);
        cancel.Click += (_, _) => dialog.Close(false);

        dialog.Content = new StackPanel
        {
            Margin = new Thickness(12),
            Spacing = 10,
            Children =
            {
                new TextBlock { Text = "Delete selected record?" },
                new StackPanel
                {
                    Orientation = Orientation.Horizontal,
                    HorizontalAlignment = HorizontalAlignment.Right,
                    Spacing = 8,
                    Children = { cancel, confirm }
                }
            }
        };

        return await dialog.ShowDialog<bool>(owner);
    }
}
```

## Troubleshooting

1. Toasts do not appear.
- ensure notification manager is created for a live `Window`/`TopLevel`.

2. Confirmation flows remain blocking and tangled.
- move to async dialog commands and explicit result propagation.

3. Tray and in-app notifications diverge in behavior.
- centralize notification intents and route to tray/toast channels consistently.
