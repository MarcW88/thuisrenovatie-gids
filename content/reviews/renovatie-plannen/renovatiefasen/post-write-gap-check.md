# Post-write gap check — Renovatiefasen

- Route: `/renovatie-plannen/renovatiefasen/`
- Reviewed: 2026-09-13
- Research source: `content/research/renovatie-plannen/renovatiefasen/serp-coverage.md`
- Decision: `LIGHT_UPDATE`

## MUST coverage

| Requirement | Status | Evidence in final page |
|---|---|---|
| Explain phases vs physical work order | COVERED | Opening + closing compare-grid explicitly separate lifecycle from `/renovatie-volgorde/` |
| Explicit lifecycle from orientation to handover | COVERED | Seven named phases from inventory through handover |
| Concrete output of each phase | COVERED | Every phase contains a `Resultaat van fase X` block |
| Gate before moving to next phase | COVERED | Every phase contains `Ga pas door als...` or equivalent completion gate |
| Orientation / current state / wishes | COVERED | Phase 1 |
| Scope / design with explicit exclusions | COVERED | Phase 2 explains included and excluded work |
| Technical + regulatory feasibility before procurement | COVERED | Phase 3 + Rijksoverheid / Omgevingsloket source box |
| Budget, offers and contract decision | COVERED | Phase 4 includes same-scope comparison, responsibilities, payments and written agreements |
| Execution preparation | COVERED | Phase 5 covers lead times, access, temporary arrangements, living situation and handoffs |
| Formal handover / defects / documentation | COVERED | Phase 7 + Vereniging Eigen Huis source box |

`MUST = MISSING`: none.

## SHOULD coverage

| Requirement | Status | Notes |
|---|---|---|
| Change / more-work control | COVERED | Phase 6 treats unexpected findings and owner changes as written decisions |
| Specialist / architect / bouwkundig advice calibrated | COVERED | Phase 1 says this can be useful for larger/complex work but is not universal |
| Decisions that can remain open | COVERED | Dedicated section on reversible / late decisions |
| Practical project record | COVERED | Dedicated `projectdossier` table, explicitly labelled non-universal and non-legal |

## Exclusions respected

- No generic physical sloop-installaties-afwerking sequence duplicated from `/renovatie-volgorde/`.
- No universal phase durations.
- No universal cost figures.
- No claim that seven phases are an official Dutch standard.
- No claim that every renovation requires an architect, project manager or formal legal dossier.
- No manufactured FAQ section.

## Evidence check

### Regulatory feasibility
Status: CONFIRMED.

Rijksoverheid's current `Stappenplan bij bouwen en verbouwen` covers checks for omgevingsplan, welstand, bouwvoorschriften and omgevingsvergunning. The page routes the project-specific decision to Omgevingsloket rather than presenting a universal answer.

### Preparation / offers / contract
Status: CONFIRMED.

Vereniging Eigen Huis' current `Checklist verbouwen` recommends a clear description of the works, requesting and comparing offers and making clear contract agreements before execution.

### Handover
Status: CONFIRMED.

Vereniging Eigen Huis states that a formal handover is not always customary for renovations, but recommends planning a moment with the contractor to review the work and record open points. The final page preserves that nuance.

## Cannibalisation check

- `/huis-renoveren/`: pre-planning diagnosis and readiness.
- `/renovatiefasen/`: project lifecycle and decision gates.
- `/renovatie-volgorde/`: physical execution order.
- `/complete-renovatie/`: coordination of interdependent whole-house systems.

Central answers are not interchangeable after the update.

## Voice / anti-slop

PASS.

The repeated `central question / result / gate` structure is retained because it performs a functional navigation job for this specific page. It is not reused as a site-wide editorial template. No unsupported specificity, generic conclusion, forced FAQ, fake statistic or universal rule was added.

## Result

PASS — eligible for PUBLISH_REVIEW
