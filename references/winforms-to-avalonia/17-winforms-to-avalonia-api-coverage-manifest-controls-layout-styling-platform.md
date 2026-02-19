# WinForms to Avalonia API Coverage Manifest (Controls, Layout, Styling, Platform)

## Table of Contents
1. Purpose
2. Coverage Contract
3. WinForms Source Coverage Pointers
4. Avalonia API Coverage Path
5. Validation Workflow
6. How to Use This Manifest

## Purpose

This manifest defines how WinForms migration references map to full API lookup surfaces in this repository.

Use it when you need to move from pattern guidance to exact API signatures.

## Coverage Contract

For this repository, practical completeness is provided by combining:

1. migration recipes in this lane (`00`-`38`),
2. per-control docs in [`../controls/README.md`](../controls/README),
3. generated signature index in [`../api-index-generated.md`](../api-index-generated).

## WinForms Source Coverage Pointers

Use these source roots for WinForms-side verification:

- `/Users/wieslawsoltes/GitHub/winforms/src/System.Windows.Forms/System/Windows/Forms/Control.cs`
- `/Users/wieslawsoltes/GitHub/winforms/src/System.Windows.Forms/System/Windows/Forms/Form.cs`
- `/Users/wieslawsoltes/GitHub/winforms/src/System.Windows.Forms/System/Windows/Forms/ControlStyles.cs`
- `/Users/wieslawsoltes/GitHub/winforms/src/System.Windows.Forms/System/Windows/Forms/Layout/LayoutEngine.cs`
- `/Users/wieslawsoltes/GitHub/winforms/src/System.Windows.Forms/System/Windows/Forms/Layout/DefaultLayout.cs`
- `/Users/wieslawsoltes/GitHub/winforms/src/System.Windows.Forms/System/Windows/Forms/Layout/LayoutTransaction.cs`
- `/Users/wieslawsoltes/GitHub/winforms/src/System.Windows.Forms/System/Windows/Forms/Layout/Containers/SplitContainer.cs`
- `/Users/wieslawsoltes/GitHub/winforms/src/System.Windows.Forms/System/Windows/Forms/Controls/Splitter/Splitter.cs`
- `/Users/wieslawsoltes/GitHub/winforms/src/System.Windows.Forms/System/Windows/Forms/Scrolling/ScrollableControl.cs`
- `/Users/wieslawsoltes/GitHub/winforms/src/System.Windows.Forms/System/Windows/Forms/Rendering/PaintEventArgs.cs`
- `/Users/wieslawsoltes/GitHub/winforms/src/System.Windows.Forms/System/Windows/Forms/Rendering/ControlPaint.cs`
- `/Users/wieslawsoltes/GitHub/winforms/src/System.Windows.Forms/System/Windows/Forms/Controls/DataGridView/`
- `/Users/wieslawsoltes/GitHub/winforms/src/System.Windows.Forms/System/Windows/Forms/Controls/ListView/ListView.cs`
- `/Users/wieslawsoltes/GitHub/winforms/src/System.Windows.Forms/System/Windows/Forms/Controls/TreeView/TreeView.cs`
- `/Users/wieslawsoltes/GitHub/winforms/src/System.Windows.Forms/System/Windows/Forms/Controls/RichTextBox/RichTextBox.cs`
- `/Users/wieslawsoltes/GitHub/winforms/src/System.Windows.Forms/System/Windows/Forms/Controls/Labels/LinkLabel.cs`
- `/Users/wieslawsoltes/GitHub/winforms/src/System.Windows.Forms/System/Windows/Forms/Controls/ToolStrips/ToolStripDropDownButton.cs`
- `/Users/wieslawsoltes/GitHub/winforms/src/System.Windows.Forms/System/Windows/Forms/Controls/ToolStrips/ToolStripSplitButton.cs`
- `/Users/wieslawsoltes/GitHub/winforms/src/System.Windows.Forms/System/Windows/Forms/DataBinding/BindingSource.cs`
- `/Users/wieslawsoltes/GitHub/winforms/src/System.Windows.Forms/System/Windows/Forms/ErrorProvider/ErrorProvider.cs`

## Avalonia API Coverage Path

Primary lookup references:

- controls index: [`../52-controls-reference-catalog.md`](../52-controls-reference-catalog)
- generated control docs: [`../controls/README.md`](../controls/README)
- signatures: [`../api-index-generated.md`](../api-index-generated)

Useful signature queries:

```bash
rg -n "TopLevel|IClassicDesktopStyleApplicationLifetime|Window" references/api-index-generated.md
rg -n "Grid|GridSplitter|DockPanel|WrapPanel|RelativePanel" references/api-index-generated.md
rg -n "Dispatcher|DispatcherTimer|KeyBinding|KeyGesture" references/api-index-generated.md
rg -n "IStorageProvider|OpenFilePickerAsync|SaveFilePickerAsync|OpenFolderPickerAsync" references/api-index-generated.md
rg -n "DataValidationErrors|AutomationProperties|FlowDirection" references/api-index-generated.md
```

## Validation Workflow

Run after significant migration-reference updates:

```bash
python3 scripts/find_uncovered_apis.py --output plan/api-coverage-not-covered.md
python3 -m unittest scripts.test_find_uncovered_apis
```

## How to Use This Manifest

1. pick the migration topic doc (`00`-`38`),
2. confirm concrete APIs via control docs and generated index,
3. validate against pinned Avalonia `11.3.12` behavior before adopting patterns.
