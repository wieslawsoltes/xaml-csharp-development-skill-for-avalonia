# WinForms Native Interop and WebBrowser Replacement Strategies to Avalonia

## Table of Contents
1. Scope and APIs
2. Interop Mapping
3. Web Browser Replacement Strategy
4. Conversion Example
5. C# Equivalent
6. Troubleshooting

## Scope and APIs

Primary WinForms APIs:

- `AxHost`
- `WebBrowser`
- handle-centric interop patterns

Primary Avalonia APIs:

- `NativeControlHost`
- platform handles (`IPlatformHandle`)
- `TopLevel` integration for host-aware behaviors

## Interop Mapping

| WinForms | Avalonia |
|---|---|
| embedded ActiveX via `AxHost` | `NativeControlHost` with platform-specific child handle |
| handle-manual positioning | `NativeControlHost` automatic host/visibility positioning |
| built-in `WebBrowser` control | custom wrapper around external webview technology |

## Web Browser Replacement Strategy

Avalonia core `11.3.12` does not ship a direct drop-in `WebBrowser` control equivalent.

Recommended approach:

- isolate browser requirements behind an abstraction,
- choose a platform-specific or cross-platform webview integration package,
- host through a dedicated wrapper control or native-host bridge,
- keep navigation and script bridge logic out of view code.

## Conversion Example

WinForms C#:

```csharp
var browser = new WebBrowser { Dock = DockStyle.Fill };
browser.Navigate("https://example.com");
Controls.Add(browser);
```

Avalonia XAML:

```xaml
<local:EmbeddedWebHost xmlns="https://github.com/avaloniaui"
                       xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
                       xmlns:local="using:MyApp.Controls"
                       Width="800"
                       Height="600" />
```

## C# Equivalent

```csharp
using Avalonia.Controls;
using Avalonia.Controls.Platform;
using Avalonia.Platform;

public class EmbeddedNativeHost : NativeControlHost
{
    protected override IPlatformHandle CreateNativeControlCore(IPlatformHandle parent)
    {
        // Replace this with your platform-specific control/webview creation logic.
        return base.CreateNativeControlCore(parent);
    }

    protected override void DestroyNativeControlCore(IPlatformHandle control)
    {
        // Dispose platform-native resources created in CreateNativeControlCore.
        base.DestroyNativeControlCore(control);
    }
}
```

## Troubleshooting

1. Native host surface is invisible.
- ensure control is attached to a live `TopLevel` and has non-zero bounds.

2. Browser integration leaks resources.
- centralize native object lifetime and release in `DestroyNativeControlCore`.

3. Platform behavior differs across targets.
- keep browser APIs behind an abstraction and provide target-specific adapters.
