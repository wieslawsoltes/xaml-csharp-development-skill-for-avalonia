# WinForms Resources, Localization, Settings, and Assets to Avalonia

## Table of Contents
1. Scope and APIs
2. Resource and Localization Mapping
3. Settings Mapping
4. Conversion Example
5. C# Equivalent
6. Troubleshooting

## Scope and APIs

Primary WinForms APIs:

- `.resx` resources
- `ComponentResourceManager`
- `Properties.Settings.Default`

Primary Avalonia APIs/patterns:

- `ResourceDictionary`, theme resources
- asset URIs (`avares://...` and app-relative assets)
- localization service pattern bound into view models
- configuration-backed app settings service

## Resource and Localization Mapping

| WinForms | Avalonia |
|---|---|
| designer-set localized strings in `.resx` | bind text via localization service/view-model properties |
| embedded image resources | asset URIs and `WindowIcon`/`Image` sources |
| per-form resource managers | app-level resource dictionaries and typed localization abstractions |

## Settings Mapping

| WinForms | Avalonia |
|---|---|
| `Properties.Settings.Default` | explicit settings service (for example JSON + DI/service locator) |
| automatic setting save on close | controlled persistence in lifetime shutdown path |

## Conversion Example

WinForms C#:

```csharp
Text = Properties.Resources.MainWindowTitle;
iconPictureBox.Image = Properties.Resources.Logo;

if (Properties.Settings.Default.RememberFilter)
    filterCheckBox.Checked = true;
```

Avalonia XAML:

```xaml
<StackPanel xmlns="https://github.com/avaloniaui"
            xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
            xmlns:vm="using:MyApp.ViewModels"
            x:DataType="vm:ShellViewModel"
            Spacing="8">
  <TextBlock Text="{CompiledBinding TitleText}" />
  <Image Source="avares://MyApp/Assets/logo.png" Width="96" Height="96" />
  <CheckBox Content="Remember filter"
            IsChecked="{CompiledBinding RememberFilter, Mode=TwoWay}" />
</StackPanel>
```

## C# Equivalent

```csharp
public interface IAppSettings
{
    bool RememberFilter { get; set; }
    string PreferredCulture { get; set; }
    void Save();
}

public sealed class ShellViewModel
{
    private readonly IAppSettings _settings;

    public ShellViewModel(IAppSettings settings, ILocalizationService localization)
    {
        _settings = settings;
        TitleText = localization["MainWindowTitle"];
        RememberFilter = _settings.RememberFilter;
    }

    public string TitleText { get; }
    public bool RememberFilter { get; set; }

    public void Persist()
    {
        _settings.RememberFilter = RememberFilter;
        _settings.Save();
    }
}
```

## Troubleshooting

1. Localized text updates inconsistently.
- centralize lookup through one localization service and notify bindings on culture change.

2. Settings are lost after restart.
- ensure save is called in a deterministic shutdown path.

3. Asset paths break after migration.
- use consistent Avalonia asset URIs and verify build action/packaging.
