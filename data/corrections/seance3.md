# Correction — Séance 3

Document enseignant. Chaque bloc est un fichier Python complet et indépendant, sans affichage ni saisie. Les solutions utilisent uniquement les notions des séances 1 à 3.

## Ex. 1 — Calculer une distance

Fichier : `s3_ex1.py`

```python
import math


def calculer_distance(horizontal, vertical):
    return math.sqrt(horizontal ** 2 + vertical ** 2)
```

## Ex. 2 — Relire les profondeurs

Fichier : `s3_ex2.py`

```python
def lire_valeurs(chemin):
    valeurs = []
    with open(chemin, "r", encoding="utf-8") as fichier:
        for ligne in fichier:
            valeurs.append(float(ligne.strip()))
    return valeurs
```

## Ex. 3 — Décoder le journal CSV

Fichier : `s3_ex3.py`

```python
def lire_mesures_csv(chemin):
    temps = []
    temperatures = []
    with open(chemin, "r", encoding="utf-8") as fichier:
        fichier.readline()
        for ligne in fichier:
            cellules = ligne.strip().split(";")
            temps.append(float(cellules[0]))
            temperatures.append(float(cellules[1]))
    return (temps, temperatures)
```

## Ex. 4 — Rédiger le bilan de plongée

Fichier : `s3_ex4.py`

```python
def ecrire_rapport(chemin, temperatures):
    moyenne = sum(temperatures) / len(temperatures)
    with open(chemin, "w", encoding="utf-8") as fichier:
        fichier.write(f"Moyenne : {moyenne:.2f} °C\n")
        fichier.write(f"Minimum : {min(temperatures):.2f} °C\n")
        fichier.write(f"Maximum : {max(temperatures):.2f} °C\n")
```

## Ex. 5 — Convertir la série en kelvins

Fichier : `s3_ex5.py`

```python
import numpy as np


def convertir_en_kelvins(temperatures):
    tableau = np.array(temperatures)
    return tableau + 273.15
```

## Ex. 6 — Construire l'axe du temps

Fichier : `s3_ex6.py`

```python
import numpy as np


def creer_instants(duree, nombre):
    return np.linspace(0, duree, nombre)
```

## Ex. 7 — Charger les colonnes avec NumPy

Fichier : `s3_ex7.py`

```python
import numpy as np


def charger_mesures_numpy(chemin):
    donnees = np.loadtxt(chemin, delimiter=";", skiprows=1)
    return (donnees[:, 0], donnees[:, 1])
```

## Ex. 8 — Corriger l'étalonnage

Fichier : `s3_ex8.py`

```python
import numpy as np


def corriger_mesures(mesures, coefficient, decalage):
    tableau = np.array(mesures)
    return tableau * coefficient + decalage
```

## Ex. 9 — Résumer la campagne

Fichier : `s3_ex9.py`

```python
import numpy as np


def calculer_statistiques(mesures):
    tableau = np.array(mesures)
    return (tableau.mean(), tableau.std(), tableau.min(), tableau.max())
```

## Ex. 10 — Comparer les capteurs

Fichier : `s3_ex10.py`

```python
def calculer_moyennes(tableau):
    return (tableau.mean(axis=1), tableau.mean(axis=0))
```
