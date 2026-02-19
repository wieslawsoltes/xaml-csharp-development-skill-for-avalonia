# WPF CollectionView Group/Sort/Filter to Avalonia Patterns

## Table of Contents
1. Scope and APIs
2. Collection Shaping Mapping
3. Conversion Example
4. Avalonia C# Equivalent
5. Troubleshooting

## Scope and APIs

Primary WPF APIs:

- `CollectionViewSource`
- `ICollectionView` sorting/filtering/grouping

Primary Avalonia patterns:

- view-model projection lists for filter/sort/group state
- item controls (`ListBox`, `TreeView`, optional external `DataGrid` package)
- explicit query state in view-models instead of implicit view-side filters

## Collection Shaping Mapping

| WPF | Avalonia |
|---|---|
| `CollectionViewSource.View.Filter` | view-model predicate and projected collection |
| `SortDescriptions` | view-model sort state and projected ordering |
| grouping in `CollectionView` | grouped view-model collections + templates |

## Conversion Example

WPF C#:

```csharp
CollectionView view = (CollectionView)CollectionViewSource.GetDefaultView(Items);
view.Filter = item => ((Customer)item).IsActive;
view.SortDescriptions.Add(new SortDescription(nameof(Customer.Name), ListSortDirection.Ascending));
```

Avalonia XAML:

```xaml
<StackPanel xmlns="https://github.com/avaloniaui"
            xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
            xmlns:vm="using:MyApp.ViewModels"
            x:DataType="vm:CustomersViewModel"
            Spacing="8">
  <TextBox Watermark="Filter" Text="{CompiledBinding Query, Mode=TwoWay}" />
  <ListBox ItemsSource="{CompiledBinding VisibleCustomers}" />
</StackPanel>
```

## Avalonia C# Equivalent

```csharp
using System;
using System.Collections.ObjectModel;
using System.Linq;

public sealed class CustomersViewModel
{
    public ObservableCollection<Customer> AllCustomers { get; } = new();
    public ObservableCollection<Customer> VisibleCustomers { get; } = new();

    public void Refresh(string query)
    {
        var filtered = AllCustomers
            .Where(x => x.IsActive)
            .Where(x => string.IsNullOrWhiteSpace(query) || x.Name.Contains(query, StringComparison.OrdinalIgnoreCase))
            .OrderBy(x => x.Name)
            .ToList();

        VisibleCustomers.Clear();
        foreach (var item in filtered)
            VisibleCustomers.Add(item);
    }
}
```

## Troubleshooting

1. Filtering logic spread across view and model.
- keep sort/filter state explicit in view-model properties.

2. grouping output is unstable.
- model groups as explicit objects and template them directly.

3. very large collections stutter on every keystroke.
- debounce query updates and reduce full-collection recomputation.
