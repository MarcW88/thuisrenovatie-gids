# Post-write gap check — Aanbouw

- Route: `/renovatieprojecten/aanbouw/`
- Checked: 2026-09-13
- Workflow version: 2
- Decision: `DEEP_REWRITE`

## MUST coverage

| MUST | Status | Where covered | Evidence / note |
|---|---|---|---|
| Doel en gebruik vóór maatvoering | COVERED | Lead + `Wat doet de aanbouw met het huis dat er al staat?` | Page starts from function and impact on the existing house. |
| Constructieve impact geveldoorbraak | COVERED | Existing-house test + haalbaarheidsgate | Opening is explicitly a design input before scope/pricing. |
| Fundering as project-specific design input | COVERED | Haalbaarheidsgate + quote matrix | No generic foundation recipe; risk/assumptions must be explicit. |
| Daglicht impact on existing + new part | COVERED | Existing-house test + haalbaarheidsgate + IPLO source box | Existing room behind the extension is explicitly checked. |
| Isolatie / verwarming / ventilatie as linked interface | COVERED | Existing-house test + schil/installaties rows | Treated as integrated scope, not loose afterthoughts. |
| Project/location-specific rules + Vergunningcheck | COVERED | `Vergunningvrij betekent niet regelvrij` | Omgevingsloket and Rijksoverheid linked. |
| `Vergunningvrij ≠ regelvrij` | COVERED | Dedicated H2 + source box | Bbl/burenrecht caveat present. |
| Current 2026 price benchmark with scope | COVERED | `Wat kost een aanbouw in 2026?` | VEH price-level 2026, incl. VAT, explicit scope. |
| Casco / doorbraak / afbouw / installaties / inrichting separated | COVERED | Price caveat + `Casco, wind- en waterdicht of afgebouwd?` | Prevents false total-price comparison. |
| Offerte-ready gate with shared technical assumptions | COVERED | `Wanneer is een aanbouw offerte-klaar?` + quote comparison | Contractors are asked to price same basis. |

**MUST missing: 0**  
**MUST partial: 0**

## SHOULD coverage

| SHOULD | Status | Where covered | Note |
|---|---|---|---|
| Buren / erfgrens / execution access | COVERED | Quote comparison + official-rule text | Kept practical; no legal advice beyond official-source boundary. |
| Prefab vs traditional | COVERED | Dedicated section | No universal winner or fabricated speed/cost claim. |

## Information-gain survival check

- `Haalbaarheidsgate`: PRESENT
- `Bestaande-woning-test`: PRESENT
- `Casco is geen totaalprijs`: PRESENT
- `Offerteklaar ontwerp`: PRESENT
- Scoped VEH 2026 benchmark: PRESENT

## GEO / extractability

- Direct answer early in page: PASS
- Official permit distinction adjacent to claim: PASS
- Current price facts with source/scope/date: PASS
- IPLO technical distinction with claim boundary: PASS
- No artificial FAQ block: PASS
- No repeated answer snippets for bots: PASS

## Ownership / cannibalisation

- Broad permit mechanics delegated to `renovatievergunning`: PASS
- Broad renovation benchmark delegated to `renovatiekosten`: PASS
- Whole-house coordination delegated to `complete-renovatie`: PASS
- Foundation repair/diagnosis not absorbed into this page: PASS

## Style / quality passes

- Brand voice: PASS
- Humanizer / general-writing principles: PASS
- Anti-AI-slop review: PASS
- No cloned bathroom/kitchen structure: PASS
- No fake experience or inspection: PASS
- No universal build duration: PASS
- No unsupported permit shortcut: PASS

## Result

**PASS — ready for PUBLISH_REVIEW**