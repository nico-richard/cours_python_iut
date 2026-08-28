# Séance 1
## Machine, logiciel et bases de Python

L'objectif de cette séance est de comprendre les bases nécessaires pour écrire un premier programme Python.

On part de la machine elle-même, puis on progresse vers le programme :
**ordinateur → Python → données → calculs → décisions**.

À la fin de la séance, vous devez être capables de lire et d'écrire un petit programme qui manipule des valeurs et prend des décisions.
---
## Architecture matérielle

Avant d'écrire du code, il est utile de comprendre très rapidement où « vit » un programme et où sont stockées les données qu'il manipule.

Un ordinateur est composé de plusieurs éléments qui collaborent :

- **CPU (processeur)** : exécute les instructions ;
- **RAM** : mémoire de travail, rapide mais volatile ;
- **Stockage** : conserve les fichiers même lorsque l'ordinateur est éteint ;
- **Périphériques** : clavier, écran, capteurs, ports USB et liaison série.

Quand un programme travaille sur des données, celles-ci sont généralement chargées depuis le stockage vers la RAM, puis traitées par le processeur.

Cette distinction deviendra importante lorsque nous travaillerons avec des fichiers de mesures et de grandes quantités de données.
---
## Architecture logicielle

Le matériel seul ne sait pas quoi faire : il a besoin de logiciels qui lui donnent des instructions.

Le **système d'exploitation** (Windows, Linux ou macOS) fait le lien entre le matériel et les applications. Il gère notamment la mémoire, les fichiers, les périphériques et l'exécution des programmes.

Deux modes d'exécution sont couramment distingués :

- **compilation préalable** : le programme est traduit avant son exécution ;
- **exécution par un interpréteur** : un autre programme prend en charge son exécution.

Dans son usage courant, un programme Python est lancé par l'interpréteur Python. En pratique, Python réalise aussi des étapes internes de traduction ; l'opposition « compilé ou interprété » est donc un modèle simplifié.

L'idée importante pour nous est donc :
**notre fichier Python contient des instructions, et Python se charge de les faire exécuter par l'ordinateur.**
---
## Installation et exécution de Python

Avant de programmer, il faut disposer d'un environnement permettant d'écrire et d'exécuter du code.

Python peut être utilisé de deux façons complémentaires :

- **console interactive** : pratique pour tester immédiatement une instruction ;
- **script `.py`** : permet d'enregistrer un programme et de le réexécuter.

La console est utile pour expérimenter. Le fichier `.py` devient rapidement indispensable dès que le programme comporte plusieurs instructions.

L'objectif n'est pas seulement de savoir lancer Python : il faut comprendre que **le code que nous écrivons est un fichier que Python va ensuite exécuter**.
---
## Mémoriser une valeur

Un programme manipule des informations : températures, distances, résultats de mesures, noms ou états d'un système.

Si une information doit être réutilisée, il faut pouvoir la conserver et lui donner un nom.

C'est le rôle d'une **variable**.

Une variable permet donc de donner un nom à une valeur afin de pouvoir la réutiliser ou la modifier au cours du programme.

```python
temperature = 20.5
```

Ici, `temperature` est le nom choisi par le programmeur et `20.5` est la valeur associée.

Le choix des noms est important : un nom explicite rend un programme beaucoup plus facile à comprendre.
---
## Variables et types de données

Toutes les données ne sont pas de même nature.

Une température peut être un nombre réel, un âge un entier, le nom d'un étudiant du texte et l'état d'un système une valeur vraie ou fausse.

Python distingue notamment :

- `int` : nombre entier ;
- `float` : nombre à virgule flottante ;
- `str` : chaîne de caractères ;
- `bool` : valeur logique `True` ou `False`.

Python détermine automatiquement le type d'une valeur.

Le **type** est important car il indique à Python comment cette valeur peut être utilisée.

La fonction `type()` permet de l'observer :

```python
temperature = 20.5
print(type(temperature))  # <class 'float'>
```
---
## Conversions explicites

Les données ne sont pas toujours dans le type dont nous avons besoin.

C'est particulièrement fréquent lorsque les données proviennent d'une saisie utilisateur ou d'un fichier : une information peut être lue comme du texte alors que nous voulons effectuer un calcul numérique.

Python permet de demander explicitement une conversion :

```python
int("42")
float("3.14")
str(42)
```

Certaines conversions sont impossibles. Il faut donc distinguer **une donnée qui ressemble à un nombre** d'une donnée réellement stockée comme nombre.
---
## Opérateurs arithmétiques

Une fois les données stockées, un programme doit pouvoir effectuer des opérations dessus.

Les opérateurs arithmétiques permettent de réaliser les calculs courants :

```python
7 + 2
7 - 2
7 * 2
7 / 2
7 // 2
7 % 2
7 ** 2
```

Quelques points importants :

- `/` réalise une division réelle ;
- `//` calcule le quotient arrondi vers le bas ;
- `%` donne le reste d'une division ;
- `**` représente une puissance.

Ces opérateurs sont la base des calculs que nous effectuerons ensuite sur des mesures.
---
## Comparaisons et affectations

Python propose également des opérateurs pour comparer des valeurs :

```python
a == b
a != b
a < b
a <= b
a > b
a >= b
```

Le résultat d'une comparaison est un **booléen** : `True` ou `False`.

Il existe aussi des affectations combinées :

```python
x += 1
x *= 2
```

Il faut surtout distinguer `=` et `==` :

- `=` affecte une valeur à une variable ;
- `==` teste si deux valeurs sont égales.

Ces comparaisons vont nous permettre de faire prendre des décisions au programme.
---
## Influence du type sur le résultat

Le type d'une donnée influence les opérations que Python réalise.

Par exemple :

```python
7 / 2
```

donne `3.5`, alors que :

```python
7 // 2
```

donne `3`.

Avec les nombres flottants, il faut également connaître une limite importante : leur représentation en mémoire n'est pas infiniment précise.

Ainsi, un calcul comme `0.1 + 0.2` peut produire une valeur très légèrement différente de `0.3`.

Pour un premier cours, retenez surtout :
**un `float` est une approximation numérique, pas un nombre réel mathématique exact.**

:::support
De nombreux nombres décimaux ne peuvent pas être représentés exactement avec
un nombre fini de chiffres binaires. Pour comparer deux résultats calculés,
on utilise donc parfois une tolérance plutôt qu'une égalité stricte.
:::

:::retenir
L'affichage d'un écart minuscule ne signifie pas nécessairement que Python a
effectué une mauvaise opération.
:::
---
## Entrées et sorties simples

Jusqu'ici, les valeurs étaient écrites directement dans le programme.

Un programme devient plus intéressant lorsqu'il peut **communiquer avec l'utilisateur** ou récupérer une information extérieure.

`input()` permet de demander une valeur à l'utilisateur.

Attention : `input()` renvoie toujours une **chaîne de caractères**.

Il faut donc souvent convertir le résultat :

```python
valeur = input("Température : ")
temperature = float(valeur)
```

À l'inverse, `print()` permet d'afficher une information.

Les f-strings permettent de construire facilement un texte contenant des valeurs.

```python
print(f"Température mesurée : {temperature:.1f} °C")
```

Le format `.1f` modifie l'affichage, pas la valeur utilisée dans les calculs.
---
## Tests logiques

Un programme ne doit pas toujours exécuter les mêmes instructions.

Il peut devoir déclencher une alerte si une température dépasse un seuil, afficher un message différent selon une valeur ou effectuer une action uniquement dans certaines conditions.

On utilise pour cela `if`, `elif` et `else`.

```python
if temperature < 0:
    print("Risque de gel")
elif temperature < 30:
    print("Température dans la plage prévue")
else:
    print("Seuil supérieur dépassé")
```

Les opérateurs `and`, `or` et `not` permettent de combiner ou modifier des conditions.

L'**indentation** est essentielle en Python : elle indique quelles instructions appartiennent au bloc conditionnel.
---
## Comprendre les erreurs

Une erreur fait partie du travail de programmation. Il faut identifier sa nature avant de la corriger.

- **erreur de syntaxe** : le code ne respecte pas la grammaire de Python ;
- **erreur d'exécution** : une instruction valide échoue, par exemple `float("abc")` ;
- **erreur de logique** : le programme s'exécute mais produit un résultat incorrect.

Le message d'erreur indique généralement le fichier, la ligne concernée et le type d'erreur. Il doit être lu en commençant par sa dernière ligne.
---
## Bilan de la séance

Nous avons construit les premières briques d'un programme :

1. l'ordinateur fournit les ressources matérielles ;
2. Python permet d'exécuter notre code ;
3. les variables permettent de conserver les données ;
4. les types décrivent la nature des données ;
5. les opérateurs permettent de calculer et comparer ;
6. `input()` et `print()` permettent de communiquer ;
7. les conditions permettent au programme de prendre des décisions.

La prochaine étape consiste à gérer des programmes plus longs :
**comment éviter de répéter du code et comment traiter plusieurs données ?**
