# Exercices — Séance 2 : Organiser et répéter les traitements

**Ex. 1 — Fonction sans `max()`**
Écrire une fonction `maximum(liste)` qui renvoie le plus grand élément, sans utiliser `max()`, à l'aide d'une boucle.

**Ex. 2 — Fonctions de conversion**
Écrire une fonction `convertir(valeur, unite="m")` gérant au moins 3 unités de longueur (m, cm, km) avec une valeur par défaut.

**Ex. 3 — Tuple et dépaquetage**
Créer un tuple de coordonnées GPS `(latitude, longitude)`, le dépaqueter dans deux variables, et afficher un message formaté.

**Ex. 4 — Découpage de texte**
À partir d'une phrase saisie par l'utilisateur, afficher : les 5 premiers caractères, les 5 derniers, un mot sur deux (via `split()` et slicing de liste).

**Ex. 5 — Nettoyage de texte**
À partir d'une chaîne du type `"  Alice ; Bob ;Charlie  "`, obtenir la liste `["Alice", "Bob", "Charlie"]` propre (sans espaces) en utilisant `strip`, `split`, et une boucle ou une compréhension simple.

**Ex. 6 — Recherche avec `while`/`break`**
Écrire un programme qui parcourt une liste de mesures avec `while` et s'arrête (`break`) dès qu'une valeur dépasse un seuil, en affichant sa position (utiliser `continue` pour ignorer les valeurs négatives).
