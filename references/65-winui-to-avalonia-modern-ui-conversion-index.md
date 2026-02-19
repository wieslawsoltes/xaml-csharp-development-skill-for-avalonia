# WinUI to Avalonia Modern UI Conversion Index

## Table of Contents
1. Scope and Coverage Contract
2. WinUI Areas Mapped
3. Migration Workflow
4. Granular Reference Set
5. Full API Coverage Pointers
6. First Conversion Example
7. AOT/Trimming and Threading Notes
8. Troubleshooting

## Scope and Coverage Contract

This lane maps WinUI (Windows App SDK / WinUI 3) app patterns to Avalonia `11.3.12` XAML/C# patterns.

Coverage focuses on:

- property, layout, and rendering systems,
- controls, templating, resources, states, and theming,
- input/commands/navigation/dialog flows,
- platform integration and migration sequencing.

## WinUI Areas Mapped

- `DependencyObject`/`DependencyProperty` to `AvaloniaProperty`.
- WinUI panels and measure/arrange flows to Avalonia layout passes.
- `x:Bind`/`{Binding}` migration to compiled bindings.
- `VisualStateManager`/adaptive states to styles/selectors/transitions.
- control family migration (`NavigationView`, `TabView`, `TreeView`, `ItemsRepeater`, `InfoBar`, `TeachingTip`).
- `AppWindow`, `ContentDialog`, and app lifetime migration.
- composition/rendering workflows to Avalonia rendering + compositor APIs.
- command-surface migration (`CommandBarFlyout`, `MenuFlyout`, `SplitButton`, keyboard accelerators).
- advanced list/shell migration (`ListView`/`GridView` selection semantics, pane routing, container styling).
- interop/render-host migration (`SwapChainPanel`, Win2D, native host boundaries).
- platform service migration (file pickers, launcher, activation contracts, notifications, tray/menu integration).
- advanced control migration (`SwipeControl`, `RefreshContainer`, `TwoPaneView`, `Pager`, `BreadcrumbBar`, `ItemsView`).
- low-level system migration (property types/metadata/value precedence, visual vs logical trees, template name scopes).
- low-level styling/theming migration (resource lookup order, selector mapping, control themes, high-contrast live updates).
- drag/drop, clipboard, and data transfer workflows.
- localization, automation, RTL, and diagnostics/testing hardening.

## Migration Workflow

1. Port shell/lifetime first.
2. Port navigation and command surfaces.
3. Convert bindings/resources/templates/states.
4. Port control families and dialogs.
5. Port layout and rendering hot paths.
6. Verify accessibility, testing, and performance parity.

## Granular Reference Set

All detailed WinUI conversion references live under [`winui-to-avalonia/README.md`](winui-to-avalonia/README):

- [`00-winui-dependency-property-system-to-avalonia-property-system.md`](winui-to-avalonia/00-winui-dependency-property-system-to-avalonia-property-system)
- [`01-winui-layout-panels-measure-arrange-and-effective-pixels.md`](winui-to-avalonia/01-winui-layout-panels-measure-arrange-and-effective-pixels)
- [`02-winui-events-commands-keyboardaccelerators-and-input.md`](winui-to-avalonia/02-winui-events-commands-keyboardaccelerators-and-input)
- [`03-winui-binding-xbind-binding-modes-relativesource-and-updates.md`](winui-to-avalonia/03-winui-binding-xbind-binding-modes-relativesource-and-updates)
- [`04-winui-collectionviewsource-grouping-and-itemsource-patterns.md`](winui-to-avalonia/04-winui-collectionviewsource-grouping-and-itemsource-patterns)
- [`05-winui-validation-databinding-and-data-errors.md`](winui-to-avalonia/05-winui-validation-databinding-and-data-errors)
- [`06-winui-resources-theme-resources-and-merged-dictionaries.md`](winui-to-avalonia/06-winui-resources-theme-resources-and-merged-dictionaries)
- [`07-winui-styles-controltemplate-datatemplate-and-selectors.md`](winui-to-avalonia/07-winui-styles-controltemplate-datatemplate-and-selectors)
- [`08-winui-visualstatemanager-adaptive-triggers-and-state-mapping.md`](winui-to-avalonia/08-winui-visualstatemanager-adaptive-triggers-and-state-mapping)
- [`09-winui-usercontrol-custom-control-and-templatedcontrol.md`](winui-to-avalonia/09-winui-usercontrol-custom-control-and-templatedcontrol)
- [`10-winui-itemscontrol-listview-gridview-itemsrepeater-treeview.md`](winui-to-avalonia/10-winui-itemscontrol-listview-gridview-itemsrepeater-treeview)
- [`11-winui-windowing-appwindow-contentdialog-and-lifetime.md`](winui-to-avalonia/11-winui-windowing-appwindow-contentdialog-and-lifetime)
- [`12-winui-navigationview-frame-page-and-shell-patterns.md`](winui-to-avalonia/12-winui-navigationview-frame-page-and-shell-patterns)
- [`13-winui-animations-storyboard-transitions-and-composition.md`](winui-to-avalonia/13-winui-animations-storyboard-transitions-and-composition)
- [`14-winui-text-richtextblock-hyperlinks-and-rich-content.md`](winui-to-avalonia/14-winui-text-richtextblock-hyperlinks-and-rich-content)
- [`15-winui-menuflyout-commandbar-appbar-and-context-actions.md`](winui-to-avalonia/15-winui-menuflyout-commandbar-appbar-and-context-actions)
- [`16-winui-dispatcherqueue-background-work-and-async-workflows.md`](winui-to-avalonia/16-winui-dispatcherqueue-background-work-and-async-workflows)
- [`17-winui-rendering-pipeline-compositiontarget-and-custom-drawing.md`](winui-to-avalonia/17-winui-rendering-pipeline-compositiontarget-and-custom-drawing)
- [`18-winui-interop-win32-xaml-islands-and-webview2-boundaries.md`](winui-to-avalonia/18-winui-interop-win32-xaml-islands-and-webview2-boundaries)
- [`19-winui-acrylic-mica-brushes-images-media-and-asset-pipelines.md`](winui-to-avalonia/19-winui-acrylic-mica-brushes-images-media-and-asset-pipelines)
- [`20-winui-theming-high-contrast-and-requestedtheme-variants.md`](winui-to-avalonia/20-winui-theming-high-contrast-and-requestedtheme-variants)
- [`21-winui-accessibility-automation-rtl-and-localization.md`](winui-to-avalonia/21-winui-accessibility-automation-rtl-and-localization)
- [`22-winui-testing-diagnostics-and-performance-regression-safety.md`](winui-to-avalonia/22-winui-testing-diagnostics-and-performance-regression-safety)
- [`23-winui-to-avalonia-migration-playbook.md`](winui-to-avalonia/23-winui-to-avalonia-migration-playbook)
- [`24-winui-to-avalonia-api-coverage-manifest-controls-layout-styling-platform.md`](winui-to-avalonia/24-winui-to-avalonia-api-coverage-manifest-controls-layout-styling-platform)
- [`25-winui-form-input-controls-text-password-autosuggest-and-numberbox.md`](winui-to-avalonia/25-winui-form-input-controls-text-password-autosuggest-and-numberbox)
- [`26-winui-date-time-calendar-and-picker-controls.md`](winui-to-avalonia/26-winui-date-time-calendar-and-picker-controls)
- [`27-winui-choice-controls-checkbox-radio-toggle-and-splitbutton.md`](winui-to-avalonia/27-winui-choice-controls-checkbox-radio-toggle-and-splitbutton)
- [`28-winui-tabview-expander-and-sectioned-shell-layouts.md`](winui-to-avalonia/28-winui-tabview-expander-and-sectioned-shell-layouts)
- [`29-winui-tooltip-flyout-teachingtip-and-context-help-patterns.md`](winui-to-avalonia/29-winui-tooltip-flyout-teachingtip-and-context-help-patterns)
- [`30-winui-progress-slider-scrollviewer-and-feedback-controls.md`](winui-to-avalonia/30-winui-progress-slider-scrollviewer-and-feedback-controls)
- [`31-winui-dragdrop-clipboard-datapackage-and-data-transfer.md`](winui-to-avalonia/31-winui-dragdrop-clipboard-datapackage-and-data-transfer)
- [`32-winui-layout-system-invalidations-and-measure-arrange-migration.md`](winui-to-avalonia/32-winui-layout-system-invalidations-and-measure-arrange-migration)
- [`33-winui-rendering-system-visual-layer-and-composition-migration.md`](winui-to-avalonia/33-winui-rendering-system-visual-layer-and-composition-migration)
- [`34-winui-navigationview-pane-modes-and-selection-routing.md`](winui-to-avalonia/34-winui-navigationview-pane-modes-and-selection-routing)
- [`35-winui-itemsrepeater-layouts-virtualization-and-scrollhost.md`](winui-to-avalonia/35-winui-itemsrepeater-layouts-virtualization-and-scrollhost)
- [`36-winui-commandbarflyout-and-rich-command-surfaces.md`](winui-to-avalonia/36-winui-commandbarflyout-and-rich-command-surfaces)
- [`37-winui-infobar-teachingtip-and-inline-guidance-surfaces.md`](winui-to-avalonia/37-winui-infobar-teachingtip-and-inline-guidance-surfaces)
- [`38-winui-contentdialog-and-modal-workflow-migration.md`](winui-to-avalonia/38-winui-contentdialog-and-modal-workflow-migration)
- [`39-winui-theme-resource-high-contrast-and-theme-dictionaries.md`](winui-to-avalonia/39-winui-theme-resource-high-contrast-and-theme-dictionaries)
- [`40-winui-visualstatemanager-gotostate-and-adaptive-trigger-recipes.md`](winui-to-avalonia/40-winui-visualstatemanager-gotostate-and-adaptive-trigger-recipes)
- [`41-winui-xamlroot-appwindow-and-multiwindow-coordination.md`](winui-to-avalonia/41-winui-xamlroot-appwindow-and-multiwindow-coordination)
- [`42-winui-composition-visual-layer-implicit-animations-and-effects.md`](winui-to-avalonia/42-winui-composition-visual-layer-implicit-animations-and-effects)
- [`43-winui-scrollviewer-scroller-anchoring-and-bringintoview.md`](winui-to-avalonia/43-winui-scrollviewer-scroller-anchoring-and-bringintoview)
- [`44-winui-listview-gridview-selection-and-item-container-patterns.md`](winui-to-avalonia/44-winui-listview-gridview-selection-and-item-container-patterns)
- [`45-winui-swapchainpanel-win2d-and-native-render-hosting-boundaries.md`](winui-to-avalonia/45-winui-swapchainpanel-win2d-and-native-render-hosting-boundaries)
- [`46-winui-file-pickers-storage-provider-and-launcher.md`](winui-to-avalonia/46-winui-file-pickers-storage-provider-and-launcher)
- [`47-winui-activation-protocols-file-contracts-and-lifecycle.md`](winui-to-avalonia/47-winui-activation-protocols-file-contracts-and-lifecycle)
- [`48-winui-menubar-native-menu-and-system-tray-patterns.md`](winui-to-avalonia/48-winui-menubar-native-menu-and-system-tray-patterns)
- [`49-winui-toast-infobadge-and-in-app-notification-migration.md`](winui-to-avalonia/49-winui-toast-infobadge-and-in-app-notification-migration)
- [`50-winui-text-editing-ime-undo-redo-and-input-scope-mapping.md`](winui-to-avalonia/50-winui-text-editing-ime-undo-redo-and-input-scope-mapping)
- [`51-winui-pointer-gestures-touch-pen-and-inkcanvas-migration.md`](winui-to-avalonia/51-winui-pointer-gestures-touch-pen-and-inkcanvas-migration)
- [`52-winui-scrollpresenter-scrollview-snap-points-and-chaining.md`](winui-to-avalonia/52-winui-scrollpresenter-scrollview-snap-points-and-chaining)
- [`53-winui-refreshcontainer-and-pull-to-refresh-migration.md`](winui-to-avalonia/53-winui-refreshcontainer-and-pull-to-refresh-migration)
- [`54-winui-swipecontrol-list-gestures-and-item-actions.md`](winui-to-avalonia/54-winui-swipecontrol-list-gestures-and-item-actions)
- [`55-winui-adaptive-controls-twopaneview-selectorbar-breadcrumb-pager.md`](winui-to-avalonia/55-winui-adaptive-controls-twopaneview-selectorbar-breadcrumb-pager)
- [`56-winui-titlebar-systembackdrop-and-custom-window-chrome.md`](winui-to-avalonia/56-winui-titlebar-systembackdrop-and-custom-window-chrome)
- [`57-winui-xamlreader-resource-packaging-and-runtime-xaml-loading.md`](winui-to-avalonia/57-winui-xamlreader-resource-packaging-and-runtime-xaml-loading)
- [`58-winui-webview2-navigation-permissions-and-host-interop.md`](winui-to-avalonia/58-winui-webview2-navigation-permissions-and-host-interop)
- [`59-winui-itemsview-layoutpanel-and-virtualization-strategies.md`](winui-to-avalonia/59-winui-itemsview-layoutpanel-and-virtualization-strategies)
- [`60-winui-property-types-metadata-value-precedence-and-inheritance.md`](winui-to-avalonia/60-winui-property-types-metadata-value-precedence-and-inheritance)
- [`61-winui-visual-tree-logical-tree-namescope-and-templated-parent-mapping.md`](winui-to-avalonia/61-winui-visual-tree-logical-tree-namescope-and-templated-parent-mapping)
- [`62-winui-resource-lookup-order-static-vs-theme-resource-and-overrides.md`](winui-to-avalonia/62-winui-resource-lookup-order-static-vs-theme-resource-and-overrides)
- [`63-winui-style-resolution-basedon-implicit-style-and-selector-mapping.md`](winui-to-avalonia/63-winui-style-resolution-basedon-implicit-style-and-selector-mapping)
- [`64-winui-controltemplate-template-parts-and-state-contracts.md`](winui-to-avalonia/64-winui-controltemplate-template-parts-and-state-contracts)
- [`65-winui-theme-variants-high-contrast-and-live-theme-switching-internals.md`](winui-to-avalonia/65-winui-theme-variants-high-contrast-and-live-theme-switching-internals)
- [`66-winui-style-resource-and-tree-diagnostics-runtime-inspection.md`](winui-to-avalonia/66-winui-style-resource-and-tree-diagnostics-runtime-inspection)

## Full API Coverage Pointers

For exhaustive lookup (not only migration samples):

- controls: [`52-controls-reference-catalog.md`](52-controls-reference-catalog) and [`controls/README.md`](controls/README)
- layout and rendering: [`30-layout-measure-arrange-and-custom-layout-controls.md`](30-layout-measure-arrange-and-custom-layout-controls), [`14-custom-drawing-text-shapes-and-skia.md`](14-custom-drawing-text-shapes-and-skia), [`15-compositor-and-custom-visuals.md`](15-compositor-and-custom-visuals)
- styles/resources/templates: [`04-styles-themes-resources.md`](04-styles-themes-resources), [`10-templated-controls-and-control-themes.md`](10-templated-controls-and-control-themes), [`17-resources-assets-theme-variants-and-xmlns.md`](17-resources-assets-theme-variants-and-xmlns)
- signatures: [`api-index-generated.md`](api-index-generated)

## First Conversion Example

WinUI XAML:

```xaml
<Button Content="Save"
        Command="{x:Bind ViewModel.SaveCommand}" />
```

Avalonia XAML:

```xaml
<UserControl xmlns="https://github.com/avaloniaui"
             xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
             xmlns:vm="using:MyApp.ViewModels"
             x:DataType="vm:MainViewModel">
  <Button Content="Save"
          Command="{CompiledBinding SaveCommand}" />
</UserControl>
```

WinUI C# (dependency property):

```csharp
public static readonly DependencyProperty TitleProperty =
    DependencyProperty.Register(nameof(Title), typeof(string), typeof(HeaderCard), new PropertyMetadata(""));
```

Avalonia C#:

```csharp
public static readonly StyledProperty<string> TitleProperty =
    AvaloniaProperty.Register<HeaderCard, string>(nameof(Title), string.Empty);
```

## AOT/Trimming and Threading Notes

- Prefer compiled bindings in migrated Avalonia views.
- Replace dispatcher assumptions with explicit `Dispatcher.UIThread` usage.
- Keep runtime-dynamic XAML paths isolated from hot application paths.

## Troubleshooting

1. Visual states don't map directly.
- Model state via classes/pseudo-classes and transitions.

2. Navigation shell behavior diverges.
- Move to explicit view-model routing and content-host composition.

3. Rendering loops are expensive after migration.
- Use transitions/compositor animations first, custom draw only where necessary.
