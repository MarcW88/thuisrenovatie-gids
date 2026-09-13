# Post-write gap check — Gevelisolatie

- Route: `/verduurzamen/isolatie/gevelisolatie/`
- Checked: 2026-09-13
- Workflow version: 2

## MUST coverage

| # | Requirement | Status | Where covered |
|---|---|---|---|
| 1 | Gevelopbouw, spouw, bestaande isolatie, conditie, vocht, afwerklagen en toekomstwerk eerst | COVERED | `Maak eerst een gevelroutekaart` |
| 2 | Vier routes: spouw, binnen, buiten, eerst onderzoek/herstel | COVERED | `Kies daarna één van vier routes` |
| 3 | Spouw is eerste te onderzoeken route wanneer technisch geschikt, niet op bouwjaar alleen | COVERED | Quick answer + routekaart + spouwsectie |
| 4 | Spouwgeschiktheid: breedte, vervuiling, gevelconditie, bestaande isolatie, afwerklagen | COVERED | `Een spouw is niet automatisch geschikt om te vullen` |
| 5 | Vocht/lekkage/scheuren/poreus metselwerk als stopvoorwaarden | COVERED | `Vocht en gevelschade krijgen voorrang op isolatie` + aside |
| 6 | Binnenisolatie: ruimteverlies, aansluitingen, dampremming en houten balkkoppen | COVERED | `Binnenisolatie vraagt een bouwfysische check` |
| 7 | Onbekende dampopbouw/balkkoppen = professionele beoordeling | COVERED | quick answer binnenisolatie + body text |
| 8 | Buitenisolatie: hoge prestatie + dikkere gevel + aansluitdetails | COVERED | `Buitenisolatie is een gevelproject` |
| 9 | Vergunningcheck vóór uiterlijk wijzigende buitenisolatie | COVERED | `Vergunning en natuur zijn echte pre-work gates` |
| 10 | Natuurbescherming/eDNA/provinciale route als pre-work gate | COVERED | vergunning/natuur sectie |
| 11 | Ventilatie blijft parallelle randvoorwaarde | COVERED | `Ventilatie verdwijnt niet doordat je de gevel isoleert` |
| 12 | Routegebonden isolatiewaarden correct begrensd | COVERED | `Vergelijk isolatiewaarde per route` |
| 13 | Kosten scoped rather than universal €/m² | COVERED | `Wat kost gevelisolatie in 2026?` |
| 14 | Gevelspecifieke offertematrix | COVERED | `Wat moet in een gevelisolatie-offerte staan?` |

**MUST covered: 14/14**  
**MUST partial: 0**  
**MUST missing: 0**

## Evidence gaps

No blocking evidence gaps.

Boundaries deliberately retained:

- bouwjaar is only an indicator of wall type, never proof of a cavity;
- circa 4 cm is not presented as an automatic suitability guarantee;
- moisture source, crack significance and timber condition are not diagnosed remotely;
- no universal vapour-control detail is prescribed without wall context;
- eDNA/nature route is explicitly current/province-dependent rather than a permanent universal procedure;
- `Rd 1.2`, `Rd 3.5` and `Rd 4.5` are presented as route-specific examples/advice, not one legal minimum for all walls;
- cost examples are tied to Milieu Centraal reference scopes;
- RVO meldcodes/conditions must be checked at decision time.

## Cannibalisation check

### `/verduurzamen/isolatie/`
PASS. Parent remains the whole-home priority map; this page starts only once the façade is the relevant building element.

### `/problemen-oplossen/vochtproblemen/`
PASS. This page uses moisture/leakage as a stop gate but routes unresolved diagnosis to the troubleshooting page.

### `/renovatie-plannen/renovatievergunning/`
PASS. Only façade-specific triggers are stated here; general permit logic remains on the permit page.

### `/renovatie-plannen/subsidies-renovatie/`
PASS. This page only establishes current wall categories/meldcode checks; general ISDE timing and combinations remain elsewhere.

### `/vakman-en-offertes/offertes-vergelijken/`
PASS. Generic comparison remains there; this page owns the façade-specific technical scope.

## Information gain check

Present:

- `gevelroutekaart`;
- four-route decision instead of a three-card method list;
- cavity suitability gate;
- moisture/façade-condition gate;
- explicit internal-wall timber beam/vapour gate;
- exterior detail matrix;
- permit + nature pre-work gate;
- route-specific thermal-performance framing;
- route-specific cost normalisation;
- façade-specific quotation matrix.

## GEO / extractability

Direct answers present for:

- spouw vs binnenzijde vs buitenzijde;
- whether a cavity is suitable;
- what to do first with moisture/façade damage;
- timber-beam risk with internal insulation;
- insulation values by route;
- permit requirement for exterior insulation;
- nature/eDNA check before cavity-related work;
- why prices differ;
- what belongs in a façade-insulation quote.

## Result

`PASS`

The rewritten page covers all 14 MUST requirements with no blocking overlap or unresolved central factual claim.
