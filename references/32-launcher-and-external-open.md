# Launcher and External Open Workflows

## Table of Contents
1. Scope and APIs
2. Launcher Access Model
3. URI and File Launch Patterns
4. XAML-First and Code-Only Usage
5. Best Practices
6. Troubleshooting

## Scope and APIs

Primary APIs:
- `TopLevel.GetTopLevel(...)`
- `TopLevel.Launcher`
- `ILauncher`
- `LauncherExtensions`
- `IStorageItem`

Important members:
- `ILauncher.LaunchUriAsync(...)`
- `ILauncher.LaunchFileAsync(...)`
- `LauncherExtensions.LaunchFileInfoAsync(...)`
- `LauncherExtensions.LaunchDirectoryInfoAsync(...)`

Reference source files:
- `src/Avalonia.Controls/TopLevel.cs`
- `src/Avalonia.Base/Platform/Storage/ILauncher.cs`

## Launcher Access Model

Access pattern:
1. Resolve `TopLevel` for current visual.
2. Use `TopLevel.Launcher`.
3. Treat result as best-effort (`bool` success/failure).

Note:
- Fallback `NoopLauncher` returns `false` when no platform launcher is available.

## URI and File Launch Patterns

```csharp
using System;
using System.Threading.Tasks;
using Avalonia.Controls;
using Avalonia.Platform.Storage;

public static class LauncherWorkflows
{
    public static async Task<bool> OpenWebsiteAsync(Control anchor, Uri uri)
    {
        TopLevel? top = TopLevel.GetTopLevel(anchor);
        if (top is null)
            return false;

        return await top.Launcher.LaunchUriAsync(uri);
    }

    public static async Task<bool> OpenStorageItemAsync(Control anchor, IStorageItem item)
    {
        TopLevel? top = TopLevel.GetTopLevel(anchor);
        if (top is null)
            return false;

        return await top.Launcher.LaunchFileAsync(item);
    }
}
```

## XAML-First and Code-Only Usage

Default mode:
- Bind launch actions from XAML to commands.
- Keep launch orchestration in viewmodel/service layer.
- Use code-only UI tree setup only when requested.

XAML-first complete example:

```xml
<UserControl xmlns="https://github.com/avaloniaui"
             xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
             xmlns:vm="using:MyApp.ViewModels"
             x:DataType="vm:LauncherViewModel">
  <StackPanel Margin="12" Spacing="8">
    <Button Content="Open Website" Command="{CompiledBinding OpenWebsiteCommand}" />
    <Button Content="Reveal Export Folder" Command="{CompiledBinding OpenExportFolderCommand}" />
    <TextBlock Text="{CompiledBinding LastLaunchStatus}" />
  </StackPanel>
</UserControl>
```

Code-only alternative (on request):

```csharp
using System;
using System.Threading.Tasks;
using Avalonia.Controls;

public static class CodeOnlyLauncherSample
{
    public static async Task OpenDocsAsync(Control anchor)
    {
        TopLevel? top = TopLevel.GetTopLevel(anchor);
        if (top is null)
            return;

        bool launched = await top.Launcher.LaunchUriAsync(new Uri("https://docs.avaloniaui.net"));
        _ = launched;
    }
}
```

## Best Practices

- Validate and normalize URIs before launch.
- Treat launch failures as normal runtime outcomes.
- Keep launch side-effects explicit in user-driven commands.

## Troubleshooting

1. Launch returns false:
- Platform does not support the scheme.
- No default app is registered for URI or file type.

2. Launch works on one OS and fails on another:
- Platform policy/association behavior differs.

3. Silent failures in tests/headless:
- Headless or sandbox backends may not provide real launcher integration.
