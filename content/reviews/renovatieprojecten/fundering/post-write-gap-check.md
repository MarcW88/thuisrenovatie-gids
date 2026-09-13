# Post-write gap check — fundering

- Route: `/renovatieprojecten/fundering/`
- Reviewed: 2026-09-13
- Workflow version: 2
- Decision: `DEEP_REWRITE`

## MUST coverage

| MUST | Status | Evidence in final page |
|---|---|---|
| Explicitly start after diagnosis and route unresolved cases back to diagnostic page | COVERED | Opening, quick answer and `Heb je al genoeg onderzoek voor een herstelofferte?` link to `/problemen-oplossen/funderingsproblemen/` |
| State what research outcome is needed before repair quotations | COVERED | readiness table + `herstelklaar dossier` |
| Explain `bouwkundige eenheid` / multiple-owner issue | COVERED | dedicated H2 `Gedeelde fundering? Bepaal eerst de bouwkundige eenheid` |
| Introduce a repair-ready dossier | COVERED | dedicated dossier table |
| Translate dossier into a Programma van Eisen | COVERED | dedicated PvE section + checklist |
| Give all repair contractors the same information / relevant access | COVERED | quick answer, PvE and quotation-comparison sections |
| Compare method rationale, scope, consequence work, responsibilities, control and price structure | COVERED | foundation-specific quotation table |
| Separate contractor repair price from owner total `stichtingskosten` | COVERED | dedicated H2 and cost-group table |
| Make KCAF owner-side cost categories visible | COVERED | preparation, technical side work, house repair, project/stay cost groups |
| Provide a current cost-estimation route without fake universal average | COVERED | KCAF 2026 Herstelkostencalculator source box and explicit refusal of one national project price |
| Keep acute structural-safety boundary | COVERED | early `Veiligheidsgrens` note box |
| Continue through execution/control and post-repair evidence/registration | COVERED | `Tijdens de uitvoering` + `Wat leg je na funderingsherstel vast?` + NHR source |

MUST summary: **12 COVERED / 0 PARTIAL / 0 MISSING**

## SHOULD coverage

| SHOULD | Status | Evidence |
|---|---|---|
| Current Fonds Duurzaam Funderingsherstel context | COVERED | financing H2 + Rijksoverheid source box dated 28 August 2026 |
| Local support may differ | COVERED | financing paragraph mentions municipal arrangements without inventing locality-specific rules |
| `handhavingstermijn` when present in research report | COVERED | dossier table says relevant term/randvoorwaarden from investigation; brief/fact-check preserve claim boundary |
| Post-repair evidence for future management/taxation/sale/registration | COVERED | quotation and post-repair sections |

## Information gain check

- `herstelklaar dossier`: COVERED
- PvE before price: COVERED
- contractor price vs `stichtingskosten`: COVERED
- investigation → execution → proof loop: COVERED
- building-unit / owner coordination: COVERED
- KCAF property-level cost calculator rather than generic range: COVERED

## Cannibalisation check

### vs `/problemen-oplossen/funderingsproblemen/`

PASS. The diagnostic page owns signals and the decision to investigate. This page explicitly starts after investigation has shown that repair is needed and links back when that condition is not met.

### vs `/vakman-en-offertes/offertes-vergelijken/`

PASS. The generic page owns general quotation-comparison mechanics. This page owns foundation-specific tender inputs, PvE, building-unit coordination and scope normalization.

### vs `/renovatie-plannen/renovatiekosten/`

PASS. No generic cross-project price table is duplicated. Current KCAF calculator is used as an indicative project-specific route.

### vs `/renovatie-plannen/renovatievergunning/`

PASS. The page only tells readers to check the concrete repair plan where relevant and links to the general permit page. It does not publish a universal permit verdict.

## Fact / safety check

- No universal repair method: PASS
- No remote diagnosis: PASS
- No universal national repair price: PASS
- No automatic financing/subsidy promise: PASS
- No fixed legal owner cost-sharing formula: PASS
- Acute structural warning retained: PASS
- Fact-check artifact: PASS

## GEO / extraction check

Direct answer blocks now support:

- when repair quotations are ready;
- what belongs in a repair-ready dossier;
- why a PvE matters;
- what often sits outside the contractor price;
- how to compare foundation-repair quotations;
- what to document after repair.

Status: PASS.

## Result

**PASS — 0 MUST MISSING / 0 MUST PARTIAL**
