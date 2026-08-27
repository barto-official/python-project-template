---
name: research-solutions
description: Research credible implementation strategies for a feature or technical decision. Use only when the user explicitly requests solution research before design or implementation.
disable-model-invocation: true
---

Your goal is take context and requirements provided by the user and make an extensive resaerch online on possible implementations of the given feature/request. What credible implementation strategies exist for these requirements, what evidence exists for each, and what constraints/trade-offs would matter to the later design process?

MUST NOT: edit code, install dependencies, or make external state changes. This is a research skill. ONLY READ and then write a document.

1. Make sure requirements are clear. If you have any doubt about the request, ask follow-up questions to the user before starting a research.

2. Understand the local context

Inspect relevant repository code and configuration to identify:

- existing implementations of similar behavior;
- existing dependencies and frameworks;
- extension points or abstractions already in use;
- compatibility constraints;
- language/runtime versions;
- current architectural/design conventions;
- mechanisms that should be reused rather than duplicated.

3. Do the research online on possible what implementatioj strategies exists Priorities should be put to:
    1. Official/current documentation and specifications
    2. Source code of the relevant project/tool
    3. Mature open-source implementations
    4. Maintainer discussions/issues/ADRs
    5. High-quality technical discussions
    6. Practitioner reports (HN, Reddit, Stack Overflow)
    7. Blog posts

Find one or more comparable, mature systems using this strategy
when such evidence exists. Explain what aspect is comparable and avoid assuming their context
matches ours.

Identify 2–4 credible implementation strategies. Do not manufacture alternatives to reach a target count

Goal: create a table with alternative implementations. For each possible strategy, gather:
    * Name
    * descritpion
    * trade-offs




4. For each strategy resarch on relevant techniques/patterns. Gather: name, description, code sample, trade-off.

5. For each techniques/patterns resarch on relevant candidate libraries/tools. Gather: name, description, code sample, trade-off.


Final output — table with:

| Field             | Purpose                              |
| ----------------- | ------------------------------------ |
| Approach          | Short name                           |
| Mechanism         | How it actually works                |
| Fit               | Which requirements it serves         |
| Dependencies      | New/existing dependencies            |
| Repository impact | What would need to change            |
| Advantages        | Concrete benefits                    |
| Costs             | Complexity/maintenance/runtime cost  |
| Risks             | Failure modes/uncertainties          |
| Constraints       | Cases where it won't work            |
| Evidence          | Sources/examples                     |
| Open questions    | Things the design phase must resolve |
| Design implications | The choices the next design process must make |

Do not make the implementation decision. Identify options that merit the design phase and options that are clearly unsuitable. The purpose of this research is to map the credible solution space and provide evidence for the software-design process. You may identify clearly dominated or unsuitable options, but preserve multiple credible alternatives when meaningful trade-offs remain.

Prefer current primary sources. Verify that documentation and library versions apply to the repository’s runtime/tool versions. Distinguish documented facts from practitioner opinion and from your own inference. Cite evidence for material claims.