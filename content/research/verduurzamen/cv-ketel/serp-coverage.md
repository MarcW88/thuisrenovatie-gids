# SERP & evidence coverage — Cv-ketel

- Route: `/verduurzamen/cv-ketel/`
- Checked: 2026-09-13
- Workflow: v2 research-first

## Current search intent
Dutch results around `cv-ketel vervangen`, `cv ketel vervangen 2026`, `cv ketel of hybride warmtepomp` and `kosten cv ketel vervangen` mix four intents:

1. **replacement timing** — age, failures, repair versus replacement;
2. **system choice** — new HR boiler versus hybrid versus all-electric;
3. **price** — boiler-only, installation and all-in project prices are frequently mixed;
4. **regulation/subsidy** — many users still search around the abandoned 2026 hybrid-obligation proposal and current ISDE.

## Evidence

### Milieu Centraal — Cv-ketel vervangen
Current page checked 13 September 2026.

Relevant points:
- replacement is a natural moment to consider a more efficient heating route;
- alternatives include hybrid and fully electric heat pumps;
- if a new boiler is chosen, Milieu Centraal advises an efficient HR boiler and discusses combination with hybrid;
- an electric cv-boiler / inductie-cv is discouraged because of high electricity use.

URL: https://www.milieucentraal.nl/energie-besparen/verwarmen-met-gas/cv-ketel-vervangen/

### Milieu Centraal — Cv-ketel onderhoud en instelling
Last modified 24 June 2026.

Relevant points:
- old open or semi-open boilers have a higher risk around combustion gases;
- modern HR boilers are closed systems with separate combustion-air supply and flue-gas discharge;
- for an old open/semi-open boiler, professional assessment/replacement is especially relevant;
- points users to reliable certified installers.

URL: https://www.milieucentraal.nl/energie-besparen/verwarmen-met-gas/cv-ketel-onderhoud-en-instelling/

### Rijksoverheid — abandoned 2026 heating-installation standard
Published 31 October 2024; still current policy reference.

Relevant point:
- the cabinet abandoned the planned efficiency standard for heating installations that would have made the (hybrid) heat pump the norm from 2026.

URL: https://www.rijksoverheid.nl/documenten/2024/10/31/rapporten-onderzoeken-voor-vervallen-normering-verwarmingsinstallaties-in-2026

### Rijksoverheid — carbon monoxide / certified gas work
Current page checked 13 September 2026.

Relevant points:
- installation, maintenance and repair of gas-combustion appliances must be performed by a CO-vrij certified company;
- DIY work on these appliances is not allowed;
- in apartment buildings, shared flue-gas discharge and combustion-air supply require explicit VvE/landlord attention and control.

URL: https://www.rijksoverheid.nl/vraag-en-antwoord/gezond-en-veilig-wonen/hoe-voorkom-ik-koolmonoxidevergiftiging-in-mijn-huis

### RVO — ISDE heat-pump meldcodelijst
Content checked by RVO on 10 September 2026.

Relevant points:
- subsidy is attached to qualifying heat-pump products / meldcodes and current technical conditions;
- a loose replacement gas boiler is not the subsidised measure on this list;
- current product/meldcode must be checked before assignment/application rather than hard-coding one generic subsidy amount.

URL: https://www.rvo.nl/subsidies-financiering/isde/meldcodelijsten/warmtepompen

## Commercial SERP pattern
Current September 2026 result pages publish strongly differing all-in price ranges for boiler replacement and hybrid systems. Some mix:

- device only;
- standard replacement at the same location;
- installation including old-boiler removal;
- flue-gas changes;
- thermostat/control;
- hybrid addition;
- VAT-included and VAT-excluded figures.

Conclusion: **do not publish one universal national 2026 replacement price as if the scope were stable.** The page should teach scope normalisation and route comparison.

## Information gap in the SERP
Most pages jump quickly from `ketel oud` to a product choice. The stronger decision-support opportunity is to make users establish a **`ketelbeslisstaat`** first:

- safety / failure / maintainability;
- boiler type;
- individual/shared flue;
- heating versus hot-water requirement;
- heat-pump readiness already assessed or not;
- future heating plan;
- intended ownership horizon.

Then route to four outcomes:

1. retain/repair;
2. new HR boiler;
3. hybrid at replacement moment;
4. no new gas boiler: fully electric / other heat route.

## Ownership / cannibalisation

### This page owns
- replacement moment;
- keep/repair/replace decision;
- new HR boiler versus hybrid versus no new gas boiler at that moment;
- gas-boiler safety and flue scope;
- tap-water comfort as a boiler-selection variable;
- boiler-specific tender scope.

### `/verduurzamen/warmtepomp/` owns
- 50 °C readiness evidence;
- heat-loss / sizing logic;
- emitters;
- outdoor-unit noise/placement;
- electrical capacity;
- heat-pump-specific quotation scope.

### `/renovatie-plannen/subsidies-renovatie/` owns
- broad ISDE orchestration and timing.

## Coverage matrix

| Decision need | Typical SERP coverage | v2 answer |
|---|---|---|
| Can I still install a gas boiler in 2026? | often confused by old rule | explicit abandoned-rule correction |
| Is age alone enough to replace? | often age threshold shorthand | no; separate age from safety/failure/repairability |
| Open/semi-open old boiler | fragmented | explicit safety route |
| Shared flue in apartment | weak | VvE/shared-flue gate |
| HR vs hybrid vs all-electric | common but product-led | route-led decision |
| Hot-water comfort | often buried in CW class | treated separately from space heating |
| Heat-pump readiness | duplicated everywhere | handoff to dedicated warmtepomp page |
| Electric cv boiler | often presented as alternative | explicitly not normalized as equivalent sustainable route |
| Subsidy | often generic amount | current heat-pump meldcode boundary |
| Costs | broad ranges | functional scope normalization |
| Quote comparison | weak | boiler-specific quote matrix |
| Certified execution | sometimes footnote | mandatory gate |

## Editorial decision
**DEEP_REWRITE**.

The old page had the correct high-level idea but lacked keep/repair logic, shared-flue scope, open-boiler safety, hot-water separation, quote normalisation and evidence-backed routing.