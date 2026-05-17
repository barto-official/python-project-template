from __future__ import annotations

from my_package.config.errors import ConfigurationError
from my_package.config.models import ConfigFile, PartialConfig, PartialHistoryConfig


def select_active_profile(
    *,
    explicit_profile: str | None,
    env_profile: str | None,
    project_config: ConfigFile | None,
    user_config: ConfigFile | None,
) -> tuple[str | None, str]:
    """Select active profile and source according to precedence."""

    if explicit_profile is not None:
        return explicit_profile, "cli:--profile"

    if env_profile is not None:
        return env_profile, "env:PROFILE"

    if project_config is not None and project_config.default_profile is not None:
        return project_config.default_profile, "project:default_profile"

    if user_config is not None and user_config.default_profile is not None:
        return user_config.default_profile, "user:default_profile"

    return None, "default"


def apply_profile(
    *,
    config_file: ConfigFile | None,
    profile: str | None,
    source_name: str,
) -> PartialConfig | None:
    """Return base config overlaid with selected profile config."""

    if config_file is None:
        return None

    base = config_file.base_config()

    if profile is None:
        return base

    profile_config = config_file.profiles.get(profile)

    if profile_config is None:
        # Missing profile is ignored only if file has no profiles at all.
        # If profiles exist, the selected profile should be valid for that file.
        if config_file.profiles:
            available = ", ".join(sorted(config_file.profiles))
            raise ConfigurationError(
                f"{source_name}: profile {profile!r} does not exist. "
                f"Available profiles: {available}."
            )

        return base

    return merge_partial_config(
        lower=base,
        higher=profile_config,
    )


def merge_partial_config(
    *,
    lower: PartialConfig,
    higher: PartialConfig,
) -> PartialConfig:
    """Merge two partial configs. Non-None values in `higher` win."""

    return PartialConfig(
        output_format=higher.output_format if higher.output_format is not None else lower.output_format,
        precision=higher.precision if higher.precision is not None else lower.precision,
        color=higher.color if higher.color is not None else lower.color,
        quiet=higher.quiet if higher.quiet is not None else lower.quiet,
        verbose=higher.verbose if higher.verbose is not None else lower.verbose,
        debug=higher.debug if higher.debug is not None else lower.debug,
        non_interactive=(
            higher.non_interactive
            if higher.non_interactive is not None
            else lower.non_interactive
        ),
        no_progress=(
            higher.no_progress
            if higher.no_progress is not None
            else lower.no_progress
        ),
        history=merge_history_config(
            lower=lower.history,
            higher=higher.history,
        ),
    )


def merge_history_config(
    *,
    lower: PartialHistoryConfig,
    higher: PartialHistoryConfig,
) -> PartialHistoryConfig:
    return PartialHistoryConfig(
        enabled=higher.enabled if higher.enabled is not None else lower.enabled,
        path=higher.path if higher.path is not None else lower.path,
    )