from __future__ import annotations

from dataclasses import dataclass
from typing import Generic, TypeVar

T = TypeVar("T")


@dataclass(frozen=True)
class ResolvedValue(Generic[T]):
    value: T
    source: str


@dataclass(frozen=True)
class RuntimeConfigSources:
    output_format: ResolvedValue[str]
    precision: ResolvedValue[int | None]
    color: ResolvedValue[str]
    quiet: ResolvedValue[bool]
    verbose: ResolvedValue[bool]
    debug: ResolvedValue[bool]
    non_interactive: ResolvedValue[bool]
    no_progress: ResolvedValue[bool]
    history_enabled: ResolvedValue[bool]
    history_path: ResolvedValue[str]
    active_profile: ResolvedValue[str | None]


@dataclass(frozen=True)
class ResolvedConfig:
    """Runtime config plus optional source tracing."""

    runtime_config: object
    sources: RuntimeConfigSources | None = None