# WinForms Control Lifecycle and Layout Basics to Avalonia

## Table of Contents
1. Scope and APIs
2. Lifecycle Mapping
3. Layout Contract Mapping
4. Common Conversion Example
5. AOT/Trimming Notes
6. Troubleshooting

## Scope and APIs

Primary WinForms APIs:

- `Control` (`Load`, `VisibleChanged`, `SuspendLayout`, `ResumeLayout`, `Dock`, `Anchor`)
- `Form` (`Shown`, `FormClosing`, `Dispose`)

Primary Avalonia APIs:

- `Control` and `Visual` lifecycle (`AttachedToVisualTree`, `DetachedFromVisualTree`)
- `TopLevel.GetTopLevel(...)`
- `Layoutable` sizing/alignment properties
- `Grid`, `DockPanel`, `Border`, `ContentControl`

## Lifecycle Mapping

| WinForms pattern | Avalonia mapping |
|---|---|
| `Form.Load` | constructor + `AttachedToVisualTree` for visual-root-dependent logic |
| `Form.Shown` | `Window.Opened` |
| `FormClosing` | `Window.Closing` |
| `Control.HandleCreated` | visual tree attachment + platform handle access via `TopLevel` |
| `SuspendLayout/ResumeLayout` | batch updates on view-model state and minimize redundant layout invalidations |

## Layout Contract Mapping

| WinForms | Avalonia |
|---|---|
| `Dock = Fill` | `Grid` cell with `HorizontalAlignment="Stretch"` and `VerticalAlignment="Stretch"` |
| `Anchor = Top | Right` | set `HorizontalAlignment="Right"` and top row placement |
| `Padding` on containers | `Padding` on `Border`, `Panel`-like controls that expose it |
| `AutoSize` | explicit layout sizing + content-driven measurement |

## Common Conversion Example

WinForms C#:

```csharp
public partial class MainForm : Form
{
    public MainForm()
    {
        InitializeComponent();

        SuspendLayout();

        var panel = new Panel { Dock = DockStyle.Fill };
        var save = new Button
        {
            Text = "Save",
            Anchor = AnchorStyles.Top | AnchorStyles.Right,
            Location = new Point(680, 8)
        };
        save.Click += (_, _) => SaveDocument();

        panel.Controls.Add(save);
        Controls.Add(panel);

        ResumeLayout();
    }
}
```

Avalonia XAML:

```xaml
<UserControl xmlns="https://github.com/avaloniaui"
             xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
             xmlns:vm="using:MyApp.ViewModels"
             x:DataType="vm:MainViewModel">
  <Grid RowDefinitions="Auto,*" ColumnDefinitions="*,Auto" Margin="8">
    <Button Grid.Row="0"
            Grid.Column="1"
            Content="Save"
            Command="{CompiledBinding SaveCommand}"
            HorizontalAlignment="Right" />
  </Grid>
</UserControl>
```

Avalonia C#:

```csharp
using Avalonia;
using Avalonia.Controls;
using Avalonia.Layout;

var root = new Grid
{
    RowDefinitions = RowDefinitions.Parse("Auto,*"),
    ColumnDefinitions = ColumnDefinitions.Parse("*,Auto"),
    Margin = new Thickness(8)
};

var save = new Button
{
    Content = "Save",
    Command = viewModel.SaveCommand,
    HorizontalAlignment = HorizontalAlignment.Right
};

Grid.SetRow(save, 0);
Grid.SetColumn(save, 1);
root.Children.Add(save);
```

## AOT/Trimming Notes

- compiled bindings are the default for migrated views.
- prefer explicit, typed view-model properties instead of string-based dynamic property access.

## Troubleshooting

1. Lifecycle code runs too early.
- move code requiring `TopLevel` from constructor to `AttachedToVisualTree`.

2. Converted layout clips unexpectedly.
- verify parent container constraints and row/column definitions.

3. Frequent visual churn after migration.
- coalesce model updates and avoid unnecessary layout invalidation loops.
