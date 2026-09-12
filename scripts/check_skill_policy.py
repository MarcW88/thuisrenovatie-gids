from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / '.agents' / 'skills'

records = []
errors = []
for skill_file in sorted(SKILLS.glob('*/SKILL.md')):
    text = skill_file.read_text(encoding='utf-8')
    match = re.search(r'^provenance:\s*(upstream|custom)\s*$', text, re.M)
    if not match:
        errors.append(f'{skill_file}: ontbrekende provenance (upstream/custom)')
        continue
    provenance = match.group(1)
    if provenance == 'upstream':
        upstream = re.search(r'^upstream:\s*(https://github\.com/\S+)\s*$', text, re.M)
        if not upstream:
            errors.append(f'{skill_file}: upstream skill zonder geldige GitHub-URL')
    records.append((skill_file.parent.name, provenance))

if errors:
    print('\n'.join(errors))
    raise SystemExit(1)

if not records:
    raise SystemExit('Geen skills gevonden')

upstream_count = sum(p == 'upstream' for _, p in records)
custom_count = sum(p == 'custom' for _, p in records)
total = len(records)
custom_ratio = custom_count / total
upstream_ratio = upstream_count / total

print(f'Skills: {total} | upstream={upstream_count} ({upstream_ratio:.1%}) | custom={custom_count} ({custom_ratio:.1%})')
for name, provenance in records:
    print(f'- {name}: {provenance}')

if custom_ratio > 0.20:
    raise SystemExit(f'FAIL: custom skill ratio {custom_ratio:.1%} is hoger dan 20%')
if upstream_ratio < 0.80:
    raise SystemExit(f'FAIL: upstream skill ratio {upstream_ratio:.1%} is lager dan 80%')

print('PASS: 80/20 skill policy gerespecteerd')
