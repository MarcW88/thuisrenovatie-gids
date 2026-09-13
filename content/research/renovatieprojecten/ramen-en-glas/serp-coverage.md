# SERP coverage — Ramen en glas

- Route: `/renovatieprojecten/ramen-en-glas/`
- Market: Nederland
- Checked: 2026-09-13
- Decision: `DEEP_REWRITE`

## Ownership decision

This project page owns the **replacement project**: which openings to tackle, whether an existing frame can stay/be repaired/must be replaced, ventilation and airtightness consequences, removal/mounting risks, finishing and comparable quotations.

`/verduurzamen/dubbel-glas/` owns the **energy/glass decision**: HR++ versus triple/vacuum glass, U-values, energy performance, subsidy conditions and when a glazing upgrade is worthwhile.

The current two pages overlap too strongly on `HR++ vs triple`, so the project page must stop being a second glass-comparison page.

## Queries / sub-intents inspected

- ramen vervangen
- kozijnen vervangen
- glas vervangen
- kozijnen vervangen kosten 2026
- kozijnen vervangen offerte
- glas of kozijnen vervangen
- ventilatie bij kozijnen vervangen

## Current SERP pattern

### Milieu Centraal — Kozijnen en deuren vervangen (updated 8 July 2026)
Strong on:
- ask first whether replacement is necessary; repair/adaptation may be possible;
- insulating frames/doors and U-value;
- ventilation when frames become tighter;
- double draught seals / closing quality;
- sealing frame-to-wall joints;
- rain detailing;
- nature-protection issue when replacing frames at an uninsulated cavity;
- possible asbestos-containing putty/sealant in frames/windows from before 1994.

### Milieu Centraal — Triple, HR++ or vacuum glass (updated 18 August 2026)
Strong on:
- glass choice and existing-frame suitability;
- HR++ in existing frames where technically possible;
- triple mainly with new frames in their advice;
- ventilation consequences;
- solar orientation / summer comfort;
- quote-conversation checklist.

This is primarily owned by our `/verduurzamen/dubbel-glas/` page, not this project page.

### Vereniging Eigen Huis — Kozijnen vervangen
Strong on:
- replacement reasons: condition and energy;
- existing frame may not suit thicker/heavier glazing;
- frame-to-wall sealing;
- ventilation during replacement;
- guarantee and comparing multiple offers;
- current page still displays cost/subsidy examples dated February 2025, so those figures are not suitable as our central 2026 benchmark.

### 2026 commercial SERP (Homedeal / Trustoo / other lead sites)
Recurring pattern:
- per-m² or per-frame price ranges;
- material comparison: wood / plastic / aluminium;
- HR++ / triple and subsidy;
- generic installation duration;
- lead form / quote CTA.

Problem: scopes vary heavily between `per raam`, `per m² kozijnoppervlak`, glass included/excluded, montage included/excluded, demolition/finishing included/excluded. Current market guides therefore do not provide one sufficiently stable national project total to publish as truth.

## Reader needs

1. Decide per opening whether to keep, repair, adapt or replace the frame.
2. Avoid choosing a glass product before frame condition and future facade plan are known.
3. Define opening type, ventilation strategy, airtightness and finishing before quotations.
4. Know which removal risks must be checked before work starts.
5. Compare quotations on the same opening schedule and same installation/finishing scope.
6. Understand why `€ / raam`, `€ / m² glas` and `€ / m² kozijn` are not interchangeable.
7. Route detailed glass/energy/subsidy questions to `/verduurzamen/dubbel-glas/`.

## Coverage matrix

| Need | Current page | Strong SERP | Priority |
|---|---|---|---|
| Keep / repair / adapt / replace frame | PARTIAL | COVERED | MUST |
| Explicit separation project vs glass-choice ownership | MISSING | Rare | MUST |
| Per-opening inventory / schedule | MISSING | Rare | MUST |
| Frame condition before glass choice | COVERED | COVERED | MUST |
| Ventilation plan after airtightness changes | COVERED | COVERED | MUST |
| Frame-to-wall sealing / installation detail | PARTIAL | COVERED | MUST |
| Interior/exterior finishing and disposal in quote | PARTIAL | PARTIAL | MUST |
| Pre-removal asbestos check for pre-1994 frames/putty | MISSING | BEST-ONLY | MUST |
| Nature-protection check at uninsulated cavity | MISSING | BEST-ONLY | MUST |
| Explain incompatible price units/scopes | MISSING | Rare | MUST |
| Current cost context without fake universal average | PARTIAL | COVERED but inconsistent | MUST |
| Material choice wood/plastic/aluminium | MISSING | COVERED | SHOULD |
| Guarantees / quality / branch affiliation | MISSING | COVERED | SHOULD |
| Solar shading / orientation | MISSING | COVERED | SHOULD |
| Detailed HR++ vs triple/subsidy | COVERED | COVERED | MOVE/ROUTE |

## Information gain

### 1. `Gevelopeningenstaat`
Create one row per window/door opening:
- location/orientation;
- current frame material and condition;
- current glazing;
- fixed/opening parts;
- ventilation provision;
- sill/water detail;
- interior/exterior finishing;
- keep / repair / adapt / replace decision;
- desired performance/functional outcome.

This becomes the shared input for every bidder.

### 2. Four-way decision instead of binary glass-vs-frame
For every opening distinguish:
- keep as-is;
- repair/maintain;
- adapt frame + replace glass;
- replace complete frame/window unit.

### 3. `Montagegate`
Before order/installation, resolve:
- final dimensions and opening direction;
- ventilation strategy;
- frame-to-wall sealing / airtightness;
- rain/water detailing;
- sill / trim / plaster / paint scope;
- removal and waste;
- known pre-removal constraints (asbestos/nature where relevant).

### 4. Price-unit normalization
Never compare:
- price per m² glass;
- price per m² complete frame;
- price per opening;
- whole-house total
as if they are the same unit.

Every public benchmark must be labelled with scope. Because current 2026 market sources use inconsistent scopes, the page should teach scope normalization instead of publishing one universal national total.

## GEO opportunities

Standalone extractable answers:
- Wanneer alleen glas vervangen en wanneer het kozijn?
- Wat moet je per raam/kozijn inventariseren vóór een offerte?
- Waarom moet ventilatie tegelijk met kozijnen worden bekeken?
- Welke risico's controleer je vóór het verwijderen van oude kozijnen?
- Welke onderdelen moeten in een kozijnenofferte staan?
- Waarom zijn prijzen per raam en per m² niet rechtstreeks vergelijkbaar?

## Internal overlap / cannibalisation

### `/verduurzamen/dubbel-glas/`
Owns:
- HR++ vs triple/vacuum glass;
- U-value/glass performance;
- energy savings;
- ISDE detail / meldcodes / qualifying glass;
- whether upgrading glazing is energetically worthwhile.

### `/renovatieprojecten/ramen-en-glas/`
Owns:
- frame/window replacement project;
- existing-condition inventory;
- per-opening scope;
- installation, ventilation and finishing handoff;
- removal risks;
- quotation comparison.

### `/renovatie-plannen/renovatievergunning/`
Owns general permission logic. This page only flags project-specific triggers and routes onward rather than giving a universal permit verdict.

## Data gaps / claim boundaries

- No sufficiently consistent authoritative 2026 national cost benchmark for complete frame replacement was found. VEH's displayed whole-house example is dated February 2025; current commercial 2026 guides use incompatible scope units. Do not invent a universal project price.
- No universal permit verdict for frame replacement.
- Do not prescribe asbestos handling; only flag pre-1994 putty/sealant as a check per Milieu Centraal.
- Do not claim every uninsulated-cavity replacement affects protected species; flag that nature-protection rules may apply and route to Omgevingsloket.

## Research gate

PASS for drafting.

All central MUST items have current evidence or an explicit safe boundary. The cost inconsistency is handled as an information-gain feature rather than papered over with a fake average.
