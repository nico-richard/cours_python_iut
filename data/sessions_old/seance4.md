# Séance 4
## Visualisation et instrumentation

---

## Pourquoi visualiser des données ?

Un tableau de nombres contient beaucoup d'informations, mais il est souvent difficile d'en percevoir rapidement les tendances.

Un graphique permet notamment de :

- repérer une évolution ;
- comparer plusieurs séries ;
- identifier des valeurs anormales ;
- observer une dispersion ;
- détecter un seuil dépassé ;
- communiquer plus facilement un résultat.

En sciences expérimentales et en métrologie, la visualisation constitue donc une étape importante de l'analyse des mesures.

---

## Qu'est-ce que Matplotlib ?

**Matplotlib** est une bibliothèque Python permettant de créer des graphiques.

Elle est très utilisée dans les domaines scientifiques et techniques.

```python
import matplotlib.pyplot as plt
```

Le sous-module `pyplot` fournit les fonctions couramment utilisées pour créer et personnaliser les graphiques.

Matplotlib permet de construire des graphiques simples mais également des figures complexes comprenant plusieurs représentations.

---

## Choisir le bon type de graphique

Le choix du graphique dépend du type de données et de la question que l'on souhaite étudier.

- **Courbe** : évolution d'une grandeur, notamment dans le temps.
- **Nuage de points** : relation entre deux variables.
- **Histogramme** : distribution d'une série de valeurs.

Un graphique n'est donc pas uniquement une question de programmation : il faut également savoir **quelle représentation est adaptée aux données**.

---

## Graphique en courbes

Une courbe permet de représenter l'évolution d'une grandeur en fonction d'une autre.

```python
temps = [0, 1, 2, 3, 4]
temperature = [20.1, 20.4, 20.9, 21.5, 22.0]

plt.plot(temps, temperature)
plt.show()
```

Ici, le temps est placé sur l'axe horizontal et la température sur l'axe vertical.

Une courbe est particulièrement adaptée aux mesures réalisées successivement dans le temps.

---

## Nuage de points

Un nuage de points permet d'étudier la relation entre deux variables.

```python
plt.scatter(temps, temperature)
plt.show()
```

Chaque point représente une observation.

Contrairement à une courbe, les points ne sont pas nécessairement reliés entre eux.

Le nuage de points est notamment utile pour rechercher une tendance ou une corrélation entre deux grandeurs.

---

## Histogramme

Un histogramme représente la **distribution** d'une série de valeurs.

```python
mesures = [12.1, 12.5, 12.4, 12.6, 12.3, 12.9]

plt.hist(mesures, bins=5)
plt.show()
```

L'axe horizontal représente les intervalles de valeurs, appelés classes.

L'axe vertical représente le nombre de mesures appartenant à chaque classe.

Un histogramme permet donc de voir comment les valeurs sont réparties.

---

## Personnaliser un graphique

Un graphique scientifique doit être compréhensible sans avoir à deviner ce que représentent les axes.

On peut ajouter :

```python
plt.xlabel("Temps (s)")
plt.ylabel("Température (°C)")
plt.title("Évolution de la température")
plt.legend()
plt.grid(True)
```

On peut également personnaliser l'apparence des courbes avec la couleur, le style de ligne ou les marqueurs.

La personnalisation doit cependant rester au service de la **lisibilité**.

---

## Axes, unités et légendes

Les noms des axes sont particulièrement importants.

Il faut indiquer :

- la grandeur représentée ;
- l'unité lorsque cela est pertinent.

Par exemple :

```text
Temps (s)
Température (°C)
Tension (V)
Pression (Pa)
```

Une légende est nécessaire lorsque plusieurs séries sont représentées sur le même graphique.

Un graphique sans unité ou sans contexte peut être difficile, voire impossible, à interpréter correctement.

---

## Figures et axes

Matplotlib distingue notamment la **figure** et les **axes**.

La figure correspond à la fenêtre ou à l'image globale.

Les axes correspondent aux zones dans lesquelles les données sont réellement tracées.

On peut créer plusieurs axes :

```python
fig, axes = plt.subplots(1, 2, figsize=(10, 4))
```

Cela permet de construire une figure regroupant plusieurs graphiques.

---

## Sous-figures

Plusieurs représentations peuvent être regroupées dans une même figure.

```python
fig, axes = plt.subplots(1, 2)

axes[0].plot(temps, temperature)
axes[0].set_title("Courbe")

axes[1].hist(mesures, bins=5)
axes[1].set_title("Histogramme")

plt.tight_layout()
plt.show()
```

Cette organisation est utile lorsque l'on souhaite présenter plusieurs aspects d'une même expérience.

---

## Sauvegarder un graphique

Un graphique peut être affiché à l'écran mais également enregistré dans un fichier.

```python
plt.plot(temps, temperature)
plt.savefig("courbe_temperature.png", dpi=150)
```

La sauvegarde permet notamment :

- d'intégrer un graphique dans un rapport ;
- de conserver les résultats d'une analyse ;
- de partager une figure avec d'autres personnes.

---

## Notions d'instrumentation

L'**instrumentation** regroupe les techniques permettant de mesurer une grandeur physique et d'exploiter cette mesure.

Une chaîne de mesure peut être représentée simplement :

```text
Grandeur physique
       ↓
     Capteur
       ↓
Électronique / acquisition
       ↓
Communication
       ↓
Ordinateur
       ↓
Analyse et visualisation
```

Un instrument peut donc associer une partie matérielle et une partie logicielle.

Dans ce cours, l'objectif est de faire communiquer Python avec un système de mesure.

---

## Communication matériel ↔ logiciel

Pour exploiter une mesure automatiquement, l'ordinateur doit pouvoir communiquer avec l'instrument.

Différentes technologies existent :

- liaison série ;
- USB ;
- Ethernet ;
- Wi-Fi ;
- autres protocoles industriels.

Le principe reste similaire : un appareil produit ou reçoit des données et un programme interprète ces données.

Python peut alors récupérer les mesures, les stocker, les analyser avec NumPy et les visualiser avec Matplotlib.

---

## La liaison série

Une liaison série transmet les informations **séquentiellement**, sous forme d'une suite de bits.

Elle est très répandue pour communiquer avec des cartes électroniques comme Arduino.

Une communication série nécessite que les deux appareils utilisent des paramètres compatibles, notamment :

- vitesse de transmission ;
- nombre de bits ;
- parité ;
- nombre de bits d'arrêt.

Si les paramètres ne correspondent pas, les données reçues peuvent être incorrectes ou illisibles.

---

## Le protocole SCPI

**SCPI** signifie *Standard Commands for Programmable Instruments*.

Il s'agit d'un ensemble de commandes textuelles standardisées utilisées pour piloter de nombreux instruments de mesure : multimètres, oscilloscopes, alimentations, etc.

Par exemple :

```text
*IDN?
```

peut demander l'identification d'un instrument.

Une commande de mesure peut avoir une forme telle que :

```text
MEASure:VOLTage:DC?
```

L'instrument reçoit une commande et renvoie généralement une réponse que le programme doit ensuite interpréter.

SCPI est donc un **protocole de commande**, tandis que la liaison série ou USB correspond au moyen de communication.

---

## Port série sur un PC

Le système d'exploitation identifie les ports de communication par un nom.

Sous Windows, on rencontre par exemple :

```text
COM3
COM4
```

Sous Linux :

```text
/dev/ttyUSB0
/dev/ttyACM0
```

Le programme doit connaître le port auquel l'instrument est connecté.

Il faut également configurer les paramètres de communication, notamment le débit en bauds.

---

## Encodage des caractères

Une communication informatique transmet initialement des données sous forme d'**octets**.

Lorsqu'un appareil transmet du texte, ces octets doivent être interprétés avec un encodage.

Les encodages courants sont notamment :

- ASCII ;
- UTF-8.

Python distingue notamment les données binaires (`bytes`) et le texte (`str`).

On peut convertir des octets en texte avec `decode()` :

```python
ligne = b"21.5\n"
texte = ligne.decode("utf-8")
```

Cette distinction sera importante avec `pyserial`.

---

## Utiliser pyserial

`pyserial` est une bibliothèque Python permettant d'utiliser les ports série.

```python
import serial
```

On peut ouvrir une liaison :

```python
port = serial.Serial(
    "COM3",
    baudrate=9600,
    timeout=1
)
```

Le programme peut ensuite lire des données :

```python
ligne = port.readline()
```

La donnée reçue est généralement de type `bytes`.

On peut la convertir en texte :

```python
texte = ligne.decode("utf-8").strip()
```

---

## Lire des mesures reçues par série

Une fois la donnée convertie en texte, on peut la transformer en nombre si l'appareil envoie une valeur numérique.

```python
valeur = float(texte)
```

On retrouve alors toutes les notions étudiées précédemment :

```text
donnée reçue
      ↓
texte
      ↓
conversion numérique
      ↓
NumPy
      ↓
calcul
      ↓
Matplotlib
```

La communication avec l'instrument devient ainsi une nouvelle source de données pour notre programme.

---

## Exemple : lire un capteur Arduino

Une Arduino peut envoyer périodiquement une valeur sur sa liaison série.

Python peut lire ces valeurs :

```python
import serial
import time

port = serial.Serial("COM3", baudrate=9600, timeout=1)

time.sleep(2)

for _ in range(10):
    ligne = port.readline().decode("utf-8").strip()

    if ligne:
        valeur = float(ligne)
        print(f"Mesure reçue : {valeur}")

port.close()
```

On retrouve ici plusieurs concepts vus dans les séances précédentes :

- importation d'une bibliothèque ;
- boucle `for` ;
- condition `if` ;
- conversion `float()` ;
- affichage avec une f-string.

---

## De la mesure à l'analyse

L'objectif final de la programmation scientifique est rarement de simplement afficher une valeur.

On souhaite généralement :

1. **acquérir** les mesures ;
2. **stocker** les données ;
3. **vérifier** leur qualité ;
4. **calculer** des indicateurs ;
5. **visualiser** les résultats ;
6. **interpréter** les données.

On peut donc construire une chaîne complète :

```text
Capteur
   ↓
Arduino
   ↓
PySerial
   ↓
Python
   ↓
NumPy
   ↓
Statistiques
   ↓
Matplotlib
```

---

## À retenir

À la fin de cette séance, vous devez savoir :

- pourquoi on visualise des données ;
- choisir entre courbe, nuage de points et histogramme ;
- créer un graphique avec Matplotlib ;
- ajouter titres, axes, unités et légendes ;
- créer plusieurs graphiques dans une figure ;
- sauvegarder une figure ;
- comprendre le principe d'une chaîne d'instrumentation ;
- comprendre le principe d'une liaison série ;
- identifier un port série ;
- comprendre le rôle d'un protocole comme SCPI ;
- utiliser les bases de `pyserial` ;
- convertir une donnée reçue en texte puis en nombre.

---

## À vous de jouer

Direction les exercices de la séance 4 →
