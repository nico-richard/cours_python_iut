# Séance 3
## Calcul scientifique

---

## Modules et bibliothèques

Python possède de nombreuses fonctionnalités intégrées, mais il est impossible de fournir toutes les fonctions utiles directement dans le langage de base.

On utilise donc des **modules** et des **bibliothèques**.

Un module est généralement un fichier Python contenant des fonctions, classes ou données réutilisables.

Une bibliothèque ou un package peut regrouper plusieurs modules.

On distingue notamment :

- **bibliothèque standard** : fournie avec Python (`math`, `random`, `csv`, etc.) ;
- **bibliothèque externe** : développée en dehors de Python et installée séparément (`numpy`, `matplotlib`, etc.).

---

## Installer une bibliothèque

Une bibliothèque externe doit généralement être installée avant de pouvoir être utilisée.

L'outil `pip` permet d'installer des packages Python.

```bash
pip install numpy matplotlib
```

L'installation ajoute les bibliothèques dans l'environnement Python utilisé.

Il est important de distinguer **installer une bibliothèque** et **l'importer dans un programme** : l'installation se fait généralement une fois, alors que l'importation est écrite dans les scripts qui utilisent la bibliothèque.

---

## Importer un module

Le mot-clé `import` permet d'utiliser une bibliothèque dans un programme.

```python
import math

math.sqrt(16)
```

On peut aussi importer directement un élément :

```python
from math import sqrt

sqrt(16)
```

Pour NumPy, on utilise très souvent l'alias `np` :

```python
import numpy as np
```

L'alias est simplement un autre nom utilisé dans le programme pour accéder aux fonctions de la bibliothèque.

---

## Pourquoi utiliser des bibliothèques ?

Une bibliothèque permet de **réutiliser du code déjà développé et testé**.

Cela évite de réimplémenter soi-même des fonctions complexes.

Dans ce cours :

- Python nous permet de construire le programme ;
- NumPy nous fournit des outils de calcul numérique ;
- Matplotlib nous permettra de visualiser les résultats ;
- pyserial permettra plus tard de communiquer avec une carte Arduino.

L'utilisation de bibliothèques est donc une partie essentielle de la programmation scientifique.

---

## Les fichiers : notions générales

Les programmes travaillent souvent avec des données stockées dans des fichiers.

On distingue notamment :

- **fichier texte** : contenu représenté sous forme de caractères (`.txt`, `.csv`, `.json`) ;
- **fichier binaire** : données stockées sous une forme destinée à être interprétée par un logiciel (`.png`, `.xlsx`, etc.).

Un fichier possède également un **chemin** permettant de le localiser.

Exemple de chemin relatif :

```text
data/mesures.csv
```

Exemple de chemin absolu :

```text
/home/user/data/mesures.csv
```

Les chemins relatifs sont pratiques pour construire des projets facilement déplaçables.

---

## Chemins relatifs et répertoire courant

Lorsqu'un programme utilise :

```python
open("mesures.csv")
```

Python cherche le fichier à partir du **répertoire courant** du programme.

Un grand nombre d'erreurs de lecture de fichiers viennent simplement d'un fichier placé au mauvais endroit ou d'un chemin incorrect.

Il est donc important d'organiser clairement les fichiers d'un projet :

```text
projet/
├── programme.py
└── data/
    └── mesures.csv
```

On pourra alors utiliser :

```python
open("data/mesures.csv")
```

---

## Ouvrir un fichier avec `with`

Python fournit la fonction `open()` pour ouvrir un fichier.

```python
with open("mesures.txt", "r", encoding="utf-8") as f:
    contenu = f.read()
```

Le bloc `with` permet de gérer automatiquement la fermeture du fichier.

C'est la méthode recommandée car le fichier sera correctement fermé lorsque le bloc est terminé.

---

## Modes d'ouverture

Le deuxième argument de `open()` indique ce que l'on souhaite faire avec le fichier.

Les modes courants sont :

- `"r"` : lecture ;
- `"w"` : écriture, en remplaçant le contenu existant ;
- `"a"` : ajout à la fin du fichier ;
- `"x"` : création d'un nouveau fichier.

Le choix du mode est important : utiliser `"w"` sur un fichier existant peut supprimer son contenu précédent.

---

## Encodage des fichiers texte

Un fichier texte contient des caractères représentés par des octets.

L'**encodage** indique comment transformer ces octets en caractères.

`UTF-8` est aujourd'hui un encodage très courant.

On peut donc préciser :

```python
open("mesures.txt", encoding="utf-8")
```

Cette précision évite de nombreux problèmes avec les accents et les caractères non ASCII.

---

## Lire un fichier texte

On peut lire l'intégralité du fichier :

```python
with open("mesures.txt", "r", encoding="utf-8") as f:
    contenu = f.read()
```

On peut également parcourir le fichier ligne par ligne :

```python
with open("mesures.txt", "r", encoding="utf-8") as f:
    for ligne in f:
        print(ligne.strip())
```

Le parcours ligne par ligne est particulièrement intéressant pour les fichiers contenant beaucoup de données.

---

## Le format CSV

CSV signifie **Comma-Separated Values**.

Il s'agit d'un format texte simple permettant de représenter des données sous forme de lignes et de colonnes.

Par exemple :

```text
jour,temperature
1,12.4
2,15.2
3,18.1
```

La première ligne contient généralement les **en-têtes** des colonnes.

Chaque ligne suivante contient une observation.

Le séparateur n'est pas nécessairement une virgule : en France, on rencontre fréquemment le point-virgule `;`.

---

## Lire un fichier CSV

Python possède un module standard `csv` permettant de lire ce format.

```python
import csv

with open("mesures.csv", newline="", encoding="utf-8") as f:
    lecteur = csv.reader(f)

    next(lecteur)

    for ligne in lecteur:
        temps, temperature = ligne
        print(temps, temperature)
```

Une donnée lue depuis un CSV est généralement une **chaîne de caractères**.

Si `temperature` doit être utilisée comme un nombre, il faut donc la convertir :

```python
temperature = float(temperature)
```

Cette étape est essentielle avant de réaliser des calculs.

---

## Écrire dans un fichier

On peut également produire un fichier texte avec Python.

```python
with open("resultats.txt", "w", encoding="utf-8") as f:
    f.write("Résultats\n")
    f.write(f"Moyenne : {moyenne:.2f}\n")
```

Cette possibilité permet par exemple de sauvegarder automatiquement les résultats d'une analyse.

---

## Qu'est-ce que NumPy ?

**NumPy** est une bibliothèque Python destinée au **calcul numérique et scientifique**.

Elle fournit notamment le type `ndarray`, un tableau numérique pouvant avoir une ou plusieurs dimensions.

NumPy permet :

- de manipuler efficacement de grandes quantités de nombres ;
- d'effectuer des opérations sur des tableaux entiers ;
- d'utiliser de nombreuses fonctions mathématiques ;
- de réaliser des calculs statistiques.

```python
import numpy as np
```

---

## Pourquoi ne pas utiliser uniquement les listes Python ?

Une liste Python est une structure générale permettant de stocker des objets.

Pour du calcul scientifique, on souhaite souvent manipuler des ensembles homogènes de nombres.

NumPy fournit donc des tableaux spécialisés pour le calcul numérique.

L'intérêt principal est de pouvoir appliquer une opération à **l'ensemble du tableau** sans écrire systématiquement une boucle Python.

---

## Créer un `ndarray`

On peut créer un tableau NumPy à partir d'une liste :

```python
a = np.array([1, 2, 3, 4])
```

NumPy fournit également des fonctions de création :

```python
np.zeros((3, 4))
np.arange(0, 10, 2)
np.linspace(0, 1, 5)
```

Ces fonctions sont particulièrement pratiques pour générer des données numériques ou initialiser des tableaux.

---

## Tableaux multidimensionnels

Un `ndarray` peut posséder plusieurs dimensions.

```python
a = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
```

On peut interpréter ce tableau comme une matrice contenant :

- 2 lignes ;
- 3 colonnes.

Les tableaux multidimensionnels sont très utiles pour représenter des séries de mesures contenant plusieurs variables.

---

## Dimensions et taille

NumPy fournit plusieurs informations importantes sur un tableau :

```python
a.shape
a.ndim
a.size
a.dtype
```

- `shape` : taille de chaque dimension ;
- `ndim` : nombre de dimensions ;
- `size` : nombre total d'éléments ;
- `dtype` : type des éléments stockés.

Ces informations permettent de vérifier la structure des données avant d'effectuer des calculs.

---

## Accéder aux valeurs d'un tableau

L'indexation NumPy reprend le principe vu avec les listes.

Pour un tableau 2D :

```python
mesures[0, 1]
```

permet d'accéder à une valeur précise.

On peut également sélectionner une ligne ou une colonne :

```python
mesures[1, :]
mesures[:, 0]
```

Le slicing est donc essentiel pour extraire une partie des données.

---

## Opérations vectorisées

L'un des grands intérêts de NumPy est la **vectorisation**.

Avec un tableau :

```python
temperatures_c = np.array([20.0, 21.5, 19.8])
```

on peut écrire :

```python
temperatures_k = temperatures_c + 273.15
```

L'opération est appliquée automatiquement à chaque élément.

On peut donc éviter une boucle explicite pour de nombreux calculs numériques.

Cela rend souvent le code plus court, plus lisible et plus performant.

---

## Fonctions mathématiques NumPy

NumPy fournit de nombreuses fonctions pour effectuer des calculs sur les tableaux :

```python
np.sqrt(x)
np.abs(x)
np.sin(x)
np.cos(x)
np.exp(x)
```

Ces fonctions sont généralement conçues pour fonctionner directement sur des tableaux NumPy.

On peut donc effectuer des calculs sur une série complète de mesures.

---

## Statistiques avec NumPy

NumPy fournit directement les opérations statistiques courantes.

```python
mesures.mean()
mesures.std()
mesures.min()
mesures.max()
mesures.sum()
```

On peut également utiliser les fonctions :

```python
np.mean(mesures)
np.std(mesures)
```

La moyenne donne une indication de la valeur centrale de la série.

L'écart-type mesure la **dispersion des valeurs autour de la moyenne** : plus il est grand, plus les valeurs sont dispersées.

---

## Moyenne et écart-type

Pour une série de températures, on peut calculer :

```python
moyenne = np.mean(temperatures)
ecart_type = np.std(temperatures)
```

La moyenne permet de caractériser le niveau moyen de température.

L'écart-type permet de caractériser la variabilité de la série.

Il faut cependant garder à l'esprit qu'un calcul statistique n'a de sens que si les données et leur contexte sont correctement compris.

---

## Calculs sur plusieurs dimensions

Pour un tableau 2D, on peut effectuer les calculs selon un axe.

```python
tableau = np.array([
    [1, 2],
    [3, 4]
])
```

```python
tableau.mean(axis=0)
```

calcule une moyenne pour chaque colonne.

```python
tableau.mean(axis=1)
```

calcule une moyenne pour chaque ligne.

La notion d'axe est essentielle lorsque l'on travaille avec des tableaux contenant plusieurs séries de mesures.

---

## À retenir

À la fin de cette séance, vous devez savoir :

- ce qu'est un module et une bibliothèque ;
- installer et importer une bibliothèque ;
- distinguer fichier texte et fichier binaire ;
- utiliser un chemin de fichier ;
- ouvrir, lire et écrire un fichier ;
- comprendre la structure d'un CSV ;
- convertir les données lues en nombres ;
- créer un tableau NumPy ;
- comprendre les dimensions d'un `ndarray` ;
- accéder à ses valeurs ;
- effectuer des opérations vectorisées ;
- calculer des statistiques avec NumPy.

---

## À vous de jouer

Direction les exercices de la séance 3 →
