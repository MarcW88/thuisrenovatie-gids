# SERP coverage — Dakisolatie

- Route: `/verduurzamen/isolatie/dakisolatie/`
- Market: Nederland
- Checked: 2026-09-13
- Decision: `DEEP_REWRITE`

## Ownership decision

This page owns the **roof-insulation decision**: whether to insulate the roof plane or attic floor, pitched versus flat roof, inside versus outside, whether an existing layer can stay, moisture/vapour risks, timing with roof renovation and a comparable quote scope.

`/verduurzamen/isolatie/` owns whole-home prioritisation across roof, wall, floor and glazing.

The page should therefore go deep on roof-specific decision gates, but not repeat the whole-home insulation ranking.

## Queries / sub-intents inspected

- dakisolatie
- dak isoleren
- schuin dak isoleren
- dakisolatie binnenzijde of buitenzijde
- zoldervloer isoleren of dak
- plat dak isoleren
- bestaande dakisolatie verbeteren
- dakisolatie kosten 2026
- dakisolatie subsidie 2026

## Current SERP pattern

### Milieu Centraal — Dakisolatie
Strong on:

- checking what is already in the roof before choosing a method;
- roof plane versus attic-floor decision based on attic use and whether the attic can be closed off;
- inside and outside routes for pitched roofs;
- outside insulation as a logical combination with roof renovation;
- roof-height and gutter/neighbour junction consequences when insulating above the roof deck;
- flat roofs: professional installation, normally from the outside;
- explicit warning against internal flat-roof insulation because of moisture/wood-rot risk;
- improving mediocre existing insulation;
- vapour-layer position before adding a second layer;
- current advice level around Rd 3.8;
- protected-species / Omgevingswet check.

### RVO — ISDE / meldcodelijst isolatiematerialen
Strong on:

- current approved product/meldcode data;
- separate categories for roof insulation and attic/loft-floor insulation;
- product-specific thickness and subsidy data;
- need for current verification rather than static copied subsidy claims.

### 2026 commercial SERP — Homedeal / Werkspot
Recurring pattern:

- broad cost ranges per m²;
- inside versus outside price tables;
- pitched versus flat roof;
- material lists;
- subsidy amount snippets;
- lead form / quote CTA.

Problem: ranges are not directly comparable. Some include labour, some include complete roof-renovation context, and inside/outside/flat-roof scopes differ substantially.

## Reader needs

1. Decide whether the thermal boundary should be the roof or an attic floor.
2. Separate pitched and flat roof routes immediately.
3. Know when internal pitched-roof insulation makes sense.
4. Know when outside insulation is worth coordinating with roof renewal.
5. Avoid trapping timber between vapour-resistant layers.
6. Stop before insulating over leaks, moisture or damaged timber.
7. Understand the special risk of internal flat-roof insulation.
8. Know what nature/protected-species checks can block or alter work.
9. Compare prices only after route and inclusions are normalised.
10. Ask contractors to price the same roof build-up and junction scope.

## Coverage matrix

| Need | Current page | Strong SERP | Priority |
|---|---|---|---|
| Roof plane vs attic-floor decision | PARTIAL | COVERED | MUST |
| Pitched vs flat roof split | PARTIAL | COVERED | MUST |
| Inside pitched-roof route | PARTIAL | COVERED | MUST |
| Outside pitched-roof route | PARTIAL | COVERED | MUST |
| Roof-height / gutter / neighbour junctions | MISSING | BEST-ONLY | MUST |
| Flat roof: professional exterior route | MISSING | COVERED | MUST |
| Warning against internal flat-roof route | MISSING | COVERED | MUST |
| Existing insulation + vapour-layer check | PARTIAL | COVERED | MUST |
| Moisture/leak/timber stop gate | PARTIAL | COVERED | MUST |
| Protected-species / Omgevingswet pre-work gate | MISSING | BEST-ONLY | MUST |
| Cost scope normalisation | MISSING | PARTIAL | MUST |
| Roof-specific quote matrix | PARTIAL | Rare | MUST |
| Improve mediocre existing insulation | PARTIAL | COVERED | SHOULD |
| Current RVO/meldcode handoff | PARTIAL | COVERED | SHOULD |
| Future roof windows/dormer/PV coordination | PARTIAL | PARTIAL | SHOULD |
| Material catalogue | MISSING | COVERED | LOW / ROUTE AFTER METHOD |

## Information gain

### 1. `Dakroutekaart`

Before material selection, classify the project on five axes:

- thermal boundary: roof plane or attic floor;
- roof type: pitched or flat;
- current layer: absent / mediocre / adequate / unknown;
- technical state: dry and understood / unresolved moisture or build-up;
- work moment: insulation-only / roof renewal / interior renovation.

This turns the article from a list of products into a project decision.

### 2. Four routes

1. **Closed, unheated attic** → assess attic-floor insulation.
2. **Pitched roof that stays closed** → assess internal insulation only after build-up/vapour check.
3. **Pitched roof being renewed** → assess outside insulation while tiles/roof finish are already removed.
4. **Flat roof** → professional external design, preferably coordinated with roof-covering renewal.

### 3. `Bouwfysische stopgate`

No final scope while any of these is unresolved:

- active leak;
- unexplained condensation/mould;
- wet or damaged timber;
- unknown existing vapour layer when adding insulation;
- unclear flat-roof build-up.

### 4. Junction map

The quote should name junctions that change when the insulation layer changes:

- roof window;
- dormer;
- eaves/gutter;
- roof-to-wall;
- party-roof/neighbour junction;
- ridge where relevant;
- penetrations / flues / ventilation ducts;
- internal finish.

This is more useful than asking only for “X cm insulation”.

### 5. Price normalisation

Every price must be tagged with:

- pitched / flat;
- inside / outside / attic floor;
- area;
- material only or labour included;
- demolition/removal included;
- roof covering renewed or retained;
- scaffolding/access included;
- interior finish included;
- timber repair included/excluded;
- subsidy shown separately from gross price.

## GEO opportunities

Standalone extractable answers:

- Wanneer zoldervloer isoleren in plaats van het dak?
- Wanneer een schuin dak van binnen of buiten isoleren?
- Waarom is een plat dak aan de binnenzijde riskant?
- Kun je bestaande dakisolatie aanvullen?
- Welke vocht- en dampcontroles zijn nodig vóór dakisolatie?
- Welke aansluitingen moet een dakisolatie-offerte benoemen?
- Waarom zijn dakisolatieprijzen per m² vaak niet vergelijkbaar?

## Internal overlap / cannibalisation

### `/verduurzamen/isolatie/`
Owns:
- which building element to prioritise across the whole house;
- whole-home insulation map and timing.

### `/verduurzamen/isolatie/dakisolatie/`
Owns:
- roof-plane versus attic-floor route;
- pitched/flat split;
- inside/outside roof build-up;
- roof-specific moisture/vapour and junctions;
- roof-insulation quote scope.

### `/verduurzamen/ventilatie/`
Owns:
- system choice, supply/extract strategy and ventilation design.

This roof page may note that airtightness and roof works affect the envelope, but should route full ventilation-system advice onward.

## Data gaps / claim boundaries

- Commercial cost ranges are too scope-inconsistent to publish as a single universal €/m² figure.
- Milieu Centraal's current woningtype examples can be used as clearly labelled examples, not promises.
- Subsidy data changes. Use RVO as the source of truth and do not hard-code broad future-proof amounts without a dated check.
- Do not infer that a roof is moisture-safe without inspection of its actual build-up.
- Do not infer absence/presence of protected species remotely.
- Do not turn the page into detailed structural, roof-working-at-height or asbestos DIY instructions.

## Research gate

PASS for drafting.

All central MUST items have a current evidence base or an explicit safe boundary. The strongest information gain is the decision route plus build-up/junction normalisation, not another material list.
