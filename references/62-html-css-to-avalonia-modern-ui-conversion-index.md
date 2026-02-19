# HTML/CSS to Avalonia Modern UI Conversion Index

## Table of Contents
1. Scope and Coverage Contract
2. HTML/CSS Spec Areas Mapped
3. Migration Workflow
4. Granular Reference Set
5. Full API Coverage Pointers
6. First Conversion Example
7. AOT/Trimming and Threading Notes
8. Troubleshooting

## Scope and Coverage Contract

This reference lane maps modern HTML/CSS UI idioms to Avalonia `11.3.12` XAML/C# patterns for:

- layout and responsive composition,
- styling, selectors, theming, and design tokens,
- transitions/animations/compositor motion,
- controls and form semantics for app UI.

Coverage intent for this lane:

- conversion guidance is practical and example-driven,
- API lookup is exhaustive through generated references:
  - controls: one file per control in [`controls/README.md`](controls/README),
  - signatures: [`api-index-generated.md`](api-index-generated).

## HTML/CSS Spec Areas Mapped

- CSS Box Model (`width`, `height`, `margin`, `padding`, `border`)
- CSS Display and Formatting Contexts (`block`, `inline`, `flex`, `grid`)
- CSS Positioning (`static`, `relative`, `absolute`, stacking)
- CSS Units and Sizing (`px`, `rem`, `%`, `vw/vh`, `minmax`, `clamp`)
- CSS Selectors/Cascade/Specificity
- CSS Custom Properties and theming
- CSS Transitions/Animations/Easing
- CSS Visual Effects (`box-shadow`, gradients, backdrop-like effects)
- CSS Transforms and Interaction States (`hover`, `active`, `focus-visible`)
- CSS Media/Object Fit/Aspect Ratio patterns
- CSS Functions (`calc`, `min`, `max`, `clamp`) and fluid sizing
- CSS Sticky/scroll-linked patterns and snap behavior
- CSS Pseudo-elements (`::before`, `::after`) and generated content
- CSS Grid named-area composition (`grid-template-areas`) and responsive area remapping
- CSS Logical Properties (`margin-inline`, `padding-block`, `inset-inline`) and flow-aware spacing
- CSS bidi/RTL direction mapping (`dir`, `direction`, mixed-direction text flows)
- Web components/custom elements (`customElements`, host attributes) to custom/templated controls
- Shadow DOM slots and CSS parts (`<slot>`, `::part`) to `ContentPresenter` and template-part selectors
- `data-*` behavior metadata and custom DOM events (`CustomEvent`) to attached properties and routed events
- CSS architecture features (`@layer`, `@scope`, `:has`, `@container`) to style order, scoped selectors, class-state, and `ContainerQuery`
- HTML select/listbox semantics (`<select>`, `<option>`, multi-select) to `ComboBox`, `ListBox`, and `SelectingItemsControl`
- switch/radio/tri-state semantics (`role="switch"`, `aria-checked="mixed"`) to `ToggleSwitch`, `RadioButton`, `CheckBox`
- resizable pane and drag-handle patterns (`resize`, `col-resize`, `row-resize`) to `GridSplitter` and `Thumb`
- pull-to-refresh and live-feed reload workflows to `RefreshContainer` and `RefreshVisualizer`
- headless tablist/segmented navigation (`role="tablist"`) to `TabStrip` + content host patterns
- HTML semantic/form element usage for application UIs
- Responsive/mobile-first app-shell and navigation composition
- Accessibility semantics and reduced-motion strategies

## Migration Workflow

1. Model structure first (layout containers and control tree).
2. Port design tokens (color, spacing, typography) to resources.
3. Port selectors/states to Avalonia classes and pseudo-classes.
4. Port motion from CSS transitions/keyframes to `Transitions`/`Animation`.
5. Port interaction semantics (commands, focus, validation, accessibility).
6. Validate against full API references for edge cases.

## Granular Reference Set

- All detailed HTML/CSS conversion references now live under [`html-to-avalonia/README.md`](html-to-avalonia/README):
  - [`00-html-css-layout-box-model-and-positioning.md`](html-to-avalonia/00-html-css-layout-box-model-and-positioning)
  - [`01-html-css-flexbox-grid-and-responsive-layout-recipes.md`](html-to-avalonia/01-html-css-flexbox-grid-and-responsive-layout-recipes)
  - [`02-html-css-selectors-cascade-variables-and-theming.md`](html-to-avalonia/02-html-css-selectors-cascade-variables-and-theming)
  - [`03-html-css-animations-transitions-and-motion-system.md`](html-to-avalonia/03-html-css-animations-transitions-and-motion-system)
  - [`04-html-forms-input-and-validation-to-avalonia-controls.md`](html-to-avalonia/04-html-forms-input-and-validation-to-avalonia-controls)
  - [`05-html-shell-navigation-popups-and-layering-patterns.md`](html-to-avalonia/05-html-shell-navigation-popups-and-layering-patterns)
  - [`06-html-rich-content-lists-cards-tables-and-virtualization.md`](html-to-avalonia/06-html-rich-content-lists-cards-tables-and-virtualization)
  - [`07-html-css-design-system-utilities-and-component-variants.md`](html-to-avalonia/07-html-css-design-system-utilities-and-component-variants)
  - [`08-html-css-to-avalonia-api-coverage-manifest-controls-layout-styling-animations.md`](html-to-avalonia/08-html-css-to-avalonia-api-coverage-manifest-controls-layout-styling-animations)
  - [`09-html-css-typography-fonts-text-flow-and-truncation.md`](html-to-avalonia/09-html-css-typography-fonts-text-flow-and-truncation)
  - [`10-html-css-backgrounds-gradients-shadows-and-glass-patterns.md`](html-to-avalonia/10-html-css-backgrounds-gradients-shadows-and-glass-patterns)
  - [`11-html-css-transforms-3d-and-micro-interaction-patterns.md`](html-to-avalonia/11-html-css-transforms-3d-and-micro-interaction-patterns)
  - [`12-html-css-interaction-states-focus-gestures-and-input-ux.md`](html-to-avalonia/12-html-css-interaction-states-focus-gestures-and-input-ux)
  - [`13-html-css-navigation-tabs-sidebars-breadcrumbs-and-routing-patterns.md`](html-to-avalonia/13-html-css-navigation-tabs-sidebars-breadcrumbs-and-routing-patterns)
  - [`14-html-css-modal-drawer-toast-and-overlay-system-patterns.md`](html-to-avalonia/14-html-css-modal-drawer-toast-and-overlay-system-patterns)
  - [`15-html-css-data-table-list-and-master-detail-patterns.md`](html-to-avalonia/15-html-css-data-table-list-and-master-detail-patterns)
  - [`16-html-css-accessibility-semantics-and-motion-preference-mapping.md`](html-to-avalonia/16-html-css-accessibility-semantics-and-motion-preference-mapping)
  - [`17-html-css-units-calc-clamp-and-fluid-sizing-patterns.md`](html-to-avalonia/17-html-css-units-calc-clamp-and-fluid-sizing-patterns)
  - [`18-html-css-images-media-object-fit-and-aspect-ratio-patterns.md`](html-to-avalonia/18-html-css-images-media-object-fit-and-aspect-ratio-patterns)
  - [`19-html-css-sticky-scroll-linked-and-anchor-patterns.md`](html-to-avalonia/19-html-css-sticky-scroll-linked-and-anchor-patterns)
  - [`20-html-css-pseudo-elements-generated-content-and-decorative-layer-patterns.md`](html-to-avalonia/20-html-css-pseudo-elements-generated-content-and-decorative-layer-patterns)
  - [`21-html-css-grid-template-areas-to-avalonia-grid-region-patterns.md`](html-to-avalonia/21-html-css-grid-template-areas-to-avalonia-grid-region-patterns)
  - [`22-html-css-logical-properties-to-avalonia-flow-aware-spacing-and-alignment.md`](html-to-avalonia/22-html-css-logical-properties-to-avalonia-flow-aware-spacing-and-alignment)
  - [`23-html-css-rtl-bidi-and-flow-direction-mapping.md`](html-to-avalonia/23-html-css-rtl-bidi-and-flow-direction-mapping)
  - [`24-html-css-buttons-links-toggle-and-split-command-surfaces.md`](html-to-avalonia/24-html-css-buttons-links-toggle-and-split-command-surfaces)
  - [`25-html-css-details-accordion-and-treeview-hierarchical-disclosure.md`](html-to-avalonia/25-html-css-details-accordion-and-treeview-hierarchical-disclosure)
  - [`26-html-css-range-progress-meter-and-scroll-feedback-controls.md`](html-to-avalonia/26-html-css-range-progress-meter-and-scroll-feedback-controls)
  - [`27-html-css-advanced-input-autocomplete-date-time-mask-and-numeric-controls.md`](html-to-avalonia/27-html-css-advanced-input-autocomplete-date-time-mask-and-numeric-controls)
  - [`28-html-css-color-input-spectrum-and-theme-accent-controls.md`](html-to-avalonia/28-html-css-color-input-spectrum-and-theme-accent-controls)
  - [`29-html-css-tabs-offcanvas-and-carousel-shell-patterns.md`](html-to-avalonia/29-html-css-tabs-offcanvas-and-carousel-shell-patterns)
  - [`30-html-css-menubar-dropdown-and-context-menu-command-surfaces.md`](html-to-avalonia/30-html-css-menubar-dropdown-and-context-menu-command-surfaces)
  - [`31-html-web-components-custom-elements-to-avalonia-custom-and-templated-controls.md`](html-to-avalonia/31-html-web-components-custom-elements-to-avalonia-custom-and-templated-controls)
  - [`32-html-shadow-dom-slots-and-css-parts-to-avalonia-control-templates-and-themes.md`](html-to-avalonia/32-html-shadow-dom-slots-and-css-parts-to-avalonia-control-templates-and-themes)
  - [`33-html-data-attributes-custom-events-and-behaviors-to-avalonia-attached-properties.md`](html-to-avalonia/33-html-data-attributes-custom-events-and-behaviors-to-avalonia-attached-properties)
  - [`34-html-css-cascade-layers-scope-and-has-state-to-avalonia-style-architecture.md`](html-to-avalonia/34-html-css-cascade-layers-scope-and-has-state-to-avalonia-style-architecture)
  - [`35-html-css-select-option-multiselect-and-combobox-to-avalonia-selecting-controls.md`](html-to-avalonia/35-html-css-select-option-multiselect-and-combobox-to-avalonia-selecting-controls)
  - [`36-html-css-switch-checkbox-radio-and-tristate-to-avalonia-toggle-controls.md`](html-to-avalonia/36-html-css-switch-checkbox-radio-and-tristate-to-avalonia-toggle-controls)
  - [`37-html-css-resizable-split-panes-and-drag-handles-to-avalonia-gridsplitter-and-thumb.md`](html-to-avalonia/37-html-css-resizable-split-panes-and-drag-handles-to-avalonia-gridsplitter-and-thumb)
  - [`38-html-css-pull-to-refresh-and-live-feed-patterns-to-avalonia-refreshcontainer.md`](html-to-avalonia/38-html-css-pull-to-refresh-and-live-feed-patterns-to-avalonia-refreshcontainer)
  - [`39-html-css-headless-tablist-and-segmented-navigation-to-avalonia-tabstrip.md`](html-to-avalonia/39-html-css-headless-tablist-and-segmented-navigation-to-avalonia-tabstrip)

## Full API Coverage Pointers

For exhaustive lookup (not just examples):

- controls: [`52-controls-reference-catalog.md`](52-controls-reference-catalog) and [`controls/README.md`](controls/README)
- layout internals and authoring: [`30-layout-measure-arrange-and-custom-layout-controls.md`](30-layout-measure-arrange-and-custom-layout-controls), [`21-custom-layout-authoring.md`](21-custom-layout-authoring)
- styles/themes/resources: [`04-styles-themes-resources.md`](04-styles-themes-resources), [`16-property-system-attached-properties-behaviors-and-style-properties.md`](16-property-system-attached-properties-behaviors-and-style-properties), [`17-resources-assets-theme-variants-and-xmlns.md`](17-resources-assets-theme-variants-and-xmlns)
- animation/compositor: [`12-animations-transitions-and-frame-loops.md`](12-animations-transitions-and-frame-loops), [`15-compositor-and-custom-visuals.md`](15-compositor-and-custom-visuals)
- signatures: [`api-index-generated.md`](api-index-generated)

## First Conversion Example

HTML/CSS card:

```html
<article class="card">
  <h2>Revenue</h2>
  <p class="value">$420,000</p>
</article>
```

```css
.card {
  padding: 16px;
  border-radius: 12px;
  background: #10151e;
  border: 1px solid #283348;
}
.value {
  font-size: 2rem;
  font-weight: 700;
}
```

Avalonia XAML:

```xaml
<Border Classes="card" Padding="16">
  <StackPanel Spacing="6">
    <TextBlock Classes="card-title" Text="Revenue" />
    <TextBlock Classes="card-value" Text="$420,000" />
  </StackPanel>
</Border>
```

```xaml
<Style Selector="Border.card">
  <Setter Property="CornerRadius" Value="12" />
  <Setter Property="Background" Value="#10151E" />
  <Setter Property="BorderBrush" Value="#283348" />
  <Setter Property="BorderThickness" Value="1" />
</Style>
<Style Selector="TextBlock.card-value">
  <Setter Property="FontSize" Value="32" />
  <Setter Property="FontWeight" Value="Bold" />
</Style>
```

Avalonia C#:

```csharp
using Avalonia.Controls;
using Avalonia.Media;

var card = new Border
{
    Padding = new Avalonia.Thickness(16),
    CornerRadius = new CornerRadius(12),
    Background = new SolidColorBrush(Color.Parse("#10151E")),
    BorderBrush = new SolidColorBrush(Color.Parse("#283348")),
    BorderThickness = new Avalonia.Thickness(1),
    Child = new StackPanel
    {
        Spacing = 6,
        Children =
        {
            new TextBlock { Text = "Revenue" },
            new TextBlock { Text = "$420,000", FontSize = 32, FontWeight = FontWeight.Bold }
        }
    }
};
```

## AOT/Trimming and Threading Notes

- Prefer compiled bindings with `x:DataType` in migrated views.
- Keep style/resource definitions in compiled XAML when possible.
- Marshal runtime class/style mutations to `Dispatcher.UIThread` when triggered from background work.

## Troubleshooting

1. Web-first layouts feel rigid after port.
- Replace CSS absolute-heavy patterns with `Grid` + overlays.

2. Selector behavior differs from CSS expectations.
- Move from deep descendant chains to explicit classes and control themes.

3. Animation ports jitter.
- Use built-in transitions first, then escalate to keyframes/compositor only for hotspots.
