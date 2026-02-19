# WinUI Storyboards, Transitions, and Composition to Avalonia

## Table of Contents
1. Scope and APIs
2. Concept Mapping
3. Conversion Example
4. Migration Notes

## Scope and APIs

Primary WinUI APIs:

- Storyboard, DoubleAnimation, ConnectedAnimation, Implicit animations

Primary Avalonia APIs:

- Animation, KeyFrame, Transitions, Composition APIs

## Concept Mapping

| WinUI idiom | Avalonia idiom |
|---|---|
| WinUI control/template/state pipeline | Avalonia control theme/style/selector pipeline |
| `x:Bind` or `{Binding}` data flow | `{CompiledBinding ...}` and typed `x:DataType` flow |
| WinUI layout/render invalidation model | Avalonia `InvalidateMeasure`/`InvalidateArrange`/`InvalidateVisual` model |

## Conversion Example

WinUI XAML:

```xaml
<Page
    x:Class="MyApp.Views.SamplePage"
    xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
    xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
    xmlns:local="using:MyApp.Controls">
  <Storyboard><!-- animation --></Storyboard>
</Page>
```

WinUI C#:

```csharp
var view = new Storyboard();
```

Avalonia XAML:

```xaml
<UserControl xmlns="https://github.com/avaloniaui"
             xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
             xmlns:vm="using:MyApp.ViewModels"
             xmlns:local="using:MyApp.Controls"
             x:DataType="vm:SampleViewModel">
  <UserControl.Styles>
    <Style Selector="Border#PulseTarget">
      <Setter Property="Opacity" Value="0" />
      <Style.Animations>
        <Animation Duration="0:0:0.25">
          <KeyFrame Cue="100%">
            <Setter Property="Opacity" Value="1" />
          </KeyFrame>
        </Animation>
      </Style.Animations>
    </Style>
  </UserControl.Styles>
  <Border x:Name="PulseTarget" Width="120" Height="32" />
</UserControl>
```

Avalonia C#:

```csharp
control.Transitions = new Transitions { new DoubleTransition { Property = Visual.OpacityProperty, Duration = TimeSpan.FromMilliseconds(250) } };
```

## Migration Notes

1. Start by porting behavior and state contracts first, then restyle and retune visuals.
2. Prefer typed compiled bindings and avoid reflection-heavy dynamic binding paths.
3. Keep UI-thread updates explicit when porting WinUI async/event flows.
