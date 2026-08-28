# Séance 1
## Premiers programmes Python

### De la machine aux données, calculs et décisions

Nous allons suivre le chemin qui mène de la machine à un premier programme :

:::diagram
Ordinateur
Python
Données
Calculs
Décisions
:::

À la fin de la séance, vous devez être capables de lire et d'écrire un script simple qui manipule une mesure et adapte son comportement à sa valeur.

:::support
Cette séance pose les bases utilisées dans tout le cours : exécuter un programme,
représenter une donnée, effectuer un calcul, communiquer avec l'utilisateur et
prendre une décision. Les séances suivantes permettront d'organiser ces traitements
et de les appliquer à des séries de mesures.
:::
---
## Architecture matérielle

Un programme utilise plusieurs ressources de l'ordinateur :

| Élément | Rôle principal |
|---|---|
| **CPU** | exécuter les instructions |
| **RAM** | accueillir le programme et les données en cours d'utilisation |
| **Stockage** | conserver durablement programmes et fichiers |
| **Périphériques** | échanger avec l'extérieur |

:::diagram
Fichier sur le stockage
Programme et données en RAM
Traitement par le CPU
:::

:::support
La RAM est une mémoire de travail rapide mais volatile : son contenu disparaît
lorsque la machine est éteinte. Le CPU exécute des instructions machine ; dans
notre cas, l'interpréteur fait le lien entre le code Python et leur exécution.
Les périphériques regroupent notamment le clavier, l'écran et les capteurs.
:::
---
## Architecture logicielle

Le **système d'exploitation** gère la mémoire, les fichiers, les périphériques et le lancement des applications.

Dans son usage courant, un programme Python suit cette chaîne :

:::diagram
Fichier `mesure.py`
Interpréteur Python
Instructions exécutées
:::

```python
print("Première mesure")
```

:::support
On oppose souvent les programmes compilés, traduits avant leur exécution, aux
programmes interprétés, pris en charge par un interpréteur. Cette opposition est
un modèle simplifié : l'implémentation de référence de Python produit également
une représentation intermédiaire appelée bytecode.
:::
---
## Console interactive et script

Python peut être utilisé de deux manières complémentaires :

| Console interactive | Script `.py` |
|---|---|
| tester rapidement une instruction | conserver un programme |
| obtenir un résultat immédiat | enchaîner plusieurs traitements |
| expérimenter | modifier et réutiliser le code |

```text
>>> 2 + 3
5
```

Un script peut être lancé depuis un éditeur ou avec `python mesure.py` dans un terminal (`py mesure.py` sur certaines installations Windows).
---
## Variables et affectation

Une variable permet de donner un nom à une valeur pour la réutiliser :

```python
temperature = 20.5
```

```text
temperature = 20.5
───────────   ────
    nom       valeur
```

`=` réalise une **affectation**. Une nouvelle affectation remplace la valeur associée au nom.

:::support
Une affectation n'est pas une égalité mathématique. Python évalue l'expression
située à droite, puis associe son résultat au nom situé à gauche. Des noms comme
`temperature` ou `nombre_mesures` rendent le programme plus compréhensible que
des noms génériques comme `x` ou `a`.
:::
---
## Types de données

Le type décrit la nature d'une valeur et détermine les opérations possibles :

| Type | Nature | Exemple |
|---|---|---|
| `int` | nombre entier | `12` |
| `float` | nombre à virgule flottante | `20.5` |
| `str` | chaîne de caractères | `"capteur A"` |
| `bool` | résultat logique | `True` ou `False` |

```python
print(type(20.5))  # <class 'float'>
print(type(20 > 10))  # <class 'bool'>
```

:::support
Python utilise un typage dynamique : le type est associé à la valeur et déterminé
pendant l'exécution. La fonction `type()` permet d'observer le type d'une donnée,
ce qui est notamment utile pour comprendre une erreur de conversion.
:::
---
## Conversions explicites

Une donnée doit parfois changer de représentation avant d'être utilisée :

:::diagram
Texte `"20.5"`
Conversion avec `float()`
Nombre `20.5`
:::

```python
temperature = float("20.5")
nombre_mesures = int("12")
message = str(20.5)
```

`float()`, `int()` et `str()` produisent une nouvelle valeur du type demandé. Une conversion échoue si le contenu n'est pas compatible : `float("vingt")` provoque une erreur.
---
## Opérateurs arithmétiques

Python fournit les opérations usuelles :

| Expression | Opération | Résultat pour `a = 7`, `b = 2` |
|---|---|---:|
| `a + b` | addition | `9` |
| `a - b` | soustraction | `5` |
| `a * b` | multiplication | `14` |
| `a / b` | division | `3.5` |
| `a // b` | quotient arrondi vers le bas | `3` |
| `a % b` | reste | `1` |
| `a ** b` | puissance | `49` |

Les parenthèses permettent de rendre l'ordre des calculs explicite.

:::support
L'opérateur `//` est parfois appelé « division entière », mais cette expression
peut être trompeuse : le résultat est arrondi vers le bas. Ainsi, `-7 // 2`
produit `-4`. Le reste `%` permet notamment de tester si un entier est pair avec
la condition `n % 2 == 0`.
:::
---
## Affectation, comparaison et mise à jour

Il faut distinguer la modification d'une variable et la comparaison de deux valeurs :

| Écriture | Rôle | Résultat |
|---|---|---|
| `temperature = 20` | affecter | la variable reçoit `20` |
| `temperature == 20` | comparer | `True` ou `False` |
| `temperature != 20` | comparer | `True` ou `False` |

Deux écritures possibles pour la même mise à jour :

```python
nombre = nombre + 1
# ou, sous forme abrégée : nombre += 1
```

Autres comparaisons : `<`, `<=`, `>` et `>=`.
---
## Précision des nombres flottants

Les nombres décimaux ne peuvent pas tous être représentés exactement en mémoire :

```python
resultat = 0.1 + 0.2
print(resultat)
```

```text
0.30000000000000004
```

Un `float` représente donc une valeur numérique avec une précision limitée. Cette approximation est normale et doit être prise en compte lors des comparaisons.

:::support
De nombreux nombres décimaux ne possèdent pas de représentation binaire finie.
Pour comparer deux résultats calculés, on utilise parfois une tolérance, par
exemple `abs(a - b) < 1e-9`, plutôt qu'une égalité stricte avec `==`.
:::
---
## Saisie et conversion

`input()` permet de recevoir une information saisie au clavier. Son résultat est toujours une chaîne de caractères :

```python
saisie = input("Température : ")
temperature = float(saisie)
```

:::diagram
Clavier
`input()`
Texte `"20.5"`
`float()`
Nombre `20.5`
:::

Après la conversion, `temperature` peut être utilisée dans un calcul.

:::support
`input()` interrompt le programme jusqu'à la validation de la saisie. Une saisie
invalide comme `vingt` provoque une erreur pendant la conversion. La validation
des données sera approfondie plus tard ; pour le moment, on suppose que
l'utilisateur fournit une valeur compatible.
:::
---
## Affichage et f-strings

`print()` affiche une information. Une f-string permet d'intégrer une valeur dans un texte :

```python
temperature = 20.456
print(f"Température : {temperature:.1f} °C")
```

```text
Température : 20.5 °C
```

Le format `.1f` affiche la valeur arrondie à un chiffre après la virgule. Il modifie l'affichage, pas la valeur utilisée dans les calculs.
---
## Prendre une décision

Un programme peut adapter son comportement à la valeur d'une mesure :

```python
if temperature < 0:
    print("Risque de gel")
elif temperature < 30:
    print("Température dans la plage prévue")
else:
    print("Seuil supérieur dépassé")
```

Les conditions sont évaluées dans l'ordre. Python exécute la première branche dont la condition est vraie ; `else` traite les autres cas. L'indentation délimite les instructions de chaque branche.

:::support
`if` introduit le premier test, `elif` ajoute un test lorsque les précédents sont
faux et `else` traite tous les autres cas. Une seule branche de cette structure
est exécutée. Si le second test est atteint, Python sait déjà que la température
est supérieure ou égale à zéro.
:::
---
## Combiner des conditions

Dans une condition, les opérateurs logiques permettent de combiner plusieurs tests :

| Opérateur | Signification |
|---|---|
| `and` | les deux conditions sont vraies |
| `or` | au moins une condition est vraie |
| `not` | inverse une valeur logique |

```python
if temperature >= 0 and temperature < 30:
    print("Température dans la plage prévue")
```

Les parenthèses peuvent clarifier une condition complexe. Si elle devient difficile à lire, il est préférable de la décomposer.
---
## Comprendre les erreurs

Une erreur fait partie du travail de programmation. Il faut d'abord identifier sa catégorie :

| Catégorie | Exemple |
|---|---|
| **syntaxe** | parenthèse ou deux-points absents |
| **exécution** | conversion impossible avec `float("abc")` |
| **logique** | seuil incorrect dans une condition |

Les erreurs de syntaxe et d'exécution produisent généralement un message indiquant la ligne et la nature du problème. Une erreur de logique doit être repérée en vérifiant les résultats.

:::support
Une erreur de syntaxe empêche Python de comprendre le programme. Une erreur
d'exécution apparaît pendant une opération impossible. Une erreur de logique est
plus discrète : le programme s'exécute, mais produit un mauvais résultat. Dans un
traceback, la dernière ligne donne généralement le type d'erreur.
:::
---
## Synthèse de la séance

Nous pouvons maintenant construire une première chaîne de traitement :

:::diagram vertical
Donnée extérieure
Saisie avec `input()`
Conversion du texte en nombre
Calcul et comparaison
Décision avec `if`
Résultat affiché
:::

:::support
Le programme sait recevoir une donnée, la convertir, la mémoriser, effectuer un
calcul, prendre une décision et afficher un résultat. La séance suivante permettra
d'organiser les traitements avec des fonctions et de manipuler plusieurs valeurs.
:::
