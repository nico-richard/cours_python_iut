# Exercices — Séance 3 : Exploiter des données scientifiques

**Ex. 1 — Module `math` et `random`**
Utiliser `math` pour calculer racine carrée, puissance, et `random` pour générer 10 mesures aléatoires simulées entre 10 et 20.

**Ex. 2 — Lecture d'un fichier texte**
Lire le fichier `data/donnees/notes.txt` (une valeur par ligne), puis calculer le nombre de notes, leur somme et leur moyenne.

**Ex. 3 — Lecture d'un CSV de mesures**
Charger `data/donnees/mesures.csv` (colonnes `temps` et `temperature`, séparateur `;`) dans deux listes Python, puis calculer la moyenne des températures sans NumPy.

**Ex. 4 — Écriture d'un rapport**
Écrire les résultats de l'Ex. 3 (moyenne, min, max) dans un fichier `rapport.txt`, avec `with open(..., "w")`.

**Ex. 5 — Premier tableau NumPy**
Créer un `ndarray` à partir des températures de l'exercice 3, afficher `shape` et `dtype`, puis convertir les valeurs de °C en K en une seule opération vectorisée.

**Ex. 6 — Statistiques et tableau 2D**
Construire un tableau NumPy 2D (3 capteurs × 5 instants, valeurs de votre choix) et calculer la moyenne par capteur (`axis=1`) et par instant (`axis=0`).
