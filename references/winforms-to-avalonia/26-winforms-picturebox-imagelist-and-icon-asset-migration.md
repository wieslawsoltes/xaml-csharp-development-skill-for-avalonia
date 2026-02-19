# WinForms PictureBox/ImageList and Icon Asset Migration to Avalonia

## Table of Contents
1. Scope and APIs
2. Asset and Image Mapping
3. Conversion Example
4. C# Equivalent
5. Troubleshooting

## Scope and APIs

Primary WinForms APIs:

- `PictureBox`
- `ImageList`
- form/window icons

Primary Avalonia APIs:

- `Image`
- asset URIs (`avares://...`)
- `Bitmap` and `WindowIcon`
- image-driven item templates

## Asset and Image Mapping

| WinForms | Avalonia |
|---|---|
| `PictureBox.Image` | `Image.Source` |
| `ImageList` shared icons | image paths/resources in item view-models + templates |
| `Form.Icon` | `Window.Icon` (`WindowIcon`) |
| dynamic image path strings | prefer typed `IImage`/`Bitmap` view-model properties |

## Conversion Example

WinForms C#:

```csharp
pictureBox1.Image = Properties.Resources.Logo;

var list = new ImageList();
list.Images.Add("folder", Properties.Resources.Folder16);
list.Images.Add("file", Properties.Resources.File16);

listView1.SmallImageList = list;
listView1.Items.Add(new ListViewItem("Invoices") { ImageKey = "folder" });
```

Avalonia XAML:

```xaml
<UserControl xmlns="https://github.com/avaloniaui"
             xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
             xmlns:vm="using:MyApp.ViewModels"
             x:DataType="vm:AssetsViewModel">
  <Grid RowDefinitions="Auto,*" RowSpacing="8">
    <Image Grid.Row="0"
           Height="120"
           Stretch="Uniform"
           Source="{CompiledBinding SelectedImage}" />

    <ListBox Grid.Row="1" ItemsSource="{CompiledBinding Entries}">
      <ListBox.ItemTemplate>
        <DataTemplate x:DataType="vm:AssetEntryViewModel">
          <StackPanel Orientation="Horizontal" Spacing="8">
            <Image Width="16" Height="16" Source="{CompiledBinding Icon}" />
            <TextBlock Text="{CompiledBinding Name}" />
          </StackPanel>
        </DataTemplate>
      </ListBox.ItemTemplate>
    </ListBox>
  </Grid>
</UserControl>
```

## C# Equivalent

```csharp
using System;
using Avalonia.Controls;
using Avalonia.Media.Imaging;
using Avalonia.Platform;

public static void ApplyAssets(Window window, Image previewImage)
{
    using var iconStream = AssetLoader.Open(new Uri("avares://MyApp/Assets/app.ico"));
    window.Icon = new WindowIcon(iconStream);

    using var imageStream = AssetLoader.Open(new Uri("avares://MyApp/Assets/logo.png"));
    previewImage.Source = new Bitmap(imageStream);
}
```

## Troubleshooting

1. Images fail after publish.
- verify asset URIs and build packaging for image resources.

2. Icon quality is blurry on high DPI.
- provide source assets at appropriate resolutions.

3. Image-list style reuse is hard to port.
- model icon identity in item view-models and template with `Image` per row.
