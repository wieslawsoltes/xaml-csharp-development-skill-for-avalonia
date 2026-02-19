# WPF to Avalonia Modern UI Conversion Index

## Table of Contents
1. Scope and Coverage Contract
2. WPF Areas Mapped
3. Migration Workflow
4. Granular Reference Set
5. Full API Coverage Pointers
6. First Conversion Example
7. AOT/Trimming and Threading Notes
8. Troubleshooting

## Scope and Coverage Contract

This reference lane maps WPF application patterns to Avalonia `11.3.12` XAML/C# patterns for:

- property system and control authoring,
- layout, binding, validation, and templating,
- commands/input, windowing/navigation, and platform services,
- rendering, animation, styling/theming, and diagnostics.

Coverage intent for this lane:

- migration guidance is practical and example-driven,
- API lookup is exhaustive through generated references:
  - controls: one file per control in [`controls/README.md`](controls/README),
  - signatures: [`api-index-generated.md`](api-index-generated).

## WPF Areas Mapped

- `DependencyProperty` and attached-property patterns to `AvaloniaProperty` (`StyledProperty`/`DirectProperty`).
- routed events, commanding, and input gestures.
- binding expressions (`Mode`, `UpdateSourceTrigger`, `RelativeSource`, `ElementName`) and typed bindings.
- resources, styles, templates, triggers/visual-state migration strategies.
- `UserControl`/`CustomControl` patterns and template parts.
- layout panels and measure/arrange custom layout flows.
- layout-system migration (`LayoutManager`, measure/arrange invalidation queues, `UpdateLayout` usage boundaries).
- dialogs/window lifetime and navigation shell migration.
- `Dispatcher`, timers, background work, and UI-thread marshaling.
- rendering (`OnRender`, adorner, drawing primitives) and animation/storyboards.
- rendering-system migration (`Visual`, `DrawingVisual`, `CompositionTarget.Rendering`) to Avalonia `Render` + compositor/animation patterns.
- interoperability boundaries (`HwndHost`, Win32 integration) and migration alternatives.
- form and choice controls (`TextBox`, `PasswordBox`, `ComboBox`, `CheckBox`, `RadioButton`, toggle patterns).
- date/time and calendar controls (`DatePicker`, `Calendar`, `TimePicker`, `CalendarDatePicker`) with type-mapping notes.
- sectioned shell composition (`TabControl`, `Expander`, `GroupBox`) and state-preservation patterns.
- contextual help UX (`ToolTip`, popup semantics, `HyperlinkButton`, launcher integration).
- range/feedback controls (`ProgressBar`, `Slider`, `ScrollBar`) and high-frequency update guidance.
- image/icon asset migration (`BitmapImage`/pack URIs to `avares://`, `Bitmap`, `WindowIcon`).
- drag/drop and clipboard migration (`DataObject`/`Clipboard` to `DataTransfer` and `TopLevel.Clipboard`).
- printing/document workflow migration (`PrintDialog`/`DocumentPaginator` to export-preview pipelines).
- dialog and notifications migration (`MessageBox` patterns, async dialog results, `WindowNotificationManager`).
- rich reading surfaces migration (`DocumentViewer`/`FlowDocumentReader` to templated reading hosts).
- advanced layout migration (`GridSplitter`, `UniformGrid`, `Grid.IsSharedSizeScope`, shared column groups).
- selection-model migration (`SelectionMode`, `SelectedItems`, `AutoScrollToSelectedItem` for list/tree controls).
- popup and command routing migration (`Popup`/`Flyout` light-dismiss, `RoutedCommand`/`CommandManager` replacement patterns).
- keyboard and scroll UX migration (access keys, tab navigation, `ScrollViewer` offset/deferred scrolling).
- hierarchical template migration (`HierarchicalDataTemplate` to `TreeDataTemplate`/`FuncTreeDataTemplate`).

## Migration Workflow

1. Port app lifetime and top-level window architecture.
2. Port property system and reusable control contracts.
3. Convert layouts and bindings to typed view-model patterns.
4. Replace WPF trigger/visual-state usage with Avalonia selectors/pseudo-classes/transitions.
5. Port commands/input, dialogs, and platform services.
6. Port custom rendering/interop and harden with diagnostics + tests.

## Granular Reference Set

- All detailed WPF conversion references live under [`wpf-to-avalonia/README.md`](wpf-to-avalonia/README):
  - [`00-wpf-dependency-property-system-to-avalonia-property-system.md`](wpf-to-avalonia/00-wpf-dependency-property-system-to-avalonia-property-system)
  - [`01-wpf-layout-panels-measure-arrange-and-dpi.md`](wpf-to-avalonia/01-wpf-layout-panels-measure-arrange-and-dpi)
  - [`02-wpf-routed-events-commands-and-inputbindings.md`](wpf-to-avalonia/02-wpf-routed-events-commands-and-inputbindings)
  - [`03-wpf-binding-modes-relativesource-elementname-and-updatesource.md`](wpf-to-avalonia/03-wpf-binding-modes-relativesource-elementname-and-updatesource)
  - [`04-wpf-collectionview-group-sort-filter-to-avalonia-patterns.md`](wpf-to-avalonia/04-wpf-collectionview-group-sort-filter-to-avalonia-patterns)
  - [`05-wpf-validation-rules-exceptions-and-inotifydataerrorinfo.md`](wpf-to-avalonia/05-wpf-validation-rules-exceptions-and-inotifydataerrorinfo)
  - [`06-wpf-resources-staticresource-dynamicresource-and-merged-dictionaries.md`](wpf-to-avalonia/06-wpf-resources-staticresource-dynamicresource-and-merged-dictionaries)
  - [`07-wpf-styles-controltemplate-datatemplate-and-selectors.md`](wpf-to-avalonia/07-wpf-styles-controltemplate-datatemplate-and-selectors)
  - [`08-wpf-triggers-multitriggers-datatriggers-and-visual-state-mapping.md`](wpf-to-avalonia/08-wpf-triggers-multitriggers-datatriggers-and-visual-state-mapping)
  - [`09-wpf-usercontrol-customcontrol-and-templatedcontrol.md`](wpf-to-avalonia/09-wpf-usercontrol-customcontrol-and-templatedcontrol)
  - [`10-wpf-itemscontrol-listview-datagrid-treeview-and-virtualization.md`](wpf-to-avalonia/10-wpf-itemscontrol-listview-datagrid-treeview-and-virtualization)
  - [`11-wpf-windowing-dialogs-owned-windows-and-lifetime.md`](wpf-to-avalonia/11-wpf-windowing-dialogs-owned-windows-and-lifetime)
  - [`12-wpf-navigation-frame-page-and-region-shell-patterns.md`](wpf-to-avalonia/12-wpf-navigation-frame-page-and-region-shell-patterns)
  - [`13-wpf-animations-storyboards-transforms-and-transitions.md`](wpf-to-avalonia/13-wpf-animations-storyboards-transforms-and-transitions)
  - [`14-wpf-text-typography-documents-and-rich-content.md`](wpf-to-avalonia/14-wpf-text-typography-documents-and-rich-content)
  - [`15-wpf-menus-toolbars-contextmenus-status-and-tray.md`](wpf-to-avalonia/15-wpf-menus-toolbars-contextmenus-status-and-tray)
  - [`16-wpf-dispatcher-backgroundworker-timers-and-async-workflows.md`](wpf-to-avalonia/16-wpf-dispatcher-backgroundworker-timers-and-async-workflows)
  - [`17-wpf-onrender-drawingvisual-adorner-and-custom-rendering.md`](wpf-to-avalonia/17-wpf-onrender-drawingvisual-adorner-and-custom-rendering)
  - [`18-wpf-interop-hwndhost-win32-and-native-hosting.md`](wpf-to-avalonia/18-wpf-interop-hwndhost-win32-and-native-hosting)
  - [`19-wpf-freezable-brushes-images-media-and-immutability-patterns.md`](wpf-to-avalonia/19-wpf-freezable-brushes-images-media-and-immutability-patterns)
  - [`20-wpf-theming-theme-dictionaries-high-contrast-and-variants.md`](wpf-to-avalonia/20-wpf-theming-theme-dictionaries-high-contrast-and-variants)
  - [`21-wpf-accessibility-automation-rtl-and-localization.md`](wpf-to-avalonia/21-wpf-accessibility-automation-rtl-and-localization)
  - [`22-wpf-testing-diagnostics-and-performance-regression-safety.md`](wpf-to-avalonia/22-wpf-testing-diagnostics-and-performance-regression-safety)
  - [`23-wpf-to-avalonia-migration-playbook.md`](wpf-to-avalonia/23-wpf-to-avalonia-migration-playbook)
  - [`24-wpf-to-avalonia-api-coverage-manifest-controls-layout-styling-platform.md`](wpf-to-avalonia/24-wpf-to-avalonia-api-coverage-manifest-controls-layout-styling-platform)
  - [`25-wpf-form-input-controls-text-password-combo-and-entry-patterns.md`](wpf-to-avalonia/25-wpf-form-input-controls-text-password-combo-and-entry-patterns)
  - [`26-wpf-date-time-calendar-and-picker-controls.md`](wpf-to-avalonia/26-wpf-date-time-calendar-and-picker-controls)
  - [`27-wpf-choice-controls-checkbox-radio-toggle-and-state-modeling.md`](wpf-to-avalonia/27-wpf-choice-controls-checkbox-radio-toggle-and-state-modeling)
  - [`28-wpf-tabcontrol-expander-groupbox-and-sectioned-shell-layouts.md`](wpf-to-avalonia/28-wpf-tabcontrol-expander-groupbox-and-sectioned-shell-layouts)
  - [`29-wpf-tooltip-popup-context-help-and-launcher-patterns.md`](wpf-to-avalonia/29-wpf-tooltip-popup-context-help-and-launcher-patterns)
  - [`30-wpf-progress-slider-scrollbar-and-feedback-controls.md`](wpf-to-avalonia/30-wpf-progress-slider-scrollbar-and-feedback-controls)
  - [`31-wpf-image-icon-bitmap-and-resource-asset-pipelines.md`](wpf-to-avalonia/31-wpf-image-icon-bitmap-and-resource-asset-pipelines)
  - [`32-wpf-dragdrop-clipboard-and-dataobject-to-avalonia-data-transfer.md`](wpf-to-avalonia/32-wpf-dragdrop-clipboard-and-dataobject-to-avalonia-data-transfer)
  - [`33-wpf-printing-documentpaginator-and-export-preview-workflows.md`](wpf-to-avalonia/33-wpf-printing-documentpaginator-and-export-preview-workflows)
  - [`34-wpf-messagebox-dialogs-and-notification-flows.md`](wpf-to-avalonia/34-wpf-messagebox-dialogs-and-notification-flows)
  - [`35-wpf-documentviewer-flowdocumentreader-and-rich-reading-surfaces.md`](wpf-to-avalonia/35-wpf-documentviewer-flowdocumentreader-and-rich-reading-surfaces)
  - [`36-wpf-gridsplitter-uniformgrid-and-shared-size-layout-patterns.md`](wpf-to-avalonia/36-wpf-gridsplitter-uniformgrid-and-shared-size-layout-patterns)
  - [`37-wpf-listbox-listview-selection-multiselect-and-autoscroll-patterns.md`](wpf-to-avalonia/37-wpf-listbox-listview-selection-multiselect-and-autoscroll-patterns)
  - [`38-wpf-popup-placement-target-light-dismiss-and-flyout-patterns.md`](wpf-to-avalonia/38-wpf-popup-placement-target-light-dismiss-and-flyout-patterns)
  - [`39-wpf-multibinding-stringformat-and-prioritybinding-fallback-patterns.md`](wpf-to-avalonia/39-wpf-multibinding-stringformat-and-prioritybinding-fallback-patterns)
  - [`40-wpf-commandmanager-routedcommand-and-commandbinding-migration.md`](wpf-to-avalonia/40-wpf-commandmanager-routedcommand-and-commandbinding-migration)
  - [`41-wpf-access-keys-label-target-focus-scope-and-tab-navigation.md`](wpf-to-avalonia/41-wpf-access-keys-label-target-focus-scope-and-tab-navigation)
  - [`42-wpf-scrollviewer-bringintoview-deferred-scrolling-and-offset-control.md`](wpf-to-avalonia/42-wpf-scrollviewer-bringintoview-deferred-scrolling-and-offset-control)
  - [`43-wpf-treeview-hierarchicaldatatemplate-expansion-and-selection.md`](wpf-to-avalonia/43-wpf-treeview-hierarchicaldatatemplate-expansion-and-selection)
  - [`44-wpf-layout-system-layoutmanager-invalidations-and-migration.md`](wpf-to-avalonia/44-wpf-layout-system-layoutmanager-invalidations-and-migration)
  - [`45-wpf-rendering-visual-layer-composition-and-migration.md`](wpf-to-avalonia/45-wpf-rendering-visual-layer-composition-and-migration)

## Full API Coverage Pointers

For exhaustive lookup (not only migration samples):

- controls: [`52-controls-reference-catalog.md`](52-controls-reference-catalog) and [`controls/README.md`](controls/README)
- layout and custom layout internals: [`30-layout-measure-arrange-and-custom-layout-controls.md`](30-layout-measure-arrange-and-custom-layout-controls), [`21-custom-layout-authoring.md`](21-custom-layout-authoring)
- styles/templates/resources: [`04-styles-themes-resources.md`](04-styles-themes-resources), [`10-templated-controls-and-control-themes.md`](10-templated-controls-and-control-themes), [`17-resources-assets-theme-variants-and-xmlns.md`](17-resources-assets-theme-variants-and-xmlns)
- binding/validation/automation: [`02-bindings-xaml-aot.md`](02-bindings-xaml-aot), [`22-validation-pipeline-and-data-errors.md`](22-validation-pipeline-and-data-errors), [`23-accessibility-and-automation.md`](23-accessibility-and-automation)
- signatures: [`api-index-generated.md`](api-index-generated)

## First Conversion Example

WPF XAML:

```xaml
<Button Content="Save"
        Command="{Binding SaveCommand}"
        Width="120"
        HorizontalAlignment="Right" />
```

Avalonia XAML:

```xaml
<UserControl xmlns="https://github.com/avaloniaui"
             xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
             xmlns:vm="using:MyApp.ViewModels"
             x:DataType="vm:MainViewModel">
  <Button Content="Save"
          Command="{CompiledBinding SaveCommand}"
          Width="120"
          HorizontalAlignment="Right" />
</UserControl>
```

WPF C#:

```csharp
public static readonly DependencyProperty TitleProperty =
    DependencyProperty.Register(nameof(Title), typeof(string), typeof(HeaderCard),
        new FrameworkPropertyMetadata(string.Empty));
```

Avalonia C#:

```csharp
public static readonly StyledProperty<string> TitleProperty =
    AvaloniaProperty.Register<HeaderCard, string>(nameof(Title), string.Empty);
```

## AOT/Trimming and Threading Notes

- favor compiled bindings (`x:DataType` + `{CompiledBinding ...}`) in migrated views.
- avoid reflection-heavy runtime binding features where typed alternatives exist.
- migrate `Dispatcher.Invoke` patterns to `Dispatcher.UIThread` and keep UI mutation explicit.

## Troubleshooting

1. WPF visual-state-heavy templates do not map directly.
- model states with pseudo-classes, classes, and transitions.

2. command routing behavior differs.
- register explicit `KeyBinding` and command scope on view roots.

3. navigation assumptions from `Frame/Page` fail.
- use view-model-driven region/content routing patterns.
