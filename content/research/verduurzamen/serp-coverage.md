# SERP coverage — `/verduurzamen/`

- Markt: Nederland
- Taal: nl-NL
- Onderzoek: 2026-09-13
- Workflow: editorial engine v2
- Decision: `DEEP_REWRITE`

## Queryset en intent
Gecontroleerde brede intenten:
- `woning verduurzamen welke maatregel eerst`
- `huis verduurzamen stappenplan`
- `waar beginnen woning verduurzamen`
- `verduurzamen volgorde isolatie ventilatie warmtepomp zonnepanelen`

De primaire taak is niet één product kiezen, maar bepalen welke verduurzamingsbeslissing nu logisch is en welke afhankelijkheden eerst opgelost moeten worden.

## Huidige SERP / bronpatroon

### Milieu Centraal — Stappenplan voor een energiezuinig huis
Gecontroleerd 2026-09-13.

Belangrijkste onafhankelijke bron voor de brede intentie:
- de volgorde staat expliciet niet vast;
- een logisch renovatiemoment kan een instappunt zijn;
- isolatie, ventilatie en buitenzonwering worden als samenhangende basis behandeld;
- woningcontext bepaalt de route.

Source: https://www.milieucentraal.nl/energie-besparen/energiezuinig-wonen/stappenplan-voor-een-energiezuinig-huis/

### Concurrentiepatroon
Actuele Nederlandse gidsen gebruiken vaak een lineaire volgorde zoals schil → ventilatie → verwarming → opwek. Dat is begrijpelijk als uitlegmodel, maar geeft weinig ondersteuning wanneer een dak, vloer, kozijn of cv-ketel nu al aan de beurt is.

De information gain van deze hub is daarom: **niet rangschikken op maatregelnummer, maar routeren op woningstaat, blokkade, afhankelijkheid en natuurlijk renovatiemoment.**

## Audit oude hub
Sterk:
- product-onafhankelijke insteek;
- goede child set;
- vocht/technische gebreken werden al genoemd;
- subsidie was geen startpunt.

Zwak:
- legde alsnog een vrij vaste vijfstappenvolgorde op;
- maakte natuurlijke renovatiemomenten niet expliciet;
- routeerde acute cv-vervanging onvoldoende;
- gaf geen echte `no-regret`-gate;
- overlapte inhoudelijk met de oude `/verduurzamen/energie-besparen/`.

## Cannibalisatie na child-rewrites

### `/verduurzamen/` vs `/verduurzamen/energie-besparen/`
**Resolved.**

- hub = investeringsroute, blokkades, afhankelijkheden en natuurlijke renovatiemomenten;
- energie-besparen = huidig verbruik meten, patroon verklaren, kleine ingreep testen, opnieuw meten en pas daarna escaleren.

De child is inmiddels zelf in workflow v2 herschreven, waardoor de oude structurele overlap is verdwenen.

### Hub vs technische children
**No blocking overlap.**

De hub routeert alleen. Detailbeslissingen blijven bij:
- isolatiekaart en bouwdeelroutes;
- glasbeslisstaat;
- luchtstroomkaart;
- warmtepomp-gereedheidsdossier;
- ketelbeslisstaat;
- zonnestroomplan.

### Hub vs `/renovatie-plannen/renovatie-volgorde/`
**No blocking overlap.**

`renovatie-volgorde` owns de fysieke volgorde van bouwwerkzaamheden. Deze hub owns energie-/comfortafhankelijkheden en logische instapmomenten.

## Coverage matrix
| Vraag | Oude hub | V2 |
|---|---|---|
| Geen universele vaste volgorde | partial | MUST |
| Woning-nulmeting | partial | MUST |
| Blokkades vóór investering | partial | MUST |
| Isolatie ↔ ventilatie | covered | MUST |
| Verwarming ↔ warmtevraag/afgifte | partial | MUST |
| PV ↔ dak + toekomstig verbruik | covered | MUST |
| Natuurlijke renovatiemomenten | missing | MUST |
| Unieke child-routing | partial | MUST |
| Duidelijke grens met energie-besparen | missing | MUST |
| Geen universele ROI/ranking | covered | MUST |
| Zomercomfort/buitenzonwering | missing | SHOULD |
| No-regret gate | missing | SHOULD |

## Information-gain model
1. `woning-nulmeting`;
2. `volgende-blokkade-model`;
3. natuurlijke renovatiemomenten;
4. routekaart per startsituatie;
5. `no-regret gate` vóór moeilijk omkeerbare aankopen.

## Publish blocker
FAIL wanneer de hub opnieuw één universele vaste volgorde oplegt, technische child-keuzes dupliceert, overlap met `energie-besparen` creëert of ongesourcete universele besparing/ROI/subsidiebedragen publiceert.
