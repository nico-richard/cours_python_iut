# Exercices — Séance 2 : Organiser et répéter les traitements

**Ex. 1 — Calculer puis tester une moyenne**

1. Écrire une fonction `moyenne(valeurs)` qui renvoie la moyenne des nombres
   contenus dans une liste non vide.
2. Écrire une fonction `tester_moyenne()` qui appelle `moyenne()` avec plusieurs
   listes connues et vérifie les résultats avec `assert`.
3. Appeler `tester_moyenne()` dans le programme principal et afficher un message
   lorsque tous les tests réussissent.

Exemples de résultats attendus : `moyenne([10, 12, 14])` renvoie `12.0` et
`moyenne([5])` renvoie `5.0`.

**Ex. 2 — Fonction sans `max()`**
Écrire une fonction `maximum(liste)` qui renvoie le plus grand élément d'une liste non vide, sans utiliser `max()`, à l'aide d'une boucle.

**Ex. 3 — Fonctions de conversion**
Écrire une fonction `convertir_depuis_m(valeur, unite="m")`. La valeur d'entrée est exprimée en mètres et l'unité de sortie peut être `"m"`, `"cm"` ou `"km"`. La fonction doit retourner le résultat et signaler une unité inconnue.

**Ex. 4 — Tuple et dépaquetage**
Créer un tuple de coordonnées GPS `(latitude, longitude)`, le dépaqueter dans deux variables, et afficher un message formaté.

**Ex. 5 — Découpage de texte**
À partir d'une phrase saisie par l'utilisateur, afficher : les 5 premiers caractères, les 5 derniers, un mot sur deux (via `split()` et slicing de liste).

**Ex. 6 — Nettoyage de texte**
À partir d'une chaîne du type `"  Alice ; Bob ;Charlie  "`, obtenir la liste `["Alice", "Bob", "Charlie"]` sans espaces superflus, en utilisant `strip()`, `split()` et une boucle.

**Ex. 7 — Recherche avec `while`/`break`**
Écrire un programme qui parcourt une liste de mesures avec `while` et s'arrête (`break`) dès qu'une valeur dépasse un seuil, en affichant sa position (utiliser `continue` pour ignorer les valeurs négatives). Veiller à faire avancer l'indice à chaque tour, y compris avant `continue`.
