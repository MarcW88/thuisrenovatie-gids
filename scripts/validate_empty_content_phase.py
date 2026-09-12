from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATEGORIES = [
    'renovatie-plannen', 'renovatieprojecten', 'verduurzamen',
    'problemen-oplossen', 'vakman-en-offertes', 'doe-het-zelf'
]

errors = []
checked = 0
for category in CATEGORIES:
    for page in (ROOT / category).rglob('index.html'):
        checked += 1
        text = page.read_text(encoding='utf-8')
        if 'class="skeleton"' not in text or 'aria-label="Lege contentruimte"' not in text:
            errors.append(f'{page.relative_to(ROOT)}: pagina bevat geen verwachte lege content-shell')

if errors:
    print('\n'.join(errors))
    raise SystemExit(1)
print(f'PASS: {checked} pagina\'s blijven bewust in de lege-contentfase')
