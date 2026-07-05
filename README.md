# Thuisrenovatie Gids

Site éditorial d'articles de blog sur la rénovation domiciliaire, similaire à renovatiegids.be. Le site se concentre sur les guides complets pour la rénovation, en particulier sur les vérandas.

## Structure du projet

```
thuisrenovatie-gids/
├── index.html              # Page d'accueil
├── css/
│   └── style.css          # Feuille de style principale
├── assets/
│   └── images/            # Images du site
├── veranda/               # Cluster principal sur les vérandas
│   └── veranda-bouwen-renoveren.html  # Page pilier principale
└── README.md              # Ce fichier
```

## Clusters de contenu

### 1. Page pilier principale
**Sujet**: "Veranda bouwen of renoveren: complete gids voor kosten, materialen en vergunningen"
- Rôle: Page encyclopédique couvrant le panorama complet (types, prix, vergunning, isolatie, onderhoud, inspiratie)
- Statut: ✅ Créé

### 2. Cluster "Type veranda & concept"
Angles orientés utilisateur + mots-clés transactionnels:
- Soorten veranda's: aluminium, hout, kunststof, staal
- Moderne veranda vs. klassieke veranda
- Veranda als leefruimte / woonkameruitbreiding
- Veranda als keukenuitbreiding
- Veranda als thuiskantoor / bureau aan huis
- Veranda met schuifdeuren vs. harmonicadeuren
- Veranda met plat dak vs. zadeldak
- Serre, tuinkamer of veranda: wat is het verschil?

### 3. Cluster "Prijs, budget & ROI"
Très bon potentiel volume + forte intention commerciale:
- Veranda kosten per m² (2026)
- Veranda prijs aluminium vs. hout vs. kunststof
- Goedkope veranda: waar op letten en wat vermijden
- Veranda financieren: lening, subsidie, premies energie
- Bespaart een goed geïsoleerde veranda op energiekosten?
- Veranda renoveren vs. volledig vervangen: wat is goedkoper?

### 4. Cluster "Vergunningen, regels & buren"
Questions fréquentes dans la réalité:
- Heb je een vergunning nodig voor een veranda in Nederland?
- Veranda plaatsen aan de erfgrens: wat mag wel en niet?
- Veranda en privacy: inkijk beperken, afspraken met buren
- Maximale afmetingen veranda zonder vergunning
- Veranda bij rijtjeshuis / hoekwoning: speciale regels?

### 5. Cluster "Isolatie, comfort & techniek"
Angles "confort thermique / acoustique" très porteurs:
- Veranda isoleren: dak, glas en vloer
- Beste beglazing voor veranda: dubbel, HR++ of triple glas
- Veranda warm in de winter, koel in de zomer: tips
- Zonwering voor veranda: screens, lamellen, dakzonwering
- Veranda ventilatie: condens, schimmel en vocht voorkomen
- Veranda verwarmen: vloerverwarming, radiatoren, airco-warmtepomp

### 6. Cluster "Renovatie & upgrade veranda"
Différenciation claire des sites de fabricants:
- Veranda renoveren: stappenplan en kostenindicatie
- Oud houten veranda vernieuwen naar aluminium constructie
- Enkel glas in veranda vervangen door hoogrendementsglas
- Veranda dak vervangen: polycarbonaat vs. glas vs. sandwichpanelen
- Veranda moderniseren: zwarte profielen, slanke lijnen, minimalistisch
- Veranda ombouwen tot volwaardige leefruimte (isolatie + elektra)

### 7. Cluster "Inrichting, styling & gebruik"
Plus "aspirationnel", bon pour top/mid-funnel:
- Veranda inrichten als gezellige woonkamer
- Veranda als eetkamer: indeling, verlichting en akoestiek
- Veranda als thuiswerkplek: akoestiek, licht en temperatuur
- Scandinavische veranda: lichte kleuren, hout en textiel
- Industriële veranda met staal en glas: ideeën en materialen
- Veranda planten en groen: welke planten doen het goed?
- Veranda vloer kiezen: tegel, pvc, hout, betonlook

### 8. Cluster "Vergelijking & keuzehulp"
Très utile pour la conversion + bons CTRs en SERP:
- Aluminium vs. houten veranda: wat past bij jouw huis?
- Veranda of uitbouw: verschil in kosten, vergunning en comfort
- Veranda, serre of tuinkamer: wat kies je voor jouw woning?
- Prefab veranda kit vs. maatwerk veranda
- Welke veranda past bij een jaren 30-woning?
- Veranda voor nieuwbouw vs. bestaande woning: aandachtspunten

### 9. Intention "problemen / pijn points"
Contenu très captateur d'intentions long tail qualifiées:
- Veranda te warm in de zomer: oorzaken en oplossingen
- Veranda lekt: waar komt het vandaan en wat kun je doen?
- Condens in veranda ramen: oorzaken en tips
- Veranda maakt veel lawaai bij regen: hoe verminderen?
- Schimmel in veranda: herkennen, oplossen en voorkomen

## Stack technique

- **HTML5**: Structure sémantique
- **CSS3**: Styling avec variables CSS pour la maintenance
- **JavaScript**: Minimal (optionnel pour interactions futures)
- **Responsive Design**: Mobile-first approach

## Variables CSS

```css
--primary: #2c5f2d;          /* Vert principal */
--primary-dark: #1e421f;     /* Vert foncé */
--secondary: #97bc62;        /* Vert secondaire */
--text-dark: #333;           /* Texte sombre */
--text-light: #666;          /* Texte clair */
--text-lighter: #999;        /* Texte très clair */
--bg-light: #f8f9fa;         /* Fond clair */
--bg-white: #ffffff;         /* Fond blanc */
--border: #e0e0e0;           /* Bordure */
--shadow: 0 2px 8px rgba(0,0,0,0.1);  /* Ombre */
```

## Développement

### Ouvrir le site localement
Ouvrir simplement `index.html` dans un navigateur ou utiliser un serveur local:

```bash
# Avec Python 3
python -m http.server 8000

# Avec Node.js (http-server)
npx http-server
```

### Ajouter une nouvelle page
1. Créer un fichier HTML dans le dossier approprié (ex: `veranda/`)
2. Copier la structure d'une page existante
3. Adapter le contenu et les métadonnées
4. Ajouter les liens internes depuis la page d'accueil

## SEO

- Utiliser des balises meta description optimisées
- Structure hiérarchique avec H1, H2, H3
- Liens internes entre les pages du même cluster
- Images avec alt text descriptif
- URLs propres et descriptives

## Prochaines étapes

- [ ] Créer les pages du cluster "Type veranda & concept"
- [ ] Créer les pages du cluster "Prijs, budget & ROI"
- [ ] Créer les pages du cluster "Vergunningen, regels & buren"
- [ ] Créer les pages du cluster "Isolatie, comfort & techniek"
- [ ] Créer les pages du cluster "Renovatie & upgrade veranda"
- [ ] Créer les pages du cluster "Inrichting, styling & gebruik"
- [ ] Créer les pages du cluster "Vergelijking & keuzehulp"
- [ ] Créer les pages du cluster "Problemen / pijn points"
- [ ] Ajouter des images placeholder
- [ ] Initialiser le repository git

## Licence

© 2026 Thuisrenovatie Gids. Tous droits réservés.
