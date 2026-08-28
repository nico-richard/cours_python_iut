# Séance 1
## Machine, logiciel et bases de Python

---

## Architecture matérielle

Un ordinateur est une machine capable de **stocker, traiter et transmettre de l'information**. Pour exécuter un programme, plusieurs composants travaillent ensemble.

- **CPU** (processeur) : exécute les instructions du programme. Sa fréquence est souvent exprimée en GHz, mais la fréquence seule ne suffit pas à caractériser ses performances.
- **RAM** : mémoire de travail utilisée pendant l'exécution des programmes. Elle est rapide mais **volatile** : son contenu est perdu lorsque l'ordinateur est éteint.
- **Stockage** (disque dur / SSD) : conserve durablement les fichiers et les programmes. Il est généralement plus lent que la RAM.
- **Périphériques** : permettent à l'ordinateur de communiquer avec l'extérieur : clavier, écran, souris, capteurs, ports USB, ports série...

On peut retenir une idée simple : **le stockage conserve les données, la RAM les met à disposition des programmes et le CPU les traite**.

*Exemple concret* : lorsqu'un programme analyse un gros fichier de mesures, les données doivent être récupérées depuis le stockage, placées en mémoire puis traitées par le processeur.

---

## Architecture logicielle

Le matériel seul ne sait pas directement quoi faire : il a besoin de logiciels.

- **Système d'exploitation (OS)** : Windows, Linux, macOS... Il gère les ressources matérielles et fournit des services aux programmes.
- **Programme** : ensemble d'instructions permettant de réaliser une tâche.
- **Langage de programmation** : permet à un humain d'écrire ces instructions sous une forme compréhensible.
- **Interpréteur / compilateur** : transforme le code écrit par le programmeur en instructions pouvant être exécutées par la machine.

Un programme écrit en C ou C++ est généralement compilé avant son exécution. Python utilise principalement un **interpréteur** : le code Python est pris en charge par l'environnement Python au moment de son exécution.

L'intérêt de Python est notamment sa **lisibilité** et sa grande portabilité : un même programme Python peut généralement être exécuté sur plusieurs systèmes si Python et les bibliothèques nécessaires sont disponibles.

---

## Comment un programme est-il exécuté ?

Lorsqu'on lance un programme :

1. Le système d'exploitation charge le programme depuis le stockage.
2. Le programme est placé en mémoire.
3. Le processeur exécute les instructions.
4. Le programme peut lire ou modifier des données.
5. Il peut communiquer avec l'utilisateur ou avec des périphériques.

Cette vision simplifiée sera utile pour comprendre plus tard comment Python peut lire un fichier, traiter des mesures et communiquer avec une carte Arduino.

---

## Installer et lancer Python

Python peut être installé depuis [python.org](https://www.python.org).

Sous Windows, il est important de pouvoir lancer Python depuis un terminal. Lors de l'installation, l'option permettant d'ajouter Python au `PATH` facilite cette utilisation.

Vérifier l'installation :

```bash
python --version
```

Selon le système, la commande peut aussi être `python3`.

Il existe deux façons principales d'exécuter du Python :

- **console interactive** : pratique pour tester rapidement une instruction ;
- **script** : fichier `.py` contenant un programme que l'on peut sauvegarder et réexécuter.

---

## La console interactive

La console Python permet d'exécuter immédiatement une instruction.

```bash
python
```

On obtient alors une invite :

```text
>>> 2 + 2
4
```

La console est particulièrement pratique pour **expérimenter** et vérifier rapidement le comportement d'une instruction.

Elle n'est cependant pas adaptée à un programme long : pour conserver un programme, on utilise un fichier `.py`.

---

## Le script Python

Un script est simplement un fichier texte dont l'extension est `.py`.

```python
print("Bonjour")
```

On peut ensuite lancer ce fichier depuis un terminal :

```bash
python mon_script.py
```

Le fichier constitue alors une version **sauvegardée et réutilisable** du programme.

Dans la suite du cours, on travaillera principalement avec des scripts, même si la console reste très utile pour tester des instructions.

---

## Variables et types de données

Une **variable** est un nom associé à une valeur.

```python
age = 20
temperature = 20.5
nom = "Alice"
actif = True
```

Une variable permet donc de donner un nom à une information afin de pouvoir la réutiliser dans le programme.

Python utilise notamment les types suivants :

- `int` : nombre entier
- `float` : nombre réel
- `str` : chaîne de caractères
- `bool` : valeur logique, `True` ou `False`

Python détermine automatiquement le type lors de l'affectation : on parle de **typage dynamique**.

On peut connaître le type d'une valeur avec :

```python
type(temperature)
```

---

## L'affectation

L'instruction :

```python
temperature = 20.5
```

signifie que la valeur `20.5` est affectée au nom `temperature`.

Le symbole `=` est donc un **opérateur d'affectation** et non un test d'égalité.

Une variable peut ensuite recevoir une nouvelle valeur :

```python
temperature = 20.5
temperature = 21.2
```

Après ces instructions, la valeur associée à `temperature` est `21.2`.

---

## Nommage des variables

Un bon nom de variable permet de comprendre rapidement ce que représente une donnée.

```python
temperature = 21.5
nombre_mesures = 100
nom_capteur = "sonde_1"
```

On évite les noms trop courts ou ambigus lorsque le programme devient plus complexe.

Par convention, les noms de variables Python utilisent généralement le **snake_case** :

```python
temperature_moyenne
nombre_de_mesures
```

---

## Conversions explicites

Une donnée peut parfois être convertie d'un type vers un autre.

```python
x = "42"
y = int(x)
```

Ici, `"42"` est une chaîne de caractères alors que `42` est un entier.

Conversions courantes :

```python
int("42")
float("3.14")
str(42)
```

Les conversions sont particulièrement importantes lorsqu'on récupère des données provenant de l'utilisateur ou d'un fichier.

Par exemple, `input()` renvoie du texte : il faudra donc convertir cette valeur si l'on souhaite effectuer un calcul numérique.

Certaines conversions ne sont pas possibles :

```python
int("bonjour")
```

Cette instruction provoque une erreur car `"bonjour"` ne représente pas un entier.

---

## Les opérateurs arithmétiques

Python permet d'effectuer les opérations mathématiques usuelles :

```python
7 + 2   # addition
7 - 2   # soustraction
7 * 2   # multiplication
7 / 2   # division réelle
7 // 2  # division entière
7 % 2   # reste de la division
7 ** 2  # puissance
```

Quelques opérations ont donc un comportement spécifique :

- `/` produit une division réelle ;
- `//` donne le quotient entier ;
- `%` donne le reste ;
- `**` correspond à une puissance.

---

## Affectation combinée

Python permet de modifier une variable à partir de sa valeur actuelle :

```python
x = 5
x += 1
```

est équivalent à :

```python
x = x + 1
```

On trouve également :

```python
x -= 1
x *= 2
x /= 2
```

Ces opérateurs sont particulièrement utiles dans les boucles et les calculs successifs.

---

## Les opérateurs de comparaison

Les comparaisons produisent une valeur booléenne : `True` ou `False`.

```python
a == b   # égalité
a != b   # différence
a < b
a <= b
a > b
a >= b
```

Attention à la différence entre :

```python
x = 5
```

qui affecte `5` à `x`, et :

```python
x == 5
```

qui vérifie si `x` vaut `5`.

---

## Les opérateurs logiques

Les opérateurs logiques permettent de combiner plusieurs conditions.

- `and` : les deux conditions doivent être vraies ;
- `or` : au moins une condition doit être vraie ;
- `not` : inverse la valeur logique.

Par exemple :

```python
temperature > 0 and temperature < 30
```

correspond à une température comprise entre 0 et 30 °C.

Ces opérateurs deviennent particulièrement utiles avec les structures conditionnelles.

---

## Le type influence le résultat !

Le comportement d'une opération dépend du type des données.

```python
7 / 2
# 3.5

7 // 2
# 3
```

Les nombres réels (`float`) sont représentés avec une précision limitée.

Ainsi :

```python
0.1 + 0.2
```

peut produire :

```text
0.30000000000000004
```

Ce comportement vient de la représentation binaire des nombres réels et ne signifie pas que Python « se trompe » dans son calcul.

En calcul scientifique et en métrologie, il faut donc être prudent avec les comparaisons exactes entre nombres flottants.

---

## Entrées / sorties simples

La fonction `input()` permet de demander une information à l'utilisateur.

```python
valeur = input("Température en °C : ")
```

**Point important : `input()` renvoie toujours une chaîne de caractères (`str`).**

Pour utiliser cette valeur dans un calcul, il faut généralement la convertir :

```python
temperature = float(valeur)
```

La fonction `print()` permet d'afficher une information.

```python
print(temperature)
```

---

## Formater du texte avec les f-strings

Les **f-strings** permettent d'intégrer facilement des valeurs dans un texte.

```python
temperature = 20.567

print(f"Température : {temperature} °C")
```

On peut également contrôler l'affichage numérique :

```python
print(f"Température : {temperature:.1f} °C")
```

Ici, `.1f` demande un affichage avec **un chiffre après la virgule**.

Les f-strings seront très utiles pour afficher des résultats de mesures de manière lisible.

---

## Tests conditionnels

Un programme doit souvent prendre une décision en fonction d'une donnée.

Python utilise pour cela :

```python
if condition:
    ...
elif autre_condition:
    ...
else:
    ...
```

Exemple :

```python
if temperature < 0:
    print("Gel")
elif temperature < 30:
    print("Normal")
else:
    print("Chaud")
```

Le programme teste les conditions dans l'ordre et exécute le bloc correspondant à la première condition vraie.

---

## L'indentation en Python

En Python, l'indentation n'est pas uniquement une question de présentation : elle fait partie de la syntaxe.

```python
if temperature < 0:
    print("Gel")
```

L'instruction `print()` appartient au bloc du `if` parce qu'elle est indentée.

Toutes les instructions d'un même bloc doivent avoir la même indentation.

Cette particularité rend le code Python très lisible, mais impose de respecter rigoureusement les niveaux d'indentation.

---

## À retenir

À la fin de cette séance, vous devez savoir :

- distinguer matériel, système d'exploitation et programme ;
- lancer Python et exécuter un script ;
- créer et utiliser des variables ;
- reconnaître les principaux types de données ;
- effectuer des conversions ;
- réaliser des calculs ;
- demander une valeur avec `input()` ;
- afficher un résultat avec `print()` ;
- comparer des valeurs ;
- utiliser `if / elif / else` pour prendre une décision.

---

## À vous de jouer

Direction les exercices de la séance 1 →
