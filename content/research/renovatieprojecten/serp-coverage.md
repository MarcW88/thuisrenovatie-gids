# SERP coverage — Renovatieprojecten hub

- Workflow version: 2
- Route: `/renovatieprojecten/`
- Market: Netherlands / nl-NL
- Review date: 2026-09-13
- Decision: `DEEP_REWRITE`

## Query set

Primary discovery set:
- `renovatieprojecten woning`
- `huis verbouwen projecten`
- `woning verbouwen badkamer keuken aanbouw`
- `verbouwing project kiezen`

Related project intents inspected:
- badkamer renoveren
- keuken renoveren
- aanbouw plaatsen
- funderingsproblemen herstellen
- ramen en glas vervangen

## SERP / evidence inspected

| Source | Page type | Relevant signal |
| --- | --- | --- |
| Milieu Centraal — Verbouwen en verduurzamen | consumer guidance hub | Project type changes the technical opportunities: aanbouw, kozijnen/ramen and other works should be coordinated with insulation, ventilation and heating to avoid double work. |
| Vereniging Eigen Huis — Verbouwen: maak een plan | consumer planning guidance | Start from current situation and desired outcome before requesting quotes. |
| Vereniging Eigen Huis — Wat kost verbouwen | current price benchmark | Treats kitchen, bathroom/toilet, aanbouw, dakkapel and zolder as distinct project scopes; pricing only becomes meaningful when scope is comparable. |
| Rijksoverheid — Stappenplan bij bouwen en verbouwen | official rules | Building/renovation projects can trigger omgevingsplan, welstand, technical rules and permit checks. |
| Homedeal — Stappenplan huis verbouwen | commercial broad guide | Generic lifecycle content is already abundant and should not be duplicated by this hub. |
| DamTask — Renovatie-planner | planning tool | Broad renovation planning/sequence is already a separate intent from project-specific decision support. |

## Intent finding

The literal query `renovatieprojecten` is ambiguous and often surfaces contractor portfolios, construction projects or inspiration rather than a strong consumer-planning SERP. The hub therefore should not pretend to own one broad high-intent keyword. Its strategic role is cluster navigation and project selection: help a homeowner identify which project guide owns the next decision.

## Coverage matrix

| Reader need | Current status | Priority | Information-gain opportunity |
| --- | --- | --- | --- |
| Choose the correct project guide | COVERED | MUST | Route by the type of uncertainty, not only by room/object name. |
| Understand how project types differ before quotes | PARTIAL | MUST | Distinguish room renovation, extension, defect/repair and building-envelope project. |
| Know what must be clear before asking for quotes | PARTIAL | MUST | Provide a minimum project brief rather than one generic four-step workflow. |
| Know when diagnosis must precede a repair solution | PARTIAL | MUST | Make foundation route explicitly diagnosis-first. |
| Know when a single project becomes an integrated renovation | MISSING | MUST | Add escalation trigger to `/renovatie-plannen/complete-renovatie/`. |
| Avoid overlap between windows/glass project and energy glazing page | MISSING | MUST | Project page owns replacement scope/frames/installation; energy page owns HR++ vs triple decision. |
| Avoid overlap with broad planning hub | PARTIAL | MUST | This hub owns project selection and project-specific scoping, not lifecycle/order/budget/permit frameworks. |
| Route to quote comparison only when scope is comparable | COVERED | SHOULD | Convert into a concrete project-brief gate. |
| Include current price tables | NOT NEEDED | OPTIONAL | Delegate to `/renovatie-plannen/renovatiekosten/` and child pages where scope is specific. |

## Ownership / cannibalisation map

- `/renovatieprojecten/` — select project route and understand project-specific scoping.
- `/renovatie-plannen/` — broad planning decision router: phase, work order, costs, budget, permit, subsidy, ROI.
- `/renovatie-plannen/complete-renovatie/` — integrated multi-system coordination.
- `/renovatieprojecten/badkamer-renovatie/` — wet-room renovation scope and technical dependencies.
- `/renovatieprojecten/keuken-renovatie/` — kitchen scope, layout and service dependencies.
- `/renovatieprojecten/aanbouw/` — extension-specific structure, foundation, envelope, daylight, services and permission decisions.
- `/renovatieprojecten/fundering/` — repair project after diagnosis / investigation.
- `/problemen-oplossen/funderingsproblemen/` — symptoms and diagnosis trigger before selecting repair.
- `/renovatieprojecten/ramen-en-glas/` — replacement project: frames, glass, ventilation, installation scope.
- `/verduurzamen/dubbel-glas/` — energy decision: HR++ vs triple and insulation/ventilation trade-offs.

## Information gain to build

1. Project selector based on what changes: room/services, floor area/structure, defect/repair or building envelope.
2. Different pre-quote questions for each project type rather than a reusable generic template.
3. A `minimum projectbrief` that makes quotes comparable without forcing finish/product decisions too early.
4. A clear escalation rule: when one project forces decisions in several other systems, move to integrated-renovation planning.
5. Diagnosis-first warning for foundation work.

## GEO / extractability opportunities

- Direct definition of what a renovation project is on this site: a bounded change with a defined outcome, dependencies and quote scope.
- Atomic distinction between project scope and project plan.
- Atomic distinction between repair-from-diagnosis and chosen improvement project.
- Short routing statements for each child page.

## Data gaps

- No reliable single national SERP intent exists for the literal term `renovatieprojecten`; this is treated as an IA/support hub rather than grounds for inventing a keyword target.
- No project-wide price or duration figures are required on the hub; those belong to scoped child pages/current price sources.

## Gate

- Search intent ownership clear: YES
- MUST coverage explicit: YES
- Child-page boundaries clear: YES
- Blocking data gap: NO
- Ready for brief: YES
