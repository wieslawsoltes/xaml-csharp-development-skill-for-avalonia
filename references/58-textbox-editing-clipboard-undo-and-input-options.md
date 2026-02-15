# TextBox Editing, Clipboard, Undo/Redo, and Text Input Options

## Table of Contents
1. Scope and APIs
2. Baseline `TextBox` Authoring
3. Selection and Caret Control
4. Clipboard Pipeline (`Cut`, `Copy`, `Paste`)
5. Undo/Redo and Edit History
6. Text Input Options for Virtual Keyboard/IME
7. Programmatic Patterns in C#
8. Best Practices
9. Troubleshooting

## Scope and APIs

Primary APIs:
- `TextBox`
- `TextInputOptions`
- `TextInputContentType`
- `TextInputReturnKeyType`
- `InputElement.TextInputMethodClientRequestedEvent`

Important `TextBox` members:
- `Text`, `CaretIndex`, `SelectionStart`, `SelectionEnd`, `SelectedText`
- `AcceptsReturn`, `AcceptsTab`, `TextWrapping`
- `IsReadOnly`, `PasswordChar`, `RevealPassword`
- `MaxLength`, `MaxLines`, `MinLines`
- `PlaceholderText`, `PlaceholderForeground`, `UseFloatingPlaceholder`
- `CanCut`, `CanCopy`, `CanPaste`, `CanUndo`, `CanRedo`
- `IsUndoEnabled`, `UndoLimit`
- `ClearSelection()`, `SelectAll()`, `Clear()`, `ScrollToLine(int)`
- `Cut()`, `Copy()`, `Paste()`, `Undo()`, `Redo()`
- `CopyingToClipboard`, `CuttingToClipboard`, `PastingFromClipboard`
- `TextChanging`, `TextChanged`
- static gestures: `CutGesture`, `CopyGesture`, `PasteGesture`

Important `TextInputOptions` attached properties:
- `TextInputOptions.ContentType`
- `TextInputOptions.ReturnKeyType`
- `TextInputOptions.Multiline`
- `TextInputOptions.AutoCapitalization`
- `TextInputOptions.IsSensitive`
- `TextInputOptions.Lowercase`
- `TextInputOptions.Uppercase`
- `TextInputOptions.ShowSuggestions`

Reference source files:
- `src/Avalonia.Controls/TextBox.cs`
- `src/Avalonia.Base/Input/TextInput/TextInputOptions.cs`
- `src/Avalonia.Base/Input/TextInput/TextInputContentType.cs`
- `src/Avalonia.Base/Input/TextInput/TextInputReturnKeyType.cs`

## Baseline `TextBox` Authoring

```xml
<TextBox xmlns="https://github.com/avaloniaui"
         xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
         Width="360"
         Text="{Binding Notes}"
         AcceptsReturn="True"
         TextWrapping="Wrap"
         MaxLines="6"
         PlaceholderText="Write a note..." />
```

Single-line defaults are usually enough for search/filter boxes. Use `AcceptsReturn` + `TextWrapping` for document-like input.

## Selection and Caret Control

`CaretIndex`, `SelectionStart`, and `SelectionEnd` are style/binding-friendly properties.

```csharp
using Avalonia.Controls;

void HighlightAll(TextBox textBox)
{
    textBox.SelectAll();
}

void MoveCaretToEnd(TextBox textBox)
{
    var textLength = textBox.Text?.Length ?? 0;
    textBox.CaretIndex = textLength;
    textBox.SelectionStart = textLength;
    textBox.SelectionEnd = textLength;
}
```

Use `ClearSelection()` to collapse selection while preserving caret location semantics.

## Clipboard Pipeline (`Cut`, `Copy`, `Paste`)

`TextBox` exposes routed clipboard events and imperative methods.

```csharp
using Avalonia.Controls;
using Avalonia.Interactivity;

void WireClipboardGuards(TextBox textBox)
{
    textBox.CopyingToClipboard += OnCopying;
    textBox.CuttingToClipboard += OnCutting;
    textBox.PastingFromClipboard += OnPasting;
}

void OnCopying(object? sender, RoutedEventArgs e)
{
    // e.Handled = true; // enable if copy should be blocked.
}

void OnCutting(object? sender, RoutedEventArgs e)
{
}

void OnPasting(object? sender, RoutedEventArgs e)
{
}
```

Shortcut notes:
- `CutGesture`, `CopyGesture`, `PasteGesture` expose platform-preferred defaults.
- If you provide custom `KeyBinding`s, keep behavior consistent with these defaults.

## Undo/Redo and Edit History

Use the built-in history rather than custom stacks where possible.

```xml
<TextBox xmlns="https://github.com/avaloniaui"
         xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
         Text="{Binding Script}"
         IsUndoEnabled="True"
         UndoLimit="200" />
```

```csharp
void ApplyUndoRedo(TextBox textBox)
{
    if (textBox.CanUndo)
        textBox.Undo();

    if (textBox.CanRedo)
        textBox.Redo();
}
```

## Text Input Options for Virtual Keyboard/IME

`TextInputOptions` configures keyboard and IME behavior via attached properties.

```xml
<TextBox xmlns="https://github.com/avaloniaui"
         xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
         Width="320"
         TextInputOptions.ContentType="Email"
         TextInputOptions.ReturnKeyType="Done"
         TextInputOptions.Multiline="False"
         TextInputOptions.AutoCapitalization="False"
         TextInputOptions.ShowSuggestions="True"
         PlaceholderText="name@example.com" />
```

Sensitive input pattern:

```xml
<TextBox xmlns="https://github.com/avaloniaui"
         xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
         PasswordChar="*"
         TextInputOptions.ContentType="Password"
         TextInputOptions.IsSensitive="True"
         TextInputOptions.ShowSuggestions="False" />
```

At runtime, effective options can be read with `TextInputOptions.FromStyledElement(...)`.

## Programmatic Patterns in C#

```csharp
using Avalonia.Controls;
using Avalonia.Input.TextInput;

void ConfigureInput(TextBox textBox)
{
    TextInputOptions.SetContentType(textBox, TextInputContentType.Search);
    TextInputOptions.SetReturnKeyType(textBox, TextInputReturnKeyType.Search);
    TextInputOptions.SetShowSuggestions(textBox, true);
}

void MoveToLine(TextBox textBox, int line)
{
    textBox.ScrollToLine(line);
}
```

## Best Practices

- Prefer binding on `Text` with validation enabled (default for `TextProperty`).
- Keep clipboard handlers lightweight; avoid blocking UI thread.
- Use `CanCut`/`CanCopy`/`CanPaste` and `CanUndo`/`CanRedo` to drive command availability.
- Set `TextInputOptions` explicitly for mobile and tablet scenarios.
- Use `PlaceholderText`; keep `Watermark` aliases only for legacy compatibility.

## Troubleshooting

1. Undo/redo never activates.
- Check `IsUndoEnabled` and avoid replacing `Text` on every keystroke from external code.

2. Paste command disabled unexpectedly.
- Verify `IsReadOnly`, selection state, and clipboard availability (`CanPaste`).

3. Virtual keyboard type does not match intent.
- Confirm `TextInputOptions.ContentType` and `ReturnKeyType` are set on the focused control.

4. Text wrapping not applied.
- Ensure `AcceptsReturn="True"` for multiline editing and set `TextWrapping` explicitly.

5. Clipboard event not firing.
- Subscribe to `CopyingToClipboard`, `CuttingToClipboard`, and `PastingFromClipboard` on the actual active `TextBox` instance.
