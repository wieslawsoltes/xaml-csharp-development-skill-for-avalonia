# WinForms to Avalonia Modern UI Conversion Index

## Table of Contents
1. Scope and Coverage Contract
2. WinForms Areas Mapped
3. Migration Workflow
4. Granular Reference Set
5. Full API Coverage Pointers
6. First Conversion Example
7. AOT/Trimming and Threading Notes
8. Troubleshooting

## Scope and Coverage Contract

This reference lane maps Windows Forms application patterns to Avalonia `11.3.12` XAML/C# patterns for:

- layout and composition,
- events, commands, and input routing,
- data binding and validation,
- dialogs, menus, tray, notifications, and platform services,
- rendering, styling, custom controls, and migration sequencing.

Coverage intent for this lane:

- migration guidance is practical and example-driven,
- API lookup is exhaustive through generated references:
  - controls: one file per control in [`controls/README.md`](controls/README),
  - signatures: [`api-index-generated.md`](api-index-generated).

## WinForms Areas Mapped

- `Control` lifecycle (`Load`, `Shown`, `HandleCreated`, `Dispose`) to Avalonia visual tree and `TopLevel` lifecycle.
- `Dock`/`Anchor`, `FlowLayoutPanel`, `TableLayoutPanel`, `SplitContainer`, and MDI shell patterns.
- event-driven handlers to command-first patterns with `ICommand`, `KeyBinding`, and routed input.
- `BindingSource`, `DataBindings`, `ErrorProvider`, and validation behaviors.
- `DataGridView`, `ListView`, `TreeView` migration to Avalonia list/data controls.
- `MenuStrip`, `ToolStrip`, `ContextMenuStrip`, `NotifyIcon`, and status bar-style shells.
- `OpenFileDialog`/`SaveFileDialog`/`FolderBrowserDialog` to `IStorageProvider` workflows.
- `Timer`, `BackgroundWorker`, `Control.Invoke` to `DispatcherTimer` and `Dispatcher.UIThread`.
- owner-draw and `OnPaint(Graphics)` to `Render(DrawingContext)` and template/style pipelines.
- layout-system migration (`LayoutEngine`, `PerformLayout`, `SuspendLayout`/`ResumeLayout`) to Avalonia `Measure`/`Arrange` invalidation and pass sequencing.
- rendering-system migration (`WM_PAINT`, owner-draw, buffering styles) to Avalonia `Render`, `AffectsRender`, and compositor-driven redraw.
- custom WinForms controls to Avalonia `UserControl` and `TemplatedControl`.
- input-control migration (`MaskedTextBox`, `ComboBox` autocomplete, `NumericUpDown`).
- date/time and calendar migration (`DateTimePicker`, `MonthCalendar`).
- choice controls migration (`CheckBox`, `RadioButton`, `CheckedListBox` patterns).
- tabbed workspace migration (`TabControl`/`TabPage` to view-model driven tabs).
- tooltip/help guidance migration (`ToolTip`, `HelpProvider`, contextual launchers).
- progress/track feedback migration (`ProgressBar`, `TrackBar`, status indicators).
- image/icon asset migration (`PictureBox`, `ImageList`, form icons).
- inspector patterns for `PropertyGrid` replacement.
- drag/drop and clipboard migration using `DataTransfer` + `TopLevel.Clipboard`.
- printing/report workflows migrated to export + preview + launcher integrations.
- notification migration (balloon tips/dialogs to tray + in-app toasts + async dialogs).
- splitter + scrollable region migration (`Splitter`, `ScrollableControl.AutoScroll`, scrollbar visibility patterns).
- advanced `ListView` migration (details columns, grouped sections, large-data virtualization strategy).
- advanced `TreeView` migration (lazy node loading, selection sync, tri-state check patterns).
- rich text and link migration (`RichTextBox`, `LinkLabel` to inline-rich text + hyperlink command surfaces).
- toolstrip split/dropdown command-surface migration (`ToolStripSplitButton`, `ToolStripDropDownButton` to `SplitButton`/`DropDownButton` + flyouts).
- dialog key processing migration (`AcceptButton`, `CancelButton`, `ProcessCmdKey` to `IsDefault`/`IsCancel` + `KeyBinding`).
- DPI/RTL/localization/app-lifetime migration considerations.

## Migration Workflow

1. Port app shell and window lifetime first.
2. Replace layout primitives (`Dock`/`Anchor`/panels) with `Grid`-based composition.
3. Convert event handlers to command + typed binding surfaces.
4. Port data binding and validation with compiled bindings.
5. Move dialogs/menus/tray/platform services to Avalonia platform abstractions.
6. Convert custom rendering/style layers.
7. Validate behavior parity and performance.
8. Port high-usage input/date/choice control workflows.
9. Port advanced interaction patterns (drag/drop, clipboard, notifications).
10. Replace print/property-grid dependencies with explicit Avalonia patterns.

## Granular Reference Set

- All detailed WinForms conversion references live under [`winforms-to-avalonia/README.md`](winforms-to-avalonia/README):
  - [`00-winforms-control-lifecycle-and-layout-basics.md`](winforms-to-avalonia/00-winforms-control-lifecycle-and-layout-basics)
  - [`01-winforms-layout-panels-flow-table-dock-anchor.md`](winforms-to-avalonia/01-winforms-layout-panels-flow-table-dock-anchor)
  - [`02-winforms-split-container-mdi-and-navigation-shells.md`](winforms-to-avalonia/02-winforms-split-container-mdi-and-navigation-shells)
  - [`03-winforms-events-commands-shortcuts-and-input.md`](winforms-to-avalonia/03-winforms-events-commands-shortcuts-and-input)
  - [`04-winforms-data-binding-bindingsource-and-viewmodels.md`](winforms-to-avalonia/04-winforms-data-binding-bindingsource-and-viewmodels)
  - [`05-winforms-validation-errorprovider-and-data-errors.md`](winforms-to-avalonia/05-winforms-validation-errorprovider-and-data-errors)
  - [`06-winforms-datagridview-listview-treeview-to-avalonia-items-controls.md`](winforms-to-avalonia/06-winforms-datagridview-listview-treeview-to-avalonia-items-controls)
  - [`07-winforms-menus-toolstrips-contextmenus-status-and-tray.md`](winforms-to-avalonia/07-winforms-menus-toolstrips-contextmenus-status-and-tray)
  - [`08-winforms-dialogs-file-pickers-and-window-modal-workflows.md`](winforms-to-avalonia/08-winforms-dialogs-file-pickers-and-window-modal-workflows)
  - [`09-winforms-timers-backgroundworker-and-ui-thread-dispatch.md`](winforms-to-avalonia/09-winforms-timers-backgroundworker-and-ui-thread-dispatch)
  - [`10-winforms-ownerdraw-gdi-and-custom-rendering-to-avalonia.md`](winforms-to-avalonia/10-winforms-ownerdraw-gdi-and-custom-rendering-to-avalonia)
  - [`11-winforms-styling-theming-and-control-templates.md`](winforms-to-avalonia/11-winforms-styling-theming-and-control-templates)
  - [`12-winforms-custom-controls-usercontrol-and-templatedcontrol.md`](winforms-to-avalonia/12-winforms-custom-controls-usercontrol-and-templatedcontrol)
  - [`13-winforms-high-dpi-scaling-and-flow-direction-rtl.md`](winforms-to-avalonia/13-winforms-high-dpi-scaling-and-flow-direction-rtl)
  - [`14-winforms-application-lifetime-window-management-and-services.md`](winforms-to-avalonia/14-winforms-application-lifetime-window-management-and-services)
  - [`15-winforms-resources-localization-settings-and-assets.md`](winforms-to-avalonia/15-winforms-resources-localization-settings-and-assets)
  - [`16-winforms-to-avalonia-migration-playbook.md`](winforms-to-avalonia/16-winforms-to-avalonia-migration-playbook)
  - [`17-winforms-to-avalonia-api-coverage-manifest-controls-layout-styling-platform.md`](winforms-to-avalonia/17-winforms-to-avalonia-api-coverage-manifest-controls-layout-styling-platform)
  - [`18-winforms-native-interop-and-webbrowser-replacement-strategies.md`](winforms-to-avalonia/18-winforms-native-interop-and-webbrowser-replacement-strategies)
  - [`19-winforms-testing-diagnostics-and-regression-safety.md`](winforms-to-avalonia/19-winforms-testing-diagnostics-and-regression-safety)
  - [`20-winforms-input-controls-text-masked-combo-autocomplete-numeric.md`](winforms-to-avalonia/20-winforms-input-controls-text-masked-combo-autocomplete-numeric)
  - [`21-winforms-date-time-and-calendar-controls.md`](winforms-to-avalonia/21-winforms-date-time-and-calendar-controls)
  - [`22-winforms-choice-controls-checkbox-radio-and-checked-lists.md`](winforms-to-avalonia/22-winforms-choice-controls-checkbox-radio-and-checked-lists)
  - [`23-winforms-tabcontrol-tabpage-and-document-workspaces.md`](winforms-to-avalonia/23-winforms-tabcontrol-tabpage-and-document-workspaces)
  - [`24-winforms-tooltip-helpprovider-and-context-guidance.md`](winforms-to-avalonia/24-winforms-tooltip-helpprovider-and-context-guidance)
  - [`25-winforms-progress-trackbar-and-status-feedback-patterns.md`](winforms-to-avalonia/25-winforms-progress-trackbar-and-status-feedback-patterns)
  - [`26-winforms-picturebox-imagelist-and-icon-asset-migration.md`](winforms-to-avalonia/26-winforms-picturebox-imagelist-and-icon-asset-migration)
  - [`27-winforms-propertygrid-and-inspector-editor-patterns.md`](winforms-to-avalonia/27-winforms-propertygrid-and-inspector-editor-patterns)
  - [`28-winforms-dragdrop-clipboard-and-data-transfer.md`](winforms-to-avalonia/28-winforms-dragdrop-clipboard-and-data-transfer)
  - [`29-winforms-printing-printpreview-and-export-workflows.md`](winforms-to-avalonia/29-winforms-printing-printpreview-and-export-workflows)
  - [`30-winforms-notifications-balloon-tip-and-toast-patterns.md`](winforms-to-avalonia/30-winforms-notifications-balloon-tip-and-toast-patterns)
  - [`31-winforms-splitter-scrollablecontrol-autoscroll-and-resizable-regions.md`](winforms-to-avalonia/31-winforms-splitter-scrollablecontrol-autoscroll-and-resizable-regions)
  - [`32-winforms-listview-details-groups-and-large-data-sets.md`](winforms-to-avalonia/32-winforms-listview-details-groups-and-large-data-sets)
  - [`33-winforms-treeview-lazy-loading-selection-and-check-state.md`](winforms-to-avalonia/33-winforms-treeview-lazy-loading-selection-and-check-state)
  - [`34-winforms-richtextbox-linklabel-and-rich-content-patterns.md`](winforms-to-avalonia/34-winforms-richtextbox-linklabel-and-rich-content-patterns)
  - [`35-winforms-toolstrip-dropdown-and-split-button-patterns.md`](winforms-to-avalonia/35-winforms-toolstrip-dropdown-and-split-button-patterns)
  - [`36-winforms-acceptbutton-cancelbutton-and-keyboard-processing.md`](winforms-to-avalonia/36-winforms-acceptbutton-cancelbutton-and-keyboard-processing)
  - [`37-winforms-layout-system-engine-invalidations-and-migration.md`](winforms-to-avalonia/37-winforms-layout-system-engine-invalidations-and-migration)
  - [`38-winforms-rendering-paint-pipeline-double-buffering-and-migration.md`](winforms-to-avalonia/38-winforms-rendering-paint-pipeline-double-buffering-and-migration)

## Full API Coverage Pointers

For exhaustive lookup (not only migration samples):

- controls: [`52-controls-reference-catalog.md`](52-controls-reference-catalog) and [`controls/README.md`](controls/README)
- layout and measure/arrange internals: [`30-layout-measure-arrange-and-custom-layout-controls.md`](30-layout-measure-arrange-and-custom-layout-controls), [`21-custom-layout-authoring.md`](21-custom-layout-authoring)
- styling/themes/resources: [`04-styles-themes-resources.md`](04-styles-themes-resources), [`10-templated-controls-and-control-themes.md`](10-templated-controls-and-control-themes), [`17-resources-assets-theme-variants-and-xmlns.md`](17-resources-assets-theme-variants-and-xmlns)
- data/validation/accessibility: [`22-validation-pipeline-and-data-errors.md`](22-validation-pipeline-and-data-errors), [`23-accessibility-and-automation.md`](23-accessibility-and-automation)
- platform services: [`29-storage-provider-and-file-pickers.md`](29-storage-provider-and-file-pickers), [`31-clipboard-and-data-transfer.md`](31-clipboard-and-data-transfer), [`34-dragdrop-workflows.md`](34-dragdrop-workflows), [`53-menu-controls-contextmenu-and-menuflyout-patterns.md`](53-menu-controls-contextmenu-and-menuflyout-patterns), [`55-tray-icons-and-system-tray-integration.md`](55-tray-icons-and-system-tray-integration)
- signatures: [`api-index-generated.md`](api-index-generated)

## First Conversion Example

WinForms C#:

```csharp
var panel = new Panel { Dock = DockStyle.Fill };
var button = new Button { Text = "Save", Anchor = AnchorStyles.Top | AnchorStyles.Right };
button.Click += (_, _) => Save();
panel.Controls.Add(button);
Controls.Add(panel);
```

Avalonia XAML:

```xaml
<UserControl xmlns="https://github.com/avaloniaui"
             xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
             xmlns:vm="using:MyApp.ViewModels"
             x:DataType="vm:MainViewModel">
  <Grid ColumnDefinitions="*,Auto" RowDefinitions="Auto,*">
    <Button Grid.Column="1"
            Margin="8"
            HorizontalAlignment="Right"
            Command="{CompiledBinding SaveCommand}"
            Content="Save" />
  </Grid>
</UserControl>
```

Avalonia C#:

```csharp
using Avalonia;
using Avalonia.Controls;

var grid = new Grid
{
    ColumnDefinitions = ColumnDefinitions.Parse("*,Auto"),
    RowDefinitions = RowDefinitions.Parse("Auto,*")
};

var saveButton = new Button
{
    Content = "Save",
    Margin = new Thickness(8),
    HorizontalAlignment = Avalonia.Layout.HorizontalAlignment.Right,
    Command = viewModel.SaveCommand
};
Grid.SetColumn(saveButton, 1);
grid.Children.Add(saveButton);
```

## AOT/Trimming and Threading Notes

- prefer compiled bindings (`{CompiledBinding ...}` + `x:DataType`) in migrated views.
- keep reflection-heavy dynamic binding patterns from WinForms out of hot paths.
- marshal UI updates to `Dispatcher.UIThread` when migrating code that used `Control.Invoke`.

## Troubleshooting

1. Converted views feel over-coupled to code-behind.
- move WinForms event handlers to commands and viewmodel state.

2. Layout parity is off after replacing `Dock` and `Anchor`.
- use explicit `Grid` rows/columns and alignment instead of absolute offsets.

3. Modal flows regress.
- use `Window.ShowDialog(owner)` and async command pipelines instead of blocking loops.
