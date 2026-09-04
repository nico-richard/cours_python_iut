# Validation locale — séance 2

## Utilisation

1. Copiez `validation_seance2.py` dans le dossier où vous écrivez votre travail.
2. Créez dans ce même dossier un fichier nommé `seance2.py`.
3. Écrivez vos fonctions dans `seance2.py`.
4. Lancez :

```text
python validation_seance2.py
```

Le correcteur indique les fonctions réussies et les cas qui échouent. Les
tests visibles ne remplacent pas la réflexion : ajoutez vous-même des cas de
test, notamment avec des listes ou des chaînes vides et des valeurs limites.

## Fonctions attendues

```python
maximum(liste)
convertir_depuis_m(valeur, unite="m")
coordonnees_gps(coordonnees)              # renvoie le tuple reçu
analyser_phrase(phrase)                   # renvoie (5 premiers, 5 derniers, mot sur deux)
nettoyer_noms(texte)
premiere_mesure_superieure(mesures, seuil) # renvoie l'indice, ou None
```

Pour `convertir_depuis_m`, une unité inconnue peut être signalée en levant
`ValueError`. Pour `premiere_mesure_superieure`, les valeurs négatives sont
ignorées et la première valeur strictement supérieure au seuil est recherchée.

Les affichages et les appels à `input()` doivent être placés dans un bloc
protégé :

```python
if __name__ == "__main__":
    # éventuel programme interactif
    ...
```

Ainsi, le correcteur peut importer vos fonctions sans lancer le programme
interactif.
