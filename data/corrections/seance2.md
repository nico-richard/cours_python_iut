# Correction — Séance 2

Document enseignant. Chaque bloc est un fichier Python complet et indépendant, sans affichage ni saisie. Les solutions utilisent uniquement les notions des séances 1 et 2.

## Ex. 1 — Démarrer le capteur de température

Fichier : `s2_ex1.py`

```python
def convertir_c_en_k(temperature_c):
    return temperature_c + 273.15
```

## Ex. 2 — Adapter les unités de distance

Fichier : `s2_ex2.py`

```python
def convertir_depuis_m(valeur, unite="m"):
    if unite == "cm":
        resultat = valeur * 100
    elif unite == "km":
        resultat = valeur / 1000
    else:
        resultat = valeur
    return round(resultat, 1)
```

## Ex. 3 — Positionner un capteur

Fichier : `s2_ex3.py`

```python
def deplacer(position, dx, dy):
    x, y = position
    return (x + dx, y + dy)
```

## Ex. 4 — Produire le premier bilan

Fichier : `s2_ex4.py`

```python
def moyenne(valeurs):
    return round(sum(valeurs) / len(valeurs), 2)
```

## Ex. 5 — Lire un message de la station

Fichier : `s2_ex5.py`

```python
def analyser_phrase(phrase):
    premier = phrase[:1]
    debut = phrase[:5]
    fin = phrase[-5:]
    mots = phrase.split()
    return (premier, debut, fin, mots)
```

## Ex. 6 — Simuler une campagne de mesures

Fichier : `s2_ex6.py`

```python
def generer_mesures(debut, pas, nombre):
    mesures = []
    for indice in range(nombre):
        mesures.append(debut + indice * pas)
    return mesures
```

## Ex. 7 — Repérer le pic de mesure

Fichier : `s2_ex7.py`

```python
def maximum(valeurs):
    plus_grand = valeurs[0]
    for valeur in valeurs[1:]:
        if valeur > plus_grand:
            plus_grand = valeur
    return plus_grand
```

## Ex. 8 — Enregistrer les capteurs

Fichier : `s2_ex8.py`

```python
def nettoyer_noms(texte):
    noms = []
    for morceau in texte.split(";"):
        nom = morceau.strip()
        if nom != "":
            noms.append(nom)
    return noms
```

## Ex. 9 — Suivre la recharge de la batterie

Fichier : `s2_ex9.py`

```python
def atteindre_objectif(initial, ajout, objectif):
    quantite = initial
    etapes = 0
    while quantite < objectif:
        quantite += ajout
        etapes += 1
    return (etapes, quantite)
```

## Ex. 10 — Déclencher la première alerte

Fichier : `s2_ex10.py`

```python
def premiere_mesure_superieure(mesures, seuil):
    indice = 0
    resultat = -1
    while indice < len(mesures):
        mesure = mesures[indice]
        if mesure < 0:
            indice += 1
            continue
        if mesure > seuil:
            resultat = indice
            break
        indice += 1
    return resultat
```
