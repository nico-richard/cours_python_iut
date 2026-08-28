# Séance 2
## Structures

Dans la séance précédente, nous avons écrit des programmes capables de manipuler des valeurs et de prendre des décisions.

Mais un vrai programme devient rapidement plus complexe :
- certaines instructions doivent être réutilisées ;
- nous devons stocker plusieurs valeurs ;
- nous devons parcourir des données ;
- nous devons répéter des traitements.

Cette séance introduit les structures qui permettent d'organiser ces programmes.
---
## Pourquoi des fonctions ?

Imaginez que le même calcul apparaisse à plusieurs endroits dans un programme.

Copier-coller les mêmes instructions fonctionne au début, mais rend le programme difficile à modifier et augmente le risque d'erreur.

Une **fonction** permet de regrouper un traitement sous un nom et de le réutiliser.

```python
def convertir_c_en_k(temperature_c):
    resultat = temperature_c + 273.15
    return resultat
```

Une fonction peut recevoir des données en entrée et produire une donnée en sortie.

Elle permet donc de transformer un programme long en plusieurs petits traitements compréhensibles.
---
## Paramètres et valeurs par défaut

Les paramètres rendent une fonction générale.

Plutôt que d'écrire une fonction pour une seule température, nous pouvons lui transmettre la valeur à traiter.

```python
def convertir(valeur, unite="celsius"):
    ...
```

Un **paramètre** est une information fournie à la fonction.

Une **valeur par défaut** est utilisée lorsque l'appelant ne fournit pas cette information.

Cela permet d'avoir des fonctions faciles à utiliser tout en conservant une certaine flexibilité.
---
## Fonctions avec / sans valeur de retour

Certaines fonctions calculent un résultat que le reste du programme doit pouvoir réutiliser :

```python
def calculer_moyenne(liste):
    return sum(liste) / len(liste)
```

D'autres réalisent principalement une action, par exemple afficher une alerte.

La distinction importante est :

- **retourner une valeur** permet de réutiliser le résultat ;
- **produire un effet** modifie quelque chose à l'extérieur de la fonction, par exemple l'affichage.

`return` termine également l'exécution de la fonction et renvoie la valeur indiquée.
---
## Portée des variables

Une fonction peut créer ses propres variables.

Ces variables sont dites **locales** : elles appartiennent au contexte d'exécution de la fonction et ne sont pas directement accessibles depuis l'extérieur.

```python
def f():
    x = 1
    return x

x = 5
```

Ici, les deux `x` correspondent à des variables différentes.

En pratique, on cherche généralement à limiter les variables globales et à faire circuler les informations par les paramètres et les valeurs de retour.
---
## Listes : pourquoi en avons-nous besoin ?

Jusqu'ici, une variable contenait généralement une seule valeur.

Mais une série de mesures contient potentiellement des dizaines, des centaines ou des milliers de valeurs.

Il faut donc pouvoir regrouper plusieurs valeurs dans une même structure.

Une **liste** est une séquence ordonnée et modifiable :

```python
mesures = [12.3, 14.1, 13.8]
```

On peut ajouter, modifier ou supprimer des éléments.

Les listes sont très pratiques pour commencer à manipuler des séries de données.
---
## Tuples

Le **tuple** ressemble à une liste, mais il est immuable : une fois créé, son contenu ne peut pas être modifié.

```python
point = (48.85, 2.35)
```

Il est donc adapté à des ensembles de valeurs qui représentent une information fixe.

Le dépaquetage permet de récupérer directement ses éléments :

```python
x, y = point
```

Pour ce cours, retenez surtout la différence :
**liste = modifiable ; tuple = non modifiable.**
---
## Indexage et découpage (1/2)

Une séquence contient plusieurs éléments, chacun possédant une position appelée **index**.

En Python, le premier élément possède l'index `0`.

```python
liste = [10, 20, 30, 40, 50]

liste[0]
liste[1]
liste[-1]
```

L'index négatif permet de partir de la fin.

Cette convention `0, 1, 2, ...` est fondamentale et sera également utilisée avec NumPy.
---
## Indexage et découpage (2/2)

On peut également récupérer une partie d'une séquence : c'est le **slicing**.

```python
liste[1:3]
liste[:2]
liste[::2]
```

La borne de début est incluse et la borne de fin est exclue.

Le découpage fonctionne sur les listes, les tuples et les chaînes de caractères.

Cette façon de sélectionner des données deviendra particulièrement utile avec les tableaux NumPy.
---
## Fonctions Python utiles sur les séquences

Python fournit déjà de nombreuses fonctions permettant d'analyser une séquence :

```python
len(...)
sum(...)
max(...)
min(...)
sorted(...)
```

Il existe également le test d'appartenance avec `in`.

Avant de créer nous-mêmes une fonction, il est donc intéressant de vérifier si Python fournit déjà l'opération recherchée.

Cette idée deviendra encore plus importante lorsque nous utiliserons des bibliothèques spécialisées.
---
## Manipulation de texte

Une chaîne de caractères (`str`) est elle-même une séquence de caractères.

On peut donc l'indexer et la découper comme une liste.

On peut aussi concaténer, rechercher, remplacer, séparer et reconstruire du texte.

Ces opérations sont particulièrement utiles pour traiter des données provenant de fichiers, car les valeurs lues dans un fichier sont souvent initialement du texte.
---
## Formatage de texte (f-strings)

Un programme doit souvent produire des messages lisibles contenant des valeurs calculées.

Les **f-strings** permettent d'insérer directement des expressions dans un texte.

```python
valeur = 3.14159
print(f"Valeur : {valeur:.2f}")
```

Le formatage permet notamment de contrôler le nombre de chiffres affichés.

Il faut distinguer la **valeur utilisée pour les calculs** de sa **représentation affichée**.
---
## Chercher, remplacer, séparer, joindre

Les chaînes possèdent de nombreuses méthodes utiles :

```python
texte.strip()
texte.replace(...)
texte.find(...)
texte.split(...)
```

`split()` est particulièrement important pour les données textuelles : il permet de transformer une ligne contenant plusieurs valeurs séparées en une liste.

À l'inverse, `join()` permet de reconstruire une chaîne à partir de plusieurs morceaux.

Ces opérations prépareront directement la lecture de fichiers structurés comme les CSV.
---
## Pourquoi les boucles ?

Nous savons maintenant stocker plusieurs valeurs dans une liste.

Mais comment appliquer le même traitement à chacune d'elles ?

Écrire une instruction différente pour chaque élément serait impossible dès que le nombre de données augmente.

Une **boucle** permet de demander à Python de répéter automatiquement un traitement.

C'est une idée centrale en programmation scientifique : une même opération peut devoir être appliquée à une longue série de mesures.
---
## Boucle `for`

La boucle `for` est adaptée lorsque l'on souhaite parcourir une séquence ou répéter un traitement pour un ensemble d'éléments.

```python
for mesure in mesures:
    print(mesure)
```

On peut également utiliser `range()` lorsque l'on travaille avec une suite d'indices ou un nombre connu de répétitions.

```python
for i in range(5):
    ...
```

Le bloc indenté est exécuté à chaque tour de boucle.
---
## Boucle `while`

La boucle `while` répète un traitement **tant qu'une condition est vraie**.

```python
while condition:
    ...
```

Elle est utile lorsque le nombre de répétitions dépend d'une condition plutôt que d'une séquence connue.

Il faut cependant faire attention à ce que la condition puisse devenir fausse : sinon, le programme peut rester bloqué dans une **boucle infinie**.
---
## `break` et `continue`

Deux instructions permettent de modifier le comportement d'une boucle.

- `break` arrête complètement la boucle ;
- `continue` abandonne le tour courant et passe au suivant.

Ces instructions sont utiles dans certaines situations, mais il faut éviter d'en abuser : une boucle dont le fonctionnement est simple est plus facile à lire et à maintenir.
---
## Bilan de la séance

Nous savons maintenant :

- organiser un programme avec des **fonctions** ;
- transmettre des données avec des paramètres et récupérer un résultat avec `return` ;
- stocker plusieurs valeurs avec des **listes** et des tuples ;
- sélectionner des éléments avec l'indexage et le slicing ;
- manipuler du texte ;
- parcourir et répéter des traitements avec des **boucles**.

Nous avons donc les bases nécessaires pour commencer à traiter de vraies données.
---
## À vous de jouer

Direction les exercices de la séance 2 →
