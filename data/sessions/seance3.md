# Séance 3
## Exploiter des données scientifiques

### Fichiers, CSV et calcul avec NumPy

Les données d'une expérience doivent être conservées, relues et transformées avant de produire des résultats.

À la fin de la séance, vous devez être capables de lire un fichier de mesures, de convertir son contenu et d'effectuer des calculs simples avec NumPy.

:::support
Cette séance construit la chaîne qui relie un fichier à une analyse numérique.
Elle réutilise les conversions, les listes et les boucles, puis introduit les
tableaux NumPy adaptés au calcul scientifique.
:::
---
## Modules et bibliothèques

Une bibliothèque fournit du code déjà développé pour un domaine particulier.

| Élément | Rôle |
|---|---|
| **module** | unité de code importable, souvent un fichier `.py` |
| **package** | ensemble organisé de modules |
| **bibliothèque standard** | installée avec Python |
| **bibliothèque externe** | installée séparément |

Exemples : `math`, `csv`, `numpy`, `matplotlib` et `serial`.

:::support
Dans l'usage courant, les mots package et bibliothèque sont parfois employés de
manière souple. L'idée essentielle est la réutilisation : on s'appuie sur des
fonctions testées au lieu de reconstruire tous les outils nécessaires.
:::
---
## Installer et importer

Une bibliothèque externe est installée une fois dans l'environnement Python :

```text
python -m pip install numpy
```

Elle est ensuite importée dans chaque programme qui l'utilise :

```python
import math
from math import sqrt
import numpy as np
```

Avec `import numpy as np`, `np` est un alias court et conventionnel.

:::support
`import math` conserve le nom du module dans les appels, par exemple
`math.sqrt(16)`. `from math import sqrt` permet d'écrire directement `sqrt(16)`,
mais rend l'origine de la fonction moins visible. L'installation doit être faite
dans le même environnement que celui qui exécute le programme.
:::
---
## Conserver les données

Une variable existe seulement pendant l'exécution du programme. Un fichier permet de retrouver les données après son arrêt.

```text
programme en cours → variables en RAM
expérience terminée → données conservées dans un fichier
```

Les fichiers permettent également d'échanger des mesures avec un tableur, un instrument ou un autre programme.
---
## Formats et chemins

Un fichier **texte** contient des caractères directement lisibles, tandis qu'un fichier **binaire** suit une organisation qui dépend de son format.

| Chemin relatif | Chemin absolu |
|---|---|
| `data/mesures.csv` | `C:/projet/data/mesures.csv` |
| dépend du dossier de travail | désigne un emplacement complet |

Le format du fichier et son extension ne suffisent pas : le programme doit connaître l'organisation réelle des données.

:::support
Les fichiers `.txt`, `.csv` et `.json` sont des formats textuels. Les images,
certains fichiers de tableur et de nombreux formats scientifiques sont binaires.
Un chemin relatif est interprété à partir du dossier de travail courant, qui peut
différer du dossier où se trouve le script.
:::
---
## Ouvrir un fichier avec `with`

```python
with open("mesures.txt", "r", encoding="utf-8") as fichier:
    contenu = fichier.read()
```

Le bloc `with` ferme automatiquement le fichier à sa sortie, même si une erreur survient.

| Mode | Action |
|---|---|
| `r` | lire un fichier existant |
| `w` | écrire en remplaçant le contenu |
| `a` | ajouter à la fin |
| `x` | créer un nouveau fichier |

:::support
Le mode de lecture `r` est utilisé par défaut. Le paramètre `encoding="utf-8"`
indique comment les octets du fichier texte sont convertis en caractères. Le mode
`w` doit être utilisé avec prudence car il efface le contenu précédent.
:::
---
## Lire un fichier ligne par ligne

Une boucle permet de traiter un fichier sans charger tout son contenu en une seule fois :

```python
with open("mesures.txt", "r", encoding="utf-8") as fichier:
    for ligne in fichier:
        texte = ligne.strip()
        mesure = float(texte)
        print(mesure)
```

:::diagram
Ligne du fichier
Texte nettoyé
Conversion
Nombre `float`
:::

:::support
Chaque ligne contient généralement un caractère de fin de ligne retiré par
`strip()`. La conversion peut échouer si une ligne est vide ou mal formée. Dans
une application réelle, il faut définir une stratégie pour ces données invalides.
:::
---
## Structure d'un fichier CSV

Un CSV représente des données tabulaires dans un fichier texte :

```text
temps;temperature
0;20.1
1;20.4
2;20.9
```

| Ligne | Rôle |
|---|---|
| première ligne | noms des colonnes |
| lignes suivantes | observations |
| `;` | séparateur utilisé ici |

Les valeurs visibles comme des nombres sont d'abord lues comme du texte.

:::support
CSV signifie *Comma-Separated Values*, mais le séparateur dépend des usages et de
la configuration régionale. En France, le point-virgule est fréquent afin de ne
pas le confondre avec la virgule décimale. Le séparateur doit être indiqué au
lecteur lorsque ce n'est pas une virgule.
:::
---
## Lire et convertir un CSV

```python
import csv

temps = []
temperatures = []

with open("mesures.csv", newline="", encoding="utf-8") as fichier:
    lecteur = csv.reader(fichier, delimiter=";")
    next(lecteur)  # ignorer l'en-tête

    for ligne in lecteur:
        temps.append(float(ligne[0]))
        temperatures.append(float(ligne[1]))
```

:::diagram
Fichier
Lignes
Colonnes
Conversions
Listes numériques
:::

:::support
`csv.reader` gère correctement les séparateurs et les champs éventuellement
protégés par des guillemets. `next(lecteur)` consomme la première ligne. Cette
version suppose que le fichier possède un en-tête et que chaque ligne contient
deux nombres valides.
:::
---
## Écrire un résultat

Le mode `w` permet de produire un rapport ou un nouveau fichier de données :

```python
moyenne = 20.47

with open("rapport.txt", "w", encoding="utf-8") as fichier:
    fichier.write(f"Moyenne : {moyenne:.2f} °C\n")
```

`write()` attend une chaîne de caractères et n'ajoute pas automatiquement de retour à la ligne.

:::support
L'écriture permet de conserver un résultat ou de le transmettre à un autre outil.
Pour produire un véritable CSV, il est préférable d'utiliser `csv.writer` plutôt
que d'assembler manuellement les séparateurs.
:::
---
## NumPy et le calcul scientifique

Une liste Python peut stocker des mesures, mais elle n'est pas spécialisée dans le calcul numérique.

```python
temperatures = np.array([20.1, 20.4, 20.9])
```

Un `ndarray` NumPy fournit :

- des données numériques homogènes ;
- des tableaux à plusieurs dimensions ;
- des opérations appliquées à l'ensemble des valeurs ;
- des fonctions de calcul scientifique.

:::support
NumPy stocke les éléments de manière régulière et exécute de nombreuses opérations
dans du code optimisé. Pour de grandes séries numériques, cela rend les calculs
plus rapides et leur écriture souvent plus concise qu'avec des boucles Python.
:::
---
## Créer un tableau NumPy

```python
import numpy as np

a = np.array([1, 2, 3, 4])
zeros = np.zeros(4)
indices = np.arange(0, 10, 2)
temps = np.linspace(0, 1, 5)
```

| Fonction | Usage |
|---|---|
| `np.array` | convertir une séquence existante |
| `np.zeros` | initialiser avec des zéros |
| `np.arange` | créer une progression avec un pas |
| `np.linspace` | répartir un nombre donné de valeurs |
---
## Dimensions et type des éléments

```python
tableau = np.array([[1, 2, 3],
                    [4, 5, 6]])
```

| Propriété | Valeur | Signification |
|---|---|---|
| `tableau.shape` | `(2, 3)` | 2 lignes et 3 colonnes |
| `tableau.ndim` | `2` | 2 dimensions |
| `tableau.size` | `6` | 6 éléments au total |
| `tableau.dtype` | type entier | type commun des éléments |

Un `ndarray` possède une forme et un type d'éléments homogène.
---
## Accéder aux valeurs

Pour un tableau à deux dimensions, les indices sont donnés dans l'ordre **ligne, colonne** :

```python
tableau[0, 1]   # élément de la ligne 0, colonne 1
tableau[1, :]   # deuxième ligne
tableau[:, 0]   # première colonne
tableau[0:2, 1:3]
```

Le symbole `:` signifie ici « tous les indices » de la dimension concernée.

:::support
L'indexage commence à zéro comme pour les listes. NumPy étend le slicing à
plusieurs dimensions en séparant les sélections par une virgule.
:::
---
## Opérations vectorisées

NumPy applique une opération à tous les éléments d'un tableau :

```python
temperatures_c = np.array([18.2, 19.1, 20.0])
temperatures_k = temperatures_c + 273.15
```

:::diagram
Tableau en degrés Celsius
Addition de `273.15`
Tableau en kelvins
:::

La vectorisation remplace ici une boucle explicite par une expression portant sur le tableau entier.
---
## Statistiques descriptives

```python
mesures = np.array([18.2, 19.1, 20.0, 19.7])

mesures.mean()  # moyenne
mesures.std()   # écart-type
mesures.min()   # minimum
mesures.max()   # maximum
mesures.sum()   # somme
```

La moyenne résume le niveau central ; l'écart-type décrit la dispersion autour de cette moyenne.

:::support
`std()` calcule ici l'écart-type de la population décrite par le tableau. Dans un
cours de statistique, une correction peut être appliquée lorsqu'un échantillon est
utilisé pour estimer une population. Cette distinction n'est pas nécessaire pour
les premiers traitements descriptifs de cette séance.
:::
---
## Calculer suivant un axe

```python
tableau = np.array([[1, 2, 3],
                    [4, 5, 6]])

tableau.mean(axis=0)  # [2.5, 3.5, 4.5]
tableau.mean(axis=1)  # [2.0, 5.0]
```

| Calcul | Résultat |
|---|---|
| `axis=0` | une moyenne par colonne |
| `axis=1` | une moyenne par ligne |

Si les lignes sont des capteurs, `axis=1` calcule une moyenne par capteur.

:::support
Une manière rigoureuse de comprendre `axis` est de considérer que l'axe indiqué
est supprimé par le calcul. Avec `axis=0`, les lignes sont agrégées et il reste une
valeur par colonne. Avec `axis=1`, les colonnes sont agrégées et il reste une
valeur par ligne.
:::
---
## Synthèse de la séance

La chaîne complète de traitement est désormais :

:::diagram vertical
Fichier CSV
Lecture des chaînes de caractères
Conversion en listes numériques
Création du tableau NumPy
Calcul des indicateurs scientifiques
:::

La séance suivante utilisera ces données pour produire des représentations graphiques et réaliser une acquisition.
