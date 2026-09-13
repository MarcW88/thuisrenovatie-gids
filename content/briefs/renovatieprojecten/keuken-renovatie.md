---
workflow_version: 2
route: /renovatieprojecten/keuken-renovatie/
decision: DEEP_REWRITE
market: Nederland
language: nl-NL
page_type: PROJECT
---

# Content brief — Keuken renovatie

## Primary query + cluster

Primary:
- `keuken renovatie`

Supporting:
- keuken renoveren
- keuken verbouwen
- nieuwe keuken waar beginnen
- keuken renovatie kosten
- keuken vervangen of renoveren

## Search intent

Commercial-informational hybrid. The reader is orienting on a renovation or new kitchen, but is often close enough to purchase that layout, technical preparation, price scope and quotation quality directly influence a large spend.

Dominant SERP format: hybrid guide + cost guidance + purchase preparation.

## Audience

Dutch homeowner with an existing kitchen who may:
- refresh the current kitchen;
- replace the kitchen in roughly the same layout;
- substantially change the layout and services;
- coordinate a kitchen retailer with a contractor / electrician / plumber.

They are not assumed to have technical building knowledge.

## Job to be done

Help the homeowner decide how deep the kitchen renovation goes, make the design technically order-ready, understand the real cost layers and give supplier / contractor the same preparation scope before committing.

## Ownership

This page owns:
- kitchen-specific scope choice;
- order readiness;
- layout-to-installation interfaces;
- kitchen-specific 2026 cost benchmarks;
- supplier / contractor handoff;
- kitchen-specific quotation scope.

It does not own:
- general renovation budget control (`/renovatie-plannen/renovatie-budget/`);
- general market-cost methodology (`/renovatie-plannen/renovatiekosten/`);
- generic offer comparison (`/vakman-en-offertes/offertes-vergelijken/`);
- whole-home energy strategy (`/verduurzamen/energie-besparen/`);
- universal project work order (`/renovatie-plannen/renovatie-volgorde/`).

## Thesis / angle

A kitchen is not ready to order when the visible design is finished. It is ready when the kitchen drawing and the technical preparation describe the same final kitchen: dimensions, services, electrical demand, extraction and finished building surfaces all line up, with clear responsibility for discrepancies.

## MUST coverage

1. Decide between refresh, replace in same layout, and layout-changing renovation.
2. Start from daily use / functions before style.
3. Lock the layout before technical preparation.
4. Verify real room dimensions and define who owns final measurement before order.
5. Translate appliance choices, especially induction, into an electrical / meter-cupboard check without giving DIY electrical design instructions.
6. Fix water, drainage and relevant hot-water routing before room finishes and order.
7. Check cooker hood / extraction against the dwelling ventilation system, including apartment/shared-channel exception.
8. Separate kitchen product price from building/installations preparation.
9. Publish current 2026 VEH kitchen benchmarks with scope and separate preparation figures.
10. Introduce an explicit `bestelgate` before final order.
11. Clarify kitchen supplier vs contractor / installers responsibilities.
12. Require a specified quotation and comparable end totals, supported by Consumentenbond.

## SHOULD coverage

- partial reuse / refurbishment when the base remains useful;
- sequencing dependencies between demolition, technical prep, finished floor/walls and installation;
- future electrification readiness only where directly triggered by the kitchen works;
- no unsupported universal duration.

## Required evidence

### Vereniging Eigen Huis — price level 2026
Use exactly as market guidance, not as a promised total:
- budget kitchen incl. montage: €3,990–€6,670;
- normal kitchen: €6,670–€14,475;
- luxury kitchen incl. montage: €14,475–€21,000;
- super-luxury kitchen incl. montage: €20,475–€30,600;
- professional kitchen demolition: €395–€1,340;
- moving water and electrics: €710–€1,050;
- extending meter cupboard: €395–€815.

Mention that VEH describes its 2026 renovation figures as market guide prices; actual costs vary with region, work location, extra costs and market conditions.

### Milieu Centraal — Nieuwe keuken
Required factual points:
- partial renovation can avoid unnecessary replacement when the base remains usable;
- induction may require an extra cable and usually additional meter-cupboard groups; grid connection reinforcement may also be necessary;
- extraction to outside removes cooking moisture more effectively than recirculation;
- apartment/shared mechanical exhaust may require a motorless hood / expert check;
- kitchen renovation can be used to anticipate future electric demand where the meter cupboard is already being changed.

### Consumentenbond — kitchen/bathroom purchase advice, updated 14 April 2026
Required factual points:
- prepare wishes / room measurements before showroom visit;
- request a specified quotation;
- equipment brand/type and installation costs should be visible;
- compare final amounts, not only discount percentages;
- no urgency / same-day sales framing in our copy.

## Information gain

### 1. `Bestelgate`
The page must define a project-control gate. The kitchen is sufficiently order-ready only when:
- actual room dimensions are verified;
- final layout / cabinet and appliance plan is fixed;
- water and drainage positions are fixed;
- appliance electrical requirements and meter-cupboard implications are checked;
- extraction route / compatibility is clear;
- finished floor and wall build-up that affects dimensions is known;
- structural changes affecting the room are resolved;
- final-measure responsibility and discrepancy handling are assigned.

Do not present this as law or a formal standard.

### 2. Two drawings
Use a concrete distinction:
- `keukentekening`: cabinets, equipment, worktop and visible dimensions;
- `voorbereidingstekening`: water, drainage, electrics, extraction, finished floor/wall levels and other building interfaces.

The reader should understand that the two drawings must match before order and execution.

### 3. Price anatomy
Use `keukenproduct` vs `voorbereiding` rather than one generic total. The VEH figures may be shown as benchmark ranges, while preparation items remain separate.

### 4. Responsibility handoff
Create a matrix for at least:
- inmeten;
- final kitchen drawing;
- preparation drawing;
- demolition;
- water/drainage;
- electrics/meter cupboard;
- extraction;
- finished walls/floor;
- installation / connection;
- completion defects.

The purpose is to expose gaps between supplier and contractor, not to prescribe one contract model.

## Proposed structure

Do not use the bathroom page's architecture.

Suggested flow:
1. direct answer / order-readiness thesis;
2. choose the depth of the renovation based on what remains;
3. design from use and room constraints;
4. `keukentekening` vs `voorbereidingstekening`;
5. explicit `bestelgate`;
6. technical issues that can block the order: induction/electrics, water/drainage, extraction, floor/wall level;
7. 2026 costs: kitchen product benchmark + separate prep items;
8. supplier/contractor responsibility matrix;
9. quotation comparison + next action.

## Internal links

Outbound, only where useful:
- `/renovatie-plannen/renovatiekosten/` — broader price methodology;
- `/renovatie-plannen/renovatie-budget/` — budget / reserve control;
- `/vakman-en-offertes/offertes-vergelijken/` — general quote comparison;
- `/renovatie-plannen/renovatie-volgorde/` — relation with floors/walls/installations;
- `/verduurzamen/energie-besparen/` only where future electrification becomes a next question.

Potential inbound after publication:
- `/renovatieprojecten/` hub;
- `/renovatie-plannen/renovatiekosten/` where kitchen example is relevant.

## Safety / exclusions

- no DIY design for gas, meter cupboard or high-load electrical circuits;
- no universal rule for cooker hoods in every apartment ventilation system;
- no universal permit verdict;
- no structural alteration advice without professional assessment;
- no invented dimensions, group sizes, cable specifications or ventilation flow rates;
- no universal number of renovation weeks;
- no claim that a new kitchen guarantees a property-value increase.

## Anti-patterns

Avoid:
- `de keuken is het hart van het huis`;
- showroom/inspiration fluff;
- generic style/trend sections;
- fake scarcity or sales urgency;
- a bathroom-page clone with six numbered decisions;
- generic price table without scope;
- a closing summary that merely repeats the article.

## Voice

Use `content/brand/voice.md`.
Tone: practical, technical enough to expose hidden dependencies, calm around purchase decisions, independent of retailers and contractors.

## Success criteria

Editorial:
- all MUST items are `COVERED` in post-write gap check;
- every volatile price has source/date/scope;
- the page has a clearly extractable definition of `bestelklaar`;
- `keukentekening` vs `voorbereidingstekening` is understandable without specialist knowledge;
- no structural clone of bathroom page;
- fact-check passes;
- PUBLISH_REVIEW can reach `PASS — READY_FOR_HUMAN_VALIDATION` without unresolved central data gaps.
