# Getting Started

This guide helps you install the CLI and run your first commands.


# Installation

## Requirements

Before installing the CLI, ensure you have:

- Python 3.11+
- `uv` installed (recommended)
- A supported terminal:
  - macOS Terminal / iTerm2
  - Linux terminal
  - Windows Terminal / PowerShell

---

## Install `uv`

`uv` is the recommended package and environment manager.

### macOS / Linux

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Windows (PowerShell)

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Verify installation:

```bash
uv --version
```

---

# Local Development Installation

Clone the repository:

```bash
git clone https://github.com/your-org/your-cli.git
cd your-cli
```

Create a virtual environment:

```bash
uv venv
```

Activate the environment.

### macOS / Linux

```bash
source .venv/bin/activate
```

### Windows

```powershell
.venv\Scripts\activate
```

Install dependencies:

```bash
uv sync
```

---

# Verify Installation

Run:

```bash
your-cli --help
```

Expected output:

```text
Usage: your-cli [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.
```

---

# Quickstart

## Show Available Commands

```bash
your-cli --help
```

Show help for a specific command:

```bash
your-cli validate --help
```

---

# Basic Command Execution

Example:

```bash
your-cli validate contracts/
```

Example output:

```text
Validating contracts...

✓ users_contract
✓ payments_contract
✗ events_contract

Validation completed with 1 issue.
```

---

# Reading Input from stdin

The CLI supports Unix-style piping.

Example:

```bash
cat contracts.txt | your-cli validate
```

---

# Output Formats

Many commands support multiple output formats.

## Terminal Output

```bash
your-cli validate contracts/
```

## JSON Output

```bash
your-cli validate contracts/ --output json
```

## Markdown Report

```bash
your-cli validate contracts/ --output markdown
```

---

# Configuration

The CLI supports configuration through:

1. CLI arguments
2. Environment variables
3. Configuration files

Priority order:

```text
CLI arguments > Environment variables > Config file > Defaults
```

Example:

```bash
export YOUR_CLI_ENV=prod
```

---

# Shell Completion

Enable shell completion for a better terminal experience.

## Bash

```bash
eval "$(_YOUR_CLI_COMPLETE=bash_source your-cli)"
```

## Zsh

```bash
eval "$(_YOUR_CLI_COMPLETE=zsh_source your-cli)"
```

---

# Common Development Commands

Run linting:

```bash
ruff check .
```

Run formatting:

```bash
ruff format .
```

Run tests:

```bash
pytest
```

Build the package:

```bash
uv build
```

---

# Troubleshooting

## Command Not Found

Ensure:

* the virtual environment is activated
* the package is installed
* the executable is on your `PATH`

Verify:

```bash
which your-cli
```

---

## Unicode / Encoding Issues

Use UTF-8 compatible terminals.

Recommended:

* Windows Terminal
* iTerm2
* modern Linux terminals

---

## Dependency Issues

Reinstall dependencies:

```bash
uv sync --reinstall
```
