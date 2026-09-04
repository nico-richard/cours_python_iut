# Exercices — Séance 4 : Visualiser et acquérir des mesures

## Fichier nécessaire

Copier `mesures.csv` depuis le dossier `seance3` vers le dossier `seance4`, puis enregistrer les programmes de cette feuille dans `seance4`.

**Ex. 1 — Première courbe**
À partir du CSV de la séance 3, tracer température en fonction du temps avec `plt.plot`, en ajoutant titre et légendes des axes.

**Ex. 2 — Nuage de points et histogramme**
Dans un même script, créer d'abord une figure contenant un nuage de points (deux séries de mesures liées), puis une seconde figure contenant l'histogramme d'une série de valeurs.

**Ex. 3 — Personnalisation et export**
Reprendre l'Ex. 1 : changer couleur/style de ligne, ajouter une grille et une légende, puis exporter le graphique en `.png`.

**Ex. 4 — Détection de dépassement de seuil**
Ajouter au graphique une ligne horizontale représentant un seuil (`plt.axhline`), et faire apparaître en rouge les points qui le dépassent.

**Ex. 5 — Sous-figures**
Créer une figure avec 2 sous-graphiques côte à côte (courbe + histogramme) pour la même série de mesures, avec `plt.subplots`.

**Ex. 6 — Lecture d'un port série (si matériel disponible)**
Avec `pyserial`, lister les ports avec `serial.tools.list_ports.comports()`, se connecter à une carte, lire 10 mesures, les stocker dans une liste puis les tracer. Sans matériel, relire progressivement les lignes de `data/donnees/mesures.csv` comme si elles arrivaient du port série.
