# Content brief — Verduurzamen

- Route: `/verduurzamen/`
- Type: `HUB`
- Markt: Nederland
- Taal: Nederlands
- Workflow version: 2
- Status: `QA_COMPLETE`
- Laatste broncheck: 2026-09-13
- Decision: `DEEP_REWRITE`

## Primaire gebruikersjob
Ik wil mijn woning verduurzamen maar weet niet welke beslissing nu logisch is, welke afhankelijkheden eerst moeten worden opgelost en welke maatregelpagina bij mijn startsituatie hoort.

## Ownership
Deze hub bezit de **routekeuze door het verduurzamingscluster**:
- huidige woningstaat vastleggen;
- blokkades vóór investeringen herkennen;
- afhankelijkheden tussen schil, ventilatie, verwarming en opwek begrijpen;
- natuurlijke renovatiemomenten benutten;
- gebruiker naar de juiste child page sturen.

De hub bezit niet de detailkeuze van isolatiemethode, glas, ventilatiesysteem, warmtepomp, cv-ketel, PV-dimensionering of dagelijks energiegebruik. Die blijven op de child pages.

## Centrale thesis
Er is geen universele verduurzamingsvolgorde. Kies de volgende stap op basis van **de huidige staat van de woning, blokkades die eerst opgelost moeten worden, afhankelijkheden met andere maatregelen en het eerstvolgende natuurlijke renovatiemoment**.

## MUST
1. Open expliciet met: geen universele vaste volgorde.
2. Laat gebruiker eerst een nulmeting maken van schil, glas, ventilatie, verwarming/afgifte, dak/opwek, gebreken en toekomstige plannen.
3. Maak lekkage, vocht, constructieve/onderhoudsproblemen en onbekende opbouw expliciete blokkades vóór grote investeringen.
4. Behandel isolatie/kierdichting en ventilatie als gekoppelde beslissingen.
5. Verwarmingskeuze hangt af van warmtevraag, afgifte en toekomstig woningplan; routeer naar warmtepomp/cv-ketel.
6. Zonnepanelen worden afgestemd op dakconditie en toekomstig stroomgebruik; routeer naar de PV-pagina.
7. Introduceer natuurlijke renovatiemomenten: dak, kozijnen, vloer, aanbouw/keuken en cv-ketel.
8. Routeer alle child intents op een unieke gebruikersvraag.
9. Maak de grens met `/verduurzamen/energie-besparen/` expliciet: hub = investeringsroute; child = huidig verbruik meten/verlagen.
10. Geen universele prijs-, besparings-, subsidie- of ROI-rangorde.

## SHOULD
- buitenzonwering en zomercomfort als cross-cutting aandachtspunt;
- `no-regret gate` vóór moeilijk omkeerbare aankopen;
- subsidies en rendement alleen doorlinken naar hun eigen routes;
- acute cv-vervanging als logisch afwijkend instapmoment.

## Information gain assets
### Woning-nulmeting
- dak/gevel/vloer/glas: isolatie en conditie;
- ventilatie: toevoer, doorstroming, afvoer;
- verwarming: bron + afgiftesysteem;
- dak: conditie/schaduw/geplande werken;
- vocht/lekkage/onderhoud;
- geplande keuken/aanbouw/vloer/kozijnen;
- toekomstig stroomgebruik.

### Volgende-blokkade-model
1. Wat is aantoonbaar zwak, defect of oncomfortabel?
2. Welke keuze verandert de scope van andere maatregelen?
3. Wat wordt binnenkort toch opengebroken of vervangen?
4. Welke aankoop is later duur om opnieuw te doen?

### Natuurlijke renovatiemomenten
- dakwerk → dakisolatie + PV-plan;
- kozijnen → glas + ventilatie + gevelaansluiting;
- vloer open → vloerisolatie + toekomstige afgifte;
- cv einde levensduur → warmteplan;
- aanbouw/keuken → installaties + ventilatie + warmtevraag.

### No-regret gate
Vóór warmtepomp, complete kozijnvervanging, grote isolatie-ingreep of PV: zijn scope-afhankelijkheden bekend, komt er binnenkort ander werk, blijft ventilatie/comfort goed en past de keuze bij het volgende project?

## Current child ownership after completed V2 rewrites
- `/verduurzamen/energie-besparen/` — verbruiksdiagnose vandaag;
- `/verduurzamen/isolatie/` — whole-home insulation map;
- dak/vloer/gevel children — bouwdeelroute;
- `/verduurzamen/dubbel-glas/` — glass performance decision;
- `/verduurzamen/ventilatie/` — airflow strategy;
- `/verduurzamen/warmtepomp/` — heat-pump readiness dossier;
- `/verduurzamen/cv-ketel/` — replacement-state decision;
- `/verduurzamen/zonnepanelen/` — zonnestroomplan.

## Source
Milieu Centraal, `Stappenplan voor een energiezuinig huis`, gecontroleerd 13 september 2026. De volgorde staat niet vast en logische renovatiemomenten kunnen instappunten zijn.

## Publish success
PASS alleen wanneer 10/10 MUST gedekt zijn, child ownership klopt, geen vaste universele volgorde wordt opgelegd, canonical correct is en `noindex,follow` behouden blijft.
