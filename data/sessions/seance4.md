# Séance 4
## Visualisation et instrumentation

Nous savons maintenant récupérer et analyser des données.

Mais une série de nombres n'est pas toujours facile à interpréter. La visualisation permet de repérer rapidement des tendances, des variations, des anomalies ou des relations entre grandeurs.

Nous allons ensuite aller plus loin : au lieu de lire des données depuis un fichier, nous verrons comment un programme Python peut communiquer directement avec un instrument ou une carte Arduino.
---
## Pourquoi visualiser des données ?

Une analyse scientifique ne consiste pas uniquement à calculer une moyenne ou un écart-type.

On cherche aussi à comprendre **comment les données évoluent**.

Un graphique peut révéler rapidement une tendance, une variation périodique, une valeur aberrante, un changement brutal ou un dépassement de seuil.

La visualisation est donc une étape de l'analyse, pas simplement une décoration du résultat.
---
## Qu'est-ce que Matplotlib ?

**Matplotlib** est une bibliothèque Python permettant de produire des graphiques.

Elle fonctionne naturellement avec les listes Python et les tableaux NumPy.

```python
import matplotlib.pyplot as plt
```

L'idée générale est simple :
**préparer les données → choisir une représentation → tracer → annoter → afficher ou sauvegarder.**
---
## Graphique en courbes

Le graphique en courbes est particulièrement adapté lorsqu'une grandeur évolue selon une autre, par exemple une température en fonction du temps.

```python
plt.plot(temps, temperature)
plt.show()
```

Il faut fournir une série de valeurs pour l'axe horizontal et une série correspondante pour l'axe vertical.

Dans le cas d'une mesure temporelle, on place généralement le temps sur l'axe `x` et la grandeur mesurée sur l'axe `y`.
---
## Nuage de points et histogramme

Tous les graphiques ne répondent pas au même besoin.

Le **nuage de points** permet notamment d'étudier la relation entre deux variables.

```python
plt.scatter(x, y)
```

L'**histogramme** permet d'étudier la répartition d'une série de valeurs.

```python
plt.hist(mesures, bins=5)
```

Le choix du graphique doit donc dépendre de la question que l'on cherche à résoudre.
---
## Personnaliser un graphique

Un graphique scientifique doit être compréhensible sans explication orale.

Il faut notamment indiquer :
- le nom des grandeurs ;
- les unités ;
- le titre ;
- les différentes séries si nécessaire ;
- éventuellement une grille.

```python
plt.xlabel("Temps (s)")
plt.ylabel("Température (°C)")
plt.title("Évolution de la température")
plt.legend()
```

La personnalisation a pour objectif de **rendre l'information lisible et interprétable**.
---
## Figures, axes et sous-figures

Lorsqu'un programme produit plusieurs graphiques, il devient utile de les organiser.

Matplotlib distingue notamment :
- la **figure** : l'ensemble du document graphique ;
- les **axes** : les zones dans lesquelles sont tracés les graphiques.

Avec `plt.subplots()`, on peut créer plusieurs zones de tracé dans une même figure.

Cette organisation devient pratique pour comparer plusieurs grandeurs ou plusieurs représentations d'un même jeu de données.
---
## Exporter et sauvegarder

Afficher un graphique à l'écran ne suffit pas toujours.

Un résultat peut devoir être intégré dans un rapport, envoyé à un collègue ou conservé pour une analyse ultérieure.

Matplotlib permet de sauvegarder une figure :

```python
plt.savefig("courbe_temperature.png")
```

Il faut donc distinguer **afficher une figure** et **produire un fichier graphique**.
---
## Notions d'instrumentation

Jusqu'ici, nos données provenaient d'un fichier.

Dans une chaîne expérimentale réelle, les données peuvent provenir directement d'un instrument.

On peut représenter la chaîne ainsi :

**grandeur physique → capteur → électronique → communication → ordinateur → programme Python → analyse**

Un instrument peut mesurer une grandeur, convertir cette mesure en données numériques et communiquer ces données au logiciel.

Python peut alors automatiser l'acquisition, le traitement et la visualisation.
---
## Communication matériel ↔ logiciel

Pour qu'un ordinateur dialogue avec un instrument, il faut un moyen de communication et des règles communes.

Les communications peuvent passer par différents supports :
- USB ;
- liaison série ;
- réseau ;
- autres interfaces spécialisées.

Le logiciel doit connaître la manière dont l'instrument attend de recevoir les commandes et la manière dont il transmet ses réponses.

C'est cette interface entre le monde matériel et le programme qui permet l'automatisation des mesures.
---
## Le protocole SCPI

De nombreux instruments de laboratoire utilisent **SCPI** (*Standard Commands for Programmable Instruments*).

SCPI définit un ensemble de commandes textuelles permettant notamment d'identifier un instrument ou de lui demander une mesure.

L'intérêt d'un protocole standardisé est de donner au logiciel une façon structurée de dialoguer avec différents instruments.

Il faut distinguer :
- le **support de communication** : par exemple une liaison série ou USB ;
- le **protocole** : les règles et commandes échangées.
---
## Port série sur un PC et encodage

Une liaison série transmet les données sous forme d'une suite d'octets.

Le PC et l'instrument doivent notamment être configurés avec des paramètres compatibles, comme la vitesse de transmission.

Sous Windows, les ports peuvent apparaître sous la forme `COM3`, `COM4`, etc. Sous Linux, on rencontre notamment `/dev/ttyUSB0` ou `/dev/ttyACM0`.

Les données reçues peuvent être des **bytes**. Pour obtenir du texte exploitable par Python, il faut alors les décoder.

Cette distinction entre **octets** et **texte** est importante lorsqu'on communique avec un appareil.
---
## Utiliser pyserial (1/2)

`pyserial` est une bibliothèque Python permettant d'utiliser les ports série.

Le principe général est :

1. ouvrir le port ;
2. configurer la communication ;
3. envoyer ou recevoir des données ;
4. convertir les données reçues si nécessaire ;
5. fermer le port.

```python
import serial

port = serial.Serial("COM3", baudrate=9600, timeout=1)
```

Une fois le port ouvert, Python peut communiquer avec l'appareil comme avec un flux de données.
---
## Utiliser pyserial (2/2)

Les données reçues peuvent être des octets :

```python
ligne = port.readline()
```

Il faut alors éventuellement les décoder :

```python
texte = ligne.decode("utf-8").strip()
```

À l'inverse, une commande envoyée peut être représentée sous forme de `bytes`.

Cette succession est importante :

**octets reçus → décodage → texte → conversion numérique → donnée utilisable**.
---
## Exemple : lire un capteur Arduino

Une carte Arduino peut envoyer régulièrement une mesure sur sa liaison série.

Python peut alors :
- ouvrir la liaison ;
- lire les mesures ;
- convertir le texte reçu en nombre ;
- stocker les valeurs ;
- calculer des statistiques ;
- tracer un graphique.

Nous retrouvons ainsi toutes les notions des quatre séances.

La chaîne complète devient :

**capteur → Arduino → série → Python → données → NumPy → statistiques → Matplotlib**.
---
## Le fil conducteur du cours

Les notions vues ne sont pas indépendantes.

Nous avons progressivement construit une chaîne complète de traitement des données :

**1. Programmer**
→ variables, types, conditions, fonctions, boucles

**2. Stocker**
→ listes, fichiers, CSV

**3. Calculer**
→ NumPy, moyenne, écart-type

**4. Visualiser**
→ Matplotlib

**5. Acquérir**
→ liaison série, Arduino, instrumentation

L'objectif final est de pouvoir automatiser une petite chaîne de mesure et d'analyse.
---
## Bilan de la séance

Vous devez maintenant comprendre les grandes étapes d'un programme scientifique :

- récupérer des données ;
- les convertir dans un format exploitable ;
- les stocker ;
- les analyser ;
- produire des indicateurs ;
- représenter les résultats ;
- éventuellement communiquer directement avec un instrument.

Les bibliothèques Python permettent d'ajouter progressivement ces capacités sans devoir tout programmer soi-même.
---
## À vous de jouer

Direction les exercices de la séance 4 →
