# Séance 3
## Calcul scientifique

Nous savons maintenant programmer les traitements de base.

L'étape suivante consiste à travailler avec de vraies données scientifiques : des fichiers de mesures, des séries de températures et de grandes quantités de valeurs.

Nous allons introduire les bibliothèques Python, les fichiers et surtout **NumPy**, qui permettra de réaliser efficacement des calculs scientifiques.
---
## Pourquoi des bibliothèques ?

Python possède déjà de nombreuses fonctionnalités, mais un langage généraliste ne peut pas fournir toutes les fonctions nécessaires à tous les domaines.

Des bibliothèques permettent de réutiliser du code déjà développé et testé.

On distingue notamment :
- la **bibliothèque standard**, fournie avec Python ;
- les **bibliothèques externes**, installées séparément.

En calcul scientifique, NumPy est une bibliothèque fondamentale.
---
## Modules et bibliothèques

Un **module** est un fichier Python contenant du code réutilisable.

Une **bibliothèque** ou un **package** regroupe généralement plusieurs modules et fournit un ensemble cohérent de fonctionnalités.

Quelques bibliothèques standard : `math`, `random`, `csv`, `os`.

Parmi les bibliothèques externes que nous utiliserons : `numpy`, `matplotlib` et `pyserial`.

L'intérêt est de ne pas réinventer des outils déjà disponibles.
---
## Importer un module

Avant d'utiliser une bibliothèque, Python doit savoir que nous souhaitons l'utiliser.

On utilise pour cela `import`.

```python
import math
math.sqrt(16)
```

On peut aussi importer un élément précis :

```python
from math import sqrt
```

Avec NumPy, la convention courante est :

```python
import numpy as np
```

`np` devient alors un raccourci utilisé dans le reste du programme.
---
## Les fichiers : pourquoi en avons-nous besoin ?

Une variable ne suffit pas pour conserver durablement les résultats d'une expérience.

Si un capteur réalise des mesures pendant plusieurs heures, nous voulons pouvoir conserver les mesures, fermer le programme, puis rouvrir les données plus tard.

Les **fichiers** permettent cette persistance.

Dans ce cours, nous nous intéresserons surtout aux fichiers texte et aux fichiers **CSV**, très utilisés pour échanger des données tabulaires.
---
## Fichiers texte, binaires et chemins

Un fichier texte contient des caractères que nous pouvons interpréter comme du texte : `.txt`, `.csv`, `.json`...

Un fichier binaire contient des données organisées selon un format spécifique : image, tableur, etc.

Pour accéder à un fichier, Python doit connaître son **chemin**.

Un chemin peut être relatif au programme ou absolu sur l'ordinateur.

Comprendre les chemins est essentiel lorsque le programme doit retrouver automatiquement ses fichiers de données.
---
## Ouvrir un fichier avec `with`

Pour lire ou écrire un fichier, Python fournit `open()`.

```python
with open("mesures.txt", "r", encoding="utf-8") as f:
    contenu = f.read()
```

Le bloc `with` garantit que le fichier sera correctement fermé à la fin du traitement.

Les principaux modes sont :
- `r` : lecture ;
- `w` : écriture ;
- `a` : ajout ;
- `x` : création.
---
## Lire un fichier texte

Un fichier peut être parcouru ligne par ligne :

```python
with open("mesures.txt", "r", encoding="utf-8") as f:
    for ligne in f:
        print(ligne.strip())
```

Cela réutilise une notion déjà vue : la boucle `for`.

Une ligne lue depuis un fichier est du **texte**. Si elle contient une mesure numérique, il faudra donc généralement convertir la partie correspondante en `float` ou en `int`.

Cette conversion est une source fréquente d'erreurs chez les débutants.
---
## Lire un fichier CSV (1/2)

Un CSV est un fichier texte dans lequel les données sont organisées en lignes et séparées par un caractère.

Exemple de structure :

```text
temps;temperature
0;20.1
1;20.4
2;20.9
```

Même si nous voyons des nombres, un lecteur de texte les récupère initialement comme des chaînes de caractères.

Il faut donc comprendre la structure du fichier avant de convertir et traiter les données.
---
## Lire un fichier CSV (2/2)

Python fournit le module `csv` pour faciliter cette lecture.

```python
import csv

with open("mesures.csv", newline="", encoding="utf-8") as f:
    lecteur = csv.reader(f)
    for ligne in lecteur:
        ...
```

Le programme peut ensuite séparer les colonnes, ignorer l'en-tête et convertir les valeurs numériques.

Cette étape constitue le passage entre :
**un fichier contenant des caractères** et **des données utilisables pour un calcul scientifique**.
---
## Écrire dans un fichier

La même logique permet de sauvegarder des résultats.

```python
with open("resultats.txt", "w", encoding="utf-8") as f:
    f.write("...")
```

L'écriture est utile pour conserver les résultats d'une analyse ou produire un fichier destiné à un autre logiciel.

Attention au mode `w` : il remplace le contenu existant du fichier.
---
## Qu'est-ce que NumPy ?

Nous pourrions stocker une série de mesures dans une liste Python.

Mais les calculs scientifiques nécessitent souvent de manipuler des tableaux numériques importants et d'effectuer les mêmes opérations sur toutes leurs valeurs.

**NumPy** fournit une structure spécialisée : le `ndarray`.

NumPy apporte notamment des tableaux numériques efficaces, des opérations mathématiques et des fonctions statistiques.

C'est une des briques fondamentales du calcul scientifique en Python.
---
## Créer un `ndarray`

On peut créer un tableau NumPy à partir d'une liste :

```python
a = np.array([1, 2, 3, 4])
```

NumPy permet également de créer directement des tableaux selon un besoin :

```python
np.zeros((3, 4))
np.arange(0, 10, 2)
np.linspace(0, 1, 5)
```

Ces fonctions sont particulièrement utiles pour initialiser des tableaux ou construire des séries régulières.
---
## Dimensions et taille

Un tableau NumPy peut avoir plusieurs dimensions.

```python
a = np.array([[1, 2, 3],
              [4, 5, 6]])
```

Quelques propriétés importantes :
- `shape` : forme du tableau ;
- `ndim` : nombre de dimensions ;
- `size` : nombre total d'éléments ;
- `dtype` : type des éléments.

Un tableau `2 × 3` possède 2 lignes, 3 colonnes, mais 6 éléments.
---
## Accéder aux valeurs

L'accès aux éléments reprend le principe d'indexage vu avec les listes.

Pour un tableau 2D :

```python
mesures[0, 1]
```

On peut sélectionner une ligne entière :

```python
mesures[1, :]
```

ou une colonne :

```python
mesures[:, 0]
```

Cette notation permet de travailler directement sur des sous-ensembles de données.
---
## Opérations vectorisées

L'un des intérêts majeurs de NumPy est de pouvoir appliquer une opération à tout un tableau sans écrire explicitement une boucle.

```python
temperatures_k = temperatures_c + 273.15
```

Python comprend que l'opération doit être appliquée à chaque élément.

On parle d'**opération vectorisée**.

Cela rend souvent le code plus court, plus lisible et plus efficace qu'un parcours manuel.
---
## Statistiques avec NumPy

Une fois les données placées dans un tableau, les fonctions statistiques deviennent très simples.

```python
mesures.mean()
mesures.std()
mesures.min()
mesures.max()
mesures.sum()
```

La moyenne résume le niveau central de la série. L'écart-type renseigne sur la dispersion des valeurs autour de cette moyenne.

Dans un contexte expérimental, ces indicateurs permettent de passer d'une longue liste de mesures à quelques informations synthétiques.
---
## Attention aux axes

Pour un tableau multidimensionnel, il faut préciser ce que l'on souhaite calculer.

```python
tableau.mean(axis=0)
tableau.mean(axis=1)
```

L'argument `axis` indique la direction selon laquelle le calcul est effectué.

Cette notion devient importante dès que les données représentent plusieurs variables, plusieurs capteurs ou plusieurs expériences.
---
## Bilan de la séance

Nous savons maintenant passer :

**fichier → texte → données Python → tableau NumPy → calcul scientifique**

Nous avons vu :
- modules et bibliothèques ;
- lecture et écriture de fichiers ;
- structure d'un CSV ;
- tableaux NumPy ;
- dimensions et indexage ;
- opérations vectorisées ;
- moyenne, écart-type et autres statistiques.

La prochaine étape est de rendre ces résultats compréhensibles visuellement.
---
## À vous de jouer

Direction les exercices de la séance 3 →
