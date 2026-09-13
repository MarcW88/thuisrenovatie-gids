# Post-write gap check — Renovatiebudget

- Route: `/renovatie-plannen/renovatie-budget/`
- Checked: 2026-09-13
- Decision entering production: `DEEP_REWRITE`

## MUST trace

| MUST from SERP coverage | Status | Where covered |
|---|---|---|
| Start from maximum financial room | COVERED | `Begin met een budgetplafond...` and four-concept distinction. |
| Separate estimate from budget | COVERED | Opening definitions + link to `renovatiekosten`. |
| Fixed/necessary scope | COVERED | Four budget parts + priority ladder. |
| Optional choices / cut list | COVERED | `Keuzes en opties` + MUST/SHOULD/COULD. |
| Project overhead | COVERED | Separate `Projectkosten` row with examples. |
| Contingency / reserve | COVERED | Dedicated reserve section + NN 10–20% guidance. |
| Project contingency vs household emergency buffer | COVERED | Dedicated source box and explanation. |
| Quotes and commitments replacing estimates | COVERED | Five-number dashboard with `vastgelegd` vs `verwacht`. |
| Stelposten / provisional sums | COVERED | Dedicated section; kept under expected uncertainty. |
| More/less work and changes during execution | COVERED | Event-driven reforecast section. |
| What to cut when total exceeds ceiling | COVERED | Priority ladder + dynamic EUR 80k scenario. |
| Rebudgeting milestones | COVERED | Fixed checkpoints plus event-driven recalculation. |
| Subsidy not treated as contingency | COVERED | Dedicated subsidy section. |

`MUST = MISSING`: 0

## SHOULD review

- `budgetplafond`, `begroting`, `vastgelegd`, `verwacht`, `vrij`, `reserve`: COVERED in plain-language definitions.
- No universal allocation percentages: PASS.
- EUR 80k example is dynamic and explicitly labelled illustrative: PASS.
- Signed quote / provisional amount distinction: COVERED via stelpost section.
- Financing remains concise and does not turn page into loan guide: PASS.

## Cannibalisation

- `/renovatiekosten/`: current market prices and price anatomy; this page links out rather than copying tables.
- `/offertes-vergelijken/`: supplier/scope comparison remains there.
- `/offerte-controleren/`: contract and offer-detail checking remains there.
- `/subsidies-renovatie/`: eligibility/amounts remain there.

Result: PASS.

## GEO / extraction

- Direct answer near top: PASS.
- Atomic definitions: PASS.
- Five-number dashboard is extractable: PASS.
- Numerical worked example is explicit and method-labelled: PASS.
- Current source dates are visible near volatile guidance: PASS.
- No manufactured FAQ block: PASS.

## Style / anti-slop

- No generic intro about renovation being difficult/exciting: PASS.
- No repeated fixed page template conclusion: PASS.
- No fake precision around personal financial capacity: PASS.
- Consumer guidance clearly distinguished from site-created method: PASS.

## Result

`PASS — READY_FOR_PUBLISH_REVIEW`
