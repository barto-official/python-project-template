"""Minimal Typer application for template docs and CLI reference generation."""

from __future__ import annotations

import typer

app = typer.Typer(help="my_package CLI template.", no_args_is_help=True)


@app.command()
def ping() -> None:
    """Print a short acknowledgement (smoke-test friendly)."""

    typer.echo("pong")


if __name__ == "__main__":
    app()
