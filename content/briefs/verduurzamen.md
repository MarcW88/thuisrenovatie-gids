# Content brief — Verduurzamen

- Route: `/verduurzamen/`
- Type: `HUB`
- Markt: Nederland
- Taal: Nederlands
- Workflow version: 2
- Status: `BRIEF_READY`
- Laatste broncheck: 2026-09-13
- Decision: `DEEP_REWRITE`

## Primaire gebruikersjob

Ik wil mijn woning verduurzamen maar weet niet **welke beslissing nu logisch is, welke afhankelijkheden eerst moeten worden opgelost en welke maatregelpagina bij mijn startsituatie hoort**.

## Ownership

Deze hub bezit de **routekeuze door het verduurzamingscluster**:

- huidige woningstaat vastleggen;
- blokkades vóór investeringen herkennen;
- afhankelijkheden tussen schil, ventilatie, verwarming en opwek begrijpen;
- natuurlijke renovatiemomenten benutten;
- gebruiker naar de juiste child page sturen.

De hub bezit **niet**:

- gedetailleerde isolatiemethode of bouwdeelkeuze → `/verduurzamen/isolatie/` en subpages;
- HR++ vs triple/vacuüm, U-waarden en ISDE voor glas → `/verduurzamen/dubbel-glas/`;
- ventilatiesysteemkeuze → `/verduurzamen/ventilatie/`;
- hybride/all-electric readiness en toestelkeuze → `/verduurzamen/warmtepomp/`;
- vervanging van bestaande cv in context van toekomstige warmte → `/verduurzamen/cv-ketel/`;
- zonnepaneeldimensionering en dak/omvormer/meterkast → `/verduurzamen/zonnepanelen/`;
- verbruik nu verlagen, instellingen en laagdrempelige besparingen → `/verduurzamen/energie-besparen/`;
- actuele subsidiebedragen → `/renovatie-plannen/subsidies-renovatie/`;
- financiële ROI / woningwaarde → `/renovatie-plannen/rendement-renovatie/`.

## Zoekintentie

Breed informatief/commercieel oriënterend:

- woning verduurzamen
- huis verduurzamen
- waar beginnen met verduurzamen
- welke verduurzamingsmaatregel eerst
- verduurzamen volgorde
- stappenplan woning verduurzamen

De SERP wordt gedomineerd door stappenplannen. De sterkste onafhankelijke bron, Milieu Centraal, zegt juist expliciet dat de volgorde **niet vaststaat** en dat logische renovatiemomenten een geldig instappunt zijn.

## Centrale thesis

Er is geen universele verduurzamingsvolgorde. Kies de volgende stap op basis van **de huidige staat van de woning, blokkades die eerst opgelost moeten worden, afhankelijkheden met andere maatregelen en het eerstvolgende natuurlijke renovatiemoment**.

## MUST-cover

1. Open expliciet met: geen universele vaste volgorde.
2. Laat gebruiker eerst een compacte nulmeting maken van schil, glas, ventilatie, verwarming/afgifte, dak/opwek, gebreken en toekomstige plannen.
3. Introduceer `blokkades vóór maatregelen`: lekkage, vocht, constructieve/onderhoudsproblemen of onbekende opbouw eerst voldoende begrijpen/oplossen.
4. Behandel isolatie/kierdichting en ventilatie als gekoppelde beslissingen.
5. Leg uit dat verwarmingskeuze afhankelijk is van warmtevraag, afgifte en toekomstig woningplan; routeer naar warmtepomp/cv-ketel.
6. Leg uit dat zonnepanelen worden afgestemd op dakconditie en toekomstig stroomgebruik.
7. Introduceer `natuurlijke renovatiemomenten` als geldige startpunten: dak, kozijnen, vloer, aanbouw/keuken, cv-ketel.
8. Routeer alle child intents met een unieke vraag en duidelijke ownership.
9. Maak de grens met `/verduurzamen/energie-besparen/` expliciet: hub = investeringsroute; child = verbruik nu verlagen / prioriteren zonder compleet renovatieproject.
10. Geen universele prijs-, besparings-, subsidie- of ROI-rangorde.

## SHOULD-cover

- buitenzonwering en zomercomfort als cross-cutting onderdeel van woningprestatie;
- `no-regret gate` vóór moeilijk omkeerbare aankoop;
- actuele subsidie-informatie doorlinken, niet dupliceren;
- rendement/waarde doorlinken naar de aparte pagina;
- expliciet scenario voor cv-ketel die onverwacht aan vervanging toe is.

## Information gain assets

### 1. Volgende-blokkade-model

Gebruik vier vragen:

1. Wat is aantoonbaar zwak, defect of oncomfortabel?
2. Welke keuze verandert de maatvoering/scope van andere maatregelen?
3. Wat wordt binnenkort toch opengebroken of vervangen?
4. Welke aankoop is later duur om opnieuw te doen?

### 2. Woning-nulmeting

Minimaal vastleggen:

- dak, gevel, vloer en glas: wat is bekend over isolatie/conditie?
- ventilatie: natuurlijke toevoer, roosters, mechanische afvoer of ander systeem?
- verwarming: bron, leeftijd/conditie, afgiftesysteem;
- dak: conditie, schaduw, geplande dakwerken;
- bekende vocht-, lekkage- of onderhoudsproblemen;
- geplande keuken, aanbouw, vloer, kozijnen of andere renovaties;
- verwacht toekomstig stroomgebruik: warmtepomp, EV, koken, thuiswerken etc.

### 3. Natuurlijke renovatiemomenten

Voorbeelden:

- dakwerk → dakisolatie en zonnepaneelplan samen bekijken;
- kozijnen → glas, kierdichting, ventilatie en gevelaansluiting samen bekijken;
- vloer open → vloerisolatie en toekomstige warmteafgifte meenemen;
- cv-ketel einde levensduur → warmteplan versnellen;
- aanbouw/keuken → installaties, ventilatie en toekomstige warmtevraag meenemen.

### 4. Routekaart per startsituatie

| Startsituatie | Eigenaar van volgende vraag |
| --- | --- |
| Hoge rekening / nog geen groot project | `/verduurzamen/energie-besparen/` |
| Onbekende of zwakke schil | `/verduurzamen/isolatie/` |
| Specifiek dak/vloer/gevel | betreffende isolatie-subpage |
| Oud glas / glassoort kiezen | `/verduurzamen/dubbel-glas/` |
| Benauwd, vochtige lucht of woning wordt luchtdichter | `/verduurzamen/ventilatie/` |
| Warmtepomp overwegen | `/verduurzamen/warmtepomp/` |
| Bestaande cv moet worden vervangen | `/verduurzamen/cv-ketel/` |
| Dak geschikt en toekomstige stroomvraag bekend | `/verduurzamen/zonnepanelen/` |

### 5. No-regret gate

Voor warmtepomp, complete kozijnvervanging, grote isolatie-ingreep of zonnepanelen:

- zijn de technische afhankelijkheden die scope/dimensionering veranderen voldoende bekend?
- is binnenkort een onderhouds- of renovatiemoment dat de keuze verandert?
- wordt ventilatie/comfort niet verslechterd?
- is de maatregel verenigbaar met het volgende geplande project?

## Fact sources

### Milieu Centraal — Stappenplan voor een energiezuinig huis

Gecontroleerd 13 september 2026.

https://www.milieucentraal.nl/energie-besparen/energiezuinig-wonen/stappenplan-voor-een-energiezuinig-huis/

Te gebruiken voor:

- volgorde staat niet vast;
- instappen op logisch renovatiemoment;
- isolatie + ventilatie + buitenzonwering als basis;
- Verbetercheck als woningafhankelijke route.

### Current SERP — augustus/september 2026

VerduurzaamOnline, GOG GROUP, Voltafy en Wil Ik Hier Wonen gebruiken grotendeels lineaire stappenplannen. Gebruik dit alleen als concurrentiecontext, niet als primaire fact source.

## Internal links

Primair:

- `/verduurzamen/energie-besparen/`
- `/verduurzamen/isolatie/`
- `/verduurzamen/isolatie/dakisolatie/`
- `/verduurzamen/isolatie/vloerisolatie/`
- `/verduurzamen/isolatie/gevelisolatie/`
- `/verduurzamen/dubbel-glas/`
- `/verduurzamen/ventilatie/`
- `/verduurzamen/warmtepomp/`
- `/verduurzamen/cv-ketel/`
- `/verduurzamen/zonnepanelen/`

Cross-cluster:

- `/renovatie-plannen/subsidies-renovatie/`
- `/renovatie-plannen/rendement-renovatie/`
- `/renovatieprojecten/ramen-en-glas/` wanneer het kozijn-/raamproject de primaire taak is.

## Anti-patterns

- geen vaste universele `1 isoleren → 2 ventileren → 3 warmtepomp → 4 zonnepanelen`-regel;
- geen tweede inhoudelijke versie van elke child page;
- geen generieke `top 5 beste maatregelen`;
- geen subsidie als technische startbeslissing;
- geen ROI-/besparingsbedragen zonder woningcontext;
- geen product-first CTA vóór de routekeuze;
- geen overlap waarbij `energie-besparen` opnieuw dezelfde clusterkaart wordt.

## GEO / extractable answers

De pagina moet zelfstandig beantwoordbare blokken bevatten voor:

- Waar begin je met je woning verduurzamen?
- Is er een vaste volgorde voor verduurzamen?
- Welke problemen moet je eerst oplossen vóór isoleren of installaties?
- Wanneer is een renovatiemoment slim om verduurzaming mee te nemen?
- Wat moet je weten vóór een warmtepomp of zonnepanelen?
- Welke pagina past bij mijn startsituatie?

## Publish success criteria

`PUBLISH_REVIEW` mag alleen PASS zijn als:

- alle MUST-items zijn afgedekt;
- de pagina geen vaste universele volgorde meer oplegt;
- alle child intents uniek worden gerouteerd;
- de overlap met `energie-besparen` aantoonbaar is verkleind;
- geen ongesourcete universele bedragen/ROI staan;
- generated HTML canonical correct houdt en `noindex,follow` behouden blijft.
