# Commands

## `contract-check validate`

Validate a single contract from a file or stdin.

### Usage

```bash
contract-check validate SOURCE [OPTIONS]
```

### Arguments

| Argument | Required | Description                                         |
| -------- | -------: | --------------------------------------------------- |
| `SOURCE` |      Yes | Path to a contract file, or `-` to read from stdin. |

### Options

| Option                 |       Default | Description                                        |
| ---------------------- | ------------: | -------------------------------------------------- |
| `--format`, `-f`       |       `table` | Output format: `table`, `json`, `markdown`, `csv`. |
| `--profile`            |         unset | Configuration profile to use.                      |
| `--strict/--no-strict` | `--no-strict` | Treat warnings as failures.                        |
| `--output`, `-o`       |        stdout | Write result to a file instead of stdout.          |
| `--no-color`           |         false | Disable colored terminal output.                   |
| `--verbose`, `-v`      |         false | Enable verbose diagnostics on stderr.              |

### Output

The validation report is written to stdout unless `--output` is provided.

Diagnostics, warnings, progress messages, and debug logs are written to stderr.

### Exit codes

|  Code | Meaning                                     |
| ----: | ------------------------------------------- |
|   `0` | Validation completed and passed.            |
|   `1` | Validation completed but issues were found. |
|   `2` | Invalid CLI usage or invalid input.         |
|   `3` | Configuration error.                        |
|   `4` | External system error.                      |
| `130` | Interrupted by Ctrl+C.                      |

### Examples

Validate a file:

```bash
contract-check validate contract.yaml
```

Validate and write JSON:

```bash
contract-check validate contract.yaml --format json > report.json
```

Read from stdin:

```bash
cat contract.yaml | contract-check validate - --format json
```

Write Markdown report:

```bash
contract-check validate contract.yaml --format markdown > report.md
```

Save diagnostics separately:

```bash
contract-check validate contract.yaml --format json > report.json 2> debug.log
```

---

Example for `validate-many`:

## `contract-check validate-many`

Validate multiple contract files.

### Usage

```bash
contract-check validate-many SOURCES... [OPTIONS]
```

### Arguments

| Argument     | Required | Description                                                         |
| ------------ | -------: | ------------------------------------------------------------------- |
| `SOURCES...` |      Yes | One or more contract files. Shell globs are supported by the shell. |

### Options

| Option                | Default | Description                                                   |
| --------------------- | ------: | ------------------------------------------------------------- |
| `--format`, `-f`      | `table` | Output format: `table`, `json`, `ndjson`, `markdown`.         |
| `--fail-fast`         |   false | Stop after the first execution error.                         |
| `--continue-on-error` |    true | Continue validating remaining files after a file-level error. |
| `--summary-only`      |   false | Print only aggregate summary.                                 |

### Output modes

`json` emits one aggregate JSON document.

`ndjson` emits one JSON object per validated file. Use this for streaming and pipelines.

### Examples

Validate shell-expanded files:

```bash
contract-check validate-many contracts/*.yaml
```

Validate recursively using an app-level pattern:

```bash
contract-check validate-many --pattern "contracts/**/*.yaml"
```

Stream NDJSON and filter failed contracts:

```bash
contract-check validate-many contracts/*.yaml --format ndjson \
  | jq 'select(.status != "passed")'
```
