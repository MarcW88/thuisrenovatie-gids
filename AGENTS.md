# Thuisrenovatie Gids — agentregels

## Taal en positionering

- Schrijf standaard in helder Nederlands (`nl`).
- De site helpt woningeigenaars betere renovatiebeslissingen nemen en vakmensen/offertes vergelijken.
- De toon is praktisch, onafhankelijk, rustig en deskundig. Geen verkooppraat, kunstmatige urgentie of overdreven claims.
- Behoud de bestaande visuele richting en routes. Genereer geen nieuwe pagina's buiten de afgesproken informatiearchitectuur zonder expliciete opdracht.

## Contenttypes en routing

| Type | Map | Doel |
|---|---|---|
| PLAN | `renovatie-plannen/` | volgorde, budget, fasering, vergunningen, voorbereiding |
| PROJECT | `renovatieprojecten/` | concrete renovatieprojecten en keuzes |
| SUSTAINABILITY | `verduurzamen/` | energie, isolatie, installaties en besparing |
| DIY | `doe-het-zelf/` | veilige uitvoerbare klussen |
| TROUBLESHOOTING | `problemen-oplossen/` | symptomen, diagnose, oorzaken en oplossingen |
| LEAD | `vakman-en-offertes/` | vakman kiezen, offerte voorbereiden en vergelijken |

## Verplichte workflow

Voor inhoudelijk werk:

1. Gebruik eerst `renovation-analysis-workflow`.
2. Laat generieke taken uitvoeren door de vendored upstream-skills.
3. Gebruik daarna `renovation-content-workflow` voor briefing, schrijven of herschrijven.
4. Sluit af met SEO-, bewijs- en editorial-QA.

De twee custom skills zijn alleen orkestratie. Nieuwe generieke SEO-, research-, copy-, CRO- of QA-logica hoort niet in een nieuwe custom skill zolang een geschikte upstream-skill bestaat.

## Betrouwbaarheid bij renovatiecontent

- Verzin nooit prijzen, premies, subsidies, normen, rendementen, terugverdientijden, vergunningseisen, certificaten of garanties.
- Tijd- of plaatsgebonden informatie moet een land/regio en controledatum hebben. Als de markt niet expliciet bekend is, formuleer niet alsof een Belgische of Nederlandse regel universeel geldt.
- Gebruik bandbreedtes alleen wanneer de aannames en bronbasis duidelijk zijn.
- Onderscheid feit, aanname, voorbeeld en advies.
- Bij elektriciteit, gas, draagconstructies, asbest, dakwerk op hoogte en andere risicovolle werkzaamheden: geef een duidelijke stopconditie en verwijs naar een gekwalificeerde vakman wanneer nodig.

## Lead- en offertepagina's

`vakman-en-offertes/` is conversion-first maar trust-first:

- leg uit wat in een goede offerte moet staan;
- maak scope, uitsluitingen, timing, betaalmomenten en garanties vergelijkbaar;
- geef concrete vragen voor de vakman;
- benoem red flags zonder angstmarketing;
- CTA's moeten passen bij de beslisfase en mogen nooit doen alsof schaarste of prijsvoordeel bewezen is wanneer dat niet zo is.

## SEO en interne links

- Eén duidelijke hoofdintentie per pagina.
- Geen keyword stuffing, vaste woordquota of geforceerde FAQ's.
- Link contextueel naar een logische vorige/volgende stap in de renovatiebeslissing.
- Voorkom kannibalisatie tussen planning-, project-, probleem- en leadpagina's.
- Schema alleen gebruiken wanneer het overeenkomt met zichtbare content en echte bewijsbasis.

## Huidige publicatiestatus

De pagina's zijn bewust nog leeg. `generate_pages.py` mag op dit moment alleen de lege paginastructuur regenereren. De workflows in deze PR mogen dus geen nieuwe artikeltekst in de HTML schrijven.