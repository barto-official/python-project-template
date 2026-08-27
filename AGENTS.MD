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

## Referenced Engineering Guidance

Before making changes that involve the relevant concerns, read and follow:

- if you work on new feature: `{SOFTWARE_DESIGN_GUIDE_PATH}`
- if you work on package, architecture design, refactoring, or high level architecture: `{ARCHITECTURE_DESIGN_GUIDE_PATH}`
- if you do code implementation: `{CODE_STYLE_GUIDE_PATH}`

These documents take precedence for their respective domains. Do not restate or independently reinterpret their rules here.

## Working Principles

### Prefer strategic programming

Except for fixes, hotfixes, and clearly small changes, **do not jump directly into implementation**.

For substantial work, first:

1. Define the problem and desired outcome.
2. Identify relevant constraints and existing behavior.
3. Consider viable implementation approaches.
4. Analyze trade-offs, risks, maintenance cost, and compatibility.
5. Recommend an approach and explain why.
6. Produce a concrete implementation plan.
7. Implement only after the direction is established.

Planning should be proportional to the task. Avoid ceremony for trivial changes, but do not treat significant design decisions as implementation details.

When requirements are ambiguous or significantly affect architecture, public behavior, compatibility, or maintenance cost, discuss the ambiguity before committing to a design.

## Implementation Guidelines

### Keep designs proportional

Avoid unnecessary abstraction and fragmentation, including:

- classes that do not meaningfully model state, behavior, or a domain concept;
- functions created only to reduce line count or satisfy an arbitrary notion of decomposition;
- wrappers that add indirection without adding semantics;
- interfaces, factories, registries, or extension points without a demonstrated need;
- premature generalization for hypothetical future requirements
- error exceptions that are unnecessary and can be moved to the edge

Defensive programming is appropriate when it protects real boundaries, invariants, failure modes, or external inputs. Do not add defensive layers for impossible or purely speculative conditions.

Prefer cohesive code with clear ownership over excessive decomposition ("classitis", "functionitis", or abstraction for its own sake).

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

Branh names: follow conventional commit types.

Never push to a remote repository. Do not alter remote state, publish branches, create releases, or perform equivalent remote Git operations unless the user explicitly changes this rule.

Before committing:

```bash
uv run prek run --all-files
```

Keep commits coherent and scoped to the work being performed. Do not include unrelated changes.

For commits, use conventional commits. Create logical commits based on  branch changes. Avoid one big commit. Don't push. Use simple, straightforward language so users and other developers will understand it. Don't use jargon or obfuscated language. Description of the commit should be a maximum of 2 bullet points. Description should not use mention to internal agent chat. Rather it should contain what outside users/customers should not about his change: high level overview.

Branch changes will be delivered as Pull Request. Pull Requests SHOULD stay below 500 lines. This rule is not hardcoded but notify if this treshold will be crossed and propose how to split changes.


## Secrets and Sensitive Data

Never publish, commit, expose, or reproduce secrets or sensitive credentials.