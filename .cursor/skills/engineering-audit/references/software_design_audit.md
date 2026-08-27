---# Software-design diagnostic checklist

Use these questions to test the `software-design` rule. Do not answer every question in the final report; use them to discover evidence.

MUST: Do not report a finding merely because a pattern, smell, heuristic,
or preferred principle is present. Every finding must identify:
- concrete evidence,
- affected design property,
- actual or credible cost/risk,
- applicable rule,
- smallest reasonable remediation.

## Finding threshold

**MUST NOT** report a finding merely because a pattern, smell, heuristic, or preferred principle is present.

Every finding must identify:

-   **Evidence** — concrete code, dependency, behavior, contract, state flow, or test evidence.
-   **Affected property** — what aspect of the design is harmed.
-   **Impact** — actual or credible cognitive, maintenance, coupling, change, correctness, misuse, or operational cost.
-   **Principle** — applicable `software-design` rule.
-   **Recommendation** — smallest reasonable remediation.

Smells and checklist questions are investigation triggers only.

If no meaningful cost can be demonstrated, do not report a finding.

## Severity

Assign severity from demonstrated impact, not from the number of principles implicated.

### HIGH

Use when the problem creates substantial or systemically important risk, such as:

-   broken or unstable public contracts;
-   invalid state or unenforced critical invariants;
-   broad change amplification across multiple modules or callers;
-   unclear ownership causing conflicting authorities;
-   severe hidden coupling or dependency inversion that prevents local reasoning;
-   abstraction or boundary failure that repeatedly causes misuse or defects;
-   substantial correctness, data integrity, compatibility, or operational risk.

A high-severity finding should normally require remediation before the change is considered complete.

### MEDIUM

Use when there is a concrete design problem that materially increases:

-   cognitive load;
-   coupling;
-   misuse risk;
-   non-local reasoning;
-   maintenance cost;
-   future change cost;
-   duplicated/scattered policy;
-   fragility of an important boundary or contract.

The issue is real and worth fixing, but the design remains locally understandable and operationally viable.

### LOW

Use for localized design debt with limited impact.

Examples include:

-   unnecessary indirection confined to a small area;
-   a locally weak abstraction;
-   minor leakage of implementation knowledge;
-   avoidable but contained complexity;
-   a design choice likely to make one narrow class of future change harder.

Report LOW findings only when they are materially useful. Do not manufacture them to make an audit appear comprehensive.

### Severity rules

-   Do not increase severity because multiple rules describe the same root cause.
-   Do not use severity to represent confidence.
-   An uncertain high-impact risk should have high/medium severity with lower confidence, not artificially reduced severity.
-   Prefer one finding describing the root cause over several findings describing its symptoms.

## 1. Complexity and changeability

- Is the design actually simpler, or has it only added structure?
- Has the number of concepts a caller must understand decreased?
- Can the core behavior be explained in a small, coherent mental model?
- Does a small requirement change stay local, or require edits across many branches/files?
- Are important dependencies or state hidden from signatures and interfaces?
- Can behavior be predicted without inspecting many unrelated modules?
- Is accidental complexity isolated behind a boundary, or spread through the system?
- Is readability favored over cleverness and premature optimization?

Flag when there is evidence of high cognitive load, change amplification, or unknown-unknown risk.

## 2. Abstraction

- Does the abstraction hide meaningful complexity behind a simpler concept?
- Is its interface materially simpler than its implementation?
- Does it provide a stable mental model while internals can change?
- Does it have a clear purpose and boundary?
- Does it expose only guarantees callers can safely rely on?

### Recognizing a wrong abstraction

Investigate when:

- The abstraction requires frequent exceptions or "except when" rules.
- The interface accumulates flags and optional parameters.
- Callers import internals, bypass layers, or otherwise reach around it.
- Bugs are repeatedly caused by misuse of the abstraction.
- Performance problems cluster around a supposedly convenient API.
- The abstraction keeps its name but repeatedly changes semantics.
- One implementation sits behind multiple layers without meaningful protection or variation.

Do not assume one implementation is automatically wrong; a boundary may still isolate I/O, nondeterminism, vendor APIs, or an important architectural seam.

## 3. Information hiding and leakage

- Are representation, invariants, algorithms, infrastructure details, and recovery mechanics hidden from callers where practical?
- Is the same piece of domain or technical knowledge encoded in multiple places?
- Do callers need to know undocumented ordering, performance, lifecycle, or special-case rules?
- Are external/vendor/framework representations translated at the boundary, or leaked through core code?
- Are callers using public interfaces rather than private internals?
- Are low-level errors translated into a small, meaningful error model?

Flag **information leakage** when one decision must be understood or edited in multiple modules.

## 4. General vs. specific

- Is general mechanism separated from caller-specific policy?
- Does a general-purpose module contain product-specific rules or special cases?
- Is a method present for one narrow caller rather than a reusable capability?
- Could special cases be moved to the layer that owns the policy?

## 5. Decomposition
- What is the primary decomposition axis: workflow, data ownership, or domain capability?
- Does that axis match the system's actual change patterns?
- Which concepts, rules, data, and workflows change together?
- Does each important change stay mostly within one module/domain?
- Are units separated that must constantly be understood or changed together?
- Are unrelated concepts forced into the same unit?

Good decomposition should localize knowledge, invariants, and change.

## 6. Responsibility / SRP

For each important unit ask:

- Can its purpose be described in one short, specific sentence?
- Who is its primary consumer or stakeholder?
- What invariants does it own?
- Why would this unit need to change?
- Are those reasons part of one coherent policy boundary?
- Does it expose one conceptual capability?
- Is there one clear authority over the concept it represents?
- Does it mix orchestration, domain policy, persistence, formatting, or infrastructure without a reason?

Flag when unrelated change reasons or invariant sets coexist in the same unit.

## 7. Cohesion
- Do all elements contribute to the same purpose?
- Do they operate on the same concepts, state, or invariants?
- Would any element naturally belong somewhere else?
- Do callers use the unit as a capability, or cherry-pick unrelated pieces?
- Do unrelated features repeatedly modify the same file/class/module?
- Does the unit feel like a grab bag of helpers or utilities?
- Does a proposed split create meaningful information hiding/change isolation, or merely move lines into more files?

Do not optimize for maximum fragmentation. High cohesion is semantic unity, not minimum file size.

## 8. Coupling and connascence

- Are dependencies explicit in parameters, constructors, imports, or contracts?
- Does a unit depend on another unit's internals or representation?
- Is coupling caused by shared mutable state, call order, flags, magic values, naming conventions, or hidden ambient context?
- Can the unit be tested in useful isolation?
- Does it receive large objects but use only a small portion?
- Does one change require coordinated edits in many consumers?

For risky coupling, judge:

- **Strength:** how fragile is the dependency?
- **Locality:** how far across the system does it reach?
- **Degree:** how many components participate?


## 9. Modules and boundaries

Ask:

- Can the module's job be described clearly and specifically?
- Is it deep: small public interface, substantial hidden functionality?
- Which module is authoritative for each important concept/state?
- Where are invariants enforced?
- What operations are allowed across the boundary?
- What types/DTOs cross it?
- What errors cross it?
- Which details may change without affecting callers?
- Which dependency direction is allowed?
- Are private/internal modules actually protected from external use?
- Do tests protect important public contracts?

Flag shallow wrappers unless they create a deliberate facade, adapter, transaction boundary, authorization boundary, or other meaningful protection.

## 10. Interface and contract quality

For every important public interface ask:

- What operations exist, and what do they mean precisely?
- Is the interface narrow enough to understand quickly?
- Does it cover current use cases without exposing unnecessary choices?
- What assumptions and preconditions exist?
- What does success guarantee?
- What side effects occur?
- What errors are possible, and which are retryable/fatal?
- Are ordering, idempotency, consistency, and lifecycle guarantees explicit when relevant?
- Could the implementation change without forcing caller changes?
- Are callers forced to depend on methods they do not use?
- Did implementations need to violate or work around the contract?

Flag long parameter lists, behavior-changing booleans, broad service/repository interfaces, raw untyped payloads, and contracts that leak vendor/framework semantics when they create real misuse or change risk.

## 11. Defensive design and determinism

- Is untrusted input validated and normalized at the boundary?
- Are invariants enforced by the authority that owns the domain state?
- Is trusted internal code repeatedly validating guarantees already established elsewhere?
- Are time, randomness, environment/config, filesystem/database state, ordering, or concurrency hidden inputs to behavior?
- Can tests control those inputs deterministically?
- Are external failures translated and handled at the integration boundary?
- Are configuration errors detected early, ideally at startup?
- Is shared mutable state creating action-at-a-distance behavior?


## 12. YAGNI and future-proofing

Before accepting extension points, configuration, patterns, or extra layers ask:

- Are there at least two concrete current use cases or observed variation?
- Is adding the capability later unusually expensive or risky?
- Can a simpler design be changed safely when the need appears?
- Does the proposed flexibility introduce new failure modes or operational cost?
- What happens if this future requirement never arrives?

Flag speculative generality when the design pays complexity today for hypothetical variation with no strong evidence.

## 13. SOLID checks

### Open/Closed Principle

- Is there repeated, demonstrated variation around a stable concept?
- Does adding a real variant require editing many existing conditionals or modules?
- Would a deliberate extension seam localize that variation?
- Is the extension mechanism simpler than continuing direct modification?

Do not flag OCP merely because code can be modified. Premature extension mechanisms violate YAGNI.

### Liskov Substitution Principle

For subtype `S` of `T`, ask:

- Can `S` be used wherever `T` is expected without type-specific branching?
- Does `S` accept at least the same valid input domain?
- Does it preserve output guarantees and invariants?
- Does it preserve compatible exception and side-effect semantics?
- Does it disable inherited behavior or raise `NotImplementedError` for valid base operations?

### Interface Segregation Principle

Ask:

- Do clients depend only on operations they actually need?
- Does an interface mirror a large implementation/SDK rather than a client role?
- Are implementations forced to stub or reject unsupported methods?
- Would splitting by client capability improve clarity without creating micro-interface fragmentation?

### Dependency Inversion Principle

- Does high-level policy import databases, frameworks, vendor SDKs, or other volatile details directly?
- Is the needed abstraction owned by the high-level side that knows the requirement?
- Do volatile implementations depend on the stable contract rather than the reverse?
- Are concrete implementations wired at a composition edge?
- Is dependency injection explicit and simpler than a container/framework would be?

## 14. Data and control flow

- Are meaningful domain concepts represented explicitly rather than as undifferentiated primitives/dictionaries?
- Is data ownership clear, including who may mutate it and which invariants govern it?
- Are state transitions explicit and valid states constrained where practical?
- Is imperative orchestration still easy to follow, or has control flow become deeply branched and scattered?
- For push/concurrent/event-driven flows, are backpressure, ordering, retries, and ownership explicit where relevant?

Flag primitive obsession or generic context dictionaries when they erase domain meaning, duplicate validation, or allow invalid states.

## 15. Dependency direction and layering

Inspect the module/package dependency graph where useful.

- Is the graph acyclic, or are there circular dependencies?
- Can the direction between two modules be stated clearly?
- Do dependencies point toward stable domain/policy contracts rather than volatile details?
- Is framework/infrastructure knowledge leaking into domain/core code?
- Are logical boundaries being enforced by imports and public APIs?
- Does a stable/highly depended-on component itself depend on volatile components?
- Are layer violations deliberate simplifications, or accidental shortcuts that create future change amplification?

A cycle is strong evidence that responsibility, ownership, or dependency direction deserves inspection; it is not by itself a prescription for adding an interface.

## 16. Splitting, indirection, and method design

- Can the new unit be understood independently?
- Can the parent/caller be understood without reading the new unit's implementation?
- Does the split simplify an interface or isolate a coherent subtask?
- Will callers usually need both new pieces together?
- Does the split reduce total complexity despite adding another interface?
- Are developers forced to jump back and forth between conjoined helpers?

