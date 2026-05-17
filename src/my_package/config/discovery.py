"""Locate standard configuration files used by ``my_package`` (library layer).

This duplicates the resolver-facing discovery helpers that also exist under ``my_package_cli``
so wheels that ship ``my_package`` alone do not need the CLI scaffold on ``PYTHONPATH``.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Literal

from platformdirs import user_config_dir

from my_package.config.errors import ConfigurationError

ConfigKind = Literal["explicit", "project", "user"]


@dataclass(frozen=True)
class ConfigLocation:
    """Describes where a resolved configuration file was found."""

    path: Path
    kind: ConfigKind


PROJECT_CONFIG_NAMES = ("my_package.toml",)


def get_user_config_path() -> Path:
    """Return the canonical per-user ``my_package`` configuration file.

    Returns:
        Absolute-ish path pointing at the user's expected ``config.toml`` location.
    """

    return Path(user_config_dir("my_package", appauthor=False)) / "config.toml"


def discover_user_config() -> ConfigLocation | None:
    """Locate the user-scope config file if present.

    Returns:
        A ``ConfigLocation`` pointing at an existing user file; otherwise ``None``.
    """

    path = get_user_config_path()

    if path.is_file():
        return ConfigLocation(path=path, kind="user")

    return None


def discover_project_config(start: Path | None = None) -> ConfigLocation | None:
    """Walk ancestor directories searching for ``my_package.toml``.

    Args:
        start: Directory to begin probing from (defaults to the process working dir).

    Returns:
        Location metadata when a matching file exists; otherwise ``None``.
    """

    current = (start or Path.cwd()).resolve()

    for directory in (current, *current.parents):
        for name in PROJECT_CONFIG_NAMES:
            candidate = directory / name
            if candidate.is_file():
                return ConfigLocation(path=candidate, kind="project")

    return None


def resolve_explicit_config(path: Path) -> ConfigLocation:
    """Normalize *path* and ensure it resolves to an existing plain file.

    Args:
        path: User-provided filesystem path referencing a concrete file.

    Returns:
        Wrapped ``ConfigLocation`` tagged ``explicit``.

    Raises:
        ConfigurationError: When the path is missing or not a file.
    """

    resolved = path.expanduser().resolve()

    if not resolved.exists():
        raise ConfigurationError(f"config file not found: {resolved}")

    if not resolved.is_file():
        raise ConfigurationError(f"config path is not a file: {resolved}")

    return ConfigLocation(path=resolved, kind="explicit")


def discover_config_locations(
    *,
    explicit_config_path: Path | None,
    start: Path | None = None,
) -> tuple[ConfigLocation | None, ConfigLocation | None]:
    """Return ``(user_config, project_config)``.

    Args:
        explicit_config_path: If set, validates and resolves that project-level file.
        start: Starting directory used when probing for ``my_package.toml``.

    Returns:
        A tuple of discovered user/project locations; either side may be ``None``.
    """

    user_location = discover_user_config()

    project_location: ConfigLocation | None
    if explicit_config_path is not None:
        project_location = resolve_explicit_config(explicit_config_path)
    else:
        project_location = discover_project_config(start=start)

    return user_location, project_location
