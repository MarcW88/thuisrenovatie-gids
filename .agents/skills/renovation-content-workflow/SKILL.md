---
name: renovation-content-workflow
description: Sitespecifieke orkestratie van analyse naar brief, Nederlandse renovatiecontent, SEO en QA.
provenance: custom
---

# Renovation Content Workflow

Gebruik deze skill nadat `renovation-analysis-workflow` de pagina heeft geclassificeerd en de belangrijkste datagaten heeft benoemd.

## Workflow

1. **Analyse overnemen** — contenttype, JTBD, intentie, risico's en bewijsbehoefte.
2. **Brief** — gebruik `content-brief-authoring`.
3. **Schrijven/herschrijven** — gebruik `content-and-copy` in natuurlijk Nederlands.
4. **Bewijscontrole** — gebruik `evidence-based-reviews`; downgrade of verwijder claims die niet voldoende zijn onderbouwd.
5. **Structuur & links** — gebruik `information-architecture`.
6. **SEO** — gebruik `seo-onpage`; schakel `seo-technical` alleen in wanneer de taak technisch is.
7. **Conversie** — voor `LEAD` gebruik `cro-optimization`.
8. **Finale controle** — gebruik `editorial-qa`.

## Contentpatronen per type

### PLAN
Antwoord eerst op de planningsbeslissing. Behandel vervolgens volgorde, afhankelijkheden, budgetfactoren, checkpoints en alleen geverifieerde regels/premies.

### PROJECT
Leg uit wanneer de renovatie relevant is, welke opties bestaan, hoe de voorbereiding en uitvoering verlopen, welke trade-offs tellen en welk onderhoud volgt.

### SUSTAINABILITY
Start vanuit de bestaande woning/context. Bespreek maatregel, comfort, energie-impact en terugverdienlogica alleen met expliciete aannames; actuele steunmaatregelen vereisen bron + marktcontext.

### DIY
Geef eerst aan voor wie de klus geschikt is. Daarna materiaal/gereedschap, stappen, fouten en een duidelijke veiligheidsgrens. Hoog-risicowerk niet normaliseren als gewone DIY.

### TROUBLESHOOTING
Structuur: symptoom → veilige controles → mogelijke oorzaken → oplossing → wanneer stoppen en een vakman inschakelen. Vermijd diagnosezekerheid zonder inspectie.

### LEAD
Structuur: wanneer een vakman nodig is → voorbereiding → wat in de offerte moet staan → appels met appels vergelijken → vragen → red flags → transparante CTA.

## Schrijfregels

- Nederlands, concreet en antwoordgericht.
- Geen generieke intro's of keyword stuffing.
- Geen verzonnen prijzen, normen, subsidies, rendementen of reviews.
- Geen fictieve hands-on ervaring.
- Geen nieuwe route of CTA-flow introduceren zonder aansluiting op de bestaande architectuur.

## Huidige beperking

Zolang de site in de lege-contentfase zit, mag deze workflow briefs en voorstellen opleveren maar niet automatisch tekst in de gegenereerde HTML publiceren.