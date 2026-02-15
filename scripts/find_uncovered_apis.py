#!/usr/bin/env python3
"""Find APIs from api-index-generated.md that are not covered in reference docs."""

from __future__ import annotations

import argparse
from collections import defaultdict
from dataclasses import dataclass
import fnmatch
import pathlib
import re
import sys

INDEX_SOURCE_RE = re.compile(r"^### `([^`]+)`\s*$")
INDEX_ENTRY_RE = re.compile(r"^- `([^`]+)`\s*$")
TYPE_DECL_RE = re.compile(
    r"^public\s+(?:new\s+|unsafe\s+|abstract\s+|sealed\s+|static\s+|partial\s+|readonly\s+|ref\s+)*"
    r"(?:class|interface|struct|enum|record)\s+([A-Za-z_][A-Za-z0-9_`.]*)"
)
DELEGATE_RE = re.compile(
    r"^public\s+(?:new\s+|unsafe\s+|static\s+|partial\s+|readonly\s+|ref\s+)*delegate\s+[^(]*\b([A-Za-z_][A-Za-z0-9_]*)\s*\("
)
EVENT_RE = re.compile(r"^public\s+event\s+.+?\b([A-Za-z_][A-Za-z0-9_]*)\s*(?:[;=]|{)")
INDEXER_RE = re.compile(r"\bthis\s*\[")
OPERATOR_RE = re.compile(r"\boperator\s+([^\s(]+)")


@dataclass(frozen=True)
class ApiEntry:
    source_file: str
    signature: str
    kind: str
    symbol: str
    container: str | None = None


def normalize_ws(value: str) -> str:
    return " ".join(value.split()).strip()


def display_path(path: pathlib.Path) -> str:
    try:
        return path.relative_to(pathlib.Path.cwd()).as_posix()
    except ValueError:
        return path.as_posix()


def normalize_symbol(token: str) -> str:
    name = token.strip().rstrip(",;:{}")
    if "." in name:
        name = name.rsplit(".", 1)[-1]
    if "<" in name:
        name = name.split("<", 1)[0]
    name = re.sub(r"`\d+$", "", name)
    return name


def parse_signature(signature: str) -> tuple[str, str]:
    sig = normalize_ws(signature)
    type_match = TYPE_DECL_RE.match(sig)
    if type_match:
        return "type", normalize_symbol(type_match.group(1))

    delegate_match = DELEGATE_RE.match(sig)
    if delegate_match:
        return "delegate", normalize_symbol(delegate_match.group(1))

    event_match = EVENT_RE.match(sig)
    if event_match:
        return "event", normalize_symbol(event_match.group(1))

    if INDEXER_RE.search(sig):
        return "indexer", "this[]"

    operator_match = OPERATOR_RE.search(sig)
    if operator_match:
        return "operator", operator_match.group(1)

    if "(" in sig:
        pre = sig.split("(", 1)[0].strip()
        token = pre.split()[-1] if pre else ""
        symbol = normalize_symbol(token)
        return ("method", symbol) if symbol else ("unknown", "")

    pre = re.split(r"{|=>|=|;", sig, maxsplit=1)[0].strip()
    token = pre.split()[-1] if pre else ""
    symbol = normalize_symbol(token)
    return ("member", symbol) if symbol else ("unknown", "")


def parse_api_index(index_path: pathlib.Path) -> list[ApiEntry]:
    entries: list[ApiEntry] = []
    current_source = "<unknown>"
    current_type: str | None = None

    for raw_line in index_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        source_match = INDEX_SOURCE_RE.match(line)
        if source_match:
            current_source = source_match.group(1)
            current_type = None
            continue

        entry_match = INDEX_ENTRY_RE.match(line)
        if not entry_match:
            continue

        content = normalize_ws(entry_match.group(1))
        if not content.startswith("public "):
            continue

        kind, symbol = parse_signature(content)
        if not symbol:
            continue

        container: str | None = None
        if kind == "type":
            current_type = symbol
        else:
            container = current_type

        entries.append(
            ApiEntry(
                source_file=current_source,
                signature=content,
                kind=kind,
                symbol=symbol,
                container=container,
            )
        )

    deduped: list[ApiEntry] = []
    seen: set[tuple[str, str]] = set()
    for entry in entries:
        key = (entry.source_file, entry.signature)
        if key in seen:
            continue
        seen.add(key)
        deduped.append(entry)
    return deduped


def is_excluded(path: pathlib.Path, root: pathlib.Path, patterns: list[str]) -> bool:
    rel = path.relative_to(root).as_posix()
    for pattern in patterns:
        if fnmatch.fnmatch(path.name, pattern) or fnmatch.fnmatch(rel, pattern):
            return True
    return False


def load_reference_docs(
    references_dir: pathlib.Path,
    index_path: pathlib.Path,
    output_path: pathlib.Path | None,
    exclude_patterns: list[str],
) -> tuple[list[pathlib.Path], str]:
    docs: list[pathlib.Path] = []
    corpus_parts: list[str] = []

    for path in sorted(references_dir.rglob("*.md")):
        if not path.is_file():
            continue
        if path.resolve() == index_path.resolve():
            continue
        if output_path is not None and path.resolve() == output_path.resolve():
            continue
        if is_excluded(path, references_dir, exclude_patterns):
            continue

        docs.append(path)
        corpus_parts.append(path.read_text(encoding="utf-8"))

    return docs, "\n\n".join(corpus_parts)


def has_token(corpus: str, token: str) -> bool:
    pattern = re.compile(rf"(?<![A-Za-z0-9_]){re.escape(token)}(?![A-Za-z0-9_])")
    return bool(pattern.search(corpus))


def has_qualified(corpus: str, container: str, symbol: str) -> bool:
    pattern = re.compile(
        rf"(?<![A-Za-z0-9_]){re.escape(container)}\s*\.\s*{re.escape(symbol)}(?![A-Za-z0-9_])"
    )
    return bool(pattern.search(corpus))


def has_method_call(corpus: str, symbol: str) -> bool:
    pattern = re.compile(
        rf"(?<![A-Za-z0-9_]){re.escape(symbol)}\s*(?:<[^>\n]+>)?\s*\("
    )
    return bool(pattern.search(corpus))


def is_covered(entry: ApiEntry, corpus: str) -> bool:
    if entry.kind == "type":
        if f"`{entry.symbol}`" in corpus:
            return True
        return has_token(corpus, entry.symbol)

    if entry.kind == "indexer":
        return "this[" in corpus

    if entry.kind == "operator":
        text = f"operator {entry.symbol}"
        if f"`{text}`" in corpus:
            return True
        return has_token(corpus, text)

    if entry.kind in {"method", "delegate"}:
        if entry.container and has_qualified(corpus, entry.container, entry.symbol):
            return True
        if has_method_call(corpus, entry.symbol):
            return True
        return f"`{entry.symbol}`" in corpus

    if entry.container and has_qualified(corpus, entry.container, entry.symbol):
        return True

    if f"`{entry.symbol}`" in corpus:
        return True

    # Fallback for longer member names where plain-token matching is less noisy.
    if len(entry.symbol) >= 8 and entry.symbol[:1].isupper():
        return has_token(corpus, entry.symbol)

    return False


def build_report(
    entries: list[ApiEntry],
    uncovered: list[ApiEntry],
    docs: list[pathlib.Path],
    index_path: pathlib.Path,
    references_dir: pathlib.Path,
) -> str:
    covered_count = len(entries) - len(uncovered)
    by_source: dict[str, list[ApiEntry]] = defaultdict(list)
    for entry in uncovered:
        by_source[entry.source_file].append(entry)

    lines: list[str] = []
    lines.append("# API Coverage Gap Report")
    lines.append("")
    lines.append(f"- API index: `{display_path(index_path)}`")
    lines.append(f"- References scanned: `{display_path(references_dir)}`")
    lines.append(f"- Reference docs scanned: `{len(docs)}`")
    lines.append(f"- API signatures parsed: `{len(entries)}`")
    lines.append(f"- Covered APIs: `{covered_count}`")
    lines.append(f"- Not covered APIs: `{len(uncovered)}`")
    lines.append("")
    lines.append("## Not Covered API Signatures")
    lines.append("")

    if not uncovered:
        lines.append("All parsed API signatures appear to be covered by the scanned docs.")
        lines.append("")
        return "\n".join(lines)

    for source in sorted(by_source.keys()):
        lines.append(f"### `{source}`")
        for entry in by_source[source]:
            lines.append(f"- `{entry.signature}`")
        lines.append("")

    return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Scan references against api-index-generated.md and report APIs "
            "that are not covered."
        )
    )
    parser.add_argument(
        "--index",
        type=pathlib.Path,
        default=pathlib.Path("references/api-index-generated.md"),
        help="Path to generated API index markdown.",
    )
    parser.add_argument(
        "--references-dir",
        type=pathlib.Path,
        default=pathlib.Path("references"),
        help="Directory containing reference markdown docs to scan.",
    )
    parser.add_argument(
        "--output",
        type=pathlib.Path,
        default=pathlib.Path("references/api-coverage-not-covered.md"),
        help="Output markdown report path.",
    )
    parser.add_argument(
        "--exclude",
        action="append",
        default=[],
        help=(
            "Exclude pattern (file name or relative path glob). "
            "Can be used multiple times."
        ),
    )
    parser.add_argument(
        "--stdout",
        action="store_true",
        help="Also print the full report to stdout.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    index_path = args.index.resolve()
    references_dir = args.references_dir.resolve()
    output_path = args.output.resolve() if args.output else None

    if not index_path.is_file():
        print(f"error: API index file not found: {index_path}", file=sys.stderr)
        return 1
    if not references_dir.is_dir():
        print(f"error: references directory not found: {references_dir}", file=sys.stderr)
        return 1

    exclude_patterns = ["api-index-generated.md", "api-coverage-*.md", *args.exclude]
    entries = parse_api_index(index_path)
    docs, corpus = load_reference_docs(
        references_dir=references_dir,
        index_path=index_path,
        output_path=output_path,
        exclude_patterns=exclude_patterns,
    )

    uncovered = [entry for entry in entries if not is_covered(entry, corpus)]
    report = build_report(entries, uncovered, docs, index_path, references_dir)

    if output_path is not None:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(report, encoding="utf-8")

    print(
        f"Parsed {len(entries)} API signatures; "
        f"covered {len(entries) - len(uncovered)}; "
        f"not covered {len(uncovered)}."
    )
    if output_path is not None:
        print(f"Report written to: {display_path(output_path)}")
    if args.stdout:
        print()
        print(report)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
