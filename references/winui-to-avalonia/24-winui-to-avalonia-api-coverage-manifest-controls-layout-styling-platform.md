# WinUI to Avalonia API Coverage Manifest (Controls, Layout, Styling, Platform)

## Table of Contents
1. Purpose
2. Coverage Contract
3. WinUI Source Coverage Pointers
4. WinUI Online API Documentation Pointers
5. Avalonia API Coverage Path
6. Validation Workflow
7. How to Use This Manifest

## Purpose

This manifest defines how WinUI migration references map to exact API lookup surfaces.

Use it to move from recipe-level guidance to concrete source and API signatures.

## Coverage Contract

Practical completeness is provided by combining:

1. WinUI migration topic docs (`00`-`66`) in this lane,
2. per-control docs in [`../controls/README.md`](../controls/README),
3. generated signatures in [`../api-index-generated.md`](../api-index-generated).

## WinUI Source Coverage Pointers

Use these source roots for WinUI-side verification:

- `/Users/wieslawsoltes/GitHub/microsoft-ui-xaml/src/dxaml/xcp/core/inc/CDependencyObject.h`
- `/Users/wieslawsoltes/GitHub/microsoft-ui-xaml/src/dxaml/xcp/core/inc/CControl.h`
- `/Users/wieslawsoltes/GitHub/microsoft-ui-xaml/src/dxaml/xcp/core/inc/Grid.h`
- `/Users/wieslawsoltes/GitHub/microsoft-ui-xaml/src/dxaml/xcp/core/inc/StackPanel.h`
- `/Users/wieslawsoltes/GitHub/microsoft-ui-xaml/src/dxaml/xcp/core/inc/RelativePanel.h`
- `/Users/wieslawsoltes/GitHub/microsoft-ui-xaml/src/dxaml/xcp/core/inc/ScrollViewer.h`
- `/Users/wieslawsoltes/GitHub/microsoft-ui-xaml/src/dxaml/xcp/core/inc/VisualStateManager.h`
- `/Users/wieslawsoltes/GitHub/microsoft-ui-xaml/src/dxaml/xcp/components/resources/ResourceDictionary.cpp`
- `/Users/wieslawsoltes/GitHub/microsoft-ui-xaml/src/dxaml/xcp/core/inc/frameworkelementex.h`
- `/Users/wieslawsoltes/GitHub/microsoft-ui-xaml/src/dxaml/xcp/components/DependencyObject/PropertySystem.cpp`
- `/Users/wieslawsoltes/GitHub/microsoft-ui-xaml/src/dxaml/xcp/components/vsm/CVisualStateManager2.cpp`
- `/Users/wieslawsoltes/GitHub/microsoft-ui-xaml/src/controls/dev/NavigationView/NavigationView.idl`
- `/Users/wieslawsoltes/GitHub/microsoft-ui-xaml/src/controls/dev/TabView/TabView.idl`
- `/Users/wieslawsoltes/GitHub/microsoft-ui-xaml/src/controls/dev/TreeView/TreeView.idl`
- `/Users/wieslawsoltes/GitHub/microsoft-ui-xaml/src/controls/dev/InfoBar/InfoBar.idl`
- `/Users/wieslawsoltes/GitHub/microsoft-ui-xaml/src/controls/dev/TeachingTip/TeachingTip.idl`
- `/Users/wieslawsoltes/GitHub/microsoft-ui-xaml/src/controls/dev/Repeater/ItemsRepeater.idl`
- `/Users/wieslawsoltes/GitHub/microsoft-ui-xaml/src/controls/dev/MenuBar/MenuBar.idl`
- `/Users/wieslawsoltes/GitHub/microsoft-ui-xaml/src/controls/dev/InfoBadge/InfoBadge.idl`
- `/Users/wieslawsoltes/GitHub/microsoft-ui-xaml/src/controls/dev/ScrollPresenter/ScrollPresenter.idl`
- `/Users/wieslawsoltes/GitHub/microsoft-ui-xaml/src/controls/dev/ScrollView/ScrollView.idl`
- `/Users/wieslawsoltes/GitHub/microsoft-ui-xaml/src/controls/dev/PullToRefresh/RefreshContainer/RefreshContainer.idl`
- `/Users/wieslawsoltes/GitHub/microsoft-ui-xaml/src/controls/dev/SwipeControl/SwipeControl.idl`
- `/Users/wieslawsoltes/GitHub/microsoft-ui-xaml/src/controls/dev/TwoPaneView/TwoPaneView.idl`
- `/Users/wieslawsoltes/GitHub/microsoft-ui-xaml/src/controls/dev/SelectorBar/SelectorBar.idl`
- `/Users/wieslawsoltes/GitHub/microsoft-ui-xaml/src/controls/dev/Breadcrumb/BreadcrumbBar.idl`
- `/Users/wieslawsoltes/GitHub/microsoft-ui-xaml/src/controls/dev/PagerControl/PagerControl.idl`
- `/Users/wieslawsoltes/GitHub/microsoft-ui-xaml/src/controls/dev/PipsPager/PipsPager.idl`
- `/Users/wieslawsoltes/GitHub/microsoft-ui-xaml/src/controls/dev/TitleBar/TitleBar.idl`
- `/Users/wieslawsoltes/GitHub/microsoft-ui-xaml/src/controls/dev/WebView2/WebView2.idl`
- `/Users/wieslawsoltes/GitHub/microsoft-ui-xaml/src/controls/dev/LayoutPanel/LayoutPanel.idl`
- `/Users/wieslawsoltes/GitHub/microsoft-ui-xaml/src/controls/dev/ItemsView/ItemsView.idl`

## WinUI Online API Documentation Pointers

Use official WinUI/Windows App SDK docs for API verification:

- `https://learn.microsoft.com/windows/windows-app-sdk/api/winrt/microsoft.ui.xaml`
- `https://learn.microsoft.com/windows/windows-app-sdk/api/winrt/microsoft.ui.xaml.controls.navigationview`
- `https://learn.microsoft.com/windows/windows-app-sdk/api/winrt/microsoft.ui.xaml.controls.tabview`
- `https://learn.microsoft.com/windows/windows-app-sdk/api/winrt/microsoft.ui.xaml.controls.treeview`
- `https://learn.microsoft.com/windows/windows-app-sdk/api/winrt/microsoft.ui.xaml.controls.itemsrepeater`
- `https://learn.microsoft.com/windows/windows-app-sdk/api/winrt/microsoft.ui.xaml.controls.infobar`
- `https://learn.microsoft.com/windows/windows-app-sdk/api/winrt/microsoft.ui.xaml.controls.teachingtip`
- `https://learn.microsoft.com/windows/windows-app-sdk/api/winrt/microsoft.ui.xaml.controls.menubar`
- `https://learn.microsoft.com/windows/windows-app-sdk/api/winrt/microsoft.ui.xaml.controls.infobadge`
- `https://learn.microsoft.com/windows/windows-app-sdk/api/winrt/microsoft.ui.xaml.controls.scrollpresenter`
- `https://learn.microsoft.com/windows/windows-app-sdk/api/winrt/microsoft.ui.xaml.controls.scrollview`
- `https://learn.microsoft.com/windows/windows-app-sdk/api/winrt/microsoft.ui.xaml.controls.refreshcontainer`
- `https://learn.microsoft.com/windows/windows-app-sdk/api/winrt/microsoft.ui.xaml.controls.swipecontrol`
- `https://learn.microsoft.com/windows/windows-app-sdk/api/winrt/microsoft.ui.xaml.controls.twopaneview`
- `https://learn.microsoft.com/windows/windows-app-sdk/api/winrt/microsoft.ui.xaml.controls.selectorbar`
- `https://learn.microsoft.com/windows/windows-app-sdk/api/winrt/microsoft.ui.xaml.controls.breadcrumbbar`
- `https://learn.microsoft.com/windows/windows-app-sdk/api/winrt/microsoft.ui.xaml.controls.pagercontrol`
- `https://learn.microsoft.com/windows/windows-app-sdk/api/winrt/microsoft.ui.xaml.controls.pipspager`
- `https://learn.microsoft.com/windows/windows-app-sdk/api/winrt/microsoft.ui.xaml.controls.titlebar`
- `https://learn.microsoft.com/windows/windows-app-sdk/api/winrt/microsoft.ui.xaml.controls.webview2`
- `https://learn.microsoft.com/windows/windows-app-sdk/api/winrt/microsoft.ui.xaml.controls.itemsview`
- `https://learn.microsoft.com/windows/windows-app-sdk/api/winrt/microsoft.ui.xaml.media.visualtreehelper`
- `https://learn.microsoft.com/windows/windows-app-sdk/api/winrt/microsoft.ui.xaml.dependencyproperty`
- `https://learn.microsoft.com/windows/windows-app-sdk/api/winrt/microsoft.ui.xaml.resourcedictionary`
- `https://learn.microsoft.com/windows/windows-app-sdk/api/winrt/microsoft.ui.xaml.visualstatemanager`
- `https://learn.microsoft.com/windows/windows-app-sdk/api/winrt/microsoft.ui.windowing.appwindow`
- `https://learn.microsoft.com/windows/windows-app-sdk/api/winrt/microsoft.ui.xaml.media.compositiontarget`

## Avalonia API Coverage Path

Primary lookup references:

- controls catalog: [`../52-controls-reference-catalog.md`](../52-controls-reference-catalog)
- generated control docs: [`../controls/README.md`](../controls/README)
- signatures: [`../api-index-generated.md`](../api-index-generated)

Useful signature queries:

```bash
rg -n "AvaloniaProperty|StyledProperty|DirectProperty|RegisterAttached" references/api-index-generated.md
rg -n "TabControl|TreeView|SplitView|ItemsControl|AutoCompleteBox" references/api-index-generated.md
rg -n "ControlTheme|DataTemplate|ControlTemplate|TemplateBinding" references/api-index-generated.md
rg -n "Dispatcher|DispatcherTimer|KeyBinding|KeyGesture" references/api-index-generated.md
rg -n "DataValidationErrors|AutomationProperties|FlowDirection" references/api-index-generated.md
rg -n "StorageProvider|FilePickerOpenOptions|Launcher|IActivatableLifetime" references/api-index-generated.md
rg -n "NativeMenu|NativeMenuBar|TrayIcon|WindowNotificationManager" references/api-index-generated.md
rg -n "TextInputOptions|RefreshContainer|PullGestureRecognizer|ScrollViewer|VirtualizingStackPanel" references/api-index-generated.md
rg -n "StyledProperty|DirectProperty|AttachedProperty|BindingPriority|SetCurrentValue|GetBaseValue" references/api-index-generated.md
rg -n "GetVisualParent|GetVisualChildren|GetLogicalParent|GetLogicalChildren|NameScope|TemplatedParent" references/api-index-generated.md
rg -n "ControlTheme|Style|Selector|PseudoClasses|ThemeVariant|ThemeDictionaries" references/api-index-generated.md
```

## Validation Workflow

Run after significant migration-reference updates:

```bash
python3 scripts/find_uncovered_apis.py --output plan/api-coverage-not-covered.md
python3 -m unittest scripts.test_find_uncovered_apis
```

## How to Use This Manifest

1. choose the migration topic doc (`00`-`66`),
2. confirm concrete WinUI and Avalonia APIs in source/docs,
3. validate against pinned Avalonia `11.3.12` behavior before adopting patterns.
