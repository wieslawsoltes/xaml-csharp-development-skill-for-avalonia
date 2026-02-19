# WPF Image, Icon, Bitmap, and Resource Asset Pipelines to Avalonia

## Table of Contents
1. Scope and APIs
2. Image/Asset Mapping
3. Conversion Example
4. Avalonia C# Equivalent
5. Troubleshooting

## Scope and APIs

Primary WPF APIs:

- `Image`
- `BitmapImage` + pack URIs
- `Window.Icon`

Primary Avalonia APIs:

- `Image`
- asset URIs (`avares://...`)
- `Bitmap`, `WindowIcon`

## Image/Asset Mapping

| WPF | Avalonia |
|---|---|
| pack URI resource image | `avares://` resource URI |
| `BitmapImage` loading | `Bitmap` from asset stream |
| `Window.Icon` | same concept via `WindowIcon` |
| dynamic image path strings in bindings | prefer typed `IImage`/`Bitmap` view-model properties |

## Conversion Example

WPF XAML:

```xaml
<Image Source="/MyApp;component/Assets/logo.png" />
```

Avalonia XAML:

```xaml
<UserControl xmlns="https://github.com/avaloniaui"
             xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
             xmlns:vm="using:MyApp.ViewModels"
             x:DataType="vm:AssetsViewModel">
  <StackPanel Spacing="8">
    <Image Width="160"
           Height="80"
           Stretch="Uniform"
           Source="avares://MyApp/Assets/logo.png" />

    <Image Width="24"
           Height="24"
           Source="{CompiledBinding SelectedIcon}" />
  </StackPanel>
</UserControl>
```

## Avalonia C# Equivalent

```csharp
using System;
using Avalonia.Controls;
using Avalonia.Media.Imaging;
using Avalonia.Platform;

public static void ApplyWindowAssets(Window window)
{
    using var imageStream = AssetLoader.Open(new Uri("avares://MyApp/Assets/logo.png"));
    var logo = new Bitmap(imageStream);

    using var iconStream = AssetLoader.Open(new Uri("avares://MyApp/Assets/app.ico"));
    window.Icon = new WindowIcon(iconStream);
}
```

## Troubleshooting

1. Images fail after publish.
- verify asset packaging and `avares://` URI paths.

2. Icons look blurry on high DPI.
- provide appropriately sized source assets.

3. Dynamic image switching lags.
- avoid repeatedly decoding large bitmaps on the UI thread.
