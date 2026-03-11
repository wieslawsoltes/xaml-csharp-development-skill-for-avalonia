# Forms, Decision-Heavy UX, and Data-Dense Surfaces in Avalonia

## Table of Contents
1. Scope and Primary APIs
2. Form Design Rules
3. Data-Dense Surface Rules
4. Validation and Recovery Patterns
5. AOT and Runtime Notes
6. Do and Don't Guidance
7. Troubleshooting
8. Official Resources

## Scope and Primary APIs

Use this reference to design operational UI where correctness matters more than decoration.

Primary APIs:
- `TextBox`, `ComboBox`, `AutoCompleteBox`
- `DatePicker`, `CalendarDatePicker`, `NumericUpDown`
- `CheckBox`, `ToggleSwitch`, `RadioButton`
- `DataValidationErrors`
- `ListBox`, `TreeView`, `ScrollViewer`, `Grid`

This file covers:
- form structure and field hierarchy,
- dense operational layouts,
- validation and recovery,
- keeping high-information surfaces readable and calm.

## Form Design Rules

Forms should optimize for completion accuracy:

- keep labels visible; do not depend on placeholder text as the main label,
- group related fields into short sections,
- use helper text only where it removes ambiguity,
- place primary action near the decision boundary,
- surface validation close to the field and in a summary when needed.

```xml
<StackPanel xmlns="https://github.com/avaloniaui"
            xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
            Spacing="12">
  <TextBlock Classes="section-title" Text="Schedule rollout" />

  <TextBox Watermark="Release name"
           Text="{CompiledBinding ReleaseName}" />

  <CalendarDatePicker SelectedDate="{CompiledBinding StartDate}" />

  <NumericUpDown Value="{CompiledBinding MaxParallelNodes}"
                 Minimum="1"
                 Maximum="20" />

  <AutoCompleteBox Text="{CompiledBinding Owner}"
                   MinimumPrefixLength="2"
                   Watermark="Owner" />
</StackPanel>
```

## Data-Dense Surface Rules

Dense UI needs stronger structure, not more styling noise.

Rules:
- use spacing and alignment to create scanning lanes,
- keep column or row semantics stable across refreshes,
- use quiet surfaces and stronger typography hierarchy,
- reserve accent color for state or priority, not for every control,
- make bulk actions and filters discoverable without dominating the screen.

```xml
<Grid xmlns="https://github.com/avaloniaui"
      xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
      ColumnDefinitions="Auto,*,Auto"
      RowDefinitions="Auto,Auto,*"
      RowSpacing="12"
      ColumnSpacing="12">
  <TextBlock Grid.ColumnSpan="3"
             Classes="title"
             Text="Environment health" />

  <ComboBox Grid.Row="1"
            Width="220"
            SelectedItem="{CompiledBinding SeverityFilter}" />

  <TextBox Grid.Row="1"
           Grid.Column="1"
           Watermark="Search incidents"
           Text="{CompiledBinding SearchText}" />

  <Button Grid.Row="1"
          Grid.Column="2"
          Content="Refresh" />

  <ListBox Grid.Row="2"
           Grid.ColumnSpan="3"
           ItemContainerTheme="{StaticResource DenseListItemTheme}" />
</Grid>
```

## Validation and Recovery Patterns

```xml
<DataValidationErrors xmlns="https://github.com/avaloniaui"
                      xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml">
  <TextBox Text="{CompiledBinding ReleaseName}" />
</DataValidationErrors>
```

Guidance:
- validate early enough to prevent wasted effort,
- write errors in corrective language,
- show one recovery action when possible,
- keep warning, error, and success treatments visually related,
- use summary surfaces only when the form is large enough to justify them.

## AOT and Runtime Notes

- Prefer compiled bindings and built-in validation plumbing over ad hoc runtime form logic.
- Keep dense list and form themes shared so compact mode remains coherent.
- Avoid runtime-generated form layout unless a schema-driven product truly requires it.

## Do and Don't Guidance

Do:
- favor visible labels and clear grouping,
- make dense screens scannable with alignment and restraint,
- keep validation precise and recoverable.

Do not:
- rely on placeholder-only forms,
- color every field state aggressively,
- compress data-dense UI until targets become hard to use.

## Troubleshooting

1. The form looks clean but completion errors are high.
- Add visible labels, helper text at ambiguity points, and clearer validation.

2. Dense screens feel chaotic.
- Reduce accent use, normalize alignment, and strengthen section grouping.

3. Recovery feels frustrating.
- Rewrite validation and status content around the next corrective action.

## Official Resources

- ListView and GridView guidance: [learn.microsoft.com/en-us/windows/apps/design/controls/listview-and-gridview](https://learn.microsoft.com/en-us/windows/apps/design/controls/listview-and-gridview)
- Buttons for Windows apps: [learn.microsoft.com/en-us/windows/apps/design/controls/buttons](https://learn.microsoft.com/en-us/windows/apps/design/controls/buttons)
- Fluent 2 content design: [fluent2.microsoft.design/content-design](https://fluent2.microsoft.design/content-design)
- Fluent 2 message bar guidance: [fluent2.microsoft.design/components/web/react/core/messagebar/usage](https://fluent2.microsoft.design/components/web/react/core/messagebar/usage)
