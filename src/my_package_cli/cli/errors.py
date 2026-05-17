from __future__ import annotations

import json
import logging
from dataclasses import dataclass, field
from typing import Any, NoReturn

import typer

from my_package.cli.context import CliContext
from my_package.cli.output import ColorMode, OutputPolicy
from my_package.config.errors import ConfigurationError
from my_package.domain.errors import DomainError
from my_package.domain.exit_codes import ExitCode

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class ErrorDetail:
    """Structured detail for a specific error issue."""

    location: str | None = None
    problem: str | None = None
    expected: str | None = None
    actual: Any | None = None
    fix: str | None = None


@dataclass(frozen=True)
class CliErrorPayload:
    """Structured CLI error representation.

    The same payload can be rendered as human-readable text or JSON.
    """

    type: str
    message: str
    exit_code: int
    retriable: bool = False
    details: list[ErrorDetail] = field(default_factory=list)


class UserCancelledError(Exception):
    """Raised when the user intentionally cancels an interactive action."""


def handle_cli_error(exc: Exception, *, context: CliContext) -> NoReturn:
    """Map internal exceptions to CLI stderr output and process exit codes.

    Expected errors become structured payloads.
    Unexpected errors are hidden unless --debug is enabled.
    """
    payload = map_exception_to_payload(exc)

    if payload is not None:
        render_error_payload(
            payload,
            output_format=_get_error_output_format(context),
        )
        raise typer.Exit(code=payload.exit_code)

    logger.exception("Unhandled internal error")

    if context.debug:
        raise

    payload = CliErrorPayload(
        type="internal_error",
        message="Internal error. Re-run with --debug for details.",
        exit_code=int(ExitCode.INTERNAL_ERROR),
        retriable=False,
    )

    render_error_payload(
        payload,
        output_format=_get_error_output_format(context),
    )
    raise typer.Exit(code=payload.exit_code)


def map_exception_to_payload(exc: Exception) -> CliErrorPayload | None:
    """Convert expected exceptions to structured CLI error payloads."""

    if isinstance(exc, InvalidInputError):
        return CliErrorPayload(
            type="invalid_input",
            message=f"Invalid input: {exc}",
            exit_code=int(ExitCode.INVALID_INPUT),
            retriable=False,
        )

    if isinstance(exc, ConfigurationError):
        return CliErrorPayload(
            type="configuration_error",
            message=f"Configuration error: {exc}",
            exit_code=int(ExitCode.CONFIGURATION_ERROR),
            retriable=False,
        )

    if isinstance(exc, UserCancelledError):
        return CliErrorPayload(
            type="user_cancelled",
            message="Aborted.",
            exit_code=int(ExitCode.SUCCESS),
            retriable=False,
        )

    if isinstance(exc, DomainError):
        return CliErrorPayload(
            type="domain_error",
            message=f"Domain error: {exc}",
            exit_code=int(ExitCode.DOMAIN_ERROR),
            retriable=False,
        )

    return None


def render_error_payload(
    payload: CliErrorPayload,
    *,
    output_format: str,
) -> None:
    """Render a structured error payload to stderr."""

    if output_format == "json":
        typer.echo(
            json.dumps(
                {
                    "error": {
                        "type": payload.type,
                        "message": payload.message,
                        "exit_code": payload.exit_code,
                        "retriable": payload.retriable,
                        "details": [
                            {
                                "location": detail.location,
                                "problem": detail.problem,
                                "expected": detail.expected,
                                "actual": detail.actual,
                                "fix": detail.fix,
                            }
                            for detail in payload.details
                        ],
                    }
                },
                default=str,
                separators=(",", ":"),
                sort_keys=True,
            ),
            err=True,
        )
        return

    typer.echo(format_human_error(payload), err=True)


def format_human_error(payload: CliErrorPayload) -> str:
    """Render a structured error payload as readable terminal text."""

    lines: list[str] = [payload.message]

    for detail in payload.details:
        detail_lines: list[str] = []

        if detail.location:
            detail_lines.append(f"Location: {detail.location}")

        if detail.problem:
            detail_lines.append(f"Problem: {detail.problem}")

        if detail.expected:
            detail_lines.append(f"Expected: {detail.expected}")

        if detail.actual is not None:
            detail_lines.append(f"Actual: {detail.actual}")

        if detail.fix:
            detail_lines.append(f"Fix: {detail.fix}")

        if detail_lines:
            lines.append("")
            lines.extend(detail_lines)

    if payload.retriable:
        lines.append("")
        lines.append("This error may be temporary. Retry the command later.")

    return "\n".join(lines)


def fail(
    message: str,
    *,
    context: CliContext,
    code: ExitCode = ExitCode.INVALID_INPUT,
    type_: str = "invalid_input",
    details: list[ErrorDetail] | None = None,

) -> NoReturn:

    payload = CliErrorPayload(
        type=type_,
        message=message,
        exit_code=int(code),
        retriable=False,
        details=details or [],
    )
    render_error_payload(
        payload,
        output_format=_get_error_output_format(context),
    )

    raise typer.Exit(code=int(code)
)


def require_confirmation(
    *,
    prompt: str,
    yes: bool,
    non_interactive: bool,
    dry_run: bool = False,
) -> None:
    """Handle confirmation policy for side-effecting commands.

    Policy:
      - dry-run does not require confirmation
      - --yes bypasses prompt
      - non-interactive mode cannot prompt
      - interactive mode prompts
    """
    if dry_run or yes:
        return

    if non_interactive:
        raise InvalidInputError(
            "confirmation required in non-interactive mode. "
            "Use --yes to apply or --dry-run to preview."
        )

    confirmed = typer.confirm(prompt, default=False)

    if not confirmed:
        raise UserCancelledError()


def _get_error_output_format(context: CliContext) -> str:
    """Return error rendering mode.

    If the resolved output format is JSON, errors are JSON too.
    Otherwise errors are human-readable text.
    """
    output_format = getattr(context.runtime_config, "output_format", "text")

    if hasattr(output_format, "value"):
        return str(output_format.value)

    return str(output_format)

def _normalize_color(value: str | None) -> ColorMode:
    if value is None:
        return ColorMode.AUTO

    try:
        return ColorMode(value)
    except ValueError:
        return ColorMode.AUTO