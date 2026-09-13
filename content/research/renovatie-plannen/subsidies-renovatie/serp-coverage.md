# SERP coverage — Subsidies renovatie

- Route: `/renovatie-plannen/subsidies-renovatie/`
- Research date: 2026-09-13
- Market: Netherlands / nl-NL
- Decision: `DEEP_REWRITE`
- Primary queries: `subsidie verbouwing 2026`, `renovatie subsidie 2026`, `ISDE 2026`, `subsidie woning verduurzamen 2026`

## Search intent

The dominant intent is not simply “what subsidies exist?” Homeowners need to know which national route applies, which measures qualify, what must be checked before commissioning work, how combinations change the amount, and what evidence/timing can make an otherwise eligible measure fail at application stage.

## SERP observations

- RVO owns the authoritative current ISDE decision flow, calculator and meldcode lists.
- Rijksoverheid explains ISDE as the main national homeowner subsidy route for insulation and sustainable installations and points to additional financing/support.
- Vereniging Eigen Huis and Milieu Centraal translate the rules into homeowner language, especially combination rules and the new 2026 ventilation subsidy.
- Commercial subsidy pages often publish complete static amount tables. They are easy to scan but become stale quickly and sometimes flatten important conditions.
- Current official RVO surfaces are not perfectly consistent in cached warm-network amounts. Therefore this page must not publish a fixed warm-network amount unless verified on the exact current measure page at publication time.

## MUST coverage

| Need | Current page | Required action |
|---|---|---|
| Identify ISDE as the main national route for owner-occupiers | COVERED | Keep, but clarify scope and alternative routes for VvE/other situations. |
| Show eligible measure families | COVERED | Keep current RVO categories. |
| Explain that exact amount depends on m²/product/system | COVERED | Keep and make calculator/meldcode the source of truth. |
| 2026 ventilation subsidy | COVERED | Keep €400 one-time and combination requirement. |
| Explain combination logic for isolation | MISSING | Add: isolation amount can double with another eligible isolation measure or warmtepomp/zonneboiler/warmtenet within the applicable 24-month logic. |
| Explain that ventilation alone does not double isolation subsidy | MISSING | Add explicitly; this is a high-risk misunderstanding in 2026. |
| Application timing / 24-month rule | PARTIAL | Make deadline and sequence explicit. |
| Evidence/photos/invoice/product details | PARTIAL | Turn into an application-proof checklist. |
| Meldcode logic including product not on list | PARTIAL | Explain that application can still be possible with technical documentation, but eligibility is not guaranteed. |
| Distinguish subsidy from financing/loan | MISSING | Separate subsidy from Warmtefonds/financing; do not call loans subsidies. |
| Local schemes | COVERED | Keep generic and route to current local/official lookup rather than invent examples. |
| Monument / VvE exception routes | PARTIAL | Flag that other conditions/routes can apply instead of forcing standard-owner rules. |

## SHOULD coverage

- Explain that the installation/placement date determines which year's amount applies for product/material registers.
- Warn against choosing a technically inferior measure purely for subsidy.
- Keep subsidy provisional in the renovation budget until concrete product, execution, timing and evidence match the current rules.
- Explain why screenshots/old blog tables are weak evidence compared with RVO's live register.
- Mention 2026 policy freshness and link to the RVO 2026 calculator rather than reproducing every volatile amount.

## Information gain

1. **Subsidy route map:** owner-occupier → measure → current conditions → meldcode/technical proof → execution/evidence → application → budget status.
2. **Combination matrix:** what can double isolation support and what does not.
3. **Evidence gate:** what must be captured before/during work so eligibility is not lost after installation.
4. **Volatility rule:** a subsidy figure is usable only together with measure/product, installation date and current source.
5. **Budget rule:** treat subsidy as expected support, not guaranteed cash, until the concrete application conditions are satisfied.

## GEO / extractability opportunities

- Atomic answer to “Welke renovatiesubsidie is er in 2026?”
- Atomic explanation of the 2026 €400 ventilation measure.
- Atomic distinction between `subsidie`, `lening` and `lokale regeling`.
- Compact combination matrix for isolation + second measure.
- Current-source hierarchy: RVO decision tree/calculator/meldcode list first.

## Cannibalisation boundary

- `/subsidies-renovatie/` owns financial support eligibility, current application logic and evidence requirements.
- `/renovatie-budget/` owns how subsidy is treated in the project budget and cash-control process.
- `/verduurzamen/*` pages own technical measure selection; they may mention subsidy but should link here for the general ISDE logic.
- `/renovatiekosten/` owns gross market cost benchmarks, not net-of-subsidy pricing.

## Data gaps / risks

- Do not publish a fixed warm-network amount from mixed RVO cached surfaces; official search results currently show conflicting figures.
- Do not freeze complete per-m² or product tables into site copy. Use current RVO live lists/calculator.
- Local schemes require location-specific current verification.

## Gate

- [x] Current SERP inspected
- [x] Primary official RVO/Rijksoverheid sources inspected
- [x] MUST items explicit
- [x] Cannibalisation boundary explicit
- [x] Volatile/contradictory amount handled as a data-risk rather than guessed
- [x] Ready for v2 brief and production