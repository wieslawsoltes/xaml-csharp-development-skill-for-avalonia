# HTML `<select>`, `<option>`, and Multi-Select Patterns to Avalonia Selecting Controls

## Table of Contents
1. Scope and APIs
2. Mapping Table
3. Single-Select Dropdown Pattern
4. Multi-Select Listbox Pattern
5. Searchable Select Pattern
6. Conversion Example: Environment + Region Picker
7. C# Equivalent: Environment + Region Picker
8. AOT/Threading Notes
9. Troubleshooting

## Scope and APIs

Primary APIs:

- `SelectingItemsControl` (`SelectedIndex`, `SelectedItem`, `SelectedValue`, `SelectedValueBinding`, `SelectionChanged`, `IsTextSearchEnabled`, `WrapSelection`)
- `ComboBox` (`IsEditable`, `Text`, `PlaceholderText`, `MaxDropDownHeight`, `SelectionBoxItemTemplate`)
- `ListBox` (`SelectionMode`, `SelectedItems`, `SelectAll()`, `UnselectAll()`)
- `AutoCompleteBox` (`ItemsSource`, `Text`, `SelectedItem`, `FilterMode`, `AsyncPopulator`)

Reference docs:

- [`04-html-forms-input-and-validation-to-avalonia-controls.md`](04-html-forms-input-and-validation-to-avalonia-controls)
- [`27-html-css-advanced-input-autocomplete-date-time-mask-and-numeric-controls.md`](27-html-css-advanced-input-autocomplete-date-time-mask-and-numeric-controls)
- [`controls/combo-box.md`](../controls/combo-box)
- [`controls/list-box.md`](../controls/list-box)

## Mapping Table

| HTML/CSS idiom | Avalonia mapping |
|---|---|
| `<select>` single value | `ComboBox` |
| `<select multiple size="...">` | `ListBox SelectionMode="Multiple"` |
| selected option value | `SelectedValue` + `SelectedValueBinding` |
| keyboard type-to-select | `IsTextSearchEnabled` |
| searchable select / datalist | `AutoCompleteBox` or editable `ComboBox` |

## Single-Select Dropdown Pattern

HTML/CSS:

```html
<label for="env">Environment</label>
<select id="env" name="env">
  <option value="dev">Development</option>
  <option value="staging">Staging</option>
  <option value="prod" selected>Production</option>
</select>
```

```css
select {
  min-width: 14rem;
  border: 1px solid #2a3348;
  border-radius: .5rem;
  padding: .5rem .75rem;
}
```

Avalonia:

```xaml
<ComboBox ItemsSource="{CompiledBinding Environments}"
          SelectedValueBinding="{Binding Id}"
          SelectedValue="{CompiledBinding SelectedEnvironmentId, Mode=TwoWay}"
          PlaceholderText="Choose environment"
          IsTextSearchEnabled="True"
          MaxDropDownHeight="320" />
```

## Multi-Select Listbox Pattern

HTML/CSS:

```html
<label for="regions">Regions</label>
<select id="regions" multiple size="6">
  <option selected>us-east</option>
  <option>us-west</option>
  <option selected>eu-central</option>
  <option>ap-south</option>
</select>
```

```css
select[multiple] {
  min-height: 12rem;
}
```

Avalonia:

```xaml
<ListBox ItemsSource="{CompiledBinding Regions}"
         SelectionMode="Multiple"
         WrapSelection="False"
         IsTextSearchEnabled="True" />
```

## Searchable Select Pattern

HTML/CSS often combines `<input>` + datalist/autocomplete JS for large option sets.

```html
<label for="assignee">Assignee</label>
<input id="assignee" list="people" autocomplete="off" />
<datalist id="people"></datalist>
```

Avalonia pattern:

```xaml
<AutoCompleteBox Text="{CompiledBinding AssigneeQuery, Mode=TwoWay}"
                 SelectedItem="{CompiledBinding SelectedAssignee, Mode=TwoWay}"
                 ItemsSource="{CompiledBinding AssigneeSuggestions}"
                 FilterMode="StartsWith"
                 MinimumPrefixLength="2"
                 MinimumPopulateDelay="0:0:0.15" />
```

## Conversion Example: Environment + Region Picker

```html
<form class="deploy-form">
  <label>Environment</label>
  <select>
    <option value="dev">Development</option>
    <option value="staging">Staging</option>
    <option value="prod">Production</option>
  </select>

  <label>Regions</label>
  <select multiple size="5">
    <option>us-east</option>
    <option>us-west</option>
    <option>eu-central</option>
    <option>ap-south</option>
  </select>
</form>
```

```css
.deploy-form {
  display: grid;
  gap: .6rem;
  max-width: 24rem;
}
```

```xaml
<StackPanel Spacing="8" MaxWidth="420">
  <TextBlock Text="Environment" />
  <ComboBox ItemsSource="{CompiledBinding Environments}"
            SelectedValueBinding="{Binding Id}"
            SelectedValue="{CompiledBinding SelectedEnvironmentId, Mode=TwoWay}"
            IsTextSearchEnabled="True"
            PlaceholderText="Choose environment" />

  <TextBlock Text="Regions" />
  <ListBox ItemsSource="{CompiledBinding Regions}"
           SelectionMode="Multiple"
           IsTextSearchEnabled="True"
           MinHeight="180" />
</StackPanel>
```

## C# Equivalent: Environment + Region Picker

```csharp
using System.Collections.Generic;
using System.Threading.Tasks;
using Avalonia.Controls;
using Avalonia.Data;

var environments = new[]
{
    new { Id = "dev", Name = "Development" },
    new { Id = "staging", Name = "Staging" },
    new { Id = "prod", Name = "Production" }
};

var picker = new StackPanel
{
    Spacing = 8,
    MaxWidth = 420
};

var envCombo = new ComboBox
{
    ItemsSource = environments,
    SelectedValueBinding = new Binding("Id"),
    PlaceholderText = "Choose environment",
    IsTextSearchEnabled = true,
    MaxDropDownHeight = 320
};
envCombo.SelectedValue = "prod";

var regionsList = new ListBox
{
    ItemsSource = new[] { "us-east", "us-west", "eu-central", "ap-south" },
    SelectionMode = SelectionMode.Multiple,
    IsTextSearchEnabled = true,
    MinHeight = 180
};

var assigneeBox = new AutoCompleteBox
{
    FilterMode = AutoCompleteFilterMode.StartsWith,
    MinimumPrefixLength = 2,
    MinimumPopulateDelay = System.TimeSpan.FromMilliseconds(150),
    AsyncPopulator = async (text, ct) =>
    {
        await Task.Delay(80, ct);
        var values = new List<object>();
        if (!string.IsNullOrWhiteSpace(text))
            values.Add($"{text}-owner");
        return values;
    }
};

picker.Children.Add(new TextBlock { Text = "Environment" });
picker.Children.Add(envCombo);
picker.Children.Add(new TextBlock { Text = "Regions" });
picker.Children.Add(regionsList);
picker.Children.Add(new TextBlock { Text = "Assignee" });
picker.Children.Add(assigneeBox);
```

## AOT/Threading Notes

- Keep option item contracts typed and stable; use `SelectedValueBinding` for durable ID-based selection.
- For server-backed autocomplete, cancel stale requests and update suggestion collections on `Dispatcher.UIThread`.

## Troubleshooting

1. `SelectedValue` does not update.
- Confirm `SelectedValueBinding` points to a real member on each item.

2. Multi-select behaves like single-select.
- Verify `SelectionMode="Multiple"` (or another multi-select mode) is set on `ListBox`.

3. Text search jumps unpredictably.
- Disable `WrapSelection` if cyclic keyboard navigation is undesirable.
