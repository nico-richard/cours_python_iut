# Exercices — Séance 3 : Exploiter des données scientifiques

**Ex. 1 — Module `math` et `random`**
Utiliser `math` pour calculer racine carrée, puissance, et `random` pour générer 10 mesures aléatoires simulées entre 10 et 20.

**Ex. 2 — Lecture d'un fichier texte**
Lire un fichier `notes.txt` (une valeur par ligne) et compter le nombre de lignes ainsi que la somme des valeurs.

**Ex. 3 — Lecture d'un CSV de mesures**
Charger un fichier `mesures.csv` (colonnes temps, température) dans deux listes Python, puis calculer la moyenne "à la main".

**Ex. 4 — Écriture d'un rapport**
Écrire les résultats de l'Ex. 3 (moyenne, min, max) dans un fichier `rapport.txt`, avec `with open(..., "w")`.

**Ex. 5 — Premier tableau NumPy**
Créer un `ndarray` à partir des données de l'Ex. 3, afficher `shape`, `dtype`, puis convertir les températures de °C en K en une seule opération vectorisée.

**Ex. 6 — Statistiques et tableau 2D**
Construire un tableau NumPy 2D (3 capteurs × 5 instants, valeurs de votre choix) et calculer la moyenne par capteur (`axis=1`) et par instant (`axis=0`).
