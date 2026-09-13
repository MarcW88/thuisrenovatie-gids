# Brief v2 - Huis renoveren

- Route: `/renovatie-plannen/huis-renoveren/`
- Status: QA_IN_PROGRESS
- Market: Nederland
- Primary query: `huis renoveren`
- Reader task: begrijpen waar een woningrenovatie begint en welke beslissingen vóór uitvoering vast moeten staan.
- Decision: DEEP_REWRITE
- Last researched: 2026-09-13

## Intent and role

Broad planning pillar. Answer "waar begin ik?" early, then move from technical state to scope, dependencies, rules, cost/budget, comparable offers, work order and handover. Do not duplicate the detailed physical work order or project lifecycle pages.

## Evidence

- Rijksoverheid / Omgevingsloket for permit and notification checks.
- Cost figures belong on `/renovatiekosten/`; summarize and hand off rather than duplicate tables.
- Safety claims must preserve escalation for structure, foundation, gas, electricity and asbestos.

## Architecture rationale

A sequential homeowner decision path is justified by the query. It is not the cluster template. Use mostly prose and only one compact start check when it improves actionability.

## Boundaries

- `/renovatie-volgorde/`: physical order of works.
- `/renovatiefasen/`: project lifecycle and decision gates.
- `/complete-renovatie/`: multi-system whole-house coordination.
- `/renovatiekosten/`: current market price benchmarks.

## Internal next steps

Link only where the next question naturally becomes order, phases, costs, budget, permits or offers.
