# SERP coverage — `/verduurzamen/`

- Markt: Nederland
- Taal: nl-NL
- Onderzoek: 2026-09-13
- Workflow: editorial engine v2
- Decision: `DEEP_REWRITE`

## Queryset en subintenties

Gecontroleerde querygroepen:

- `woning verduurzamen welke maatregel eerst`
- `huis verduurzamen stappenplan`
- `verduurzamen volgorde isolatie ventilatie warmtepomp zonnepanelen`
- `waar beginnen woning verduurzamen`
- `energiebesparende maatregelen woning volgorde`

Dominante intentie: informatief/commercieel oriënterend. De gebruiker wil niet één product kiezen, maar bepalen **welke verduurzamingsbeslissing nu logisch is en welke afhankelijkheden eerst opgelost moeten worden**.

## Werkelijk geïnspecteerde SERP — 13 september 2026

### Milieu Centraal — `Stappenplan voor een energiezuinig huis`

https://www.milieucentraal.nl/energie-besparen/energiezuinig-wonen/stappenplan-voor-een-energiezuinig-huis/

Sterkste onafhankelijke resultaat voor de brede intentie.

Belangrijke observaties:

- de volgorde staat expliciet **niet vast**;
- gebruiker kan instappen op een logisch renovatiemoment, bijvoorbeeld wanneer keuken, cv-ketel of aanbouw aan de beurt is;
- basis wordt beschreven als isolatie + ventilatie + buitenzonwering;
- Verbetercheck biedt woningafhankelijke route;
- isolatie en ventilatie worden als samenhangende beslissingen behandeld;
- nadruk op comfort en gezondheid naast energiebesparing.

### VerduurzaamOnline — `Huis verduurzamen: waar begint u?`

https://www.verduurzaamonline.nl/woning-verduurzamen/waar-beginnen

Bijgewerkt 30 augustus 2026.

Patroon:

- uitgangssituatie eerst;
- daarna een grotendeels lineaire route schil → ventilatie → verwarming → opwek;
- sterk antwoord op `waar beginnen`, maar minder sterk op uitzonderingen en renovatiemomenten.

### GOG GROUP — `Stappenplan verduurzaming van je woning`

https://goggroup.nl/kennisbank/verduurzamen-stappenplan-woning

Patroon:

- meet huidige situatie;
- isolatie/kierdichting;
- warmte-installatie;
- zon/opslag;
- sterk afhankelijkheidsargument, maar opnieuw vooral één lineaire volgorde.

### Voltafy — `Je huis verduurzamen: de juiste volgorde`

https://voltafy.nl/kennisbank/huis-verduurzamen-volgorde

Bijgewerkt 3 september 2026.

Patroon:

- zeer duidelijke vaste volgorde;
- veel nadruk op rendement en apparaatdimensionering;
- minder ruimte voor woninggebreken, onderhoudsmomenten of uitzonderingen.

### Wil Ik Hier Wonen — `Huis verduurzamen: waar beginnen?`

https://wilikhierwonen.nl/blog/huis-verduurzamen-waar-beginnen

Gepubliceerd 23 juli 2026.

Patroon:

- schil → installaties → opwek;
- benoemt wel dat precieze volgorde per woning verschilt;
- blijft inhoudelijk een klassiek stappenplan.

## SERP-features / format

De SERP wordt vooral gevuld door:

- brede gidsen;
- genummerde stappenplannen;
- maatregeloverzichten;
- calculators/scans;
- secties rond kosten, subsidie en terugverdientijd.

Er is weinig echte beslisondersteuning rond **wanneer je van de standaardvolgorde mag of moet afwijken**.

## Bestaande pagina — audit

Huidige sterke punten:

- begint al vanuit de woning in plaats van een product;
- koppelt isolatie, ventilatie, verwarming en zonnepanelen;
- benoemt vocht/technische gebreken vóór verduurzaming;
- verwijst naar de belangrijkste child pages;
- subsidie wordt niet als startpunt behandeld.

Huidige zwakke punten:

- presenteert alsnog een vrij vaste 5-stappenvolgorde;
- mist het officiële Milieu Centraal-principe dat de volgorde niet vaststaat;
- mist `natuurlijke renovatiemomenten` als routekeuze;
- overlap met `/verduurzamen/energie-besparen/` is groot: beide beantwoorden `welke maatregel eerst?` met vrijwel dezelfde keten;
- geen expliciete router voor `cv-ketel is nu defect/aan vervanging toe` versus `ik plan rustig vooruit`;
- geen duidelijk model voor blokkades die vóór een verduurzamingsmaatregel opgelost moeten worden;
- buitenzonwering/zomercomfort ontbreekt als cross-cutting aandachtspunt;
- geen compleet overzicht dat alle child intents een unieke vraag geeft.

## Cannibalisatie

### `/verduurzamen/` vs `/verduurzamen/energie-besparen/`

**Structureel risico: hoog.**

Beide pagina's hebben nu dezelfde centrale conclusie: eerst huidige staat/gebruik begrijpen, daarna schil/ventilatie, verwarming en opwek.

Nieuwe ownership:

- `/verduurzamen/` = **routekaart voor investerings- en renovatiekeuzes**. Welke beslisroute hoort bij de huidige woning, welk probleem blokkeert een volgende stap en welke child page bezit de uitwerking?
- `/verduurzamen/energie-besparen/` = **energiegebruik nu verlagen en besparingen prioriteren**, inclusief gedrag/instellingen en maatregelen die zonder compleet renovatieproject kunnen starten. Geen tweede clusterhub.

### `/verduurzamen/` vs `/renovatie-plannen/renovatie-volgorde/`

Geen directe cannibalisatie wanneer de hub geen fysieke werkvolgorde geeft. `renovatie-volgorde` blijft eigenaar van de volgorde van bouwwerkzaamheden; `verduurzamen` bezit energie-/comfortafhankelijkheden.

## Coverage matrix

| Vraag / behoefte | Huidig | SERP | Nieuwe prioriteit |
| --- | --- | --- | --- |
| Uitgangssituatie eerst vastleggen | COVERED | recurring | MUST |
| Geen universele vaste volgorde | PARTIAL | best-source / Milieu Centraal | MUST |
| Blokkades: vocht, lekkage, technisch gebrek | PARTIAL | inconsistent | MUST |
| Isolatie + ventilatie samen beoordelen | COVERED | recurring | MUST |
| Zomercomfort / buitenzonwering meenemen | MISSING | strong official source | SHOULD |
| Verwarming pas kiezen met bekende warmtevraag/afgifte | PARTIAL | recurring | MUST |
| Cv-ketel-einde-levensduur als afwijkend beslismoment | MISSING | official logical-entry example | MUST |
| Zonnepanelen afstemmen op dak en toekomstig stroomgebruik | COVERED | recurring | MUST |
| Natuurlijke renovatiemomenten benutten | MISSING | strong official source | MUST |
| Alle child pages routen op unieke vraag | PARTIAL | n/a | MUST |
| Subsidie niet als technische startbeslissing | COVERED | recurring | SHOULD |
| Onderscheid hub vs `energie-besparen` | MISSING | internal gap | MUST |
| No-regret / irreversible-choice gate | MISSING | information gain | SHOULD |

## MUST

1. Open met: er is geen universele vaste verduurzamingsvolgorde.
2. Laat gebruiker eerst huidige staat vastleggen: schil, glas, ventilatie, verwarming/afgifte, dak/opwek, bekende gebreken en relevante toekomstige plannen.
3. Maak `blokkades vóór maatregelen` expliciet: lekkage/vocht/constructieve of onderhoudsproblemen eerst voldoende begrijpen/oplossen.
4. Behandel isolatie, kierdichting en ventilatie als gekoppelde beslissingen.
5. Leg uit dat verwarmingskeuze afhankelijk is van warmtevraag, afgiftesysteem en woningplan; routeer naar warmtepomp/cv-ketel.
6. Leg uit dat zonnepanelen op dakconditie en toekomstig stroomgebruik worden afgestemd.
7. Introduceer natuurlijke renovatiemomenten: combineer verduurzaming wanneer dak, kozijnen, vloer, keuken/aanbouw of verwarmingssysteem toch aan de beurt is.
8. Routeer alle child intents met unieke vraag/ownership.
9. Reduceer structurele overlap met `/verduurzamen/energie-besparen/` en geef die pagina een duidelijke `besparen-nu`-rol.
10. Geen universele ROI, besparings- of subsidiebedragen op de hub.

## SHOULD

- zomercomfort en buitenzonwering benoemen als onderdeel van de woningprestatie;
- `no-regret gate` vóór een moeilijk omkeerbare aankoop;
- route naar `/renovatie-plannen/subsidies-renovatie/` voor actuele regelingen;
- route naar `/renovatie-plannen/rendement-renovatie/` voor financiële/waarde-afweging;
- expliciete uitzondering: acute cv-vervanging kan een ander instapmoment geven dan een geplande totaalroute.

## Information gain

### 1. `Volgende-blokkade-model`

Niet vragen `welke maatregel staat op nummer 1?`, maar:

1. wat is nu aantoonbaar zwak of defect?
2. welke keuze beïnvloedt andere maatregelen?
3. wat wordt binnenkort toch opengebroken/vervangen?
4. welke aankoop zou later duur zijn om opnieuw te doen?

### 2. `Natuurlijk renovatiemoment`

Koppel verduurzaming aan geplande werkzaamheden:

- dakwerk → dakisolatie + eventueel zonnepanelen voorbereiden;
- kozijnwerk → glas + ventilatie + aansluiting;
- vloer open → vloerisolatie / afgifte;
- cv-ketel einde levensduur → warmteplan versnellen;
- aanbouw/keuken → installaties en ventilatie meenemen.

### 3. `Routekaart per startsituatie`

Geen productlijst maar een beslismatrix:

- hoge rekening / geen duidelijk project → energie besparen;
- koude schil / tocht → isolatie/glas;
- vochtige/stuffe lucht of luchtdichter maken → ventilatie;
- verwarming aan vervanging toe → cv/warmtepomp-keuze;
- dak geschikt + toekomstig stroomprofiel bekend → zonnepanelen.

### 4. `No-regret gate`

Voor bestelling van warmtepomp, nieuwe kozijnen, grote isolatie-ingreep of zonnepanelen: zijn de afhankelijkheden die de dimensionering/scope veranderen voldoende bekend?

## Data gaps

- Geen woningdata of GSC-querydata beschikbaar in deze audit; intentie is bepaald via huidige URL-set, bestaande content en actuele SERP.
- Geen universele besparings- of kostenrangorde publiceren. Die verschilt per woning en hoort op maatregelpagina's met eigen actuele bronnen.

## Publish blocker

`PUBLISH_REVIEW` moet FAIL blijven wanneer:

- de pagina alsnog één vaste universele volgorde als regel presenteert;
- `energie-besparen` en de hub dezelfde primaire taak blijven bezitten;
- niet alle bestaande child intents logisch worden gerouteerd;
- ongesourcete bedragen of universele rendementclaims worden toegevoegd;
- technische gebreken/ventilatie worden genegeerd in de beslisroute.
