# Post-write gap check — keuken renovatie

- Route: `/renovatieprojecten/keuken-renovatie/`
- Decision: `DEEP_REWRITE`
- Workflow version: 2
- Checked: 2026-09-13

## MUST coverage

| MUST from research | Status | Where covered | Evidence / rationale |
|---|---|---|---|
| Decide refresh vs replace vs layout-changing renovation | COVERED | `Renoveren, vervangen of de indeling veranderen?` | Three scope levels make the technical depth visible. |
| Start from daily use before style | COVERED | `Ontwerp eerst hoe je de keuken gebruikt` | Cooking, washing, preparation, storage, appliances, doors and work surface are considered before finishes. |
| Lock layout before technical preparation | COVERED | Intro + design section + bestelgate | Layout is explicitly upstream of water/electrics/extraction preparation. |
| Verify room dimensions and define measurement ownership before order | COVERED | `Wanneer is je keuken bestelklaar?` + responsibility matrix | Final measurement and responsibility for discrepancies are explicit. |
| Translate appliance plan into electrical / meter-cupboard check | COVERED | `Inductie en meterkast` | Milieu Centraal support preserved; no DIY circuit design. |
| Fix water, drainage and hot-water route before finish/order | COVERED | `Water, afvoer en warmwaterroute` + preparation drawing | Positions and route are explicit project interfaces. |
| Check extraction against dwelling ventilation | COVERED | `Afzuiging en woningventilatie` | Outside extraction vs recirculation plus apartment/shared exhaust exception. |
| Separate kitchen product from building/installations prep | COVERED | `Scheid keukenprijs en voorbereiding in je begroting` | Two explicit cost layers. |
| Give current 2026 price context with scope | COVERED | `Wat kost een keukenrenovatie in 2026?` | VEH price-level 2026 ranges + separate demolition / services / meter-cupboard items and scope warning. |
| Define when it is safe to place final order | COVERED | `Wanneer is je keuken bestelklaar?` | Four visible gate conditions plus unresolved-change examples. |
| Clarify supplier vs contractor / installer responsibility | COVERED | `Wie is verantwoordelijk tussen bestelling en montage?` | Seven interface rows from measuring through handover issues. |
| Require specified quotations / comparable final amounts | COVERED | `Wat moet je kunnen vergelijken vóór je akkoord geeft?` | Consumentenbond evidence + renovation-prep scope added. |

**MUST summary: 12 COVERED / 0 PARTIAL / 0 MISSING.**

## SHOULD coverage

| SHOULD | Status | Notes |
|---|---|---|
| Partial reuse / refurbishment | COVERED | Milieu Centraal-supported opening scope. |
| Sequencing dependencies | COVERED | Bestelgate and preparation drawing show when technical prep must precede final order/montage; no unsupported universal timeline. |
| Future electrification readiness | COVERED | Limited to meter-cupboard work / future electric demand, close to Milieu Centraal source. |
| No unsupported universal duration | COVERED | No fixed week count appears. |

## Information gain survived production

- `bestelgate`: **PASS**
- `keukentekening` vs `voorbereidingstekening`: **PASS**
- price anatomy (`keukenproduct` vs preparation): **PASS**
- supplier/contractor responsibility handoff: **PASS**

## GEO / AEO usefulness

- Direct answer appears before first H2: PASS.
- 2026 price facts are atomic, sourced and scoped: PASS.
- Induction / ventilation claims keep conditions next to the facts: PASS.
- `bestelklaar` has an extractable operational definition: PASS.
- No artificial FAQ section: PASS.

## Internal ownership / cannibalisation

- Bathroom page remains moisture / water-management / close-up-gate focused: PASS.
- Kitchen page now owns order-readiness and supplier-contractor handoff: PASS.
- Cross-project cost methodology remains on `/renovatie-plannen/renovatiekosten/`: PASS.
- Budget control remains on `/renovatie-plannen/renovatie-budget/`: PASS.
- General quote methodology remains on `/vakman-en-offertes/offertes-vergelijken/`: PASS.

## Style passes

- Brand voice: PASS. Practical and decision-led; no showroom hype.
- Humanizer: PASS after full-page review; no decorative conclusion, fake insight or uniform numbered cadence.
- General-writing: PASS; point is front-loaded and technical distinctions remain intact.
- Anti-AI-slop: PASS; architecture is purpose-built around ordering/coordination rather than a reusable project template.
- Structural-cloning check against bathroom: PASS.

## Technical / editorial checks

- Source of truth: `content/renovatieprojecten/keuken-renovatie/body.html`.
- Generated route synced: PASS.
- Canonical route unchanged: PASS.
- `noindex,follow` preserved: PASS.
- No global indexing change: PASS.

## Result before PUBLISH_REVIEW

**READY FOR PUBLISH_REVIEW**

No central `MUST` remains partial or missing. No blocking data gap remains.
