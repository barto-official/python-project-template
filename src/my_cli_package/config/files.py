from __future__ import annotations

import tomllib
from pathlib import Path
from typing import Any

from pydantic import ValidationError

from my_package.config.errors import ConfigurationError
from my_package.config.models import ConfigFile


def load_config_file(path: Path) -> ConfigFile:
    """Load and validate a TOML config file."""

    resolved_path = path.expanduser().resolve()

    if not resolved_path.exists():
        raise ConfigurationError(f"config file not found: {resolved_path}")

    if not resolved_path.is_file():
        raise ConfigurationError(f"config path is not a file: {resolved_path}")

    try:
        with resolved_path.open("rb") as file:
            raw_data = tomllib.load(file)
    except tomllib.TOMLDecodeError as exc:
        raise ConfigurationError(f"{resolved_path}: invalid TOML: {exc}") from exc
    except OSError as exc:
        raise ConfigurationError(f"{resolved_path}: cannot read config file: {exc}") from exc

    return parse_config_data(raw_data, source=resolved_path)


def parse_config_data(data: dict[str, Any], *, source: Path) -> ConfigFile:
    try:
        return ConfigFile.model_validate(data)
    except ValidationError as exc:
        raise ConfigurationError(format_validation_error(exc, source=source)) from exc


def format_validation_error(exc: ValidationError, *, source: Path) -> str:
    messages: list[str] = []

    for error in exc.errors():
        location = ".".join(str(part) for part in error["loc"])
        message = error["msg"]
        messages.append(f"{source}: {location}: {message}")

    return "\n".join(messages)
