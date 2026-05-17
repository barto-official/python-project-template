from __future__ import annotations

from typing import Annotated

import typer

from my_package.cli.context import get_cli_context
from my_package.cli.options import FormatOption

app = typer.Typer(no_args_is_help=True)


@app.command()
def example(
    ctx: typer.Context,
    path: Annotated[str, typer.Argument(help="Input path.")],
    output_format: FormatOption = None,
) -> None:
    cli_context = get_cli_context(ctx)

    result = cli_context.container.some_service.run(path)

    cli_context.container.result_renderer.render(
        result,
        output_format=output_format or cli_context.runtime_config.output_format,
    )
