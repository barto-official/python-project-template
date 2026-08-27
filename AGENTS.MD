# AGENTS.md

## Project Context

- Project type: Python package (API + CLI)
- Python: 3.12+
- Package and environment management: `uv`. Never edit `uv.lock` by
hand.
- Tests: `pytest`
- Linting and formatting: `ruff`
- Type checking: `ty`
- Pre-commit checks: `prek`
- CI: GitHub Actions

Use the repository's existing configuration as the source of truth. Do not introduce parallel tooling, duplicate configuration, or alternative workflows without a clear reason.

## Domain Knowledge & Reference

{ADD IF NEEDED}

## Working Principles

Add Google-style docstrings for public modules, classes, functions, and externally meaningful behavior where they improve use. All code should stick to quality rules defined in `pyproject.toml`

### Prefer strategic programming

Except for fixes, hotfixes, and clearly small changes, **do not jump directly into implementation**.

Planning should be proportional to the task. Avoid ceremony for trivial changes, but do not treat significant design decisions as implementation details.

When requirements are ambiguous or significantly affect architecture, public behavior, compatibility, or maintenance cost, discuss the ambiguity before committing to a design.

## Implementation Guidelines

### Keep designs proportional

The main design goal is the code to be understandable not clever and reduce complexity.

Defensive programming is appropriate when it protects real boundaries, invariants, failure modes, or external inputs. Do not add defensive layers for impossible or purely speculative conditions.

Prefer cohesive code with clear ownership over excessive decomposition.

For non-trivial implementation and design work, prefer the
smallest design that adequately addresses the demonstrated problem.

Apply the software-design skill when the change materially affects
responsibilities, interfaces, dependencies, state ownership, or
module/package structure.

### Preserve compatibility

Do not introduce a breaking change without explicit approval.

If a breaking change appears to be the best solution:

1. identify the compatibility impact;
2. explain why the break is justified;
3. describe non-breaking alternatives where reasonable;
4. ask for approval before implementing the breaking change.

## Validation

Validate changes at the narrowest useful level during development, then run the repository checks before considering the work complete.

Typical commands:

```bash
uv run pytest
uv run ty check
uv run prek run --all-files
```

Use focused tests while iterating when appropriate, for example:

```bash
uv run pytest path/to/test_file.py
```

If a check cannot be run, state that explicitly and explain why.

### Tests

Behavior changes should normally include or update tests.

Tests should verify externally meaningful behavior and important invariants rather than mirror implementation details unnecessarily.

For bug fixes, add a regression test when practical.

Do not weaken, delete, or bypass a failing test simply to make the suite pass unless the test is demonstrably obsolete or incorrect.


## Git Workflow

Branch names: follow conventional commit types so branches follow the same: feat, fix, style, refactor etc.

Never push to a remote repository. Do not alter remote state, publish branches, create releases, or perform equivalent remote Git operations unless the user explicitly changes this rule.

Before committing:

```bash
uv run prek run --all-files
```

Keep commits coherent and scoped to the work being performed. Do not include unrelated changes.

For commits, use conventional commits.
* Create logical commits based on  branch changes and avoid one big commit. Don't push.
* Use simple, straightforward language so users and other developers will understand it.
* Don't use jargon or obfuscated language.
* Description of the commit should be a maximum of 2 bullet points.
* In description, do not mention internal agent conversations; describe the customer-relevant change.

Branch changes will be delivered as Pull Request. Pull Requests SHOULD stay below 500 lines. This rule is not hardcoded but notify if this treshold will be crossed and propose how to split changes.


## Secrets and Sensitive Data

Never publish, commit, expose, or reproduce secrets or sensitive credentials.