# Information Architecture, Navigation, and Progressive Disclosure in Avalonia

## Table of Contents
1. Scope and Primary APIs
2. Information-Architecture Rules
3. Navigation Model Selection
4. Progressive Disclosure Patterns
5. AOT and Runtime Notes
6. Do and Don't Guidance
7. Troubleshooting
8. Official Resources

## Scope and Primary APIs

Use this reference to structure a product so the design system supports task flow, not just styling.

Primary APIs:
- `SplitView`, `TabControl`, `TreeView`, `Expander`
- `ListBox`, `MenuFlyout`, `ContextMenu`
- `TransitioningContentControl`
- `ScrollViewer`, `Grid`, `UniformGrid`
- `Window`, `Flyout`, `ToolTip`

This file covers:
- choosing the right shell model,
- grouping features by task rather than by implementation,
- reducing cognitive load with progressive disclosure,
- keeping navigation patterns stable across desktop workflows.

## Information-Architecture Rules

Structure the app around user goals:

1. Orientation
- users should know where they are and what area they are in.

2. Progress
- each surface should suggest the next sensible action.

3. Scope
- related actions and information stay together.

4. Escalation
- advanced settings and risky actions appear later, not first.

Practical rules:
- organize by workflow or object model, not only by technical modules,
- keep global navigation stable and local actions contextual,
- avoid making every page a dashboard and a settings surface at the same time,
- let layout, headings, and motion communicate depth before chrome does.

## Navigation Model Selection

Use the shell model that matches the product shape:

- `SplitView` for larger products with stable left-rail navigation,
- `TabControl` for peer workspaces or documents,
- `TreeView` for hierarchical content and explorer flows,
- `MenuFlyout` for overflow or contextual actions,
- `Expander` for secondary settings or advanced options.

```xml
<SplitView xmlns="https://github.com/avaloniaui"
           xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
           DisplayMode="Inline"
           IsPaneOpen="True"
           OpenPaneLength="280"
           CompactPaneLength="56">
  <SplitView.Pane>
    <ListBox ItemContainerTheme="{StaticResource NavItemTheme}" />
  </SplitView.Pane>

  <TransitioningContentControl Content="{CompiledBinding CurrentPage}"
                               PageTransition="{StaticResource ShellPageTransition}" />
</SplitView>
```

Choose one primary navigation model per shell. Secondary models should explain local scope, not replace the global model.

## Progressive Disclosure Patterns

Use disclosure to reduce initial complexity:

- show the core path first,
- reveal advanced options only when relevant,
- keep dangerous actions behind an extra layer of intent,
- promote details only when they change the decision.

```xml
<StackPanel xmlns="https://github.com/avaloniaui"
            xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
            Spacing="12">
  <TextBlock Classes="title" Text="Release rollout" />
  <TextBlock Classes="body"
             Text="Choose an environment and confirm the rollout settings." />

  <Expander Header="Advanced rollout options">
    <StackPanel Spacing="8">
      <CheckBox Content="Pause after verification" />
      <CheckBox Content="Notify stakeholders on completion" />
    </StackPanel>
  </Expander>
</StackPanel>
```

Guidance:
- use `Expander` or nested surfaces for advanced detail,
- use `Flyout` for supporting actions that should stay near the trigger,
- use dedicated pages or modal windows for high-risk or high-complexity flows,
- keep the shell consistent when details expand.

## AOT and Runtime Notes

- Keep shell layouts, disclosure patterns, and navigation themes in compiled XAML.
- Prefer stable view composition and page transitions over frequent runtime navigation-template swapping.
- Keep navigation state explicit in the viewmodel so shell transitions remain predictable.

## Do and Don't Guidance

Do:
- choose one dominant shell structure,
- group by task and decision flow,
- use progressive disclosure to lower cognitive load.

Do not:
- mix several primary navigation models in one window,
- expose advanced settings before core actions,
- let overflow menus become the real navigation model.

## Troubleshooting

1. The product feels visually polished but hard to use.
- The problem is likely information architecture, not token quality.

2. Users get lost between pages.
- Rework the shell to make global and local navigation roles more distinct.

3. Advanced options overwhelm simple tasks.
- Move optional controls into disclosure surfaces and re-evaluate the default path.

## Official Resources

- Navigation basics for Windows apps: [learn.microsoft.com/en-us/windows/apps/design/basics/navigation-basics](https://learn.microsoft.com/en-us/windows/apps/design/basics/navigation-basics)
- Content design basics for Windows apps: [learn.microsoft.com/en-us/windows/apps/design/basics/content-basics](https://learn.microsoft.com/en-us/windows/apps/design/basics/content-basics)
- List-details view guidance: [learn.microsoft.com/en-us/windows/apps/design/controls/list-details](https://learn.microsoft.com/en-us/windows/apps/design/controls/list-details)
- Fluent 2 navigation guidance: [fluent2.microsoft.design/components/web/react/core/nav/usage](https://fluent2.microsoft.design/components/web/react/core/nav/usage)
- Fluent 2 tab list guidance: [fluent2.microsoft.design/components/web/react/core/tablist/usage](https://fluent2.microsoft.design/components/web/react/core/tablist/usage)
