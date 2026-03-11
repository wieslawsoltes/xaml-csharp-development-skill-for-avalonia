# Responsive Layout, Density, and Stateful Feedback in Avalonia

## Table of Contents
1. Scope and Primary APIs
2. Responsive Host Pattern
3. Density Strategy
4. Loading, Empty, and Error States
5. AOT and Performance Notes
6. Do and Don't Guidance
7. Troubleshooting
8. Official Resources

## Scope and Primary APIs

Use this reference for adaptive shells, density control, and high-quality loading or error states.

Primary APIs:
- `Grid`, `UniformGrid`, `SplitView`, `ScrollViewer`
- `ContainerQuery`, `Container.SetName(...)`, `Container.SetSizing(...)`, `ContainerSizing`
- `Classes`
- `ProgressBar`, `TransitioningContentControl`, `RefreshContainer`

## Responsive Host Pattern

```xml
<Grid xmlns="https://github.com/avaloniaui"
      xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
      x:Name="Root"
      Container.Name="ShellHost"
      Container.Sizing="Width">
  <Grid.Styles>
    <ContainerQuery Name="ShellHost" Query="max-width:720">
      <Style Selector="UniformGrid#CardGrid">
        <Setter Property="Columns" Value="1" />
      </Style>
    </ContainerQuery>
    <ContainerQuery Name="ShellHost" Query="min-width:721 and max-width:1100">
      <Style Selector="UniformGrid#CardGrid">
        <Setter Property="Columns" Value="2" />
      </Style>
    </ContainerQuery>
    <ContainerQuery Name="ShellHost" Query="min-width:1101">
      <Style Selector="UniformGrid#CardGrid">
        <Setter Property="Columns" Value="3" />
      </Style>
    </ContainerQuery>
  </Grid.Styles>

  <UniformGrid x:Name="CardGrid" Columns="3" />
</Grid>
```

## Density Strategy

- Tighten padding and row heights before shrinking type.
- Let density be a tokenized mode, not a one-off patch.
- Keep primary actions and titles readable in all density modes.

## Loading, Empty, and Error States

```xml
<StackPanel xmlns="https://github.com/avaloniaui"
            xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
            Spacing="12">
  <ProgressBar IsIndeterminate="True"
               IsVisible="{CompiledBinding IsLoading}" />

  <TextBlock Text="No incidents found"
             IsVisible="{CompiledBinding IsEmpty}" />

  <Border Classes.error="{CompiledBinding HasError}"
          IsVisible="{CompiledBinding HasError}"
          Padding="12">
    <TextBlock Text="{CompiledBinding ErrorMessage}" />
  </Border>
</StackPanel>
```

Guidance:
- loading copy should explain what is happening,
- empty states should suggest the next useful action,
- error states should be specific and recoverable.

## AOT and Performance Notes

- Prefer class toggles, viewmodel state, and container queries over runtime template swapping.
- Keep loading surfaces simple in virtualized regions.

## Do and Don't Guidance

Do:
- adapt layout by container width rather than window width alone,
- define explicit empty and error treatments,
- keep density modes deliberate and limited.

Do not:
- rely on only color for error communication,
- overfit many breakpoint ranges,
- use busy skeletons for simple waits.

## Troubleshooting

1. Container query styles never activate.
- Confirm both `Container.Name` and `Container.Sizing` are set on the intended host.

2. Compact mode feels broken.
- Revisit padding and spacing tokens first; do not treat density as only a font-size reduction.

3. Empty and error states feel disconnected.
- Theme them with the same token system as normal surfaces.

## Official Resources

- Avalonia container queries: [docs.avaloniaui.net/docs/basics/user-interface/styling/container-queries](https://docs.avaloniaui.net/docs/basics/user-interface/styling/container-queries)
- Fluent 2 layout: [fluent2.microsoft.design/layout](https://fluent2.microsoft.design/layout)
- Fluent 2 wait UX: [fluent2.microsoft.design/wait-ux](https://fluent2.microsoft.design/wait-ux)
- Fluent 2 onboarding: [fluent2.microsoft.design/onboarding](https://fluent2.microsoft.design/onboarding/)
