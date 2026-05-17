from __future__ import annotations

from pathlib import Path
from typing import Annotated, Literal

import typer


OutputFormat = Literal["text", "json", "plain"]
ColorMode = Literal["auto", "always", "never"]


ConfigPathOption = Annotated[
    Path | None,
    typer.Option(
        "--config",
        "-c",
        help="Path to a configuration file.",
        exists=False,
        file_okay=True,
        dir_okay=False,
        resolve_path=True,
    ),
]


ProfileOption = Annotated[
    str | None,
    typer.Option(
        "--profile",
        help="Configuration profile to use, for example dev, staging, prod, or ci.",
    ),
]


VerboseOption = Annotated[
    bool,
    typer.Option(
        "--verbose",
        "-v",
        help="Enable diagnostic output.",
    ),
]


QuietOption = Annotated[
    bool,
    typer.Option(
        "--quiet",
        "-q",
        help="Suppress non-essential diagnostic output.",
    ),
]


DebugOption = Annotated[
    bool,
    typer.Option(
        "--debug",
        help="Enable debug logging and show internal tracebacks.",
    ),
]


NonInteractiveOption = Annotated[
    bool,
    typer.Option(
        "--non-interactive",
        help="Disable prompts. Fail fast if confirmation would be required.",
    ),
]


ColorOption = Annotated[
    ColorMode | None,
    typer.Option(
        "--color",
        help="Color mode: auto, always, or never.",
        case_sensitive=False,
    ),
]


NoProgressOption = Annotated[
    bool,
    typer.Option(
        "--no-progress",
        help="Disable progress bars and spinners.",
    ),
]


FormatOption = Annotated[
    OutputFormat | None,
    typer.Option(
        "--format",
        help="Output format: text, json, or plain.",
        case_sensitive=False,
    ),
]


PrettyJsonOption = Annotated[
    bool,
    typer.Option(
        "--pretty",
        help="Pretty-print JSON output.",
    ),
]


DryRunOption = Annotated[
    bool,
    typer.Option(
        "--dry-run",
        help="Preview side effects without applying changes.",
    ),
]


YesOption = Annotated[
    bool,
    typer.Option(
        "--yes",
        "-y",
        help="Skip confirmation prompts.",
    ),
]