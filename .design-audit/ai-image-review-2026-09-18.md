# AI image review — 2026-09-18

## Conclusie

De huidige beeldworkflow maakt terecht onderscheid tussen lage en hogere waarheidsrisico's, maar laat nog toe dat FLUX informatieve infographics, schema's, matrices en flows genereert. Dat is niet betrouwbaar genoeg voor publicatie.

De betrokken prompts vragen meestal al expliciet om "no words" of "no letters". Het feit dat de uiteindelijke beelden toch Engelse labels, pseudo-tekst of betekenisloze tekens kunnen bevatten, is dus geen vertaalprobleem maar een outputcontroleprobleem.

Nieuwe regel:
- AI: alleen voor fotografische/contextuele beelden zonder functionele tekst.
- HTML/CSS/SVG: voor alle informatieve visuals met labels, stappen, categorieën, getallen of beslislogica.
- Alle functionele tekst in visuals: gecontroleerd Nederlands.
- Pseudo-tekst of onleesbare typografie = blocker.

## Bestaande gegenereerde beelden die als code-visual moeten worden vervangen

1. `energie-besparen-hierarchy.webp`
2. `fundering-proces.webp`
3. `funderingsproblemen-signalen.webp`
4. `offerte-controleren-checklist.webp`
5. `opstijgend-vocht-bronnen.webp`
6. `problemen-oplossen-diagnostic-flow.webp`
7. `rendement-renovatie-value-matrix.webp`
8. `renovatie-budget-reserve.webp`
9. `renovatie-plannen-roadmap.webp`
10. `renovatie-volgorde-visual.webp`
11. `renovatiefasen-roadmap.webp`
12. `renovatiekosten-cost-structure.webp`
13. `renovatievergunning-decision-flow.webp`
14. `subsidies-renovatie-aid-map.webp`
15. `ventilatie-luchtstroom.webp`
16. `verduurzamen-layers.webp`
17. `vocht-in-muren-bronnen.webp`
18. `warmtepomp-diy-veiligheidsgrenzen.webp`
19. `zelf-doen-of-uitbesteden-matrix.webp`
20. `zonnepanelen-diy-veiligheidsgrenzen.webp`

Deze visuals bevatten informatiestructuur die semantisch belangrijk is. Ze horen daarom niet uit een rastergenerator te komen.

## Gegenereerde contextbeelden die AI mogen blijven gebruiken

De onderstaande categorie kan AI-gegenereerd blijven, op voorwaarde van een visuele QA zonder leesbare pseudo-tekst, merken, onrealistische bouwdetails of typische generatieve artefacten:

- `aanbouw-context.webp`
- `aannemer-kiezen-context.webp`
- `badkamer-renovatie-context.webp`
- `complete-renovatie-context.webp`
- `cv-ketel-context.webp`
- `dakisolatie-context.webp`
- `dubbel-glas-context.webp`
- `gevelisolatie-context.webp`
- `huis-renoveren-startscan.webp`
- `isolatie-woning-context.webp`
- `keuken-renovatie-context.webp`
- `offertes-vergelijken-tafel.webp`
- `ramen-en-glas-context.webp`
- `traprenovatie-diy-context.webp`
- `vakman-kiezen-context.webp`
- `vloerisolatie-context.webp`
- `vochtproblemen-signaal.webp`
- `warmtepomp-woning-context.webp`
- `zonnepanelen-context.webp`

## Visuele QA voor contextbeelden

Afkeuren wanneer één van deze signalen zichtbaar is:
- leesbare of half-leesbare pseudo-tekst;
- Engelse labels die geen echte bron/merknaam zijn;
- onmogelijke leidingen, ramen, deuren, gereedschappen of handen;
- bouwdetails die technisch logisch lijken maar fysiek niet kloppen;
- overmatig perfecte symmetrie, zwevende objecten of repetitieve texturen;
- generieke "AI showroom"-look waar een gewone Nederlandse woning wordt bedoeld;
- te veel iconen, badges, pijlen of decoratieve informatie zonder functie;
- een visueel element dat de gebruiker als technische instructie zou kunnen interpreteren terwijl het alleen illustratief is.

## Richting voor vervanging

Code-visuals moeten dezelfde site-identiteit gebruiken: crème achtergrond, mineraalgroen, terracotta en warm antraciet. Gebruik korte Nederlandse labels, echte hiërarchie en veel witruimte. Geen extra decoratie wanneer die geen informatie draagt.

Voorbeelden:
- renovatievolgorde: genummerde stappen met echte Nederlandse labels;
- renovatiekosten: zes kostencategorieën rond één woning, geen verzonnen verhoudingen;
- vergunningen: neutrale beslisflow met labels als `Controleren`, `Melding`, `Vergunning`, zonder een juridisch resultaat te claimen;
- ventilatie: kamers benoemen in HTML/SVG en pijlen als SVG/CSS, zodat de tekst altijd correct blijft.
