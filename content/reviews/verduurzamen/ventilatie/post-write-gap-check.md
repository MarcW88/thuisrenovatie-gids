# Post-write gap check — Ventilatie

- Route: `/verduurzamen/ventilatie/`
- Checked: 2026-09-13
- Workflow version: 2
- Result: `PASS`

## MUST coverage

| # | Requirement | Status | Evidence in page |
|---|---|---|---|
| 1 | Bestaand systeem herkennen | COVERED | sectie `Herken eerst welk systeem je nu hebt` + luchtstroomkaart |
| 2 | Toevoer + doorstroming + afvoer als keten | COVERED | luchtstroomkaart + aparte doorstromingssectie |
| 3 | Luchten ≠ ventileren | COVERED | directe quick answer + Rijksoverheid-context |
| 4 | Mechanische afvoer vraagt bewuste toevoer en blijft normaal aan | COVERED | systeemherkenning + kozijnmatrix + bronblok |
| 5 | Kozijnen/glas als ventilatiebeslismoment | COVERED | volledige kozijnsectie + interne links |
| 6 | Vier renovatieroutes | COVERED | optimaliseren / vraaggestuurde afvoer / decentrale WTW / centrale WTW |
| 7 | Centrale balansventilatie geen universele winnaar | COVERED | expliciet gekoppeld aan renovatiemoment/kanaalruimte |
| 8 | Decentrale balansventilatie als bestaande-woningroute | COVERED | eigen route met gevel-/geluidvoorwaarden |
| 9 | Doorstroom tussen kamers | COVERED | eigen sectie + offerte-item |
| 10 | Geluid/onderhoud/filtertoegang | COVERED | ontwerpsectie + checkpoint-grid + offerte |
| 11 | Inregeling/oplevercontrole | COVERED | eigen sectie + oplevertabel |
| 12 | Veilige vochtgrens | COVERED | eigen sectie + route naar vochtproblemen |
| 13 | Actuele ISDE 2026 met officiële bron | COVERED | RVO-sectie: combinatie met isolatie, €400, meldcodecheck |
| 14 | Volledige ventilatie-offertematrix | COVERED | systeem, ruimtes, luchtketen, kanalen, regeling, geluid, installaties, inregeling, onderhoud, subsidie |

MUST covered: **14/14**  
MUST partial: **0**  
MUST missing: **0**

## Cannibalisation check

### `/verduurzamen/isolatie/`
No blocking overlap. Parent page owns whole-home insulation priority; ventilatie owns air strategy.

### `/verduurzamen/dubbel-glas/`
No blocking overlap. Glass page owns glazing choice/U-value. Ventilatie only owns supply consequences after tighter glazing.

### `/renovatieprojecten/ramen-en-glas/`
No blocking overlap. Project page owns opening replacement/mounting. Ventilatie provides the pre-order system decision about supply/roosters.

### `/problemen-oplossen/vochtproblemen/`
No blocking overlap. Ventilatie flags inadequate air exchange as one possible factor and explicitly routes broader diagnosis away.

### `/renovatie-plannen/subsidies-renovatie/`
No blocking overlap. Only current ventilation-specific ISDE facts are stated; general application orchestration is routed onward.

## Factual gap check

- No unsupported universal ventilation rate.
- No universal CO2 diagnostic threshold.
- No claim that ventilation solves every moisture problem.
- No universal requirement for window vents.
- No claim that central WTW is always best.
- Current 2026 subsidy claim is explicitly time-bound and sourced to RVO.
- No fabricated national installation cost.

## Information-gain check

Distinctive assets present:

- `luchtstroomkaart`;
- four renovation routes instead of system ranking;
- explicit window-rooster decision by system type;
- transfer-air / doorstroming check;
- noise + maintainability design gate;
- commissioning / handover gate;
- functional-scope quotation matrix.

## GEO extractability

Direct answer blocks exist for:

- ventilation after insulation;
- natural/mechanical/balanced system recognition;
- airing versus ventilation;
- window vents after new frames;
- why more exhaust alone is insufficient;
- moisture/condensation boundary;
- 2026 ISDE ventilation.

## Conclusion

`PASS`

All 14 MUST items are fully covered with no blocking factual or cannibalisation gaps.
