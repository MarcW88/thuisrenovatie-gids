# Post-write gap check — Vloerisolatie

- Route: `/verduurzamen/isolatie/vloerisolatie/`
- Checked: 2026-09-13
- Workflow version: 2

## MUST coverage

| # | Requirement | Status | Where covered |
|---|---|---|---|
| 1 | Floor type, crawlspace, access/height, moisture and existing insulation first | COVERED | `Maak eerst een vloerroutekaart` |
| 2 | Floor insulation and ground insulation are distinct | COVERED | Quick answer + four routes |
| 3 | ~35 cm Milieu Centraal rule correctly bounded | COVERED | `35 cm is een route-indicatie, geen garantie` |
| 4 | Four decision routes | COVERED | `Kies daarna één van vier routes` |
| 5 | Lower direct thermal effect of ground insulation explained | COVERED | Quick answer + bodem route |
| 6 | Wooden-floor moisture/rot/fungi/ventilation gate | COVERED | `Een houten vloer krijgt eerst een conditiegate` |
| 7 | Leak/water/wood rot/concrete damage stop conditions | COVERED | moisture gate + aside stop moment |
| 8 | Pipes, sewer, hatch and ventilation in scope | COVERED | route map + `Laat ventilatiegaten en installaties niet verdwijnen` |
| 9 | Rd ≥3.5 and Rd ≥5 with UFH | COVERED | `Bij vloerverwarming wordt de isolatie-eis belangrijker` |
| 10 | Underfloor heating changes route/performance need | COVERED | UFH section + direct answer |
| 11 | Costs scoped rather than universal €/m² | COVERED | `Wat kost vloerisolatie?` |
| 12 | Floor-specific quote matrix | COVERED | `Wat moet in een vloerisolatie-offerte staan?` |

**MUST covered: 12/12**  
**MUST partial: 0**  
**MUST missing: 0**

## Evidence gaps

No blocking evidence gaps.

Boundaries deliberately retained:

- 35 cm is a practical rule of thumb, not a universal acceptance threshold;
- water/moisture source is not diagnosed remotely;
- no claim that ground insulation equals floor insulation;
- no universal national €/m² price;
- no remembered/generalised ISDE amount;
- RVO meldcodes must be checked at decision time.

## Cannibalisation check

### `/verduurzamen/isolatie/`
PASS. Parent remains the whole-home priority map; this page starts only once the floor is the relevant building element.

### `/problemen-oplossen/vochtproblemen/`
PASS. This page uses moisture as a stop gate but routes unresolved diagnosis to the troubleshooting page.

### `/renovatie-plannen/subsidies-renovatie/`
PASS. This page only establishes that floor and ground insulation are distinct RVO categories and routes general ISDE logic onward.

### `/vakman-en-offertes/offertes-vergelijken/`
PASS. Generic comparison remains there; this page owns the floor-specific technical scope.

## Information gain check

Present:

- `vloerroutekaart`;
- four-route decision instead of a product list;
- bounded ~35 cm access rule;
- moisture/condition gate;
- explicit thermal distinction between floor and ground insulation;
- UFH performance gate;
- route-specific cost normalisation;
- floor-specific quotation matrix.

## GEO / extractability

Direct answers present for:

- vloerisolatie vs bodemisolatie;
- crawlspace height;
- water/moisture first action;
- wooden-floor checks;
- Rd with underfloor heating;
- quote contents;
- why prices are not directly comparable.

## Result

`PASS`

The rewritten page covers all 12 MUST requirements with no blocking overlap or unresolved central factual claim.
