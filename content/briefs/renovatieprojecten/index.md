# Brief v2 — Renovatieprojecten hub

- Route: `/renovatieprojecten/`
- Status: QA_COMPLETE
- Market: Netherlands / nl-NL
- Primary role: project-selection and scoping hub
- Decision: `DEEP_REWRITE`
- Last researched: 2026-09-13

## Search intent and page role

The hub should not behave like another generic renovation article. Literal `renovatieprojecten` intent is mixed and often portfolio/inspiration-led. The page therefore earns its place through information architecture: help homeowners select the correct project route and understand what has to be clear before a project can be priced sensibly.

## Core answer

A renovation project becomes comparable when the desired outcome, what stays/changes, major technical dependencies and unresolved risks are explicit enough that multiple contractors can price the same assignment. Different project types need different pre-quote questions.

## Required information architecture

1. **Direct answer:** choose the project route by the kind of change or uncertainty.
2. **Five project routes:** bathroom, kitchen, extension, foundation, windows/glass.
3. **Project-type model:**
   - room + services project;
   - structural/extra-space project;
   - diagnosis-to-repair project;
   - building-envelope replacement project.
4. **Different pre-quote questions per type** rather than one fixed four-step template.
5. **Minimum projectbrief:** desired outcome, keep/remove/move, technical dependencies, rules/constraints, unresolved unknowns, quote boundary.
6. **Escalation to complete renovation:** if a project forces linked decisions across multiple systems/rooms, route to integrated planning.
7. **Quote handoff:** only compare contractors once the main scope-driving decisions are clear.
8. **What can stay open:** finishes/products that do not change structure, services, permit needs or quote boundary can remain flexible.

## Child-page ownership

### Bathroom renovation
Owns wet-room scope: layout, plumbing, drainage, electrical zones, ventilation, waterproofing/build-up and finish level.

### Kitchen renovation
Owns kitchen scope: keep/replace/move, layout, water/drainage, electrical capacity, ventilation/extraction and appliance/finish boundary.

### Aanbouw
Owns extension-specific questions: purpose/size, structural connection, foundation, building envelope, daylight, heating/services and regulatory check.

### Foundation
Owns the repair project after investigation. It must not imply that visible symptoms alone identify the correct repair. Link symptoms/diagnosis to `/problemen-oplossen/funderingsproblemen/`.

### Windows and glass
Owns replacement-project scope: existing frames, replacement vs glass-only, installation details, ventilation provisions and interface with facade work. Energy-choice depth belongs to `/verduurzamen/dubbel-glas/`.

## Cannibalisation boundaries

- `/renovatieprojecten/` = select/scoping of a bounded project.
- `/renovatie-plannen/` = broad project planning decisions across lifecycle, order, cost, budget, permit, subsidy and ROI.
- `/renovatie-plannen/complete-renovatie/` = integrated coordination when one project is no longer bounded.
- Child project pages = depth for their specific project.

## Evidence register

- Milieu Centraal — `Verbouwen en verduurzamen`: project works such as aanbouw and kozijnen are opportunities to coordinate insulation, ventilation/heating and avoid double work.
- Vereniging Eigen Huis — `Verbouwen: maak een plan`: current situation and desired outcome should be clarified before quote requests.
- Vereniging Eigen Huis — `Wat kost verbouwen` (price level 2026): different renovation categories carry different scope and cost drivers.
- Rijksoverheid — `Stappenplan bij bouwen en verbouwen`: project-specific building/permit checks may apply.

No broad hub-level project prices or universal durations should be published.

## GEO / extractability requirements

- Direct 1–3 sentence answers at major decision points.
- Clear atomic definition of `projectscope` and `projectbrief`.
- Route-specific statements should be self-contained enough to quote.
- No FAQ padding and no invented universal process.

## Voice / style

- Practical and architectural rather than contractor-sales language.
- Avoid repeating `eerst bepalen, dan offertes` as a slogan in every section.
- Use concrete project differences to create rhythm.
- Keep the hub shorter than child guides.

## QA completion

- SERP/content-gap matrix persisted.
- Ownership/cannibalisation map explicit.
- No blocking data gaps.
- Ready for source-of-truth rewrite and post-write review.
