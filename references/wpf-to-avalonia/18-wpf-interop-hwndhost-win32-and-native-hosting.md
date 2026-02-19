# WPF Interop (HwndHost/Win32) and Native Hosting to Avalonia

## Table of Contents
1. Scope and APIs
2. Interop Mapping
3. Conversion Example
4. Avalonia C# Equivalent
5. Troubleshooting

## Scope and APIs

Primary WPF APIs:

- `HwndHost`
- `WindowInteropHelper`
- `WindowsFormsHost`

Primary Avalonia APIs:

- `NativeControlHost`
- platform handles (`IPlatformHandle`)
- `TopLevel` and platform features

## Interop Mapping

| WPF | Avalonia |
|---|---|
| `HwndHost` for native child window | `NativeControlHost` |
| direct window handle interop helper | `TopLevel`/platform-handle access paths |
| `WindowsFormsHost` | explicit native-host integration layer |

## Conversion Example

WPF C#:

```csharp
public sealed class NativePreviewHost : HwndHost
{
    protected override HandleRef BuildWindowCore(HandleRef hwndParent)
    {
        // create child HWND
    }
}
```

Avalonia XAML:

```xaml
<local:NativePreviewHost xmlns="https://github.com/avaloniaui"
                         xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
                         xmlns:local="using:MyApp.Controls" />
```

## Avalonia C# Equivalent

```csharp
using Avalonia.Controls;
using Avalonia.Controls.Platform;
using Avalonia.Platform;

public sealed class NativePreviewHost : NativeControlHost
{
    protected override IPlatformHandle CreateNativeControlCore(IPlatformHandle parent)
    {
        // create platform-native child and return its handle wrapper.
        return base.CreateNativeControlCore(parent);
    }

    protected override void DestroyNativeControlCore(IPlatformHandle control)
    {
        // release native resources allocated in CreateNativeControlCore.
        base.DestroyNativeControlCore(control);
    }
}
```

## Troubleshooting

1. hosted native view stays hidden.
- ensure host has non-zero size and is attached to a live `TopLevel`.

2. crashes on close/reparent.
- centralize ownership and teardown in `DestroyNativeControlCore`.

3. behavior differs by platform.
- isolate interop behind adapters and keep the app-facing interface stable.
