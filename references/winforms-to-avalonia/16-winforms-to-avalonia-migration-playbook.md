# WinForms to Avalonia Migration Playbook

## Table of Contents
1. Scope
2. Migration Phases
3. Risk-Control Checklist
4. Example Slice Plan
5. C# Equivalent Migration Skeleton
6. Exit Criteria

## Scope

This playbook provides a practical sequencing model for migrating production WinForms applications to Avalonia with minimal regression risk.

## Migration Phases

1. Baseline and inventory:
- catalog forms, controls, dialogs, threading hotspots, and owner-draw surfaces.

2. Shell and lifetime:
- establish Avalonia app startup, desktop lifetime, main window host, and navigation skeleton.

3. Layout and binding:
- port containers, replace `Dock/Anchor`, migrate data binding to typed view models.

4. Interaction and services:
- migrate commands/shortcuts, menus/tray/dialogs/storage, and background workflows.

5. Styling and custom controls:
- port visual system using resources/styles/templates; move custom rendering where needed.

6. Hardening:
- validate accessibility, performance, and platform behavior; close parity gaps.

## Risk-Control Checklist

- compile with typed bindings (`x:DataType`) for migrated views.
- keep winforms and avalonia parity test scenarios per feature slice.
- avoid all-at-once migrations of owner-draw + data + platform services.
- keep migration PRs small and reversible.

## Example Slice Plan

WinForms baseline (slice candidate):

```csharp
var toolbar = new FlowLayoutPanel
{
    Dock = DockStyle.Top,
    AutoSize = true
};

var searchBox = new TextBox { Width = 220 };
var exportButton = new Button { Text = "Export" };
var customersGrid = new DataGridView
{
    Dock = DockStyle.Fill,
    AutoGenerateColumns = false
};

exportButton.Click += (_, _) => ExportVisibleCustomers();
searchBox.TextChanged += (_, _) => ApplyFilter(searchBox.Text);

toolbar.Controls.Add(searchBox);
toolbar.Controls.Add(exportButton);

Controls.Add(customersGrid);
Controls.Add(toolbar);
```

Avalonia XAML target slice:

```xaml
<Grid xmlns="https://github.com/avaloniaui"
      xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
      xmlns:vm="using:MyApp.ViewModels"
      x:DataType="vm:CustomerSearchViewModel"
      RowDefinitions="Auto,*"
      RowSpacing="8">
  <StackPanel Orientation="Horizontal" Spacing="8">
    <TextBox Watermark="Search" Text="{CompiledBinding Query, Mode=TwoWay}" />
    <Button Content="Export" Command="{CompiledBinding ExportCommand}" />
  </StackPanel>

  <ListBox Grid.Row="1" ItemsSource="{CompiledBinding FilteredCustomers}" />
</Grid>
```

## C# Equivalent Migration Skeleton

```csharp
public sealed class MigrationSlice
{
    public string Name { get; init; } = string.Empty;
    public bool LayoutPorted { get; set; }
    public bool BindingPorted { get; set; }
    public bool CommandsPorted { get; set; }
    public bool DialogsPorted { get; set; }
    public bool Verified { get; set; }
}

public static bool ReadyForCutover(MigrationSlice slice)
    => slice.LayoutPorted && slice.BindingPorted && slice.CommandsPorted && slice.DialogsPorted && slice.Verified;
```

## Exit Criteria

- parity-critical workflows pass on target platforms.
- no blocking UI-thread regressions under typical workloads.
- startup/lifetime/dialog/menu/tray patterns are fully migrated.
- remaining gaps are documented with mitigation timelines.
