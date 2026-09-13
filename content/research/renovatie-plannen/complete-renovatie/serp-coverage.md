# SERP coverage matrix - Complete renovatie

- Route: `/renovatie-plannen/complete-renovatie/`
- Research date: 2026-09-13
- Market: Netherlands / Dutch
- Primary query family: `complete renovatie`, `complete woningrenovatie`, `totaalrenovatie woning`, `complete renovatie kosten`
- Decision: **DEEP_REWRITE**

## Search intent

The SERP is mixed commercial/informational. Searchers want to understand:

1. what a `complete` or `totale` renovation actually includes;
2. what cost scale to expect;
3. whether it is smarter to renovate everything at once or in phases;
4. how to coordinate multiple trades and avoid rework;
5. whether they can remain in the property during the works;
6. what must be defined before asking for serious quotes.

The page should not become another generic `huis renoveren` or `renovatie stappenplan` page. Its unique job is **integrated whole-house coordination** when several building systems and trades affect each other.

## SERP observations

### Recurring patterns

Current ranking pages commonly cover:

- definition / what is included in a total renovation;
- broad price ranges or €/m2 estimates;
- kitchen, bathroom, electrical, plumbing, insulation and finishes as typical scope items;
- one contractor / one project manager as a coordination proposition;
- phased versus all-at-once execution;
- generic planning or quote CTAs.

### Price inconsistency is itself a finding

Commercial 2026 sources use materially different definitions and price bands for `complete renovatie`:

- Homedeal: complete woningrenovatie around EUR 60,000-150,000+ as a broad market indication;
- MULTI Klussenbedrijf: around EUR 60,000-150,000 for an 80-120 m2 complete renovation, with higher ranges for structural changes;
- Archi/Sulerr: around EUR 160,000-250,000+ for a 120 m2 `complete` scope that includes facade, roof, installations, kitchen/bathrooms and structural work;
- Bouwctrl: around EUR 50,000-150,000 for a 100 m2 `volledige woningrenovatie`, depending on depth.

These ranges are too inconsistent to present as a reliable Dutch national average. The page should use them only to demonstrate that **scope definition changes the number**, not to promise a universal cost.

### Stronger sources for decision logic

- Vereniging Eigen Huis: define the works clearly, compare several offers, document contract scope and plan an explicit handover.
- Rijksoverheid / Omgevingsloket: project-specific permit and building-rule checks remain necessary even in a large renovation.
- Milieu Centraal / Vereniging Eigen Huis: major renovation is a logical moment to coordinate insulation, ventilation, heating and future technical space rather than treat them as isolated products.
- Nationale-Nederlanden 2026: after clarifying scope and comparing offers, keep a 10-20% contingency for unexpected cost.

## Coverage matrix

| Reader need / query | Priority | Current page | Required treatment | Ownership |
|---|---|---|---|---|
| What counts as a complete renovation? | MUST | COVERED | Define by interdependencies, not room count | this page |
| What is usually included? | MUST | PARTIAL | Show systems / work packages, but avoid implying every project includes all | this page |
| When does an integrated approach become necessary? | MUST | PARTIAL | Add an interdependency test | this page |
| What does a complete renovation cost? | MUST | PARTIAL | Explain why one national average is unreliable; give one clearly labelled market orientation plus cost-model logic | this page + `/renovatiekosten/` |
| Which factors move the total most? | MUST | PARTIAL | Structure, envelope, installations, wet rooms, finish level, logistics, temporary housing | this page |
| All at once or phased? | MUST | COVERED but generic | Decision matrix based on shared interfaces / rework risk / occupancy / cashflow | this page |
| Can I stay in the house? | SHOULD | COVERED | Replace vague answer with habitability test: water, toilet, heat, cooking, safe access, dust/separation | this page |
| Who coordinates the work? | MUST | COVERED but generic | Define coordination interfaces and decision ownership; self / main contractor / architect or adviser depending project | this page |
| What must be fixed before quotes? | MUST | PARTIAL | Add minimum integrated scope baseline | this page |
| How do I manage changes? | SHOULD | MISSING | Link to lifecycle/change-management logic without duplicating `/renovatiefasen/` | this page + `/renovatiefasen/` |
| How do sustainability systems interact? | SHOULD | PARTIAL | Explain insulation + ventilation + heating + technical-space interfaces | this page + `/verduurzamen/` |
| Permit / rules | SHOULD | PARTIAL | Brief route to official check; no universal rule | `/renovatievergunning/` |
| Exact work order | NOT OWNER | PARTIAL | Summarise only; route to `/renovatie-volgorde/` | `/renovatie-volgorde/` |
| Generic project lifecycle | NOT OWNER | TOO MUCH in old closing list | Remove generic six-step duplication | `/renovatiefasen/` |

## Information gain to build

### 1. Complete-renovation interdependency test

Editorial heuristic, explicitly labelled as such:

A project behaves like an integrated renovation when a change in one of these groups materially changes two or more others:

- structure / layout;
- envelope / insulation / windows;
- electrical / plumbing / heating / ventilation;
- floor build-up and fixed levels;
- kitchen / bathroom / fixed joinery;
- occupancy / logistics.

The heuristic is not a legal or technical classification. Its purpose is to tell the homeowner when separate trade-by-trade decisions become risky.

### 2. Interface map

Show which decisions must be made together:

- layout <-> structure <-> service routes;
- insulation / airtightness <-> ventilation <-> heating demand;
- floor build-up <-> underfloor heating <-> doors / thresholds <-> kitchen levels;
- windows / facade <-> ventilation / shading / heating;
- wet rooms <-> drainage / ventilation / electrical zones / floor levels.

### 3. One-go vs phased decision matrix

Do not claim that one approach is universally cheaper. Compare:

- shared demolition/opening work;
- temporary services;
- duplicate protection / access / setup;
- ability to keep living in the home;
- cashflow;
- dependency on future decisions.

### 4. Minimum integrated scope baseline before quotes

Before comparing total-renovation offers, make the same baseline visible to every bidder:

- what remains / goes;
- structural changes;
- installations retained / replaced;
- energy / comfort target;
- floor levels / major interfaces;
- finish level;
- exclusions / client-supplied work;
- occupancy and logistics assumptions.

### 5. Cost model instead of fake average

Explain cost as a stack of scope blocks:

- structure / shell;
- services;
- envelope / energy;
- kitchen / bathroom;
- interior finishes;
- design / permits / coordination;
- logistics / temporary housing;
- contingency.

Use current market ranges only as context and label secondary commercial sources clearly.

## Cannibalisation boundaries

- `/huis-renoveren/`: where to start and what to investigate before planning.
- `/renovatiefasen/`: project lifecycle, decisions and handoffs from inventory to handover.
- `/renovatie-volgorde/`: physical order of works.
- `/complete-renovatie/`: integrated coordination of a whole-house / multi-system renovation.
- `/renovatiekosten/`: current price benchmarks by project/component.
- `/renovatie-budget/`: financial allocation, reserve and budget control.

## Evidence set

Primary / stronger sources:

- Vereniging Eigen Huis, `Checklist verbouwen` - https://www.eigenhuis.nl/huis-verbeteren/klussen/verbouwen/checklist-verbouwen
- Vereniging Eigen Huis, `Offerte en contract bij verbouwing` - https://www.eigenhuis.nl/huis-verbeteren/klussen/verbouwen/aannemer-offerte-contract
- Rijksoverheid, `Stappenplan bij bouwen en verbouwen` - https://www.rijksoverheid.nl/themas/bouwen-en-wonen/bouwregelgeving/stappenplan-bij-bouwen-en-verbouwen
- Milieu Centraal, `Verbouwen en verduurzamen` - https://www.milieucentraal.nl/huis-en-tuin/verbouwen/
- Milieu Centraal, `Stap voor stap naar een energiezuinig huis` - https://www.milieucentraal.nl/energie-besparen/aardgasvrij-wonen/stappenplan-voor-een-energiezuinig-huis/
- Nationale-Nederlanden, `Wat kost een verbouwing?`, updated 2026-07-01 - https://www.nn.nl/Inspiratie/Wat-kost-een-verbouwing.htm

Secondary market orientation:

- Homedeal 2026 - https://www.homedeal.nl/verbouwing/verbouwing-kosten/
- MULTI Klussenbedrijf 2026 - https://multiklussenbedrijf.nl/blog/wat-kost-complete-woningrenovatie
- Archi/Sulerr 2026 - https://archi.sulerr.com/nl/blog/kosten-renovatie-woning-2026
- Bouwctrl 2026 - https://bouwctrl.nl/blog/kosten-volledige-woning-renovatie

## Gate before writing

No blocking evidence gap for the editorial decision.

Do **not** write:

- a national `average complete-renovation cost` as if one definition exists;
- a universal duration;
- a universal rule that phased renovation is more expensive;
- a universal requirement for an architect or main contractor;
- a universal permit answer.
