# Brief v2 — Rendement renovatie

- Workflow version: 2
- Route: `/renovatie-plannen/rendement-renovatie/`
- Status: QA_COMPLETE
- Market: Netherlands / nl-NL
- Primary queries: `welke verbouwing verhoogt woningwaarde`, `rendement verbouwing`, `renovatie rendement`
- Reader task: compare renovation options without collapsing property value, annual savings, avoided repair and personal use value into one misleading ROI percentage.
- Decision: `DEEP_REWRITE`
- Last researched: 2026-09-13
- Research artifact: `content/research/renovatie-plannen/rendement-renovatie/serp-coverage.md`

## Search intent and ownership

The reader usually wants one of two answers:

1. `Welke verbouwing verhoogt mijn woningwaarde het meest?`
2. `Verdien ik deze renovatie terug?`

The page must explain that those are not identical questions. It owns the whole-renovation return model and the market/value perspective. It must not become a price guide, budget page or technical energy-measure calculator.

## Core thesis

There is no defensible universal ranking such as `dakkapel 95% ROI` or `keuken 60% ROI` for the Dutch market. A useful renovation business case separates:

- **incremental market value** created by the renovation;
- **recurring operating savings** while the owner occupies the home;
- **avoided future cost / risk**;
- **personal use value** such as comfort or space.

The page must also correct for general market appreciation. A house becoming more valuable during the project does not mean the renovation created the full increase.

## Required information architecture

The final page should follow the reader's decision task, not a fixed article template, but MUST contain these assets:

### 1. Direct answer

Open with a concise answer: added usable space and improved technical/energy quality often have the clearest relation to market value; kitchen/bathroom are more taste-sensitive. But the best renovation depends on the return type and holding period.

### 2. Four-return model

Define separately:
- woningwaarde;
- jaarlijkse gebruiksbesparing;
- vermeden herstel/onderhoud;
- woonwaarde / use value.

Do not convert comfort into a fabricated euro amount.

### 3. Market-baseline correction

Explain the counterfactual:

`renovatie-effect ≠ totale waardestijging tijdens de verbouwing`

Use Brainbay Q2 2026 market data to show why: Dutch home values were +3.7% YoY nationally with large regional differences. The useful question is what the renovated home is worth versus a comparable unrenovated home in the same market, not simply before price versus after price.

### 4. Current market evidence

Use NVM/brainbay 23 Jul 2026 carefully:
- fixer-upper cohort;
- modelled average value increase €178,000 after improvement to excellent condition at equal floor area;
- location/type/size matter;
- extra floor area can add further value;
- this is NOT net profit and does not itself deduct purchase position, renovation cost, financing or project costs.

### 5. Scope-specific hierarchy without fake ROI percentages

Explain qualitatively:
- added usable floor area: often strongest/clearest value channel;
- energy/technical quality: can affect both resale value and running costs;
- maintenance/defect resolution: protects value and prevents deterioration;
- kitchen/bathroom/luxury finish: can improve appeal and comfort but is taste-sensitive and often weaker as a pure financial case.

### 6. Energy-return model

Separate:
- market-value effect of better energy performance;
- annual energy savings during ownership.

Use Milieu Centraal's long-term 2026–2040 energy-price assumptions (€1.37/m³ gas, €0.21/kWh electricity) when illustrating the principle, not today's spot price.

Do not double count the same benefit. If an estimated resale value already reflects improved energy quality, that is a capital-value channel; annual savings are only accumulated for the years the current owner actually benefits from them.

### 7. Time-horizon gate

Show why the answer changes depending on how long the owner expects to stay:
- short horizon: marketability, value certainty and transaction timing matter more;
- long horizon: recurring savings, comfort and avoided maintenance matter more.

### 8. Renovatie-rendementkaart

Provide a repeatable comparison card for each option:
- net investment after confirmed subsidy;
- estimated incremental market value (range, not false precision);
- annual recurring savings;
- expected holding period;
- avoided-cost argument;
- technical necessity;
- uncertainty level;
- qualitative comfort/use value.

Use `conservative / base / favourable` scenarios rather than one percentage.

### 9. Value-evidence ladder

Teach the reader what evidence is strongest:
1. independent valuation / relevant comparable sales;
2. robust market/model evidence;
3. actual or well-grounded consumption data;
4. contractor/industry claims;
5. generic internet ROI lists.

### 10. Decision rule

The page should finish with a practical rule:
- fix technical risk first;
- then compare options using the same return model;
- only use a resale-value claim when supported by local/property-specific evidence;
- do not reject a renovation simply because it does not fully return in the sale price if the owner will consume years of comfort/savings.

## Evidence register

### Primary / high-confidence

- NVM / brainbay — `Kluswoning na verbouwing bijna 50% meer waard`, 23 Jul 2026.
- Brainbay — `Woningen stijgen flink in waarde, vooral buiten de Randstad`, 22 Jul 2026.
- Brainbay — `Waardestijging koopwoningen zwakt af, verschil tussen energielabels groot`, 28 Jan 2026.
- Vereniging Eigen Huis — `Wat kost verbouwen`, price level 2026.
- Milieu Centraal — long-term energy-price method for 2026–2040 and insulation benefit methodology.

### Supporting

- Brainbay / NHG — 23 Sep 2025 sustainability/value research, useful as evidence that energy investment can be reflected in value for a defined cohort; never generalise the headline percentage to every home.

## GEO / extractability

- Major questions should open with a direct 1–3 sentence answer.
- Keep facts atomic and source/date adjacent where time-sensitive.
- Strong extractable facts:
  - €178k modelled value increase in the defined NVM/brainbay fixer-upper cohort at equal floor area;
  - Q2 2026 Dutch market value +3.7% YoY nationally, with large regional variation;
  - Milieu Centraal's long-term 2026–2040 calculation prices: €1.37/m³ gas and €0.21/kWh electricity.
- Do not manufacture FAQ sections or ROI tables merely for GEO.

## Cannibalisation boundaries

- `/renovatiekosten/`: current price benchmarks and scope.
- `/renovatie-budget/`: affordability, reserve and ongoing spend control.
- `/subsidies-renovatie/`: subsidy eligibility/application.
- `/verduurzamen/*`: technical, measure-specific energy economics.
- project pages: execution/scope of the specific project.

This page may link to them but must not duplicate their detailed content.

## Safety / factuality constraints

- No universal ROI percentages for kitchens, bathrooms, dakkapellen, extensions or full renovations.
- No claim that market value increase equals profit.
- No claim that energy-label premium is guaranteed by a specific intervention.
- No invented avoided-cost probability.
- Subsidy only reduces net investment once eligibility is sufficiently established; otherwise treat it as expected, not guaranteed.

## QA completion

- SERP matrix persisted and applied.
- MUST gaps explicit and resolved in the planned structure.
- Fact-check required after drafting.
- Post-write gap check required before publish review.
- Site-level `noindex` remains unchanged.
