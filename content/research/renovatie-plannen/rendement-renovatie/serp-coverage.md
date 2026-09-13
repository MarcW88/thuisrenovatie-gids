# SERP coverage — rendement renovatie

- Workflow version: 2
- Route: `/renovatie-plannen/rendement-renovatie/`
- Market: Netherlands / nl-NL
- Researched: 2026-09-13
- Decision: `DEEP_REWRITE`

## Query set

Primary:
- `welke verbouwing verhoogt woningwaarde`
- `rendement verbouwing`
- `renovatie rendement`

Variants / sub-intents:
- `welke verbouwing levert meeste waardestijging op`
- `uitbouw waarde woning`
- `keuken badkamer woningwaarde`
- `energielabel woningwaarde`
- `isolatie rendement`
- `verbouwing terugverdienen`

## Current SERP evidence

| Source | Date | What it covers | Use in page |
|---|---|---|---|
| NVM / brainbay — `Kluswoning na verbouwing bijna 50% meer waard` | 2026-07-23 | Brainbay modelvalue analysis of renovated fixer-uppers; average value change €178k at equal living area; location/type/size matter; added floor area can add more | Strong evidence that renovation quality can add market value, with strict caveat that value change is not profit or universal ROI |
| Brainbay — `Woningen stijgen flink in waarde, vooral buiten de Randstad` | 2026-07-22 | Overall Dutch housing value +3.7% YoY in Q2 2026, with strong regional differences | MUST caveat: do not credit general market appreciation to the renovation |
| Brainbay — `Waardestijging koopwoningen zwakt af, verschil tussen energielabels groot` | 2026-01-28 | Label A comparable homes valued >17% above label G in current model; market/value context | Evidence that energy quality is priced by the market; do not present as guaranteed renovation return |
| Brainbay / NHG — `Verduurzaming koopwoning loont` | 2025-09-23 | 15,000 homes under NHG; full insulation investment often reflected in value, with substantial heterogeneity | Use as supporting evidence for energy-value channel, not a universal percentage promise |
| Vereniging Eigen Huis — `Wat kost verbouwen` | price level 2026 | Extra usable space often creates clearest value effect; kitchen/bathroom more comfort- and taste-sensitive | Strong consumer-language benchmark for scope-specific value |
| Milieu Centraal — energy savings methodology | current, 2026–2040 assumptions | Uses long-term energy prices (€1.37/m³ gas, €0.21/kWh electricity) instead of spot prices for recurring savings | MUST for sensible energy-return method |
| Milieu Centraal — insulation long-term benefit | current | 25-year benefit methodology; examples differ by insulation type | Show that energy measures have recurring cashflow economics, not only resale value |

## SERP pattern

The SERP is dominated by ranked lists such as `top renovations for ROI`, often with unsourced 60–120% ROI percentages. Stronger sources are more cautious: usable floor area, energy performance and condition can influence value, while kitchens/bathrooms are more taste-sensitive.

### Competitor weakness

Most ranking pages collapse different concepts into one percentage:
- market value increase;
- recovery of construction cost;
- energy savings;
- avoided future repair;
- personal comfort;
- general house-price appreciation.

This creates false precision and makes different projects incomparable.

## Coverage matrix

| Reader need | Priority | Current page | Required action |
|---|---|---|---|
| Explain that `rendement` is not one metric | MUST | COVERED | Keep and sharpen |
| Separate renovation-created value from general market appreciation | MUST | MISSING | Add explicit baseline / counterfactual method |
| Explain extra usable floor area as a strong value channel | MUST | COVERED | Keep, source to VEH + NVM/brainbay |
| Explain kitchen/bathroom as taste-sensitive rather than guaranteed ROI | MUST | COVERED | Keep, source to VEH |
| Explain energy measures through both resale value and recurring savings | MUST | PARTIAL | Add two-channel model + long-term energy-price method |
| Prevent NVM €178k from being read as profit | MUST | COVERED | Strengthen with cost and market-baseline caveats |
| Give a repeatable method to compare two renovation options | MUST | MISSING | Add rendementkaart / scorecard |
| Include avoided costs / maintenance backlog | SHOULD | COVERED | Keep, avoid invented probabilities |
| Explain holding period / time horizon | MUST | MISSING | Add: 2-year seller vs 15-year occupier have different economics |
| Include subsidy in net investment without treating it as guaranteed | SHOULD | MISSING | Link to subsidy page and use `netto investering` only after eligibility |
| Show scenario ranges rather than one ROI number | MUST | PARTIAL | Add conservative/base/favourable scenario method |
| Avoid double counting value gain + savings | MUST | MISSING | Add explicit anti-double-counting rule |
| Recommend pre/post valuation when resale-value question is material | SHOULD | MISSING | Add independent valuation / comparable-sales step |

## Information gain opportunities

1. **Renovatie-rendementmodel** with four separate outputs: incremental market value, recurring savings, avoided cost, use value.
2. **Market baseline correction**: compare the renovated home's value change against what a similar unrenovated home would have done in the same market. Brainbay Q2 2026 shows why this matters: national value +3.7% YoY with large regional differences.
3. **Time-horizon gate**: short holding period favours sale/value certainty; long holding period increases the relevance of recurring energy savings and comfort.
4. **No-double-counting rule**: if improved energy performance is already reflected in an estimated resale-value uplift, do not automatically add the same benefit again as a capital-value gain; annual energy savings remain a separate cashflow only for the period the owner actually occupies the home.
5. **Scenario card** instead of universal ROI rankings.
6. **Value-evidence ladder**: hard evidence (valuation/comparables), model evidence (Brainbay), operational savings (actual/estimated consumption), qualitative comfort.

## GEO / citation opportunities

- NVM/brainbay 23 Jul 2026: average modelled value increase €178,000 for fixer-uppers renovated to excellent condition at equal floor area; not a profit figure.
- Brainbay 22 Jul 2026: overall Dutch home value +3.7% YoY in Q2 2026, with much higher/lower local growth; useful to explain baseline correction.
- Brainbay 28 Jan 2026: comparable label-A homes carried a >17% premium versus label-G in the model; this is a market association, not guaranteed renovation ROI.
- Milieu Centraal: long-term 2026–2040 prices €1.37/m³ gas and €0.21/kWh electricity are used for savings calculations, avoiding spot-price distortion.
- VEH: added usable space tends to have a clearer value relation; kitchens/bathrooms are more taste-sensitive.

## Internal ownership / cannibalisation

- `/rendement-renovatie/` owns the decision model for total return/value.
- `/renovatiekosten/` owns current cost benchmarks and scopes.
- `/renovatie-budget/` owns affordability, reserve and live spend control.
- `/subsidies-renovatie/` owns eligibility/application; this page only uses confirmed subsidy as a reduction of net investment.
- `/verduurzamen/*` owns measure-specific technical and energy economics.
- `/aanbouw/`, kitchen/bathroom and other project pages own project-specific execution details, not generic ROI ranking.

## Data gaps / constraints

- No universal ROI percentage can be defended for kitchen, bathroom, dakkapel, extension or full renovation across the Dutch market.
- The NVM/brainbay €178k figure is modelled value change for a defined fixer-upper cohort, not net profit and not a before/after transaction study of identical homes.
- Energy-label premiums vary by period, location, dwelling type and market conditions.
- Personal comfort has no objective euro value unless the owner explicitly assigns one; do not fabricate one.

## Gate

- Current SERP inspected: YES
- Primary/current evidence identified: YES
- MUST gaps explicit: YES
- Cannibalisation ownership clear: YES
- Blocking data gaps resolved by excluding unsupported universal ROI rankings: YES
- Eligible for brief: YES
