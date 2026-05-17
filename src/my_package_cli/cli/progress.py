from __future__ import annotations

import os
import sys
from collections.abc import Iterator
from contextlib import contextmanager
from dataclasses import dataclass

from rich.console import Console
from rich.progress import (
    BarColumn,
    Progress,
    SpinnerColumn,
    TaskProgressColumn,
    TextColumn,
    TimeElapsedColumn,
    TimeRemainingColumn,
)


@dataclass(frozen=True)
class ProgressPolicy:
    """Policy deciding whether progress UI should be shown."""

    quiet: bool = False
    no_progress: bool = False
    force_progress: bool = False

    def enabled(self) -> bool:
        if self.quiet or self.no_progress:
            return False

        if self.force_progress:
            return True

        if is_ci_environment():
            return False

        return sys.stderr.isatty()


def is_ci_environment() -> bool:
    return os.getenv("CI", "").strip().lower() in {"1", "true", "yes", "on"}


def build_progress(policy: ProgressPolicy) -> Progress:
    """Create a Rich progress instance configured for CLI-safe stderr output."""
    console = Console(stderr=True)

    return Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TaskProgressColumn(),
        TimeElapsedColumn(),
        TimeRemainingColumn(),
        console=console,
        transient=False,
        disable=not policy.enabled(),
    )


@contextmanager
def progress_context(policy: ProgressPolicy) -> Iterator[Progress]:
    """Context manager for progress bars/spinners.

    Progress output goes to stderr and is disabled automatically in CI,
    quiet mode, redirected stderr, or --no-progress mode.
    """
    progress = build_progress(policy)

    with progress:
        yield progress


@contextmanager
def maybe_progress(
    *,
    description: str,
    total: int | None,
    policy: ProgressPolicy,
) -> Iterator[tuple[Progress, int]]:
    """Create a single progress task and yield `(progress, task_id)`.

    Example:
        with maybe_progress(description="Processing", total=100, policy=policy) as (p, task):
            ...
            p.advance(task)
    """
    with progress_context(policy) as progress:
        task_id = progress.add_task(description, total=total)
        yield progress, task_id
