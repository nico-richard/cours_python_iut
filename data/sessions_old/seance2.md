# Séance 2
## Structures

---

## Pourquoi des fonctions ?

Lorsque les programmes deviennent plus longs, on retrouve souvent les mêmes opérations à plusieurs endroits.

Une **fonction** permet de regrouper plusieurs instructions sous un nom afin de pouvoir les réutiliser.

Elle permet notamment :

- d'éviter de répéter du code ;
- de découper un programme en petites tâches ;
- de rendre le programme plus lisible ;
- de tester plus facilement chaque partie du programme.

---

## Définir une fonction

Une fonction se définit avec le mot-clé `def`.

```python
def convertir_c_en_k(temperature_c):
    resultat = temperature_c + 273.15
    return resultat
```

Cette définition ne lance pas immédiatement la fonction : elle indique à Python **comment effectuer le traitement**.

On peut ensuite appeler la fonction :

```python
t = convertir_c_en_k(20)
```

Le programme exécute alors les instructions de la fonction avec `temperature_c = 20`.

---

## Paramètres et arguments

Un **paramètre** est une donnée attendue par la fonction.

```python
def convertir_c_en_k(temperature_c):
    ...
```

Ici, `temperature_c` est un paramètre.

Lorsqu'on appelle la fonction :

```python
convertir_c_en_k(20)
```

`20` est l'**argument** fourni à la fonction.

Une fonction peut avoir plusieurs paramètres :

```python
def moyenne(a, b):
    return (a + b) / 2
```

---

## Valeurs par défaut

On peut donner une valeur par défaut à un paramètre.

```python
def convertir(valeur, unite="celsius"):
    ...
```

Si l'utilisateur ne fournit pas `unite`, Python utilise `"celsius"`.

```python
convertir(20)
```

On peut également fournir explicitement le paramètre :

```python
convertir(68, unite="fahrenheit")
```

Les valeurs par défaut permettent de rendre certaines informations facultatives.

---

## La valeur de retour

Le mot-clé `return` permet à une fonction de **renvoyer une valeur** au programme qui l'a appelée.

```python
def carre(x):
    return x ** 2

resultat = carre(5)
```

Après l'appel, `resultat` contient la valeur renvoyée.

Il est important de distinguer :

- **calculer et renvoyer un résultat** ;
- **effectuer une action**, comme afficher un message.

Une fonction avec `return` peut donc être utilisée dans d'autres calculs.

---

## Fonctions avec ou sans valeur de retour

Une fonction peut simplement produire un effet :

```python
def afficher_alerte(valeur, seuil):
    if valeur > seuil:
        print("ALERTE : seuil dépassé")
```

Elle ne renvoie pas explicitement de résultat.

À l'inverse :

```python
def calculer_moyenne(liste):
    return sum(liste) / len(liste)
```

renvoie une valeur qui peut être stockée ou utilisée dans un autre calcul.

Cette distinction est importante pour concevoir des fonctions claires.

---

## Portée des variables

Une variable créée à l'intérieur d'une fonction est généralement **locale** à cette fonction.

```python
def f():
    x = 1
    return x

x = 5
f()
print(x)
```

Le `x` créé dans `f()` et le `x` créé à l'extérieur sont deux variables distinctes.

Il est préférable de limiter l'utilisation des variables globales et de transmettre les informations nécessaires aux fonctions grâce à leurs paramètres et à leur valeur de retour.

---

## Listes

Une **liste** est une collection ordonnée et modifiable de valeurs.

```python
mesures = [12.3, 14.1, 13.8]
```

Une liste peut contenir plusieurs éléments et peut être modifiée :

```python
mesures.append(15.0)
mesures[0] = 12.5
```

Les listes seront très importantes pour stocker temporairement des séries de mesures avant leur traitement avec NumPy.

---

## Modifier une liste

Quelques opérations courantes :

```python
mesures.append(15.0)
mesures.remove(14.1)
```

On peut également connaître le nombre d'éléments :

```python
len(mesures)
```

Une liste est donc une structure **mutable** : son contenu peut changer après sa création.

---

## Tuples

Un **tuple** ressemble à une liste, mais son contenu ne peut pas être modifié après sa création.

```python
point = (48.85, 2.35)
```

Les tuples sont utiles pour représenter des données qui doivent rester fixes, par exemple les coordonnées d'un point.

On peut récupérer leurs valeurs par **dépaquetage** :

```python
x, y = point
```

Le choix entre liste et tuple dépend donc notamment du fait que les données doivent pouvoir être modifiées ou non.

---

## Indexage

Les listes, tuples et chaînes de caractères sont des séquences.

Python utilise des **indices** pour accéder à leurs éléments.

```python
liste = [10, 20, 30, 40, 50]

liste[0]
liste[1]
```

Le premier élément possède l'indice `0`, et non `1`.

On peut également utiliser des indices négatifs :

```python
liste[-1]
```

qui correspond au dernier élément.

---

## Découpage : slicing

Le slicing permet d'extraire une partie d'une séquence.

```python
liste[1:3]
```

signifie :

- commencer à l'indice `1` ;
- s'arrêter avant l'indice `3`.

On obtient donc les éléments d'indices `1` et `2`.

On peut également écrire :

```python
liste[:2]
liste[2:]
liste[::2]
```

Le slicing sera également utilisé avec les tableaux NumPy.

---

## Fonctions Python utiles sur les séquences

Python fournit plusieurs fonctions très utiles :

```python
len([1, 2, 3])
sum([1, 2, 3])
max([1, 5, 2])
min([1, 5, 2])
sorted([3, 1, 2])
```

Ces fonctions permettent d'effectuer rapidement des opérations courantes sur des collections de données.

On peut également tester l'appartenance d'une valeur :

```python
"a" in ["a", "b"]
```

qui renvoie `True`.

---

## Manipulation de texte

Une chaîne de caractères (`str`) est elle-même une séquence de caractères.

```python
prenom = "Alice"
nom = "Dupont"
```

On peut donc utiliser l'indexage :

```python
prenom[0]
```

et le slicing :

```python
prenom[:3]
```

On peut également concaténer plusieurs chaînes :

```python
nom_complet = prenom + " " + nom
```

---

## Les chaînes sont immuables

Une chaîne de caractères ne peut pas être modifiée directement caractère par caractère.

On crée généralement une nouvelle chaîne à partir de l'ancienne.

```python
nom = "Dupont"
```

Les méthodes comme `replace()` renvoient donc une nouvelle chaîne :

```python
nouveau_nom = nom.replace("D", "T")
```

Cette notion d'**immutabilité** explique certaines différences de comportement entre les chaînes, les listes et les tuples.

---

## Caractères spéciaux et échappement

Certains caractères ont une signification particulière dans une chaîne.

```python
"\n"
```

représente un retour à la ligne.

```python
"\t"
```

représente une tabulation.

Le caractère `\` est utilisé pour introduire ces séquences spéciales.

On peut également écrire un guillemet dans une chaîne en l'échappant lorsque cela est nécessaire :

```python
"Il a dit : \"Bonjour\""
```

---

## Formatage de texte

Les f-strings permettent d'insérer des valeurs dans du texte.

```python
valeur = 3.14159

print(f"Pi vaut environ {valeur:.2f}")
```

Elles permettent également de choisir le format d'affichage des nombres.

C'est particulièrement pratique pour afficher des résultats scientifiques avec un nombre contrôlé de chiffres significatifs ou de décimales.

---

## Chercher et remplacer

Les chaînes possèdent de nombreuses méthodes utiles.

```python
phrase = "Bonjour le monde"

phrase.find("monde")
phrase.replace("monde", "IUT")
```

On peut également supprimer les espaces inutiles au début et à la fin :

```python
phrase.strip()
```

Ces opérations sont particulièrement utiles lorsqu'on doit nettoyer des données provenant d'un fichier.

---

## Séparer et joindre du texte

La méthode `split()` transforme une chaîne en plusieurs éléments.

```python
"a,b,c".split(",")
```

produit une liste.

À l'inverse, `join()` permet de construire une chaîne à partir d'une séquence :

```python
"-".join(["a", "b", "c"])
```

Ces deux opérations sont fondamentales pour manipuler des données textuelles et des fichiers structurés.

---

## Pourquoi les boucles ?

Une boucle permet de **répéter automatiquement un ensemble d'instructions**.

Sans boucle, traiter 100 mesures nécessiterait d'écrire 100 fois les mêmes instructions.

Avec une boucle, on décrit une seule fois le traitement à effectuer et Python le répète.

Les deux structures principales sont :

- `for` : parcourir une séquence ou répéter un nombre déterminé de fois ;
- `while` : répéter tant qu'une condition reste vraie.

---

## Boucle `for`

La boucle `for` est particulièrement adaptée au parcours d'une séquence.

```python
for mesure in [12.3, 14.1, 13.8]:
    print(mesure)
```

Python prend successivement chaque élément de la liste et l'associe à la variable `mesure`.

Le même mécanisme sera utilisé plus tard pour parcourir des lignes d'un fichier CSV.

---

## `range()`

`range()` permet de générer une suite d'entiers, très souvent utilisée avec `for`.

```python
for i in range(5):
    print(i)
```

Les valeurs produites vont de `0` à `4`.

On peut aussi préciser un début, une fin et un pas :

```python
range(2, 10, 2)
```

La valeur de fin n'est pas incluse.

Cette convention correspond à celle utilisée pour les indices et les slices.

---

## Boucle `while`

Une boucle `while` répète un bloc **tant qu'une condition est vraie**.

```python
x = 10

while x > 0:
    print(x)
    x -= 1
```

Il faut faire attention à ce que la condition puisse finalement devenir fausse.

Sinon, la boucle ne s'arrête jamais : on parle de **boucle infinie**.

---

## `break` et `continue`

`break` permet de quitter immédiatement une boucle.

```python
for i in range(10):
    if i == 5:
        break
```

`continue` permet de passer directement à l'itération suivante.

```python
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
```

Ces instructions sont utiles pour contrôler finement le comportement d'une boucle, mais il faut éviter d'en abuser afin de conserver un code lisible.

---

## À retenir

À la fin de cette séance, vous devez savoir :

- stocker plusieurs valeurs dans une liste ;
- accéder à un élément avec un indice ;
- extraire une partie d'une séquence ;
- manipuler des chaînes de caractères ;
- parcourir une séquence avec `for` ;
- répéter une opération avec `while` ;
- contrôler une boucle avec `break` et `continue` ;
- créer une fonction ;
- transmettre des paramètres à une fonction ;
- récupérer une valeur avec `return`.

---

## À vous de jouer

Direction les exercices de la séance 2 →
