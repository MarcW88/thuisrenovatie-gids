# Brief v2 - Renovatiebudget

- Route: `/renovatie-plannen/renovatie-budget/`
- Status: QA_IN_PROGRESS
- Primary query: `renovatie budget` / `verbouwing budget maken`
- Reader task: turn available money and changing project costs into a controllable renovation budget.
- Decision: DEEP_REWRITE
- Last researched: 2026-09-13

## Search task

The reader already knows or is discovering what the renovation may cost. This page must answer a different question: how much can be spent safely, how should that money be allocated, and how do you keep control when offers, provisional sums or changes move the forecast?

## Core distinction

- `renovatiekosten` = what comparable work currently costs;
- `begroting` = expected cost of the chosen project;
- `budgetplafond` = maximum amount the homeowner chooses to make available;
- `reserve` = project contingency for uncertainty;
- household emergency buffer = separate personal financial safety net.

Do not blur those concepts.

## Required method

Build the page around a live control model, not a static one-off allocation.

Always keep five numbers visible:
1. total budget ceiling;
2. `vastgelegd`: signed/committed amounts that are sufficiently fixed;
3. `verwacht`: known work or provisional amounts not yet fully fixed;
4. project `reserve` for uncertainty;
5. `vrij`: room that can still be assigned to options or later decisions.

`Stelposten`, unresolved quantities and likely extra work must remain visible as uncertainty. Do not silently count them as fixed prices.

## Priority ladder

Before offers arrive, classify choices as:
- MUST: necessary for safety, functionality, approved scope or dependencies;
- SHOULD: high-value choices that can be simplified if necessary;
- COULD: finish/options that can be delayed or removed without breaking the project.

If the forecast exceeds the ceiling, adjust COULD/SHOULD before raiding the contingency without thought.

## Evidence

- Nationale-Nederlanden, `Wat kost een verbouwing?`, updated 1 July 2026: clarify scope, compare several offers, practical 10–20% extra buffer.
- Nationale-Nederlanden, `Je verbouwing betalen?`, updated 23 June 2026: reserve 10–20% for unexpected renovation costs and keep a financial buffer after the renovation.
- Vereniging Eigen Huis, `Verbouwen: maak een plan`: determine total budget and decide what falls away if an offer is above budget.
- Vereniging Eigen Huis, `Verbouwen: offerte en contract aannemer`: a `stelpost` is an estimate, not a fully known final amount.

Present 10–20% as consumer guidance, never as a technical rule for every project.

## Worked example

Use an illustrative EUR 80,000 budget dynamically:
- EUR 52,000 necessary/selected works;
- EUR 8,000 optional choices;
- EUR 7,000 project overhead;
- EUR 13,000 contingency.

Then show what happens if selected work rises EUR 4,000 and an unexpected technical issue adds EUR 3,000. The non-reserve forecast becomes EUR 74,000, leaving EUR 6,000. If the homeowner still wants EUR 10,000 contingency, at least EUR 4,000 of optional work must be cut/postponed or the ceiling must consciously change.

State explicitly that this is an illustration, not a recommended allocation.

## Boundary

Do not reproduce current project price tables from `/renovatiekosten/`. Link to that page.
Do not become a mortgage/personal-loan guide. Financing options may be mentioned briefly and routed outward.
Do not reproduce detailed contract checking from `/offerte-controleren/`.

## Voice

Practical, numerate and calm. No financial scare tactics. No fake precision. Make trade-offs explicit.