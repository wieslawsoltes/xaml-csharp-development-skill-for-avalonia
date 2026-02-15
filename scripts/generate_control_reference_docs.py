#!/usr/bin/env python3
"""Generate one reference markdown doc per Avalonia control type.

The generator scans Avalonia source at a given git ref and emits docs with:
- basic metadata (namespace/assembly/base/source),
- basic API list (public members declared on the type),
- minimal XAML usage,
- minimal C# usage.
"""

from __future__ import annotations

import argparse
from collections import defaultdict
from dataclasses import dataclass, field
import datetime as dt
import pathlib
import re
import subprocess

TYPE_DECL_RE = re.compile(
    r"^\s*(public|internal|private|protected)\s+"
    r"(?P<mods>(?:new\s+|unsafe\s+|abstract\s+|sealed\s+|static\s+|partial\s+|readonly\s+|ref\s+)*)"
    r"(?P<kind>class|interface|struct|enum|record(?:\s+class|\s+struct)?)\s+"
    r"(?P<name>[A-Za-z_][A-Za-z0-9_`]*)"
)
NAMESPACE_RE = re.compile(r"^\s*namespace\s+([A-Za-z_][A-Za-z0-9_.]*)\s*(?:[;{])?\s*$")
PUBLIC_RE = re.compile(r"^\s*public\s+")


@dataclass
class TypeInfo:
    name: str
    namespace: str
    source_file: str
    assembly: str
    declaration: str
    is_abstract: bool
    base_names: set[str] = field(default_factory=set)
    members: list[str] = field(default_factory=list)

    @property
    def full_name(self) -> str:
        return f"{self.namespace}.{self.name}" if self.namespace else self.name


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate per-control reference docs.")
    parser.add_argument(
        "--repo",
        type=pathlib.Path,
        default=pathlib.Path("/Users/wieslawsoltes/GitHub/Avalonia"),
        help="Path to Avalonia git repository.",
    )
    parser.add_argument(
        "--git-ref",
        default="11.3.12",
        help="Git ref/tag to scan.",
    )
    parser.add_argument(
        "--output-dir",
        type=pathlib.Path,
        default=pathlib.Path("references/controls"),
        help="Output directory for generated docs.",
    )
    parser.add_argument(
        "--max-members",
        type=int,
        default=16,
        help="Maximum basic API members to show per control.",
    )
    return parser.parse_args()


def run_git(repo: pathlib.Path, args: list[str]) -> str:
    return subprocess.check_output(["git", "-C", str(repo), *args], text=True)


def git_list_control_files(repo: pathlib.Path, git_ref: str) -> list[str]:
    files = run_git(repo, ["ls-tree", "-r", "--name-only", git_ref, "src"]).splitlines()
    out: list[str] = []
    for rel in files:
        if not rel.endswith(".cs"):
            continue
        parts = rel.split("/")
        if len(parts) < 2:
            continue
        if parts[0] == "src" and parts[1].startswith("Avalonia.Controls"):
            out.append(rel)
    return sorted(out)


def strip_comments(line: str, in_block: bool) -> tuple[str, bool]:
    i = 0
    out: list[str] = []

    while i < len(line):
        if in_block:
            end = line.find("*/", i)
            if end == -1:
                return "", True
            i = end + 2
            in_block = False
            continue

        if line.startswith("/*", i):
            in_block = True
            i += 2
            continue

        if line.startswith("//", i):
            break

        out.append(line[i])
        i += 1

    return "".join(out), in_block


def sanitize_for_braces(text: str) -> str:
    text = re.sub(r'"([^"\\]|\\.)*"', '""', text)
    text = re.sub(r"'([^'\\]|\\.)*'", "''", text)
    return text


def normalize_signature(raw: str) -> str:
    return " ".join(raw.replace("\t", " ").split()).strip()


def declaration_terminated(sig: str) -> bool:
    return ";" in sig or "=>" in sig or "{" in sig


def extract_signatures(content: str) -> tuple[str | None, list[str]]:
    namespace: str | None = None
    in_block = False
    depth = 0
    type_stack: list[tuple[str, bool, int]] = []
    pending_type: tuple[str, bool] | None = None
    pending_sig: str | None = None
    signatures: list[str] = []

    for raw in content.splitlines():
        line, in_block = strip_comments(raw, in_block)
        line = line.lstrip("\ufeff")
        if not line.strip():
            continue

        ns_match = NAMESPACE_RE.match(line)
        if ns_match:
            namespace = ns_match.group(1)

        clean = sanitize_for_braces(line)

        if pending_type is not None and "{" in clean:
            t_name, t_public = pending_type
            type_stack.append((t_name, t_public, depth + 1))
            pending_type = None

        type_match = TYPE_DECL_RE.match(line)
        is_type_decl = type_match is not None
        if type_match:
            access = type_match.group(1)
            name = type_match.group("name")
            parent_public = type_stack[-1][1] if type_stack else True
            is_public = access == "public" and parent_public

            if is_public:
                signatures.append(normalize_signature(line))

            if "{" in clean:
                type_stack.append((name, is_public, depth + 1))
            else:
                pending_type = (name, is_public)

        innermost_public = type_stack[-1][1] if type_stack else False
        member_depth = type_stack[-1][2] if type_stack else -1

        if pending_sig is None:
            if (
                innermost_public
                and depth == member_depth
                and PUBLIC_RE.match(line)
                and not is_type_decl
                and not line.lstrip().startswith("public:")
            ):
                pending_sig = normalize_signature(line)
                if declaration_terminated(pending_sig):
                    signatures.append(pending_sig)
                    pending_sig = None
        else:
            pending_sig = normalize_signature(pending_sig + " " + line)
            if declaration_terminated(pending_sig):
                signatures.append(pending_sig)
                pending_sig = None

        depth += clean.count("{")
        depth -= clean.count("}")

        while type_stack and depth < type_stack[-1][2]:
            type_stack.pop()

    if pending_sig:
        signatures.append(pending_sig)

    return namespace, signatures


def base_names_from_declaration(signature: str) -> list[str]:
    decl = signature.split("{", 1)[0].strip()
    if ":" not in decl:
        return []

    base_part = decl.split(":", 1)[1]
    base_part = base_part.split(" where ", 1)[0]

    result: list[str] = []
    for part in base_part.split(","):
        token = part.strip()
        if not token:
            continue
        token = token.replace("?", "")
        token = token.split(".")[-1]
        if "<" in token:
            token = token.split("<", 1)[0]
        token = token.strip()
        if token:
            result.append(token)
    return result


def assembly_from_source(source: str) -> str:
    parts = source.split("/")
    if len(parts) >= 2 and parts[0] == "src":
        return parts[1]
    return "Avalonia.Controls"


def kebab_case(name: str) -> str:
    name = re.sub(r"([a-z0-9])([A-Z])", r"\1-\2", name)
    name = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1-\2", name)
    return name.replace("_", "-").lower()


def slug_for(full_name: str) -> str:
    if full_name.startswith("Avalonia.Controls."):
        reduced = full_name[len("Avalonia.Controls.") :]
    else:
        reduced = full_name
    parts = [kebab_case(p) for p in reduced.split(".") if p]
    return "-".join(parts)


def is_class_type(kind: str) -> bool:
    return kind == "class" or kind.startswith("record")


def collect_types(repo: pathlib.Path, git_ref: str, files: list[str]) -> dict[str, TypeInfo]:
    type_infos: dict[str, TypeInfo] = {}

    for source in files:
        content = run_git(repo, ["show", f"{git_ref}:{source}"])
        namespace, signatures = extract_signatures(content)
        namespace = namespace or ""

        current_full_name: str | None = None

        for sig in signatures:
            tmatch = TYPE_DECL_RE.match(sig)
            if tmatch:
                kind = tmatch.group("kind")
                if not is_class_type(kind):
                    current_full_name = None
                    continue

                short_name = tmatch.group("name").split("`", 1)[0]
                full_name = f"{namespace}.{short_name}" if namespace else short_name
                is_abstract = " abstract " in f" {sig} "
                bases = base_names_from_declaration(sig)

                info = type_infos.get(full_name)
                if info is None:
                    type_infos[full_name] = TypeInfo(
                        name=short_name,
                        namespace=namespace,
                        source_file=source,
                        assembly=assembly_from_source(source),
                        declaration=sig,
                        is_abstract=is_abstract,
                        base_names=set(bases),
                        members=[],
                    )
                else:
                    if not info.base_names and bases:
                        info.base_names = set(bases)
                    else:
                        info.base_names.update(bases)
                    info.is_abstract = info.is_abstract or is_abstract

                current_full_name = full_name
                continue

            if current_full_name is not None:
                type_infos[current_full_name].members.append(sig)

    return type_infos


def determine_control_types(type_infos: dict[str, TypeInfo]) -> set[str]:
    by_short_name: dict[str, set[str]] = defaultdict(set)
    for full_name, info in type_infos.items():
        by_short_name[info.name].add(full_name)

    control_short_names: set[str] = {"Control", "TopLevel", "WindowBase"}

    changed = True
    while changed:
        changed = False
        for info in type_infos.values():
            if info.name in control_short_names:
                continue
            if any(base in control_short_names for base in info.base_names):
                control_short_names.add(info.name)
                changed = True

    controls: set[str] = set()
    for full_name, info in type_infos.items():
        if info.name in control_short_names:
            controls.add(full_name)
    return controls


def unique_member_signatures(signatures: list[str], max_members: int) -> list[str]:
    out: list[str] = []
    seen: set[str] = set()
    for sig in signatures:
        s = normalize_signature(sig)
        if s in seen:
            continue
        seen.add(s)
        out.append(s)
        if len(out) >= max_members:
            break
    return out


def render_xaml_example(info: TypeInfo) -> str:
    if info.is_abstract:
        return (
            "```xml\n"
            "<!-- Requires xmlns:local=\"using:MyApp.Controls\" -->\n"
            f"<!-- {info.name} is abstract; use a concrete derived type -->\n"
            f"<local:My{info.name} x:Name=\"Sample{info.name}\" />\n"
            "```"
        )

    return (
        "```xml\n"
        f"<{info.name} x:Name=\"Sample{info.name}\" />\n"
        "```"
    )


def render_csharp_example(info: TypeInfo) -> str:
    if info.is_abstract:
        return (
            "```csharp\n"
            f"using {info.namespace};\n\n"
            f"public sealed class My{info.name} : {info.name}\n"
            "{\n"
            "}\n\n"
            f"var control = new My{info.name}();\n"
            "```"
        )

    return (
        "```csharp\n"
        f"using {info.namespace};\n\n"
        f"var control = new {info.name}();\n"
        "```"
    )


def write_control_doc(output_path: pathlib.Path, info: TypeInfo, max_members: int) -> None:
    bases = ", ".join(sorted(info.base_names)) if info.base_names else "None"
    members = unique_member_signatures(info.members, max_members=max_members)

    lines: list[str] = []
    lines.append(f"# {info.name}")
    lines.append("")
    lines.append("> Note: This document is auto-generated by `scripts/generate_control_reference_docs.py`. Do not edit manually.")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append(f"- Full type: `{info.full_name}`")
    lines.append(f"- Namespace: `{info.namespace}`")
    lines.append(f"- Assembly: `{info.assembly}`")
    lines.append(f"- Source: `{info.source_file}`")
    lines.append(f"- Base types: `{bases}`")
    lines.append(f"- Kind: `{'abstract control' if info.is_abstract else 'control'}`")
    lines.append("")
    lines.append("## Basic APIs")
    lines.append("")

    if members:
        for sig in members:
            lines.append(f"- `{sig}`")
    else:
        lines.append("- No additional public members are declared on this type in source files scanned; use base control APIs.")

    lines.append("")
    lines.append("## XAML Usage")
    lines.append("")
    lines.append(render_xaml_example(info))
    lines.append("")
    lines.append("## C# Usage")
    lines.append("")
    lines.append(render_csharp_example(info))
    lines.append("")

    output_path.write_text("\n".join(lines), encoding="utf-8")


def write_index(output_dir: pathlib.Path, controls: list[TypeInfo], git_ref: str) -> None:
    now = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d %H:%M:%SZ")
    grouped: dict[str, list[tuple[str, str, str]]] = defaultdict(list)

    for info in controls:
        slug = slug_for(info.full_name)
        grouped[info.namespace].append((info.name, slug, info.full_name))

    lines: list[str] = []
    lines.append("# Avalonia Controls Reference Index")
    lines.append("")
    lines.append(f"- Generated at (UTC): `{now}`")
    lines.append(f"- Avalonia git ref: `{git_ref}`")
    lines.append(f"- Controls documented: `{len(controls)}`")
    lines.append("")
    lines.append("Each control has a dedicated reference with basic APIs and XAML/C# usage.")
    lines.append("")

    for namespace in sorted(grouped.keys()):
        lines.append(f"## {namespace}")
        lines.append("")
        for name, slug, full_name in sorted(grouped[namespace], key=lambda x: x[2]):
            lines.append(f"- [{name}]({slug}) (`{full_name}`)")
        lines.append("")

    (output_dir / "README.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    args = parse_args()

    repo = args.repo.resolve()
    output_dir = args.output_dir.resolve()

    files = git_list_control_files(repo, args.git_ref)
    type_infos = collect_types(repo, args.git_ref, files)
    control_full_names = determine_control_types(type_infos)

    controls = sorted(
        (type_infos[full_name] for full_name in control_full_names),
        key=lambda x: x.full_name,
    )

    output_dir.mkdir(parents=True, exist_ok=True)

    slugs_seen: set[str] = set()
    for info in controls:
        slug = slug_for(info.full_name)
        if slug in slugs_seen:
            slug = f"{slug}-{kebab_case(info.assembly)}"
        slugs_seen.add(slug)
        write_control_doc(output_dir / f"{slug}.md", info, max_members=args.max_members)

    write_index(output_dir, controls, args.git_ref)

    print(f"Scanned files: {len(files)}")
    print(f"Control types documented: {len(controls)}")
    print(f"Output directory: {output_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
