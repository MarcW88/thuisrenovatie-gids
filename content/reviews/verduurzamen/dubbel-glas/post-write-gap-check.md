# Post-write gap check — Dubbel glas

- Route: `/verduurzamen/dubbel-glas/`
- Checked: 2026-09-13
- Workflow version: 2
- Result: `PASS`

## MUST coverage

| # | MUST item | Coverage | Where |
|---|---|---|---|
| 1 | Existing glass, room use, frame, ventilation, future works | COVERED | `Maak eerst een glasbeslisstaat` |
| 2 | U-value as key performance metric | COVERED | `Kijk naar de U-waarde` |
| 3 | Five explicit routes | COVERED | `Geef iedere ruit één van vijf routes` |
| 4 | Heated vs unheated room prioritisation | COVERED | `Oud dubbelglas` section + table |
| 5 | Existing-frame suitability: condition/thickness/weight/opening parts | COVERED | glasbeslisstaat + HR++ route |
| 6 | HR++ as main glass-only route in suitable frames | COVERED | quick answer + route 2 |
| 7 | Triple primarily with new insulating frames / route project onward | COVERED | route 4 + project handoff |
| 8 | Vacuum glazing as contextual thin/high-performance option | COVERED | U-value cards + route 3 |
| 9 | Ventilation before order, without universal grille prescription | COVERED | `Ventilatie staat vast vóór je glas bestelt` |
| 10 | Summer comfort / orientation / external shading | COVERED | `Vergeet zomercomfort niet` |
| 11 | Current RVO meldcode/product check | COVERED | subsidy section + RVO source box |
| 12 | Price/scope normalization | COVERED | cost section + normalization table |
| 13 | External condensation explanation | COVERED | condensation section + diagnosis boundary |
| 14 | Glass-specific quotation matrix | COVERED | final quote table |

- MUST covered: **14/14**
- MUST partial: **0**
- MUST missing: **0**

## Ownership / cannibalisation check

### Against `/renovatieprojecten/ramen-en-glas/`

PASS.

The glazing page does **not** rebuild the project page's:

- gevelopeningenstaat;
- complete keep/repair/adapt/replace frame assessment;
- dimension/opening-function schedule;
- frame-to-wall installation specification;
- rain/water detail;
- pre-removal asbestos/nature gate;
- full frame finishing/handover scope.

Instead it owns:

- existing-glass assessment;
- heated-room filter;
- U-value;
- HR++ / triple / vacuum decision;
- glass-specific ventilation dependency;
- summer comfort;
- current glazing meldcode check;
- glass-only quote normalization.

The `glasbeslisstaat` is deliberately narrower than the project's `gevelopeningenstaat`.

### Against `/verduurzamen/ventilatie/`

PASS.

This page checks whether conscious air supply remains after glazing/airtightness changes, but does not choose or dimension a ventilation system.

### Against `/renovatie-plannen/subsidies-renovatie/`

PASS.

This page uses only the glazing-specific RVO meldcode gate and routes broader subsidy planning onward.

## Factual gap check

No central unresolved claim remains.

Explicit boundaries retained:

- triple + new frames is an evidence-based current advice route, not a universal technical law;
- HR++ suitability is frame-specific;
- vacuum glass is context-dependent;
- external condensation is explained as a possible normal condition, not diagnosed remotely;
- no fixed subsidy amount is hardcoded;
- no universal national price is presented.

## GEO / answer extraction

Direct answer blocks are available for:

- HR++ vs triple;
- when old double glazing is worth replacing;
- what U-value means;
- when vacuum glazing is interesting;
- ventilation after glazing replacement;
- external condensation;
- glass-offer contents;
- fair price comparison.

## Final gate

`PASS`

Ready for PUBLISH_REVIEW after generated-page and machine-gate verification.
