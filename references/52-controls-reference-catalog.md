# Controls Reference Catalog

This catalog provides one reference document per public Avalonia control type.

## Scope

- Source: Avalonia `11.3.12` control assemblies (`src/Avalonia.Controls*`)
- Coverage: public classes identified as controls by inheritance from `Control`, `TopLevel`, or `WindowBase`
- Per-control content:
  - basic type metadata,
  - basic public API list,
  - minimal XAML usage,
  - minimal C# usage.

## Entry Point

- [`controls/README.md`](controls/README)

## Generation

Use the generator script to rebuild all control references:

```bash
python3 scripts/generate_control_reference_docs.py \
  --repo /Users/wieslawsoltes/GitHub/Avalonia \
  --git-ref 11.3.12 \
  --output-dir references/controls
```

## Notes

- Some controls are abstract; their docs include derived-type usage snippets.
- These docs are intentionally basic and uniform to support fast lookup across the full control surface.
