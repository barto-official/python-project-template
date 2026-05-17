# Reference

- **[CLI Reference](cli.md)** — command-line usage. Regenerate with `python scripts/generate_cli_reference.py my_package` (not part of the Python API autogen).
- **Python API** — under *Python API* in the sidebar; module pages are generated at build time from docstrings (`scripts/gen_ref_pages.py`).

Configure Python API scope in `mkdocs.yml` under `extra.api_reference` (`packages`, `public_only`, `exclude`). `my_package.cli` is excluded; CLI lives only in `cli.md`.
