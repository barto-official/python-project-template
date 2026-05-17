from __future__ import annotations

from pathlib import Path
from typing import Any

from my_package.config.defaults import default_runtime_config
from my_package.config.discovery import ConfigLocation, discover_config_locations
from my_package.config.env import load_env_config
from my_package.config.files import load_config_file
from my_package.config.models import ConfigFile, PartialConfig, RuntimeConfig
from my_package.config.profiles import apply_profile, select_active_profile
from my_package.config.sources import ResolvedValue, RuntimeConfigSources


def resolve_runtime_config(
    *,
    explicit_config_path: Path | None,
    explicit_profile: str | None,
    cli_overrides: dict[str, Any | None],
    include_sources: bool = False,
) -> RuntimeConfig:
    """Resolve final runtime config.

    Precedence:
      CLI > env > project profile/base > user profile/base > defaults
    """

    result, _sources = resolve_runtime_config_with_sources(
        explicit_config_path=explicit_config_path,
        explicit_profile=explicit_profile,
        cli_overrides=cli_overrides,
        include_sources=include_sources,
    )
    return result


def resolve_runtime_config_with_sources(
    *,
    explicit_config_path: Path | None,
    explicit_profile: str | None,
    cli_overrides: dict[str, Any | None],
    include_sources: bool = True,
) -> tuple[RuntimeConfig, RuntimeConfigSources | None]:
    defaults = default_runtime_config()

    user_location, project_location = discover_config_locations(
        explicit_config_path=explicit_config_path,
    )

    user_file = _load_location(user_location)
    project_file = _load_location(project_location)

    env_config, env_profile = load_env_config()

    active_profile, active_profile_source = select_active_profile(
        explicit_profile=explicit_profile,
        env_profile=env_profile,
        project_config=project_file,
        user_config=user_file,
    )

    user_config = apply_profile(
        config_file=user_file,
        profile=active_profile,
        source_name=_source_name(user_location),
    )

    project_config = apply_profile(
        config_file=project_file,
        profile=active_profile,
        source_name=_source_name(project_location),
    )

    cli_config = PartialConfig.model_validate(
        _normalize_cli_overrides(cli_overrides)
    )

    sources_builder = _SourcesBuilder(active_profile, active_profile_source)

    runtime_config = RuntimeConfig(
        output_format=sources_builder.resolve(
            name="output_format",
            default=defaults.output_format,
            user=_get(user_config, "output_format"),
            project=_get(project_config, "output_format"),
            env=env_config.output_format,
            cli=cli_config.output_format,
        ),
        precision=sources_builder.resolve(
            name="precision",
            default=defaults.precision,
            user=_get(user_config, "precision"),
            project=_get(project_config, "precision"),
            env=env_config.precision,
            cli=cli_config.precision,
        ),
        color=sources_builder.resolve(
            name="color",
            default=defaults.color,
            user=_get(user_config, "color"),
            project=_get(project_config, "color"),
            env=env_config.color,
            cli=cli_config.color,
        ),
        quiet=sources_builder.resolve(
            name="quiet",
            default=defaults.quiet,
            user=_get(user_config, "quiet"),
            project=_get(project_config, "quiet"),
            env=env_config.quiet,
            cli=cli_config.quiet,
        ),
        verbose=sources_builder.resolve(
            name="verbose",
            default=defaults.verbose,
            user=_get(user_config, "verbose"),
            project=_get(project_config, "verbose"),
            env=env_config.verbose,
            cli=cli_config.verbose,
        ),
        debug=sources_builder.resolve(
            name="debug",
            default=defaults.debug,
            user=_get(user_config, "debug"),
            project=_get(project_config, "debug"),
            env=env_config.debug,
            cli=cli_config.debug,
        ),
        non_interactive=sources_builder.resolve(
            name="non_interactive",
            default=defaults.non_interactive,
            user=_get(user_config, "non_interactive"),
            project=_get(project_config, "non_interactive"),
            env=env_config.non_interactive,
            cli=cli_config.non_interactive,
        ),
        no_progress=sources_builder.resolve(
            name="no_progress",
            default=defaults.no_progress,
            user=_get(user_config, "no_progress"),
            project=_get(project_config, "no_progress"),
            env=env_config.no_progress,
            cli=cli_config.no_progress,
        ),
        history_enabled=sources_builder.resolve(
            name="history_enabled",
            default=defaults.history_enabled,
            user=_get_history(user_config, "enabled"),
            project=_get_history(project_config, "enabled"),
            env=env_config.history.enabled,
            cli=cli_config.history.enabled,
        ),
        history_path=sources_builder.resolve(
            name="history_path",
            default=defaults.history_path,
            user=_get_history(user_config, "path"),
            project=_get_history(project_config, "path"),
            env=env_config.history.path,
            cli=cli_config.history.path,
        ),
        active_profile=active_profile,
    )

    if not include_sources:
        return runtime_config, None

    return runtime_config, sources_builder.build()


def _load_location(location: ConfigLocation | None) -> ConfigFile | None:
    if location is None:
        return None

    return load_config_file(location.path)


def _source_name(location: ConfigLocation | None) -> str:
    if location is None:
        return "none"

    return f"{location.kind}:{location.path}"


def _normalize_cli_overrides(overrides: dict[str, Any | None]) -> dict[str, Any]:
    """Drop None values and normalize common external names."""

    normalized: dict[str, Any] = {}

    alias_map = {
        "output_format": "format",
    }

    for key, value in overrides.items():
        if value is None:
            continue

        normalized[alias_map.get(key, key)] = value

    return normalized


def _get(config: PartialConfig | None, name: str) -> Any | None:
    if config is None:
        return None

    return getattr(config, name)


def _get_history(config: PartialConfig | None, name: str) -> Any | None:
    if config is None:
        return None

    return getattr(config.history, name)


class _SourcesBuilder:
    """Internal helper for resolving values and tracking their winning source."""

    def __init__(self, active_profile: str | None, active_profile_source: str) -> None:
        self._values: dict[str, ResolvedValue[Any]] = {}
        self._active_profile = active_profile
        self._active_profile_source = active_profile_source

    def resolve(
        self,
        *,
        name: str,
        default: Any,
        user: Any | None,
        project: Any | None,
        env: Any | None,
        cli: Any | None,
    ) -> Any:
        candidates = (
            ("cli", cli),
            ("env", env),
            ("project", project),
            ("user", user),
            ("default", default),
        )

        for source, value in candidates:
            if value is not None:
                self._values[name] = ResolvedValue(value=value, source=source)
                return value

        # Should not happen because default must always exist.
        self._values[name] = ResolvedValue(value=None, source="unresolved")
        return None

    def build(self) -> RuntimeConfigSources:
        return RuntimeConfigSources(
            output_format=_string_value(self._values["output_format"]),
            precision=self._values["precision"],
            color=_string_value(self._values["color"]),
            quiet=self._values["quiet"],
            verbose=self._values["verbose"],
            debug=self._values["debug"],
            non_interactive=self._values["non_interactive"],
            no_progress=self._values["no_progress"],
            history_enabled=self._values["history_enabled"],
            history_path=_string_value(self._values["history_path"]),
            active_profile=ResolvedValue(
                value=self._active_profile,
                source=self._active_profile_source,
            ),
        )


def _string_value(value: ResolvedValue[Any]) -> ResolvedValue[str]:
    return ResolvedValue(
        value=str(value.value),
        source=value.source,
    )