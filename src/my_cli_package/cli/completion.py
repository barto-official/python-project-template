from __future__ import annotations

from collections.abc import Callable, Iterable, Sequence
from dataclasses import dataclass
from pathlib import Path

CompletionFn = Callable[[str], Iterable[str]]


@dataclass(frozen=True)
class CompletionSource:
    """Named completion source.

    The source receives the incomplete shell token and returns candidates.
    """

    name: str
    complete: CompletionFn


class CompletionRegistry:
    """Small registry for reusable shell completion sources."""

    def __init__(self) -> None:
        self._sources: dict[str, CompletionSource] = {}

    def register(self, source: CompletionSource) -> None:
        self._sources[source.name] = source

    def get(self, name: str) -> CompletionFn:
        try:
            return self._sources[name].complete
        except KeyError as exc:
            raise KeyError(f"completion source not registered: {name}") from exc

    def names(self) -> list[str]:
        return sorted(self._sources)


def complete_from_choices(choices: Sequence[str]) -> CompletionFn:
    """Create a completion function from static choices."""

    normalized_choices = tuple(choices)

    def complete(incomplete: str) -> Iterable[str]:
        return (
            choice
            for choice in normalized_choices
            if choice.startswith(incomplete)
        )

    return complete


def complete_from_mapping_keys(mapping: dict[str, object]) -> CompletionFn:
    """Create a completion function from mapping keys."""

    return complete_from_choices(tuple(mapping.keys()))


def complete_files(
    incomplete: str,
    *,
    suffixes: set[str] | None = None,
    include_directories: bool = True,
) -> Iterable[str]:
    """Complete local filesystem paths.

    This is intentionally conservative and avoids recursive scanning.
    """
    raw = incomplete or "."
    path = Path(raw).expanduser()

    if path.is_dir():
        directory = path
        prefix = ""
    else:
        directory = path.parent if str(path.parent) else Path(".")
        prefix = path.name

    if not directory.exists() or not directory.is_dir():
        return []

    candidates: list[str] = []

    for child in directory.iterdir():
        if not child.name.startswith(prefix):
            continue

        if child.is_dir():
            if include_directories:
                candidates.append(str(child) + "/")
            continue

        if suffixes is not None and child.suffix not in suffixes:
            continue

        candidates.append(str(child))

    return sorted(candidates)


def complete_profiles(incomplete: str) -> Iterable[str]:
    """Default static profile completion.

    You can replace this with config-aware profile loading later.
    """
    return complete_from_choices(("dev", "test", "staging", "prod", "ci"))(
        incomplete
    )


def complete_output_formats(incomplete: str) -> Iterable[str]:
    return complete_from_choices(("text", "json", "plain"))(incomplete)


def complete_color_modes(incomplete: str) -> Iterable[str]:
    return complete_from_choices(("auto", "always", "never"))(incomplete)


def complete_config_keys(incomplete: str) -> Iterable[str]:
    """Default config-key completion.

    Keep this list close to your public config schema.
    """
    keys = (
        "profile",
        "format",
        "color",
        "quiet",
        "verbose",
        "debug",
        "no_progress",
        "history.enabled",
        "history.path",
    )
    return complete_from_choices(keys)(incomplete)


def complete_toml_files(incomplete: str) -> Iterable[str]:
    return complete_files(
        incomplete,
        suffixes={".toml"},
        include_directories=True,
    )


registry = CompletionRegistry()

registry.register(
    CompletionSource(
        name="profiles",
        complete=complete_profiles,
    )
)
registry.register(
    CompletionSource(
        name="output_formats",
        complete=complete_output_formats,
    )
)
registry.register(
    CompletionSource(
        name="color_modes",
        complete=complete_color_modes,
    )
)
registry.register(
    CompletionSource(
        name="config_keys",
        complete=complete_config_keys,
    )
)
registry.register(
    CompletionSource(
        name="toml_files",
        complete=complete_toml_files,
    )
)

"""
How to extend:


def complete_environments(incomplete: str) -> Iterable[str]:
    return complete_from_choices(("local", "dev", "staging", "prod"))(incomplete)


registry.register(
    CompletionSource(
        name="environments",
        complete=complete_environments,
    )
)

Then use it in the command:

environment: Annotated[
    str,
    typer.Option(
        "--environment",
        autocompletion=registry.get("environments"),
    ),
]

For dynamic completions, keep them fast:

def complete_resource_ids(incomplete: str) -> Iterable[str]:
    # Good: read from small local cache
    # Bad: slow network call on every tab press
    ids = load_cached_resource_ids()
    return (resource_id for resource_id in ids if resource_id.startswith(incomplete))
    
"""