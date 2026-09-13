# SERP coverage — Isolatie

- Route: `/verduurzamen/isolatie/`
- Market: Nederland
- Checked: 2026-09-13
- Decision: `DEEP_REWRITE`

## Ownership decision

This page owns the **whole-home insulation decision**: what is already insulated, which part of the heated envelope is weakest, what should happen now versus at a planned renovation moment, and which moisture/ventilation/nature/subsidy constraints must be resolved before ordering work.

Child pages own execution-specific decisions:

- `/verduurzamen/isolatie/dakisolatie/` — roof type, existing build-up and roof-specific route;
- `/verduurzamen/isolatie/vloerisolatie/` — floor/bottom route, crawlspace and moisture;
- `/verduurzamen/isolatie/gevelisolatie/` — cavity/internal/external wall route and facade-specific constraints;
- `/verduurzamen/dubbel-glas/` — glass performance and glazing choice.

Adjacent ownership:

- `/verduurzamen/ventilatie/` — ventilation-system choice;
- `/verduurzamen/warmtepomp/` — heat-pump readiness and sizing/choice;
- `/verduurzamen/energie-besparen/` — broader energy-saving actions outside the insulation-envelope decision.

## Queries / sub-intents inspected

- huis isoleren
- woning isoleren
- welke isolatie eerst
- huis isoleren waar beginnen
- isolatie woning
- isolatie kosten 2026
- isolatie subsidie 2026
- dak vloer gevel glas isoleren
- isoleren en ventileren

## Current SERP pattern

### Milieu Centraal — Stappenplan voor een energiezuinig huis
Strong on:

- the order is explicitly **not fixed**;
- first inspect existing insulation, ventilation and solar shading;
- use drawings, invoices, previous-owner information and physical checks;
- start with parts of the heated home that are still uninsulated;
- combine improvements with logical renovation moments.

This is the strongest basis for rejecting a universal fixed isolation order.

### Milieu Centraal — Alles over isoleren / Verbetercheck
Strong on:

- roof, walls, floor and glazing as main envelope routes;
- actual savings/costs depend on current insulation level and dwelling characteristics;
- going from no insulation to good insulation is a different case from upgrading an already moderately insulated house;
- the Verbetercheck turns dwelling data into a house-specific plan.

### Rijksoverheid — Hoe kan ik mijn woning isoleren?
Strong on:

- the four broad routes: floor, facade, roof and insulating glazing;
- municipal energy desks as local help route;
- public routing to Milieu Centraal for measure-specific details.

### RVO — ISDE 2026 / insulation meldcodes
Strong on:

- current insulation categories and qualifying products;
- subsidy depends on type/product and m²;
- official meldcodes are continuously updated;
- the insulation subsidy can double when multiple qualifying measures are combined under the current 24-month rules and other conditions are met.

### Vereniging Eigen Huis — Isolatie woningen per bouwjaar
Strong on:

- building year as a useful first indicator;
- different building eras have different likely starting points;
- explicit reminder to check whether previous residents already improved the home.

Boundary: build year is a clue, not proof of today's insulation condition.

### Volkshuisvesting Nederland — Natuurvriendelijk Isoleren
Strong on:

- protected species can affect cavity-wall insulation;
- the current route can involve eDNA, a municipal SMP or a province-specific permit/research process;
- the correct route depends on local and property context.

### Current commercial / affiliate SERP
Recurring pattern:

- fixed `best order` lists;
- generic heat-loss percentages;
- cost-per-m² tables;
- material catalogues;
- lead forms;
- generic payback periods;
- subsidy tables copied into the article.

Problem: these formats often skip the current condition of each building element, planned renovation moments and the fact that a fixed order can be wrong for an already partly renovated house.

## Reader needs

1. Know what is actually insulated now, not what should be present based on age alone.
2. Decide which envelope part is weakest **for this house**.
3. Avoid paying twice for demolition/finishing by combining insulation with planned roof/floor/facade/window works.
4. Stop before insulating over moisture, leaks or an unknown build-up.
5. Understand that ventilation changes are part of the insulation decision.
6. Know when nature-protection checks must happen before wall/roof work.
7. Keep heat-pump decisions connected to future heat demand without creating a false `fully insulate first` rule.
8. Use current RVO logic for subsidy timing rather than stale copied amounts.
9. Compare contractor offers on one shared scope.

## Coverage matrix

| Need | Current page | Strong SERP | Priority |
|---|---|---|---|
| No universal fixed isolation order | PARTIAL | BEST-ONLY | MUST |
| Whole-home existing-state inventory | PARTIAL | COVERED | MUST |
| Evidence per building element, not build year only | MISSING | COVERED | MUST |
| `Now / combine / investigate / leave` decision | MISSING | Rare | MUST |
| Moisture/leak/build-up stop gate | PARTIAL | COVERED | MUST |
| Ventilation as parallel constraint | COVERED but brief | COVERED | MUST |
| Planned renovation moment in priority | PARTIAL | COVERED | MUST |
| Future heating handoff | PARTIAL | COVERED | MUST |
| Nature/protected-species pre-work check | MISSING | BEST-ONLY | MUST |
| Current ISDE 24-month coordination | MISSING | COVERED | MUST |
| Cost context tied to starting state | MISSING | COVERED | MUST |
| Shared quote scope across measures | PARTIAL | PARTIAL | MUST |
| Detailed material catalogue | MISSING | COVERED | MOVE/ROUTE |
| Detailed roof/floor/wall installation methods | MISSING | COVERED | MOVE/ROUTE |
| Detailed HR++ vs triple | MISSING | COVERED | MOVE/ROUTE |

## Information gain

### 1. `Isolatiekaart`
One row per envelope part:

- roof / facade / floor / glazing;
- inside or outside the heated envelope;
- current state: unknown / none / moderate / good;
- evidence source: visible measure, drawing, invoice, label, inspection;
- moisture/structural status;
- ventilation impact if airtightness changes;
- planned related work within 1–3 years;
- decision: now / combine / investigate / leave.

This prevents a generic house from being treated as if all four envelope parts were equally weak.

### 2. Four outcomes instead of a universal ranking

- **Now** — clearly weak, technically ready and no blocker.
- **Combine** — improvement makes sense, but another planned job creates a better intervention moment.
- **Investigate** — moisture, build-up, nature conditions or current insulation are uncertain.
- **Leave for now** — already reasonable/good or lower priority than another building element.

### 3. Renovation-moment matrix

Link each building element to works that already open or replace the same layer:

- roof work / dormer / attic conversion → roof insulation;
- new floor / underfloor heating → floor insulation;
- facade maintenance / extension → wall insulation;
- frame replacement → glazing and junction details.

### 4. Quote-scope normalisation

Never compare a cheap `€/m²` isolation quote with a more complete quote until these are aligned:

- net area;
- existing build-up and removal;
- target thermal performance/product code where relevant;
- preparation and repairs;
- moisture/nature/ventilation provisions;
- access/scaffolding;
- finishing;
- waste;
- guarantee;
- exclusions.

## GEO opportunities

Standalone extractable answers:

- Welke isolatie moet je eerst doen?
- Hoe weet je of je dak, muur of vloer al geïsoleerd is?
- Wanneer is het slimmer isolatie mee te nemen met ander renovatiewerk?
- Wanneer moet je eerst vocht of de opbouw onderzoeken?
- Waarom hoort ventilatie bij een isolatieplan?
- Hoe vergelijk je isolatieoffertes eerlijk?
- Wat betekent de ISDE-termijn van 24 maanden op hoofdlijnen?

## Internal overlap / cannibalisation

### `/verduurzamen/isolatie/`
Owns:

- whole-home insulation inventory;
- priority and timing;
- cross-building-element dependencies;
- decision to route into one or more child measures.

### Child insulation pages
Own:

- technical feasibility and method of the specific building element;
- measure-specific details and contractor questions.

### `/verduurzamen/energie-besparen/`
Owns:

- wider energy-saving order including behaviour/settings/installations/opwek;
- not the envelope-specific diagnostic and scoping workflow.

### `/verduurzamen/ventilatie/`
Owns:

- ventilation system selection and design.

### `/verduurzamen/warmtepomp/`
Owns:

- heating-system readiness and choice.

## Data gaps / claim boundaries

- No universal insulation order is valid for every house; the page must not invent one.
- No universal `cost to insulate a house` is meaningful without current condition, area and method.
- Build year is only a first clue because homes may have been retrofitted later.
- Do not diagnose moisture or structural condition remotely.
- Do not give a universal protected-species/permit outcome; route concrete cases to current local/provincial rules.
- Do not freeze one ISDE amount in the page when RVO's meldcodes and product conditions are continuously updated.

## Research gate

PASS for drafting.

All central MUST items have current evidence or a deliberate claim boundary. The main information-gain opportunity is to replace the generic fixed-order article with a dwelling-specific `isolatiekaart` and intervention-timing decision.
