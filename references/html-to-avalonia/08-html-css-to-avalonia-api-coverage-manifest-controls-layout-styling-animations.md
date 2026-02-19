# HTML/CSS to Avalonia API Coverage Manifest (Controls, Layout, Styling, Animations)

## Table of Contents
1. Purpose
2. Coverage Contract
3. Controls API Coverage (100% Type Surface)
4. Layout API Coverage Path
5. Styling API Coverage Path
6. Animation API Coverage Path
7. Coverage Validation Workflow
8. How to Use This Manifest in Migration Work
9. Extended HTML/CSS Topic Coverage

## Purpose

This manifest defines how the HTML/CSS conversion references map to full Avalonia API lookup for `11.3.12`.

Use it when you need to move from pattern guidance to exhaustive public API signatures.

This file is index/coverage metadata only and intentionally contains no HTML/CSS/XAML/C# code samples.

## Coverage Contract

For this repository, complete lookup coverage is provided by combining:

1. generated per-control docs:
- [`controls/README.md`](../controls/README)
- one file per control under [`controls/`](../controls/)

2. generated signature index:
- [`api-index-generated.md`](../api-index-generated)

As of `2026-02-18` in this repo snapshot:

- controls documented: `135` (see [`controls/README.md`](../controls/README)),
- animation signatures matched by source-group query: `223`,
- layout signatures matched by source-group query: `385`,
- styling signatures matched by source-group query: `172`.

These counts are lookup baselines for this snapshot, not promises of static values across future regenerations.

## Controls API Coverage (100% Type Surface)

Entry points:

- [`52-controls-reference-catalog.md`](../52-controls-reference-catalog)
- [`controls/README.md`](../controls/README)

The controls catalog is generated from Avalonia `11.3.12` and includes:

- control metadata,
- basic public API members,
- minimal XAML/C# usage per control.

For any HTML element-to-control migration decision, resolve to specific control docs first, then apply the conversion patterns in `00`, `01`, and `06`.

## Layout API Coverage Path

Primary app-facing layout references:

- [`30-layout-measure-arrange-and-custom-layout-controls.md`](../30-layout-measure-arrange-and-custom-layout-controls)
- [`21-custom-layout-authoring.md`](../21-custom-layout-authoring)
- [`00-html-css-layout-box-model-and-positioning.md`](00-html-css-layout-box-model-and-positioning)
- [`01-html-css-flexbox-grid-and-responsive-layout-recipes.md`](01-html-css-flexbox-grid-and-responsive-layout-recipes)

Full source-group lookup commands:

```bash
rg -n '^### `src/Avalonia.Base/Layout/' references/api-index-generated.md
rg -n '^### `src/Avalonia.Controls/(Grid|StackPanel|DockPanel|WrapPanel|Canvas|RelativePanel|Panel|ScrollViewer|VirtualizingPanel|VirtualizingStackPanel|LayoutTransformControl|Viewbox)' references/api-index-generated.md
```

## Styling API Coverage Path

Primary styling references:

- [`04-styles-themes-resources.md`](../04-styles-themes-resources)
- [`16-property-system-attached-properties-behaviors-and-style-properties.md`](../16-property-system-attached-properties-behaviors-and-style-properties)
- [`17-resources-assets-theme-variants-and-xmlns.md`](../17-resources-assets-theme-variants-and-xmlns)
- [`02-html-css-selectors-cascade-variables-and-theming.md`](02-html-css-selectors-cascade-variables-and-theming)
- [`07-html-css-design-system-utilities-and-component-variants.md`](07-html-css-design-system-utilities-and-component-variants)

Full source-group lookup command:

```bash
rg -n '^### `src/Avalonia.Base/Styling/' references/api-index-generated.md
```

## Animation API Coverage Path

Primary animation references:

- [`12-animations-transitions-and-frame-loops.md`](../12-animations-transitions-and-frame-loops)
- [`15-compositor-and-custom-visuals.md`](../15-compositor-and-custom-visuals)
- [`03-html-css-animations-transitions-and-motion-system.md`](03-html-css-animations-transitions-and-motion-system)

Full source-group lookup command:

```bash
rg -n '^### `src/Avalonia.Base/Animation/' references/api-index-generated.md
```

## Coverage Validation Workflow

Run after adding or expanding API-focused references:

```bash
python3 scripts/find_uncovered_apis.py --output plan/api-coverage-not-covered.md
python3 -m unittest scripts.test_find_uncovered_apis
```

If counts change materially, update:

- [`plan/api-coverage-detailed-report.md`](../../plan/api-coverage-detailed-report)
- [`plan/api-coverage-reference-update-plan.md`](../../plan/api-coverage-reference-update-plan)

## How to Use This Manifest in Migration Work

1. Find the web idiom conversion recipe (`00`-`39`).
2. Resolve exact control/layout/style/animation APIs via this manifest links.
3. Validate against generated signatures before finalizing production patterns.

## Extended HTML/CSS Topic Coverage

Use these additional comparison references for common modern app topics:

- [`09-html-css-typography-fonts-text-flow-and-truncation.md`](09-html-css-typography-fonts-text-flow-and-truncation)
- [`10-html-css-backgrounds-gradients-shadows-and-glass-patterns.md`](10-html-css-backgrounds-gradients-shadows-and-glass-patterns)
- [`11-html-css-transforms-3d-and-micro-interaction-patterns.md`](11-html-css-transforms-3d-and-micro-interaction-patterns)
- [`12-html-css-interaction-states-focus-gestures-and-input-ux.md`](12-html-css-interaction-states-focus-gestures-and-input-ux)
- [`13-html-css-navigation-tabs-sidebars-breadcrumbs-and-routing-patterns.md`](13-html-css-navigation-tabs-sidebars-breadcrumbs-and-routing-patterns)
- [`14-html-css-modal-drawer-toast-and-overlay-system-patterns.md`](14-html-css-modal-drawer-toast-and-overlay-system-patterns)
- [`15-html-css-data-table-list-and-master-detail-patterns.md`](15-html-css-data-table-list-and-master-detail-patterns)
- [`16-html-css-accessibility-semantics-and-motion-preference-mapping.md`](16-html-css-accessibility-semantics-and-motion-preference-mapping)
- [`17-html-css-units-calc-clamp-and-fluid-sizing-patterns.md`](17-html-css-units-calc-clamp-and-fluid-sizing-patterns)
- [`18-html-css-images-media-object-fit-and-aspect-ratio-patterns.md`](18-html-css-images-media-object-fit-and-aspect-ratio-patterns)
- [`19-html-css-sticky-scroll-linked-and-anchor-patterns.md`](19-html-css-sticky-scroll-linked-and-anchor-patterns)
- [`20-html-css-pseudo-elements-generated-content-and-decorative-layer-patterns.md`](20-html-css-pseudo-elements-generated-content-and-decorative-layer-patterns)
- [`21-html-css-grid-template-areas-to-avalonia-grid-region-patterns.md`](21-html-css-grid-template-areas-to-avalonia-grid-region-patterns)
- [`22-html-css-logical-properties-to-avalonia-flow-aware-spacing-and-alignment.md`](22-html-css-logical-properties-to-avalonia-flow-aware-spacing-and-alignment)
- [`23-html-css-rtl-bidi-and-flow-direction-mapping.md`](23-html-css-rtl-bidi-and-flow-direction-mapping)
- [`24-html-css-buttons-links-toggle-and-split-command-surfaces.md`](24-html-css-buttons-links-toggle-and-split-command-surfaces)
- [`25-html-css-details-accordion-and-treeview-hierarchical-disclosure.md`](25-html-css-details-accordion-and-treeview-hierarchical-disclosure)
- [`26-html-css-range-progress-meter-and-scroll-feedback-controls.md`](26-html-css-range-progress-meter-and-scroll-feedback-controls)
- [`27-html-css-advanced-input-autocomplete-date-time-mask-and-numeric-controls.md`](27-html-css-advanced-input-autocomplete-date-time-mask-and-numeric-controls)
- [`28-html-css-color-input-spectrum-and-theme-accent-controls.md`](28-html-css-color-input-spectrum-and-theme-accent-controls)
- [`29-html-css-tabs-offcanvas-and-carousel-shell-patterns.md`](29-html-css-tabs-offcanvas-and-carousel-shell-patterns)
- [`30-html-css-menubar-dropdown-and-context-menu-command-surfaces.md`](30-html-css-menubar-dropdown-and-context-menu-command-surfaces)
- [`31-html-web-components-custom-elements-to-avalonia-custom-and-templated-controls.md`](31-html-web-components-custom-elements-to-avalonia-custom-and-templated-controls)
- [`32-html-shadow-dom-slots-and-css-parts-to-avalonia-control-templates-and-themes.md`](32-html-shadow-dom-slots-and-css-parts-to-avalonia-control-templates-and-themes)
- [`33-html-data-attributes-custom-events-and-behaviors-to-avalonia-attached-properties.md`](33-html-data-attributes-custom-events-and-behaviors-to-avalonia-attached-properties)
- [`34-html-css-cascade-layers-scope-and-has-state-to-avalonia-style-architecture.md`](34-html-css-cascade-layers-scope-and-has-state-to-avalonia-style-architecture)
- [`35-html-css-select-option-multiselect-and-combobox-to-avalonia-selecting-controls.md`](35-html-css-select-option-multiselect-and-combobox-to-avalonia-selecting-controls)
- [`36-html-css-switch-checkbox-radio-and-tristate-to-avalonia-toggle-controls.md`](36-html-css-switch-checkbox-radio-and-tristate-to-avalonia-toggle-controls)
- [`37-html-css-resizable-split-panes-and-drag-handles-to-avalonia-gridsplitter-and-thumb.md`](37-html-css-resizable-split-panes-and-drag-handles-to-avalonia-gridsplitter-and-thumb)
- [`38-html-css-pull-to-refresh-and-live-feed-patterns-to-avalonia-refreshcontainer.md`](38-html-css-pull-to-refresh-and-live-feed-patterns-to-avalonia-refreshcontainer)
- [`39-html-css-headless-tablist-and-segmented-navigation-to-avalonia-tabstrip.md`](39-html-css-headless-tablist-and-segmented-navigation-to-avalonia-tabstrip)
