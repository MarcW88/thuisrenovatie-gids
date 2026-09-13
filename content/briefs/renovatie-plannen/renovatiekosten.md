# Brief v2 - Renovatiekosten

- Route: `/renovatie-plannen/renovatiekosten/`
- Status: QA_IN_PROGRESS
- Primary query: `renovatiekosten` / `huis renoveren kosten`
- Secondary intents: `verbouwing kosten 2026`, `renovatie kosten per m2`, project cost benchmarks
- Reader task: get useful current price benchmarks, understand their scope and translate them into a first project estimate.
- Decision: DEEP_REWRITE
- Last researched: 2026-09-13

## Search intent

The SERP expects current numbers. A useful page cannot answer only with `het hangt ervan af`. It must give concrete 2026 benchmarks while making inclusion/exclusion boundaries visible enough that the reader does not compare unlike scopes.

## Evidence register

Primary current source: Vereniging Eigen Huis, `Wat kost verbouwen?`, price level 2026. The source describes its figures as minimum guideline prices and generally includes VAT, materials and labour, while noting regional, location, extra-project and market effects.

Benchmarks to use:
- dakkapel: 2.5-6 m; wooden EUR 9,660-14,200 and plastic EUR 8,505-12,025 depending on width;
- kitchen incl. installation: EUR 3,990-30,600 depending on level; demolition, relocated water/electricity and meter-box work are listed separately by the source;
- bathroom 2x3m: EUR 4,095-19,925 depending on level, excluding demolition;
- casco masonry extension 10m2: EUR 21,750-27,550, excluding opening, finishing, installations and interior; larger sizes have separate ranges;
- attic: EUR 6,565-19,925 depending on scenario and scope.

Freshness context: CBS July 2026 input-price index for new-build housing was 5.1% higher year-on-year. Use only as context showing why dated price data matters. Do not present CBS as a renovation-tariff index.

## Ownership boundary

- This page owns current benchmark prices, inclusions/exclusions, cost drivers and the method for turning public benchmarks into a first estimate.
- `/renovatie-budget/` owns affordability, allocation, contingency and spend control.
- `/complete-renovatie/` owns integrated whole-house scope and coordination; do not invent a national average for a `complete renovatie` here.
- Project pages own detailed technical/buying decisions for bathroom, kitchen, extension, etc.

## Required information gain

1. **Price anatomy:** number + source year + scope + major exclusions in one place.
2. **Scope normalisation:** before comparing two numbers, check VAT/labour, demolition, installations, finish level, access/waste and project preparation.
3. **Benchmark-to-estimate method:** base benchmark -> enabling/adjacent works -> project-specific costs. Contingency remains a budget topic.
4. **€/m2 decision rule:** explain when it is useful and when mixed technical density makes it misleading.
5. **Freshness rule:** older undated tables are not carried forward as 2026 facts.

## Editorial rule

Do not hide behind `it depends`. Give numbers where scope and source are clear, then explain the conditions. Do not imply that `incl. montage` means all surrounding construction and installation work is included.
