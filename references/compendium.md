# Avalonia App Development Compendium

Use this as the entry page for the full skill reference set.

## Table of Contents

1. API map: `00-api-map.md`
2. Architecture and lifetimes: `01-architecture-and-lifetimes.md`
3. Bindings, XAML, AOT: `02-bindings-xaml-aot.md`
4. Reactive + threading: `03-reactive-threading.md`
5. Styles/themes/resources: `04-styles-themes-resources.md`
6. Platform bootstrap: `05-platforms-and-bootstrap.md`
7. MSBuild and AOT tooling: `06-msbuild-aot-and-tooling.md`
8. Troubleshooting: `07-troubleshooting.md`
9. Performance checklist: `08-performance-checklist.md`
10. End-to-end examples: `09-end-to-end-examples.md`
11. Templated controls + control themes: `10-templated-controls-and-control-themes.md`
12. View locator + tree patterns: `11-user-views-locator-and-tree-patterns.md`
13. Animations, transitions, frame loops: `12-animations-transitions-and-frame-loops.md`
14. Windowing + custom decorations: `13-windowing-and-custom-decorations.md`
15. Custom drawing, text, shapes, Skia: `14-custom-drawing-text-shapes-and-skia.md`
16. Compositor + compositor animations: `15-compositor-and-custom-visuals.md`
17. Property system + attached behaviors + style/media queries: `16-property-system-attached-properties-behaviors-and-style-properties.md`
18. Resources, assets, theme variants, xmlns: `17-resources-assets-theme-variants-and-xmlns.md`
19. Input system + routed events: `18-input-system-and-routed-events.md`
20. Focus + keyboard navigation: `19-focus-and-keyboard-navigation.md`
21. ItemsControl virtualization + recycling: `20-itemscontrol-virtualization-and-recycling.md`
22. Custom layout authoring: `21-custom-layout-authoring.md`
23. Validation pipeline + data errors: `22-validation-pipeline-and-data-errors.md`
24. Accessibility + automation: `23-accessibility-and-automation.md`
25. Commands + hotkeys + gestures: `24-commands-hotkeys-and-gestures.md`
26. Popups/flyouts/tooltips + overlays: `25-popups-flyouts-tooltips-and-overlays.md`
27. Testing stack (headless/render/UI): `26-testing-stack-headless-render-and-ui-tests.md`
28. Diagnostics/profiling + devtools: `27-diagnostics-profiling-and-devtools.md`
29. Custom themes (XAML + code-only): `28-custom-themes-xaml-and-code-only.md`
30. Storage provider + file pickers: `29-storage-provider-and-file-pickers.md`
31. Layout measure/arrange + custom controls/panels: `30-layout-measure-arrange-and-custom-layout-controls.md`
32. Clipboard + data transfer: `31-clipboard-and-data-transfer.md`
33. Launcher + external open: `32-launcher-and-external-open.md`
34. Screens + display awareness: `33-screens-and-display-awareness.md`
35. DragDrop workflows: `34-dragdrop-workflows.md`
36. Path icons + vector geometry assets: `35-path-icons-and-vector-geometry-assets.md`
37. Adorners, focus visuals, overlay layers: `36-adorners-focus-and-overlay-layers.md`
38. Shapes, geometry, hit testing: `37-shapes-geometry-and-hit-testing.md`
39. Data templates + IDataTemplate selector patterns: `38-data-templates-and-idatatemplate-selector-patterns.md`
40. Visual tree inspection + traversal: `39-visual-tree-inspection-and-traversal.md`
41. Logical tree inspection + traversal: `40-logical-tree-inspection-and-traversal.md`
42. XAML compiler and build pipeline: `41-xaml-compiler-and-build-pipeline.md`
43. Runtime XAML loader and dynamic loading: `42-runtime-xaml-loader-and-dynamic-loading.md`
44. XAML in libraries and resource packaging: `43-xaml-in-libraries-and-resource-packaging.md`
45. Runtime XAML manipulation and service-provider patterns: `44-runtime-xaml-manipulation-and-service-provider-patterns.md`
46. Generated API index: `api-index-generated.md`

## Fast Navigation by Task

- Startup/lifetime wiring:
  - `01-architecture-and-lifetimes.md`
  - `05-platforms-and-bootstrap.md`
  - `29-storage-provider-and-file-pickers.md`

- Platform services and external integration:
  - `29-storage-provider-and-file-pickers.md`
  - `31-clipboard-and-data-transfer.md`
  - `32-launcher-and-external-open.md`
  - `33-screens-and-display-awareness.md`
  - `34-dragdrop-workflows.md`

- XAML compiler, runtime loader, and manipulation:
  - `41-xaml-compiler-and-build-pipeline.md`
  - `42-runtime-xaml-loader-and-dynamic-loading.md`
  - `43-xaml-in-libraries-and-resource-packaging.md`
  - `44-runtime-xaml-manipulation-and-service-provider-patterns.md`

- Binding correctness and AOT safety:
  - `02-bindings-xaml-aot.md`
  - `06-msbuild-aot-and-tooling.md`
  - `41-xaml-compiler-and-build-pipeline.md`
  - `42-runtime-xaml-loader-and-dynamic-loading.md`
  - `44-runtime-xaml-manipulation-and-service-provider-patterns.md`
  - `38-data-templates-and-idatatemplate-selector-patterns.md`

- Reactive UI correctness:
  - `03-reactive-threading.md`

- Theme/style consistency:
  - `04-styles-themes-resources.md`
  - `10-templated-controls-and-control-themes.md`
  - `16-property-system-attached-properties-behaviors-and-style-properties.md`
  - `17-resources-assets-theme-variants-and-xmlns.md`
  - `43-xaml-in-libraries-and-resource-packaging.md`
  - `28-custom-themes-xaml-and-code-only.md`

- View composition and lookup patterns:
  - `11-user-views-locator-and-tree-patterns.md`
  - `38-data-templates-and-idatatemplate-selector-patterns.md`
  - `39-visual-tree-inspection-and-traversal.md`
  - `40-logical-tree-inspection-and-traversal.md`

- Input, focus, and interaction routing:
  - `18-input-system-and-routed-events.md`
  - `19-focus-and-keyboard-navigation.md`
  - `24-commands-hotkeys-and-gestures.md`
  - `34-dragdrop-workflows.md`
  - `36-adorners-focus-and-overlay-layers.md`
  - `39-visual-tree-inspection-and-traversal.md`

- Large-data item controls:
  - `30-layout-measure-arrange-and-custom-layout-controls.md`
  - `20-itemscontrol-virtualization-and-recycling.md`
  - `21-custom-layout-authoring.md`
  - `38-data-templates-and-idatatemplate-selector-patterns.md`

- Validation and accessibility:
  - `22-validation-pipeline-and-data-errors.md`
  - `23-accessibility-and-automation.md`

- Animation and rendering loops:
  - `12-animations-transitions-and-frame-loops.md`
  - `15-compositor-and-custom-visuals.md`

- Windowing and custom chrome:
  - `13-windowing-and-custom-decorations.md`
  - `25-popups-flyouts-tooltips-and-overlays.md`

- Drawing and graphics:
  - `14-custom-drawing-text-shapes-and-skia.md`
  - `35-path-icons-and-vector-geometry-assets.md`
  - `37-shapes-geometry-and-hit-testing.md`

- Testing and diagnostics:
  - `26-testing-stack-headless-render-and-ui-tests.md`
  - `27-diagnostics-profiling-and-devtools.md`

- Production hardening:
  - `07-troubleshooting.md`
  - `08-performance-checklist.md`

- API lookup by file/signature:
  - `api-index-generated.md`
