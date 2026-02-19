# WPF Date/Time, Calendar, and Picker Controls to Avalonia

## Table of Contents
1. Scope and APIs
2. Date/Time Mapping
3. Conversion Example
4. Avalonia C# Equivalent
5. Troubleshooting

## Scope and APIs

Primary WPF APIs:

- `DatePicker`
- `Calendar`

Primary Avalonia APIs:

- `CalendarDatePicker`
- `DatePicker`
- `TimePicker`
- `Calendar`

## Date/Time Mapping

| WPF | Avalonia |
|---|---|
| `DatePicker.SelectedDate` (`DateTime?`) | `DatePicker.SelectedDate` (`DateTimeOffset?`) |
| date drop-down bound to `DateTime?` models | `CalendarDatePicker.SelectedDate` (`DateTime?`) |
| date selector with drop-down calendar | `CalendarDatePicker` |
| inline calendar | `Calendar` |
| time selection (custom controls/toolkit in WPF) | built-in `TimePicker` |

## Conversion Example

WPF XAML:

```xaml
<StackPanel>
  <DatePicker SelectedDate="{Binding DueDate, Mode=TwoWay}" />
  <Calendar SelectedDate="{Binding DueDate, Mode=TwoWay}" />
</StackPanel>
```

Avalonia XAML:

```xaml
<UserControl xmlns="https://github.com/avaloniaui"
             xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
             xmlns:vm="using:MyApp.ViewModels"
             x:DataType="vm:ScheduleViewModel">
  <Grid RowDefinitions="Auto,Auto,Auto,*" RowSpacing="8">
    <DatePicker Grid.Row="0"
                SelectedDate="{CompiledBinding DueDateOffset, Mode=TwoWay}" />

    <CalendarDatePicker Grid.Row="1"
                        SelectedDate="{CompiledBinding DueDate, Mode=TwoWay}" />

    <TimePicker Grid.Row="2"
                SelectedTime="{CompiledBinding DueTime, Mode=TwoWay}" />

    <Calendar Grid.Row="3"
              SelectionMode="SingleDate"
              SelectedDate="{CompiledBinding DueDate, Mode=TwoWay}" />
  </Grid>
</UserControl>
```

## Avalonia C# Equivalent

```csharp
using System;
using Avalonia.Controls;

var dateOffset = new DatePicker { SelectedDate = DateTimeOffset.Now };
var date = new CalendarDatePicker { SelectedDate = DateTime.Today };
var time = new TimePicker { SelectedTime = TimeSpan.FromHours(9) };
var calendar = new Calendar
{
    SelectionMode = CalendarSelectionMode.SingleDate,
    SelectedDate = DateTime.Today
};
```

## Troubleshooting

1. Date type conversions become inconsistent.
- normalize model date/time types and map `DateTime?` (calendar-like controls) versus `DateTimeOffset?` (`DatePicker`) explicitly.

2. Time-selection UX differs from legacy WPF flows.
- explicitly design time-entry behavior with `TimePicker` rather than ad-hoc text input.

3. Calendar selection mode surprises users.
- verify `SelectionMode` and communicate single/range semantics clearly.
