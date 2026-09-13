# SERP coverage — Aanbouw

- Route: `/renovatieprojecten/aanbouw/`
- Markt: Nederland
- Datum onderzoek: 2026-09-13
- Workflow version: 2
- Voorlopige auditbeslissing: `DEEP_REWRITE`

## 1. Query set en subintenties

Primair:
- aanbouw
- aanbouw woning
- uitbouw woning

Commercieel / prijs:
- aanbouw kosten 2026
- uitbouw kosten 2026
- aanbouw kosten per m2
- aanbouw offerte

Haalbaarheid / regels:
- aanbouw vergunning
- uitbouw vergunning
- aanbouw fundering
- aanbouw daglicht
- aanbouw constructie geveldoorbraak

## 2. Actueel geïnspecteerde SERP

### `aanbouw kosten 2026`

- Vereniging Eigen Huis — `Wat kost verbouwen?`, prijspeil 2026. Sterke bron door concrete casco-ranges per formaat plus expliciete uitsluitingen en losse opties.
- Werkspot — `Kosten voor het plaatsen van een aanbouw`, bijgewerkt 21-08-2026. Sterke commerciële prijsintentie met prefab/casco/maatwerk-ranges.
- Heidstra Bouw — `Wat kost een aanbouw in 2026?`, bijgewerkt 04-09-2026. Bouwbedrijf met m²-ranges en praktijkuitleg.
- Homedeal — `Aanbouw of uitbouw`, 2026-ranges en formaatvoorbeelden.
- Hollands Prefab — `Wat kost een aanbouw in 2026?`, bijgewerkt 02-07-2026. Transparante eigen prefab-prijzen, maar productspecifiek.

### `aanbouw vergunning`

- Omgevingsloket — Vergunningcheck; `Aanbouw of schuur plaatsen` is een expliciete werkzaamheid.
- Rijksoverheid — `Vergunningvrij bouwen en verbouwen`: vergunningvrij betekent niet regelvrij; Bbl en burenrecht blijven relevant en andere vergunningen kunnen spelen.
- Rijksoverheid — `Stappenplan bij bouwen en verbouwen`: omgevingsplan, welstand, bouwvoorschriften, vergunningcheck en buren.

### Technische / bouwkundige intent

- IPLO — `Verbouwen van een bouwwerk: dit houdt het in`: bij een aanbouw verandert de uitwendige scheidingsconstructie. Voor geluidwering en daglichttoetreding geldt in beginsel minimaal het rechtens verkregen niveau van de weggehaalde gevel; voor onder meer Rc/U-waarde gelden specifieke verbouweisen waarbij nieuwbouwwaarden kunnen gelden.
- IPLO — daglichtregels nieuwbouw/bestaande bouw: daglicht is een expliciet Bbl-onderwerp; ramen, lichtkoepels en geometrie bepalen de equivalente daglichtoppervlakte.

## 3. Dominant SERP-format

Hybride commercieel-informatieve gidsen:
- prijsranges vroeg op de pagina;
- stappenplan / planning;
- vergunning als vaste sectie;
- prefab vs traditioneel;
- offerte-CTA.

De meeste resultaten starten vanuit `hoeveel m² / hoeveel kost het?`. Ze behandelen constructie, fundering, daglicht en vergunning vaak als losse kosten- of checklistitems, niet als voorwaarden die het ontwerp eerst moeten begrenzen.

## 4. Gebruikersbehoeften

De lezer moet kunnen beslissen:
1. welke functie de extra ruimte krijgt;
2. hoe groot/diep de aanbouw logisch kan zijn zonder het bestaande huis functioneel te verslechteren;
3. welke constructieve en funderingsonzekerheden vóór een vaste prijs moeten worden opgelost;
4. hoe daglicht van de bestaande ruimte verandert wanneer de achtergevel opschuift;
5. welke installaties en comfortkeuzes mee moeten worden ontworpen;
6. welke regels voor de concrete locatie gelden;
7. welke scope bij een prijsbenchmark hoort;
8. wanneer een ontwerp werkelijk `offerteklaar` is.

## 5. Coverage matrix

| Behoefte | Huidige pagina | Prioriteit | Opmerking |
|---|---|---|---|
| Doel en gebruik vóór maatvoering | COVERED | MUST | Goede basis behouden. |
| Constructieve impact geveldoorbraak | PARTIAL | MUST | Nu te algemeen; moet expliciet ontwerp-input vóór offerte worden. |
| Fundering afhankelijk van belasting/bodem/bestaand gebouw | COVERED | MUST | Behouden, maar koppelen aan haalbaarheidsgate. |
| Daglicht bestaand + nieuw deel | PARTIAL | MUST | Nu comfortclaim; Bbl/IPLO maakt dit explicieter en belangrijker. |
| Isolatie/verwarming/ventilatie integraal | PARTIAL | MUST | Nu genoemd maar niet als interface. |
| Vergunningcheck locatie/projectspecifiek | COVERED | MUST | Versterken met `vergunningvrij ≠ regelvrij`. |
| Actuele prijsbenchmark 2026 met scope | MISSING | MUST | VEH heeft sterke casco-ranges + uitsluitingen. |
| Casco vs afgebouwd / scope-normalisatie | MISSING | MUST | Nodig om SERP-prijzen vergelijkbaar te maken. |
| Offerte-ready gate | PARTIAL | MUST | Nu CTA, geen expliciete voorwaarden voor een betrouwbare prijs. |
| Buren / erfgrens / uitvoeringstoegang | MISSING | SHOULD | Rijksoverheid noemt buren; praktisch relevant. Geen juridisch advies. |
| Prefab vs traditioneel | MISSING | SHOULD | SERP veel aanwezig, maar alleen als keuze-impact; geen generiek winnaar. |
| Universele bouwduur | MISSING | OPTIONAL | Niet toevoegen zonder voldoende scope. |

## 6. Information gain

### A. `Haalbaarheidsgate` vóór ontwerpfixatie

Een aanbouw gaat pas door naar definitief ontwerp/offerte wanneer vijf interfaces voldoende duidelijk zijn:
- opening / draagconstructie;
- funderingsprincipe en bodemrisico;
- daglichtimpact;
- installaties + thermische schil;
- regels / Vergunningcheck.

### B. `Bestaande woning-test`

Niet alleen vragen wat de nieuwe ruimte oplevert, maar wat de aanbouw met het bestaande deel doet:
- wordt de oude woonkamer/keuken dieper en donkerder?
- verdwijnen radiatorposities, ventilatieroutes of gevelvoorzieningen?
- veranderen vloerhoogte en drempels?
- blijft de bestaande indeling logisch?

### C. `Casco is geen totaalprijs`

Gebruik VEH 2026 als benchmark met zichtbare uitsluitingen:
- casco stenen aanbouw;
- exclusief doorbraak, afwerking, installaties en inrichting;
- losse opties apart tonen.

Daarmee voorkomen we dat een casco-benchmark als complete aanbouwprijs wordt gelezen.

### D. `Offerteklaar ontwerp`

Een ontwerp is pas offertewaardig als verschillende aannemers dezelfde constructieve uitgangspunten, funderingsscope, schil, installaties, afwerking, sloop/herstel en verantwoordelijkheid kunnen prijzen.

## 7. GEO / citation opportunities

Extractable facts / distinctions:
- Vergunningvrij bouwen betekent niet regelvrij bouwen; Bbl en burenrecht blijven gelden en andere toestemmingen kunnen relevant zijn. Bron: Rijksoverheid.
- De Vergunningcheck kan uitkomen op vergunning, melding, informatieplicht of geen indieningsplicht voor de gekozen activiteit. Bron: Omgevingsloket.
- Bij een aanbouw verandert de bestaande uitwendige scheidingsconstructie; IPLO beschrijft specifieke verbouwregels voor onder andere daglicht en thermische prestaties.
- VEH prijspeil 2026 voor casco stenen aanbouw: 10 m² €21.750–€27.550; 12 m² €23.900–€29.950; 15 m² €33.850–€43.325; 20 m² €39.900–€48.300, incl. btw, exclusief doorbraak, afwerking, installaties en inrichting.
- VEH losse opties 2026: heipalen per 2 €1.850; geveldoorbraak €3.600; stucwerk €1.225; elektra €675; centrale verwarming €1.230; aftimmerwerk €395.

## 8. Interne ownership / cannibalisatie

- `/renovatieprojecten/aanbouw/` owns: voorbereiding en chiffrage van één concreet uitbreidingsproject.
- `/renovatie-plannen/renovatievergunning/` owns: uitleg van het vergunningstelsel en procedurele regels in brede zin.
- `/renovatie-plannen/renovatiekosten/` owns: brede marktbenchmark tussen renovatietypen.
- `/renovatie-plannen/complete-renovatie/` owns: coördinatie wanneer de aanbouw onderdeel wordt van een woningbrede renovatie.
- `/renovatieprojecten/fundering/` owns: funderingsherstel; hier alleen fundering als ontwerpinput van een nieuwe aanbouw.
- `/verduurzamen/...` owns: detailkeuzes rond isolatie/verwarming/ventilatie.

## 9. Data gaps

- Geen betrouwbare universele bouwduur voor alle aanbouwen. Niet publiceren als vaste weekrange.
- Geen universele vergunningvrij-regel publiceren; altijd locatie + werkzaamheden via Omgevingsloket.
- Geen generieke funderingsmethode voorschrijven zonder bodem/constructiegegevens.
- Geen exacte daglichtberekening of grenswaarde als projectadvies geven; wel uitleggen dat daglicht expliciet moet worden meegetoetst.

## 10. Beslissing

`DEEP_REWRITE`

Reden: de huidige pagina heeft een goede dependency-first basis, maar mist een actuele scoped prijsbenchmark, een expliciete haalbaarheidsgate en een sterk genoeg onderscheid tussen een aantrekkelijk ontwerp en een technisch/reglementair offertewaardig ontwerp. De rewrite moet informatie toevoegen, niet alleen verlengen.