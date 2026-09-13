# SERP coverage — Ventilatie

- Route: `/verduurzamen/ventilatie/`
- Market: Nederland
- Checked: 2026-09-13
- Decision: `DEEP_REWRITE`

## Ownership decision

Deze pagina bezit de **ventilatiestrategie in een bestaande woning en bij renovatie**: bestaand systeem herkennen, toevoer + doorstroming + afvoer als keten ontwerpen, systeemroute kiezen, afstemmen op luchtdichtheid/kozijnen en offertes op dezelfde functionele scope vergelijken.

De pagina bezit niet:

- woningbrede isolatieprioritering → `/verduurzamen/isolatie/`;
- glassoort/U-waarde → `/verduurzamen/dubbel-glas/`;
- kozijnvervangingsproject → `/renovatieprojecten/ramen-en-glas/`;
- algemene vochtdiagnose → `/problemen-oplossen/vochtproblemen/`;
- algemene ISDE-orchestratie → `/renovatie-plannen/subsidies-renovatie/`.

## Queries / sub-intents inspected

- ventilatie huis verbeteren
- ventilatie na isoleren
- mechanische ventilatie verbeteren
- mechanische ventilatie vervangen
- balansventilatie bestaande woning
- decentrale balansventilatie wtw
- ventilatieroosters nieuwe kozijnen
- ventilatie subsidie 2026

## Current SERP pattern

### Milieu Centraal — Ventilatie in huis / woning ventileren
Strong on:
- drie hoofdvormen: natuurlijk, mechanische afvoer, balansventilatie;
- continu ventileren; systeem niet normaal uitzetten;
- mechanische afvoer heeft bewuste toevoer nodig via roosters/klepramen;
- onderhoud van roosters, ventielen en filters;
- isolatie/luchtdichtheid maakt bewuste ventilatie belangrijker.

### Milieu Centraal — Mechanische ventilatie
Strong on:
- afvoer in keuken, badkamer en toilet;
- toevoer via gevel-/raamroosters;
- winddrukgeregelde roosters en CO2-sturing als verbeteropties;
- bestaand huis zonder centraal systeem: volledige mechanische aanleg kan ingrijpend zijn;
- lokale WTW kan in bestaande woning een alternatief zijn.

### Milieu Centraal — Balansventilatie
Strong on:
- centrale versus lokale/decentrale balansventilatie;
- centrale variant vraagt in bestaande woning vaak een grotere verbouwing wegens kanalen;
- lokale units kunnen goed in bestaande woningen;
- bij balansventilatie zijn ventilatieroosters in ramen niet nodig en kunnen ze het ontwerp/rendement verstoren;
- filters, onderhoud en zomerbypass;
- ISDE sinds 2026 wanneer gecombineerd met isolatie.

### Rijksoverheid — Hoe kan ik mijn huis ventileren?
Strong on:
- dag en nacht voldoende ventileren;
- alleen kort luchten is geen vervanging voor ventileren;
- goed geïsoleerde woningen vragen extra aandacht voor ventilatie;
- vocht en vervuilde lucht als redenen voor ventilatie.

### RVO — ISDE 2026 / meldcodelijst ventilatie-units
Current facts:
- ventilatie kan in 2026 binnen ISDE vallen wanneer gecombineerd met één of meer isolatiemaatregelen en overige voorwaarden;
- huidig bedrag: eenmalig €400;
- meldcodelijst bevat centrale CO2-gestuurde mechanische ventilatie, centrale balansventilatie WTW en decentrale balansventilatie WTW;
- meldcodes en producttechniek vóór opdracht controleren.

### Vereniging Eigen Huis
Strong on:
- bestaande systeem verbeteren op basis van huidige situatie;
- vraagsturing met CO2/vocht;
- kozijnvervanging als logisch moment om toevoerroosters mee te nemen bij mechanische afvoer;
- centrale nieuwe kanaalaanleg kan ingrijpend zijn.

### Commercial SERP pattern
Recurring:
- systeem A/B/C/D-overzichten;
- losse productprijzen;
- WTW als premium oplossing;
- generieke `beste ventilatiesysteem`-claims;
- leadform zonder luchtstroomontwerp.

Problem: prijzen en adviezen zijn moeilijk vergelijkbaar wanneer onduidelijk is welke kamers bediend worden, of kanalen al bestaan, hoeveel bouwkundig werk nodig is en of toevoer/doorstroming is meegenomen.

## Reader needs

1. Herkennen welk systeem er nu is.
2. Begrijpen dat ventilatie uit toevoer, doorstroming en afvoer bestaat.
3. Weten wat verandert na isolatie of nieuwe kozijnen.
4. Beslissen of het bestaande systeem vooral onderhoud/optimalisatie nodig heeft of een andere systeemroute.
5. Mechanische afvoer niet verwarren met balansventilatie.
6. Centrale versus decentrale WTW kunnen plaatsen in renovatiecontext.
7. Vocht-/condenssignalen niet automatisch verkeerd diagnosticeren.
8. Subsidie pas na technische route gebruiken.
9. Offertes op dezelfde kamers, kanalen, regeling, geluid en afwerking vergelijken.

## Coverage matrix

| Need | Current page | Strong SERP | Priority |
|---|---|---|---|
| Bestaand systeem herkennen | PARTIAL | COVERED | MUST |
| Toevoer + doorstroming + afvoer als keten | PARTIAL | PARTIAL | MUST |
| Luchten ≠ ventileren | MISSING | COVERED | MUST |
| Mechanische afvoer heeft bewuste toevoer nodig | PARTIAL | COVERED | MUST |
| Kozijnen/glasisolatie koppeling | PARTIAL | COVERED | MUST |
| Systeemafhankelijk oordeel over raamroosters | MISSING | BEST-ONLY | MUST |
| Bestaand systeem eerst optimaliseren | MISSING | COVERED | MUST |
| Vraaggestuurde mechanische afvoer | PARTIAL | COVERED | MUST |
| Decentrale balansventilatie | MISSING | COVERED | MUST |
| Centrale balansventilatie renovatie-impact | MISSING | COVERED | MUST |
| Doorstroom tussen kamers | MISSING | COVERED | MUST |
| Geluid/onderhoud/filtertoegang | MISSING | COVERED | MUST |
| Inregeling / oplevercheck | MISSING | PARTIAL | MUST |
| Veilige vochtgrens | PARTIAL | COVERED | MUST |
| Actuele ISDE 2026 | COVERED | COVERED | MUST |
| Offerte normaliseren op functionele scope | PARTIAL | RARE | MUST |

## Information gain

### 1. `Luchtstroomkaart`
Per ruimte/zone:
- functie;
- toevoerbron;
- doorstroomroute;
- afvoerpunt;
- bestaand rooster/ventiel;
- renovatie-effect;
- klacht/signaal;
- gewenste functie na renovatie.

### 2. Vier routes in plaats van één systeemranking
- bestaand systeem herstellen/optimaliseren;
- vraaggestuurde mechanische afvoer;
- decentrale/lokale balansventilatie;
- centrale balansventilatie wanneer renovatiemoment en kanaalruimte dat dragen.

### 3. `Kozijn- en isolatiegate`
Voor bestelling van kozijnen/glas of afronding van isolatiescope:
- toevoerstrategie vast;
- raamroosters wel/niet nodig op basis van systeemtype;
- afvoer in natte ruimtes geborgd;
- doorstroom geborgd;
- unit/kanalen/geveldoorvoeren afgestemd.

### 4. Offertenormalisatie
Geen vergelijking op alleen `ventilatie-unit + montage`.
Normaliseer op:
- bediende ruimtes;
- toevoer/afvoer/doorstroom;
- kanaalwerk/geveldoorvoeren;
- unit/box;
- sensoren/regeling;
- geluid;
- elektra/condensafvoer;
- inregeling;
- onderhoudstoegang;
- bouwkundige afwerking;
- garantie/subsidiebewijs.

## Cannibalisation / handoff

### `/verduurzamen/isolatie/`
Owns welke schilmaatregel eerst. Ventilatiepagina neemt de luchtstrategie over zodra luchtdichtheid verandert.

### `/verduurzamen/dubbel-glas/`
Owns HR++/triple/vacuüm en U-waarde. Ventilatiepagina bepaalt toevoer na de glas-/kozijningreep.

### `/renovatieprojecten/ramen-en-glas/`
Owns gevelopeningen, maatvoering, montage en vervangingsscope. Ventilatiepagina levert de systeemkeuze die vóór bestelling moet vaststaan.

### `/problemen-oplossen/vochtproblemen/`
Owns diagnose van condensatie/lekkage/infiltratie/bouwkundige vochtbronnen. Ventilatiepagina mag alleen signaleren dat onvoldoende luchtverversing een factor kan zijn.

## Data gaps / claim boundaries

- Geen universele `beste ventilatiesysteem`-keuze zonder woning- en renovatiecontext.
- Geen universele kostenrange: centrale WTW, lokale WTW en box/sensor-upgrades hebben fundamenteel andere scopes.
- Geen vaste CO2-diagnosegrens zonder norm-/gebruikerscontext.
- Geen claim dat ventilatie alle vochtproblemen oplost.
- Geen standaard advies voor raamroosters: dat hangt af van mechanische afvoer versus balansventilatie.
- Subsidievoorwaarden/meldcodes blijven tijdgebonden en moeten bij RVO worden gecontroleerd.

## Research gate

PASS for drafting.

De centrale systeem-, renovatie-, gezondheids- en subsidieclaims hebben actuele bronnen. Kosten worden bewust als scopeprobleem behandeld in plaats van met één kunstmatig gemiddelde.
