# Post-write gap check — Dakisolatie

- Route: `/verduurzamen/isolatie/dakisolatie/`
- Checked: 2026-09-13
- Workflow version: 2
- Decision: `DEEP_REWRITE`

## MUST coverage

| # | Requirement | Status | Evidence in final page |
|---|---|---|---|
| 1 | Start with attic use / heated-space boundary | COVERED | Quick answer + `Dakroutekaart` starts with thermische grens. |
| 2 | Roof plane vs attic/loft floor | COVERED | Dedicated quick answer + route 1. |
| 3 | Pitched vs flat roof split | COVERED | `Vier routes` explicitly separates both. |
| 4 | Internal pitched-roof route | COVERED | Route 2 + vapour/build-up boundary. |
| 5 | External pitched-roof route | COVERED | Route 3 + roof-renovation timing. |
| 6 | Roof height / gutter / neighbour junction consequences | COVERED | Route 3 explicitly names all three. |
| 7 | Flat roof professional exterior route + internal warning | COVERED | Route 4 explicitly cites moisture/wood-rot/mould risk. |
| 8 | Existing insulation + vapour-layer check before adding layer | COVERED | `Vocht of onbekende lagen` + `Bestaande dakisolatie verbeteren`. |
| 9 | Leak/condensation/timber/unknown-build-up stop conditions | COVERED | Four checkpoint cards + explicit stopmoment. |
| 10 | Protected animals / Omgevingswet pre-work gate | COVERED | Dedicated nature section + stop-and-ecologist boundary. |
| 11 | Cost scope normalisation | COVERED | Cost section + 4-row comparison matrix + source-bounded example. |
| 12 | Roof-specific quote matrix | COVERED | Dedicated offer table covers build-up, route, performance, vapour/airtightness, junctions, repair/finish and conditions. |

## SHOULD coverage

- mediocre existing insulation improvement: COVERED;
- Rd 3.8 advice level separated from subsidy requirements: COVERED;
- RVO meldcode verification before order: COVERED;
- attic hatch / air leakage context: COVERED;
- dormer, roof window, PV and future heating coordination: COVERED;
- DIY boundary: COVERED through professional flat-roof route and no high-risk roof instructions.

## Cannibalisation check

### Against `/verduurzamen/isolatie/`
PASS.

The parent page remains responsible for whole-home prioritisation. This page starts only after the roof has become a candidate measure and owns the roof-specific route.

### Against `/verduurzamen/ventilatie/`
PASS.

No ventilation-system comparison is duplicated. The page focuses on roof build-up, vapour/moisture and airtight junction scope.

### Against `/renovatie-plannen/subsidies-renovatie/`
PASS.

The article uses RVO as current source of truth and does not duplicate the full ISDE decision tree.

## Information-gain check

Distinctive assets present:

1. `dakroutekaart`;
2. four non-interchangeable roof routes;
3. building-physics stop gate;
4. work-moment matrix;
5. price-scope normalisation;
6. roof-specific quote matrix including junctions.

## Unresolved factual claims

- Central unresolved claims: **0**.
- Source-bounded cost example: clearly labelled.
- Current subsidy values: deliberately not hard-coded.
- Nature/permit outcome: deliberately not determined remotely.

## Final gap result

- MUST covered: **12/12**
- MUST partial: **0**
- MUST missing: **0**
- Blocking cannibalisation issues: **0**
- Unbounded high-risk claims: **0**

`PASS`
