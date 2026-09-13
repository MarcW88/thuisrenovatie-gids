# Post-write gap check — Badkamer renovatie

- Route: `/renovatieprojecten/badkamer-renovatie/`
- Workflow version: 2
- Checked: 2026-09-13
- Decision before writing: `DEEP_REWRITE`

## MUST coverage

| Requirement | Status | Where covered | Evidence / rationale |
|---|---|---|---|
| Three levels of bathroom scope based on what changes behind the finish | COVERED | `Hoe ingrijpend is je badkamerrenovatie?` | `Opfrissen`, `Technisch vernieuwen`, `Herindelen` are separated by hidden technical scope rather than luxury level. |
| Explain consequences of changing layout, water and drainage | COVERED | Scope table + `Wat moet achter de tegel al vaststaan?` | Layout, measurement, water and drainage are explicitly linked to routes, floor/wall build-up and montage. |
| Treat substrate + water management/waterproofing as technical scope, not a tile choice | COVERED | `Techniekkaart` + `Dichtmaak-gate` + quote matrix | The page requires the underlying build-up, wet zones, joints/penetrations and responsibility to be specified without publishing a universal DIY recipe. |
| Treat wet-room electrical work as safety-sensitive; NEN 1010 only at verified high level | COVERED | NEN source box + techniekkaart | NEN 1010 claim is limited to new/modified/extended low-voltage installations. No invented zone distances or IP ratings. |
| Ventilation is a pre-close/pre-finish decision | COVERED | Techniekkaart + dichtmaak-gate + Milieu Centraal source box | Ventilation is resolved before closing and is tied to moisture control, with current source adjacent. |
| Current VEH price level 2026 benchmark with scope and demolition exclusion | COVERED | `Wat kost een badkamerrenovatie in 2026?` | All six VEH values are present with room size, finish level, incl. VAT/montage and explicit demolition exclusion. |
| Explain why market ranges cannot be blended blindly | COVERED | Price intro + `Waar ontstaan de grootste prijsverschillen?` | Benchmark is framed as scope-dependent; visible products and hidden/building scope are separated. No fake national average or €/m² figure. |
| Bathroom-specific offer comparison scope | COVERED | `Wat moet in een badkamer-offerte staan?` | Covers demolition/disposal, substrate/repair, water/drainage, electrical/heating, ventilation, water management, sanitary/finishing, planning/morework/handover. |
| Clear `dichtmaak-gate` before walls/floor/tiling close hidden work | COVERED | `De dichtmaak-gate` | Six pre-close checks plus escalation for unexplained moisture/hidden defects. |

**MUST result: 9 COVERED / 0 PARTIAL / 0 MISSING.**

## SHOULD coverage

| Requirement | Status | Where covered | Rationale |
|---|---|---|---|
| Planning dependencies rather than universal duration | COVERED | `Hoe plan je de doorlooptijd zonder een fictief aantal weken?` | Page explicitly avoids one week-range and compares blockers/handoffs. |
| Water/energy-saving opportunities only after core technical scope | COVERED | `Wat kun je slim meenemen nu de badkamer toch openligt?` | Milieu Centraal options are secondary and conditional. |
| Future use/accessibility as a design question, without universal spec | PARTIAL | Scope/maatvoering model | Page makes layout and actual dimensions an early decision but does not add generic accessibility dimensions. This remains intentionally light because no verified, intent-central accessibility standard was required by the SERP research. |
| Regulatory escalation only when relevant | COVERED | Final note | Structural/regulated work routes to the permit page/Omgevingsloket; ordinary bathroom replacement gets no universal permit verdict. |

## Information gain survival

- **3-level badkamerscope:** present and central.
- **Techniekkaart achter de tegel:** present as a six-interface comparison table.
- **Dichtmaak-gate:** present as an explicit project stop point.
- **Scoped 2026 benchmark:** present with exact VEH scope/exclusions.
- **Offerte-scopekaart:** present and bathroom-specific.

## GEO / citation-worthiness check

COVERED:
- direct answer near page start;
- extractable definition of the three renovation scopes;
- atomic NEN 1010 high-level statement with direct source;
- extractable 2026 VEH price table with methodology boundaries;
- Milieu Centraal ventilation/moisture statement adjacent to source;
- Consumentenbond specified-offer guidance adjacent to source;
- no artificial FAQ block or repeated snippet bait.

## Cannibalization / page-role check

- Does not duplicate `/renovatie-plannen/renovatiekosten/`: this page owns bathroom-specific benchmark + technical scope; planning page owns cross-project normalization.
- Does not duplicate `/renovatie-plannen/renovatie-budget/`: no reserve/reforecast system here.
- Does not duplicate `/verduurzamen/ventilatie/`: ventilation is a gate, not a system-selection guide.
- Does not duplicate `/problemen-oplossen/vochtproblemen/`: unexplained moisture is routed there instead of diagnosed here.
- Materially distinct from `keuken-renovatie`: bathroom architecture is built around wet-room hidden layers, water management and a close-before-finishing gate rather than ordering a fitted product after service preparation.

## Editorial passes

- Brand voice: applied before copy and rechecked after factual changes.
- `content-and-copy`: substance/structure pass applied.
- `fact-check`: PASS, persisted separately.
- `seo-aeo-geo`: extractability and source adjacency applied after fact verification.
- `humanizer`: applied to complete visible copy; em-dash source labels and mechanical binary phrasing removed.
- `general-writing`: clarity/directness pass applied; technical distinctions preserved.
- `anti-ai-slop`: reviewed for templating, generic filler and cloned structure; no blocking pattern remains.
- `seo-onpage`: title/meta/header/intent/internal-link pass applied.
- `editorial-qa`: brief adherence, voice, factuality, structure and AI-smell checks applied.

## Final post-write result

**PASS for post-write coverage.**

No `MUST = MISSING` or `MUST = PARTIAL`. The one partial SHOULD is deliberately bounded and does not block the page's core search task, safety, factuality or conversion logic.
