from __future__ import annotations

import json
import os
import sys
from dataclasses import dataclass
from enum import StrEnum
from typing import Any, TextIO

import typer


class OutputFormat(StrEnum):
    TEXT = "text"
    JSON = "json"
    PLAIN = "plain"


class ColorMode(StrEnum):
    AUTO = "auto"
    ALWAYS = "always"
    NEVER = "never"


@dataclass(frozen=True)
class OutputPolicy:
    """Terminal output policy for one CLI invocation."""

    color: ColorMode = ColorMode.AUTO
    quiet: bool = False
    pretty_json: bool = False

    def should_use_color(self, *, stream: TextIO) -> bool:
        if self.color == ColorMode.ALWAYS:
            return True

        if self.color == ColorMode.NEVER:
            return False

        if os.getenv("NO_COLOR") is not None:
            return False

        if os.getenv("FORCE_COLOR") is not None:
            return True

        if os.getenv("TERM") == "dumb":
            return False

        return stream.isatty()


class CliOutput:
    """Small stdout/stderr boundary for CLI rendering.

    Rules:
      - command data goes to stdout
      - diagnostics/errors/progress go to stderr
      - JSON output must not be polluted by diagnostics
    """

    def __init__(self, *, policy: OutputPolicy | None = None) -> None:
        self._policy = policy or OutputPolicy()

    def data(self, message: str = "") -> None:
        """Write primary command output to stdout."""
        typer.echo(message)

    def plain(self, value: object) -> None:
        """Write extraction-friendly scalar output to stdout."""
        typer.echo(str(value))

    def json(
        self,
        payload: dict[str, Any] | list[Any],
        *,
        pretty: bool | None = None,
    ) -> None:
        """Write machine-readable JSON to stdout."""
        use_pretty = self._policy.pretty_json if pretty is None else pretty

        if use_pretty:
            typer.echo(json.dumps(payload, indent=2, sort_keys=True, default=str))
            return

        typer.echo(
            json.dumps(
                payload,
                separators=(",", ":"),
                sort_keys=True,
                default=str,
            )
        )

    def diagnostic(self, message: str) -> None:
        """Write non-essential diagnostic output to stderr."""
        if self._policy.quiet:
            return

        typer.echo(message, err=True)

    def warning(self, message: str) -> None:
        """Write warning output to stderr."""
        typer.echo(f"Warning: {message}", err=True)

    def error(self, message: str) -> None:
        """Write error output to stderr."""
        typer.echo(message, err=True)

    def success(self, message: str) -> None:
        """Write human success message to stdout.

        Use only for human-readable command output, not JSON mode.
        """
        typer.echo(message)

    @property
    def stdout_is_terminal(self) -> bool:
        return sys.stdout.isatty()

    @property
    def stderr_is_terminal(self) -> bool:
        return sys.stderr.isatty()

    @property
    def stdin_is_terminal(self) -> bool:
        return sys.stdin.isatty()


def render_mapping_text(mapping: dict[str, Any]) -> str:
    """Render a small mapping as aligned human-readable text."""
    if not mapping:
        return ""

    width = max(len(str(key)) for key in mapping)

    return "\n".join(f"{key:<{width}}  {value}" for key, value in mapping.items())


def render_output(
    payload: Any,
    *,
    output_format: OutputFormat,
    output: CliOutput,
    plain_value: object | None = None,
) -> None:
    """Generic output router for simple command results.

    For more complex output, prefer dedicated renderers.
    """
    if output_format == OutputFormat.JSON:
        if isinstance(payload, (dict, list)):
            output.json(payload)
            return

        output.json({"value": payload})
        return

    if output_format == OutputFormat.PLAIN:
        output.plain(payload if plain_value is None else plain_value)
        return

    if isinstance(payload, dict):
        output.data(render_mapping_text(payload))
        return

    output.data(str(payload))
