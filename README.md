# XAML and C# Cross-Platform Development Skill (for Avalonia)

Comprehensive Codex skill for building, reviewing, migrating, and optimizing Avalonia applications with modern XAML/C# patterns, compiled bindings, and AOT-friendly architecture.

## Usage Restriction Notice

At maintainer request, AvaloniaUI OÜ may not use this repository in any form.
This restriction is defined in the repository `LICENSE`.

## License

This repository uses an MIT-based license with an additional Restricted Party
Clause. See `LICENSE` for the full terms.

## Skill Identity

- Skill name: `xaml-csharp-development-skill-for-avalonia`
- Primary definition: [`SKILL.md`](SKILL)
- Main reference index: [`references/compendium.md`](references/compendium)
- Avalonia upstream repository: [AvaloniaUI/Avalonia](https://github.com/AvaloniaUI/Avalonia)

## Avalonia Version Coverage

This skill is currently pinned to Avalonia **11.3.12**.

- API references and guidance are aligned to `11.3.12` behavior.
- Generated API indexing is expected to use `--git-ref 11.3.12`.
- Guidance should avoid relying on `master`-only APIs unless a document explicitly states that exception.

As of **February 15, 2026**, this repository is maintained against the 11.3.12 release line.

## Scope

This skill covers app-development-facing Avalonia topics, including:

- App startup and lifetime wiring (desktop, single-view, activity hooks)
- XAML compilation and runtime loading patterns
- Compiled bindings, typed templates, and data/template composition
- Styling, theming, resources, and asset packaging
- Controls, templates, input/focus, layout, rendering, and animation
- Platform services (storage provider, clipboard, launcher, drag/drop, screens)
- Diagnostics, performance, testing, accessibility, and troubleshooting

It includes both curated guidance and a generated API index for signature lookup.

## Out of Scope

This skill is not intended to be:

- A full Avalonia internals/source-contributor guide
- A replacement for upstream API docs or source browsing
- A mandate to use unstable/private APIs in production code

When internals are mentioned, it is usually for diagnostics, constraints, or behavioral explanation.

## Repository Structure

- [`SKILL.md`](SKILL)
  - Skill entrypoint and execution rules
- `references/`
  - Numbered, topic-focused reference documents
- [`references/compendium.md`](references/compendium)
  - Top-level table of contents and task-oriented navigation
- [`references/api-index-generated.md`](references/api-index-generated)
  - Broad generated API signature index
- `scripts/generate_api_index.py`
  - API index generator script
- `assets/`
  - Supporting skill assets/templates
- `agents/`
  - Agent-specific instructions/context files

## How to Use the Skill

1. Start from [`SKILL.md`](SKILL).
2. Follow the workflow sections to load only the references needed for the current task.
3. Use [`references/compendium.md`](references/compendium) for fast navigation.
4. Use [`references/api-index-generated.md`](references/api-index-generated) when exact public signatures are required.

## XAML and API Coverage Notes

Recent additions include focused references for:

- XAML compiler/build pipeline
- Runtime XAML loader and dynamic loading
- XAML in libraries and resource packaging
- Runtime XAML manipulation and service-provider patterns
- Visual tree and logical tree inspection/traversal
- Data templates and `IDataTemplate` selector patterns
- Value converters
- Binding value/notification and instanced binding semantics
- Dispatcher priority, operations, and timers
- TopLevel, window, and runtime services
- Adaptive markup and dynamic resource patterns
- Relative/static resource and name resolution markup
- Template content and func template patterns
- Path icons, adorners, and shapes
- Per-control references for the full Avalonia control surface (`references/controls/`)

These are designed to reduce accidental drift to unreleased APIs.

## Regenerating API Index (Pinned)

```bash
python3 scripts/generate_api_index.py \
  --repo <path-to-avalonia-repo> \
  --git-ref 11.3.12 \
  --output references/api-index-generated.md
```

Recommended checks after regeneration:

- Verify key startup/binding/platform signatures still match references.
- Audit docs for master-only APIs introduced by mistake.
- Update this README and [`SKILL.md`](SKILL) if version coverage changes.

## Maintenance Checklist for New Avalonia Release

1. Switch target release tag (for example `11.3.x` -> `11.4.x`).
2. Regenerate [`references/api-index-generated.md`](references/api-index-generated) from the new tag.
3. Diff critical APIs referenced by docs.
4. Update affected reference files.
5. Update:
   - [`README.md`](README)
   - [`SKILL.md`](SKILL)
   - [`references/compendium.md`](references/compendium)

## Quality Bar

Skill guidance should remain:

- Version-accurate to the declared release
- Explicit about tradeoffs (trim/AOT/runtime dynamic paths)
- Focused on production-safe defaults (compiled XAML + compiled bindings)
- Structured for rapid task execution and review
