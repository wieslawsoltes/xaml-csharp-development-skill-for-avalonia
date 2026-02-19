---
name: xaml-csharp-development-skill-for-avalonia
description: Build, review, migrate, and optimize Avalonia applications with modern XAML/C# patterns, compiled bindings, and AOT-friendly architecture. Use for tasks involving Avalonia app startup and lifetime wiring, view/viewmodel composition, bindings in .axaml/.xaml and C#, styles/themes/resources, platform-specific bootstrapping (desktop/browser/mobile/headless), trimming/NativeAOT compatibility, reactive UI flows, performance tuning, and troubleshooting build/runtime issues in Avalonia projects.
---

# XAML and C# Cross-Platform Development (for Avalonia)

Use this skill to produce reflection-minimized, modern, fast Avalonia apps that stay maintainable across desktop, browser, and mobile targets.

Primary entry for the full reference set:
- `references/compendium.md`

## Workflow

1. Define app scope, API surface, and lifetime model.
- Read `references/00-api-map.md`.
- Read `references/01-architecture-and-lifetimes.md`.
- Choose the root lifetime first (`IClassicDesktopStyleApplicationLifetime` or `ISingleViewApplicationLifetime`) and use `IActivatableLifetime` as an optional feature hook when needed.

2. Lock platform bootstrap and build pipeline before UI work.
- Read `references/05-platforms-and-bootstrap.md`.
- Read `references/29-storage-provider-and-file-pickers.md`.
- Read `references/31-clipboard-and-data-transfer.md`.
- Read `references/32-launcher-and-external-open.md`.
- Read `references/33-screens-and-display-awareness.md`.
- Read `references/06-msbuild-aot-and-tooling.md`.
- Read `references/41-xaml-compiler-and-build-pipeline.md`.
- Set platform options and confirm XAML/compiled-binding configuration for AOT.

3. Establish binding, XAML, reactive, and command architecture.
- Read `references/02-bindings-xaml-aot.md`.
- Read `references/45-value-converters-single-multi-and-binding-wiring.md`.
- Read `references/46-binding-value-notification-and-instanced-binding-semantics.md`.
- Read `references/49-adaptive-markup-and-dynamic-resource-patterns.md`.
- Read `references/50-relative-static-resource-and-name-resolution-markup.md`.
- Read `references/42-runtime-xaml-loader-and-dynamic-loading.md`.
- Read `references/44-runtime-xaml-manipulation-and-service-provider-patterns.md`.
- Read `references/03-reactive-threading.md`.
- Read `references/47-dispatcher-priority-operations-and-timers.md`.
- Read `references/24-commands-hotkeys-and-gestures.md`.
- Default to compiled bindings with `x:DataType`; keep UI-thread mutations explicit.

4. Build view composition, locator strategy, and interaction routing.
- Read `references/11-user-views-locator-and-tree-patterns.md`.
- Read `references/38-data-templates-and-idatatemplate-selector-patterns.md`.
- Read `references/51-template-content-and-func-template-patterns.md`.
- Read `references/39-visual-tree-inspection-and-traversal.md`.
- Read `references/40-logical-tree-inspection-and-traversal.md`.
- Read `references/18-input-system-and-routed-events.md`.
- Read `references/19-focus-and-keyboard-navigation.md`.
- Read `references/57-scrollviewer-offset-anchoring-and-snap-points.md`.
- Read `references/58-textbox-editing-clipboard-undo-and-input-options.md`.
- Read `references/34-dragdrop-workflows.md`.
- Keep routed-input handling thin and deterministic; prefer command/state dispatch.

5. Author properties, styles, themes, resources, and assets as one system.
- Read `references/16-property-system-attached-properties-behaviors-and-style-properties.md`.
- Read `references/04-styles-themes-resources.md`.
- Read `references/17-resources-assets-theme-variants-and-xmlns.md`.
- Read `references/43-xaml-in-libraries-and-resource-packaging.md`.
- Read `references/35-path-icons-and-vector-geometry-assets.md`.
- Read `references/28-custom-themes-xaml-and-code-only.md`.
- Keep property metadata, style selectors, media rules, and resource lookup predictable.

6. Implement controls and window surfaces.
- Read `references/10-templated-controls-and-control-themes.md`.
- Read `references/36-adorners-focus-and-overlay-layers.md`.
- Read `references/13-windowing-and-custom-decorations.md`.
- Read `references/48-toplevel-window-and-runtime-services.md`.
- Read `references/53-menu-controls-contextmenu-and-menuflyout-patterns.md`.
- Read `references/54-native-menu-and-native-menubar-integration.md`.
- Read `references/55-tray-icons-and-system-tray-integration.md`.
- Read `references/56-managed-notifications-and-window-notification-manager.md`.
- Read `references/52-controls-reference-catalog.md` for per-control API quick lookup.
- Read `references/25-popups-flyouts-tooltips-and-overlays.md`.
- Separate control contract, template parts, and platform-specific window/popup behavior.

7. Implement layout and large-data item presentation.
- Read `references/30-layout-measure-arrange-and-custom-layout-controls.md`.
- Read `references/21-custom-layout-authoring.md`.
- Read `references/20-itemscontrol-virtualization-and-recycling.md`.
- Read `references/57-scrollviewer-offset-anchoring-and-snap-points.md`.
- Use invalidation discipline (`InvalidateMeasure`/`InvalidateArrange`) and recycling-aware templates.

8. Add motion, compositor effects, and custom rendering only where needed.
- Read `references/12-animations-transitions-and-frame-loops.md`.
- Read `references/15-compositor-and-custom-visuals.md`.
- Read `references/14-custom-drawing-text-shapes-and-skia.md`.
- Read `references/37-shapes-geometry-and-hit-testing.md`.
- Read `references/59-media-colors-brushes-and-formatted-text-practical-usage.md`.
- Read `references/61-rendering-and-interop-boundaries-opengl-vulkan-framebuffer.md` for advanced interop only.
- Prefer built-in transitions/animations first; use custom draw/compositor paths for hotspots.

9. Complete validation, accessibility, and automation semantics.
- Read `references/22-validation-pipeline-and-data-errors.md`.
- Read `references/23-accessibility-and-automation.md`.
- Read `references/60-automation-properties-and-attached-behavior-patterns.md`.
- Ensure data errors, labels, focus order, and automation metadata are stable and testable.

10. Verify quality with tests, diagnostics, and performance passes.
- Read `references/26-testing-stack-headless-render-and-ui-tests.md`.
- Read `references/27-diagnostics-profiling-and-devtools.md`.
- Read `references/08-performance-checklist.md`.
- Read `references/07-troubleshooting.md`.

11. Finalize with integrated examples and API lookup.
- Read `references/09-end-to-end-examples.md`.
- Use `references/api-index-generated.md` for signature-level API lookup and drift checks.

12. For web-to-desktop migration work, map HTML/CSS idioms explicitly.
- Read `references/62-html-css-to-avalonia-modern-ui-conversion-index.md`.
- Use detailed topic docs under `references/html-to-avalonia/` (index at `references/html-to-avalonia/README.md`, currently `00`-`39`).

13. For Windows desktop migration work, map WinForms idioms explicitly.
- Read `references/63-winforms-to-avalonia-modern-ui-conversion-index.md`.
- Use detailed topic docs under `references/winforms-to-avalonia/` (index at `references/winforms-to-avalonia/README.md`, currently `00`-`38`).

14. For XAML desktop migration work, map WPF idioms explicitly.
- Read `references/64-wpf-to-avalonia-modern-ui-conversion-index.md`.
- Use detailed topic docs under `references/wpf-to-avalonia/` (index at `references/wpf-to-avalonia/README.md`, currently `00`-`45`).

15. For Windows App SDK / WinUI migration work, map WinUI idioms explicitly.
- Read `references/65-winui-to-avalonia-modern-ui-conversion-index.md`.
- Use detailed topic docs under `references/winui-to-avalonia/` (index at `references/winui-to-avalonia/README.md`, currently `00`-`66`).

## Public API Coverage

Use curated app-building API guidance first:
- `references/00-api-map.md`

For a generated, broad signature index of app-building surface:
- `references/api-index-generated.md`

Regenerate index after repo upgrades or if API drift is suspected:

```bash
python3 scripts/generate_api_index.py \
  --repo <path-to-avalonia-repo> \
  --git-ref 11.3.12 \
  --output references/api-index-generated.md
```

Search patterns for the large generated index:
- `rg -n "AppBuilder|ApplicationLifetime|StartWithClassicDesktopLifetime" references/api-index-generated.md`
- `rg -n "CompiledBinding|ReflectionBinding|AvaloniaXamlLoader" references/api-index-generated.md`
- `rg -n "AvaloniaRuntimeXamlLoader|RuntimeXamlLoaderConfiguration|ResourceInclude|StyleInclude" references/api-index-generated.md`
- `rg -n "UseWin32|UseX11|UseAvaloniaNative|UseBrowser|UseAndroid|UseiOS" references/api-index-generated.md`

## Execution Rules

- Prefer compiled XAML and compiled bindings for production.
- Default to XAML-first examples and guidance; provide code-only UI construction only when the user explicitly requests it.
- Treat `RequiresUnreferencedCode` and `RequiresDynamicCode` APIs as opt-in tradeoffs.
- Keep binding paths typed (`x:DataType`) and avoid runtime parser fallbacks when equivalent typed APIs exist.
- Use platform option classes through `AppBuilder.With<T>(...)` instead of ad-hoc globals.
- Preserve clear separation: startup wiring, view definitions, viewmodel/reactive state, and styling/resources.
- Include end-to-end examples in responses when asked for architecture changes.
