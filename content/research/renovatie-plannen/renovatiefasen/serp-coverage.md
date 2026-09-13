# SERP coverage — Renovatiefasen

- Route: `/renovatie-plannen/renovatiefasen/`
- Market: Nederland / nl-NL
- Researched: 2026-09-13
- Workflow mode: page audit before production
- Decision: `LIGHT_UPDATE`
- Confidence: high

## Target query set

Primary ownership:
- `renovatiefasen`
- `fasen verbouwing`
- `fases van een verbouwing`

Supporting query language:
- `verbouwing van voorbereiding tot oplevering`
- `verbouwproces stappen`
- `wanneer offertes aanvragen verbouwing`
- `wanneer aannemer kiezen verbouwing`
- `oplevering verbouwing`

Do **not** broaden ownership to `huis renoveren waar beginnen` or the physical `volgorde verbouwing`; those belong to sibling URLs.

## SERP / competitor observations

### Vereniging Eigen Huis — Checklist verbouwen
URL: https://www.eigenhuis.nl/huis-verbeteren/klussen/verbouwen/checklist-verbouwen

Strong homeowner lifecycle coverage: orientation, budget, preparation, permits, contractors/offers/contracts, control during works, and formal handover. It is the clearest Dutch evidence that the reader's task spans the project lifecycle rather than only physical work order.

### Vereniging Eigen Huis — Verbouwen / Hulp bij verbouwen
URLs:
- https://www.eigenhuis.nl/huis-verbeteren/klussen/verbouwen
- https://www.eigenhuis.nl/huis-verbeteren/verbouwen/hulp-bij-verbouwen

Confirms a broad homeowner lifecycle from preparation through execution to handover, plus separate needs around financing, contract review and delivery inspection.

### Rijksoverheid — Stappenplan bij bouwen en verbouwen
URL: https://www.rijksoverheid.nl/themas/bouwen-en-wonen/bouwregelgeving/stappenplan-bij-bouwen-en-verbouwen

Strong official source for the regulatory feasibility phase: omgevingsplan, welstand, building rules, permit and neighbours. This is not the full renovation lifecycle, but it supports a separate feasibility gate before execution.

### Homedeal — Stappenplan huis verbouwen (14 July 2026)
URL: https://www.homedeal.nl/verbouwing/huis-verbouwen-stappenplan/

Commercial SERP competitor with seven broad steps: plan/goals, budget, quotes/contractors, permits, schedule/preparation, execution, handover. Useful for format/coverage observation, not primary evidence.

### Verbouw Je Eigen Huis — Stappenplan
URL: https://www.verbouwjeeigenhuis.nl/proces/stappenplan

Uses project phases such as initiative/feasibility and subsequent design/preparation stages. Reinforces that a phase model can be organised by decision maturity rather than by trades.

## Intent ownership

This page should answer:

> Welke projectfasen doorloop je bij een verbouwing, wat moet elke fase opleveren en wanneer ben je klaar om naar de volgende fase te gaan?

It should **not** answer:
- which physical trade comes first → `/renovatie-plannen/renovatie-volgorde/`
- what kind of renovation the homeowner has / where to start → `/renovatie-plannen/huis-renoveren/`
- how to coordinate a whole-house multi-system renovation → `/renovatie-plannen/complete-renovatie/`

## Coverage matrix

| Need | Priority | Current page | Action |
|---|---|---|---|
| Explain phases vs physical work order | MUST | COVERED | Preserve prominently |
| Give an explicit lifecycle from orientation to handover | MUST | COVERED | Preserve 7-phase model |
| Define output/result of each phase | MUST | PARTIAL | Make consistent and concrete |
| Define a gate before moving to next phase | MUST | MISSING | Add `Ga pas door als...` per phase |
| Orientation / problems / wishes / existing state | MUST | COVERED | Tighten |
| Scope / design with explicit exclusions | MUST | COVERED | Preserve |
| Technical + regulatory feasibility before procurement | MUST | COVERED | Strengthen with official source |
| Budget, offers and contract decision | MUST | PARTIAL | Add contract/roles, not only prices |
| Execution preparation: materials, access, responsibilities, living situation | MUST | COVERED | Strengthen handoff readiness |
| Change / more-work control during execution | SHOULD | COVERED | Preserve written decision logic |
| Formal handover / defects / documentation | MUST | PARTIAL | Strengthen with VEH evidence |
| Identify when specialist/architect/bouwkundig advice may be useful | SHOULD | MISSING | Add calibrated routing, no universal requirement |
| Show which decisions can still remain open in each phase | SHOULD | MISSING | Add anti-overplanning guidance |
| Project documents / decision trail | SHOULD | PARTIAL | Add compact `projectdossier` concept |
| Project durations | OPTIONAL | MISSING | Do not add generic durations without scoped evidence |
| Generic physical order of demolition/installations/finishing | EXCLUDE | appropriately delegated | Keep out |

## Information gain opportunity

Do not compete by adding more phases. Compete by making the phase model operational.

### Asset 1 — phase gate
For every phase:
- central question;
- concrete output;
- `Ga pas door als...` gate.

This converts a generic lifecycle list into a homeowner decision system.

### Asset 2 — project dossier that grows with the project
Show which artifacts should exist by the time execution starts, for example:
- problem/wish inventory;
- scope + exclusions;
- drawings / technical decisions where needed;
- permit/notification result where relevant;
- budget + selected offer/contract;
- planning / responsibilities / access;
- written changes and more/less work;
- handover list, documentation and guarantees.

This is not a mandatory legal dossier; label it as a practical project record.

### Asset 3 — reversible vs irreversible decisions
Explain that not every aesthetic detail must be fixed early. The gate should focus on decisions that affect feasibility, price, contracts, technical routes or lead times. This avoids turning project phases into overplanning.

## Evidence hierarchy

Primary / authoritative:
- Rijksoverheid: regulatory checks before building/renovating.
- Omgevingsloket for project-specific permit/notification check.
- Vereniging Eigen Huis for homeowner preparation, offers/contracts, execution control and handover.

Secondary SERP competitors are used only for format and coverage comparison.

## Data gaps / claims not to make

- No universal duration per phase.
- No claim that every renovation requires an architect, bouwkundig adviseur or formal project manager.
- No universal legal list of documents for every renovation.
- No claim that seven phases are an official Dutch standard; this is the site's practical lifecycle model.

## Production acceptance criteria

- Preserve clear separation from `/renovatie-volgorde/`.
- Each of the 7 phases has a distinct output and gate.
- No `MUST = MISSING` after production.
- At least one official/regulatory source adjacent to feasibility claims.
- Handover reflects current Dutch homeowner guidance and written defect/rest-point capture.
- No invented timelines or generic cost figures.
- Generated page remains `noindex,follow`.