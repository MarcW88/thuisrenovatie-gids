---
workflow_version: 2
status: BRIEF_READY
route: /renovatieprojecten/aanbouw/
decision: DEEP_REWRITE
market: Nederland
language: nl-NL
last_research: 2026-09-13
---

# Content brief — Aanbouw

## Primary query + cluster

Primary:
- aanbouw

Supporting:
- uitbouw woning
- aanbouw kosten 2026
- aanbouw vergunning
- aanbouw fundering
- aanbouw offerte

## Search intent

Commercieel-informatief. De gebruiker wil extra woonruimte en zoekt tegelijk haalbaarheid, kosten, regels en een aannemer. De SERP is prijs- en stappenplan-zwaar, maar de beslissing die vóór prijs komt is onderbelicht: **is het gekozen concept technisch, ruimtelijk en regeltechnisch voldoende uitgewerkt om betrouwbaar te laten offreren?**

## Target audience / maturity

Woningeigenaar in Nederland die een aanbouw of uitbouw overweegt en nog vóór definitieve opdracht, ontwerpfixatie of offertevergelijking zit. Geen bouwkundige voorkennis veronderstellen.

## Job to be done

Ik wil bepalen welke aanbouw bij mijn woning past, welke onzekerheden ik vóór een vaste prijs moet oplossen en wanneer mijn ontwerp voldoende duidelijk is om meerdere aannemers dezelfde opdracht te laten offreren.

## Ownership

Deze URL owns:
- projectvoorbereiding van één concrete aanbouw/uitbouw;
- interface tussen gebruik, bestaand huis, constructie, fundering, daglicht, schil, installaties en regels;
- scoped prijsbenchmark voor aanbouw;
- voorwaarden voor een offertewaardig ontwerp.

Niet ownen:
- brede uitleg van het vergunningstelsel → `/renovatie-plannen/renovatievergunning/`;
- algemene prijsvergelijking tussen renovatietypen → `/renovatie-plannen/renovatiekosten/`;
- woningbrede coördinatie → `/renovatie-plannen/complete-renovatie/`;
- funderingsherstel / diagnose → `/renovatieprojecten/fundering/` en `/problemen-oplossen/funderingsproblemen/`;
- detailadvies isolatie/verwarming/ventilatie → `/verduurzamen/`.

## MUST coverage

1. doel en gebruik vóór maatvoering;
2. constructieve impact van geveldoorbraak;
3. fundering als project-specifieke ontwerpinput;
4. daglichtimpact op bestaand + nieuw deel;
5. isolatie, verwarming en ventilatie als gekoppelde interface;
6. locatie-/projectspecificiteit van regels en Vergunningcheck;
7. `vergunningvrij ≠ regelvrij`;
8. actuele 2026-prijsbenchmark met scope;
9. expliciete scheiding casco / doorbraak / afbouw / installaties / inrichting;
10. offerte-ready gate met gedeelde technische uitgangspunten.

## SHOULD coverage

- buren, erfgrens en uitvoeringstoegang als praktische randvoorwaarden;
- prefab versus traditioneel alleen als projectkeuze, zonder universele winnaar.

## Central thesis

**Een aanbouw is pas klaar om te laten prijzen als duidelijk is wat de extra ruimte met de bestaande woning doet én welke technische en regeltechnische randvoorwaarden het ontwerp begrenzen.** Vierkante meters zijn pas daarna nuttig.

## Information gain

### 1. Haalbaarheidsgate

Vóór definitief ontwerp/offerte moeten vijf vragen voldoende zijn opgelost:
- opening / draagconstructie;
- funderingsprincipe / bodemrisico;
- daglichtimpact;
- schil + installaties;
- regels / Vergunningcheck.

Geen DIY-berekeningen. Het is een beslis- en handoffmodel.

### 2. Bestaande-woning-test

Voor elke ontwerpvariant expliciet controleren:
- wordt de bestaande woonkamer/keuken donkerder of onhandiger diep?
- verdwijnen radiator-, ventilatie- of gevelvoorzieningen?
- veranderen vloerhoogte, drempels of doorloop?
- blijft de bestaande plattegrond logisch nadat de achtergevel opschuift?

### 3. Casco ≠ totaalprijs

Gebruik Vereniging Eigen Huis prijspeil 2026 als kernbenchmark:
- 5 × 2 m / 10 m²: €21.750–€27.550;
- 4 × 3 m / 12 m²: €23.900–€29.950;
- 5 × 3 m / 15 m²: €33.850–€43.325;
- 5 × 4 m / 20 m²: €39.900–€48.300.

Scope expliciet: casco stenen aanbouw, incl. btw, **exclusief geveldoorbraak, afwerking, installaties en inrichting**.

Relevante losse VEH-opties mogen apart worden genoemd, niet stilzwijgend in het totaal worden opgeteld:
- heipalen per 2 €1.850;
- geveldoorbraak €3.600;
- stucwerk €1.225;
- elektra €675;
- centrale verwarming €1.230;
- aftimmerwerk €395.

### 4. Offerteklaar ontwerp

Een ontwerp is pas offertewaardig wanneer verschillende aannemers dezelfde basis kunnen prijzen:
- maatvoering en opening;
- constructieve uitgangspunten;
- funderingsscope;
- schil / kozijnen / glas / dak;
- installaties;
- sloop en herstel bestaand huis;
- afwerkingsniveau;
- uitsluitingen, meerwerk en verantwoordelijkheden.

## Evidence / entities

Required:
- Vereniging Eigen Huis — `Wat kost verbouwen`, prijspeil 2026;
- Omgevingsloket — Vergunningcheck / `Aanbouw of schuur plaatsen`;
- Rijksoverheid — vergunningvrij bouwen en verbouwen + stappenplan;
- IPLO — verbouwen van een bouwwerk / aanbouw, rechtens verkregen niveau, daglicht en thermische eisen.

Do not:
- cite leadgen-sites as primary evidence when official/independent source exists;
- publish a universal `vergunningvrij tot X meter` shortcut;
- publish a universal foundation recipe;
- give exact daylight calculations as project advice;
- give a universal build duration.

## Proposed structure

1. Direct answer: start with function + existing-house impact, not m².
2. `Wat verandert er aan je bestaande woning?` → bestaande-woning-test.
3. `Haalbaarheidsgate` → 5 interfaces before design lock.
4. Rules box → Vergunningcheck + vergunningvrij ≠ regelvrij.
5. Price section → VEH 2026 scoped casco benchmarks + loose options.
6. `Casco, wind- en waterdicht of afgebouwd?` → scope normalization, no universal supplier terminology.
7. `Wanneer is je ontwerp offerte-klaar?` → package for contractors.
8. Offer comparison → scope/risks/responsibilities, then CTA.

## Safety / freshness

- constructie, geveldoorbraak en fundering: passende deskundige beoordeling;
- electrical/gas changes: no DIY instructions;
- legal/regulatory claims: official Dutch source and current date;
- prices: always price level + inclusions/exclusions;
- no claim that the site inspected soil, foundation or structure.

## Internal links

Outbound:
- `/renovatie-plannen/renovatievergunning/` for system-level permit explanation;
- `/renovatie-plannen/renovatiekosten/` for broad market benchmarks;
- `/renovatie-plannen/renovatie-budget/` for project budget/reserve;
- `/vakman-en-offertes/offertes-vergelijken/` after scope gate;
- `/renovatie-plannen/complete-renovatie/` when the extension triggers wider coordinated renovation.

## Existing value to preserve

- project-specific foundation warning;
- early day-light concern;
- existing CTA concept: same design and technical assumptions for every contractor;
- safe refusal to make universal permit claims.

## Success criteria

- all 10 MUST items COVERED in post-write gap check;
- no central unverified price/regulatory/technical claim;
- page reads unmistakably as an `aanbouw` decision page, not a generic project template;
- reader can tell when an idea is ready for quotes and what is still unresolved;
- indexation stays unchanged (`noindex,follow`).