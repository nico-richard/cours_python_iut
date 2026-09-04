# Correction — Séance 2

## Exercice 1 — Calculer puis tester une moyenne

```python
def moyenne(valeurs):
    """Renvoie la moyenne d'une liste non vide."""
    return sum(valeurs) / len(valeurs)


def tester_moyenne():
    assert moyenne([10, 12, 14]) == 12.0
    assert moyenne([5]) == 5.0
    assert moyenne([-2, 2]) == 0.0


if __name__ == "__main__":
    tester_moyenne()
    print("Tous les tests de moyenne sont réussis.")
```

La fonction `moyenne` réalise uniquement le calcul et renvoie le résultat.
La fonction `tester_moyenne` la réutilise avec plusieurs cas dont on connaît la
réponse. `assert` interrompt le test si le résultat obtenu est différent du
résultat attendu.

## Exercice 2 — Fonction sans `max()`

```python
def maximum(liste):
    plus_grand = liste[0]
    for valeur in liste[1:]:
        if valeur > plus_grand:
            plus_grand = valeur
    return plus_grand
```

## Exercice 3 — Fonctions de conversion

```python
def convertir_depuis_m(valeur, unite="m"):
    if unite == "m":
        return valeur
    if unite == "cm":
        return valeur * 100
    if unite == "km":
        return valeur / 1000
    raise ValueError("Unité inconnue")
```

## Exercice 4 — Tuple et dépaquetage

```python
def coordonnees_gps(coordonnees):
    latitude, longitude = coordonnees
    print(f"Latitude : {latitude}, longitude : {longitude}")
    return coordonnees
```

## Exercice 5 — Découpage et nettoyage de texte

```python
def analyser_phrase(phrase):
    mots = phrase.split()
    return phrase[:5], phrase[-5:], mots[::2]


def nettoyer_noms(texte):
    return [nom.strip() for nom in texte.split(";")]
```

## Exercice 6 — Recherche avec `while` et `break`

```python
def premiere_mesure_superieure(mesures, seuil):
    indice = 0
    while indice < len(mesures):
        mesure = mesures[indice]
        indice += 1
        if mesure < 0:
            continue
        if mesure > seuil:
            return indice - 1
    return None
```
