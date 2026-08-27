---
name: engineering-audit
description: Audit code, a proposed design, a refactor, or a pull request against the repository's code-quality, software-design, and/or architecture standards. Use when the user explicitly requests an audit or review and specifies the dimension or dimensions to assess.
disable-model-invocation: true
---

# Engineering Quality Audit

## Purpose

Audit engineering quality against the repository's own standards. The rules define **what good looks like**; this skill defines **how to inspect, judge, and report it**.

Before auditing, read `AGENTS.md`. Treat repository rules as authoritative. Do not replace them with generic best practices.

This skill is read-only unless the user explicitly requests remediation. Do not edit source code, tests, configuration, or dependencies during an audit. Running existing validation commands is permitted when useful and safe. State any material checks that were not run.


## Audit principles

- Require concrete evidence before reporting a violation.
- Treat smells as investigation triggers, not automatic failures.
- Judge total system complexity, not local neatness or pattern usage.
- Prefer observed change risk over hypothetical purity.
- Do not require a pattern unless its absence creates a concrete problem.
- Prefer the smallest change that reduces cognitive load, change amplification, coupling, or hidden knowledge.
- Distinguish confirmed violations from concerns when evidence is incomplete.
- Do not use a numeric quality score unless explicitly requested.

## Workflow

1. **Establish scope**
   - Identify the requested diff, PR, files, module, package, service, or repository.
   - For a change audit, understand the intended behavior first.
   - Read enough adjacent code to verify callers, contracts, invariants, dependencies, and ownership.
   - Select audit dimensions based on user intent: architecture audit, software design audit, code quality audit.

2. **Load standards for the selected dimension**
   - Read `AGENTS.md`.
   - Read only the repository rules and diagnostic references for the requested audit dimensions.
   - If a requested rule or reference is unavailable, mark that dimension `NOT ASSESSED`.
   - Do not load or judge unrequested dimensions.


3. **Collect evidence**
   - Inspect implementation, interfaces, tests, dependencies, and boundary crossings.
   - Run existing tests, linters, type checks, or architecture checks when useful and available.
   - Inspect import/dependency graphs for cycles, layering, or boundary claims when relevant.
   - Use history only when needed to verify change-locality claims such as divergent change or shotgun surgery.

4. **Select and apply audit dimensions**

   Determine which audit dimensions the user requested:

   - `software-design`
   - `architecture`
   - `code-quality`

   If no dimension is specified, ask the user which dimension or dimensions to audit. Do not silently run a broad three-dimension audit.

   For each requested dimension:

   - Read the corresponding repository rule.
   - Read its corresponding diagnostic checklist in `references/`.
   - Use the checklist only to discover and test possible findings.
   - Apply the shared finding and severity standards in this skill.

   Current mapping:

   | Dimension | Repository rule | Diagnostic reference |
   | --- | --- | --- |
   | Software design | `.cursor/rules/software_design.mdc` | `references/software-design-audit.md` |
   | Architecture | `.cursor/rules/architecture.mdc` | `references/architecture-audit.md` |
   | Code quality | `.cursor/rules/code_quality.mdc` | `references/code-quality-audit.md` |

   If a requested rule or reference does not exist, mark that dimension `NOT ASSESSED`; do not substitute generic advice.

5. **Challenge every candidate finding**
   - What exact evidence proves the problem?
   - What complexity, maintenance, correctness, or change risk does it create?
   - Is it a rule violation or only a stylistic preference?
   - Would the proposed fix reduce total complexity, or merely move/add it?

6. **Report material findings only**
   - Merge findings that share one root cause.
   - Prioritize impact over number of principles implicated.
   - Do not manufacture low-value findings to fill the report.

## Finding standard

A finding is valid only when it includes:

- **Evidence:** exact file/line/symbol, dependency, test result, or observed behavior.
- **Principle:** applicable repository rule or diagnostic category.
- **Impact:** concrete complexity, coupling, change, misuse, correctness, or operational risk.
- **Recommendation:** smallest credible fix or direction.
- **Confidence:** `high`, `medium`, or `low` when context is incomplete.

### Severity

- **High:** broad change amplification, broken contracts, invalid state, architecture erosion, or substantial maintenance/correctness risk.
- **Medium:** concrete debt that materially increases cognitive load, coupling, misuse risk, or future change cost.
- **Low:** localized issue with limited impact; report only when useful.

Do not inflate severity because several principles describe the same root cause.

## Output

Use this structure unless the user requests another format:

```markdown
# Engineering Quality Audit

**Scope:** ...
**Verdict:** PASS | PASS WITH CONCERNS | NEEDS CHANGES

## Findings

### [HIGH|MEDIUM|LOW] Short finding title
- Evidence: `path:line` — concrete observation
- Area: code-quality | software-design | architecture-quality
- Principle: rule/section
- Impact: why this matters here
- Recommendation: smallest useful change
- Confidence: high | medium | low

## Not assessed / missing evidence
- Only material limitations.
```

If there are no material findings, say so directly.

## Final validation

Before finalizing, verify:

- Every issue has concrete evidence and a real impact.
- Smells were treated as signals, not automatic failures.
- Recommendations reduce total complexity instead of adding ceremonial abstraction.
- Duplicate findings were merged by root cause.
- Missing context is reflected in confidence or `NOT ASSESSED`, not guessed.
