#!/usr/bin/env python3
"""Generate CLI reference documentation with Typer's docs utility.

Overwrites ``docs/reference/cli.md`` with Typer-generated Markdown.

Usage::

    python scripts/generate_cli_reference.py my_cli_package
    python scripts/generate_cli_reference.py my_cli_package --name my_package
"""

from __future__ import annotations

import argparse
import importlib
from pathlib import Path

import typer
import typer.main
from typer.cli import get_docs_for_click

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = REPO_ROOT / "docs/reference/cli.md"
CLI_APP_ATTR = "app"


def _cli_app_module(package: str) -> str:
    return f"{package}.cli.app"


def _load_typer_app(package: str) -> typer.Typer:
    module = importlib.import_module(_cli_app_module(package))
    obj = getattr(module, CLI_APP_ATTR)
    if not isinstance(obj, typer.Typer):
        msg = f"Not a Typer application: {_cli_app_module(package)}:{CLI_APP_ATTR} ({type(obj)!r})"
        raise TypeError(msg)
    return obj


def _program_name(app: typer.Typer, override: str | None, package: str) -> str:
    if override:
        return override
    if app.info.name:
        return app.info.name
    return package


def generate_markdown(
    app: typer.Typer,
    *,
    name: str,
    title: str | None,
) -> str:
    click_command = typer.main.get_command(app)
    ctx = click_command.make_context(name, [], resilient_parsing=True)
    return get_docs_for_click(obj=click_command, ctx=ctx, name=name, title=title)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "package",
        help="Python package name, e.g. my_package (loads {package}.cli.app).",
    )
    parser.add_argument(
        "--name",
        default=None,
        help="CLI program name shown in generated usage examples (default: Typer app name).",
    )
    parser.add_argument(
        "--title",
        default=None,
        help="Optional title for the generated docs page.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT,
        help=f"Output markdown file (default: {DEFAULT_OUTPUT}).",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Exit with code 1 if the output file would change.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)

    app = _load_typer_app(args.package)
    program_name = _program_name(app, args.name, args.package)
    title = args.title or f"`{program_name}` CLI"
    markdown = f"{generate_markdown(app, name=program_name, title=title).strip()}\n"

    output_path = args.output.resolve()
    current = output_path.read_text(encoding="utf-8") if output_path.exists() else ""

    if current == markdown:
        print("CLI reference already up to date.")
        return 0

    if args.check:
        print("CLI reference is stale. Run the generate_cli_reference script.")
        return 1

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(markdown, encoding="utf-8")
    print(f"Updated CLI reference → {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
