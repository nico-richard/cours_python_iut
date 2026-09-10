# Correction — Séance 4

Document enseignant. Chaque bloc est un fichier Python complet et indépendant, sans affichage ni saisie. Les solutions utilisent uniquement les notions des séances 1 à 4.

## Ex. 1 — Tracer l'évolution d'une mesure

Fichier : `s4_ex1.py`

```python
import matplotlib.pyplot as plt


def tracer_evolution(temps, mesures):
    plt.plot(temps, mesures)
```

## Ex. 2 — Produire un graphique scientifique

Fichier : `s4_ex2.py`

```python
import matplotlib.pyplot as plt


def annoter_courbe(temps, temperatures):
    plt.plot(
        temps,
        temperatures,
        color="tab:blue",
        marker="o",
        label="Température",
    )
    plt.xlabel("Temps (s)")
    plt.ylabel("Température (°C)")
    plt.title("Évolution de la température")
    plt.grid(alpha=0.3)
    plt.legend()
```

## Ex. 3 — Étudier la relation entre deux grandeurs

Fichier : `s4_ex3.py`

```python
import matplotlib.pyplot as plt


def tracer_nuage(tensions, courants):
    plt.scatter(tensions, courants)
```

## Ex. 4 — Observer une distribution

Fichier : `s4_ex4.py`

```python
import matplotlib.pyplot as plt


def tracer_histogramme(mesures, nombre_classes=5):
    plt.hist(mesures, bins=nombre_classes)
```

## Ex. 5 — Comparer deux représentations

Fichier : `s4_ex5.py`

```python
import matplotlib.pyplot as plt


def creer_comparaison(temps, temperatures):
    plt.subplot(1, 2, 1)
    plt.plot(temps, temperatures)
    plt.subplot(1, 2, 2)
    plt.hist(temperatures, bins=5)
    plt.tight_layout()
```

## Ex. 6 — Exporter une courbe

Fichier : `s4_ex6.py`

```python
import matplotlib.pyplot as plt


def exporter_courbe(chemin, temps, temperatures):
    plt.plot(temps, temperatures)
    plt.xlabel("Temps (s)")
    plt.ylabel("Température (°C)")
    plt.savefig(chemin, dpi=300, bbox_inches="tight")
```

## Ex. 7 — Décoder une mesure reçue

Fichier : `s4_ex7.py`

```python
def decoder_mesure(donnees):
    texte = donnees.decode("utf-8").strip()
    return float(texte)
```

## Ex. 8 — Préparer une commande

Fichier : `s4_ex8.py`

```python
def encoder_commande(commande):
    return (commande + "\n").encode("utf-8")
```

## Ex. 9 — Lire une série de mesures

Fichier : `s4_ex9.py`

```python
def lire_mesures(port, nombre):
    mesures = []
    for _ in range(nombre):
        ligne = port.readline()
        texte = ligne.decode("utf-8").strip()
        mesures.append(float(texte))
    return mesures
```

## Ex. 10 — Interroger un instrument

Fichier : `s4_ex10.py`

```python
def interroger_instrument(port, commande):
    port.write((commande + "\n").encode("utf-8"))
    reponse = port.readline()
    return reponse.decode("utf-8").strip()
```
