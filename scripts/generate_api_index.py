#!/usr/bin/env python3
"""Generate an app-building public API signature index for Avalonia.

The goal is pragmatic coverage of APIs used to build Avalonia apps (startup, lifetime,
binding, styling, threading, platform bootstrap), not a full compiler-accurate API dump.
"""

from __future__ import annotations

import argparse
from collections.abc import Callable
import datetime as dt
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile
from dataclasses import dataclass

DEFAULT_PATTERNS = [
    "src/Avalonia.Controls/AppBuilder.cs",
    "src/Avalonia.Controls/Application.cs",
    "src/Avalonia.Controls/ApplicationLifetimes/*.cs",
    "src/Avalonia.Controls/TopLevel.cs",
    "src/Avalonia.Controls/Window*.cs",
    "src/Avalonia.Controls/UserControl.cs",
    "src/Avalonia.Controls/ThemeVariantScope.cs",
    "src/Avalonia.Controls/DesktopApplicationExtensions.cs",
    "src/Avalonia.Controls/Templates/*.cs",
    "src/Avalonia.Base/AvaloniaObject*.cs",
    "src/Avalonia.Base/AvaloniaProperty*.cs",
    "src/Avalonia.Base/StyledProperty.cs",
    "src/Avalonia.Base/DirectProperty.cs",
    "src/Avalonia.Base/AttachedProperty.cs",
    "src/Avalonia.Base/Data/*.cs",
    "src/Avalonia.Base/Threading/Dispatcher*.cs",
    "src/Avalonia.Base/Styling/*.cs",
    "src/Avalonia.Base/Controls/ResourceDictionary.cs",
    "src/Avalonia.Base/Input/ICommandSource.cs",
    "src/Avalonia.Base/Input/KeyGesture.cs",
    "src/Avalonia.Base/Input/KeyBinding.cs",
    "src/Avalonia.Base/Interactivity/*.cs",
    "src/Markup/Avalonia.Markup/Data/Binding.cs",
    "src/Markup/Avalonia.Markup.Xaml/AvaloniaXamlLoader.cs",
    "src/Markup/Avalonia.Markup.Xaml.Loader/AvaloniaRuntimeXamlLoader.cs",
    "src/Markup/Avalonia.Markup.Xaml/MarkupExtensions/*.cs",
    "src/Markup/Avalonia.Markup.Xaml/Templates/*.cs",
    "src/Markup/Avalonia.Markup.Xaml/Styling/*.cs",
    "src/Avalonia.Desktop/AppBuilderDesktopExtensions.cs",
    "src/Avalonia.Dialogs/ManagedFileDialogExtensions.cs",
    "src/Skia/Avalonia.Skia/SkiaApplicationExtensions.cs",
    "src/Skia/Avalonia.Skia/SkiaOptions.cs",
    "src/HarfBuzz/Avalonia.HarfBuzz/HarfBuzzApplicationExtensions.cs",
    "src/Avalonia.Fonts.Inter/AppBuilderExtension.cs",
    "src/Windows/Avalonia.Win32/Win32Platform.cs",
    "src/Windows/Avalonia.Win32/Win32PlatformOptions.cs",
    "src/Avalonia.X11/X11Platform.cs",
    "src/Avalonia.Native/AvaloniaNativePlatformExtensions.cs",
    "src/Android/Avalonia.Android/AndroidPlatform.cs",
    "src/iOS/Avalonia.iOS/Platform.cs",
    "src/Browser/Avalonia.Browser/BrowserAppBuilder.cs",
    "src/Linux/Avalonia.LinuxFramebuffer/LinuxFramebufferPlatform.cs",
    "src/Linux/Avalonia.LinuxFramebuffer/LinuxFramebufferPlatformOptions.cs",
    "src/Headless/Avalonia.Headless/AvaloniaHeadlessPlatform.cs",
    "packages/Avalonia/Avalonia.props",
    "packages/Avalonia/AvaloniaBuildTasks.props",
    "packages/Avalonia/AvaloniaBuildTasks.targets",
    "build/BuildTargets.targets",
    "build/TrimmingEnable.props",
    "src/tools/Avalonia.Generators/Avalonia.Generators.props",
]

TYPE_DECL_RE = re.compile(
    r"^\s*(public|internal|private|protected)\s+"
    r"(?:new\s+|unsafe\s+|abstract\s+|sealed\s+|static\s+|partial\s+|readonly\s+|ref\s+)*"
    r"(class|interface|struct|enum|record)\s+([A-Za-z_][A-Za-z0-9_`]*)"
)

NAMESPACE_RE = re.compile(r"^\s*namespace\s+([A-Za-z_][A-Za-z0-9_.]*)\s*[;{]")
PUBLIC_RE = re.compile(r"^\s*public\s+")


@dataclass
class TypeScope:
    name: str
    is_public: bool
    brace_depth: int


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
    # Remove string literals so brace counting is less noisy.
    text = re.sub(r'"([^"\\]|\\.)*"', '""', text)
    text = re.sub(r"'([^'\\]|\\.)*'", "''", text)
    return text


def normalize_signature(raw: str) -> str:
    sig = " ".join(raw.replace("\t", " ").split())
    return sig.strip()


def declaration_terminated(sig: str) -> bool:
    return ";" in sig or "=>" in sig or "{" in sig


def area_for(rel: str) -> str:
    checks = [
        ("src/Avalonia.Controls/", "Application Model and Controls"),
        ("src/Avalonia.Base/", "Property, Data, Styling, Threading"),
        ("src/Markup/", "XAML and Markup"),
        ("src/Avalonia.Desktop/", "Desktop Bootstrap"),
        ("src/Windows/", "Windows Platform"),
        ("src/Avalonia.X11/", "Linux/X11 Platform"),
        ("src/Avalonia.Native/", "macOS Native Platform"),
        ("src/Android/", "Android Platform"),
        ("src/iOS/", "iOS Platform"),
        ("src/Browser/", "Browser Platform"),
        ("src/Linux/", "Linux Framebuffer"),
        ("src/Headless/", "Headless Platform"),
        ("src/Skia/", "Rendering and Text"),
        ("src/HarfBuzz/", "Rendering and Text"),
        ("src/Avalonia.Fonts.Inter/", "Rendering and Text"),
        ("packages/Avalonia/", "Build and MSBuild Integration"),
        ("build/", "Build and MSBuild Integration"),
        ("src/tools/Avalonia.Generators/", "Source Generator Integration"),
    ]

    for prefix, area in checks:
        if rel.startswith(prefix):
            return area
    return "Other"


def extract_signatures(path: pathlib.Path) -> tuple[str | None, list[str]]:
    namespace: str | None = None
    in_block = False
    depth = 0
    type_stack: list[TypeScope] = []
    pending_type: tuple[str, bool] | None = None
    pending_sig: str | None = None
    signatures: list[str] = []

    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except UnicodeDecodeError:
        return None, []

    for raw in lines:
        line, in_block = strip_comments(raw, in_block)
        if not line.strip():
            continue

        ns_match = NAMESPACE_RE.match(line)
        if ns_match:
            namespace = ns_match.group(1)

        clean = sanitize_for_braces(line)

        if pending_type is not None and "{" in clean:
            t_name, t_public = pending_type
            type_stack.append(TypeScope(name=t_name, is_public=t_public, brace_depth=depth + 1))
            pending_type = None

        type_match = TYPE_DECL_RE.match(line)
        is_type_decl = type_match is not None
        if type_match:
            access = type_match.group(1)
            kind = type_match.group(2)
            name = type_match.group(3)
            parent_public = type_stack[-1].is_public if type_stack else True
            is_public = access == "public" and parent_public

            if is_public:
                signatures.append(normalize_signature(line))

            if "{" in clean:
                type_stack.append(TypeScope(name=f"{kind} {name}", is_public=is_public, brace_depth=depth + 1))
            else:
                pending_type = (f"{kind} {name}", is_public)

        innermost_public = type_stack[-1].is_public if type_stack else False
        member_depth = type_stack[-1].brace_depth if type_stack else -1

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

        while type_stack and depth < type_stack[-1].brace_depth:
            type_stack.pop()

    if pending_sig:
        signatures.append(normalize_signature(pending_sig))

    return namespace, signatures


def resolve_files(repo: pathlib.Path, patterns: list[str]) -> list[pathlib.Path]:
    files: set[pathlib.Path] = set()
    for pattern in patterns:
        for match in repo.glob(pattern):
            if match.is_file():
                files.add(match)
    return sorted(files)


def write_markdown(
    output: pathlib.Path,
    repo: pathlib.Path,
    repo_label: str,
    files: list[pathlib.Path],
    max_per_file: int,
    git_ref: str | None = None,
) -> tuple[int, int]:
    now = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d %H:%M:%SZ")

    by_area: dict[str, list[tuple[str, str | None, list[str]]]] = {}
    total_sigs = 0

    for path in files:
        rel = path.relative_to(repo).as_posix()
        namespace, signatures = extract_signatures(path)
        if not signatures:
            continue

        total_sigs += len(signatures)
        area = area_for(rel)
        by_area.setdefault(area, []).append((rel, namespace, signatures))

    lines: list[str] = []
    lines.append("# Avalonia App-Building API Index (Generated)")
    lines.append("")
    lines.append(f"- Generated at (UTC): `{now}`")
    lines.append(f"- Repository: `{repo_label}`")
    if git_ref:
        lines.append(f"- Git ref: `{git_ref}`")
    lines.append(f"- Files scanned: `{len(files)}`")
    lines.append(f"- Captured public signatures: `{total_sigs}`")
    lines.append("")
    lines.append("## Scope")
    lines.append("")
    lines.append("This index intentionally targets app-construction APIs (startup, lifetime, XAML, binding, styling, threading, platform bootstrap, and build settings).")
    lines.append("")
    lines.append("## Regenerate")
    lines.append("")
    regen_cmd = "python3 scripts/generate_api_index.py --repo <path-to-avalonia-repo>"
    if git_ref:
        regen_cmd += f" --git-ref {git_ref}"
    regen_cmd += " --output references/api-index-generated.md"
    lines.append("```bash")
    lines.append(regen_cmd)
    lines.append("```")
    lines.append("")

    for area in sorted(by_area.keys()):
        lines.append(f"## {area}")
        lines.append("")
        for rel, namespace, signatures in sorted(by_area[area], key=lambda x: x[0]):
            lines.append(f"### `{rel}`")
            if namespace:
                lines.append(f"- Namespace: `{namespace}`")

            if len(signatures) > max_per_file:
                shown = signatures[:max_per_file]
                hidden = len(signatures) - max_per_file
            else:
                shown = signatures
                hidden = 0

            for sig in shown:
                lines.append(f"- `{sig}`")

            if hidden:
                lines.append(f"- `... {hidden} more signatures omitted (increase --max-per-file to include them).`")

            lines.append("")

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("\n".join(lines), encoding="utf-8")

    return len(files), total_sigs


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Generate app-facing Avalonia public API index markdown."
    )
    parser.add_argument(
        "--repo",
        required=True,
        help="Path to Avalonia repository root.",
    )
    parser.add_argument(
        "--output",
        required=True,
        help="Output markdown file path.",
    )
    parser.add_argument(
        "--git-ref",
        default=None,
        help="Optional git ref (tag/branch/commit) to scan via a detached worktree.",
    )
    parser.add_argument(
        "--pattern",
        action="append",
        default=[],
        help="Additional glob pattern relative to repo (repeatable).",
    )
    parser.add_argument(
        "--max-per-file",
        type=int,
        default=300,
        help="Maximum signatures to print per file before truncation note.",
    )
    return parser


def prepare_scan_repo(repo: pathlib.Path, git_ref: str | None) -> tuple[pathlib.Path, str, Callable[[], None]]:
    if not git_ref:
        return repo, repo.name, lambda: None

    if not (repo / ".git").exists():
        raise RuntimeError(f"--git-ref requires a git repository path: {repo}")

    safe_ref = re.sub(r"[^A-Za-z0-9._-]+", "-", git_ref)
    temp_repo = pathlib.Path(tempfile.mkdtemp(prefix=f"{repo.name}-{safe_ref}-"))

    try:
        subprocess.run(
            ["git", "-C", str(repo), "worktree", "add", "--detach", str(temp_repo), git_ref],
            check=True,
            capture_output=True,
            text=True,
        )
    except subprocess.CalledProcessError as ex:
        shutil.rmtree(temp_repo, ignore_errors=True)
        message = ex.stderr.strip() or ex.stdout.strip() or str(ex)
        raise RuntimeError(f"failed to create worktree for git ref '{git_ref}': {message}") from ex

    def cleanup() -> None:
        subprocess.run(
            ["git", "-C", str(repo), "worktree", "remove", "--force", str(temp_repo)],
            check=False,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        shutil.rmtree(temp_repo, ignore_errors=True)

    return temp_repo, f"{repo.name}@{git_ref}", cleanup


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    repo = pathlib.Path(args.repo).expanduser().resolve()
    output = pathlib.Path(args.output).expanduser().resolve()

    if not repo.exists() or not repo.is_dir():
        print(f"error: invalid repo path: {repo}", file=sys.stderr)
        return 2

    try:
        scan_repo, repo_label, cleanup = prepare_scan_repo(repo, args.git_ref)
    except RuntimeError as ex:
        print(f"error: {ex}", file=sys.stderr)
        return 4

    patterns = list(DEFAULT_PATTERNS)
    patterns.extend(args.pattern)

    try:
        files = resolve_files(scan_repo, patterns)
        if not files:
            print("error: no files matched configured patterns", file=sys.stderr)
            return 3

        file_count, sig_count = write_markdown(
            output,
            scan_repo,
            repo_label,
            files,
            max_per_file=args.max_per_file,
            git_ref=args.git_ref,
        )
        print(f"Wrote {output} ({file_count} files, {sig_count} signatures)")
        return 0
    finally:
        cleanup()


if __name__ == "__main__":
    raise SystemExit(main())
