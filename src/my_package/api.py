"""Public API surface for programmatic use (library + thin CLI adapter)."""

from __future__ import annotations

from pathlib import Path


def validate(path: str | Path) -> bool:
    """Return True if *path* exists on the local filesystem.

    This is a small template hook; replace with real validation logic for your domain.
    """
    return Path(path).exists()
