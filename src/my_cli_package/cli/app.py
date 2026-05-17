from __future__ import annotations

from typing import Annotated

import typer

from my_package.cli import options as cli_options
from my_package.cli.commands import config, doctor
from my_package.cli.context import GlobalCliOptions, build_cli_context
from my_package.runtime.logging import configure_logging
from my_package.version import __version__

app = typer.Typer(
    name="my_package",
    help="Professional CLI for my_package.",
    no_args_is_help=True,
    add_completion=True,
    rich_markup_mode="rich",
)


def _version_callback(value: bool) -> None:
    if value:
        typer.echo(__version__)
        raise typer.Exit(code=0)


@app.callback()
def root(
    ctx: typer.Context,
    version: Annotated[
        bool,
        typer.Option(
            "--version",
            callback=_version_callback,
            is_eager=True,
            help="Show version and exit.",
        ),
    ] = False,
    config_path: cli_options.ConfigPathOption = None,
    profile: cli_options.ProfileOption = None,
    verbose: cli_options.VerboseOption = False,
    quiet: cli_options.QuietOption = False,
    debug: cli_options.DebugOption = False,
    non_interactive: cli_options.NonInteractiveOption = False,
    color: cli_options.ColorOption = None,
    no_progress: cli_options.NoProgressOption = False,
) -> None:
    """Initialize global CLI runtime state before dispatching subcommands."""

    if verbose and quiet:
        typer.echo(
            "Invalid options: --verbose and --quiet cannot be used together.",
            err=True,
        )
        raise typer.Exit(code=2)

    global_options = GlobalCliOptions(
        config_path=config_path,
        profile=profile,
        verbose=verbose,
        quiet=quiet,
        debug=debug,
        non_interactive=non_interactive,
        color=color,
        no_progress=no_progress,
    )

    configure_logging(
        quiet=quiet,
        verbose=verbose,
        debug=debug,
    )

    ctx.obj = build_cli_context(global_options)


app.add_typer(
    config.app,
    name="config",
    help="Inspect and manage configuration.",
)

app.add_typer(
    doctor.app,
    name="doctor",
    help="Diagnose local environment and installation.",
)
