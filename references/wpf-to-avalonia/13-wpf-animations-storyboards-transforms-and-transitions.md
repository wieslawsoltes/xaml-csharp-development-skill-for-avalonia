# WPF Animations, Storyboards, Transforms, and Transitions to Avalonia

## Table of Contents
1. Scope and APIs
2. Animation Mapping
3. Conversion Example
4. Avalonia C# Equivalent
5. Troubleshooting

## Scope and APIs

Primary WPF APIs:

- `Storyboard`
- keyframe/timeline animation classes
- transform animations

Primary Avalonia APIs:

- `Transitions` (`DoubleTransition`, etc.)
- `Animation` keyframes
- transforms + compositor path for advanced scenarios

## Animation Mapping

| WPF | Avalonia |
|---|---|
| property animation with `Storyboard` | transitions or `Animation` keyframes |
| visual-state storyboard sets | class/pseudo-class switches + transitions |
| per-frame custom animation | compositor/custom render path when required |

## Conversion Example

WPF XAML:

```xaml
<DoubleAnimation Storyboard.TargetProperty="Opacity"
                 To="0.6"
                 Duration="0:0:0.2" />
```

Avalonia XAML:

```xaml
<Button xmlns="https://github.com/avaloniaui"
        xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
        Classes="fade-on-hover"
        Content="Hover me">
  <Button.Transitions>
    <Transitions>
      <DoubleTransition Property="Opacity" Duration="0:0:0.2" />
    </Transitions>
  </Button.Transitions>
</Button>

<Style xmlns="https://github.com/avaloniaui" Selector="Button.fade-on-hover:pointerover">
  <Setter Property="Opacity" Value="0.6" />
</Style>
```

## Avalonia C# Equivalent

```csharp
using System;
using Avalonia;
using Avalonia.Animation;
using Avalonia.Controls;

var btn = new Button { Content = "Hover me" };
btn.Transitions = new Transitions
{
    new DoubleTransition
    {
        Property = Visual.OpacityProperty,
        Duration = TimeSpan.FromMilliseconds(200)
    }
};
```

## Troubleshooting

1. animation feels different than WPF storyboard timing.
- tune easing and duration in transitions/keyframes.

2. state-driven animation never starts.
- verify class or pseudo-class state actually changes.

3. performance drops on many animated elements.
- keep animations simple and use compositor/custom paths for hotspots only.
