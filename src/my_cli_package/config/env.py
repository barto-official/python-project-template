from __future__ import annotations

import os
from pathlib import Path
from typing import Any

from pydantic import ValidationError

from my_package.config.errors import ConfigurationError
from my_package.config.models import PartialConfig


def load_env_config() -> tuple[PartialConfig, str | None]:
    """Load configuration overrides from environment variables.

    Returns:
        A tuple of `(env_config, env_profile)`.
    """

    raw: dict[str, Any] = {}

    _set_if_present(raw, "format", "FORMAT")
    _set_if_present(raw, "color", "COLOR")
    _set_if_present(raw, "quiet", "QUIET", parser=parse_bool)
    _set_if_present(raw, "verbose", "VERBOSE", parser=parse_bool)
    _set_if_present(raw, "debug", "DEBUG", parser=parse_bool)
    _set_if_present(raw, "non_interactive", "NON_INTERACTIVE", parser=parse_bool)
    _set_if_present(raw, "no_progress", "NO_PROGRESS", parser=parse_bool)

    history: dict[str, Any] = {}
    _set_if_present(history, "enabled", "HISTORY_ENABLED", parser=parse_bool)
    _set_if_present(history, "path", "HISTORY_PATH", parser=Path)

    if history:
        raw["history"] = history

    profile = _empty_to_none(os.getenv("PROFILE"))

    try:
        return PartialConfig.model_validate(raw), profile
    except ValidationError as exc:
        raise ConfigurationError(format_env_validation_error(exc)) from exc


def _set_if_present(
    target: dict[str, Any],
    key: str,
    env_name: str,
    *,
    parser=None,
) -> None:
    raw = _empty_to_none(os.getenv(env_name))

    if raw is None:
        return

    try:
        target[key] = parser(raw) if parser is not None else raw
    except ValueError as exc:
        raise ConfigurationError(f"{env_name}: invalid value {raw!r}: {exc}") from exc


def _empty_to_none(value: str | None) -> str | None:
    if value is None:
        return None

    stripped = value.strip()

    if stripped == "":
        return None

    return stripped


def parse_bool(value: str) -> bool:
    normalized = value.strip().lower()

    if normalized in {"1", "true", "yes", "y", "on"}:
        return True

    if normalized in {"0", "false", "no", "n", "off"}:
        return False

    raise ValueError("expected one of: 1, 0, true, false, yes, no, on, off")


def format_env_validation_error(exc: ValidationError) -> str:
    messages: list[str] = []

    for error in exc.errors():
        location = ".".join(str(part) for part in error["loc"])
        message = error["msg"]
        messages.append(f"environment: {location}: {message}")

    return "\n".join(messages)
