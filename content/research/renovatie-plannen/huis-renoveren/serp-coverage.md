# SERP coverage matrix — Huis renoveren

- Route: `/renovatie-plannen/huis-renoveren/`
- Workflow: `renovation-analysis-workflow` v2
- Decision: `DEEP_REWRITE`
- Market: Netherlands / nl-NL
- Researched: 2026-09-13
- Primary query: `huis renoveren`
- Close variants inspected: `huis verbouwen waar beginnen`, `huis renoveren stappenplan`, `woning renoveren stappenplan`, `huis verbouwen budget vergunning aannemer`

## 1. Search intent and ownership

Dominant intent is broad informational planning: the reader wants to know where a renovation starts, what must be clarified before work begins, and what decisions prevent expensive rework. Current SERPs often satisfy this with a generic chronological `stappenplan`.

That format is already owned internally by `/renovatie-plannen/renovatiefasen/` for the project lifecycle and `/renovatie-plannen/renovatie-volgorde/` for the physical order of work. Repeating the same lifecycle on `/huis-renoveren/` creates internal cannibalisation even if the wording differs.

**Ownership for this URL:** answer the pre-planning question: *what kind of renovation do I actually have, what must I investigate or decide first, and when am I ready to plan or request comparable quotes?*

This page should function as an orientation / decision page, not as another generic step-by-step lifecycle.

## 2. SERP pages inspected

| Source | Page type / angle | What it covers well | What not to copy |
|---|---|---|---|
| Homedeal — `https://www.homedeal.nl/verbouwing/huis-verbouwen-stappenplan/` (14 Jul 2026) | Generic chronological stappenplan | goals, budget/financing, quotes, permits, schedule, work, handover | A second lifecycle page would collide with our `renovatiefasen` URL |
| Homedeal — `https://www.homedeal.nl/verbouwing/huis-verbouwen/` (13 Jul 2026) | Broad renovation guide | reasons, where to start, costs, mistakes, contractor lead | Commercial breadth without a strong decision framework |
| De Huisgids — `https://dehuisgids.nl/verbouwen/verbouwing-plannen/huis-verbouwen/` (checked Aug 2026) | Practical planning guide | must-vs-want distinction, budget ceiling, renovation depth, dependency logic, one shared work description | Do not mirror its sequence or wording; use the underlying decision problems |
| Bouwbedrijf DLN — `https://bouwbedrijfdln.nl/kennis/huis-renoveren-stappenplan` (May 2026) | Technical renovation plan | safety / structure / moisture before finish, scope, work order | Detailed work order belongs primarily to our `renovatie-volgorde` page |
| vtwonen — `https://www.vtwonen.nl/verbouwen/beste-volgorde-voor-verbouwing~3ccfc6a2` (16 Mar 2026) | Physical work order | what comes before what in execution | This confirms separate ownership for `/renovatie-volgorde/` |
| Nationale-Nederlanden — `https://www.nn.nl/Inspiratie/Wat-kost-een-verbouwing.htm` (1 Jul 2026) | Cost / budget guidance | clarify scope, obtain multiple quotes, 10–20% buffer guidance, 2026 price context | Detailed price tables belong to `/renovatiekosten/` and budget method to `/renovatie-budget/` |
| Vereniging Eigen Huis — `https://www.eigenhuis.nl/huis-verbeteren/verbouwen/wat-kost-verbouwen` (2026 price level) | Cost guidance | detailed plan, realistic cost picture, compare quotes | Do not turn this page into the cost page |
| Omgevingsloket — `https://omgevingswet.overheid.nl/checken` | Official permit check | location/activity-specific check for permit / notification requirements | Never state a universal permit rule from memory |

## 3. Recurring needs in the SERP

1. Where do I start?
2. What must be fixed before cosmetic wishes?
3. How large / invasive is my renovation really?
4. Which decisions affect many other works?
5. How much budget can I spend, and how is that different from a cost estimate?
6. When do I need technical investigation or a specialist?
7. Which permits / formal checks may affect the plan?
8. When is my scope clear enough to request comparable quotes?
9. In what order do works happen?
10. What happens from planning to handover?

Items 9 and 10 are real user needs but belong primarily to `/renovatie-volgorde/` and `/renovatiefasen/`, not to this page.

## 4. Coverage matrix

| Need | Priority | Current page | Target after rewrite | Ownership / note |
|---|---|---:|---:|---|
| Direct answer to “where do I start?” | MUST | COVERED | COVERED | Keep, but answer with diagnosis + decisions rather than a lifecycle |
| Separate technical necessity from wishes | MUST | COVERED | COVERED | Strong existing value to preserve |
| Classify renovation depth / complexity | MUST | PARTIAL | COVERED | Add a practical three-level orientation, explicitly editorial rather than legal taxonomy |
| Identify high-impact / hard-to-reverse decisions | MUST | COVERED | COVERED | Preserve and deepen into a dependency test |
| Know when specialist investigation comes before planning | MUST | PARTIAL | COVERED | Add explicit stop conditions for structure/foundation, persistent moisture, gas/electricity, asbestos suspicion |
| Know what must be clear before requesting quotes | MUST | PARTIAL | COVERED | Define a minimum viable renovation brief / scope |
| Permit / formal check | MUST | COVERED | COVERED | Keep concise + official Omgevingsloket handoff |
| Budget ceiling versus cost estimate | MUST | PARTIAL | COVERED | Correct current “cost picture first, budget second” overstatement |
| Current detailed costs | SHOULD | PARTIAL | HANDOFF | Summary only; detailed values belong to `/renovatiekosten/` |
| Compare contractor quotes | SHOULD | PARTIAL | HANDOFF | Define readiness, then route to `offertes-vergelijken` |
| Contract / payment / guarantees | SHOULD | MISSING | HANDOFF | Belongs mainly to `vakman-en-offertes`; do not bloat this page |
| Physical work order | MUST in journey | TOO MUCH | HANDOFF | Route to `/renovatie-volgorde/` |
| Project lifecycle / phases | MUST in journey | TOO MUCH | HANDOFF | Route to `/renovatiefasen/` |
| Whole-house coordination | SHOULD | PARTIAL | HANDOFF | Route to `/complete-renovatie/` |
| “What do I not need to decide yet?” | SHOULD | MISSING | COVERED | Useful information gain: prevent premature finish/product decisions |
| A practical readiness check before planning / quotes | MUST | PARTIAL | COVERED | Turn existing startcheck into stronger decision asset |

## 5. Information gain opportunities

### A. Renovatie-startscan
Create a short decision framework that checks five things before planning:

1. **State:** is the home safe, stable and dry enough to plan from?
2. **Change:** cosmetic, functional/layout, or system-wide renovation?
3. **Dependencies:** which decisions alter structure, routes, floor build-up, ventilation, heating or fixed dimensions?
4. **Uncertainty:** which unknown can invalidate design, price or planning?
5. **Readiness:** is the scope clear enough for permits, cost estimate or quotes?

This is more useful than another seven- or eight-step chronology and differentiates the page from internal neighbours.

### B. Minimum viable renovation brief
Before comparing quotes, the homeowner should be able to state at least:

- what stays and what changes;
- which technical uncertainties remain;
- whether layout/structure/installations are affected;
- the desired functional/performance outcome;
- the budget ceiling and which items are optional;
- which responsibilities are expected from the contractor versus owner.

This can become a reusable decision asset for SEO, lead readiness and GEO extraction.

### C. “Not yet” decisions
Explain which finish choices can usually wait, unless they affect dimensions, technical routes, floor build-up, lead time or installation requirements. This reduces premature detail and gives the page a distinct planning perspective.

## 6. GEO / citation opportunities

- Open with a concise, extractable answer to where renovation planning starts.
- Use atomic distinctions: `budgetplafond` vs `begroting`, `projectfasen` vs `werkvolgorde`, `wens` vs `technische noodzaak`.
- Keep official permit source adjacent to the claim.
- Keep NN 2026 buffer guidance only as supporting context, with date/source and handoff to the dedicated budget page.
- Present the startscan as an editorial framework, not an external standard or invented methodology.
- Do not manufacture FAQ or duplicate the same answer in snippet blocks.

## 7. Cannibalisation / internal ownership

### `/renovatie-plannen/huis-renoveren/`
Owns: first diagnosis and decision readiness — *where do I start and what must be known before I can plan properly?*

### `/renovatie-plannen/renovatiefasen/`
Owns: project lifecycle — *which phases does the renovation project go through from inventory to handover?*

### `/renovatie-plannen/renovatie-volgorde/`
Owns: physical execution order — *which works happen before which other works?*

### `/renovatie-plannen/complete-renovatie/`
Owns: coordination when many building systems and disciplines interact.

### `/renovatie-plannen/renovatiekosten/`
Owns: current price benchmarks and cost drivers.

### `/renovatie-plannen/renovatie-budget/`
Owns: financial allocation, buffers and budget control.

## 8. Data gaps

- No Search Console query/impression data is available for this new/noindex site; intent is therefore based on current SERP inspection rather than actual ranking/query history.
- No Ahrefs/Semrush backlink or keyword-overlap export was available in this run, so the `seo-competitor` backlink and authority angles are not scored. This does not block the content-depth / SERP decision but must not be represented as completed.
- No direct cross-engine AI citation test (ChatGPT Search, Gemini, Perplexity, AI Overviews) was available in this run. GEO recommendations are therefore structural/citation-worthiness recommendations, not measured visibility claims.

## 9. Handoff decision

`DEEP_REWRITE` can proceed.

Blocking gaps: none for the content rewrite.

The rewrite must **not** use a generic chronological stappenplan as its architecture. It must preserve the existing must-vs-want and dependency reasoning, add the startscan + minimum viable renovation brief, distinguish budget ceiling from estimate, and hand off lifecycle/work-order detail to their owner URLs.
