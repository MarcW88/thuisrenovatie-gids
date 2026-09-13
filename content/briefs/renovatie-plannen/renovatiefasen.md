# Brief v2 - Renovatiefasen

- Route: `/renovatie-plannen/renovatiefasen/`
- Status: QA_IN_PROGRESS
- Market: Nederland / nl-NL
- Primary query: `renovatiefasen`
- Supporting queries: `fasen verbouwing`, `fases van een verbouwing`, `verbouwing van voorbereiding tot oplevering`
- Search intent: informational / project lifecycle
- SERP format: guide / checklist / phased process
- Decision: `LIGHT_UPDATE`
- Last researched: 2026-09-13
- Research: `content/research/renovatie-plannen/renovatiefasen/serp-coverage.md`

## Audience

Homeowner planning a renovation who understands roughly what they want but needs to know how the project matures from first inventory to handover.

## Job to be done

Help the reader know what each project phase must produce and when it is safe to move to the next one, without confusing project phases with the physical order of construction work.

## Page ownership

`renovatiefasen` owns the lifecycle:
1. inventarisatie;
2. ontwerp en scope;
3. haalbaarheid, regels en techniek;
4. begroting, offertes en contract;
5. uitvoeringsvoorbereiding;
6. uitvoering en wijzigingen;
7. oplevering en overdracht.

It does **not** own:
- where to start / renovation depth diagnosis → `/huis-renoveren/`;
- physical trade order → `/renovatie-volgorde/`;
- whole-house multi-system coordination → `/complete-renovatie/`.

## Editorial thesis

A useful renovation phase is not finished because time has passed. It is finished when the next phase no longer depends on a fundamental guess.

## Required architecture

Open with a direct distinction between project phases and work order.

For every phase provide:
- the central question;
- the concrete output;
- `Ga pas door als...` gate.

Add a compact practical `projectdossier` section showing which decisions/documents accumulate through the lifecycle. Label it clearly as a practical record, not a universal legal dossier.

Add a short section on decisions that do **not** need to be fixed early, to prevent overplanning of aesthetic details that do not affect feasibility, price, technical routes or lead times.

## Required evidence / entities

- Vereniging Eigen Huis: homeowner lifecycle, preparation, offers/contracts, execution control and handover.
- Rijksoverheid: regulatory checks for building/renovation.
- Omgevingsloket: project-specific permit/notification check.

Do not use commercial competitors as primary evidence for regulatory or contractual claims.

## Internal linking

Outbound where naturally useful:
- `/renovatie-plannen/huis-renoveren/`
- `/renovatie-plannen/renovatie-volgorde/`
- `/renovatie-plannen/renovatie-budget/`
- `/vakman-en-offertes/offertes-vergelijken/`
- `/vakman-en-offertes/offerte-controleren/`
- `/renovatie-plannen/renovatievergunning/`

## Anti-patterns

- Do not turn the page into a physical order of demolition, installations and finishing.
- Do not prescribe universal phase durations.
- Do not imply every project needs an architect, project manager or formal handover report.
- Do not make the seven-phase model sound like an official Dutch standard.
- Do not duplicate the `huis-renoveren` startscan.
- No generic FAQ block unless a question genuinely adds a distinct intent.

## Success criteria

- Reader can distinguish lifecycle from work order immediately.
- Every phase has a concrete output and gate.
- The page provides more operational value than a generic seven-step list.
- All MUST items in the research matrix are covered.
- No unsupported duration, cost or legal claim.
- Generated page remains `noindex,follow`.

## Voice

Use `content/brand/voice.md`: practical, expert, direct, independent. The phase model should feel like project guidance for a homeowner, not construction-management jargon.