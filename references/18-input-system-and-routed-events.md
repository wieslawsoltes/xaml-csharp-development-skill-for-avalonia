# Input System and Routed Events

## Table of Contents
1. Scope and APIs
2. Input and Routing Flow
3. Routed Event Metadata and Diagnostics
4. Authoring Patterns
5. Best Practices
6. Troubleshooting

## Scope and APIs

Primary APIs:
- `Interactive`
- `RoutedEvent` and `RoutedEvent<TEventArgs>`
- `RoutingStrategies`
- `RoutedEventArgs`
- `EventRoute`
- `RoutedEventRegistry`
- `InputElement`
- `PointerEventArgs`, `PointerPressedEventArgs`, `PointerReleasedEventArgs`
- `KeyEventArgs`
- `Gestures`
- `InteractiveExtensions`

Important members:
- `Interactive.AddHandler(...)`, `RemoveHandler(...)`, `RaiseEvent(...)`
- `RoutedEvent.Register<TOwner, TEventArgs>(...)`
- `RoutedEvent.AddClassHandler(...)`
- `RoutedEvent.EventArgsType`, `RoutedEvent.HasRaisedSubscriptions`
- `RoutedEvent.Raised`, `RoutedEvent.RouteFinished`
- `RoutedEventArgs.Handled`, `Route`, `Source`, `RoutedEvent`
- `CancelRoutedEventArgs`, `CancelRoutedEventArgs.Cancel`
- `InputElement.KeyDownEvent`, `KeyUpEvent`, `TextInputEvent`
- `InputElement.PointerPressedEvent`, `PointerMovedEvent`, `PointerReleasedEvent`, `PointerWheelChangedEvent`
- `PointerEventArgs.GetPosition(...)`, `GetCurrentPoint(...)`, `PreventGestureRecognition()`
- `Gestures.TappedEvent`, `DoubleTappedEvent`, `HoldingEvent`, `PinchEvent`, `ScrollGestureEvent`
- `EventRoute.HasHandlers`
- `RoutedEventRegistry.GetAllRegistered()`
- `InteractiveExtensions.GetObservable(...)`, `AddDisposableHandler(...)`, `GetInteractiveParent()`

Reference source files:
- `src/Avalonia.Base/Interactivity/Interactive.cs`
- `src/Avalonia.Base/Interactivity/RoutedEvent.cs`
- `src/Avalonia.Base/Interactivity/RoutedEventArgs.cs`
- `src/Avalonia.Base/Interactivity/EventRoute.cs`
- `src/Avalonia.Base/Interactivity/RoutedEventRegistry.cs`
- `src/Avalonia.Base/Interactivity/InteractiveExtensions.cs`
- `src/Avalonia.Base/Input/InputElement.cs`
- `src/Avalonia.Base/Input/PointerEventArgs.cs`
- `src/Avalonia.Base/Input/KeyEventArgs.cs`
- `src/Avalonia.Base/Input/Gestures.cs`

Version note:
- this stable reference reflects the `11.3.12` public input surface,
- for Avalonia 12 migration, see [`68-avalonia-12-migration-guide.md`](68-avalonia-12-migration-guide) because public gesture events move off the `Gestures` class onto `InputElement`, and touch/pen selection behavior changes.

## Input and Routing Flow

Runtime flow in app code:
1. Platform sends raw input.
2. Input is translated to Avalonia routed input events.
3. Event route is built (`Direct`, `Tunnel`, `Bubble`).
4. Class handlers run first, then instance handlers.
5. `Handled` controls downstream processing.

Routing strategy quick guide:
- `Direct`: source only.
- `Tunnel`: root to source.
- `Bubble`: source to root.

Use `Tunnel` for interception, `Bubble` for normal control-level handling.

## Routed Event Metadata and Diagnostics

Use routed-event metadata APIs when auditing event topology in larger control trees:

- `RoutedEvent.EventArgsType` lets you validate event-args contracts before wiring generic handlers.
- `RoutedEvent.HasRaisedSubscriptions` tells you whether `RoutedEvent.Raised` has observers.
- `RoutedEventRegistry.Instance.GetAllRegistered()` gives a global routed-event inventory for diagnostics.
- `InteractiveExtensions.GetInteractiveParent()` is a fast parent hop for event-path inspection on `Interactive`.

Example diagnostics pass:

```csharp
using Avalonia.Interactivity;

foreach (var routedEvent in RoutedEventRegistry.Instance.GetAllRegistered())
{
    _logger.Debug(
        "Event={Name}, Owner={Owner}, Args={Args}, HasRaisedSubscribers={HasSubscribers}",
        routedEvent.Name,
        routedEvent.OwnerType.Name,
        routedEvent.EventArgsType.Name,
        routedEvent.HasRaisedSubscriptions);
}
```

You can instrument one routed event to inspect route activity:

```csharp
using Avalonia.Interactivity;

IDisposable raisedSub = InputElement.PointerPressedEvent.Raised
    .Subscribe(tuple =>
    {
        (object sender, RoutedEventArgs args) = tuple;
        _ = sender;
        _ = args.Route;
    });

IDisposable finishedSub = InputElement.PointerPressedEvent.RouteFinished
    .Subscribe(args => _ = args.Handled);
```

`CancelRoutedEventArgs` is the canonical cancelable routed-event args type. Constructor forms:

- `new CancelRoutedEventArgs()`
- `new CancelRoutedEventArgs(routedEvent)`
- `new CancelRoutedEventArgs(routedEvent, source)`

Cancelable custom event pattern:

```csharp
using Avalonia.Interactivity;

public class DocumentHost : Avalonia.Controls.Control
{
    public static readonly RoutedEvent<CancelRoutedEventArgs> BeforeCloseEvent =
        RoutedEvent.Register<DocumentHost, CancelRoutedEventArgs>(
            nameof(BeforeClose),
            RoutingStrategies.Bubble);

    public event EventHandler<CancelRoutedEventArgs>? BeforeClose
    {
        add => AddHandler(BeforeCloseEvent, value);
        remove => RemoveHandler(BeforeCloseEvent, value);
    }

    public bool RequestClose()
    {
        var args = new CancelRoutedEventArgs(BeforeCloseEvent, this);
        RaiseEvent(args);
        return !args.Cancel;
    }
}
```

Low-level route creation with `EventRoute` is uncommon in app code, but when used:

- use `EventRoute.HasHandlers` before raising work-heavy payloads,
- dispose routes quickly to release pooled buffers.

## Authoring Patterns

### Custom routed event

```csharp
using Avalonia.Interactivity;

public class CommitPanel : Avalonia.Controls.Control
{
    public static readonly RoutedEvent<RoutedEventArgs> CommitRequestedEvent =
        RoutedEvent.Register<CommitPanel, RoutedEventArgs>(
            nameof(CommitRequested),
            RoutingStrategies.Bubble);

    public event EventHandler<RoutedEventArgs>? CommitRequested
    {
        add => AddHandler(CommitRequestedEvent, value);
        remove => RemoveHandler(CommitRequestedEvent, value);
    }

    protected void RaiseCommitRequested()
    {
        RaiseEvent(new RoutedEventArgs(CommitRequestedEvent));
    }
}
```

### Intercept in tunnel and keep bubbling intact when needed

```csharp
root.AddHandler(
    Avalonia.Input.InputElement.PointerPressedEvent,
    (sender, e) =>
    {
        if (ShouldBlockPointer(e))
            e.Handled = true;
    },
    RoutingStrategies.Tunnel,
    handledEventsToo: false);
```

### Reactive subscription to routed events

```csharp
using Avalonia.Interactivity;

IDisposable sub = myControl
    .GetObservable(Avalonia.Input.InputElement.KeyDownEvent)
    .Subscribe(e => HandleKey(e));
```

### Pointer details

```csharp
void OnPointerPressed(object? sender, Avalonia.Input.PointerPressedEventArgs e)
{
    var point = e.GetCurrentPoint((Avalonia.Visual)e.Source!);
    if (point.Properties.IsLeftButtonPressed)
    {
        // Use point.Position and modifiers for deterministic handling.
    }
}
```

## Best Practices

- Register custom routed events once as `static readonly`.
- Keep input handlers small; dispatch to command or state methods.
- Use `Tunnel` only for pre-filtering and guard logic.
- Avoid global handlers with `handledEventsToo: true` unless truly required.
- Prefer typed `AddHandler<TEventArgs>` overloads for maintainability.
- For gesture-heavy controls, use built-in gesture events/recognizers instead of reimplementing them.
- On `11.3.12`, that usually means the public `Gestures` surface; on Avalonia 12, the public routed events move to `InputElement`.
- In tests, prefer headless input simulation APIs over directly constructing pointer/key event args.

## Troubleshooting

1. Event never fires:
- Wrong routing strategy or wrong routed event instance.
- Control is not hit-testable (`IsHitTestVisible = false`) or disabled.

2. Event fires but handler never runs:
- Upstream handler set `Handled = true`.
- Your handler was added without `handledEventsToo` where needed.

3. Gesture events not appearing:
- Gesture recognition may be skipped (`PreventGestureRecognition`).
- Pointer lifecycle is incomplete (press without move/release path).

4. Duplicate handling:
- Same handler attached both as class handler and instance handler.
- Both `Tunnel` and `Bubble` are subscribed without guards.

## XAML-First and Code-Only Usage

Default mode:
- Declare interaction wiring in XAML first (events, gestures, key bindings).
- Use pure code-only handler wiring only when requested.

XAML-first references:
- Routed event handlers in XAML attributes
- `KeyBinding` collections in XAML

XAML-first usage example:

```xml
<UserControl xmlns="https://github.com/avaloniaui"
             xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
             x:Class="MyApp.Views.EditorView"
             PointerPressed="OnPointerPressed"
             KeyDown="OnKeyDown">
  <UserControl.KeyBindings>
    <KeyBinding Gesture="Ctrl+Enter" Command="{Binding CommitCommand}" />
  </UserControl.KeyBindings>
</UserControl>
```

Code-only alternative (on request):

```csharp
AddHandler(InputElement.PointerPressedEvent, OnPointerPressed, RoutingStrategies.Bubble);
AddHandler(InputElement.KeyDownEvent, OnKeyDown, RoutingStrategies.Bubble);
```
