# WinForms Date/Time and Calendar Controls to Avalonia

## Table of Contents
1. Scope and APIs
2. Date/Time Mapping
3. Conversion Example
4. C# Equivalent
5. Troubleshooting

## Scope and APIs

Primary WinForms APIs:

- `DateTimePicker`
- `MonthCalendar`

Primary Avalonia APIs:

- `CalendarDatePicker`
- `DatePicker`
- `TimePicker`
- `Calendar`

## Date/Time Mapping

| WinForms | Avalonia |
|---|---|
| `DateTimePicker` (date) | `CalendarDatePicker` (`DateTime?`) or `DatePicker` (`DateTimeOffset?`) |
| `DateTimePicker` (time via `ShowUpDown`) | `TimePicker` |
| `MonthCalendar` | `Calendar` |
| `MinDate`/`MaxDate` constraints | `CalendarDatePicker.DisplayDateStart/DisplayDateEnd` or `DatePicker.MinYear/MaxYear` |

## Conversion Example

WinForms C#:

```csharp
var dueDate = new DateTimePicker
{
    Format = DateTimePickerFormat.Short,
    Value = DateTime.Today
};

var dueTime = new DateTimePicker
{
    Format = DateTimePickerFormat.Time,
    ShowUpDown = true,
    Value = DateTime.Now
};

var month = new MonthCalendar { MaxSelectionCount = 1 };
```

Avalonia XAML:

```xaml
<UserControl xmlns="https://github.com/avaloniaui"
             xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
             xmlns:vm="using:MyApp.ViewModels"
             x:DataType="vm:ScheduleViewModel">
  <Grid RowDefinitions="Auto,Auto,Auto,*" RowSpacing="8">
    <DatePicker Grid.Row="0"
                MinYear="{CompiledBinding MinDateOffset}"
                MaxYear="{CompiledBinding MaxDateOffset}"
                SelectedDate="{CompiledBinding SelectedDateOffset, Mode=TwoWay}" />

    <CalendarDatePicker Grid.Row="1"
                        DisplayDateStart="{CompiledBinding MinDate}"
                        DisplayDateEnd="{CompiledBinding MaxDate}"
                        SelectedDate="{CompiledBinding SelectedDate, Mode=TwoWay}" />

    <TimePicker Grid.Row="2"
                SelectedTime="{CompiledBinding SelectedTime, Mode=TwoWay}" />

    <Calendar Grid.Row="3"
              SelectedDate="{CompiledBinding SelectedDate, Mode=TwoWay}"
              SelectionMode="SingleDate" />
  </Grid>
</UserControl>
```

## C# Equivalent

```csharp
using System;
using Avalonia.Controls;

var dueDateOffset = new DatePicker
{
    MinYear = new DateTimeOffset(2025, 1, 1, 0, 0, 0, TimeSpan.Zero),
    MaxYear = new DateTimeOffset(2030, 12, 31, 0, 0, 0, TimeSpan.Zero),
    SelectedDate = DateTimeOffset.Now
};

var dueDate = new CalendarDatePicker
{
    DisplayDateStart = DateTime.Today.AddYears(-1),
    DisplayDateEnd = DateTime.Today.AddYears(1),
    SelectedDate = DateTime.Today
};

var dueTime = new TimePicker
{
    SelectedTime = TimeSpan.FromHours(9)
};

var month = new Calendar
{
    SelectionMode = CalendarSelectionMode.SingleDate,
    SelectedDate = DateTime.Today
};
```

## Troubleshooting

1. Date/time value conversions become inconsistent.
- map `DateTime?` and `DateTimeOffset?` deliberately per control; convert only at clear boundaries.

2. Locale formatting differs from WinForms.
- configure culture/format expectations explicitly in the view-model display layer.

3. Calendar selection mode behaves unexpectedly.
- verify `SelectionMode` and whether your UX expects single or range selection.
