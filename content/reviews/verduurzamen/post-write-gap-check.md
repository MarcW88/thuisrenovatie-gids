# Post-write gap check — `/verduurzamen/`

- Checked: 2026-09-13
- Decision: `DEEP_REWRITE`
- Workflow version: 2

## MUST coverage

| # | MUST | Status | Evidence in final page |
| --- | --- | --- | --- |
| 1 | Open met geen universele vaste volgorde | COVERED | Kicker, lead, quick answer en H2 `Er is geen universele verduurzamingsvolgorde` |
| 2 | Compacte nulmeting van woningstaat | COVERED | `Begin met een woning-nulmeting` met schil, glas/kozijnen, ventilatie, verwarming/afgifte, dak/stroom en gebreken/plannen |
| 3 | Blokkades vóór maatregelen expliciet | COVERED | Quick answer + startsituatie `Lekkage, vocht of technisch gebrek` |
| 4 | Isolatie/kierdichting en ventilatie gekoppeld | COVERED | H2 `Vier afhankelijkheden die je niet los moet inkopen` + route naar ventilatie |
| 5 | Verwarmingskeuze afhankelijk van warmtevraag/afgifte/woningplan | COVERED | Nulmeting + startsituaties cv-ketel/warmtepomp + afhankelijkhedenblok |
| 6 | Zonnepanelen afstemmen op dak en toekomstig stroomgebruik | COVERED | Nulmeting + startsituatie zonnepanelen + afhankelijkhedenblok |
| 7 | Natuurlijke renovatiemomenten introduceren | COVERED | Volledige tabel voor dak, kozijnen, vloer, aanbouw/keuken en cv-ketel |
| 8 | Alle child intents uniek routen | COVERED | Startsituatietabel + `Kies de juiste verdieping` met energie besparen, isolatie + subpages, glas, ventilatie, warmtepomp, cv en zonnepanelen |
| 9 | Grens met `energie-besparen` expliciet | COVERED | Startsituatie `Hoge energierekening, maar nog geen groot renovatieproject` + cardtekst `verbruik nu verlagen...` |
| 10 | Geen universele prijs/besparing/subsidie/ROI-rangorde | COVERED | Geen bedragen of rankings; subsidie/rendement alleen doorlink |

**MUST partial:** 0  
**MUST missing:** 0

## SHOULD coverage

| SHOULD | Status | Notes |
| --- | --- | --- |
| Buitenzonwering / zomercomfort | COVERED | Note-box met Milieu Centraal-context |
| No-regret gate vóór moeilijk omkeerbare aankoop | COVERED | Vierdelige `no-regret check` |
| Subsidie doorlinken, niet dupliceren | COVERED | CTA naar `/renovatie-plannen/subsidies-renovatie/` |
| Rendement/waarde doorlinken | COVERED | CTA naar `/renovatie-plannen/rendement-renovatie/` |
| Scenario cv-ketel onverwacht/einde levensduur | COVERED | Startsituatietabel + natuurlijke renovatiemomenten |

## Intent / cannibalisation check

### Hub vs `/verduurzamen/energie-besparen/`

**Improved / acceptable.**

De hub bezit nu routekeuze en afhankelijkheden tussen investeringen. `energie-besparen` wordt in de hub expliciet gepositioneerd voor verbruik nu verlagen wanneer nog geen groot renovatieproject loopt.

De child page zelf zal later nog moeten worden herschreven om zijn huidige overlap volledig weg te nemen, maar de hub dupliceert de oude 4-niveaus-structuur niet meer.

### Hub vs `/renovatie-plannen/renovatie-volgorde/`

**No blocking overlap.**

De hub geeft geen fysieke bouwvolgorde. Hij behandelt energie-/comfortafhankelijkheden en logische instapmomenten.

### Hub vs child measure pages

**No blocking overlap.**

De hub beantwoordt alleen routekeuze. Details over isolatiemethode, glasprestatie, ventilatiesysteem, warmtepomp, cv of zonnepanelen worden doorgestuurd.

## Information gain check

- `woning-nulmeting`: COVERED
- `volgende-blokkade-model`: COVERED
- `natuurlijke renovatiemomenten`: COVERED
- routekaart per startsituatie: COVERED
- `no-regret gate`: COVERED

## Factuality / freshness

- `fact-check.md`: PASS
- centrale bron: Milieu Centraal, actueel gecontroleerd 2026-09-13
- geen ongesourcete bedragen of universele performanceclaims

## Final gap decision

`PASS`

0 MUST missing, 0 MUST partial. Geen inhoudelijke blocker voor `PUBLISH_REVIEW`.
