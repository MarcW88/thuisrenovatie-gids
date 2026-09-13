# SERP & source coverage — Zonnepanelen

- Route: `/verduurzamen/zonnepanelen/`
- Checked: 2026-09-13
- Market: Netherlands / Dutch

## Research decision
`DEEP_REWRITE`.

The old page had the correct variables — roof, shade, future demand and meterkast — but it did not yet resolve the 2026/2027 decision: system sizing must account for the end of net metering, direct self-consumption, future electrification and roof/electrical readiness before panel count.

## Current intent / SERP pattern
Current results cluster around:
- are solar panels still worthwhile after saldering;
- how many panels fit my usage;
- costs and payback;
- roof suitability, orientation and shade;
- self-consumption, feed-in fees and batteries;
- installation / meterkast / inverter questions.

A generic panel-count calculator therefore adds little information gain. The page should turn those intents into one project-ready decision state.

## Authoritative evidence

### Rijksoverheid — Salderingsregeling stopt in 2027
Checked 2026-09-13.
- salderingsregeling ends **1 January 2027**;
- from 2027 generated electricity can no longer be offset against imported electricity;
- exported electricity still receives a supplier compensation;
- until 2030 the compensation is legally bounded relative to the bare supply tariff under the current rule;
- suppliers may charge feed-in costs within the applicable framework;
- direct self-consumption reduces supplier purchases and network pressure.

Source: https://www.rijksoverheid.nl/themas/klimaat-milieu-en-natuur/energie-thuis/salderingsregeling

### Belastingdienst — btw-tarief zonnepanelen
Checked 2026-09-13.
- delivery and installation of PV on or near a dwelling is generally taxed at 0% VAT;
- the 0% scope includes several installation-specific works but not every adjacent renovation item;
- roof strengthening, full distribution-board replacement and a home battery are examples that can fall outside the PV 0% scope.

Source: https://www.belastingdienst.nl/wps/wcm/connect/bldcontentnl/belastingdienst/zakelijk/btw/tarieven_en_vrijstellingen/goederen_0_btw/btw-tarief-zonnepanelen

### Milieu Centraal — salderen / self-consumption
Checked 2026-09-13; saldering page last modified 10 September 2026.
- saldering stops in 2027;
- direct use of solar electricity becomes more important;
- typical self-consumption is around 30% before active shifting, but this is an average, not a household guarantee;
- EV charging and a heat-pump buffer can materially change daytime self-consumption;
- feed-in compensation and costs vary by contract/supplier.

Sources:
- https://www.milieucentraal.nl/energie-besparen/zonnepanelen/salderingsregeling-voor-zonnepanelen/
- https://www.milieucentraal.nl/energie-besparen/zonnepanelen/verbruik-zelf-meer-zonnestroom/
- https://www.milieucentraal.nl/energie-besparen/zonnepanelen/zonnestroom-als-de-saldering-stopt-dit-moet-je-weten/

### Milieu Centraal — roof and sizing context
Current guidance says to assess roof suitability/shade and future annual electricity demand before deciding system size. It also advises arranging practical grid-registration matters before installation.

Source: https://www.milieucentraal.nl/energie-besparen/energiezuinig-wonen/stappenplan-voor-een-energiezuinig-huis/

### Milieu Centraal — costs
Current examples vary by panel count and assumptions. The useful editorial lesson is not to publish one universal price or payback period. Outcome depends on purchase cost, electricity price, direct self-consumption, feed-in compensation and feed-in charges.

Source: https://www.milieucentraal.nl/energie-besparen/zonnepanelen/kosten-en-opbrengst-zonnepanelen/

### Milieu Centraal — home battery
A battery can increase self-consumption, but storage capacity, purchase cost and environmental impact mean it is not an automatic companion to PV. Treat battery choice as a separate decision.

Source: https://www.milieucentraal.nl/energie-besparen/zonnepanelen/thuisbatterij-zonne-energie-opslaan/

## Coverage matrix
| Intent / risk | Old page | V2 requirement |
|---|---|---|
| Roof condition before installation | present | expand into stop/combine route |
| Orientation / shade | present | production-profile decision |
| Current electricity use | partial | combine with daily profile |
| Future heat pump / EV / induction | present | make sizing input |
| End saldering 1 Jan 2027 | missing | explicit dated gate |
| Direct self-consumption | missing | central sizing/economic variable |
| Feed-in costs / compensation | missing | contract-dependent boundary |
| Meterkast / connection | partial | scope before quote |
| Inverter / cable route | partial | installability gate |
| Roof/VvE ownership | missing | pre-order gate |
| Registration | missing | execution checklist |
| Battery | missing | separate decision, no automatic upsell |
| VAT | missing | current 0% rule with scope boundary |
| Comparable quote scope | light | full PV-specific matrix |

## Information-gain model
Central asset: `zonnestroomplan`.

The page routes users through seven evidence fields and four outcomes: install now, combine with roof work, revise sizing first, investigate first. This is deliberately different from a panel catalogue or a simplistic annual-use calculator.

## Cannibalisation boundary
- This page owns PV suitability, sizing and tender scope.
- `/verduurzamen/energie-besparen/` owns operational behaviour and reducing/reshaping current consumption.
- `/verduurzamen/warmtepomp/` owns the heat-pump system; this page only includes future electric demand as a PV sizing input.
- General quotation methodology stays with `/vakman-en-offertes/offertes-vergelijken/`.

## Cost boundary
No universal payback or €/panel statement. If examples are used, they must carry source date, panel count, assumptions and exclusions. Primary content instead normalises scope between installers.
