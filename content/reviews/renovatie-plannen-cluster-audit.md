# CLUSTER_AUDIT — renovatie-plannen

Date: 2026-09-13
Market: Netherlands / nl-NL
Workflow: `renovation-analysis-workflow / CLUSTER_AUDIT`
Publication state: keep `noindex,follow`

## Cluster job

`/renovatie-plannen/` owns the decisions that come before or across individual renovation projects: where to start, work order, project phases, complete renovation, costs, budget, permits, subsidies and renovation return/value.

The cluster should not become a collection of generic planning articles. Each URL must own a distinct search task and send the reader to the next useful decision.

## Main findings

1. **Structural cloning is high.** Many current pages use the same sequence of kicker → lead → quick answer → card/list/table → link grid/CTA. Reusable visual components are fine, but editorial architecture is too predictable and contributes to AI-slop.
2. **The cluster is often too cautious.** Avoiding invented figures became avoidance of useful figures. Current SERPs for renovation costs and complete renovations expect price indications; the right response is to research and qualify them, not omit them.
3. **Search intent ownership is mostly defensible.** `huis-renoveren`, `renovatie-volgorde` and `renovatiefasen` can coexist if they answer different tasks: overall starting plan, order of physical work, and project lifecycle/decision gates.
4. **GEO value is currently thin.** Many passages are sensible but generic. Pages need more concrete, source-backed statements, examples and distinctions that can be cited or extracted without turning every section into a canned snippet.
5. **Tone is accessible but overly uniform.** The same short-card rhythm, “beslisregel” boxes and symmetric sections make the cluster read as generated. Sentence and section rhythm must vary page by page.

## SERP / evidence signals used

- Broad `huis renoveren` and `verbouwen` results commonly answer: where to start, scope, order, budget/costs, permits, sustainability and execution.
- `renovatie volgorde` / `volgorde verbouwing` results usually give an explicit usable sequence: planning/design → demolition/structure → shell → installations → insulation/closing → finishing/fixtures → handover, with variations by project.
- `renovatiekosten` results strongly expect current price indications and cost drivers. Vereniging Eigen Huis publishes 2026 price ranges for common renovations; commercial SERPs also show broad totals. We can use trustworthy current sources for component-level benchmarks and clearly label broader estimates as indicative.
- `renovatievergunning` intent is primarily “do I need one / how do I check?”. Rijksoverheid directs users to the Omgevingsloket Vergunningscheck and notes that permit-free work still has rules.
- `subsidies renovatie` intent expects actual measures, current 2026 conditions/amounts and where to apply. RVO currently provides an ISDE decision tree, calculator, measure lists and meldcodes; local schemes can be checked through the national/municipal ecosystem.
- `rendement renovatie` has weaker exact-query demand, but the adjacent task “which renovation increases home value / what pays off?” is real. NVM/brainbay published 2026 analysis showing large average value changes for renovated fixer-uppers while stressing property type, size and location effects. This page must avoid universal ROI percentages.

## URL decisions

| Route | Decision | Primary task after revision | Main reason |
|---|---|---|---|
| `/renovatie-plannen/` | LIGHT_UPDATE | route the user to the right planning decision | Useful hub, but current copy repeats the same framework as child pages. |
| `/renovatie-plannen/huis-renoveren/` | DEEP_REWRITE | “I want to renovate my house: where do I start and what must I decide?” | Correct topic, but broad intent is under-covered and the page currently mirrors the cluster template. |
| `/renovatie-plannen/renovatie-volgorde/` | DEEP_REWRITE | “In which order should renovation work happen?” | Current reasoning is good but the SERP expects a concrete sequence readers can use. |
| `/renovatie-plannen/renovatiefasen/` | LIGHT_UPDATE | “What are the phases of a renovation project from preparation to handover?” | Distinct from physical work order; content is useful but needs a less repetitive architecture and sharper phase outputs. |
| `/renovatie-plannen/complete-renovatie/` | DEEP_REWRITE | “What counts as a complete renovation and how do I plan cost, duration and coordination?” | Current page omits two major SERP expectations: realistic cost/time context and a clearer definition/scope. |
| `/renovatie-plannen/renovatiekosten/` | DEEP_REWRITE | “What does renovating a house cost and what changes the price?” | Current page avoids the main intent by refusing useful price benchmarks. |
| `/renovatie-plannen/renovatie-budget/` | DEEP_REWRITE | “How do I build and control a renovation budget?” | Current framework is generic. Needs a usable budget method, example, reserve logic and financing/subsidy handoff. |
| `/renovatie-plannen/renovatievergunning/` | LIGHT_UPDATE | “Do I need a permit and how do I check?” | Core facts are correct; needs earlier direct answer, common trigger examples and stronger official-source hierarchy. |
| `/renovatie-plannen/subsidies-renovatie/` | DEEP_REWRITE | “Which renovation subsidies are available in 2026 and what should I check before commissioning work?” | Current page is too abstract for a subsidy query and omits concrete current measures/amounts. |
| `/renovatie-plannen/rendement-renovatie/` | DEEP_REWRITE | “Which renovation choices deliver value: money, home value, energy, comfort or avoided damage?” | Current concept is sensible but too generic; retarget to measurable decision value with evidence and explicit limitations. |

## Cannibalisation boundaries

### huis-renoveren vs renovatie-volgorde
- `huis-renoveren`: overall decision path before and during a renovation.
- `renovatie-volgorde`: physical/technical sequence of works.
- The pillar may summarize the sequence in 5–7 lines but must hand off detail.

### huis-renoveren vs renovatiefasen
- `huis-renoveren`: broad “where do I start?” answer.
- `renovatiefasen`: lifecycle management: preparation, design, feasibility, quotation/contracting, execution, handover.
- Avoid repeating identical numbered steps.

### renovatiekosten vs renovatie-budget
- `renovatiekosten`: market/project cost benchmarks and cost drivers.
- `renovatie-budget`: how the homeowner allocates, reserves, updates and controls available money.

### complete-renovatie vs huis-renoveren
- `complete-renovatie`: only for multi-system, whole-house or strongly interdependent renovation; must discuss coordination, temporary living, duration/cost uncertainty and phasing.

### rendement-renovatie vs verduurzamen
- `rendement-renovatie`: whole-renovation decision value, including property value, avoided repair, space, maintenance, comfort and energy.
- `/verduurzamen/`: technical energy measures and energy-specific economics.

## Content rules for the rebuild

- No fixed article length. Cover the intent until the reader can make the next decision.
- No mandatory quick-answer, TOC, FAQ, table, decision grid or CTA. Use only when it helps that page.
- Current price, subsidy, permit and regulation claims require source + date + scope.
- Give numbers when good evidence exists; qualify ranges and never imply a quote.
- Use prose as the default. Cards/tables should compress real comparisons, not decorate the page.
- Avoid identical section openings, “beslisregel” boxes and repeated three/four-item grids across the cluster.
- Add source-backed information gain: current 2026 benchmarks, official checks, concrete examples, project-specific failure points.
- Keep the tone practical and accessible: normal Dutch homeowner language, technical terms explained where necessary.
- Run `humanizer`, `general-writing`, `anti-ai-slop`, SEO and `PUBLISH_REVIEW` after drafting.

## Handoff

Proceed with the two LIGHT_UPDATE pages within limited scope and DEEP_REWRITE the seven pages marked above. Preserve accurate safety guidance, official Omgevingsloket/RVO references and useful internal-link boundaries. Do not change indexation.