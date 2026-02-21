# XAML and C# Cross-Platform Development Skill (for Avalonia)

Comprehensive Codex skill for building, reviewing, migrating, and optimizing Avalonia applications with modern XAML/C# patterns, compiled bindings, and AOT-friendly architecture.

## License

This repository is licensed under the MIT License. See `LICENSE` for the full terms.

## Skill Identity

- Skill name: `xaml-csharp-development-skill-for-avalonia`
- Primary definition: [`SKILL.md`](SKILL)
- Main reference index: [`references/compendium.md`](references/compendium)
- Avalonia upstream repository: [AvaloniaUI/Avalonia](https://github.com/AvaloniaUI/Avalonia)

## Avalonia Version Coverage

This skill is currently pinned to Avalonia **11.3.12**.

- API references and guidance are aligned to `11.3.12` behavior.
- Generated API indexing is expected to use `--git-ref 11.3.12`.
- Guidance should avoid relying on `master`-only APIs unless a document explicitly states that exception.

As of **February 15, 2026**, this repository is maintained against the 11.3.12 release line.

## Scope

This skill covers app-development-facing Avalonia topics, including:

- App startup and lifetime wiring (desktop, single-view, activity hooks)
- XAML compilation and runtime loading patterns
- Compiled bindings, typed templates, and data/template composition
- Styling, theming, resources, and asset packaging
- Controls, templates, input/focus, layout, rendering, and animation
- Platform services (storage provider, clipboard, launcher, drag/drop, screens)
- Diagnostics, performance, testing, accessibility, and troubleshooting

It includes both curated guidance and a generated API index for signature lookup.

## Out of Scope

This skill is not intended to be:

- A full Avalonia internals/source-contributor guide
- A replacement for upstream API docs or source browsing
- A mandate to use unstable/private APIs in production code

When internals are mentioned, it is usually for diagnostics, constraints, or behavioral explanation.

## Repository Structure

- [`SKILL.md`](SKILL)
  - Skill entrypoint and execution rules
- `references/`
  - Numbered, topic-focused reference documents
- [`references/compendium.md`](references/compendium)
  - Top-level table of contents and task-oriented navigation
- [`references/api-index-generated.md`](references/api-index-generated)
  - Broad generated API signature index
- `scripts/generate_api_index.py`
  - API index generator script
- `assets/`
  - Supporting skill assets/templates
- `agents/`
  - Agent-specific instructions/context files

## How to Use the Skill

1. Start from [`SKILL.md`](SKILL).
2. Follow the workflow sections to load only the references needed for the current task.
3. Use [`references/compendium.md`](references/compendium) for fast navigation.
4. Use [`references/api-index-generated.md`](references/api-index-generated) when exact public signatures are required.

## XAML and API Coverage Notes

Recent additions include focused references for:

- XAML compiler/build pipeline
- Runtime XAML loader and dynamic loading
- XAML in libraries and resource packaging
- Runtime XAML manipulation and service-provider patterns
- Visual tree and logical tree inspection/traversal
- Data templates and `IDataTemplate` selector patterns
- Value converters
- Binding value/notification and instanced binding semantics
- Dispatcher priority, operations, and timers
- TopLevel, window, and runtime services
- Adaptive markup and dynamic resource patterns
- Relative/static resource and name resolution markup
- Template content and func template patterns
- Path icons, adorners, and shapes
- Menu controls, context menu, and menu flyout patterns
- Native menu and native menubar integration
- Tray icons and system tray integration
- Managed notifications and `WindowNotificationManager`
- `ScrollViewer` offset, anchoring, and snap points
- `TextBox` editing, clipboard, undo/redo, and text input options
- Media `Colors`, `Brushes`, and `FormattedText` usage
- `AutomationProperties` and attached behavior patterns
- Advanced rendering/interop boundaries (OpenGL, Vulkan, Linux framebuffer)
- Per-control references for the full Avalonia control surface (`references/controls/`)
- HTML/CSS-to-Avalonia migration lane (`references/62-html-css-to-avalonia-modern-ui-conversion-index.md`) with detailed topics in `references/html-to-avalonia/`:
  - layout/box-model/flex/grid responsive mapping,
  - selectors/cascade/tokens/theming translation,
  - transition/keyframe/easing motion mapping,
  - forms/semantic shell/overlay/rich-component migration recipes,
  - typography, truncation, gradient/shadow/glass, transform/micro-interaction recipes,
  - fluid sizing (`calc`/`clamp`), media/object-fit/aspect-ratio mappings,
  - sticky/scroll-linked patterns and pseudo-element/decorative-layer equivalents,
  - `grid-template-areas` conversion patterns and responsive area remapping,
  - logical properties (`margin-inline`/`padding-block`/`inset-inline`) flow-aware mappings,
  - RTL/BiDi direction handling (`dir`/`direction`) with `FlowDirection` patterns,
  - command-surface migration (`Button`/`ToggleButton`/`SplitButton`/`DropDownButton`/`MenuFlyout`),
  - disclosure and hierarchy migration (`details`/accordion/tree semantics to `Expander`/`TreeView`),
  - range/progress/meter/scroll feedback mapping (`ProgressBar`/`Slider`/`ScrollBar`),
  - advanced input migration (`AutoCompleteBox`, date/time pickers, `MaskedTextBox`, `NumericUpDown`),
  - color input and spectrum mapping (`ColorPicker`/`ColorView`),
  - tabs/off-canvas/carousel shell mapping (`TabControl`/`SplitView`/`Carousel`),
  - menu and context-menu command mapping (`Menu`/`MenuItem`/`ContextMenu`),
  - custom elements/web-components mapping to custom and templated controls,
  - Shadow DOM slot/part mapping to `ContentPresenter`, template parts, and control themes,
  - `data-*` metadata/custom DOM events mapping to attached properties and routed events,
  - CSS architecture mapping (`@layer`, `@scope`, `:has`, `@container`) to Avalonia style architecture,
  - select/listbox/combobox mapping using `SelectingItemsControl`, `ComboBox`, and `ListBox` APIs,
  - switch/checkbox/radio/tri-state mapping using `ToggleSwitch`, `CheckBox`, `RadioButton`, and `ToggleButton`,
  - resizable split pane and drag handle mapping using `GridSplitter` and `Thumb`,
  - pull-to-refresh and live feed reload mapping using `RefreshContainer` and `RefreshVisualizer`,
  - headless tablist and segmented navigation mapping using `TabStrip` + content host patterns,
  - navigation/routing, modal/drawer/toast systems, data table/master-detail patterns,
  - accessibility semantics, focus UX, and reduced-motion mapping,
  - API-coverage manifest linking to full controls + layout/styling/animation lookup.
- WinForms-to-Avalonia migration lane (`references/63-winforms-to-avalonia-modern-ui-conversion-index.md`) with detailed topics in `references/winforms-to-avalonia/`:
  - lifecycle/layout/docking migration (`Control`, `Form`, `Dock`/`Anchor`, panel recipes),
  - `BindingSource`/validation/data-control migration (`DataGridView`, `ListView`, `TreeView`, `ErrorProvider`),
  - command/input/menu/dialog/tray/platform-service migration (`MenuStrip`, `ContextMenuStrip`, dialogs, `NotifyIcon`),
  - owner-draw/custom-control/theming migration (`OnPaint` to `Render`, `UserControl`, `TemplatedControl`),
  - deep layout-system migration (`LayoutEngine`, `PerformLayout`, `SuspendLayout`/`ResumeLayout`) to Avalonia `Measure`/`Arrange`/invalidation discipline,
  - deep rendering-system migration (`WM_PAINT`, owner-draw, `ControlStyles` buffering) to Avalonia `Render`, `AffectsRender`, and template-first rendering,
  - input/date/choice controls migration (`MaskedTextBox`, `AutoCompleteBox`, `NumericUpDown`, date/time pickers, `CheckBox`/`RadioButton` patterns),
  - tab workspace and context guidance migration (`TabControl`, tooltips/help, progress/track feedback),
  - image/icon asset migration (`PictureBox`, `ImageList`, window/tray icon pipelines),
  - advanced workflows migration (property-grid replacement, drag/drop, clipboard, printing/export, notifications),
  - splitter and scrollable-region migration (`Splitter`, `ScrollableControl.AutoScroll`, scrollbar visibility patterns),
  - advanced list/tree migration (`ListView` details/groups/virtual mode, `TreeView` lazy loading + check-state templates),
  - rich text and toolbar command-surface migration (`RichTextBox`/`LinkLabel`, `ToolStripSplitButton`/`ToolStripDropDownButton`),
  - dialog keyboard migration (`AcceptButton`, `CancelButton`, `KeyPreview`, `ProcessCmdKey` to `IsDefault`/`IsCancel` + `KeyBinding`),
  - DPI/RTL/lifetime/resources/test-hardening and migration playbook guidance,
  - API-coverage manifest linking WinForms source checkpoints to Avalonia lookup references.
- WPF-to-Avalonia migration lane (`references/64-wpf-to-avalonia-modern-ui-conversion-index.md`) with detailed topics in `references/wpf-to-avalonia/`:
  - dependency property and control-authoring migration (`DependencyProperty`, `CustomControl`, templates),
  - binding/resource/style/template migration (`Binding`, resources, selectors, trigger-state mapping),
  - layout/window/navigation/dialog and dispatcher async migration (`Frame/Page` alternatives, lifetime, UI-thread patterns),
  - deep layout-system migration (`LayoutManager`, measure/arrange invalidation queues, `UpdateLayout` boundaries),
  - advanced layout and sizing migration (`GridSplitter`, `UniformGrid`, `Grid.IsSharedSizeScope`, shared-size groups),
  - form/choice/date-shell control migration (`TextBox`/`PasswordBox`, `ComboBox`, `CheckBox`/`RadioButton`/toggles, date/time/calendar controls),
  - selection and hierarchical control migration (`ListBox`/`ListView` selection models, `TreeView` + `TreeDataTemplate` patterns),
  - workspace/context UX migration (`TabControl`, `Expander`, `GroupBox`, tooltips/help launchers, progress/range feedback controls),
  - popup/command/focus/scroll migration (`Popup`/`Flyout`, `CommandManager` replacement, access keys/tab navigation, `ScrollViewer` control),
  - asset and transfer workflow migration (`Image`/`BitmapImage` pipelines, drag/drop and clipboard `DataTransfer` patterns),
  - document and message flows migration (printing/export preview, `MessageBox` alternatives, notifications, rich reading surfaces),
  - rendering/animation/interop migration (`OnRender`, adorners, storyboards to transitions, `HwndHost` alternatives),
  - deep rendering-system migration (`Visual`, `DrawingVisual`, `CompositionTarget.Rendering`) to Avalonia `Render`/compositor patterns,
  - accessibility/RTL/localization/testing/perf hardening and migration playbook guidance,
  - API-coverage manifest linking WPF source checkpoints to Avalonia lookup references.
- WinUI-to-Avalonia migration lane (`references/65-winui-to-avalonia-modern-ui-conversion-index.md`) with detailed topics in `references/winui-to-avalonia/`:
  - dependency property/object-system migration (`DependencyObject`, `DependencyProperty`) to Avalonia property patterns,
  - WinUI layout-system migration (measure/arrange invalidation model, panel mapping, `UpdateLayout` boundaries),
  - WinUI rendering/composition migration (`CompositionTarget.Rendering`, compositor patterns) to Avalonia render/compositor paths,
  - navigation/shell/dialog migration (`NavigationView`, `Frame/Page`, `ContentDialog`, `AppWindow`) to Avalonia shell/dialog patterns,
  - WinUI control-family migration (`TabView`, `TreeView`, `ItemsRepeater`, `InfoBar`, `TeachingTip`, `SplitButton`) to Avalonia control equivalents,
  - resources/theming/state migration (`ThemeResource`, `VisualStateManager`, adaptive triggers) to Avalonia resources/selectors/transitions,
  - input/command/keyboard migration (`KeyboardAccelerator`, routed input, command surfaces) to `KeyBinding` + `ICommand` flows,
  - platform integration migration (drag/drop, clipboard, interop, WebView boundary patterns),
  - advanced shell/control migration (NavigationView pane modes, ItemsRepeater/virtualization, ListView/GridView selection semantics),
  - command/guidance surface migration (CommandBarFlyout, InfoBar, TeachingTip, ContentDialog workflow patterns),
  - advanced platform/render-host migration (`XamlRoot`/`AppWindow` coordination, composition visual layer, SwapChain/Win2D hosting boundaries),
  - platform services and lifecycle migration (file pickers, launcher, activation contracts, menu/tray integration, in-app notification flows),
  - advanced control migration (`RefreshContainer`, `SwipeControl`, `TwoPaneView`, `SelectorBar`, `BreadcrumbBar`, `Pager`, `PipsPager`),
  - integration and dynamic-UI migration (titlebar/system backdrop, runtime XAML loading/resource packaging, WebView2 boundaries, `ItemsView`/`LayoutPanel` strategies),
  - low-level framework migration (property type/metadata/precedence mapping, visual/logical tree traversal, NameScope/template-part contracts, selector/resource/theme resolution internals),
  - API-coverage manifest linking WinUI source checkpoints and online API docs to Avalonia lookup references.

These are designed to reduce accidental drift to unreleased APIs.

## Regenerating API Index (Pinned)

```bash
python3 scripts/generate_api_index.py \
  --repo <path-to-avalonia-repo> \
  --git-ref 11.3.12 \
  --output references/api-index-generated.md
```

Recommended checks after regeneration:

- Verify key startup/binding/platform signatures still match references.
- Audit docs for master-only APIs introduced by mistake.
- Update this README and [`SKILL.md`](SKILL) if version coverage changes.

## Maintenance Checklist for New Avalonia Release

1. Switch target release tag (for example `11.3.x` -> `11.4.x`).
2. Regenerate [`references/api-index-generated.md`](references/api-index-generated) from the new tag.
3. Diff critical APIs referenced by docs.
4. Update affected reference files.
5. Update:
   - [`README.md`](README)
   - [`SKILL.md`](SKILL)
   - [`references/compendium.md`](references/compendium)

## Quality Bar

Skill guidance should remain:

- Version-accurate to the declared release
- Explicit about tradeoffs (trim/AOT/runtime dynamic paths)
- Focused on production-safe defaults (compiled XAML + compiled bindings)
- Structured for rapid task execution and review
