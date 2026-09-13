# Content brief v2 — Huis renoveren

- `workflow_version: 2`
- Route: `/renovatie-plannen/huis-renoveren/`
- Status: `BRIEF_READY`
- Market: Netherlands / nl-NL
- Decision: `DEEP_REWRITE`
- Research artifact: `content/research/renovatie-plannen/huis-renoveren/serp-coverage.md`
- Last researched: 2026-09-13

## 1. Target keyword + supporting cluster

**Primary:** `huis renoveren`

Supporting query space:

- `huis verbouwen waar beginnen`
- `huis renoveren waar beginnen`
- `woning renoveren`
- `renovatie plannen`
- `huis verbouwen voorbereiden`

Do not optimize this page as another `renovatie stappenplan`; `/renovatiefasen/` owns the project lifecycle and `/renovatie-volgorde/` owns the physical work order.

## 2. Search intent / dominant format

Informational, broad planning/orientation. The current SERP commonly uses long-form guides and chronological step plans, but matching that format literally would create internal cannibalisation.

The page should satisfy the same broad need with a stronger **pre-planning decision framework**: determine what kind of renovation the reader has, which unknowns can invalidate the plan, what must be decided before pricing/planning, and where the next specialist page takes over.

## 3. Target audience

Dutch homeowner in the orientation or early planning phase. They may have a list of wishes but do not yet know whether their project is cosmetic, technically interconnected or risky enough to need investigation before design and quotes.

Assume no construction education. Do not hide complexity behind jargon.

## 4. Job to be done

> Help me turn a vague intention to renovate my house into a sufficiently clear starting position, so I know what must be investigated or decided before I spend money on design, quotes, materials or execution.

## 5. Depth target

Broad pillar-level orientation, but **not** comprehensive duplication of every supporting page. Depth is sufficient when every MUST from the SERP matrix is resolved and the reader can route themselves to the next correct step.

No word-count target.

## 6. Thesis / information gain

A renovation should not start with a generic sequence of works. It starts by separating **technical necessity, desired change and dependencies**. The page should introduce two useful editorial assets:

1. **Renovatie-startscan** — state, depth of change, dependencies, unknowns, readiness.
2. **Minimum viable renovatieplan** — the information that must be clear before comparing serious quotes or fixing a schedule.

Also explain what the reader **does not need to decide yet**, to avoid premature finish/product choices.

These are editorial frameworks from Thuisrenovatie Gids, not legal or industry standards.

## 7. Required coverage — MUST

- Answer `waar begin je?` immediately.
- Preserve the distinction `moeten vs willen`.
- Classify renovation depth in a practical, non-legal way: cosmetic / targeted functional renovation / interconnected or major renovation.
- Explain high-impact, hard-to-reverse decisions: layout, structural openings, kitchen/bathroom positions, major routes, heating/ventilation, floor build-up, insulation interactions.
- Explicit stop conditions before planning: signs of structural/foundation issues, persistent moisture with unknown cause, risky electrical/gas questions, suspected asbestos or other hazardous material.
- Explain what must be clear before requesting comparable quotes.
- Keep permit/formal checks concise and route to the official Omgevingsloket.
- Distinguish **budget ceiling** from **cost estimate / begroting**.
- Route physical order to `/renovatie-volgorde/` and project lifecycle to `/renovatiefasen/` rather than reproducing them.

## 8. SHOULD coverage

- Mention that current 2026 budget guidance from Nationale-Nederlanden recommends a 10–20% buffer for unexpected costs, but keep the method/detail on `/renovatie-budget/`.
- Explain which decisions can usually wait: colors, finishes and products that do not affect dimensions, technical routes, floor build-up, lead time or installation requirements.
- Make quote readiness tangible: same scope, same responsibilities, same performance/finish assumptions.
- Link to `/complete-renovatie/` when multiple systems/disciplines interact strongly.

## 9. Required entities / proof

- **Omgevingsloket / Vergunningscheck** — official source for activity/location-specific permit or notification checks: `https://omgevingswet.overheid.nl/checken`.
- **Nationale-Nederlanden, “Wat kost een verbouwing?”**, updated 1 July 2026 — supports 10–20% contingency guidance and the logic of defining scope before collecting quotes: `https://www.nn.nl/Inspiratie/Wat-kost-een-verbouwing.htm`.
- **Vereniging Eigen Huis, “Wat kost verbouwen?”** — current 2026 price context belongs mainly on the dedicated cost page: `https://www.eigenhuis.nl/huis-verbeteren/verbouwen/wat-kost-verbouwen`.

Do not introduce unsupported national averages, project durations or universal permit rules.

## 10. Proposed page architecture

Structure follows the reader's diagnosis, **not a numbered lifecycle**.

1. Direct answer: renovation begins with state + desired end state + dependencies.
2. `Welke renovatie heb je eigenlijk?` — practical three-level classification.
3. `Doe eerst de renovatie-startscan` — five diagnostic dimensions with consequences.
4. `Wanneer moet je stoppen en eerst laten onderzoeken?` — safety/unknowns.
5. `Wat moet vaststaan vóór je offertes of planning serieus maakt?` — minimum viable renovation plan.
6. `Budgetplafond en begroting zijn niet hetzelfde` — early financial constraint vs later market estimate; brief NN buffer context.
7. `Wat hoef je nog niet te beslissen?` — delay reversible finish decisions.
8. `Welke vervolgstap hoort bij jouw vraag?` — route explicitly to order, phases, complete renovation, costs/budget, permit and quotes.

A compact table is justified for the startscan or final routing. Avoid two near-identical tables.

## 11. Internal linking strategy

Outbound from this page:

- `/renovatie-plannen/renovatie-volgorde/` — anchor around physical work order.
- `/renovatie-plannen/renovatiefasen/` — project lifecycle.
- `/renovatie-plannen/complete-renovatie/` — strongly interconnected whole-house scope.
- `/renovatie-plannen/renovatiekosten/` — current 2026 price benchmarks.
- `/renovatie-plannen/renovatie-budget/` — budget method and buffer.
- `/renovatie-plannen/renovatievergunning/` — permit context.
- `/vakman-en-offertes/offertes-vergelijken/` — quote comparison once scope is ready.

Inbound follow-up after human approval: cluster hub should continue to position this page as the first orientation page. Do not add links from `renovatiefasen` or `renovatie-volgorde` merely for quota; add only if the reader genuinely needs to step back to diagnosis.

## 12. Anti-patterns

Do not:

- write `Stap 1 ... Stap 8` again;
- summarize the full physical work order;
- reproduce all project phases;
- turn the page into a cost guide;
- use generic intros such as `Bij een renovatie komt veel kijken`;
- force a FAQ;
- repeat `cruciaal`, `essentieel`, `weloverwogen`, `naadloos`, `optimaal`;
- imply inspection or diagnosis without one;
- push an offerte CTA before quote readiness is established.

## Voice

Use `content/brand/voice.md`.

Practical without simplism; expert without school tone; direct without being blunt; independent without distrust. Safety passages may be more sober and explicit.

## Success criteria

The draft succeeds when:

- every MUST in the research matrix is `COVERED` in the post-write gap check;
- the central answer and architecture can no longer be swapped with `/renovatiefasen/` by changing a few words;
- `renovatie-volgorde` remains the clear owner of physical sequence;
- the page adds a useful startscan / readiness framework rather than becoming a longer generic guide;
- current factual claims are sourced and safety limits remain intact;
- title/meta no longer frame the page as a `stappenplan`.
