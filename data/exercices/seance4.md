# Exercices — Séance 4 : Visualisation et instrumentation

**Ex. 1 — Première courbe**
À partir du CSV de la séance 3, tracer température en fonction du temps avec `plt.plot`, en ajoutant titre et légendes des axes.

**Ex. 2 — Nuage de points et histogramme**
Sur un même script, tracer un nuage de points (deux séries de mesures liées) puis un histogramme d'une série de valeurs.

**Ex. 3 — Personnalisation et export**
Reprendre l'Ex. 1 : changer couleur/style de ligne, ajouter une grille et une légende, puis exporter le graphique en `.png`.

**Ex. 4 — Détection de dépassement de seuil**
Ajouter au graphique une ligne horizontale représentant un seuil (`plt.axhline`), et faire apparaître en rouge les points qui le dépassent.

**Ex. 5 — Sous-figures**
Créer une figure avec 2 sous-graphiques côte à côte (courbe + histogramme) pour la même série de mesures, avec `plt.subplots`.

**Ex. 6 — Lecture d'un port série (si matériel disponible)**
Avec `pyserial`, lister les ports disponibles, se connecter à une carte (Arduino ou simulateur), lire 10 mesures, les stocker dans une liste puis les tracer.
