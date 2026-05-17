# `my_package` CLI

Professional CLI for my_package.

**Usage**:

```console
$ my_package [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--version`: Show version and exit.
* `-c, --config FILE`: Path to a configuration file.
* `--profile TEXT`: Configuration profile to use, for example dev, staging, prod, or ci.
* `-v, --verbose`: Enable diagnostic output.
* `-q, --quiet`: Suppress non-essential diagnostic output.
* `--debug`: Enable debug logging and show internal tracebacks.
* `--non-interactive`: Disable prompts. Fail fast if confirmation would be required.
* `--color [auto|always|never]`: Color mode: auto, always, or never.
* `--no-progress`: Disable progress bars and spinners.
* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.

**Commands**:

* `config`: Inspect and manage configuration.
* `doctor`: Diagnose local environment and installation.

## `my_package config`

Inspect and manage configuration.

**Usage**:

```console
$ my_package config [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `show`: Show the resolved runtime configuration.

### `my_package config show`

Show the resolved runtime configuration.

**Usage**:

```console
$ my_package config show [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.

## `my_package doctor`

Diagnose local environment and installation.

**Usage**:

```console
$ my_package doctor [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `run`: Diagnose local environment and installation.

### `my_package doctor run`

Diagnose local environment and installation.

**Usage**:

```console
$ my_package doctor run [OPTIONS]
```

**Options**:

* `--help`: Show this message and exit.
