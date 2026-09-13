---
name: renovation-content-workflow
description: Workflow unique de production et correction SEO/GEO pour thuisrenovatie-gids.nl. Utiliser après renovation-analysis-workflow lorsqu'une page existante nécessite LIGHT_UPDATE ou DEEP_REWRITE, ou pour créer une nouvelle page. Orchestre intention, recherche, preuves, brief, rédaction et QA sans imposer de template par cluster.
provenance: custom
metadata:
  adapted_for: thuisrenovatie-gids.nl
  source_engine: https://github.com/MarcW88/bloc-notes-numerique/tree/main/.agents/skills/guide-content-workflow
  orchestration_target: ">=80% existing GitHub skills"
  custom_scope: "renovation routing + category boundaries + safety + source-of-truth integration"
---

# Renovation Content Workflow

## Rôle

C'est le **seul workflow de production/correction** à utiliser pour les contenus éditoriaux de Thuisrenovatie Gids.

Pour une page existante, la séquence normale est :

`renovation-analysis-workflow / AUDIT` → décision → correction si nécessaire → `renovation-analysis-workflow / PUBLISH_REVIEW`.

Décisions consommées :

- `KEEP` → ne pas réécrire ;
- `LIGHT_UPDATE` → corriger uniquement le scope identifié ;
- `DEEP_REWRITE` → reconstruire la page tout en préservant les éléments valides ;
- `MERGE` / `NOINDEX` → ne pas produire une nouvelle version sans décision humaine sur le rôle de l'URL.

Pour une **nouvelle URL**, effectuer directement intention, recherche, preuves et brief avant la rédaction.

Le workflow ne modifie jamais `indexing_enabled` de lui-même.

---

# 1. Entrées

Lire avant toute production :

- `AGENTS.md` et les règles de design/rendu si concernées ;
- `.agents/skills/renovation-analysis-workflow/SKILL.md` ;
- l'audit de la page lorsqu'elle existe ;
- la page cible et sa source de vérité `content/<route>/body.html` ;
- `content/briefs/<route>.md` et `content/reviews/<route>.md` lorsqu'ils existent ;
- les pages voisines du cluster ;
- les pages des autres clusters qui répondent à des sous-questions proches ;
- les données sémantiques, GSC, logs ou autres signaux disponibles ;
- les sources nécessaires aux faits actuels.

Ne pas utiliser la mémoire du modèle pour combler un manque factuel.

Pour une page existante, préserver explicitement la valeur identifiée par `renovation-analysis-workflow / AUDIT`.

---

# 2. Router le travail sans créer un template

La route indique la **frontière éditoriale** :

- `PLAN` → `renovatie-plannen/` ;
- `PROJECT` → `renovatieprojecten/` ;
- `SUSTAINABILITY` → `verduurzamen/` ;
- `TROUBLESHOOTING` → `problemen-oplossen/` ;
- `DIY` → `doe-het-zelf/` ;
- `LEAD` → `vakman-en-offertes/`.

Cette classification ne dicte jamais la structure de l'article.

Identifier ensuite le travail dominant uniquement pour choisir les risques à vérifier :

- `CHOICE` — aider à arbitrer entre options, priorités, contraintes ou approches ;
- `EXPLAINER` — expliquer un mécanisme, une règle, un coût, un risque ou une technologie ;
- `HOW_TO` — permettre une tâche, une préparation, un contrôle ou une procédure.

Une page peut être hybride.

Lire si utile :

- `references/choice-guide.md` ;
- `references/explainer-guide.md` ;
- `references/how-to-guide.md`.

Ces références sont des **questions de contrôle**, pas des architectures à reproduire. Elles ne doivent jamais imposer l'ordre ou le nombre de sections, un tableau, une FAQ, une checklist ou un nombre d'étapes.

---

# 3. Chaîne de production fondée sur les skills réutilisés

La majorité de la méthode doit provenir des skills existants. Le présent fichier orchestre ; il ne duplique pas leurs méthodologies.

## Étape 1 — intention, cluster et rôle

Utiliser :

- `seo-keyword` lorsque recherche, clustering ou validation du topic est nécessaire ;
- `search-intent` pour la tâche exacte, les sous-questions, le niveau de maturité et le résultat attendu ;
- `seo-content-audit` et `content-refresh` pour une page existante lorsque l'audit l'a demandé ;
- `jtbd-framing` lorsque le job ou le contexte de décision doit être clarifié ;
- `information-architecture` lorsque le rôle de la page ou la frontière entre clusters est incertain.

Confirmer :

- requête/topic principal ;
- intention ;
- tâche ou décision du lecteur ;
- périmètre ;
- route propriétaire ;
- prochaine étape logique ;
- chevauchements internes.

### Gate de frontière

Une page ne doit pas absorber une autre fonction du site uniquement parce que le sujet est lié.

Si le rôle apparaît incorrect malgré l'audit, arrêter et renvoyer vers `renovation-analysis-workflow` plutôt que forcer un texte dans le slug.

## Étape 2 — recherche et registre de preuves

Utiliser `fact-check` pour les claims vérifiables.

Adapter la recherche à la stabilité du sujet :

- principe physique ou construction stable → exactitude et source solide ;
- prix, main-d'œuvre, disponibilité → vérification actuelle + date ;
- subside, fiscalité, permis, réglementation, norme ou procédure administrative → source officielle actuelle + territoire + date ;
- performance, rendement, économie ou valeur → conditions et hypothèses explicites ;
- claim expérientiel important → `evidence-based-reviews` si nécessaire.

Pour les claims importants, conserver :

- affirmation ;
- source ;
- date de consultation ;
- territoire ;
- portée/conditions ;
- stabilité ;
- niveau d'incertitude.

Une inconnue reste inconnue, qualifiée ou exclue.

## Étape 3 — questions propres au type dominant

### `CHOICE`

Documenter seulement ce qui change l'arbitrage : critères, compromis, critères éliminatoires, dépendances, coût lorsque pertinent, risques et situations où chaque option cesse d'être adaptée.

### `EXPLAINER`

Documenter seulement ce qui permet de comprendre correctement : concept, termes voisins, mécanisme, causalité, conséquence pratique, limites, hypothèses et exceptions.

Une définition seule n'est pas une explication.

### `HOW_TO`

Documenter seulement ce qui permet d'exécuter la tâche : contexte, prérequis, méthode vérifiée, résultat attendu, vérification, échecs probables, alternatives et stop conditions de sécurité.

Ne jamais inventer une étape parce qu'elle semble probable.

## Étape 4 — valeur affiliée / lead lorsque pertinent

Utiliser `affiliate-value` avant la rédaction finale lorsque la page influence une dépense, une demande de devis, un choix de vakman, un produit ou une installation.

Pour les pages `LEAD`, utiliser aussi `cro-optimization`, mais uniquement après avoir établi la valeur et la confiance.

La page doit rester utile sans lien affilié ni formulaire. Les critères, limites, alternatives et conséquences pratiques doivent exister indépendamment de la conversion.

## Étape 5 — brief propre à la page

Utiliser `content-brief-authoring` comme skill principal de brief et persister le résultat dans `content/briefs/<route>.md`, en conservant les champs utiles de `references/brief-template.md`.

Le brief doit contenir uniquement ce qui change réellement la page :

- intention/tâche ;
- route et rôle ;
- valeur propre ;
- périmètre et exclusions ;
- faits et entités nécessaires ;
- preuves ;
- risques ;
- contraintes de sécurité ;
- valeur existante à préserver pour une mise à jour ;
- liens vers les prochaines questions ;
- angle/thèse ;
- structure proposée **issue de cette recherche**.

### Règle centrale

Il n'existe **aucune architecture éditoriale obligatoire par type de route ou type de contenu**.

Le plan final est construit après l'intention et les preuves. Chaque grande section doit être justifiable par une question, une étape nécessaire, une distinction, une preuve, un arbitrage, une dépendance, un risque ou une limite.

Deux pages d'un même cluster peuvent avoir des structures très différentes.

## Étape 6 — rédaction

Utiliser `content-and-copy` pour produire la prose à partir du brief et du registre de preuves.

Règles :

- répondre suffisamment tôt à la question principale ;
- employer un néerlandais naturel, précis et sobre ;
- expliquer ce que les faits changent pour le lecteur ;
- distinguer faits, interprétations, hypothèses et inconnues ;
- ne jamais inventer test, inspection, mesure, prix, économie, réglementation, disponibilité ou procédure ;
- utiliser tableaux, listes et étapes uniquement lorsqu'ils améliorent la compréhension ;
- éviter les FAQ répétitives ;
- ne pas pousser un lead ou un vakman avant que la décision du lecteur soit suffisamment mûre ;
- pour `LIGHT_UPDATE`, ne pas réécrire par réflexe les passages que l'audit a demandé de préserver.

Intégrer le contenu dans la **source de vérité** :

`content/<route>/body.html`

Puis régénérer avec `generate_pages.py`. Ne pas éditer uniquement le HTML généré.

---

# 4. Contrôles post-rédaction

Exécuter les passes pertinentes séparément ; ne pas déclarer plusieurs contrôles effectués après une relecture générique.

## Étape 7 — factualité après rédaction

Relancer `fact-check` sur les claims réellement écrits. Si une modification ultérieure introduit un nouveau fait, repasser ce fait par ce gate.

Utiliser `evidence-based-reviews` seulement pour les jugements expérientiels qui le nécessitent.

## Étape 8 — sécurité et limites

Relire séparément les passages relatifs à structure, fondations, gaz, électricité, amiante, toiture/hauteur, humidité potentiellement structurelle et travaux réglementés.

Une passe de style ne peut jamais supprimer ou affaiblir une stop condition importante.

## Étape 9 — maillage

Utiliser `internal-linking-audit`.

Un lien existe parce qu'il répond à la prochaine question logique, pas pour atteindre un quota. Vérifier les cibles, les ancres et la frontière entre clusters.

## Étape 10 — finition éditoriale

Dans cet ordre logique :

1. `humanizer` sur l'intégralité du contenu visible ;
2. `general-writing` avec le minimum de changements nécessaires ;
3. `anti-ai-slop` en mode review/detection ;
4. `seo-drift` uniquement si un baseline utile existe.

Après ces passes, vérifier qu'aucun fait, prérequis, limite, nuance ou avertissement de sécurité n'a été perdu ou inventé.

## Étape 11 — SEO et QA

Utiliser :

1. `seo-onpage` ;
2. `seo-technical` ;
3. `seo-best-practices` seulement pour les règles réellement applicables ;
4. `editorial-qa` ;
5. lecture complète dans l'ordre rendu, desktop/mobile lorsque le rendu est disponible.

Le contrôle final doit notamment confirmer :

- tâche satisfaite ;
- architecture propre à la page ;
- pas de clonage mécanique des types ou références ;
- faits/procédures actuels lorsque nécessaire ;
- limites importantes préservées ;
- frontière claire avec les clusters voisins ;
- sécurité explicite ;
- valeur sans affiliation ;
- aucun faux hands-on, faux diagnostic ou fausse inspection.

---

# 5. PUBLISH_REVIEW obligatoire

Une fois la correction/rédaction terminée, **ne pas auto-valider dans ce workflow**.

Passer la main à :

`renovation-analysis-workflow / PUBLISH_REVIEW`

Ce mode exécute :

- `python3 scripts/validate_content_quality.py` pour les blockers machine ;
- les gates substantiels ;
- la comparaison au cluster.

Résultats possibles :

- `PASS — READY_FOR_HUMAN_VALIDATION` ;
- `FAIL — KEEP_NOINDEX`.

Un PASS reste suivi d'une validation humaine explicite avant toute instruction d'indexation.

---

# 6. Statuts et traçabilité

Le brief/review peut conserver :

- `BRIEF_READY` ;
- `DRAFT_READY` ;
- `QA_IN_PROGRESS` ;
- `REVISION_REQUIRED` ;
- `HUMAN_APPROVED` ;
- `PUBLISHABLE`.

Ils ne remplacent pas la décision de `renovation-analysis-workflow`.

Dans `content/reviews/<route>.md`, consigner au minimum les passes réellement effectuées, les blockers, les corrections importantes, les sources sensibles et les risques résiduels. Ne pas marquer un skill `PASS` sur la seule base du validateur machine.

`PUBLISHABLE` exige : PUBLISH_REVIEW PASS + validation humaine + contrôles techniques. L'indexation reste une instruction séparée.

---

# 7. Handoffs entre clusters

Le workflow reste unique à l'échelle du site, mais il doit renvoyer l'intention vers le bon cluster lorsque la frontière est mauvaise :

- vers `renovatie-plannen/` pour décisions transversales de planification ;
- vers `renovatieprojecten/` pour un chantier concret ;
- vers `verduurzamen/` pour énergie/confort/installation ;
- vers `problemen-oplossen/` pour symptôme/diagnostic prudent ;
- vers `doe-het-zelf/` seulement pour une tâche réellement adaptée au DIY ;
- vers `vakman-en-offertes/` lorsque la vraie tâche est de sélectionner ou cadrer un prestataire.

Ne jamais forcer une sous-question dans une page uniquement parce que le mot-clé semble proche.

---

# 8. Ce que ce workflow ne doit pas devenir

Ne pas ajouter :

- quota de mots ;
- nombre minimum de H2/H3 ;
- quota de liens ou de sources ;
- nombre obligatoire d'étapes ;
- tableau ou FAQ obligatoire ;
- score qualité artificiel ;
- architecture fixe `PLAN`, `PROJECT`, `SUSTAINABILITY`, `DIY`, `TROUBLESHOOTING`, `LEAD`, `CHOICE`, `EXPLAINER` ou `HOW_TO` ;
- deuxième copie des règles de `fact-check`, SEO, rédaction, humanisation ou QA déjà présentes dans les skills spécialisés.

La couche custom doit rester limitée au routing rénovation, aux frontières de cluster, à la sécurité et à l'intégration dans la source de vérité du site.