

This page documents the public command-line interface for `contract-check`.

Use this reference when you need exact command syntax, options, input behavior, output behavior, and exit codes.

For a guided first run, see [Quickstart](quickstart.md).

## Global behavior

`contract-check` follows these stream conventions:

| Stream | Purpose |
|---|---|
| `stdout` | Primary command result: reports, JSON, CSV, Markdown, table output. |
| `stderr` | Diagnostics: logs, warnings, progress, prompts, debug messages. |
| `stdin` | Optional input channel when `-` is used as the source. |

Common global options:

| Option | Description |
|---|---|
| `--help` | Show help and exit. |
| `--version` | Show version and exit. |
| `--verbose`, `-v` | Enable verbose diagnostics. |
| `--quiet`, `-q` | Suppress non-essential diagnostics. |
| `--no-color` | Disable colored terminal output. |
| `--config PATH` | Use a specific configuration file. |

## Exit codes

| Code | Meaning |
|---:|---|
| `0` | Command completed successfully. |
| `1` | Validation completed, but issues were found. |
| `2` | Invalid command usage or invalid input. |
| `3` | Configuration error. |
| `4` | External system error, such as Databricks/API failure. |
| `5` | Unexpected internal error. |
| `130` | Interrupted by Ctrl+C. |

---

## `contract-check validate`

Validate a single data contract from a file or from standard input.

### Usage

```bash
contract-check validate SOURCE [OPTIONS]
```

### Arguments

| Argument | Required | Description                                         |
| -------- | -------: | --------------------------------------------------- |
| `SOURCE` |      Yes | Path to a contract file, or `-` to read from stdin. |

### Options

| Option                 |       Default | Description                                           |
| ---------------------- | ------------: | ----------------------------------------------------- |
| `--format`, `-f`       |       `table` | Output format: `table`, `json`, `markdown`, or `csv`. |
| `--output`, `-o`       |        stdout | Write primary result to a file instead of stdout.     |
| `--profile`            |         unset | Configuration profile to use.                         |
| `--strict/--no-strict` | `--no-strict` | Treat warnings as validation failures.                |
| `--no-color`           |         false | Disable colored terminal output.                      |
| `--verbose`, `-v`      |         false | Enable verbose diagnostics.                           |

### Input

`SOURCE` can be a file path:

```bash
contract-check validate contract.yaml
```

Or stdin:

```bash
cat contract.yaml | contract-check validate -
```

The `-` value means “read from standard input.”

### Output

The validation report is written to stdout by default.

Diagnostics, warnings, progress, and debug messages are written to stderr.

### Examples

Validate a file:

```bash
contract-check validate contract.yaml
```

Generate JSON:

```bash
contract-check validate contract.yaml --format json
```

Write JSON to a file:

```bash
contract-check validate contract.yaml --format json > report.json
```

Write Markdown to a file:

```bash
contract-check validate contract.yaml --format markdown > report.md
```

Read from stdin:

```bash
cat contract.yaml | contract-check validate - --format json
```

Separate result and diagnostics:

```bash
contract-check validate contract.yaml --format json > report.json 2> debug.log
```

---

## `contract-check validate-many`

Validate multiple data contract files.

### Usage

```bash
contract-check validate-many SOURCES... [OPTIONS]
```

### Arguments

| Argument     | Required | Description                                                          |
| ------------ | -------: | -------------------------------------------------------------------- |
| `SOURCES...` |      Yes | One or more contract file paths. Shell-expanded globs are supported. |

### Options

| Option                | Default | Description                                                  |
| --------------------- | ------: | ------------------------------------------------------------ |
| `--format`, `-f`      | `table` | Output format: `table`, `json`, `ndjson`, or `markdown`.     |
| `--pattern`, `-p`     |   unset | App-level glob pattern, for example `contracts/**/*.yaml`.   |
| `--fail-fast`         |   false | Stop after the first execution error.                        |
| `--continue-on-error` |    true | Continue processing remaining files after file-level errors. |
| `--summary-only`      |   false | Print only the aggregate summary.                            |
| `--output`, `-o`      |  stdout | Write result to a file instead of stdout.                    |

### Output modes

`json` produces one aggregate JSON document.

`ndjson` produces one JSON object per line and is recommended for streaming pipelines.

### Examples

Validate explicit files:

```bash
contract-check validate-many a.yaml b.yaml c.yaml
```

Validate shell-expanded files:

```bash
contract-check validate-many contracts/*.yaml
```

Validate recursively with app-level globbing:

```bash
contract-check validate-many --pattern "contracts/**/*.yaml"
```

Stream NDJSON and filter failed results:

```bash
contract-check validate-many --pattern "contracts/**/*.yaml" --format ndjson \
  | jq 'select(.status != "passed")'
```

---

## `contract-check config show`

Show the resolved runtime configuration.

### Usage

```bash
contract-check config show [OPTIONS]
```

### Options

| Option           |        Default | Description                                |
| ---------------- | -------------: | ------------------------------------------ |
| `--profile`      | active profile | Show configuration for a specific profile. |
| `--format`, `-f` |        `table` | Output format: `table` or `json`.          |
| `--show-sources` |          false | Show where each setting came from.         |
| `--show-secrets` |          false | Show secret values. Disabled by default.   |

### Examples

Show resolved config:

```bash
contract-check config show
```

Show config as JSON:

```bash
contract-check config show --format json
```

Show where values came from:

```bash
contract-check config show --show-sources
```

Secret values are redacted unless explicitly requested.

---

## `contract-check doctor`

Diagnose installation, configuration, authentication, and connectivity.

### Usage

```bash
contract-check doctor [OPTIONS]
```

### Options

| Option                               |           Default | Description                       |
| ------------------------------------ | ----------------: | --------------------------------- |
| `--profile`                          |    active profile | Profile to diagnose.              |
| `--check-auth/--no-check-auth`       |    `--check-auth` | Check authentication.             |
| `--check-network/--no-check-network` | `--check-network` | Check network/API connectivity.   |
| `--format`, `-f`                     |           `table` | Output format: `table` or `json`. |

### Examples

Run all diagnostics:

```bash
contract-check doctor
```

Run diagnostics for a profile:

```bash
contract-check doctor --profile prod
```

Generate machine-readable diagnostic output:

```bash
contract-check doctor --format json
```
