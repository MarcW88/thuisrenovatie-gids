# Post-write gap check — Ramen en glas

- Route: `/renovatieprojecten/ramen-en-glas/`
- Checked: 2026-09-13
- Decision: `DEEP_REWRITE`

## MUST coverage

| MUST | Status | Evidence in final page |
|---|---|---|
| Four decisions per opening: keep / repair / adapt + glass / replace complete unit | COVERED | `Vier routes per raam of deur` |
| Shared `gevelopeningenstaat` | COVERED | Dedicated opening schedule table |
| Frame condition before glass choice | COVERED | Quick answer + routes 2/3 |
| Explicit ownership boundary with `/verduurzamen/dubbel-glas/` | COVERED | Quick answer, route 3, sidebar and internal link |
| Ventilation consequence before ordering | COVERED | `Bepaal ventilatie vóór je de kozijnen bestelt` |
| Frame-to-wall sealing / airtightness in scope | COVERED | `Het kozijnproduct is maar één deel van de montage` + montagegate |
| Water detail + interior/exterior finishing visible | COVERED | Montagegate + quote matrix |
| Pre-1994 asbestos putty/sealant check, safely bounded | COVERED | `Controleer vóór de oude kozijnen eruit gaan` |
| Uninsulated cavity / nature-protection check | COVERED | Same pre-removal section + Omgevingsloket route |
| Explain why €/m² glass, €/m² frame, €/window and project total differ | COVERED | Dedicated price-normalisation table |
| Cost context without fake universal average | COVERED | Costs section explains the data gap and scope-first approach |
| Quote matrix: product/performance, sizes/opening parts, installation, ventilation, demolition/waste, finishing, guarantee, exclusions | COVERED | `Wat moet in een kozijnenofferte staan?` |

## SHOULD coverage

| SHOULD | Status | Note |
|---|---|---|
| Material choice wood/plastic/aluminium without fake winner | PARTIAL | Not expanded into a generic material comparison; intentionally secondary to project scope |
| Orientation / solar shading | PARTIAL | Orientation captured in the opening schedule; detailed solar/glass choice remains on the glazing route |
| Guarantees / quality / branch context | COVERED | Guarantee row + VEH support |
| Handover check | COVERED | Final section reuses the same per-opening scope for handover |

## Cannibalisation check

### `/renovatieprojecten/ramen-en-glas/`
Owns:
- replacement project;
- per-opening inventory;
- keep/repair/adapt/replace decision;
- ventilation and installation handoff;
- pre-removal constraints;
- comparable quotations.

### `/verduurzamen/dubbel-glas/`
Owns:
- HR++ / triple / vacuum comparison;
- U-values and energy performance;
- savings/comfort;
- ISDE details and current meldcodes.

Result: `PASS` — overlap reduced to necessary handoff context.

## Information gain check

- `gevelopeningenstaat`: PRESENT
- four-way decision model: PRESENT
- `montagegate`: PRESENT
- price-unit normalisation: PRESENT
- explicit cost-data gap: PRESENT
- pre-removal asbestos/nature checks: PRESENT
- quote comparison from identical opening schedule: PRESENT

## Blocking gaps

- MUST = MISSING: **0**
- MUST = PARTIAL: **0**
- unresolved central factual claim: **0**
- unresolved cannibalisation blocker: **0**

## Result

`PASS`

The page is ready for `PUBLISH_REVIEW`. The non-blocking SHOULD items are deliberately kept light to avoid turning the project page into another generic material/glass buying guide.
