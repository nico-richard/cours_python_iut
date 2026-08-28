# Séance 4
## Visualiser et acquérir des mesures

### Matplotlib, instrumentation et liaison série

Une série de nombres devient plus facile à interpréter lorsqu'elle est représentée graphiquement. Python peut aussi recevoir directement les mesures d'un instrument.

À la fin de la séance, vous devez être capables de produire un graphique scientifique lisible et d'expliquer les étapes d'une acquisition par liaison série.

:::support
Cette séance termine la chaîne commencée avec les fichiers et NumPy. Matplotlib
transforme les données en représentations visuelles ; l'instrumentation et la
liaison série montrent comment ces données peuvent provenir du monde physique.
:::
---
## Rôle de la visualisation

Un indicateur résume les données ; un graphique montre leur organisation.

Une représentation peut révéler :

- une tendance ou une évolution temporelle ;
- une relation entre deux grandeurs ;
- une dispersion ou une valeur aberrante ;
- un changement brutal ou un dépassement de seuil.

Le graphique doit être choisi en fonction de la question scientifique, pas seulement pour son apparence.
---
## Choisir une représentation

| Question | Représentation adaptée |
|---|---|
| Comment une grandeur évolue-t-elle ? | courbe |
| Deux variables sont-elles liées ? | nuage de points |
| Comment les valeurs sont-elles réparties ? | histogramme |

Une même série peut être représentée de plusieurs manières, mais chaque graphique met en évidence une information différente.

:::support
Relier des points par une courbe suggère un ordre, souvent temporel. Un nuage de
points ne suppose pas cette continuité et sert à étudier une relation. Un histogramme
regroupe les valeurs par intervalles ; il ne doit pas être confondu avec un diagramme
en barres représentant des catégories.
:::
---
## Construire un graphique avec Matplotlib

```python
import matplotlib.pyplot as plt

plt.plot(temps, temperatures)
plt.xlabel("Temps (s)")
plt.ylabel("Température (°C)")
plt.title("Évolution de la température")
plt.show()
```

:::diagram
Données
Représentation
Annotations
Affichage
:::

:::support
Le module `matplotlib.pyplot`, généralement importé sous l'alias `plt`, fournit une
interface simple pour construire une figure. Les deux séries transmises à `plot`
doivent avoir le même nombre d'éléments : chaque abscisse correspond à une ordonnée.
:::
---
## Représenter une évolution

```python
plt.plot(
    temps,
    temperatures,
    color="tab:blue",
    marker="o",
    label="Température",
)
```

| Argument | Rôle |
|---|---|
| `color` | couleur de la courbe |
| `marker` | symbole placé sur les mesures |
| `label` | nom utilisé dans la légende |

Une ligne est pertinente lorsque l'ordre des points possède un sens.
---
## Nuage de points et histogramme

```python
plt.scatter(tension, courant)
```

Le nuage de points montre la relation entre deux variables mesurées sur les mêmes observations.

```python
plt.hist(temperatures, bins=10)
```

L'histogramme découpe l'étendue des valeurs en intervalles et compte les observations dans chacun d'eux. Le choix de `bins` influence la lecture de la distribution.
---
## Annoter un graphique scientifique

Un graphique doit pouvoir être compris sans l'explication orale qui l'accompagne.

```python
plt.xlabel("Temps (s)")
plt.ylabel("Température (°C)")
plt.title("Évolution de la température")
plt.grid(alpha=0.3)
plt.legend()
```

Les axes indiquent la grandeur et son unité. Une légende est nécessaire lorsque plusieurs séries sont tracées ou lorsqu'un `label` doit être identifié.

:::support
Un titre décrit la situation représentée sans répéter simplement les axes. Une
grille légère facilite la lecture des valeurs mais ne doit pas dominer les données.
`legend()` utilise les textes fournis avec l'argument `label` des tracés.
:::
---
## Figure, axes et sous-graphiques

Matplotlib distingue la **figure**, qui contient l'ensemble du document, et les **axes**, qui sont les zones de tracé.

```python
fig, axes = plt.subplots(1, 2, figsize=(10, 4))

axes[0].plot(temps, temperatures)
axes[1].hist(temperatures, bins=10)

fig.tight_layout()
```

Les sous-graphiques permettent de comparer plusieurs représentations sans les superposer.

:::support
Malgré son nom, un objet `Axes` représente une zone complète de tracé avec ses
deux axes gradués. L'interface orientée objet (`fig`, `axes`) devient plus claire
que `plt` dès que la figure contient plusieurs graphiques.
:::
---
## Exporter une figure

Une figure peut être enregistrée pour être intégrée dans un rapport :

```python
fig.savefig(
    "temperature.png",
    dpi=300,
    bbox_inches="tight",
)
```

`dpi` contrôle la résolution d'une image matricielle ; `bbox_inches="tight"` limite les marges inutiles.

La sauvegarde est généralement effectuée avant `plt.show()`.

:::support
Le format PNG convient aux documents courants. Les formats vectoriels comme SVG
ou PDF restent nets lors d'un agrandissement. Avec l'interface `pyplot`, la fonction
équivalente est `plt.savefig()`.
:::
---
## Chaîne d'instrumentation

Une mesure numérique résulte de plusieurs transformations :

:::diagram vertical
Grandeur physique
Capteur
Électronique d'acquisition
Communication
Ordinateur et programme Python
Analyse et représentation
:::

Python intervient après la conversion de la grandeur physique en données transmissibles.

:::support
Le capteur réagit à une grandeur telle qu'une température ou une tension.
L'électronique conditionne et numérise le signal. Le système communique ensuite
les valeurs à l'ordinateur, où Python peut automatiser leur stockage, leur analyse
et leur représentation.
:::
---
## Support de communication et protocole

Deux éléments sont nécessaires pour dialoguer avec un instrument :

| Élément | Question associée | Exemples |
|---|---|---|
| **support/interface** | par où circulent les données ? | USB, série, réseau |
| **protocole** | quelles règles sont utilisées ? | SCPI, protocole constructeur |

Une connexion USB n'indique pas à elle seule la forme des commandes ou des réponses échangées.

:::support
Une interface décrit le moyen de transport et ses caractéristiques. Un protocole
définit la structure, l'ordre et la signification des messages. Plusieurs protocoles
peuvent utiliser un même support, et un même protocole peut parfois être transporté
par plusieurs interfaces.
:::
---
## Commandes SCPI

SCPI (*Standard Commands for Programmable Instruments*) définit une syntaxe textuelle utilisée par de nombreux instruments de laboratoire.

```text
*IDN?
MEASure:VOLTage:DC?
```

- `*IDN?` demande l'identification de l'instrument ;
- `MEASure:VOLTage:DC?` demande une mesure de tension continue ;
- le point d'interrogation signale une requête qui attend une réponse.

:::support
SCPI standardise une partie du vocabulaire, mais les commandes réellement prises
en charge dépendent de l'instrument. Sa documentation reste la référence. Les
commandes sont généralement terminées par un caractère de fin de ligne.
:::
---
## Paramètres d'une liaison série

Une liaison série transmet une suite d'octets. Les deux équipements doivent utiliser des paramètres compatibles.

| Paramètre | Rôle |
|---|---|
| port | identifier l'interface, par exemple `COM3` |
| `baudrate` | fixer la vitesse de transmission |
| `timeout` | limiter la durée d'attente d'une lecture |
| fin de ligne | délimiter les messages |

Sous Linux, un port peut notamment apparaître sous la forme `/dev/ttyUSB0` ou `/dev/ttyACM0`.
---
## Octets, texte et nombre

Le port série échange des `bytes`, alors que le programme veut généralement manipuler du texte puis un nombre.

:::diagram
Octets `b'20.5\r\n'`
Décodage UTF-8
Texte `"20.5"`
Conversion avec `float()`
Nombre `20.5`
:::

```python
texte = ligne.decode("utf-8").strip()
mesure = float(texte)
```

L'encodage doit être identique du côté de l'émetteur et du récepteur.

:::support
Un octet est une valeur numérique comprise entre 0 et 255. Un encodage comme UTF-8
définit comment une suite d'octets représente des caractères. `strip()` retire ici
les caractères de fin de ligne avant la conversion numérique.
:::
---
## Lire avec pyserial

```python
import serial

with serial.Serial("COM3", baudrate=9600, timeout=1) as port:
    ligne = port.readline()
    texte = ligne.decode("utf-8").strip()
    mesure = float(texte)
```

Le bloc `with` ferme automatiquement le port. `readline()` lit jusqu'à une fin de ligne ou jusqu'à l'expiration du délai.

:::support
L'ouverture peut échouer si le port n'existe pas, est déjà utilisé ou si les droits
sont insuffisants. Une lecture peut être vide après un timeout et une réponse peut
être invalide. Une application réelle doit donc vérifier les données reçues avant
leur conversion.
:::
---
## Envoyer une commande

Une commande textuelle doit être encodée avant son envoi :

```python
import serial

with serial.Serial("COM3", baudrate=9600, timeout=1) as port:
    commande = "*IDN?\n".encode("utf-8")
    port.write(commande)
    reponse = port.readline().decode("utf-8").strip()
```

:::diagram vertical
Commande textuelle
Encodage en octets
Envoi et réception
Décodage des octets
Réponse textuelle
:::

:::support
La terminaison `\n` est ici incluse dans la commande car de nombreux instruments
attendent une fin de ligne avant de traiter le message. La terminaison exacte doit
être vérifiée dans la documentation de l'appareil.
:::
---
## Acquisition avec une carte Arduino

Une carte Arduino peut envoyer périodiquement une mesure terminée par un retour à la ligne. Python peut alors :

1. ouvrir la liaison série ;
2. lire et convertir chaque mesure ;
3. stocker les valeurs ;
4. calculer des indicateurs avec NumPy ;
5. tracer et sauvegarder un graphique.

:::diagram vertical
Capteur
Arduino
Liaison série
Python
NumPy
Matplotlib
:::

Une source simulée permet de tester le programme lorsqu'aucun matériel n'est disponible.
---
## Synthèse du cours

Les quatre séances construisent une chaîne complète :

| Étape | Outils principaux |
|---|---|
| programmer | variables, conditions, fonctions, boucles |
| stocker | listes, fichiers, CSV |
| calculer | NumPy et statistiques descriptives |
| visualiser | Matplotlib |
| acquérir | instrument, liaison série, Arduino |

L'objectif est de transformer une grandeur physique en données interprétables, puis en résultat scientifique communicable.

:::support
Chaque étape possède une responsabilité distincte. Cette séparation permet de
tester les traitements avec des données simulées avant de connecter le matériel,
puis de remplacer la simulation par une acquisition réelle sans reconstruire tout
le programme.
:::
