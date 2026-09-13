# Post-write gap check — Energie besparen

- Route: `/verduurzamen/energie-besparen/`
- Checked: 2026-09-13
- Workflow version: 2

## MUST coverage
1. Baseline annual use + time profile — **COVERED**
2. Heating / hot water / electricity split — **COVERED**
3. Occupancy / home / weather / system context — **COVERED**
4. Heating settings before replacement — **COVERED**
5. System-specific setback boundary — **COVERED**
6. Hot-water behaviour / comfort setting — **COVERED**
7. Baseload / standby diagnosis — **COVERED**
8. Smart-meter insight boundary — **COVERED**
9. Ventilation not switched off for savings — **COVERED**
10. Existing PV self-consumption timing — **COVERED**
11. No unbounded savings claims — **COVERED**
12. Escalation matrix — **COVERED**

**12/12 MUST covered; 0 partial; 0 missing.**

## Cannibalisation
PASS. The page owns current-use diagnosis. It explicitly hands broad investment sequencing back to `/verduurzamen/` and technical design to child pages.

## Information gain
PASS: four-bucket energy profile plus `measure → explain → test → remeasure → invest` loop replaces generic tip-list structure.

## Final
**PASS — no blocking gap.**
