# XAML and C# Cross-Platform Development (for Avalonia) Compendium

Use this as the entry page for the full skill reference set.

## Table of Contents

00. API map: [`00-api-map.md`](00-api-map)
01. Architecture and lifetimes: [`01-architecture-and-lifetimes.md`](01-architecture-and-lifetimes)
02. Bindings, XAML, AOT: [`02-bindings-xaml-aot.md`](02-bindings-xaml-aot)
03. Reactive + threading: [`03-reactive-threading.md`](03-reactive-threading)
04. Styles/themes/resources: [`04-styles-themes-resources.md`](04-styles-themes-resources)
05. Platform bootstrap: [`05-platforms-and-bootstrap.md`](05-platforms-and-bootstrap)
06. MSBuild and AOT tooling: [`06-msbuild-aot-and-tooling.md`](06-msbuild-aot-and-tooling)
07. Troubleshooting: [`07-troubleshooting.md`](07-troubleshooting)
08. Performance checklist: [`08-performance-checklist.md`](08-performance-checklist)
09. End-to-end examples: [`09-end-to-end-examples.md`](09-end-to-end-examples)
10. Templated controls + control themes: [`10-templated-controls-and-control-themes.md`](10-templated-controls-and-control-themes)
11. View locator + tree patterns: [`11-user-views-locator-and-tree-patterns.md`](11-user-views-locator-and-tree-patterns)
12. Animations, transitions, frame loops: [`12-animations-transitions-and-frame-loops.md`](12-animations-transitions-and-frame-loops)
13. Windowing + custom decorations: [`13-windowing-and-custom-decorations.md`](13-windowing-and-custom-decorations)
14. Custom drawing, text, shapes, Skia: [`14-custom-drawing-text-shapes-and-skia.md`](14-custom-drawing-text-shapes-and-skia)
15. Compositor + compositor animations: [`15-compositor-and-custom-visuals.md`](15-compositor-and-custom-visuals)
16. Property system + attached behaviors + style/media queries: [`16-property-system-attached-properties-behaviors-and-style-properties.md`](16-property-system-attached-properties-behaviors-and-style-properties)
17. Resources, assets, theme variants, xmlns: [`17-resources-assets-theme-variants-and-xmlns.md`](17-resources-assets-theme-variants-and-xmlns)
18. Input system + routed events: [`18-input-system-and-routed-events.md`](18-input-system-and-routed-events)
19. Focus + keyboard navigation: [`19-focus-and-keyboard-navigation.md`](19-focus-and-keyboard-navigation)
20. ItemsControl virtualization + recycling: [`20-itemscontrol-virtualization-and-recycling.md`](20-itemscontrol-virtualization-and-recycling)
21. Custom layout authoring: [`21-custom-layout-authoring.md`](21-custom-layout-authoring)
22. Validation pipeline + data errors: [`22-validation-pipeline-and-data-errors.md`](22-validation-pipeline-and-data-errors)
23. Accessibility + automation: [`23-accessibility-and-automation.md`](23-accessibility-and-automation)
24. Commands + hotkeys + gestures: [`24-commands-hotkeys-and-gestures.md`](24-commands-hotkeys-and-gestures)
25. Popups/flyouts/tooltips + overlays: [`25-popups-flyouts-tooltips-and-overlays.md`](25-popups-flyouts-tooltips-and-overlays)
26. Testing stack (headless/render/UI): [`26-testing-stack-headless-render-and-ui-tests.md`](26-testing-stack-headless-render-and-ui-tests)
27. Diagnostics/profiling + devtools: [`27-diagnostics-profiling-and-devtools.md`](27-diagnostics-profiling-and-devtools)
28. Custom themes (XAML + code-only): [`28-custom-themes-xaml-and-code-only.md`](28-custom-themes-xaml-and-code-only)
29. Storage provider + file pickers: [`29-storage-provider-and-file-pickers.md`](29-storage-provider-and-file-pickers)
30. Layout measure/arrange + custom controls/panels: [`30-layout-measure-arrange-and-custom-layout-controls.md`](30-layout-measure-arrange-and-custom-layout-controls)
31. Clipboard + data transfer: [`31-clipboard-and-data-transfer.md`](31-clipboard-and-data-transfer)
32. Launcher + external open: [`32-launcher-and-external-open.md`](32-launcher-and-external-open)
33. Screens + display awareness: [`33-screens-and-display-awareness.md`](33-screens-and-display-awareness)
34. DragDrop workflows: [`34-dragdrop-workflows.md`](34-dragdrop-workflows)
35. Path icons + vector geometry assets: [`35-path-icons-and-vector-geometry-assets.md`](35-path-icons-and-vector-geometry-assets)
36. Adorners, focus visuals, overlay layers: [`36-adorners-focus-and-overlay-layers.md`](36-adorners-focus-and-overlay-layers)
37. Shapes, geometry, hit testing: [`37-shapes-geometry-and-hit-testing.md`](37-shapes-geometry-and-hit-testing)
38. Data templates + IDataTemplate selector patterns: [`38-data-templates-and-idatatemplate-selector-patterns.md`](38-data-templates-and-idatatemplate-selector-patterns)
39. Visual tree inspection + traversal: [`39-visual-tree-inspection-and-traversal.md`](39-visual-tree-inspection-and-traversal)
40. Logical tree inspection + traversal: [`40-logical-tree-inspection-and-traversal.md`](40-logical-tree-inspection-and-traversal)
41. XAML compiler and build pipeline: [`41-xaml-compiler-and-build-pipeline.md`](41-xaml-compiler-and-build-pipeline)
42. Runtime XAML loader and dynamic loading: [`42-runtime-xaml-loader-and-dynamic-loading.md`](42-runtime-xaml-loader-and-dynamic-loading)
43. XAML in libraries and resource packaging: [`43-xaml-in-libraries-and-resource-packaging.md`](43-xaml-in-libraries-and-resource-packaging)
44. Runtime XAML manipulation and service-provider patterns: [`44-runtime-xaml-manipulation-and-service-provider-patterns.md`](44-runtime-xaml-manipulation-and-service-provider-patterns)
45. Value converters: [`45-value-converters-single-multi-and-binding-wiring.md`](45-value-converters-single-multi-and-binding-wiring)
46. Binding value/notification and instanced binding semantics: [`46-binding-value-notification-and-instanced-binding-semantics.md`](46-binding-value-notification-and-instanced-binding-semantics)
47. Dispatcher priority, operations, and timers: [`47-dispatcher-priority-operations-and-timers.md`](47-dispatcher-priority-operations-and-timers)
48. TopLevel, window, and runtime services: [`48-toplevel-window-and-runtime-services.md`](48-toplevel-window-and-runtime-services)
49. Adaptive markup and dynamic resource patterns: [`49-adaptive-markup-and-dynamic-resource-patterns.md`](49-adaptive-markup-and-dynamic-resource-patterns)
50. Relative/static resource and name resolution markup: [`50-relative-static-resource-and-name-resolution-markup.md`](50-relative-static-resource-and-name-resolution-markup)
51. Template content and func template patterns: [`51-template-content-and-func-template-patterns.md`](51-template-content-and-func-template-patterns)
52. Controls reference catalog: [`52-controls-reference-catalog.md`](52-controls-reference-catalog)
API index: [`api-index-generated.md`](api-index-generated)

## Fast Navigation by Task

- Startup/lifetime wiring:
  - [`01-architecture-and-lifetimes.md`](01-architecture-and-lifetimes)
  - [`05-platforms-and-bootstrap.md`](05-platforms-and-bootstrap)
  - [`48-toplevel-window-and-runtime-services.md`](48-toplevel-window-and-runtime-services)
  - [`29-storage-provider-and-file-pickers.md`](29-storage-provider-and-file-pickers)

- Platform services and external integration:
  - [`48-toplevel-window-and-runtime-services.md`](48-toplevel-window-and-runtime-services)
  - [`29-storage-provider-and-file-pickers.md`](29-storage-provider-and-file-pickers)
  - [`31-clipboard-and-data-transfer.md`](31-clipboard-and-data-transfer)
  - [`32-launcher-and-external-open.md`](32-launcher-and-external-open)
  - [`33-screens-and-display-awareness.md`](33-screens-and-display-awareness)
  - [`34-dragdrop-workflows.md`](34-dragdrop-workflows)

- XAML compiler, runtime loader, and manipulation:
  - [`41-xaml-compiler-and-build-pipeline.md`](41-xaml-compiler-and-build-pipeline)
  - [`42-runtime-xaml-loader-and-dynamic-loading.md`](42-runtime-xaml-loader-and-dynamic-loading)
  - [`43-xaml-in-libraries-and-resource-packaging.md`](43-xaml-in-libraries-and-resource-packaging)
  - [`44-runtime-xaml-manipulation-and-service-provider-patterns.md`](44-runtime-xaml-manipulation-and-service-provider-patterns)
  - [`49-adaptive-markup-and-dynamic-resource-patterns.md`](49-adaptive-markup-and-dynamic-resource-patterns)
  - [`50-relative-static-resource-and-name-resolution-markup.md`](50-relative-static-resource-and-name-resolution-markup)

- Binding correctness and AOT safety:
  - [`02-bindings-xaml-aot.md`](02-bindings-xaml-aot)
  - [`45-value-converters-single-multi-and-binding-wiring.md`](45-value-converters-single-multi-and-binding-wiring)
  - [`46-binding-value-notification-and-instanced-binding-semantics.md`](46-binding-value-notification-and-instanced-binding-semantics)
  - [`50-relative-static-resource-and-name-resolution-markup.md`](50-relative-static-resource-and-name-resolution-markup)
  - [`06-msbuild-aot-and-tooling.md`](06-msbuild-aot-and-tooling)
  - [`41-xaml-compiler-and-build-pipeline.md`](41-xaml-compiler-and-build-pipeline)
  - [`42-runtime-xaml-loader-and-dynamic-loading.md`](42-runtime-xaml-loader-and-dynamic-loading)
  - [`44-runtime-xaml-manipulation-and-service-provider-patterns.md`](44-runtime-xaml-manipulation-and-service-provider-patterns)
  - [`38-data-templates-and-idatatemplate-selector-patterns.md`](38-data-templates-and-idatatemplate-selector-patterns)

- Reactive UI correctness:
  - [`03-reactive-threading.md`](03-reactive-threading)
  - [`47-dispatcher-priority-operations-and-timers.md`](47-dispatcher-priority-operations-and-timers)

- Theme/style consistency:
  - [`04-styles-themes-resources.md`](04-styles-themes-resources)
  - [`10-templated-controls-and-control-themes.md`](10-templated-controls-and-control-themes)
  - [`16-property-system-attached-properties-behaviors-and-style-properties.md`](16-property-system-attached-properties-behaviors-and-style-properties)
  - [`17-resources-assets-theme-variants-and-xmlns.md`](17-resources-assets-theme-variants-and-xmlns)
  - [`49-adaptive-markup-and-dynamic-resource-patterns.md`](49-adaptive-markup-and-dynamic-resource-patterns)
  - [`43-xaml-in-libraries-and-resource-packaging.md`](43-xaml-in-libraries-and-resource-packaging)
  - [`28-custom-themes-xaml-and-code-only.md`](28-custom-themes-xaml-and-code-only)

- View composition and lookup patterns:
  - [`11-user-views-locator-and-tree-patterns.md`](11-user-views-locator-and-tree-patterns)
  - [`38-data-templates-and-idatatemplate-selector-patterns.md`](38-data-templates-and-idatatemplate-selector-patterns)
  - [`51-template-content-and-func-template-patterns.md`](51-template-content-and-func-template-patterns)
  - [`39-visual-tree-inspection-and-traversal.md`](39-visual-tree-inspection-and-traversal)
  - [`40-logical-tree-inspection-and-traversal.md`](40-logical-tree-inspection-and-traversal)

- Input, focus, and interaction routing:
  - [`18-input-system-and-routed-events.md`](18-input-system-and-routed-events)
  - [`19-focus-and-keyboard-navigation.md`](19-focus-and-keyboard-navigation)
  - [`24-commands-hotkeys-and-gestures.md`](24-commands-hotkeys-and-gestures)
  - [`34-dragdrop-workflows.md`](34-dragdrop-workflows)
  - [`36-adorners-focus-and-overlay-layers.md`](36-adorners-focus-and-overlay-layers)
  - [`39-visual-tree-inspection-and-traversal.md`](39-visual-tree-inspection-and-traversal)

- Large-data item controls:
  - [`30-layout-measure-arrange-and-custom-layout-controls.md`](30-layout-measure-arrange-and-custom-layout-controls)
  - [`20-itemscontrol-virtualization-and-recycling.md`](20-itemscontrol-virtualization-and-recycling)
  - [`21-custom-layout-authoring.md`](21-custom-layout-authoring)
  - [`38-data-templates-and-idatatemplate-selector-patterns.md`](38-data-templates-and-idatatemplate-selector-patterns)
  - [`51-template-content-and-func-template-patterns.md`](51-template-content-and-func-template-patterns)

- Validation and accessibility:
  - [`22-validation-pipeline-and-data-errors.md`](22-validation-pipeline-and-data-errors)
  - [`23-accessibility-and-automation.md`](23-accessibility-and-automation)

- Animation and rendering loops:
  - [`12-animations-transitions-and-frame-loops.md`](12-animations-transitions-and-frame-loops)
  - [`15-compositor-and-custom-visuals.md`](15-compositor-and-custom-visuals)

- Windowing and custom chrome:
  - [`13-windowing-and-custom-decorations.md`](13-windowing-and-custom-decorations)
  - [`48-toplevel-window-and-runtime-services.md`](48-toplevel-window-and-runtime-services)
  - [`25-popups-flyouts-tooltips-and-overlays.md`](25-popups-flyouts-tooltips-and-overlays)
  - [`52-controls-reference-catalog.md`](52-controls-reference-catalog)

- Drawing and graphics:
  - [`14-custom-drawing-text-shapes-and-skia.md`](14-custom-drawing-text-shapes-and-skia)
  - [`35-path-icons-and-vector-geometry-assets.md`](35-path-icons-and-vector-geometry-assets)
  - [`37-shapes-geometry-and-hit-testing.md`](37-shapes-geometry-and-hit-testing)

- Testing and diagnostics:
  - [`26-testing-stack-headless-render-and-ui-tests.md`](26-testing-stack-headless-render-and-ui-tests)
  - [`27-diagnostics-profiling-and-devtools.md`](27-diagnostics-profiling-and-devtools)

- Production hardening:
  - [`07-troubleshooting.md`](07-troubleshooting)
  - [`08-performance-checklist.md`](08-performance-checklist)

- API lookup by file/signature:
  - [`api-index-generated.md`](api-index-generated)
