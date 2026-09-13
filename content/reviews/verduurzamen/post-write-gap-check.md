# Post-write gap check — `/verduurzamen/`

- Checked: 2026-09-13
- Workflow version: 2
- Decision: `DEEP_REWRITE`

## MUST coverage
1. Geen universele vaste volgorde — **COVERED**
2. Woning-nulmeting — **COVERED**
3. Blokkades vóór maatregelen — **COVERED**
4. Isolatie/kierdichting ↔ ventilatie — **COVERED**
5. Verwarming ↔ warmtevraag/afgifte/woningplan — **COVERED**
6. Zonnepanelen ↔ dak/toekomstig stroomgebruik — **COVERED**
7. Natuurlijke renovatiemomenten — **COVERED**
8. Unieke routing van child intents — **COVERED**
9. Grens met `/verduurzamen/energie-besparen/` — **COVERED**
10. Geen universele prijs/besparing/subsidie/ROI-rangorde — **COVERED**

**MUST covered: 10/10**  
**Partial: 0**  
**Missing: 0**

## SHOULD coverage
- buitenzonwering / zomercomfort — **COVERED**
- no-regret gate — **COVERED**
- subsidie doorlinken zonder duplicatie — **COVERED**
- rendement doorlinken zonder duplicatie — **COVERED**
- cv-ketel als afwijkend logisch instapmoment — **COVERED**

## Cannibalisation check

### Hub vs `/verduurzamen/energie-besparen/`
**PASS / resolved.**

The energy-saving child has now itself been rewritten in v2 and owns current consumption diagnosis: meter/bill baseline, four consumption buckets, small testable interventions and remeasurement. The hub owns investment routing, blockers, dependencies and renovation moments. The primary tasks are now distinct on both sides.

### Hub vs technical child pages
**PASS.**

The hub routes to the final child decision assets rather than duplicating them:
- isolatiekaart;
- dak/vloer/gevel routes;
- glasbeslisstaat;
- luchtstroomkaart;
- warmtepomp-gereedheidsdossier;
- ketelbeslisstaat;
- zonnestroomplan.

### Hub vs renovation work sequence
**PASS.**

No physical execution sequence is prescribed; `/renovatie-plannen/renovatie-volgorde/` keeps that ownership.

## Information gain
PASS.
- woning-nulmeting;
- volgende-blokkade-model;
- natuurlijke renovatiemomenten;
- startsituation router;
- no-regret gate.

## Factuality
`fact-check.md`: PASS.

## Final
**PASS — 10/10 MUST, no blocking gap.**
