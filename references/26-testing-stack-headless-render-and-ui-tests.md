# Testing Stack: Headless, Render, and UI Tests

## Table of Contents
1. Scope and APIs
2. Test Runtime Architecture
3. Authoring Patterns
4. AOT-Safe Testing Guidance
5. Troubleshooting

## Scope and APIs

Primary APIs:
- `AvaloniaHeadlessPlatformExtensions.UseHeadless(...)`
- `AvaloniaHeadlessPlatformOptions`
- `AvaloniaHeadlessPlatform.ForceRenderTimerTick(...)`
- `HeadlessWindowExtensions`
- `HeadlessUnitTestSession`
- `AvaloniaTestApplicationAttribute`
- `AvaloniaTestIsolationAttribute`
- `AvaloniaTestIsolationLevel`
- `Avalonia.Headless.NUnit.AvaloniaTestAttribute`
- `Avalonia.Headless.XUnit.AvaloniaFactAttribute`
- `Avalonia.Headless.XUnit.AvaloniaTheoryAttribute`

Important members:
- `AvaloniaHeadlessPlatformOptions.UseHeadlessDrawing`
- `AvaloniaHeadlessPlatformOptions.FrameBufferFormat`
- `TopLevel.CaptureRenderedFrame()`
- `TopLevel.GetLastRenderedFrame()`
- `TopLevel.KeyPress(...)`, `KeyRelease(...)`, `KeyTextInput(...)`
- `TopLevel.MouseDown(...)`, `MouseMove(...)`, `MouseUp(...)`, `MouseWheel(...)`
- `TopLevel.DragDrop(...)`
- `HeadlessUnitTestSession.StartNew(...)`, `GetOrStartForAssembly(...)`
- `HeadlessUnitTestSession.Dispatch(...)`

Reference source files:
- `src/Headless/Avalonia.Headless/AvaloniaHeadlessPlatform.cs`
- `src/Headless/Avalonia.Headless/HeadlessWindowExtensions.cs`
- `src/Headless/Avalonia.Headless/HeadlessUnitTestSession.cs`
- `src/Headless/Avalonia.Headless/AvaloniaTestApplicationAttribute.cs`
- `src/Headless/Avalonia.Headless/HeadlessUnitTestIsolationAttribute.cs`
- `src/Headless/Avalonia.Headless.NUnit/AvaloniaTest.cs`
- `src/Headless/Avalonia.Headless.XUnit/AvaloniaFact.cs`
- `src/Headless/Avalonia.Headless.XUnit/AvaloniaTheoryAttribute.cs`
- `tests/Avalonia.Headless.UnitTests/TestApplication.cs`

## Test Runtime Architecture

Headless test pipeline:
1. Build app with `UseHeadless(...)`.
2. Run tests on UI dispatcher via headless test framework attributes/session.
3. Drive input via `HeadlessWindowExtensions` methods.
4. Force rendering and capture frames for snapshot/visual assertions.

## Authoring Patterns

### Headless app setup

```csharp
public static AppBuilder BuildAvaloniaApp() => AppBuilder.Configure<TestApp>()
    .UseSkia()
    .UseHeadless(new AvaloniaHeadlessPlatformOptions
    {
        UseHeadlessDrawing = false
    });
```

### Assembly-level test runtime configuration

```csharp
using Avalonia.Headless;

[assembly: AvaloniaTestApplication(typeof(TestApp))]
[assembly: AvaloniaTestIsolation(AvaloniaTestIsolationLevel.PerTest)]
```

### xUnit UI test

```csharp
using Avalonia.Controls;
using Avalonia.Headless.XUnit;

public class UiTests
{
    [AvaloniaFact]
    public void Can_render_window_frame()
    {
        var window = new Window { Width = 400, Height = 300 };
        window.Show();

        var frame = window.CaptureRenderedFrame();
        if (frame is null)
            throw new Exception("Expected rendered frame.");
    }
}
```

### Deterministic input simulation

```csharp
window.MouseMove(new Point(50, 20));
window.MouseDown(new Point(50, 20), Avalonia.Input.MouseButton.Left);
window.MouseUp(new Point(50, 20), Avalonia.Input.MouseButton.Left);
window.KeyTextInput("abc");
```

## AOT-Safe Testing Guidance

- Prefer headless input APIs over direct construction of key/pointer event args.
- Keep test UIs on compiled bindings (`x:DataType`) to match production AOT paths.
- Avoid reflection-only runtime test helpers in smoke tests.
- For render snapshots, use `.UseSkia()` with `UseHeadlessDrawing = false`.

## Troubleshooting

1. `GetLastRenderedFrame()` throws:
- Headless app is using headless drawing backend; switch to Skia + `UseHeadlessDrawing = false`.

2. Flaky async UI assertions:
- Run assertions through test dispatcher (`AvaloniaFact` / `AvaloniaTest` / session `Dispatch`).

3. Input appears ignored:
- Window/top-level not shown or no focused target.
- Missing render/job stabilization before assertion.

4. State leaks between tests:
- Use `AvaloniaTestIsolationLevel.PerTest` for strict isolation.

## XAML-First and Code-Only Usage

Default mode:
- Keep test views/components defined in XAML to match production usage.
- Use code-only test view construction when requested.

XAML-first references:
- `.axaml` test views with compiled bindings
- Standard `InitializeComponent()` path in tests

XAML-first usage example:

```xml
<UserControl xmlns="https://github.com/avaloniaui"
             xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
             xmlns:vm="using:MyApp.ViewModels"
             x:Class="MyApp.Views.TestView"
             x:DataType="vm:TestViewModel">
  <TextBlock Text="{CompiledBinding Status}" />
</UserControl>
```

Code-only alternative (on request):

```csharp
var window = new Window
{
    Content = new TextBlock { Text = "Smoke test" }
};
window.Show();
```
