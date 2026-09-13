# SERP coverage — Warmtepomp

- Route: `/verduurzamen/warmtepomp/`
- Markt: Nederland
- Onderzocht: 2026-09-13
- Workflow: v2

## Intentbeeld

De actuele Nederlandse zoekresultaten voor `warmtepomp`, `hybride warmtepomp`, `volledig elektrische warmtepomp`, `is mijn huis geschikt voor warmtepomp`, `warmtepomp radiatoren`, `warmtepomp kosten 2026` en `warmtepomp subsidie 2026` mengen vier intents:

1. systeemtype kiezen;
2. woninggeschiktheid;
3. kosten/subsidie;
4. installateur/offerte.

Veel commerciële pagina's springen snel van bouwjaar of isolatielabel naar een toesteltype. De onafhankelijke bronnen leggen juist nadruk op de combinatie van isolatie, lage-temperatuurafgifte, ruimte, geluid en installatievoorwaarden.

## Current evidence

### Milieu Centraal — volledig elektrische warmtepomp

Gecontroleerd 13 september 2026; pagina laatst gewijzigd 1 september 2026.

Belangrijk:

- all-electric vraagt minimaal een redelijk tot goed geïsoleerde woning;
- voldoende warmteafgifte bij lagere watertemperatuur is noodzakelijk;
- vloer-/wandverwarming of voldoende grote radiatoren/convectoren kunnen passen;
- warm tapwater vraagt voorraadvat/binnenruimte;
- gemeentelijke plannen voor warmtenet/aardgasvrij moeten vóór investering worden gecontroleerd;
- de Verwarmingstest is een praktische readiness-check.

### Milieu Centraal — Verwarmingstest

Gecontroleerd 13 september 2026.

Belangrijk:

- cv-ketel tijdelijk op 50 °C zetten en comfort volgen;
- blijft de woning comfortabel, dan is lage-temperatuurverwarming technisch kansrijk;
- lukt dat niet, dan eerst isolatie en/of afgifte verbeteren;
- de test vervangt geen project-specifieke warmteverliesberekening of systeemdimensionering.

### Milieu Centraal — warmtepomp / typen

Gecontroleerd 13 september 2026.

Belangrijk:

- hybride werkt samen met cv-ketel en kan bij minder vergaand geïsoleerde woningen passen;
- all-electric verzorgt ruimteverwarming en tapwater en vraagt verdergaande geschiktheid;
- buitenunits vragen geluids- en plaatsingscontrole;
- de wettelijke geluidsgrens gaat over geluid op de erfgrens, niet over één universele minimale afstand;
- natuurlijke koudemiddelen zijn een relevant selectiecriterium.

### RVO — ISDE meldcodelijst warmtepompen

Inhoud gecontroleerd 10 september 2026.

Belangrijk:

- actuele meldcodes en subsidiebedragen zijn apparaatspecifiek;
- de lijst bevat duizenden modellen in verschillende categorieën;
- een toestel buiten de lijst kan alleen onder voorwaarden met technische documentatie worden beoordeeld;
- geen generiek subsidiebedrag op de pagina zetten alsof dat voor ieder toestel geldt.

### Rijksoverheid — vervallen normering verwarmingsinstallaties in 2026

Rijksoverheid bevestigt dat het kabinet heeft afgezien van de voorgenomen normering van verwarmingsinstallaties per 2026. De oude boodschap dat bij cv-ketelvervanging vanaf 2026 minimaal een hybride warmtepomp algemeen verplicht zou zijn, mag dus niet als huidige regel worden gepresenteerd.

## SERP gaps / information gain

| Onderwerp | SERP vaak | V2-aanpak |
|---|---|---|
| Geschiktheid | bouwjaar/label als shortcut | huidige woningstaat + 50 °C-test + afgifte + warmtebehoefte |
| Hybride vs all-electric | generiek tweeluik | vier routes incl. eerst verbeteren / eerst onderzoeken |
| Radiatoren | “kan wel/niet” | capaciteit bij ontwerptemperatuur per kritische ruimte |
| Vermogen | toestel-kW centraal | dimensioneringsbasis vóór toestelvermogen |
| Tapwater | secundair | expliciete voorraadvat-/ruimtebeslissing |
| Geluid | losse dB of afstand | plaatsingsgate + erfgrens + trillingen |
| Elektra | automatisch verzwaren | eerst systeem- en aansluitingscheck |
| Gemeente | vaak ontbrekend | warmteplan/warmtenet als no-regret gate |
| Subsidie | bedrag als verkooptrigger | meldcode/voorwaarden pas na technische route |
| Offerte | toestel + montage | genormaliseerde systeemscope + commissioning |

## Ownership / anti-cannibalisatie

`/verduurzamen/warmtepomp/` bezit woninggereedheid, hybride/all-electric-route en warmtepompspecifieke offerte-scope.

Niet dupliceren:

- `/verduurzamen/isolatie/`: welke schilmaatregel eerst;
- `/verduurzamen/ventilatie/`: luchtstrategie;
- `/verduurzamen/cv-ketel/`: bredere vervangingsbeslissing cv/hybride/all-electric;
- `/renovatie-plannen/subsidies-renovatie/`: volledige ISDE-uitleg.

## Recommended page model

### Asset 1 — Warmtepomp-gereedheidsdossier

Zelfde invoer voor iedere installateur: schil, 50 °C-test, afgifte, warmtebehoefte, tapwater, ruimte, buitenunit, elektra, gemeentelijk plan.

### Asset 2 — Vier routes

- hybride nu;
- volledig elektrisch nu;
- eerst woning/afgifte verbeteren;
- eerst verder onderzoeken.

### Asset 3 — Pre-order gate

Geen definitieve toestelkeuze zonder duidelijkheid over ontwerpvermogen, ontwerp-aanvoertemperatuur, geluid/plaatsing, tapwater, elektra en warmteplan.

### Asset 4 — Offertenormalisatie

Vergelijk installateurs op dezelfde ontwerpuitgangspunten, niet op kale toestelprijs.

## Cost boundary

Geen universele projectprijs of terugverdientijd. Systeemtype, vermogen, bron, afgifte-aanpassingen, tapwater, elektra en bouwkundige werkzaamheden veranderen de scope te sterk.

## Decision

`DEEP_REWRITE`.

De bestaande pagina heeft de juiste ingrediënten, maar mist bewijsgerichte readiness, routekeuze, pre-order gates en een offertepakket dat prijsvergelijking technisch betrouwbaar maakt.
