Thank you for considering contributing to this project. All types of contributions are encouraged and valued. See the [Table of Contents](#table-of-contents) for different ways to help and details about how this project handles them. Please make sure to read the relevant section before making your contribution. It will make it a lot easier for us maintainers and smooth out the experience for all involved. The community looks forward to your contributions. 🎉

And if you like the project, but just don't have time to contribute, that's fine. There are other easy ways to support the project and show your appreciation, which we would also be very happy about:
- Star the project
- Tweet about it
- Refer this project in your project's readme
- Mention the project at local meetups and tell your friends/colleagues


## Table of Contents

- [Project Scope](#project-scope)
- [Before You Start](#before-you-start)
- [Questions](#i-have-a-question)
- [Contribution](#i-want-to-contribute)
- [Bugs](#reporting-bugs)
- [Enhancements](#suggesting-enhancement)
- [Development Setup](#development-setup)
- [Branching and Workflow](#branching-and-workflow)
- [Commit Message Guidelines](#commit-message-guidelines)
- [Testing and Quality](#testing-and-quality)
- [Documentation & ADR](#documentation--adr)
- [CI/CD and Release](#cicd-and-release)
- [Submitting a Pull Request](#submitting-a-pull-request)
- [Review Process](#review-process)
- [Security Issues](#security-issues)
- [Licensing](#licensing)
- [Getting Help](#getting-help)
- [Code of Conduct](#code-of-conduct)


## Project Scope

This repository focuses on:

- [INSERT 1–3 BULLETS DESCRIBING THE PROJECT’S PURPOSE]
- [INSERT WHAT IS IN SCOPE]
- [INSERT WHAT IS OUT OF SCOPE]

Contributions that align with the scope are more likely to be accepted.


## Before You Start

### Check existing work

Before opening a new issue or pull request:

1. Search existing issues and pull requests.
2. Read the project README and docs.
3. If proposing a large change, open a design discussion first (see below).

### Discuss larger changes first

For significant changes (architecture, major dependencies, breaking changes) open an issue labeled `type:design` (or `RFC`) and include:
  - Problem statement
  - Goals and non-goals
  - Proposed approach and alternatives
  - Compatibility and migration plan
  - Test and rollout plan

Maintainers may request an approved design before implementation.

## I Have a Question

> If you want to ask a question, we assume that you have read the available [Documentation]().

Before you ask a question, it is best to search for existing [Issues](/issues) that might help you. In case you have found a suitable issue and still need clarification, you can write your question in this issue. It is also advisable to search the internet for answers first.

If you then still feel the need to ask a question and need clarification, we recommend the following:

- Open an [Issue](/issues/new).
- Provide as much context as you can about what you're running into.
- Provide project and platform versions (nodejs, npm, etc), depending on what seems relevant.

We will then take care of the issue as soon as possible.

## I Want To Contribute

You can contribute by:

- Reporting bugs and regressions
- Proposing features or architectural improvements
- Improving documentation and examples
- Adding tests and increasing coverage
- Fixing issues labeled `good first issue` or `help wanted`
- Improving performance, observability, accessibility, or developer experience

> ### Legal Notice
> When contributing to this project, you must agree that you have authored 100% of the content, that you have the necessary rights to the content and that the content you contribute may be provided under the project license.


## Bugs

### Before Submitting a Bug Report

A good bug report shouldn't leave others needing to chase you up for more information. Therefore, we ask you to investigate carefully, collect information and describe the issue in detail in your report. Please complete the following steps in advance to help us fix any potential bug as fast as possible.

- Make sure that you are using the latest version.
- Determine if your bug is really a bug and not an error on your side e.g. using incompatible environment components/versions (Make sure that you have read the [documentation](). If you are looking for support, you might want to check [this section](#i-have-a-question)).
- To see if other users have experienced (and potentially already solved) the same issue you are having, check if there is not already a bug report existing for your bug or error in the [bug tracker](issues?q=label%3Abug).
- Also make sure to search the internet (including Stack Overflow) to see if users outside of the GitHub community have discussed the issue.
- Collect information about the bug:
- Stack trace (Traceback)
- OS, Platform and Version (Windows, Linux, macOS, x86, ARM)
- Version of the interpreter, compiler, SDK, runtime environment, package manager, depending on what seems relevant.
- Possibly your input and the output
- Can you reliably reproduce the issue? And can you also reproduce it with older versions?

### How Do I Submit a Good Bug Report?

> You must never report security related issues, vulnerabilities or bugs including sensitive information to the issue tracker, or elsewhere in public. Instead sensitive bugs must be sent by email to {ADMIN_EMAIL}.

We use GitHub issues to track bugs and errors. If you run into an issue with the project:

- Open an [Issue](/issues/new). (Since we can't be sure at this point whether it is a bug or not, we ask you not to talk about a bug yet and not to label the issue.)
- Explain the behavior you would expect and the actual behavior.
- Please provide as much context as possible and describe the *reproduction steps* that someone else can follow to recreate the issue on their own. This usually includes your code. For good bug reports you should isolate the problem and create a reduced test case.
- Provide the information you collected in the previous section.

Once it's filed:

- The project team will label the issue accordingly.
- A team member will try to reproduce the issue with your provided steps. If there are no reproduction steps or no obvious way to reproduce the issue, the team will ask you for those steps and mark the issue as `needs-repro`. Bugs with the `needs-repro` tag will not be addressed until they are reproduced.
- If the team is able to reproduce the issue, it will be marked `needs-fix`, as well as possibly other tags (such as `critical`), and the issue will be left to be [implemented by someone](#your-first-code-contribution).


### Bug Triage (EITHER REMOVE IF NOT NEEDED OR ADD DETAILS)

This sections explains how bug triaging is done for your project. Help beginners by including examples to good bug reports and providing them questions they should look to answer.

You can help report bugs by filing them here:

You can look through the existing bugs here:

You can help us diagnose and fix existing bugs by asking and providing answers for the following:

* Is the bug reproducible as explained?
* Is it reproducible in other environments (for instance, on different browsers or devices)?
* Are the steps to reproduce the bug clear? If not, can you describe how you might reproduce it?
* What tags should the bug have?
* Is this bug something you have run into? Would you appreciate it being looked into faster?
* You can close fixed bugs by testing old tickets to see if they are still happening.

You can update our changelog here: .....

You can remove duplicate bug reports by: .....

## Enhancements

This section guides you through submitting an enhancement suggestion for CONTRIBUTING.md, **including completely new features and minor improvements to existing functionality**. Following these guidelines will help maintainers and the community to understand your suggestion and find related suggestions.

### Before Submitting an Enhancement

- Make sure that you are using the latest version.
- Read the [documentation]() carefully and find out if the functionality is already covered, maybe by an individual configuration.
- Perform a [search](/issues) to see if the enhancement has already been suggested. If it has, add a comment to the existing issue instead of opening a new one.
- Find out whether your idea fits with the scope and aims of the project. It's up to you to make a strong case to convince the project's developers of the merits of this feature. Keep in mind that we want features that will be useful to the majority of our users and not just a small subset. If you're just targeting a minority of users, consider writing an add-on/plugin library.

### How Do I Submit a Good Enhancement Suggestion?

Enhancement suggestions are tracked as [GitHub issues](/issues).

- Use a **clear and descriptive title** for the issue to identify the suggestion.
- Provide a **step-by-step description of the suggested enhancement** in as many details as possible.
- **Describe the current behavior** and **explain which behavior you expected to see instead** and why. At this point you can also tell which alternatives do not work for you.
- You may want to **include screenshots and animated GIFs** which help you demonstrate the steps or point out the part which the suggestion is related to. You can use [this tool](https://www.cockos.com/licecap/) to record GIFs on macOS and Windows, and [this tool](https://github.com/colinkeenan/silentcast) or [this tool](https://github.com/GNOME/byzanz) on Linux.
- **Explain why this enhancement would be useful** to most CONTRIBUTING.md users. You may also want to point out the other projects that solved it better and which could serve as inspiration.


## Development Setup

> Replace the commands below with your project’s actual tooling. If you support multiple options (e.g., `uv`, `poetry`, `pip`), document the preferred one first and list alternatives.

### Prerequisites

- [INSERT LANGUAGE VERSION, e.g., Python 3.12+ / Node 20+]
- [INSERT TOOLING, e.g., `uv` or `poetry`, `make`, `docker`, etc.]
- [OPTIONAL: DB / services required for local dev]

### Clone

```bash
git clone [YOUR_REPO_URL]
cd [REPO_DIR]
```

### Install dependencies

Option A (preferred):

```bash
# Example (Python/uv)
uv sync
```

Option B (alternative):

```bash
# Example (Python/poetry)
poetry install
```

### Configure environment

1. Copy example environment file:

   ```bash
   cp .env.example .env
   ```
2. Update values in `.env` as needed.

If your project uses secrets, do not commit them. Prefer `.env` files ignored by Git, a secret manager, or local environment variables.

### Run the project locally

```bash
# Example
make dev
# or
uv run python -m your_app
```

### Run tests locally

```bash
make test
# or
uv run pytest
```

## Branching and Workflow

### Default workflow

1. Create a branch from the default branch (`main`)
2. Make small, focused commits.
3. Add tests for behavior changes.
4. Ensure formatting and linting pass.
5. Open a pull request and request review.

### Branch naming

Use descriptive branch names, for example:

* `feature/<short-description>`
* `fix/<short-description>`
* `docs/<short-description>`
* `chore/<short-description>`
* `refactor/<short-description>`

If you use an issue tracker, include the ticket key:

* `feature/PROJ-123-short-description`

### Commit Message Guidelines

This project follows [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/). We use **commitizen** to check whether commit message follows conventional commits.

Commits should follow this pattern:

```markdown
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

The commit contains the following structural elements, to communicate intent to the consumers of your library:

* fix: a commit of the type fix patches a bug in your codebase (this correlates with PATCH in Semantic Versioning).
* feat: a commit of the type feat introduces a new feature to the codebase (this correlates with MINOR in Semantic Versioning).
* BREAKING CHANGE: a commit that has a footer BREAKING CHANGE:, or appends a ! after the type/scope, introduces a breaking API change (correlating with MAJOR in Semantic Versioning). A BREAKING CHANGE can be part of commits of any type.
* types other than fix: and feat: are allowed, for example: chore:, ci:, docs:, style:, refactor:, perf:, test:, and others.
* footers other than BREAKING CHANGE: <description> may be provided and follow a convention similar to git trailer format.
* **Version bumps** match `[tool.semantic_release]` in `pyproject.toml` (parser: **`conventional`**; `[tool.semantic_release.commit_parser_options]`): **`feat`** → **minor**; **`fix`** and **`perf`** → **patch**; a **breaking change** (`BREAKING CHANGE:` footer or **`!`** after the type or scope, for example `feat!:` or `chore(api)!:`) → **major**. Any other valid conventional type only bumps the version if it includes a breaking change.
* **Changelog**: commits listed in `[tool.semantic_release.changelog] exclude_commit_patterns` are left out of `CHANGELOG.md`—currently typical prefixes **`docs`**, **`test`**, **`chore`**, **`ci`**, **`build`**, **`style`**, and **`refactor`**, plus messages matching **`Initial commit`**. Use those types when the change should not appear in release notes

### General guidance

* Use imperative mood: “Add”, “Fix”, “Improve”
* Keep the subject line concise (ideally under ~72 characters)
* Explain “why” in the body when needed

## Testing and Quality (UPDATE FOR YOUR NEEDS)

### Testing expectations

* Add or update tests for any behavior change.
* Prefer unit tests for logic and integration tests for critical paths.
* Tests should be deterministic and not depend on external services unless explicitly designated as integration/e2e.

### CI Expectations

Pull requests and pushes to `main` must pass CI. Before you push, run the same checks locally:

* **Pre-commit** — Ruff (lint + format), Markdown checks, spelling, YAML/TOML sanity, ADR/RFC index regeneration, and commit-message validation (after you install the hook). We use **commitizen** to check whether commit message follows conventional commits.
  * First time: `uv sync --group dev --group docs`, then `pre-commit install` and `pre-commit install --hook-type commit-msg` and `pre-commit install --hook-type commit-msg`.
  * Every run: `uv run pre-commit run --all-files`.

* **Tests** — `uv sync --group dev` then `uv run pytest --markdown-docs docs tests` (CI runs this on Python 3.12 and 3.13).

* **Type checking** — `uv sync --group dev` then `uv run mypy src/{MY_PACKAGE}`.

* **Package build** — `rm -rf dist build *.egg-info && uv build` then `uv run --with twine==6.1.0 twine check --strict dist/*`.

* **Docs site** — Match the docs CI job: sync docs deps, regenerate CLI reference and indexes, then build (set `DISABLE_MKDOCS_2_WARNING=true` if CI does).
  * `uv sync --group docs`
  * `DISABLE_MKDOCS_2_WARNING=true uv run python scripts/generate_cli_reference.py my_package --check`
  * `uv run python scripts/generate_index.py`
  * If `docs/architecture/adr/index.md` or `docs/rfc/index.md` changed, commit those updates.
  * `uv run mkdocs build`

* **Links** — Install the [lychee](https://github.com/lycheeverse/lychee) CLI, build `site/` as above, then run both passes CI uses:
  * `lychee --config .lychee.toml --offline docs/ README.md site/`
  * `lychee --config .lychee.toml site/ docs/ README.md`

### Performance considerations

If your change may impact performance:

* Provide a benchmark or before/after numbers
* Note changes in time/memory complexity where relevant

## Documentation & ADR

### Documentation toolchain

Documentation, apart from  `README.md`, is authored with [Material MkDocs](https://squidfunk.github.io/mkdocs-material/) and can be found in `docs/`. Implementation details belong in `mkdocs.yml`. We use **Google Docstring**.

- Implementation is based on [mkdocs.yml](./mkdocs.yml) and  `scripts/gen_ref_pages.py`; do not hand-maintain `reference/api/` trees. The script automatically creates the reference for all files in the package. Settings are maintained in [mkdocs.yml](./mkdocs.yml) and all changes should be made there: see `extra.api_reference` (`packages`, `exclude`, `public_only`).

- Run docs:
  ```bash
  uv sync --group docs
  uv run mkdocs serve
  ```
- Index for ADRs or RFC files is implemented by `python scripts/generate_index.py` (see `adr-index` in CI and the pre-commit hook).

- **Reference for CLI** is implemented using Typer docs utility in the script `uv run python scripts/generate_cli_reference.py my_package` (assumes structure: `my_package.cli.app`).

- Static checks include:
  - `mdformat` (for settings see [pyproject.toml](./pyproject.toml))
  - [`pymarkdown` (PyPI: `pymarkdownlnt`)](https://pypi.org/project/pymarkdownlnt/) with settings in `.pymarkdown.yaml`. Run `uv run pre-commit run --all-files`.
  - `codespell` (`.codespellrc`)
  - MkDocs `--strict` (Building the docs site with “no warnings allowed” so small config/content problems break CI)
  - Lychee (`.lychee.toml`) in CI checks internal links offline (`docs/`, `README.md`, built `site/`) and runs a full network pass on those roots.
  For local development run:
  ```bash
  #install lychee
  brew install lychee

  #offline for internal links
  lychee --config .lychee.toml --offline docs/ README.md site/

  #online for all links
  lychee --config .lychee.toml site/ docs/ README.md
  ```
  - Executable examples in docs (`pytest-markdown-docs`). The dev dependency **`pytest-markdown-docs`** registers extra pytest behaviour when you pass **`--markdown-docs`**. At collection time, the plugin reads that Markdown file, finds **only** fenced blocks whose language is **`python`**, and turns each block into pytest test item(s) that are **executed as normal Python**. **`bash`**, **`powershell`**, and other fences are **ignored** by this mechanism.


### Hosted documentation and versions

Releases rebuild and publish MkDocs outputs with **Mike → `gh-pages`** (same workflow that publishes wheels). Canonical
URLs come from `site_url` in `mkdocs.yml` (`https://barto-official.github.io/python-project-template/` today). Material’s
Mike integration (`extra.version.provider: mike`) exposes `stable`, `latest`, and per-version selectors.

### Documentation-related CI gates (`.github/workflows/ci.yml`)

- `docs-build` regenerates CLI + indices, runs `mkdocs build --strict`, uploads the `mkdocs-site` artifact.
- `link-check-internal` downloads that artifact and runs **offline** Lychee (`.lychee.toml`) over `docs/`, `README.md`, and `site/` in one pass (no network — filesystem checks for internal targets).
- `link-check-external` runs the **full network** crawl over the same three roots (`site/`, `docs/`, `README.md`) on **pull requests and pushes to `main`**; remote link failures fail the job.

### Architecture decisions (ADR / RFC)

- ADRs live in `docs/architecture/adr/` (see `docs/architecture/adr/template.md`).
- Use `NNNN-kebab-topic.md` names; supersede stale decisions with newer ADRs instead of rewriting published history.
- Store supporting diagrams beside `docs/architecture/diagrams/` when referenced.
- Read `docs/architecture/adr/README.md` for the full authoring flow.


## Packaging Policy

**Build backend and commands**

Packaging uses uv's build backend. Use `uv build` locally and in automation. On release, **semantic-release** runs `uv lock` and commits the lockfile so installs reflect declared dependencies.

**Versioning policy**

Commit messages follow conventional commits. **python-semantic-release** reads that history, updates **`project.version`** in `pyproject.toml`, updates **`CHANGELOG.md`**, and tags **`v{version}`**. When it evaluates commits since the last release, it applies the **largest** bump implied by any of them (for example one `feat` and several `fix` commits still produce a **minor** release).

* **Patch** — **`fix:`** (bugs) and **`perf:`** (performance).
* **Minor** — **`feat:`** (new behavior users can rely on).
* **Major** — **`BREAKING CHANGE:`** in the footer or **`!`** after the type or scope (e.g. `feat!:` or `chore(api)!:`). That applies on **any** type, not only `feat`.
* **No bump** — **`docs:`**, **`chore:`**, **`ci:`**, **`build:`**, **`style:`**, **`refactor:`**, **`test:`**, etc. do not change the version unless they also declare a breaking change. Several of those patterns are **omitted from `CHANGELOG.md`** by configuration so release notes highlight fixes and features.

Follow **[Commit Message Guidelines](#commit-message-guidelines)** in this document so local expectations and automation stay aligned.

**Dependency policy**

Only **`[project]`** dependencies are installed for people who use the published package. Other groups include:

* **`dev`** — Linting, tests, git hooks, and release helpers: Ruff, mypy, pytest, pytest-markdown-docs, pre-commit, codespell,python-semantic-release.
* **`docs`** — The MkDocs / Material site, API docs plugins, mike, mdformat, pymarkdownlnt, packaging, and related doc-only packages.

**Publishing policy**

PyPI updates only from the **release** workflow when the version actually changes, via **Trusted Publishing (OIDC)**. Docs deploy with Mike to `gh-pages` in the same pass, with aliases that treat stable vs prerelease.

## CI/CD and release

Automation lives under `.github/workflows/`; keep README/CONTRIBUTING notes aligned whenever jobs change.

### CI workflow (`ci.yml`)

- Installs reproducible tooling with `uv` (`astral-sh/setup-uv`).
- `tests`: `uv sync --frozen --group dev` then `pytest`including tests on python snippets in documentation across Python `3.12`: `uv run pytest --markdown-docs docs tests on Python 3.12 and 3.13`
  & `3.13`.
- `type-check`: `mypy` on `src/my_package`.
- Packaging + smoke jobs (`package-build`, `artifact-smoke-test`, `sdist-smoke-test`, `editable-install-smoke-test`) run
  `uv build`, `twine check --strict`, wheel/sdist installs, and editable installs using the canonical import name
  `my_package` with distribution metadata `my-package`.
- Documentation + Markdown quality jobs were described earlier (`docs-build`, `link-check-*`).
- `pre-commit`: mirrors local hooks (`uv sync --frozen --group dev --group docs` + `pre-commit run --all-files`).

### Release workflow (`release.yaml`)

- Runs on pushes to `main` (manual `workflow_dispatch` included) with Trusted Publisher credentials for PyPI.
- `semantic-release` (configured via `[tool.semantic_release]` in `pyproject.toml`) bumps `project.version`, rebuilds artefacts,
  and publishes distributions when the semantic version changes.
- The same guarded step syncs docs dependencies, regenerates tracked Markdown outputs (`generate_cli_reference.py`,
  `generate_index.py`), runs `mkdocs build --strict`, and executes `uv run mike deploy --push` with aliases `latest` plus
  `stable` only for non-prerelease builds (determined via `packaging.version.Version.is_prerelease`).
- Finish GitHub Pages setup once per repo: Pages source = **`gh-pages` branch / `/ (root)`** so Mike’s pushes become public.


## Submitting a Pull Request

### PR checklist (expected)

* [ ] PR is scoped and focused (avoid bundling unrelated changes)
* [ ] Linked issue or rationale is provided (e.g., “Fixes #123”)
* [ ] Tests added/updated and passing
* [ ] Lint/format/type checks passing
* [ ] Documentation updated (if needed)
* [ ] Backward compatibility considered; breaking changes clearly labeled
* [ ] Changelog entry added (if your project requires it)

### PR description guidance

Include:

1. Summary of the change
2. Motivation and context
3. How to test (commands and expected behavior)
4. Risk/impact assessment and rollout plan (if applicable)
5. Screenshots/logs (if UI/observability changes)>

## Review Process

Maintainers will review contributions for:

* Correctness and test coverage
* Alignment with project scope and design principles
* Maintainability (clarity, modularity, documentation)
* Backward compatibility and migration strategy
* Security and performance impact

You may be asked to revise your PR. Please keep discussions constructive and focused on the code and requirements.

### Response times

This is an open-source project; reviews may take time. If a PR is time-sensitive, note it explicitly in the PR description.>


## Security Issues

Do not report security vulnerabilities via public issues.

Instead:

* Email: [INSERT SECURITY CONTACT]
* Or follow: `SECURITY.md` (if present)

Include:

* Affected versions
* Reproduction steps
* Impact assessment
* Suggested mitigations (if any)>


## Licensing

By contributing, you agree that your contributions will be licensed under the project’s license.

* See: `LICENSE`

If your organization requires a CLA/DCO, add details here:

* CLA: [INSERT LINK/PROCESS]
* DCO sign-off: [INSERT PROCESS, e.g., `git commit -s`]>

## Getting Help
* Documentation: [INSERT LINK OR PATH, e.g., `docs/`]
* Issue tracker: [INSERT LINK]
* Discussions/Chat: [INSERT LINK, e.g., GitHub Discussions/Slack/Discord]
* Maintainers: [INSERT CONTACT OR TEAM]>

## Code of Conduct

This project follows a Code of Conduct. By participating, you are expected to uphold it.

- Read: `CODE_OF_CONDUCT.md` (or equivalent policy document)
- Report violations to: [INSERT CONTACT OR EMAIL]

Thank you for contributing.
