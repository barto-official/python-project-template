from __future__ import annotations

from pathlib import Path

from platformdirs import user_data_dir

from my_package.config.models import ColorMode, OutputFormat, RuntimeConfig


def default_history_path() -> Path:
    return Path(user_data_dir("my_package", appauthor=False)) / "history.json"


def default_runtime_config() -> RuntimeConfig:
    return RuntimeConfig(
        output_format=OutputFormat.TEXT,
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