# WPF to Avalonia API Coverage Manifest (Controls, Layout, Styling, Platform)

## Table of Contents
1. Purpose
2. Coverage Contract
3. WPF Source Coverage Pointers
4. Avalonia API Coverage Path
5. Validation Workflow
6. How to Use This Manifest

## Purpose

This manifest defines how WPF migration references map to exact API lookup surfaces in this repository.

Use it to move from migration guidance to concrete signatures and source verification.

## Coverage Contract

Practical lookup completeness is provided by combining:

1. WPF migration topic docs (`00`-`45`) in this lane,
2. per-control docs in [`../controls/README.md`](../controls/README),
3. generated signatures in [`../api-index-generated.md`](../api-index-generated).

## WPF Source Coverage Pointers

Use these source roots for WPF-side verification:

- `/Users/wieslawsoltes/GitHub/wpf/src/Microsoft.DotNet.Wpf/src/WindowsBase/System/Windows/DependencyObject.cs`
- `/Users/wieslawsoltes/GitHub/wpf/src/Microsoft.DotNet.Wpf/src/WindowsBase/System/Windows/DependencyProperty.cs`
- `/Users/wieslawsoltes/GitHub/wpf/src/Microsoft.DotNet.Wpf/src/PresentationFramework/System/Windows/Application.cs`
- `/Users/wieslawsoltes/GitHub/wpf/src/Microsoft.DotNet.Wpf/src/PresentationFramework/System/Windows/Window.cs`
- `/Users/wieslawsoltes/GitHub/wpf/src/Microsoft.DotNet.Wpf/src/PresentationCore/System/Windows/UIElement.cs`
- `/Users/wieslawsoltes/GitHub/wpf/src/Microsoft.DotNet.Wpf/src/PresentationFramework/System/Windows/FrameworkElement.cs`
- `/Users/wieslawsoltes/GitHub/wpf/src/Microsoft.DotNet.Wpf/src/PresentationFramework/System/Windows/Controls/Panel.cs`
- `/Users/wieslawsoltes/GitHub/wpf/src/Microsoft.DotNet.Wpf/src/PresentationCore/System/Windows/LayoutManager.cs`
- `/Users/wieslawsoltes/GitHub/wpf/src/Microsoft.DotNet.Wpf/src/PresentationCore/System/Windows/Media/Visual.cs`
- `/Users/wieslawsoltes/GitHub/wpf/src/Microsoft.DotNet.Wpf/src/PresentationCore/System/Windows/Media/DrawingVisual.cs`
- `/Users/wieslawsoltes/GitHub/wpf/src/Microsoft.DotNet.Wpf/src/PresentationCore/System/Windows/Media/DrawingContext.cs`
- `/Users/wieslawsoltes/GitHub/wpf/src/Microsoft.DotNet.Wpf/src/PresentationCore/System/Windows/Media/CompositionTarget.cs`
- `/Users/wieslawsoltes/GitHub/wpf/src/Microsoft.DotNet.Wpf/src/PresentationFramework/System/Windows/Data/Binding.cs`
- `/Users/wieslawsoltes/GitHub/wpf/src/Microsoft.DotNet.Wpf/src/WindowsBase/System/Windows/Threading/Dispatcher.cs`

## Avalonia API Coverage Path

Primary lookup references:

- controls catalog: [`../52-controls-reference-catalog.md`](../52-controls-reference-catalog)
- generated control docs: [`../controls/README.md`](../controls/README)
- signatures: [`../api-index-generated.md`](../api-index-generated)

Useful signature queries:

```bash
rg -n "AvaloniaProperty|StyledProperty|DirectProperty|RegisterAttached" references/api-index-generated.md
rg -n "ControlTheme|DataTemplate|ControlTemplate|TemplateBinding" references/api-index-generated.md
rg -n "Dispatcher|DispatcherTimer|KeyBinding|KeyGesture" references/api-index-generated.md
rg -n "IStorageProvider|Window|ShowDialog|TopLevel" references/api-index-generated.md
rg -n "DataValidationErrors|AutomationProperties|FlowDirection|AdornerLayer" references/api-index-generated.md
```

## Validation Workflow

Run after significant API-oriented migration updates:

```bash
python3 scripts/find_uncovered_apis.py --output plan/api-coverage-not-covered.md
python3 -m unittest scripts.test_find_uncovered_apis
```

## How to Use This Manifest

1. choose the migration topic doc (`00`-`45`),
2. confirm concrete APIs in controls docs and signature index,
3. verify final patterns against Avalonia `11.3.12` behavior.
