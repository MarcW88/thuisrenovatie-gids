# Brief v2 - Renovatievolgorde

- `workflow_version`: 2
- Route: `/renovatie-plannen/renovatie-volgorde/`
- Status: `BRIEF_READY`
- Market: Nederland / nl-NL
- Primary query: `renovatie volgorde`
- Supporting cluster: `volgorde verbouwing`, `huis verbouwen volgorde werkzaamheden`, `volgorde renovatiewerken`, `eerst keuken of vloer`
- Search intent: informational / procedural
- Reader: homeowner with a sufficiently defined renovation scope who now needs to sequence physical work
- Reader task: know what must physically happen before what, why, and which project choices can legitimately change the default order
- Decision: `DEEP_REWRITE`
- Research artifact: `content/research/renovatie-plannen/renovatie-volgorde/serp-coverage.md`
- Last researched: 2026-09-13

## Job to be done

"Mijn verbouwing is voldoende duidelijk om de uitvoering te plannen. Geef me een bruikbare hoofdvolgorde, laat zien welke afhankelijkheden ik niet mag omdraaien en help me herkennen wanneer de standaardvolgorde niet geldt."

## Ownership

This page owns **physical execution order**.

Exclude from the core:

- deciding whether the renovation is ready to plan -> `/huis-renoveren/`;
- project phases such as inventory, design, procurement and change management -> `/renovatiefasen/`;
- complete-renovation coordination / one-go-vs-phased strategy -> `/complete-renovatie/`;
- detailed project-specific scopes -> `/renovatieprojecten/`.

## Thesis

A renovation sequence is useful only when it explains dependencies. The practical rule is: resolve blockers first, then work from structural and hidden work toward layers that close, cover or depend on that work. The page should give a default order but make clear exactly where floor build-up, kitchen installation, occupied renovation or future phases can change it.

## MUST coverage

1. A direct, usable default physical sequence.
2. Why each layer precedes the next, not just a numbered list.
3. A pre-sloop gate for unresolved structure, permit/notification and asbestos risk.
4. Hidden-work checkpoints before walls/ceilings/floors are closed.
5. A kitchen-vs-floor explanation that does not pretend one order always wins.
6. Underfloor heating and floor build-up as a concrete dependency example.
7. Stop conditions that pause the sequence when a central unknown remains.
8. Explicit boundary with `huis-renoveren` and `renovatiefasen`.

## SHOULD coverage

- insulation, ventilation and heating coordinated as one dependency;
- occupied / phased-renovation exception;
- `ready for next trade` checkpoints;
- contextual routing to the relevant detailed page rather than duplicating it.

## Evidence / entities

- Omgevingsloket `Woning verbouwen` and Vergunningscheck for location/activity-specific permit or notification outcome.
- Rijksoverheid `Checken of vergunning nodig is voor (ver)bouwen` for demolition notification context.
- Milieu Centraal asbestos guidance for pre-1994 renovation/demolition and stop-work handling when suspected asbestos appears.
- Vereniging Eigen Huis / Milieu Centraal for floor replacement, floor heating, insulation and ventilation dependencies.

Do not turn competitor contractor sequences into hard technical or legal facts. Use them only to understand the SERP and recurring reader decisions.

## Information gain

### 1. Dependency-first sequence

For every execution layer, answer:
- what belongs here;
- what must be known/complete before it;
- what goes wrong if the next layer starts too early.

### 2. Closure checkpoints

Create a compact practical framework for:
- before walls/ceilings are closed or plastered;
- before a final floor finish is installed;
- before kitchen/custom work is fixed;
- before final paint/finish.

### 3. Exceptions without contradiction

Explain:
- floor before or after kitchen depends on build-up/finish/support/measurement;
- underfloor heating belongs to floor build-up, before final finish;
- occupied renovation may be zoned, but shared technical routes still need global coordination;
- future phases can justify empty conduits/routes or leaving access.

## Proposed structure

Do not copy a generic 8-step article template. Suggested editorial flow:

1. direct answer: default execution spine;
2. pre-sloop blockers;
3. the execution layers with `ready to move on when...` checkpoints;
4. the four decisions that commonly change the order;
5. `do not close yet` matrix;
6. occupied/phased exception;
7. concise routing to next logical pages.

The final heading count and components can change if the copy reads better another way.

## Internal links

Outbound when contextually justified:
- `/renovatie-plannen/huis-renoveren/` for readers whose scope is not ready;
- `/renovatie-plannen/renovatiefasen/` for project lifecycle;
- `/renovatie-plannen/complete-renovatie/` for multi-system coordination;
- `/renovatie-plannen/renovatievergunning/` for permit detail;
- `/renovatieprojecten/keuken-renovatie/` for kitchen-specific scope;
- `/verduurzamen/ventilatie/`, `/verduurzamen/isolatie/`, `/verduurzamen/warmtepomp/` only where a technical dependency naturally hands off.

## Anti-patterns

- no project-lifecycle stappenplan;
- no false universal `keuken altijd vóór/na vloer` rule;
- no invented durations or drying times;
- no safety/legal claim without source;
- no repeated `belangrijk/cruciaal/essentieel` rhetoric;
- no artificial FAQ block;
- no fixed number of steps just to match a title.

## Voice

Use `content/brand/voice.md`: practical, calm, decision-oriented. Safety passages become sober and unambiguous. No contractor-sales voice.

## Success criteria

- A reader can extract a default order within seconds.
- A reader understands the dependency rule behind it.
- A reader can identify at least the major cases where the order changes.
- The page no longer overlaps the lifecycle role of `renovatiefasen`.
- Every MUST in the research matrix is `COVERED` or defensibly `PARTIAL` in post-write review.
