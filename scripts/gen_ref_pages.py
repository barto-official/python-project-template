"""Generate API reference pages and literate navigation for MkDocs.

Reads ``extra.api_reference`` from ``mkdocs.yml``. See that file for options.
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any

import mkdocs_gen_files
import yaml

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
REFERENCE = Path("reference/api")

DEFAULT_CONFIG: dict[str, Any] = {
    "packages": ["my_package"],
    "public_only": True,
    "exclude": [],
}


def _load_config() -> dict[str, Any]:
    mkdocs_path = ROOT / "mkdocs.yml"
    data = yaml.safe_load(mkdocs_path.read_text(encoding="utf-8")) or {}
    extra = data.get("extra") or {}
    return {**DEFAULT_CONFIG, **(extra.get("api_reference") or {})}


def _module_parts(rel: Path) -> tuple[str, ...] | None:
    parts = rel.with_suffix("").parts
    if not parts:
        return None
    if parts[-1] == "__main__":
        return None
    if parts[-1] == "__init__":
        return parts[:-1]
    return parts


def _is_private_module(parts: tuple[str, ...]) -> bool:
    return any(part.startswith("_") and not part.startswith("__") for part in parts)


def _is_importable_package_path(path: Path, package_root: Path) -> bool:
    """Require __init__.py in each parent directory (skip stray namespace files)."""
    rel = path.relative_to(package_root)
    for parent in rel.parents:
        if parent == Path("."):
            continue
        if not (package_root / parent / "__init__.py").is_file():
            return False
    return True


def _matches_exclude(module_id: str, exclude: list[str]) -> bool:
    for pattern in exclude:
        if pattern.startswith("re:"):
            if re.search(pattern[3:], module_id):
                return True
        elif module_id == pattern or module_id.startswith(f"{pattern}."):
            return True
    return False


def _mkdocstrings_block(identifier: str, *, public_only: bool) -> str:
    if public_only:
        options = """\
    options:
      filters:
        - "!^_"
      show_if_no_docstring: false
"""
    else:
        options = """\
    options:
      filters: []
      show_if_no_docstring: true
"""
    return f"::: {identifier}\n{options}"


config = _load_config()
packages: list[str] = config["packages"]
public_only: bool = bool(config["public_only"])
exclude: list[str] = list(config.get("exclude") or [])

nav = mkdocs_gen_files.Nav()

for package in packages:
    package_root = SRC / package
    if not package_root.is_dir():
        msg = f"api_reference.packages entry not found under src/: {package}"
        raise FileNotFoundError(msg)

    for path in sorted(package_root.rglob("*.py")):
        if not _is_importable_package_path(path, package_root):
            continue

        rel = path.relative_to(SRC)
        parts = _module_parts(rel)
        if parts is None:
            continue

        module_id = ".".join(parts)
        if public_only and _is_private_module(parts):
            continue
        if _matches_exclude(module_id, exclude):
            continue

        doc_path = rel.with_suffix(".md")
        full_doc_path = REFERENCE / doc_path

        if path.name == "__init__.py":
            doc_path = doc_path.with_name("index.md")
            full_doc_path = full_doc_path.with_name("index.md")

        nav[parts] = doc_path.as_posix()

        with mkdocs_gen_files.open(full_doc_path, "w") as fd:
            fd.write(_mkdocstrings_block(module_id, public_only=public_only))

        mkdocs_gen_files.set_edit_path(full_doc_path, path.relative_to(ROOT))

# Virtual nav file for mkdocs-literate-nav (not committed; do not edit by hand).
with mkdocs_gen_files.open(REFERENCE / "SUMMARY.md", "w") as nav_file:
    nav_file.writelines(nav.build_literate_nav())
