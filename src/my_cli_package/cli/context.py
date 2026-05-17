from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import typer

from my_package.config.models import RuntimeConfig
from my_package.config.resolver import resolve_runtime_config
from my_package.runtime.container import RuntimeContainer
from my_package.runtime.composition import build_runtime_container
from my_package.config.models import RuntimeConfig
from my_package.config.resolver import resolve_runtime_config
from my_package.runtime.container import RuntimeContainer
from my_package.runtime.composition import build_runtime_container


@dataclass(frozen=True)
class GlobalCliOptions:
    """Root-level CLI options that affect the whole command execution."""

    config_path: Path | None
    profile: str | None
    verbose: bool
    quiet: bool
    debug: bool
    non_interactive: bool
    color: str | None
    no_progress: bool


@dataclass(frozen=True)
class CliContext:
    """Runtime state shared from the root Typer callback to subcommands.

    This object is stored in `typer.Context.obj`.

    It should contain already-resolved runtime state, not raw global variables.
    """

    options: GlobalCliOptions
    runtime_config: RuntimeConfig
    container: RuntimeContainer

    @property
    def debug(self) -> bool:
        return self.options.debug

    @property
    def quiet(self) -> bool:
        return self.options.quiet

    @property
    def verbose(self) -> bool:
        return self.options.verbose

    @property
    def non_interactive(self) -> bool:
        return self.options.non_interactive


def build_cli_context(options: GlobalCliOptions) -> CliContext:
    """Resolve config and compose runtime dependencies for the current CLI run."""

    runtime_config = resolve_runtime_config(
        explicit_config_path=options.config_path,
        explicit_profile=options.profile,
        cli_overrides={
            # Only pass True booleans as explicit overrides.
            # False usually means "the flag was not provided".
            "verbose": options.verbose if options.verbose else None,
            "quiet": options.quiet if options.quiet else None,
            "debug": options.debug if options.debug else None,
            "non_interactive": (
                options.non_interactive if options.non_interactive else None
            ),
            "no_progress": options.no_progress if options.no_progress else None,

            # Color is tri-state: None means not provided.
            "color": options.color,
        },
    )

    container = build_runtime_container(runtime_config)

    return CliContext(
        options=options,
        runtime_config=runtime_config,
        container=container,
    )



def get_cli_context(ctx: typer.Context) -> CliContext:
    """Return the initialized CLI context or fail with a programmer error."""

    if not isinstance(ctx.obj, CliContext):
        raise RuntimeError(
            "CLI context was not initialized. "
            "Ensure the root Typer callback sets `ctx.obj`."
        )

    return ctx.obj