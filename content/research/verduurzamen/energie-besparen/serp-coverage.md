# SERP & source coverage — Energie besparen

- Route: `/verduurzamen/energie-besparen/`
- Checked: 2026-09-13

## Decision
`DEEP_REWRITE`.

The old page still behaved like a second sustainability hub. The v2 page must own the narrower task: understand current consumption, test low-risk operational changes, remeasure, then hand off to a structural child page only when the pattern justifies it.

## Current intent
Dutch results mix:
- gas besparen / verwarming lager;
- stroom besparen / sluipverbruik;
- korter douchen;
- slimme meter / inzicht;
- zonnepanelen slimmer gebruiken;
- broad renovation measures.

The information gain is to organize these around diagnosis rather than a top-10 tip list.

## Evidence
### Milieu Centraal — compare energy use
Checked 2026-09-13; last modified 24 June 2026.
- comparison requires housing situation and energy bill context;
- year overview, build year and floor area are useful inputs.
Source: https://www.milieucentraal.nl/tests-en-tools/vergelijk-je-energieverbruik/

### Milieu Centraal — slimme meter
Last modified 18 August 2026.
- smart meter can provide consumption data;
- an energy-use manager can make patterns visible faster;
- insight is a diagnostic aid, not an automatic saving.
Source: https://www.milieucentraal.nl/energie-besparen/inzicht-in-je-energierekening/slimme-meter/

### Milieu Centraal — energy-efficient home / behaviour
Current guidance covers reducing heating, hot-water use, standby/appliance use and shifting own solar consumption. Page avoids copying fixed savings numbers because outcomes depend on starting situation.
Source: https://www.milieucentraal.nl/energie-besparen/energiezuinig-wonen/energiezuinige-woning/

### Milieu Centraal — shower use
Page checked 2026-09-13; current page modified 11 August 2026.
- shorter showers and water-saving shower heads reduce hot-water use.
Source: https://www.milieucentraal.nl/energie-besparen/duurzaam-warm-water/korter-douchen/

### Heating controls boundary
Milieu Centraal guidance differs by heating system: deep night setback can be appropriate with a conventional boiler, while low-temperature / heat-pump systems typically need smaller setback. Therefore the page must not publish one universal thermostat schedule.
Source: https://www.milieucentraal.nl/energie-besparen/energiezuinig-wonen/hoe-werkt-de-verwarmingstest/

### Rijksoverheid — ventilation
- continuous ventilation remains necessary;
- simply airing for a short period is not equivalent;
- insulation makes adequate ventilation more important, not less.
Source: https://www.rijksoverheid.nl/vraag-en-antwoord/energie-thuis/hoe-kan-ik-mijn-huis-ventileren

## Coverage matrix
| Need | Old | V2 |
|---|---|---|
| Baseline annual use | missing | central |
| Context vs generic average | missing | explicit |
| Heating vs hot water vs electricity | weak | separate buckets |
| Smart-meter diagnosis | missing | included |
| Heating system-specific settings | missing | bounded |
| Hot-water route | missing | included |
| Baseload / standby | missing | included |
| Ventilation safety boundary | missing | explicit |
| Own-solar timing | missing | included but subordinate |
| Remeasure after change | missing | central loop |
| Hand-off to investments | broad hub | evidence-led escalation |
| Universal savings claims | risk | prohibited |

## Ownership
This route owns current-use diagnosis and operational improvement. `/verduurzamen/` owns the broader investment roadmap; insulation, heating, ventilation and PV pages own system design.
