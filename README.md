# Outil de cours — Python IUT 1re année

## Installation
```bash
pip install -r requirements.txt
```

## Lancement (à projeter en cours)
```bash
streamlit run app.py
```

## Structure
```
cours_python_iut/
├── app.py                       # Point d'entrée : déclare la navigation
├── utils.py                     # Fonctions réutilisables (modularité, fichiers, images, listes)
├── pdf_export.py                # Conversion Markdown -> PDF (mise en page impression)
├── views/
│   ├── cours.py                 # Diaporama de projection + mode Lecture
│   ├── bac_a_sable.py           # Exécution de code Python en direct
│   ├── exercices.py             # Affichage des exercices
│   └── imprimer.py              # Génération de PDF imprimables
└── data/
    ├── sessions/seanceN.md      # Contenu des diapositives (modifiable librement)
    ├── sessions/images/         # Images utilisées dans les diapositives
    └── exercices/seanceN.md     # Énoncés des exercices
```

Pour modifier le contenu d'un cours ou des exercices, il suffit d'éditer les
fichiers Markdown dans `data/` — aucune modification du code n'est nécessaire.
Les diapositives sont séparées par une ligne `---`.

La page Cours propose deux affichages :
- **Diaporama** : une diapositive à la fois pour la projection ;
- **Lecture** : séance complète avec les compléments destinés aux étudiants.

## Blocs pédagogiques
Trois blocs facultatifs permettent d'adapter un contenu au support :
```markdown
:::support
Texte affiché dans une note bleue en mode Lecture et dans le PDF, mais masqué
dans le diaporama.
:::

:::attention
Erreur fréquente ou précaution importante, visible partout.
:::

:::retenir
Idée essentielle à mémoriser, visible partout.
:::
```

Les fichiers existants restent valides sans utiliser ces blocs.

## Diagrammes simples
Une chaîne conceptuelle peut être affichée sous forme de blocs encadrés :
```markdown
:::diagram
Fichier sur le stockage
Programme et données en RAM
Traitement par le CPU
:::
```

Pour une chaîne longue, utilisez `:::diagram vertical`.

## Ajouter des images dans les diapositives
Placez vos images dans `data/sessions/images/`, puis référencez-les dans le
Markdown avec un chemin **relatif au fichier de la séance** :
```markdown
![Architecture simplifiée d'un ordinateur](images/s1_ordinateur.png)
```
`utils.py` convertit automatiquement ces images locales en base64 au
chargement de la diapositive (nécessaire car `st.markdown()` ne sait pas
servir des fichiers du disque comme le ferait un serveur web classique). Les
images distantes (`http://...`, `https://...`) fonctionnent sans modification.

## Affichage du cours
Le mode **Diaporama** utilise automatiquement une typographie agrandie pour la
projection en salle. Le mode **Lecture** conserve une mise en page plus compacte
et affiche les notes `:::support` destinées à la consultation individuelle.

## Version imprimable
La page "Version imprimable" génère, à partir du contenu Markdown actuel, un
PDF par séance (cours + exercices, mise en page classique en pages A4) ou un
polycopié complet regroupant les 4 séances. Le rendu s'appuie sur `markdown`
(conversion Markdown -> HTML) et `xhtml2pdf` (HTML -> PDF), sans dépendance
système. Écrivez du Markdown standard (ligne vide avant une liste) pour un
rendu propre : `utils.corriger_espacement_listes()` rattrape automatiquement
l'oubli le plus courant.
