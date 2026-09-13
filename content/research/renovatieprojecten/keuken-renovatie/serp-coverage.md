# SERP coverage — Keuken renovatie

- Route: `/renovatieprojecten/keuken-renovatie/`
- Market: Nederland
- Language: nl-NL
- Reviewed: 2026-09-13
- Workflow: renovation-analysis-workflow v2
- Decision: `DEEP_REWRITE`

## 1. Query set

### Primary
- keuken renovatie
- keuken renoveren
- keuken verbouwen

### Close variants
- nieuwe keuken waar beginnen
- keuken renovatie kosten
- keuken verbouwen kosten
- keuken renovatie stappenplan
- keuken vervangen of renoveren

### Sub-intents
- bestaande keuken behouden of volledig vervangen
- indeling en maatvoering bepalen
- leidingen / afvoer verplaatsen
- inductie / elektra / meterkast voorbereiden
- afzuiging / ventilatie kiezen
- keukenprijs versus bouwkundige voorbereiding begrijpen
- weten wanneer bestellen verantwoord is
- leverancier, aannemer en installateur op dezelfde scope krijgen
- offertes kunnen vergelijken

## 2. Current SERP inspected

### Vereniging Eigen Huis — `Wat kost verbouwen?`
Type: independent cost benchmark.

Observed:
- price level 2026;
- kitchen price ranges by segment;
- separate figures for demolition, moving water/electrics and extending the meter cupboard;
- explicit note that real costs vary with region, site conditions and market conditions;
- kitchen product price drivers: brand, size, equipment, worktop, montage and additional building work.

Useful verified 2026 data:
- budget kitchen incl. montage: €3,990–€6,670;
- normal kitchen: €6,670–€14,475;
- luxury kitchen incl. montage: €14,475–€21,000;
- super-luxury kitchen incl. montage: €20,475–€30,600;
- demolition by professional: €395–€1,340;
- moving water and electrics: €710–€1,050;
- extending meter cupboard: €395–€815.

Important scope note: the page describes these as market guide prices, not a universal project total.

### Milieu Centraal — `Nieuwe keuken`
Type: independent technical / sustainability guidance.

Observed:
- partially refurbishing can be preferable to total replacement when the base remains usable;
- a kitchen renovation is a logical moment to move to induction;
- induction may require an extra cable and usually additional groups in the meter cupboard; grid connection reinforcement may also be necessary;
- if the meter cupboard is being changed, future electricity demand for heat pump / solar can be anticipated;
- check ventilation early; extraction to outside is more effective than recirculation at removing cooking moisture;
- apartment buildings with shared mechanical exhaust may require a motorless hood and expert check;
- keep hot-water route short where possible;
- future low-temperature heating can be considered during the renovation.

### Consumentenbond — `Keuken of badkamer kopen: onderhandelen met de verkoper`
Type: purchase / consumer decision guidance. Updated 14 April 2026.

Observed:
- prepare wishes and measure the room before visiting the showroom;
- decide a maximum spend before negotiation;
- insist on a specified quotation;
- price, equipment brand/type and installation costs should be visible;
- compare final amounts, not discount percentages;
- do not let same-day sales pressure replace comparison.

### vtwonen — `Stap voor stap: de keuken verbouwen`
Type: renovation process guide.

Observed:
- design/indeling first;
- changed layout implies moving utilities/electrical points;
- accurate measurement before product selection;
- technical work after demolition and before walls/floors/installation;
- then room preparation and kitchen installation.

### Werkspot / commercial cost pages
Type: broad cost and inspiration guides.

Observed recurring pattern:
- front refresh vs complete renovation;
- average cost ranges or €/m²;
- equipment, worktop, cabinets and labour as main cost drivers;
- generic planning / contractor CTA.

Weakness: scope definitions vary strongly, so raw price ranges are hard to compare.

## 3. Dominant SERP format and reader expectation

Dominant format is a hybrid of:
1. orientation / steps;
2. price guidance;
3. product / showroom preparation;
4. practical installation considerations.

A page that only explains design or only gives a price range is incomplete for the broader `keuken renovatie` intent.

The reader needs an answer to two different questions:
- `Welke keuken wil ik?`
- `Is mijn woning en voorbereiding klaar voor die keuken?`

The second question is underdeveloped across much of the SERP and is the best information-gain opportunity.

## 4. Current page audit

Strong elements to preserve:
- scope-first lead;
- partial refresh vs total renewal distinction;
- early focus on water, drainage, electrics, ventilation and meter cupboard;
- separation between kitchen product and building preparation;
- responsibility / measurement concept;
- quote comparison CTA after scope work;
- safety boundary for gas, meter cupboard and structural changes.

Weaknesses:
- no current 2026 independent price benchmark despite strong cost intent;
- page does not define a clear `bestelgate` before the kitchen is ordered;
- measurement responsibility is mentioned but not turned into an actionable handoff between supplier and contractor;
- no explicit split between supplier drawing and construction/installations drawing;
- quote matrix is too short for the real interface risk;
- no explicit check that extraction choice is compatible with the building / apartment ventilation system;
- future-installation paragraph is broad and risks becoming generic sustainability copy;
- structure still resembles the previous bathroom page too closely (scope → six decisions → costs → quote matrix).

## 5. Coverage matrix

| Reader need | Current | Priority | Notes |
|---|---|---|---|
| Decide refurbish vs replace | COVERED | MUST | Preserve, but make the decision more concrete. |
| Define how the kitchen is used before styling | PARTIAL | MUST | Needs daily-use / storage / work-zone logic, not trend content. |
| Fix layout before technical preparation | COVERED | MUST | Preserve. |
| Confirm actual room dimensions before order | PARTIAL | MUST | Upgrade to order gate + measurement responsibility. |
| Translate appliance plan into electrical load / meter-cupboard check | PARTIAL | MUST | Milieu Centraal supports this strongly for induction. |
| Fix water, drainage and hot-water route before finish/order | PARTIAL | MUST | Needs clearer interface logic. |
| Choose extraction compatible with dwelling ventilation | PARTIAL | MUST | Include apartment/shared-channel exception. |
| Distinguish product price from building/installations prep | COVERED | MUST | Keep and deepen. |
| Give current price context with scope | MISSING | MUST | Use VEH price-level 2026, with scope and separate prep items. |
| Define when it is safe to place the final order | MISSING | MUST | Core information gain. |
| Clarify supplier vs contractor responsibility | PARTIAL | MUST | Needs handoff matrix. |
| Compare specified quotations | PARTIAL | MUST | Consumentenbond supports itemised quote requirement. |
| Explain sequencing dependencies | PARTIAL | SHOULD | No universal week count. |
| Reuse / partial renovation | COVERED | SHOULD | Preserve with Milieu Centraal support. |
| Future electrification readiness | PARTIAL | SHOULD | Keep only concrete electricity/low-temp heating implications. |
| Universal permit verdict | MISSING | OPTIONAL / EXCLUDE | Only relevant if structural / external / other regulated work; route to permit page if needed. |

## 6. Information gain selected

### A. `Bestelgate`
Do not order the final kitchen until all of these are sufficiently fixed:
- verified room dimensions;
- final cabinet/appliance layout;
- water and drainage positions;
- electrical loads, groups and connection requirements;
- extraction / ventilation route;
- finished floor level and wall build-up where these affect dimensions;
- responsibility for final measurement and discrepancies;
- construction changes that affect the room.

This is not presented as a legal checklist. It is a project-control gate.

### B. Two drawings, not one
Distinguish:
- `keukentekening`: cabinets, appliances, worktop, visible dimensions;
- `voorbereidingstekening`: water, drainage, electrics, ventilation/extraction, finished floor/wall levels, service clearances.

The two must describe the same final kitchen before order and execution.

### C. Scope-normalised 2026 price benchmark
Use VEH 2026 ranges for the kitchen itself and separate prep items. Explicitly avoid adding these mechanically into a single “average total” because project scope varies.

### D. Responsibility handoff
For each interface, state who measures / designs / prepares / supplies / connects / signs off. This is especially valuable where kitchen retailer and renovation contractor are different parties.

## 7. GEO / citation opportunities

Useful atomic facts:
- VEH price-level 2026 ranges and separate prep-item ranges;
- Milieu Centraal: induction often means additional groups/cable and possibly grid-connection changes;
- Milieu Centraal: extraction to outside removes moisture more effectively than recirculation;
- apartment shared mechanical exhaust can change which cooker hood is suitable;
- Consumentenbond: request a specified quotation with equipment and installation costs visible.

Useful extractable distinctions:
- `keukentekening` vs `voorbereidingstekening`;
- `keukenprijs` vs `voorbereidingskosten`;
- `ontwerp klaar` vs `bestelklaar`.

## 8. Cannibalisation / ownership

### `/renovatieprojecten/badkamer-renovatie/`
Overlap: wet-room project, hidden systems, quote readiness.
Boundary: bathroom owns water-management / moisture / close-up gate; kitchen owns order gate, supplier-contractor handoff, appliance loads and extraction compatibility.

### `/renovatie-plannen/renovatiekosten/`
Owns cross-project market pricing methodology. Kitchen page may show a project-specific benchmark only.

### `/renovatie-plannen/renovatie-budget/`
Owns project financial control and reserve. Kitchen page only identifies cost layers.

### `/vakman-en-offertes/offertes-vergelijken/`
Owns general quote comparison. Kitchen page defines kitchen-specific scope lines required before using that general method.

### `/verduurzamen/energie-besparen/`
Owns broad energy sequence. Kitchen page only covers decisions directly triggered by the kitchen renovation.

## 9. Data gaps and exclusions

- No universal duration in weeks. Depends on delivery, demolition, preparation, drying/finishing and installation scope.
- No generic “permit needed / not needed” statement. Structural or other regulated work routes to the permit page.
- No detailed electrical design, group sizing or DIY wiring instructions.
- No universal cooker-hood rule for every apartment system.
- No unsupported ROI / property-value claim for a new kitchen.

## 10. Analysis decision

**DEEP_REWRITE**

Reason: the current page has a solid scope-first base but lacks three central assets required for a stronger 2026 answer: a scoped independent cost benchmark, a real order-readiness gate, and a supplier/contractor handoff model. It also remains structurally too similar to the former bathroom page. The rewrite should preserve the existing technical-first thesis while rebuilding the architecture around `ontwerp → bestelgate → voorbereiding → prijs/scope → offerte/handoff`.
