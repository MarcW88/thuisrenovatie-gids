# Post-write gap check — Isolatie

- Route: `/verduurzamen/isolatie/`
- Checked: 2026-09-13
- Workflow version: 2
- Result: `PASS`

## MUST coverage

| # | Requirement | Status | Evidence in final page |
|---|---|---|---|
| 1 | No universal fixed isolation order | COVERED | Quick answer + four-outcome decision model |
| 2 | Whole-home `isolatiekaart` | COVERED | Dedicated isolation-map table |
| 3 | Current state over build year alone | COVERED | Isolation-map evidence row + build-year boundary |
| 4 | Now / combine / investigate / leave | COVERED | Four explicit decision outcomes |
| 5 | Moisture/leak/build-up stop gate | COVERED | Dedicated stop section and quick answer |
| 6 | Ventilation as parallel constraint | COVERED | Ventilation section + decision table + route to ventilation page |
| 7 | Future heating handoff without absolute rule | COVERED | Heat-pump section with bounded wording |
| 8 | Renovation moments as priority factor | COVERED | Roof/floor/facade/frames opportunity grid |
| 9 | Nature/protected-species pre-work check | COVERED | Dedicated official-source section |
| 10 | Current ISDE/24-month coordination | COVERED | Subsidy section + RVO source box |
| 11 | Cost context without fake whole-house total | COVERED | Cost section + Verbetercheck route |
| 12 | Shared quote scope | COVERED | Quote-normalisation table |

- MUST covered: **12/12**
- MUST partial: **0**
- MUST missing: **0**

## SHOULD coverage

- Build year as clue, not proof: COVERED.
- Previous work / invoices / drawings as evidence: COVERED.
- Energielabel/Verbetercheck as tools rather than truth: COVERED at the correct depth.
- Comfort alongside energy: PARTIAL but sufficient for parent-route role; no blocker.
- Biobased material not used as first decision layer: COVERED by omission/boundary; detail belongs later.
- Local energy desk: not included in body; non-blocking because the page already has clear official/technical routes.

## Ownership / cannibalisation check

### Parent vs child isolation pages
PASS.

The page decides **what to prioritise and when**. It does not reproduce detailed construction methods for roof, floor or facade.

### vs `/verduurzamen/dubbel-glas/`
PASS.

The page only treats glazing as one element of the isolation map and routes glass-type/performance detail onward.

### vs `/verduurzamen/ventilatie/`
PASS.

The page explains why ventilation must be checked in parallel but does not choose or design the ventilation system.

### vs `/verduurzamen/warmtepomp/`
PASS.

The page connects insulation to future heat demand without duplicating heat-pump selection.

### vs `/verduurzamen/energie-besparen/`
PASS.

The page remains envelope-specific rather than becoming a general energy-saving roadmap.

## Information-gain check

Distinctive assets present:

1. woningbrede `isolatiekaart`;
2. four outcomes instead of a fixed ranking;
3. renovation-moment matrix;
4. explicit moisture/unknown-build-up stop gate;
5. ventilation dependency before completion of scope;
6. nature check before relevant wall/roof work;
7. ISDE timing as coordination layer, not technical driver;
8. quote-scope normalisation across building elements.

## Factual gap check

No central unresolved factual claim remains.

Deliberate boundaries:

- no universal insulation sequence;
- no universal total price;
- no universal nature/permit outcome;
- no frozen RVO subsidy amount;
- no remote moisture/structural diagnosis;
- no `fully insulate before heat pump` absolute claim.

## GEO / extractability check

Direct answers are present for:

- which insulation first;
- how to know what is currently insulated;
- when to combine insulation with other renovation work;
- when to investigate before insulating;
- why ventilation belongs in the plan;
- how to compare isolation quotes;
- why the RVO 24-month period matters.

## Conclusion

`PASS`

The rewrite closes all 12 MUST gaps and creates a clear parent-page role without duplicating the measure-specific child pages.
