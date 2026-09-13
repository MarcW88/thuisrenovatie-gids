# Post-write gap check — Warmtepomp

- Route: `/verduurzamen/warmtepomp/`
- Reviewed: 2026-09-13
- Workflow version: 2

## MUST coverage

1. **PASS** — isolatie, afgifte, warmtevraag, tapwater, ruimte, buitenunit/geluid en elektriciteit staan vóór toestelkeuze.
2. **PASS** — hybride en volledig elektrisch zijn duidelijk onderscheiden zonder universele winnaar.
3. **PASS** — 50 °C Verwarmingstest is opgenomen en begrensd als praktische test, niet als volledige berekening.
4. **PASS** — all-electric vraagt minimaal redelijk tot goed geïsoleerd + voldoende lage-temperatuurafgifte.
5. **PASS** — hybride kan eerder passen; lagere warmtevraag verbetert de context.
6. **PASS** — bouwjaar is slechts aanwijzing; huidige woningstaat is leidend.
7. **PASS** — capaciteit van radiatoren/convectoren/vloerverwarming wordt per kritische ruimte onderdeel van de route.
8. **PASS** — dimensioneringsbasis is verplicht; cv-ketelvermogen wordt niet gekopieerd.
9. **PASS** — tapwater, voorraadvat en binnenruimte zijn expliciete all-electric gates.
10. **PASS** — buitenunit, erfgrensgeluid en trillingen zijn pre-order gate; geen vaste afstandsclaim.
11. **PASS** — elektra wordt gecontroleerd zonder automatische netverzwaring.
12. **PASS** — gemeentelijk warmteplan/warmtenet is no-regret check vóór investering.
13. **PASS** — vervallen 2026-hybrideplicht wordt expliciet gecorrigeerd.
14. **PASS** — offertematrix bevat route, ontwerpvermogen, temperatuur, afgifte, tapwater, plaatsing/geluid, elektra, regeling/hydrauliek, oplevering, meldcode/garantie/uitsluitingen.

## Score

- MUST covered: **14/14**
- MUST partial: **0**
- MUST missing: **0**

## Intent / information gain

PASS.

De pagina verschuift van toestelkeuze naar bewijsbare woninggereedheid en maakt de technische input voor meerdere installateurs vergelijkbaar.

Distinctive assets:

- warmtepomp-gereedheidsdossier;
- vier routes;
- 50 °C-test met correcte grens;
- dimensioneringsgate;
- tapwater-/ruimtegate;
- buitenunit-/geluidgate;
- warmteplangate;
- warmtepompspecifieke offertematrix.

## Cannibalisation check

PASS.

- `/verduurzamen/warmtepomp/` = readiness + warmtepomproute + warmtepompofferte.
- `/verduurzamen/isolatie/` = woningbrede isolatieprioriteit.
- `/verduurzamen/ventilatie/` = ventilatiestrategie.
- `/verduurzamen/cv-ketel/` = ketelvervangingsbeslissing.
- `/renovatie-plannen/subsidies-renovatie/` = algemene subsidie-orchestratie.

## Risk / freshness check

PASS.

- geen universele kosten/besparing;
- geen oude wettelijke verplichting;
- subsidie alleen apparaatspecifiek en actueel;
- geluid correct als erfgrenstoets, niet afstandsregel;
- geen project-specifieke dimensionering op afstand.

## Result

**PASS — 14/14 MUST covered, 0 blocking gaps.**
