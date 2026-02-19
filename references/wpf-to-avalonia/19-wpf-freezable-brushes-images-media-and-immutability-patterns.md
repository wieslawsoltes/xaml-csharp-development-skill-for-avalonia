# WPF Freezable, Brushes, Images, Media, and Immutability Patterns to Avalonia

## Table of Contents
1. Scope and APIs
2. Immutability Mapping
3. Conversion Example
4. Avalonia C# Equivalent
5. Troubleshooting

## Scope and APIs

Primary WPF APIs:

- `Freezable`
- mutable/frozen `Brush` and geometry resources
- image/media resource patterns

Primary Avalonia APIs:

- immutable brush interfaces (`IImmutableBrush`, `ImmutableSolidColorBrush`, etc.)
- `Brushes` and brush conversion (`ToImmutable()`)
- `Bitmap` and image source assets

## Immutability Mapping

| WPF | Avalonia |
|---|---|
| `Freezable.Freeze()` for reuse | prefer immutable brush/image resources and shared static resources |
| mutable brush in hot draw paths | convert to immutable where appropriate |
| `ImageSource` resources | Avalonia `Bitmap`/asset URI image sources |

## Conversion Example

WPF C#:

```csharp
var brush = new SolidColorBrush(Colors.DodgerBlue);
if (brush.CanFreeze)
    brush.Freeze();
```

Avalonia XAML:

```xaml
<Border xmlns="https://github.com/avaloniaui"
        xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
        Background="DodgerBlue"
        Width="120"
        Height="40" />
```

## Avalonia C# Equivalent

```csharp
using Avalonia.Media;
using Avalonia.Media.Immutable;

IImmutableSolidColorBrush accent = new ImmutableSolidColorBrush(Colors.DodgerBlue);

var mutable = new SolidColorBrush(Colors.DodgerBlue);
var immutable = mutable.ToImmutable();
```

## Troubleshooting

1. draw path allocations increase after migration.
- reuse immutable brushes/pens and avoid per-frame object creation.

2. asset images fail in packaged builds.
- verify URI and resource packaging strategy.

3. attempting direct `Freezable` API parity.
- shift to immutable resource reuse patterns.
