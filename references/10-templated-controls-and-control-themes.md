# Templated Controls and Control Themes

## Table of Contents
1. Scope and APIs
2. Authoring Workflow
3. XAML and C# Patterns
4. Template Utility Bridge
5. Best Practices
6. Troubleshooting
7. XAML-First and Code-Only Usage

## Scope and APIs

Primary APIs from the Avalonia codebase:
- `TemplatedControl`
- `TemplatePartAttribute`
- `TemplateAppliedEventArgs`
- `ControlTheme`
- `StyledElement.Theme`
- `TemplateBinding`
- `IControlTemplate`
- `TemplateExtensions.GetTemplateChildren(...)`
- `ThemeVariantScope`

Important members:
- `TemplatedControl.TemplateProperty`
- `TemplatedControl.ApplyTemplate()`
- `TemplatedControl.OnApplyTemplate(TemplateAppliedEventArgs e)`
- `TemplatedControl.TemplateApplied` event
- `TemplatePartAttribute(Name, Type)` and `IsRequired`
- `ControlTheme.TargetType`
- `ControlTheme.BasedOn`
- `StyledElement.Theme`
- `TemplateBinding.Description`

Reference source files:
- `src/Avalonia.Controls/Primitives/TemplatedControl.cs`
- `src/Avalonia.Base/Controls/Metadata/TemplatePartAttribute.cs`
- `src/Avalonia.Base/Styling/ControlTheme.cs`
- `src/Avalonia.Base/Data/TemplateBinding.cs`
- `src/Avalonia.Controls/Templates/IControlTemplate.cs`
- `src/Avalonia.Controls/Templates/TemplateExtensions.cs`

## Authoring Workflow

1. Define your control as a `TemplatedControl`.
2. Register properties with the Avalonia property system.
3. Declare template parts with `[TemplatePart]`.
4. Override `OnApplyTemplate` and pull parts from `e.NameScope`.
5. Publish a `ControlTheme` keyed by `{x:Type YourControl}`.
6. Use `TemplateBinding` inside the control template for runtime-fast property flow.

### Minimal custom control

```csharp
using Avalonia;
using Avalonia.Controls;
using Avalonia.Controls.Metadata;
using Avalonia.Controls.Primitives;

[TemplatePart("PART_ContentHost", typeof(ContentPresenter), IsRequired = true)]
public class FastCard : TemplatedControl
{
    public static readonly StyledProperty<string?> TitleProperty =
        AvaloniaProperty.Register<FastCard, string?>(nameof(Title));

    private ContentPresenter? _contentHost;

    public string? Title
    {
        get => GetValue(TitleProperty);
        set => SetValue(TitleProperty, value);
    }

    protected override void OnApplyTemplate(TemplateAppliedEventArgs e)
    {
        base.OnApplyTemplate(e);
        _contentHost = e.NameScope.Find<ContentPresenter>("PART_ContentHost");
    }
}
```

### Matching `ControlTheme`

```xml
<ControlTheme x:Key="{x:Type local:FastCard}" TargetType="local:FastCard">
  <Setter Property="Padding" Value="12" />
  <Setter Property="Template">
    <ControlTemplate>
      <Border Padding="{TemplateBinding Padding}">
        <StackPanel Spacing="8">
          <TextBlock Text="{TemplateBinding Title}" FontWeight="SemiBold" />
          <ContentPresenter x:Name="PART_ContentHost"
                            Content="{TemplateBinding Content}" />
        </StackPanel>
      </Border>
    </ControlTemplate>
  </Setter>
</ControlTheme>
```

## XAML and C# Patterns

Use `TemplateBinding` for templated parent properties:
- `Padding="{TemplateBinding Padding}"`
- `Foreground="{TemplateBinding Foreground}"`
- `BorderBrush="{TemplateBinding BorderBrush}"`

For diagnostics and tooling output, `TemplateBinding.Description` returns a concise `"TemplateBinding: <Property>"` string.

Use nested styles in themes for pseudo-classes:

```xml
<Style Selector="^:pointerover /template/ Border">
  <Setter Property="Background" Value="{DynamicResource CardHoverBrush}" />
</Style>
```

Build theme inheritance with `BasedOn`:

```xml
<ControlTheme x:Key="DangerFastCard"
              TargetType="local:FastCard"
              BasedOn="{StaticResource {x:Type local:FastCard}}">
  <Setter Property="BorderBrush" Value="Tomato" />
</ControlTheme>
```

Apply per-instance theme explicitly:

```xml
<local:FastCard Theme="{StaticResource DangerFastCard}" />
```

## Template Utility Bridge

For advanced template helper APIs used by framework-style control authoring, see:
- [`51-template-content-and-func-template-patterns.md`](51-template-content-and-func-template-patterns)

Key bridge APIs:
- `IControlTemplate`
- `ITemplate<TemplatedControl, TemplateResult<Control>?>`
- `TemplateExtensions.GetTemplateChildren(...)`
- `TemplateContent.Load(...)`

Use this layer for diagnostics and advanced template composition, while keeping normal control-theme authoring in XAML.

## Best Practices

- Treat `OnApplyTemplate` as idempotent. Templates can be reapplied.
- Never assume template parts exist unless guarded.
- Keep control logic in C# and visual states in themes/styles.
- Expose state as Avalonia properties; avoid direct visual tree coupling.
- Prefer `ControlTheme` over giant global selectors for reusable controls.
- Keep part names stable and prefixed with `PART_`.
- For AOT-safe apps, avoid reflection-based control creation paths in templates.

## Troubleshooting

1. `OnApplyTemplate` not firing as expected:
- Ensure a `Template` exists through a `ControlTheme` or local setter.
- Confirm control is attached and measured/arranged.

2. Part is `null`:
- Name mismatch between `[TemplatePart]` and `x:Name`.
- Theme loaded but wrong `TargetType` so template did not apply.

3. Styles in theme not matching:
- In a `ControlTheme`, nested selectors must use `^` nesting anchors.
- Use `/template/` when targeting template visuals.

4. Control not themeable:
- Move hardcoded visuals from control logic into the `ControlTheme`.
- Expose key knobs as styled properties (`CornerRadius`, `Padding`, etc.).

## XAML-First and Code-Only Usage

Default mode:
- Author control template/theme in XAML.
- Use code-only template/theme assignment only when requested.

XAML-first complete example:

```xml
<Application xmlns="https://github.com/avaloniaui"
             xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
             xmlns:local="using:MyApp.Controls"
             x:Class="MyApp.App">
  <Application.Resources>
    <ControlTheme x:Key="{x:Type local:FastCard}" TargetType="local:FastCard">
      <Setter Property="Template">
        <ControlTemplate>
          <Border Padding="{TemplateBinding Padding}" Background="#20242B">
            <StackPanel Spacing="6">
              <TextBlock Text="{TemplateBinding Title}" FontWeight="Bold" />
              <ContentPresenter x:Name="PART_ContentHost" Content="{TemplateBinding Content}" />
            </StackPanel>
          </Border>
        </ControlTemplate>
      </Setter>
    </ControlTheme>
  </Application.Resources>
</Application>
```

Code-only alternative (on request):

```csharp
using Avalonia;
using Avalonia.Controls;
using Avalonia.Controls.Templates;
using Avalonia.Media;
using Avalonia.Styling;

var theme = new ControlTheme(typeof(FastCard));
theme.Setters.Add(new Setter(TemplatedControl.TemplateProperty,
    new FuncControlTemplate<FastCard>((owner, scope) =>
    {
        var stack = new StackPanel { Spacing = 6 };
        stack.Children.Add(new TextBlock { Text = owner.Title, FontWeight = FontWeight.Bold });
        stack.Children.Add(new ContentPresenter { Name = "PART_ContentHost", Content = owner.Content });
        return new Border { Padding = owner.Padding, Background = Brushes.DimGray, Child = stack };
    })));

Application.Current!.Resources[typeof(FastCard)] = theme;
```
