# Brief v2 - Renovatiebudget

- Route: `/renovatie-plannen/renovatie-budget/`
- Status: QA_IN_PROGRESS
- Primary query: `renovatie budget` / `verbouwing budget maken`
- Reader task: turn available money and market costs into a controllable project budget.
- Decision: DEEP_REWRITE
- Last researched: 2026-09-13

## Method

Separate maximum financial room from fixed scope, optional choices, project overhead and contingency. Rebudget after technical inventory, after design/offers and before contract.

## Evidence

Consumer guidance commonly recommends a practical contingency rather than zero buffer. Current NN guidance suggests roughly 10-20%; Funda has advised 10-15%. Present as guidance, never a universal technical norm.

## Example

An illustrative EUR 80,000 split is allowed only when clearly labelled a worked example, not a recommended allocation.

## Boundary

Do not duplicate current market prices from `/renovatiekosten/`. Link to it, then focus on allocation, control and trade-offs.
