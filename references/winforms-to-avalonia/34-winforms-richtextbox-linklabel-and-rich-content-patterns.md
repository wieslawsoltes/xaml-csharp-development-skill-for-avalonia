# WinForms RichTextBox and LinkLabel to Avalonia Rich Content Patterns

## Table of Contents
1. Scope and APIs
2. Rich Text and Link Mapping
3. Conversion Example
4. C# Equivalent
5. Troubleshooting

## Scope and APIs

Primary WinForms APIs:

- `RichTextBox` (`Text`, `Rtf`, styled selections)
- `LinkLabel` and `LinkClicked`

Primary Avalonia APIs/patterns:

- `TextBox` (`AcceptsReturn`, `TextWrapping`) for editable multiline text
- `TextBlock` inline elements (`Run`, `Bold`, `Italic`, `Underline`) for rich read-only text
- `HyperlinkButton` (`NavigateUri`) for link-like actions

## Rich Text and Link Mapping

| WinForms | Avalonia |
|---|---|
| `RichTextBox` rich editor | `TextBox` for plain/multiline editing + custom formatting pipeline if needed |
| `RichTextBox` formatted display | `TextBlock` with `Inlines` (`Run`, `Bold`, `Italic`, `Underline`) |
| `LinkLabel` navigation | `HyperlinkButton` with `NavigateUri` or command |
| `LinkClicked` event handlers | command-first navigation/open-url services |

## Conversion Example

WinForms C#:

```csharp
notesRichTextBox.Text = ticket.Notes;
statusRichTextBox.SelectionFont = new Font("Segoe UI", 9, FontStyle.Bold);
statusRichTextBox.AppendText("Ready");

docsLinkLabel.LinkClicked += (_, _) => Process.Start(ticket.HelpUrl);
```

Avalonia XAML:

```xaml
<UserControl xmlns="https://github.com/avaloniaui"
             xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
             xmlns:vm="using:MyApp.ViewModels"
             x:DataType="vm:TicketViewModel">
  <StackPanel Spacing="10">
    <TextBox AcceptsReturn="True"
             TextWrapping="Wrap"
             MinHeight="120"
             Text="{CompiledBinding Notes, Mode=TwoWay}" />

    <TextBlock>
      <Run Text="Status: " />
      <Bold>Ready</Bold>
      <Run Text=" - " />
      <Italic>review migration notes</Italic>
      <Run Text=" before deployment." />
    </TextBlock>

    <HyperlinkButton Content="Open Ticket Documentation"
                     NavigateUri="{CompiledBinding DocumentationUri}" />
  </StackPanel>
</UserControl>
```

## C# Equivalent

```csharp
using System;
using Avalonia.Controls;
using Avalonia.Controls.Documents;

var notes = new TextBox
{
    AcceptsReturn = true,
    TextWrapping = Avalonia.Media.TextWrapping.Wrap,
    Text = viewModel.Notes
};

var status = new TextBlock();
status.Inlines?.Add(new Run("Status: "));

var ready = new Bold();
ready.Inlines.Add(new Run("Ready"));
status.Inlines?.Add(ready);

status.Inlines?.Add(new Run(" - "));

var action = new Italic();
action.Inlines.Add(new Run("review migration notes"));
status.Inlines?.Add(action);
status.Inlines?.Add(new Run(" before deployment."));

var docs = new HyperlinkButton
{
    Content = "Open Ticket Documentation",
    NavigateUri = viewModel.DocumentationUri ?? new Uri("https://docs.avaloniaui.net/")
};
```

## Troubleshooting

1. Expecting built-in RTF editing parity.
- Avalonia core does not provide a direct `RichTextBox` equivalent; keep rich editing in a dedicated domain component.

2. Link styling/navigation differs from WinForms.
- use `HyperlinkButton` with explicit theme styling and route URL launching through `TopLevel.Launcher` if custom behavior is needed.

3. Rich inline content appears inconsistent.
- keep complex formatting in a view-model/document model and regenerate inline trees predictably.
