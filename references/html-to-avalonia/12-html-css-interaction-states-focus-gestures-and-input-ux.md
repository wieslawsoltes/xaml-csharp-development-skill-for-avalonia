# HTML/CSS Interaction States, Focus, Gestures, and Input UX in Avalonia

## Table of Contents
1. Scope and APIs
2. State Mapping (`hover`/`active`/`focus`)
3. Focus-Visible and Keyboard UX Mapping
4. Gesture/Event Mapping
5. Conversion Example: Interactive Command Bar
6. C# Equivalent: Interactive Command Bar
7. Accessibility and Reduced-Motion Integration
8. Troubleshooting

## Scope and APIs

Primary APIs:

- pseudo-classes: `:pointerover`, `:pressed`, `:focus`, `:disabled`
- input routing: routed events, `KeyBinding`, `HotKeyManager`
- gestures: tap/double-tap/holding/pinch/pull/scroll gesture events
- focus management APIs and keyboard navigation patterns

Reference docs:

- [`18-input-system-and-routed-events.md`](../18-input-system-and-routed-events)
- [`19-focus-and-keyboard-navigation.md`](../19-focus-and-keyboard-navigation)
- [`24-commands-hotkeys-and-gestures.md`](../24-commands-hotkeys-and-gestures)

## State Mapping (`hover`/`active`/`focus`)

| HTML/CSS | Avalonia |
|---|---|
| `:hover` | `:pointerover` |
| `:active` | `:pressed` |
| `:focus` | `:focus` |
| `:disabled` | `:disabled` |

HTML/CSS:

```css
.btn:hover { background:#3355cc; }
.btn:active { transform: scale(.98); }
.btn:disabled { opacity:.45; cursor:not-allowed; }
```

Avalonia:

```xaml
<Style Selector="Button.btn:pointerover">
  <Setter Property="Background" Value="#3355CC" />
</Style>
<Style Selector="Button.btn:pressed">
  <Setter Property="RenderTransform" Value="scale(0.98)" />
</Style>
<Style Selector="Button.btn:disabled">
  <Setter Property="Opacity" Value="0.45" />
</Style>
```

## Focus-Visible and Keyboard UX Mapping

Web idiom:

```css
.btn:focus-visible { outline: 2px solid #67a3ff; outline-offset: 2px; }
```

Avalonia pattern:

- provide explicit focus style,
- ensure keyboard-only navigation paths are testable,
- use consistent focus visual treatment across controls.

```xaml
<Style Selector="Button.btn:focus">
  <Setter Property="BorderBrush" Value="#67A3FF" />
  <Setter Property="BorderThickness" Value="2" />
</Style>
```

## Gesture/Event Mapping

| Web interaction | Avalonia mapping |
|---|---|
| click | `Button.Command` / routed `Click` |
| dblclick | `DoubleTapped` |
| contextmenu | `ContextMenu` / right tap |
| pointerdown/up/move | pointer/routed input events |
| keyboard shortcut | `KeyBinding` / `HotKeyManager` |

Minimal command + hotkey example:

```xaml
<Button Classes="btn" Content="Refresh" Command="{CompiledBinding RefreshCommand}" />
```

```csharp
HotKeyManager.SetHotKey(myButton, new KeyGesture(Key.R, KeyModifiers.Control));
```

## Conversion Example: Interactive Command Bar

HTML/CSS:

```html
<div class="cmdbar">
  <button class="btn">Search</button>
  <button class="btn">Filter</button>
  <button class="btn primary">Apply</button>
</div>
```

```css
.cmdbar { display:flex; gap:8px; }
.btn { transition: background .12s ease, transform .12s ease; }
```

Avalonia:

```xaml
<StackPanel Orientation="Horizontal" Spacing="8">
  <Button Classes="btn" Content="Search" />
  <Button Classes="btn" Content="Filter" />
  <Button Classes="btn primary" Content="Apply" Command="{CompiledBinding ApplyCommand}" />
</StackPanel>
```

## C# Equivalent: Interactive Command Bar

```csharp
using Avalonia.Controls;
using Avalonia.Input;

var commandBar = new StackPanel
{
    Orientation = Avalonia.Layout.Orientation.Horizontal,
    Spacing = 8
};

var searchButton = new Button { Content = "Search" };
var filterButton = new Button { Content = "Filter" };
var applyButton = new Button { Content = "Apply" };
HotKeyManager.SetHotKey(applyButton, new KeyGesture(Key.Enter, KeyModifiers.Control));

commandBar.Children.Add(searchButton);
commandBar.Children.Add(filterButton);
commandBar.Children.Add(applyButton);
```

## Accessibility and Reduced-Motion Integration

- Ensure pointer-only states are not the only affordance; keep focus styles visible.
- Pair interaction transitions with reduced-motion class policies.

## Troubleshooting

1. Hover styles never apply on touch targets.
- Use pressed/focus/selection states for touch-first UX.

2. Keyboard shortcuts conflict.
- Centralize `KeyBinding` policies and avoid duplicate gestures.

3. Focus ring not visible on dark themes.
- Use theme-aware focus colors from resource dictionaries.
