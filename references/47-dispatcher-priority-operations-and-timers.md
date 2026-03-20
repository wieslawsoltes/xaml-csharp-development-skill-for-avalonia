# Dispatcher Priority, Operations, and Timers

## Table of Contents
1. Scope and APIs
2. Access and Run-Loop Contract
3. Priority Model and Comparison Semantics
4. Dispatcher Operations and Result Flow
5. Priority Awaitables
6. Main Loop and Nested Frames
7. Timer Patterns
8. Exception Pipeline Types
9. Practical Patterns
10. Troubleshooting

## Scope and APIs

Primary APIs:

- `Dispatcher`
- `DispatcherPriority`
- `DispatcherOptions`
- `DispatcherOperation` / `DispatcherOperation<T>`
- `DispatcherOperationStatus`
- `DispatcherPriorityAwaitable` / `DispatcherPriorityAwaitable<T>`
- `DispatcherTimer`
- `DispatcherFrame`

Related event args/types:

- `DispatcherEventArgs`
- `DispatcherUnhandledExceptionEventArgs`
- `DispatcherUnhandledExceptionFilterEventArgs`

## Access and Run-Loop Contract

Use these APIs to guard thread access and queue flow:

- `CheckAccess()`
- `VerifyAccess()`
- `SupportsRunLoops`
- `RunJobs(...)`
- `HasJobsWithPriority(...)`

Dispatcher starvation tuning surface:

- `DispatcherOptions`
- `DispatcherOptions.InputStarvationTimeout`

Pattern:

```csharp
if (!Dispatcher.UIThread.CheckAccess())
{
    await Dispatcher.UIThread.InvokeAsync(UpdateUi);
    return;
}

Dispatcher.UIThread.VerifyAccess();
UpdateUi();
```

## Priority Model and Comparison Semantics

Useful `DispatcherPriority` members:

- `MaxValue`
- `FromValue(int value)`
- `Validate(priority, parameterName)`
- `CompareTo(...)`
- `Equals(...)`
- `GetHashCode()`
- `SystemIdle`, `Inactive`, `Invalid`
- `UiThreadRender`, `BeforeRender`, `AsyncRenderTargetResize`

Operator semantics are explicit and order-aware:

- `operator ==`
- `operator !=`
- `operator <`
- `operator >`
- `operator <=`
- `operator >=`
- `operator int`
- `operator DispatcherPriority`

Use `DispatcherPriority.Validate(...)` on externally supplied numeric values before scheduling.

## Dispatcher Operations and Result Flow

`InvokeAsync(...)` returns `DispatcherOperation` / `DispatcherOperation<T>`.

Operational members:

- `Status`
- `Priority`
- `Abort()`
- `GetTask()`
- `Wait()`
- `Completed` / `Aborted`

Typed operation result and state APIs:

- `Result`
- `DispatcherOperation<T>.Result`
- `DispatcherOperationStatus`

Pattern:

```csharp
var op = Dispatcher.UIThread.InvokeAsync(
    () => ComputeUiResult(),
    DispatcherPriority.Background);

await op.GetTask();
if (op.Status == DispatcherOperationStatus.Completed)
{
    var value = op.Result;
    _ = value;
}
```

Guidance:

- prefer `await op.GetTask()` in async flows,
- use `Wait()` only for narrow synchronous boundaries.
- Avalonia 12 migration note: app code can still use `Dispatcher.UIThread`, but library and control code should prefer `AvaloniaObject.Dispatcher` or `Dispatcher.CurrentDispatcher` for multi-dispatcher awareness. See [`68-avalonia-12-migration-guide.md`](68-avalonia-12-migration-guide).

## Priority Awaitables

`DispatcherPriorityAwaitable` APIs:

- `OnCompleted(...)`
- `IsCompleted`
- `GetResult()`

Generic variant:

- `DispatcherPriorityAwaitable<T>`
- `DispatcherPriorityAwaitable<T>.GetResult()`

These are used by `AwaitWithPriority(...)` paths to continue on the dispatcher with a selected priority.

## Main Loop and Nested Frames

Main-loop control APIs:

- `ShutdownStarted`
- `ShutdownFinished`
- `PushFrame(DispatcherFrame frame)`
- `ExitAllFrames()`
- `DisableProcessing()`
- `DispatcherProcessingDisabled`

Nested-frame type:

- `DispatcherFrame`
- `DispatcherFrame.Continue`

Use nested frames sparingly; they can re-enter app code and complicate invariants.

## Timer Patterns

`DispatcherTimer` constructors and members:

- `DispatcherTimer()`
- `DispatcherTimer(DispatcherPriority priority)`
- `DispatcherTimer(TimeSpan interval, DispatcherPriority priority, EventHandler callback)`
- `Tag`
- `Tick`
- `Start()`, `Stop()`
- `Run(...)`, `RunOnce(...)`

Pattern:

```csharp
var timer = new DispatcherTimer(TimeSpan.FromSeconds(1), DispatcherPriority.Background, (_, _) =>
{
    RefreshClock();
});

timer.Tag = "clock";
timer.Start();
```

## Exception Pipeline Types

Dispatcher exception flow uses:

- `DispatcherEventArgs`
- `DispatcherUnhandledExceptionEventArgs`
- `DispatcherUnhandledExceptionFilterEventArgs`
- `DispatcherUnhandledExceptionFilterEventArgs.RequestCatch`

Use handlers for telemetry and controlled fallback, not normal branching.

## Practical Patterns

1. Queue non-critical UI updates at `Background`.
- Keeps input/render queues responsive.

2. Keep priority explicit in shared infrastructure.
- Avoid hidden default-priority behavior in utility methods.

3. Use `RunJobs(...)` only in controlled test/simulation paths.
- Avoid forcing queue execution in production request paths.

4. Dispose timer subscriptions and stop timers during teardown.
- Prevent stale callbacks after view or window close.

## Troubleshooting

1. UI updates intermittently fail.
- Verify `CheckAccess()`/`VerifyAccess()` usage and queued priority.

2. Operation appears stuck.
- Inspect `DispatcherOperationStatus` and whether the dispatcher run loop is active.

3. Priority inversion symptoms.
- Audit for overuse of high priorities and compare with `HasJobsWithPriority(...)`.

4. Re-entrancy bugs after modal/test helpers.
- Check `PushFrame(...)` usage and ensure `ExitAllFrames()` is called in shutdown paths.
