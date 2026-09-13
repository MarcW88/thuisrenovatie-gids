# Post-write gap check — Cv-ketel

- Route: `/verduurzamen/cv-ketel/`
- Checked: 2026-09-13
- Workflow version: 2
- Result: **PASS**

## MUST coverage

1. No general hybrid obligation from 2026 — **COVERED**
2. Age alone not used as hard replacement threshold — **COVERED**
3. Safety/failure/maintainability separated from energy choice — **COVERED**
4. Older open/semi-open boiler as separate safety route — **COVERED**
5. CO-vrij certified company required — **COVERED**
6. Shared flue/VvE gate — **COVERED**
7. Flue + combustion-air scope included in tender — **COVERED**
8. HR / hybrid / all-electric treated as different system scopes — **COVERED**
9. Domestic hot water separated from space heating — **COVERED**
10. Heat-pump readiness handed off to dedicated page — **COVERED**
11. Electric cv / induction cv not normalized as equivalent sustainable route — **COVERED**
12. Subsidy linked to heat-pump product/meldcode boundary — **COVERED**
13. Cost normalization across full functional scope — **COVERED**
14. Same-scope quotation matrix with commissioning/inregeling — **COVERED**

## Counts

- MUST covered: **14/14**
- MUST partial: **0**
- MUST missing: **0**
- unresolved high-risk claims: **0**
- blocking cannibalisation issues: **0**

## Information gain

PASS.

Distinctive assets now present:

- `ketelbeslisstaat` before product choice;
- retain/repair as explicit route instead of automatic replacement;
- open/semi-open boiler safety gate;
- shared flue / VvE gate;
- heating versus domestic-hot-water split;
- four-route replacement logic;
- system-scope cost normalization;
- boiler-specific quotation matrix.

## Cannibalisation review

PASS.

This page owns the **replacement moment and gas-boiler-specific scope**.

`/verduurzamen/warmtepomp/` retains ownership of:
- 50 °C readiness test;
- heat-loss/sizing basis;
- emitter readiness;
- outdoor-unit noise/placement;
- electrical capacity;
- heat-pump-specific quotation scope.

`/renovatie-plannen/subsidies-renovatie/` retains broad subsidy orchestration.

## GEO / extractability

PASS.

Standalone answers are present for:

- whether a cv boiler may still be installed in 2026;
- whether age alone means replacement;
- what to do with an old open boiler;
- shared flue in apartments;
- HR versus hybrid versus all-electric at replacement moment;
- electric cv versus heat pump;
- current certification requirement;
- what belongs in a boiler replacement quotation.

## Final result

**PASS — 14/14 MUST covered**