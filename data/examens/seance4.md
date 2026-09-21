# Exercice noté — Moyenne des mesures valides

**Durée indicative : 15 minutes**

Écrire une fonction nommée exactement :

```python
def moyenne_mesures_valides(mesures, maximum):
```

## Données reçues

- `mesures` est une liste de nombres (`int` ou `float`), éventuellement vide ;
- `maximum` est un nombre positif ou nul ;
- les paramètres seront toujours du type attendu : il n'est pas nécessaire de les vérifier.

Une mesure est **valide** si elle est supérieure ou égale à `0` **et** inférieure ou égale à `maximum`. Les deux bornes sont incluses.

## Résultat attendu

La fonction doit renvoyer la moyenne des mesures valides, arrondie à deux chiffres après la virgule avec `round()`.

Si la liste est vide ou ne contient aucune mesure valide, la fonction doit renvoyer `None`.

```python
moyenne_mesures_valides([12, -2, 18, 35, 20], 25)  # 16.67
moyenne_mesures_valides([0, 5, 10, 11], 10)         # 5.0
moyenne_mesures_valides([-4, 25, 30], 20)           # None
moyenne_mesures_valides([], 20)                     # None
```

## Contraintes obligatoires

- utiliser une boucle `for` pour parcourir la liste ;
- utiliser une structure conditionnelle `if` ;
- calculer la somme avec une variable accumulatrice ;
- compter les mesures valides avec une variable compteur ;
- utiliser `return` pour fournir le résultat ;
- ne pas modifier la liste reçue.

Il est interdit d'utiliser `sum()`, NumPy, une compréhension de liste, `input()`, `print()`, une boucle `while` ou de définir une fonction supplémentaire.

## Fichier à remettre

Le fichier doit contenir uniquement la définition de `moyenne_mesures_valides`. Il ne doit contenir aucun appel de fonction ni code de test.
