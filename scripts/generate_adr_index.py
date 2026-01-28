#!/usr/bin/env python3
from __future__ import annotations

import re
from collections.abc import Iterable
from dataclasses import dataclass
from pathlib import Path

ADR_DIR = Path("docs/architecture/adr")
INDEX_PATH = ADR_DIR / "index.md"

START_MARKER = "<!-- ADR-INDEX:START -->"
END_MARKER = "<!-- ADR-INDEX:END -->"

ADR_FILENAME_RE = re.compile(r"^(?P<num>\d{4})-(?P<slug>.+)\.md$")

H1_RE = re.compile(r"^\s*#\s+(?P<title>.+?)\s*$", re.MULTILINE)

# Your metadata table uses "**Field**" in the first column.
META_ROW_RE = re.compile(
    r"^\|\s*\*\*(?P<key>[^*]+)\*\*\s*\|\s*(?P<val>.*?)\s*\|?\s*$",
    re.MULTILINE,
)


def clean_cell(value: str) -> str:
    v = value.strip()
    v = v.replace("<br/>", " ").replace("<br />", " ")
    v = re.sub(r"\s+", " ", v)
    # Remove surrounding backticks if present
    if len(v) >= 2 and v.startswith("`") and v.endswith("`"):
        v = v[1:-1].strip()
    return v


@dataclass(frozen=True)
class AdrRecord:
    number: int
    filename: str
    title: str
    date: str
    status: str
    tags: str


def parse_metadata(md: str) -> dict:
    meta = {}
    for m in META_ROW_RE.finditer(md):
        key = m.group("key").strip()
        val = clean_cell(m.group("val"))
        meta[key.lower()] = val
    return meta


def parse_title(md: str, fallback: str) -> str:
    m = H1_RE.search(md)
    if not m:
        return fallback
    # Often "ADR 0001: Title" in H1; keep full, or strip prefix lightly.
    title = m.group("title").strip()
    return title


def iter_adr_files() -> Iterable[Path]:
    if not ADR_DIR.exists():
        return
    for p in sorted(ADR_DIR.glob("*.md")):
        if p.name in {"README.md", "template.md", "index.md"}:
            continue
        if ADR_FILENAME_RE.match(p.name):
            yield p


def load_adr_record(path: Path) -> AdrRecord:
    md = path.read_text(encoding="utf-8")
    m = ADR_FILENAME_RE.match(path.name)
    assert m is not None
    num = int(m.group("num"))

    title = parse_title(md, fallback=path.stem)
    meta = parse_metadata(md)

    date = meta.get("date", "")
    status = meta.get("status", "")
    tags = meta.get("tags", "")

    # If title is like "ADR 0001: X", normalize to just "X" for the table display.
    # Keep it conservative: only strip exact prefix patterns.
    title_display = title
    title_display = re.sub(r"^\s*ADR\s+\d{4}\s*:\s*", "", title_display, flags=re.IGNORECASE)

    return AdrRecord(
        number=num,
        filename=path.name,
        title=title_display.strip(),
        date=date,
        status=status,
        tags=tags,
    )


def generate_table(records: list[AdrRecord]) -> str:
    lines = []
    lines.append("| ADR | Title | Status | Date | Tags |")
    lines.append("|-----|-------|--------|------|------|")
    for r in records:
        adr_link = f"[{r.number:04d}]({r.filename})"
        title = r.title or "-"
        status = r.status or "-"
        date = r.date or "-"
        tags = r.tags or "-"
        lines.append(f"| {adr_link} | {title} | {status} | {date} | {tags} |")
    return "\n".join(lines)


def replace_between_markers(text: str, start: str, end: str, replacement: str) -> str:
    if start not in text or end not in text:
        raise RuntimeError(f"INDEX missing markers. Add:\n{start}\n{end}\n")
    before, rest = text.split(start, 1)
    middle, after = rest.split(end, 1)
    # Keep markers, replace only content between them.
    return f"{before}{start}\n{replacement}\n{end}{after}"


def main() -> int:
    if not INDEX_PATH.exists():
        raise RuntimeError(f"Missing {INDEX_PATH}. Create it and add markers.")

    records = [load_adr_record(p) for p in iter_adr_files()]
    records.sort(key=lambda r: r.number)

    table = generate_table(records) if records else "_No ADRs yet._"
    index = INDEX_PATH.read_text(encoding="utf-8")
    updated = replace_between_markers(index, START_MARKER, END_MARKER, table)

    if updated != index:
        INDEX_PATH.write_text(updated, encoding="utf-8")
        print(f"Updated ADR index in {INDEX_PATH}")
    else:
        print("ADR index already up to date.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
