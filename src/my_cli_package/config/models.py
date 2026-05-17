from __future__ import annotations

from enum import StrEnum
from pathlib import Path
from platformdirs import user_data_dir
from pydantic import BaseModel, ConfigDict, Field, field_validator


class OutputFormat(StrEnum):
    TEXT = "text"
    JSON = "json"
    PLAIN = "plain"


class ColorMode(StrEnum):
    AUTO = "auto"
    ALWAYS = "always"
    NEVER = "never"


class PartialHistoryConfig(BaseModel):
    """Partial history config used by files, profiles, env, and CLI overrides."""

    model_config = ConfigDict(extra="forbid")

    enabled: bool | None = None
    path: Path | None = None

    @field_validator("path")
    @classmethod
    def expand_path(cls, value: Path | None) -> Path | None:
        if value is None:
            return None
        return value.expanduser()


class PartialConfig(BaseModel):
    """Partial config where every field is optional.

    Used for config files, env vars, profile overrides, and CLI overrides.
    """

    model_config = ConfigDict(extra="forbid")

    output_format: OutputFormat | None = Field(default=None, alias="format")
    color: ColorMode | None = None
    quiet: bool | None = None
    verbose: bool | None = None
    debug: bool | None = None
    non_interactive: bool | None = None
    no_progress: bool | None = None
    history: PartialHistoryConfig = Field(default_factory=PartialHistoryConfig)

    model_config = ConfigDict(
        extra="forbid",
        populate_by_name=True,
    )


class ConfigFile(BaseModel):
    """Top-level structure of a config file.

    Supports base config plus profile-specific overrides.
    """

    model_config = ConfigDict(
        extra="forbid",
        populate_by_name=True,
    )

    default_profile: str | None = None

    output_format: OutputFormat | None = Field(default=None, alias="format")
    color: ColorMode | None = None
    quiet: bool | None = None
    verbose: bool | None = None
    debug: bool | None = None
    non_interactive: bool | None = None
    no_progress: bool | None = None
    history: PartialHistoryConfig = Field(default_factory=PartialHistoryConfig)

    profiles: dict[str, PartialConfig] = Field(default_factory=dict)

    def base_config(self) -> PartialConfig:
        return PartialConfig(
            output_format=self.output_format,
            color=self.color,
            quiet=self.quiet,
            verbose=self.verbose,
            debug=self.debug,
            non_interactive=self.non_interactive,
            no_progress=self.no_progress,
            history=self.history,
        )


class RuntimeConfig(BaseModel):
    """Fully resolved runtime config used by the rest of the application."""

    model_config = ConfigDict(extra="forbid")

    output_format: OutputFormat
    color: ColorMode
    quiet: bool
    verbose: bool
    debug: bool
    non_interactive: bool
    no_progress: bool
    history_enabled: bool
    history_path: Path
    active_profile: str | None = None

def default_history_path() -> Path:
    return Path(user_data_dir("my_package", appauthor=False)) / "history.json"


def default_runtime_config() -> RuntimeConfig:
    return RuntimeConfig(
        output_format=OutputFormat.TEXT,
        precision=None,
        color=ColorMode.AUTO,
        quiet=False,
        verbose=False,
        debug=False,
        non_interactive=False,
        no_progress=False,
        history_enabled=True,
        history_path=default_history_path(),
        active_profile=None,
    )