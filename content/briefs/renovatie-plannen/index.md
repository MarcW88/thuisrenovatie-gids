# Brief v2 — Renovatie plannen hub

- Route: `/renovatie-plannen/`
- Workflow version: 2
- Status: QA_COMPLETE
- Market: Netherlands / nl-NL
- Decision: `DEEP_REWRITE`
- Primary query: `renovatie plannen`
- Secondary queries: `verbouwing plannen`, `huis verbouwen plannen`, `verbouwing checklist`, `renovatie planning maken`
- Reader task: identify which planning uncertainty is blocking the renovation and move to the page that owns that decision.
- Research artifact: `content/research/renovatie-plannen/serp-coverage.md`
- Last researched: 2026-09-13

## Search intent and ownership

The SERP mixes broad checklists, linear stappenplannen and planning tools. This hub must not compete by publishing another complete stappenplan. Its role is to make the cluster understandable and actionable.

Ownership statement:

> `/renovatie-plannen/` is the decision router for renovation planning. It helps the reader identify the next unresolved decision and routes to the specialist page. It does not own the full lifecycle, physical work order, cost table, budget system, permit framework or subsidy rules.

## Required page assets

### 1. Direct answer
Open by saying that a renovation plan usually stalls because one of a small number of decisions is still unclear: scope, technical uncertainty, order, cost, budget, rules, coordination or return.

### 2. Decision map covering every child route
Each child page must have one clear question:

- `/huis-renoveren/` — where do I start and what must I investigate/decide first?
- `/renovatiefasen/` — which project phase am I in and what must be completed before the next?
- `/renovatie-volgorde/` — which physical work depends on which other work?
- `/complete-renovatie/` — when must several building systems be designed/coordinated together?
- `/renovatiekosten/` — what do comparable renovation scopes cost in the market?
- `/renovatie-budget/` — how much can I spend and how do I keep control as costs change?
- `/renovatievergunning/` — what must I check before design/orders become definitive?
- `/subsidies-renovatie/` — which current support may apply and what evidence/conditions matter?
- `/rendement-renovatie/` — how do I compare value, savings, avoided costs and use value?

### 3. Confusion pairs
Explicitly separate:

- **Renovatiefasen vs renovatievolgorde** — project handoffs vs physical dependencies.
- **Renovatiekosten vs renovatiebudget** — external price benchmark vs internal spending control.
- **Huis renoveren vs complete renovatie** — broad start/orientation vs integrated multi-system coordination.

### 4. Ready-for-offers gate
Before serious quote comparison, the hub may state that these four things should be sufficiently clear:
- scope;
- major technical unknowns / blockers;
- relevant regulatory uncertainty;
- budget ceiling.

Do not duplicate the detailed quote-comparison workflow; link to `/vakman-en-offertes/offertes-vergelijken/`.

### 5. “Do not solve everything now” guidance
The page should reduce anxiety and overplanning. It should explain that not every finish/product needs to be final before planning starts; only decisions that change scope, dependencies, permissions or budget need to be stabilised early.

## Content boundaries

Do not:
- publish a numbered full-project stappenplan;
- copy price tables;
- copy ISDE amounts;
- reproduce the permit framework;
- explain detailed contractor selection;
- turn the hub into a generic long-form article.

## Brand voice

Practical, calm and decisive. The hub should feel like a map, not a lecture. Short explanatory paragraphs and useful link cards are preferred over encyclopaedic prose.

Avoid repetitive “eerst X, dan Y” cadence. Use clear contrasts only when they genuinely resolve ambiguity.

## GEO / extractability

Create short atomic definitions for the main confusion pairs. The most useful extractable unit is the cluster map itself: one question, one owner URL.

No artificial FAQ required.

## Internal linking requirements

Must link to all nine child routes and to `/vakman-en-offertes/offertes-vergelijken/` once at the readiness gate.

## QA completion criteria

- Every MUST from the SERP matrix is visibly covered.
- Hub does not reproduce child-page depth.
- Every child route has a distinct one-sentence ownership statement.
- No volatile fact requires separate fact-checking in the hub body.
- Post-write gap check passes with no `MUST = MISSING` or `PARTIAL`.