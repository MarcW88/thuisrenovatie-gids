# SERP coverage matrix - Renovatievolgorde

- Route: `/renovatie-plannen/renovatie-volgorde/`
- Workflow: `renovation-analysis-workflow v2`
- Decision: `DEEP_REWRITE`
- Market: Nederland / nl-NL
- Researched: 2026-09-13
- Primary query: `renovatie volgorde`
- Close variants inspected: `volgorde verbouwing`, `huis verbouwen volgorde werkzaamheden`, `volgorde renovatiewerken`, `eerst keuken of vloer verbouwing`

## Search intent and ownership

Dominant intent: informational / procedural. The reader wants an explicit physical work order that reduces rework and explains dependencies between trades.

This URL owns **execution order**: what must physically happen before something else can be closed, measured, installed or finished.

It does not own:

- the pre-planning readiness question -> `/renovatie-plannen/huis-renoveren/`;
- the project lifecycle from inventory to handover -> `/renovatie-plannen/renovatiefasen/`;
- whole-house coordination / phasing -> `/renovatie-plannen/complete-renovatie/`;
- detailed room/project scopes -> `/renovatieprojecten/`.

## SERP inspected

| Result | Type | Observed coverage | Useful signal |
|---|---|---|---|
| vtwonen.nl - `beste volgorde voor verbouwing` (16 Mar 2026) | editorial guide | broad sequence, demolition, utilities, walls/ceilings, kitchen/sanitary, floor, finishing | explicit sequence is expected; kitchen/floor is a recurring decision point |
| DamTask - `renovatie-planner` (29 Jul 2026) | interactive tool + guide | project inputs, complexity score, execution sequence, duration/attention points | personalization is an information-gain opportunity; static page should at least explain exceptions |
| DRO Renovaties - `volgorde verbouwing stappenplan` (17 Jun 2026) | contractor guide | plan/budget -> design -> permits -> demolition/construction -> installations -> insulation -> finishing -> handover | SERP often mixes project phases with physical order; our page must stay narrower |
| Home Plaza - kitchen/bathroom/floor sequence (27 May, updated 18 Aug 2026) | scenario guide | scope, demolition, utilities, wet rooms, kitchen prep, floor, kitchen, finishing | concrete dependencies outperform a purely generic sequence |
| Invorm Boekel - leidingwerk/vloer/keuken sequence (28 Jul 2026) | specialist guide | utilities -> wall finishing -> floor -> kitchen, with measurement dependency | readers search for pairwise decisions, not only a master list |

Market mismatch observed and excluded from ownership decisions: Belgian/Vlaanderen pages can illustrate patterns but are not used for Dutch regulatory claims.

## Official / stronger evidence for sensitive claims

- Omgevingsloket, `Woning verbouwen`: location + activity determine whether a permit, notification or information duty applies; demolition/asbestos can be separate activities.
- Rijksoverheid, `Checken of vergunning nodig is voor (ver)bouwen`: use the Vergunningscheck; a demolition notification is required if more than 10 m3 waste is released, and asbestos often triggers a notification duty.
- Milieu Centraal, asbestos guidance: renovation/demolition in pre-1994 buildings can require asbestos inventory; stop work if suspected asbestos is encountered and verify the correct procedure.
- Milieu Centraal / Vereniging Eigen Huis: floor renovation, insulation, floor heating and final floor finish form a technical stack; insulation/ventilation/heating choices should be coordinated rather than treated as isolated finishing jobs.

## Coverage matrix

| Reader need / SERP expectation | Priority | Current page | Required action |
|---|---|---:|---|
| Give a usable default physical sequence | MUST | COVERED | Preserve, but simplify into execution layers rather than pretending one rigid order fits every house |
| Explain *why* each layer comes before the next | MUST | PARTIAL | Add explicit dependency/checkpoint logic |
| Separate execution order from project phases/planning | MUST | PARTIAL | Sharpen boundary with `huis-renoveren` and `renovatiefasen`; remove planning content from the main sequence |
| Put demolition behind regulatory/safety blockers | MUST | PARTIAL | Add a short pre-sloop gate for permit/notification/asbestos/structural uncertainty |
| Explain what must be complete before walls/floors are closed | MUST | PARTIAL | Add closure checkpoints for utilities, ventilation, inspection/access and future routes |
| Address kitchen vs floor without a false universal rule | MUST | PARTIAL | Add scenario-based decision framework; floor type/build-up and kitchen support/measurement decide |
| Address underfloor heating / floor build-up dependency | MUST | PARTIAL | Make it an explicit example of hidden-work-before-finish logic |
| Address insulation + ventilation/heating interaction | SHOULD | PARTIAL | Explain coordination and route detail to `/verduurzamen/` |
| Explain occupied / phased renovation exception | SHOULD | COVERED | Keep, but distinguish zone-by-zone logistics from technical dependency order |
| Show stop signs that mean the sequence must pause | MUST | PARTIAL | Add blocker box: unknown structure, moisture source, asbestos suspicion, unresolved routes/levels |
| Make the sequence useful for handoff between trades | SHOULD | MISSING | Add `klaar-voor-de-volgende-vakman` checkpoints |
| Give pairwise decision help beyond generic competitors | SHOULD | PARTIAL | Add compact matrix: before stuc/closing, before floor, before kitchen, before paint |
| Add current legal/safety evidence only where needed | MUST | PARTIAL | Source Omgevingsloket/Rijksoverheid and Milieu Centraal next to pre-sloop claims |
| Preserve GEO extractability without artificial FAQ | SHOULD | PARTIAL | Direct answer + atomic dependency statements + real comparison/checkpoint table |

## Information gain selected

1. **Dependency-first sequence**: the order is not just a list of trades; each transition has a condition that must be satisfied before the next layer hides or depends on the previous one.
2. **Closure checkpoints**: practical `do not close yet` checks before plaster/walls, floor finish, kitchen installation and final painting.
3. **Exception framework**: kitchen/floor, underfloor heating, occupied renovation and future phases are treated as decision cases rather than contradictory one-line rules.
4. **Trade handoff readiness**: explain when a job is ready for the next trade, not merely what number comes next.

## GEO / citation opportunities

Useful extractable statements, only if retained with context:

- A safe default is: blockers resolved -> demolition -> structural/weatherproof work -> hidden installations -> insulation/build-up -> closure/drying -> fixed fit-out/floor decisions -> final finish and commissioning.
- Anything that must remain accessible or can still move belongs before the layer that hides it.
- There is no universal `floor before kitchen` rule; floor build-up, finish type, kitchen support and final measurement determine the order.
- If suspected asbestos appears during demolition, stop work and verify the required procedure before continuing.

## Cannibalisation check

### Versus `/huis-renoveren/`
`huis-renoveren` now owns readiness before planning: state, scope, dependencies, uncertainty, quote readiness. This page starts once the physical scope is sufficiently known and answers execution order.

### Versus `/renovatiefasen/`
`renovatiefasen` owns project lifecycle: inventory, design, feasibility, procurement, execution preparation, execution/change management, handover. This page must not reproduce those seven project phases.

### Versus `/complete-renovatie/`
`complete-renovatie` owns cross-system coordination and whether to renovate in one go or phases. This page may explain an occupied/phased exception but should not become a project coordination guide.

## Data gaps

- No verified keyword volume, Search Console query data, backlink data or CTR data available for this page.
- No reliable universal duration for each execution layer; do not invent timings.
- No universal rule for floor-vs-kitchen across all floor and kitchen systems; keep scenario logic instead of a single prescription.
- SERP position order is dynamic; the analysis uses currently retrievable results, not a fixed rank claim.

None of these gaps blocks the intent or the selected information gain.

## Handoff

`DEEP_REWRITE` may proceed.

Required MUST coverage in the brief:
- explicit default physical sequence;
- dependency reason for transitions;
- pre-sloop safety/regulatory gate;
- hidden-work / closure checkpoints;
- kitchen-floor exception logic;
- underfloor-heating/floor-build-up dependency;
- stop conditions;
- clean separation from `huis-renoveren` and `renovatiefasen`.
