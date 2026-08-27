---
name: software-design
description: Design a new feature, substantial refactor, public-interface change, module/package change, or dependency-boundary change. Produce an evidence-based proposed design before implementation. Do not use for small localized fixes.
---


# Purpose

Produce a proposed software design before implementation. Apply the repository's software-design rule at `.cursor/rules/software_design.mdc`. Do not edit production code, install dependencies, or begin implementation unless the user explicitly asks after reviewing the proposed design.

MUST: Apply each step proportionally. Do not invent domain concepts, state, boundaries, failure modes,
contracts, or infrastructure concerns merely to complete the template. If a section is not materially relevant, mark it "Not applicable" with at most a brief reason and move on.

MUST: When there is a consequential design choice with multiple credible
approaches, identify 2–3 viable alternatives and compare them. Do not manufacture alternatives for straightforward decisions.

**Maintain an Assumptions / Open Questions section.**

Do not silently resolve ambiguity when different answers would
materially change:
- public behavior,
- ownership,
- state model,
- compatibility,
- dependencies,
- error semantics,
- or implementation cost.

For reversible/local decisions, state the assumption and continue.
For consequential decisions, surface the question before treating
the design as final.

**Use Research Proportionally**

Use research already supplied by the user where available.

Invoke the `research-solutions` workflow only when external evidence would materially affect a consequential design decision, such as selecting a library, protocol, persistence mechanism, integration strategy, or security approach.

**Compare Consequential Options**

When a consequential design choice has multiple credible approaches:

1. Identify two or three viable alternatives.
2. Compare their fit, costs, risks, compatibility impact, and maintenance implications.
3. Recommend one approach and explain the decision.
4. Preserve unresolved decisions in the Assumptions / Open Questions section.

Do not manufacture alternatives for straightforward decisions.


# 0. Research on repository state — Before modeling a solution:
    - inspect the relevant modules and public contracts;
    - identify current responsibility and ownership boundaries;
    - identify existing domain concepts and abstractions;
    - trace the main relevant call/data flow;
    - identify constraints imposed by compatibility and existing behavior;
    - identify reusable existing mechanisms;
    - distinguish existing accidental complexity from intentional design.


# 1. **Define the Scope** — Write down:

    * capability being built,
    * actors/callers,
    * main use cases,
    * what is in scope,
    * what is explicitly out of scope,
    * required observable outcomes.

Ask a follow-up question  when in doubt.

# 2. **Identify Constraints**

Record only engineering constraints that can affect design as bullet points.

MUST: Include the following (next) sections only when they materially affect the requested change. Mark irrelevant sections as “Not applicable” with a brief reason.

- domain concepts, state, lifecycle, and invariants;
- ownership of important state, rules, and policy;
- module or package boundaries;
- public contracts and error semantics;
- dependency direction and composition;
- runtime, concurrency, integration, and failure semantics.

# 3. **Model the Important State and Rules**

Output: Bullet points/free text with identified:

* domain concepts,
* identity,
* authoritative data,
* state,
* lifecycle,
* invariants,
* valid state transitions,
* relationships.

---

# 4. Assign Ownership — For every important piece of knowledge decide which unit is authoritative. Provide a list with:

    - Responsibility — coherent capability/policy
    - Owns — state, rules, or knowledge for which it is authoritative
    - Enforces — invariants it is responsible for
    - Provides — public capability/contract
    - Hides — representation or implementation choices



---

# 5. **Define Boundaries** — Provide a list with:
    * **Ownership**
    * **Interface**
    * **Information hidden**
    * **Dependency direction**

Choose boundaries primarily around:

* domain capability,
* data ownership,
* volatility,
* trust/security,
* performance/reliability isolation.

Prefer logical boundaries before physical deployment boundaries.

---

# 6. Design the Interface and Contract

For important or newly introduced public operations, define the
semantics callers need to rely on:

* purpose,
* input,
* result,
* preconditions,
* postconditions,
* errors,
* side effects,
* idempotency if relevant.

Then, provide a function/class/similar object signature as a real code or pseudocode.

Prefer:

* narrow interfaces,
* domain language,
* explicit semantics,
* safe defaults,
* few configuration parameters,

Keep implementation details private.


---

# 7. Decide Dependency Direction — Draw the dependency graph.

Aim for:

* no accidental cycles,
* stable policy independent of volatile mechanisms,
* high-level code depending on contracts,
* implementation plugged into those contracts,
* construction/wiring kept at the composition root.

Use dependency inversion where it protects a meaningful boundary.

---

# 8. Decide Runtime and State Semantics

For state-changing, concurrent, or externally integrated flows,
decide the applicable runtime semantics: (else: skip this step)

* who orchestrates it,
* synchronous vs asynchronous execution,
* transaction boundary,
* consistency model,
* retry behavior,
* idempotency,
* concurrency behavior,
* ordering requirements,
* partial-failure behavior,
* external side effects.

Keep nondeterministic inputs explicit where useful:

* time,
* randomness,
* configuration,
* external state,
* ordering,
* concurrency.

# 9. Produce the Proposed Design

Output:

1. Design summary and recommended approach.
2. Explicit design decisions/trade-offs.
3. Scope, success criteria, assumptions, and open questions.
4. Alternatives considered and the reason for the recommendation.
5. Changes to modules, responsibilities, boundaries, and dependencies.
6. Important contracts, invariants, and state ownership.
7. Dependency structure.
8. Main execution/data flows.
9. Runtime and failure semantics, if applicable.
10. Compatibility or migration considerations, if applicable.
11. Test strategy and required validation commands.
12. Open questions/assumptions.
13. Ordered implementation sequence.



