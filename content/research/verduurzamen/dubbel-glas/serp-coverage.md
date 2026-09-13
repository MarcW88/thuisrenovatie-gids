# SERP coverage — Dubbel glas

- Route: `/verduurzamen/dubbel-glas/`
- Market: Nederland
- Checked: 2026-09-13
- Decision: `DEEP_REWRITE`

## Ownership decision

Deze verduurzamingspagina bezit de **glas- en energieprestatiebeslissing**: bestaand glastype, verwarmde ruimte, U-waarde, HR++/triple/vacuüm, geschiktheid van het bestaande kozijn, ventilatie, zomercomfort en actuele glas-/ISDE-check.

`/renovatieprojecten/ramen-en-glas/` bezit het **vervangingsproject**: per opening behouden/herstellen/aanpassen/vervangen, maatvoering, openingsdelen, montage, aansluiting op de gevel, waterdetail, afwerking, sloop, pre-removal risico's en complete kozijn-/raamofferte.

De vorige twee pagina's overlapten historisch te sterk op `HR++ vs triple`. Na de v2-herbouw van `ramen-en-glas` moet deze pagina expliciet de energetische keuze blijven bezitten en niet terugschuiven naar een tweede kozijnprojectpagina.

## Queries / sub-intents inspected

- dubbel glas vervangen
- oud dubbel glas vervangen
- HR++ glas
- HR++ of triple glas
- triple glas bestaande kozijnen
- vacuümglas
- HR++ glas U-waarde
- glas vervangen ventilatie
- dubbel glas vervangen kosten 2026
- HR++ glas subsidie 2026

## Current SERP pattern

### Milieu Centraal — Triple, HR++ of vacuümglas

Actuele pagina, laatst gewijzigd 18 augustus 2026.

Sterk op:

- verschil enkel / gewoon dubbel / HR++ / triple / vacuüm;
- U-waarde als prestatiemaatstaf;
- gewoon dubbelglas in regelmatig verwarmde ruimten vervangen;
- HR++ in geschikte bestaande kozijnen als logische glas-only route;
- triple vooral in combinatie met nieuwe isolerende kozijnen;
- vacuümglas als dunne, zeer goed isolerende maar duurdere optie;
- controle van dikte, gewicht, sponning en draaiende delen;
- ventilatie bij betere kierdichting;
- buitenzonwering en zomercomfort;
- buitencondens als mogelijk normaal verschijnsel;
- actuele voorbeeldscenario's voor kosten/besparing.

### RVO — ISDE meldcodelijst Hoogrendementsglas

Actuele meldcodelijst gecontroleerd september 2026.

Sterk op:

- productgebonden meldcodes;
- categorieën HR++ en triple;
- onderscheid naar woningtype waar relevant;
- subsidiebedragen op productniveau in de actuele lijst.

Deze data is actueel maar veranderlijk; de pagina moet daarom naar de huidige lijst verwijzen en geen onbeheerde subsidiebedragen als evergreen feit opslaan.

### Vereniging Eigen Huis — Glas vervangen / welk glas

Sterk op:

- kozijnconditie vóór glasvervanging;
- dikte/gewicht van HR++ en triple;
- ventilatie;
- bestaande kozijnen versus nieuwe kozijnen;
- condens en uitvoering;
- kwaliteitscontrole.

Prijsvoorbeelden zijn nuttig als context maar worden niet als universele nationale 2026-prijs gebruikt zonder expliciete scope.

### Commercial SERP

Terugkerend patroon:

- `HR++ prijs per m²`;
- `triple glas prijs per m²`;
- subsidiebedragen;
- glasvergelijkingen;
- leadformulieren;
- claims dat triple automatisch de beste optie is.

Probleem: prijsranges verschillen sterk door oppervlak, glasopbouw, bestaande kozijnen, sponningaanpassing, draaiende delen, ventilatieroosters, montage, glaslatten/kit, bereikbaarheid en kozijnvervanging. Een kale €/m²-range is daarom geen projectprijs.

## Reader needs

1. Eerst weten welk glas er nu zit en of de ruimte regelmatig verwarmd wordt.
2. Weten of het bestaande kozijn technisch goed genoeg is voor nieuw glas.
3. HR++ versus triple versus vacuüm kiezen zonder premium-bias.
4. U-waarde begrijpen zonder vast te lopen in productlabels.
5. Ventilatie vóór bestelling meenemen.
6. Zomercomfort en zonbelasting meenemen bij grote glasvlakken.
7. Actuele subsidie/productmeldcode kunnen controleren.
8. Offertes vergelijken op dezelfde glastype/U-waarde en uitvoeringsscope.
9. Weten wanneer volledige kozijnvervanging een ander project wordt en moet doorstromen naar `/renovatieprojecten/ramen-en-glas/`.

## Coverage matrix

| Need | Current page | Strong SERP | Priority |
|---|---|---|---|
| Existing glass + heated-room filter | MISSING | COVERED | MUST |
| U-value explanation | PARTIAL | COVERED | MUST |
| Keep / HR++ / vacuum / triple+frame / investigate routes | MISSING | RARE | MUST |
| Existing frame condition/dimension/weight gate | COVERED | COVERED | MUST |
| HR++ as main glass-only route | PARTIAL | COVERED | MUST |
| Triple primarily with new high-performance frames | PARTIAL | COVERED | MUST |
| Vacuum glass contextual route | MISSING | COVERED | MUST |
| Ventilation before order | COVERED | COVERED | MUST |
| Summer comfort / external shading | MISSING | COVERED | MUST |
| Current RVO meldcode check | PARTIAL | COVERED | MUST |
| Outside condensation explanation | MISSING | COVERED | MUST |
| Cost/scope normalization | PARTIAL | RARE | MUST |
| Glass-specific quote matrix | PARTIAL | PARTIAL | MUST |
| Explicit split vs ramen-en-glas | MISSING | Internal | MUST |

## Information gain

### 1. `Glasbeslisstaat`

Per relevante ruit/opening alleen de energie-/glasvariabelen:

- ruimte + verwarmd ja/nee;
- oriëntatie / grote zonbelasting;
- bestaand glastype;
- kozijnmateriaal en zichtbare conditie;
- vast of draaiend deel;
- technische geschiktheid voor dikker/zwaarder glas nog te bevestigen;
- huidige luchttoevoer;
- gepland kozijn-/gevelwerk;
- route: behouden / HR++ / vacuüm onderzoeken / kozijn + triple / eerst onderzoek.

Dit verschilt bewust van de `gevelopeningenstaat` op `/renovatieprojecten/ramen-en-glas/`, die het volledige vervangingsproject bezit.

### 2. Five-route decision

- **Behouden** — huidige prestatie of prioriteit rechtvaardigt geen directe vervanging.
- **HR++ in bestaand kozijn** — kozijn technisch geschikt; glas-only verbetering.
- **Vacuüm/slanke oplossing onderzoeken** — beperkte sponning/monument/context.
- **Nieuwe isolerende kozijnen + triple** — kozijnen toch aan vervanging toe / hoge woningprestatie.
- **Eerst onderzoeken** — conditie, ventilatie, vocht/gevelplan of technische geschiktheid onzeker.

### 3. U-value gate

Vergelijk niet op `++` of `+++` alleen. Vraag altijd naar de gedeclareerde U-waarde van het glas; lager betekent betere thermische isolatie. Productnaam en prestatie moeten samen in de offerte staan.

### 4. Heated-room filter

Een glasupgrade heeft andere prioriteit in:

- dagelijks verwarmde woonkamer/keuken/werkruimte;
- incidenteel verwarmde kamer;
- onverwarmde berging/zolder/serrecontext.

Milieu Centraal geeft expliciet aan dat gewoon dubbelglas in regelmatig verwarmde ruimten zinvol kan zijn om te vervangen, terwijl in onverwarmde ruimten vervanging minder voor de hand ligt tenzij kozijnen toch vernieuwd worden.

### 5. Price/scope normalization

Nooit rechtstreeks vergelijken zonder te labelen:

- €/m² glas of projecttotaal;
- glastype + U-waarde;
- bestaand kozijn behouden of vervangen;
- sponning/glaslat-aanpassing;
- scharnieren/draaidelen;
- ventilatieroosters;
- montage, kit en afwerking;
- verwijdering/afvoer;
- subsidie vóór/na prijs.

## GEO opportunities

Standalone answers:

- Wanneer is oud dubbelglas vervangen zinvol?
- HR++ of triple: wat past bij bestaande kozijnen?
- Wanneer is vacuümglas interessant?
- Wat betekent de U-waarde van glas?
- Moet ventilatie worden aangepast na glas vervangen?
- Waarom condenseert goed isolerend glas soms aan de buitenkant?
- Wat moet in een glasofferte staan?
- Waarom zijn glasprijzen per m² niet automatisch vergelijkbaar?

## Internal overlap / cannibalisation

### `/renovatieprojecten/ramen-en-glas/`

Owns:

- frame/window replacement project;
- per-opening keep/repair/adapt/replace;
- dimensions/opening functions;
- mounting, frame-to-wall connection, water detail and finishing;
- demolition/removal risks;
- complete frame/window tender.

### `/verduurzamen/dubbel-glas/`

Owns:

- existing glazing assessment;
- HR++ / triple / vacuum;
- U-value;
- heated-room prioritisation;
- energy/comfort;
- ventilation consequence as decision dependency;
- summer solar/shading context;
- current glazing subsidy/meldcode check;
- glass-only quotation normalization.

### `/verduurzamen/ventilatie/`

Owns system choice and ventilation strategy. This page only identifies ventilation as a pre-order dependency.

### `/renovatie-plannen/subsidies-renovatie/`

Owns cross-measure subsidy orchestration. This page keeps only glass-specific current proof/checks.

## Data gaps / claim boundaries

- Do not present `triple always requires new frames` as an absolute technical law. Use it as the current recommended route from Milieu Centraal for high-performance replacement, while acknowledging technical context.
- Do not claim every existing frame can accept HR++.
- Do not prescribe ventilation grilles when balanced ventilation or another supply strategy exists/planned.
- Do not present a current subsidy amount without a dated RVO check and product/category context.
- Do not turn a Milieu Centraal whole-house cost scenario into a universal national average.
- Do not diagnose external condensation or seal failure remotely; explain the normal pattern and when persistent/internal condensation needs checking.

## Research gate

PASS for drafting.

The central claims have current evidence from Milieu Centraal (18 August 2026), RVO's current high-efficiency-glazing meldcode list and current VEH guidance. The overlap with `/renovatieprojecten/ramen-en-glas/` has an explicit ownership split before writing.
