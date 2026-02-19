# HTML/CSS Advanced Input Patterns to Avalonia AutoComplete, Picker, Mask, and Numeric Controls

## Table of Contents
1. Scope and APIs
2. Mapping Table
3. Search Suggestion Pattern (`datalist` to `AutoCompleteBox`)
4. Date/Time Input Pattern
5. Masked and Numeric Input Pattern
6. Conversion Example: Scheduling Form
7. C# Equivalent: Scheduling Form
8. AOT/Threading Notes
9. Troubleshooting

## Scope and APIs

Primary APIs:

- `AutoCompleteBox` (`ItemsSource`, `Text`, `SelectedItem`, `MinimumPrefixLength`, `MinimumPopulateDelay`, `IsDropDownOpen`)
- `CalendarDatePicker` (`SelectedDate`, `DisplayDateStart`, `DisplayDateEnd`, `Watermark`)
- `DatePicker` (`SelectedDate`, `MinYear`, `MaxYear`)
- `TimePicker` (`SelectedTime`, `MinuteIncrement`, `ClockIdentifier`, `UseSeconds`)
- `MaskedTextBox` (`Mask`, `PromptChar`, `AsciiOnly`, `MaskCompleted`)
- `NumericUpDown` (`Value`, `Minimum`, `Maximum`, `Increment`, `FormatString`, `AllowSpin`)

Reference docs:

- [`04-html-forms-input-and-validation-to-avalonia-controls.md`](04-html-forms-input-and-validation-to-avalonia-controls)
- [`22-validation-pipeline-and-data-errors.md`](../22-validation-pipeline-and-data-errors)
- [`controls/auto-complete-box.md`](../controls/auto-complete-box)
- [`controls/numeric-up-down.md`](../controls/numeric-up-down)

## Mapping Table

| HTML/CSS idiom | Avalonia mapping |
|---|---|
| `<input list="cities">` + `<datalist>` | `AutoCompleteBox ItemsSource` |
| `<input type="date">` | `CalendarDatePicker` or `DatePicker` |
| `<input type="time">` | `TimePicker` |
| `<input pattern="...">` (strict format) | `MaskedTextBox Mask` |
| `<input type="number" min max step>` | `NumericUpDown Minimum/Maximum/Increment` |

## Search Suggestion Pattern (`datalist` to `AutoCompleteBox`)

HTML/CSS:

```html
<label for="city">City</label>
<input id="city" list="city-list" autocomplete="off" />
<datalist id="city-list">
  <option value="Warsaw"></option>
  <option value="Berlin"></option>
  <option value="Tokyo"></option>
</datalist>
```

```xaml
<StackPanel Spacing="6">
  <TextBlock Text="City" />
  <AutoCompleteBox ItemsSource="{CompiledBinding CityOptions}"
                   Text="{CompiledBinding City, Mode=TwoWay}"
                   MinimumPrefixLength="1"
                   MinimumPopulateDelay="0:0:0.12" />
</StackPanel>
```

## Date/Time Input Pattern

HTML/CSS:

```html
<label for="start-date">Start Date</label>
<input id="start-date" type="date" />

<label for="start-time">Start Time</label>
<input id="start-time" type="time" step="300" />
```

Avalonia options:

```xaml
<StackPanel Spacing="8">
  <CalendarDatePicker SelectedDate="{CompiledBinding StartDate, Mode=TwoWay}"
                      DisplayDateStart="2025-01-01"
                      DisplayDateEnd="2030-12-31"
                      Watermark="Pick a date" />

  <TimePicker SelectedTime="{CompiledBinding StartTime, Mode=TwoWay}"
              MinuteIncrement="5"
              ClockIdentifier="24HourClock"
              UseSeconds="False" />
</StackPanel>
```

`DatePicker` is useful when separate day/month/year selectors are preferred:

```xaml
<DatePicker SelectedDate="{CompiledBinding StartDateOffset, Mode=TwoWay}"
            MinYear="2025-01-01"
            MaxYear="2030-12-31" />
```

## Masked and Numeric Input Pattern

HTML/CSS baseline:

```html
<label for="phone">Phone</label>
<input id="phone" type="tel" placeholder="+48 (___) ___-___" />

<label for="seats">Seats</label>
<input id="seats" type="number" min="1" max="100" step="1" />
```

Avalonia:

```xaml
<StackPanel Spacing="8">
  <MaskedTextBox Mask="+00 (000) 000-000"
                 PromptChar="_"
                 Text="{CompiledBinding Phone, Mode=TwoWay}" />

  <NumericUpDown Minimum="1"
                 Maximum="100"
                 Increment="1"
                 FormatString="N0"
                 Value="{CompiledBinding Seats, Mode=TwoWay}" />
</StackPanel>
```

## Conversion Example: Scheduling Form

```html
<form class="schedule-form">
  <label>Destination</label>
  <input list="destinations" />

  <label>Departure date</label>
  <input type="date" />

  <label>Departure time</label>
  <input type="time" step="900" />

  <label>Emergency phone</label>
  <input type="tel" />

  <label>Passengers</label>
  <input type="number" min="1" max="12" step="1" />
</form>
```

```css
.schedule-form {
  display: grid;
  gap: 10px;
  max-inline-size: 420px;
}
```

```xaml
<StackPanel Spacing="10" MaxWidth="420">
  <TextBlock Text="Destination" />
  <AutoCompleteBox ItemsSource="{CompiledBinding DestinationOptions}"
                   Text="{CompiledBinding Destination, Mode=TwoWay}"
                   MinimumPrefixLength="1" />

  <TextBlock Text="Departure date" />
  <CalendarDatePicker SelectedDate="{CompiledBinding DepartureDate, Mode=TwoWay}"
                      Watermark="Pick a date" />

  <TextBlock Text="Departure time" />
  <TimePicker SelectedTime="{CompiledBinding DepartureTime, Mode=TwoWay}"
              MinuteIncrement="15"
              ClockIdentifier="24HourClock" />

  <TextBlock Text="Emergency phone" />
  <MaskedTextBox Mask="+00 (000) 000-000"
                 Text="{CompiledBinding EmergencyPhone, Mode=TwoWay}" />

  <TextBlock Text="Passengers" />
  <NumericUpDown Minimum="1"
                 Maximum="12"
                 Increment="1"
                 Value="{CompiledBinding Passengers, Mode=TwoWay}" />
</StackPanel>
```

## C# Equivalent: Scheduling Form

```csharp
using System;
using Avalonia.Controls;

var form = new StackPanel
{
    Spacing = 10,
    MaxWidth = 420
};

var destination = new AutoCompleteBox
{
    ItemsSource = new[] { "Warsaw", "Berlin", "Tokyo", "New York" },
    MinimumPrefixLength = 1,
    MinimumPopulateDelay = TimeSpan.FromMilliseconds(120)
};

var departureDate = new CalendarDatePicker
{
    SelectedDate = DateTime.Today,
    Watermark = "Pick a date"
};

var departureTime = new TimePicker
{
    SelectedTime = new TimeSpan(9, 0, 0),
    MinuteIncrement = 15,
    ClockIdentifier = "24HourClock"
};

var phone = new MaskedTextBox
{
    Mask = "+00 (000) 000-000",
    PromptChar = '_'
};

var passengers = new NumericUpDown
{
    Minimum = 1,
    Maximum = 12,
    Increment = 1,
    Value = 1,
    FormatString = "N0"
};

form.Children.Add(new TextBlock { Text = "Destination" });
form.Children.Add(destination);
form.Children.Add(new TextBlock { Text = "Departure date" });
form.Children.Add(departureDate);
form.Children.Add(new TextBlock { Text = "Departure time" });
form.Children.Add(departureTime);
form.Children.Add(new TextBlock { Text = "Emergency phone" });
form.Children.Add(phone);
form.Children.Add(new TextBlock { Text = "Passengers" });
form.Children.Add(passengers);
```

## AOT/Threading Notes

- Keep value types explicit in view models (`DateTime?`, `DateTimeOffset?`, `TimeSpan?`, `decimal?`).
- For async lookup in `AutoCompleteBox`, debounce in VM/service and update bound collections on `Dispatcher.UIThread`.

## Troubleshooting

1. AutoComplete dropdown is empty.
- Confirm `ItemsSource` is populated and `MinimumPrefixLength` is not too high.

2. Date values do not round-trip.
- Use compatible types (`DateTime?` for `CalendarDatePicker`, `DateTimeOffset?` for `DatePicker`).

3. NumericUpDown rejects typed value.
- Check `FormatString`, parsing culture, and min/max constraints.

4. Masked input never reports complete state.
- Validate that `Mask` covers the full expected user input format.
