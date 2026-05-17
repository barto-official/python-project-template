from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Literal

from platformdirs import user_config_dir

from my_package.config.errors import ConfigurationError

ConfigKind = Literal["explicit", "project", "user"]


@dataclass(frozen=True)
class ConfigLocation:
    path: Path
    kind: ConfigKind


PROJECT_CONFIG_NAMES = ("my_package.toml",)


def get_user_config_path() -> Path:
    return Path(user_config_dir("my_package", appauthor=False)) / "config.toml"


def discover_user_config() -> ConfigLocation | None:
    path = get_user_config_path()

    if path.is_file():
        return ConfigLocation(path=path, kind="user")

    return None


def discover_project_config(start: Path | None = None) -> ConfigLocation | None:
    current = (start or Path.cwd()).resolve()

    for directory in (current, *current.parents):
        for name in PROJECT_CONFIG_NAMES:
            candidate = directory / name
            if candidate.is_file():
                return ConfigLocation(path=candidate, kind="project")

    return None


def resolve_explicit_config(path: Path) -> ConfigLocation:
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
    """Return `(user_config, project_config)`.

    If explicit_config_path is provided, it is used as the project-level config source.
    Missing explicit config is an error.
    Missing discovered config is not an error.
    """

    user_location = discover_user_config()

    if explicit_config_path is not None:
        project_location = resolve_explicit_config(explicit_config_path)
    else:
        project_location = discover_project_config(start=start)

    return user_location, project_location
