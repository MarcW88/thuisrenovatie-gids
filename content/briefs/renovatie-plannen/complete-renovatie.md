# Brief v2 - Complete renovatie

- Route: `/renovatie-plannen/complete-renovatie/`
- Status: QA_IN_PROGRESS
- Primary query: `complete renovatie` / `complete woningrenovatie` / `totaalrenovatie woning`
- Reader task: understand when a renovation needs integrated whole-house planning, what must be designed together, how to phase it and how to interpret cost ranges.
- Decision: **DEEP_REWRITE**
- Last researched: 2026-09-13
- Research artifact: `content/research/renovatie-plannen/complete-renovatie/serp-coverage.md`

## Search intent

Mixed informational/commercial. The reader expects definition, inclusions, cost scale, phasing and coordination. The page must satisfy those expectations without becoming a generic renovation steps article or a contractor landing page.

## Ownership

This page owns **integrated coordination of a whole-house or multi-system renovation**.

It does not own:

- where to start before the scope is known -> `/huis-renoveren/`;
- project lifecycle -> `/renovatiefasen/`;
- physical work order -> `/renovatie-volgorde/`;
- detailed current component prices -> `/renovatiekosten/`;
- budget allocation -> `/renovatie-budget/`.

## Central answer

A renovation should be treated as `complete` when several building systems or trades are so interdependent that deciding them separately creates a meaningful risk of redesign, rework or incomparable quotes. Room count alone is a weak definition.

## Required differentiating assets

### 1. Interdependency test

Give a practical, explicitly editorial test. If changing one system materially changes two or more other systems, treat the project as integrated until those interfaces are resolved.

Groups to use:

- structure / layout;
- envelope / insulation / windows;
- electrical / plumbing / heating / ventilation;
- floor build-up / fixed levels;
- kitchen / bathroom / fixed joinery;
- occupancy / logistics.

Do not present the test as a legal or engineering classification.

### 2. Interface map

Explain concrete interfaces:

- layout <-> structure <-> service routes;
- insulation / airtightness <-> ventilation <-> heating demand;
- floor build-up <-> underfloor heating <-> doors / thresholds <-> kitchen levels;
- windows / facade <-> ventilation / shading / heating;
- wet rooms <-> drainage / ventilation / electrical / floor levels.

### 3. Cost model, not a fake average

The page must say explicitly that current Dutch market guides use incompatible definitions of `complete renovation` and therefore publish materially different totals.

Allowed:

- one clearly labelled secondary-market orientation, e.g. Homedeal 2026 EUR 60k-150k+;
- explain that other guides using heavier structural/envelope scopes run materially higher;
- use a scope-block model: structure/shell, services, envelope/energy, wet rooms, finishes, project/logistics, contingency;
- link to `/renovatiekosten/` for project-level current benchmarks.

Not allowed:

- `average Dutch complete renovation costs X`;
- unsupported €/m2 promise;
- universal duration.

### 4. One-go vs phased matrix

Compare rather than prescribe. Consider:

- shared demolition/opening work;
- temporary services;
- repeated protection/access/setup;
- habitability;
- cashflow;
- future dependencies.

Core principle: execution can be phased, but future dependencies should be designed early when they affect today's work.

### 5. Habitability test

For staying in the house, evaluate whether the household can retain or safely replace:

- water;
- toilet / washing;
- heating when seasonally necessary;
- cooking;
- safe access / escape routes;
- separation from dust/noise/work zones.

Do not claim a universal threshold.

### 6. Minimum integrated scope before quotes

Every bidder should receive the same baseline:

- retained / removed scope;
- structural changes;
- installations retained / replaced;
- energy / comfort target;
- floor levels / key interfaces;
- finish level;
- exclusions / self-performed work;
- occupancy / logistics assumptions.

## Evidence and claim boundaries

Use strong sources for rules and process:

- Rijksoverheid / Omgevingsloket for permit and building-rule checks;
- Vereniging Eigen Huis for scope, multiple quotes, contract clarity and handover;
- Milieu Centraal / Vereniging Eigen Huis for integrating insulation, ventilation and heating at major renovation moments;
- Nationale-Nederlanden, updated 2026-07-01, for 10-20% contingency guidance after scope clarification and quote comparison.

Secondary commercial price guides may illustrate market spread but must be labelled as market orientation, not authoritative averages.

## Internal links required

- `/renovatie-plannen/huis-renoveren/`
- `/renovatie-plannen/renovatie-volgorde/`
- `/renovatie-plannen/renovatiefasen/`
- `/renovatie-plannen/renovatiekosten/`
- `/renovatie-plannen/renovatie-budget/`
- `/renovatie-plannen/renovatievergunning/`
- `/vakman-en-offertes/aannemer-kiezen/`
- `/vakman-en-offertes/offertes-vergelijken/`
- relevant `/verduurzamen/` handoff where useful

## Anti-patterns

- no generic six-step `voorbereiding` list that duplicates neighbouring pages;
- no claim that one contractor is inherently better than separate trades;
- no claim that all-at-once is always cheaper;
- no generic FAQ section unless a question materially improves navigation;
- no word-count padding;
- no unsupported cost precision.

## Success condition

The page should make a homeowner able to answer:

1. Is my project integrated enough to treat as a complete renovation?
2. Which systems must I decide together?
3. Why are online price ranges so inconsistent?
4. Can I phase execution without designing each phase in isolation?
5. What must be clear before I compare complete-renovation quotes?
