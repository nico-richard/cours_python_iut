# Séance 3
## Conserver et exploiter des données scientifiques

### Fichiers texte, données tabulaires et tableaux NumPy

Les variables d'un programme sont temporaires. Pour conserver des mesures après son arrêt, les transmettre à un autre logiciel ou recommencer une analyse, il faut les enregistrer dans un fichier dont l'organisation est connue.

À la fin de la séance, vous devez être capables de choisir un format simple, de lire et d'écrire un fichier texte, d'extraire les valeurs d'un CSV et d'effectuer des calculs avec NumPy.

:::support
Cette séance distingue le stockage des données de leur traitement. La première
partie présente les fichiers et leur lecture en Python. La seconde introduit les
tableaux NumPy utilisés pour le calcul scientifique.
:::
---
## Une variable est temporaire

Pendant l'exécution, des mesures peuvent être placées dans une liste :

```python
temperatures = [18.2, 18.5, 18.9, 19.1]
```

Cette liste existe dans la mémoire vive. Lorsque le programme s'arrête, son contenu n'est pas conservé automatiquement.

:::diagram
Programme en cours
Variables en mémoire vive
Arrêt du programme
Données perdues
:::

Un fichier permet de conserver les valeurs sur un support persistant.
---
## Pourquoi utiliser des fichiers ?

Un fichier permet de :

- conserver les données après l'arrêt du programme ;
- les échanger avec un instrument ou un autre logiciel ;
- traiter automatiquement un grand nombre de valeurs ;
- archiver les données d'origine ;
- recommencer une analyse sans refaire l'acquisition.

:::diagram
Acquisition
Fichier
Lecture
Traitement
Résultat
:::

:::support
La conservation des données brutes contribue à la traçabilité et à la
reproductibilité d'un résultat scientifique.
:::
---
## Nom, extension, chemin et contenu

Dans le chemin `data/mesures.csv` :

| Élément | Exemple | Rôle |
|---|---|---|
| nom | `mesures.csv` | identifier le fichier |
| extension | `.csv` | indiquer son format attendu |
| dossier | `data` | organiser son emplacement |
| contenu | lignes de mesures | représenter les données |

Changer l'extension ne transforme pas le contenu du fichier.

:::support
**À retenir :** renommer `mesures.txt` en `mesures.csv` ne suffit pas à créer un
fichier CSV. C'est l'organisation du contenu qui définit réellement le format.
:::
---
## Fichier texte ou fichier binaire ?

| Fichier texte | Fichier binaire |
|---|---|
| représente des caractères | suit une organisation propre à son format |
| peut être inspecté dans un éditeur | nécessite généralement un logiciel adapté |
| simple à produire et à échanger | souvent plus compact ou rapide à traiter |
| TXT, CSV, TSV, JSON, XML | images, XLSX, formats scientifiques |

Dans un fichier texte, un encodage comme UTF-8 permet de convertir les octets du fichier en caractères.

:::support
Tous les fichiers sont stockés sous forme d'octets. La distinction porte sur la
manière de les interpréter : encodage de caractères pour un fichier texte,
structure propre au format pour un fichier binaire.
:::
---
## Formats de fichiers texte courants

| Format | Organisation | Usage fréquent |
|---|---|---|
| TXT | libre ou une valeur par ligne | notes, séries simples |
| CSV | colonnes séparées par `,` ou `;` | données tabulaires |
| TSV ou TAB | colonnes séparées par une tabulation | données tabulaires |
| JSON | objets et listes avec des clés | échange entre programmes |
| XML | éléments délimités par des balises | documents structurés |

Ces formats sont tous textuels, mais leur contenu n'est pas organisé de la même manière.

:::support
JSON et XML sont présentés pour situer les principaux formats textuels. Leur
lecture en Python demande des outils spécifiques et n'est pas étudiée ici.
:::
---
## Choisir un format adapté

| Besoin | Exemple de contenu | Format possible |
|---|---|---|
| série simple | une température par ligne | TXT |
| tableau | `temps;temperature` | CSV ou TSV |
| données avec des clés | `{"temperature": 20.1}` | JSON |
| structure avec des balises | `<temperature>20.1</temperature>` | XML |
| données volumineuses | format propre au logiciel | binaire |

Le choix dépend de l'organisation des données, des logiciels qui devront les relire, de la lisibilité et du volume à stocker.
---
## Chemin relatif et chemin absolu

| Chemin relatif | Chemin absolu |
|---|---|
| `data/mesures.csv` | `C:/projet/data/mesures.csv` |
| interprété depuis le dossier de travail | décrit l'emplacement complet |
| facilite le déplacement du projet | dépend davantage de l'ordinateur |

Le **répertoire de travail courant** est le dossier à partir duquel Python interprète un chemin relatif. Il n'est pas nécessairement identique au dossier du script.

:::support
Une erreur indiquant que le fichier est introuvable provient souvent d'un chemin
incorrect ou d'un répertoire de travail différent de celui qui était prévu.
:::
---
## Ouvrir et fermer un fichier

```python
fichier = open("temperatures.txt", "r", encoding="utf-8")
contenu = fichier.read()
fichier.close()
```

`open()` renvoie un **objet fichier**. `close()` libère ensuite la ressource ; l'objet ne peut plus être utilisé pour lire ou écrire.

| Mode | Action | Fichier existant |
|---|---|---|
| `r` | lire | conservé |
| `w` | écrire | contenu effacé |
| `a` | ajouter à la fin | conservé |
| `x` | créer | provoque une erreur |

:::support
Le mode `r` est utilisé par défaut. L'argument `encoding="utf-8"` indique comment
décoder ou encoder les caractères d'un fichier texte. La fermeture est notamment
importante après une écriture, car des données peuvent encore attendre en mémoire.
:::
---
## `read()`, `readline()` et `readlines()`

```python
contenu = fichier.read()       # une seule chaîne
ligne = fichier.readline()    # la ligne suivante
lignes = fichier.readlines()  # une liste de lignes
```

| Méthode | Valeur renvoyée | Mémoire |
|---|---|---|
| `read()` | tout le texte restant | charge tout le contenu |
| `readline()` | une seule ligne | charge une ligne |
| `readlines()` | la liste des lignes restantes | charge tout le contenu |

Les fins de ligne `\n` sont conservées. `readline()` renvoie une chaîne vide lorsque la fin du fichier est atteinte.

:::support
L'objet fichier mémorise une position de lecture. Chaque appel reprend à cette
position. `read(nombre)` permet aussi de lire au maximum un nombre donné de
caractères.
:::
---
## Choisir une manière de lire

```python
with open("temperatures.txt", "r", encoding="utf-8") as fichier:
    for ligne in fichier:
        print(ligne.strip())
```

| Besoin | Solution adaptée |
|---|---|
| récupérer tout un petit fichier | `read()` |
| examiner seulement la ligne suivante | `readline()` |
| obtenir immédiatement une liste de lignes | `readlines()` |
| traiter progressivement les lignes | boucle `for` |

Le parcours avec `for` évite de construire une chaîne ou une liste contenant tout le fichier.
---
## Pourquoi utiliser `with` ?

Sans `with`, il faut fermer explicitement le fichier :

```python
fichier = open("temperatures.txt", "r", encoding="utf-8")
contenu = fichier.read()
fichier.close()
```

La forme recommandée est :

```python
with open("temperatures.txt", "r", encoding="utf-8") as fichier:
    contenu = fichier.read()
```

Le bloc délimite l'utilisation du fichier et garantit sa fermeture, même si une erreur interrompt le traitement.

:::support
Après le bloc, `contenu` existe encore, mais l'objet `fichier` est fermé. `with`
évite d'oublier `close()` sur l'un des chemins possibles du programme.
:::
---
## Du texte à une liste de nombres

La lecture produit des chaînes de caractères. Il faut nettoyer, convertir puis mémoriser chaque valeur :

```python
temperatures = []

with open("temperatures.txt", "r", encoding="utf-8") as fichier:
    for ligne in fichier:
        texte = ligne.strip()
        temperature = float(texte)
        temperatures.append(temperature)
```

:::diagram
Ligne du fichier
`strip()`
`float()`
Ajout à la liste
:::

:::support
Une ligne vide, une unité ajoutée au nombre ou un texte inattendu peut empêcher
la conversion avec `float()`. Le programme doit connaître les conventions du
fichier qu'il lit.
:::
---
## Écrire dans un fichier

```python
moyenne = 18.68

with open("rapport.txt", "w", encoding="utf-8") as fichier:
    fichier.write(f"Température moyenne : {moyenne:.2f} °C\n")
```

`write()` attend une chaîne et n'ajoute pas automatiquement de retour à la ligne. Elle renvoie le nombre de caractères écrits.

:::support
**Attention :** le mode `w` efface le contenu précédent dès l'ouverture. Le mode
`a` ajoute les nouvelles données à la fin. Le mode `x` convient lorsqu'un fichier
existant ne doit jamais être remplacé.
:::
---
## Le cas d'un fichier CSV

Un fichier tabulaire place une observation par ligne et une variable par colonne :

```text
temps;temperature
0;20.1
1;20.4
2;20.9
```

| Élément | Rôle |
|---|---|
| première ligne | nommer les colonnes |
| lignes suivantes | représenter les observations |
| `;` | séparer les valeurs |

CSV signifie *Comma-Separated Values*, mais le point-virgule est fréquent lorsque la virgule sert de séparateur décimal.

:::support
Un CSV est un fichier texte, pas un fichier de tableur complet. Il ne conserve
généralement ni formules, ni couleurs, ni mise en page.
:::
---
## Lire un CSV simple avec `split()`

```python
temps = []
temperatures = []

with open("mesures.csv", "r", encoding="utf-8") as fichier:
    fichier.readline()  # ignorer l'en-tête

    for ligne in fichier:
        cellules = ligne.strip().split(";")
        temps.append(float(cellules[0]))
        temperatures.append(float(cellules[1]))
```

`split(";")` transforme la ligne `"1;20.4"` en `['1', '20.4']`. Chaque cellule doit ensuite être convertie.

:::support
Cette méthode convient au format simple utilisé dans le cours. Des CSV peuvent
aussi contenir des champs entre guillemets et des séparateurs intégrés au texte ;
un découpage avec `split()` ne suffit alors plus.
:::
---
## Pourquoi utiliser NumPy ?

Une liste Python regroupe des valeurs, mais elle n'est pas spécialisée dans le calcul numérique. NumPy fournit :

- des tableaux numériques homogènes ;
- des opérations appliquées à toutes les valeurs ;
- des tableaux à plusieurs dimensions ;
- des fonctions de calcul scientifique performantes.

NumPy sert notamment à traiter des mesures, des images, des signaux, des matrices et des résultats de simulation.

```python
import numpy as np
```

NumPy est une bibliothèque externe et `np` est son alias conventionnel.
---
## La brique centrale : le `ndarray`

```python
temperatures = np.array([20.1, 20.4, 20.9])
```

`np.array()` construit un objet de type `ndarray`. Il associe des valeurs, un type commun et une forme :

```python
temperatures.dtype  # type des éléments
temperatures.ndim   # nombre de dimensions : 1
temperatures.shape  # forme : (3,)
temperatures.size   # nombre d'éléments : 3
```

:::support
Lorsque les valeurs fournies n'ont pas toutes le même type, NumPy cherche un type
commun capable de les représenter. Un tableau mélangeant entiers et nombres
décimaux est généralement converti en nombres flottants.
:::
---
## Créer des tableaux

```python
a = np.array([1, 2, 3, 4])
zeros = np.zeros(4)
indices = np.arange(0, 10, 2)
instants = np.linspace(0, 1, 5)
```

| Fonction | Résultat |
|---|---|
| `np.array` | convertit une séquence existante |
| `np.zeros` | crée un tableau rempli de zéros |
| `np.arange` | crée des valeurs séparées par un pas |
| `np.linspace` | répartit un nombre donné de valeurs entre deux bornes |

`np.linspace(0, 1, 5)` inclut les deux bornes et produit cinq valeurs régulièrement espacées.
---
## Indexer et découper un tableau 1D

```python
temperatures = np.array([20.1, 20.4, 20.9, 21.3])

temperatures[0]    # 20.1
temperatures[-1]   # 21.3
temperatures[1:3]  # [20.4, 20.9]
temperatures[:2]   # [20.1, 20.4]
temperatures[2:]   # [20.9, 21.3]
```

Comme pour une liste, le premier index est `0`, un index négatif compte depuis la fin et la borne de fin d'un slicing est exclue.
---
## Tableaux à deux dimensions

```python
tableau = np.array([[1, 2, 3],
                    [4, 5, 6]])

tableau.shape   # (2, 3)
tableau[0, 1]   # ligne 0, colonne 1 : 2
tableau[0, :]   # première ligne
tableau[:, 1]   # deuxième colonne
```

Les indices sont donnés dans l'ordre **ligne, colonne**. `:` signifie « tous les indices » de la dimension concernée.

```python
tableau[0, 0] = 10  # modification d'un élément
```

Un `ndarray` est modifiable, comme une liste.
---
## Opérations sur les tableaux

Les opérations avec un scalaire s'appliquent à tous les éléments :

```python
a = np.array([1, 2, 3])
a + 10  # [11, 12, 13]
a * 2   # [2, 4, 6]
a ** 2  # [1, 4, 9]
```

Les opérations entre tableaux de même forme sont effectuées élément par élément :

```python
b = np.array([10, 20, 30])
a + b  # [11, 22, 33]
a * b  # [10, 40, 90]
a > 1  # [False, True, True]
```

Ces expressions produisent de nouveaux tableaux sans modifier `a` ou `b`.
---
## Calculs sur un tableau

```python
mesures = np.array([18.2, 19.1, 20.0, 19.7])

mesures.sum()   # somme
mesures.mean()  # moyenne
mesures.std()   # écart-type
mesures.min()   # minimum
mesures.max()   # maximum
```

Ces méthodes agrègent plusieurs éléments pour produire un indicateur.

:::support
`std()` calcule ici l'écart-type de la population décrite par le tableau. Une
correction peut être appliquée dans certains traitements statistiques d'un
échantillon, mais cette distinction n'est pas nécessaire ici.
:::
---
## Calculer suivant un axe

```python
tableau = np.array([[1, 2, 3],
                    [4, 5, 6]])

tableau.mean(axis=0)  # [2.5, 3.5, 4.5]
tableau.mean(axis=1)  # [2.0, 5.0]
```

| Axe | Calcul effectué | Résultat restant |
|---|---|---|
| `axis=0` | agrège les lignes | une valeur par colonne |
| `axis=1` | agrège les colonnes | une valeur par ligne |

L'axe indiqué est la dimension parcourue et supprimée par le calcul.
---
## Charger rapidement avec `np.loadtxt`

Pour un fichier numérique régulier, NumPy peut effectuer directement la lecture et les conversions :

```python
donnees = np.loadtxt(
    "mesures.csv",
    delimiter=";",
    skiprows=1,
)

temps = donnees[:, 0]
temperatures = donnees[:, 1]
```

`delimiter` indique le séparateur et `skiprows=1` ignore l'en-tête.

:::support
`np.loadtxt` est seulement un raccourci pour les fichiers simples et entièrement
numériques. Son fonctionnement devient plus clair après avoir appris à ouvrir le
fichier, parcourir ses lignes, séparer ses champs et convertir ses valeurs.
:::
---
## Synthèse de la séance

:::diagram vertical
Fichier sur le stockage
Ouverture avec `open()` ou `with`
Lecture du texte
Séparation et conversion
Création d'un `ndarray`
Calcul avec NumPy
:::

| Besoin | Outil principal |
|---|---|
| lire tout, une ligne ou plusieurs lignes | `read`, `readline`, `readlines` |
| garantir la fermeture | bloc `with` |
| séparer un CSV simple | `split()` |
| stocker des valeurs numériques | `ndarray` |
| transformer ou résumer les mesures | opérations et méthodes NumPy |

La séance suivante utilisera ces données pour produire des graphiques et recevoir des mesures provenant d'un instrument.
