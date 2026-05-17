"""Allowlisted doctest-style examples from stable public helpers."""

from __future__ import annotations

import doctest
from collections.abc import Callable
from typing import Any

from my_package.hello import add, chunked, slugify

_ALLOWLIST: tuple[Callable[..., Any], ...] = (
    add,
    slugify,
    chunked,
)


def test_allowlisted_examples_from_docstrings() -> None:
    finder = doctest.DocTestFinder(verbose=False)
    runner = doctest.DocTestRunner(verbose=False)
    for func in _ALLOWLIST:
        globs = {func.__name__: func}
        for dt in finder.find(func, globs=globs, name=func.__name__):
            result = runner.run(dt, clear_globs=True)
            assert result.failed == 0
