"""Correcteur local des exercices de la séance 2.

Usage : placer le fichier de l'étudiant sous le nom ``seance2.py`` dans le
même dossier, puis lancer :

    python validation_seance2.py

Le fichier étudiant doit définir les fonctions indiquées dans
``README_validation_seance2.md``.
"""

from __future__ import annotations

import importlib.util
import inspect
import sys
import traceback
from pathlib import Path


FICHIER_ETUDIANT = Path(__file__).with_name("seance2.py")


def charger_module():
    if not FICHIER_ETUDIANT.exists():
        print(f"Fichier introuvable : {FICHIER_ETUDIANT.name}")
        print("Créez ce fichier à côté du correcteur, puis relancez la validation.")
        return None
    spec = importlib.util.spec_from_file_location("seance2_etudiant", FICHIER_ETUDIANT)
    module = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(module)
    except Exception:
        print("Votre fichier contient une erreur lors de son chargement :")
        traceback.print_exc()
        return None
    return module


def verifier(module, nom, cas):
    """Exécute une série de cas et affiche un résultat pédagogique."""
    fonction = getattr(module, nom, None)
    if not callable(fonction):
        print(f"[À compléter] {nom} : fonction absente")
        return False

    ok = True
    for arguments, attendu in cas:
        try:
            obtenu = fonction(*arguments)
            if obtenu != attendu:
                print(f"[ÉCHEC] {nom}{arguments} -> {obtenu!r}, attendu {attendu!r}")
                ok = False
        except Exception as erreur:
            print(f"[ÉCHEC] {nom}{arguments} -> {type(erreur).__name__}: {erreur}")
            ok = False
    if ok:
        print(f"[OK] {nom} : {len(cas)} cas réussis")
    return ok


def verifier_signature(module, nom, nombre_parametres):
    fonction = getattr(module, nom, None)
    if not callable(fonction):
        return True
    try:
        parametres = inspect.signature(fonction).parameters
        if len(parametres) < nombre_parametres:
            print(f"[ÉCHEC] {nom} : au moins {nombre_parametres} paramètre(s) attendu(s)")
            return False
    except (TypeError, ValueError):
        pass
    return True


def main():
    module = charger_module()
    if module is None:
        return 1

    resultats = []
    resultats.append(verifier(module, "maximum", [
        (([3, 1, 8, 2],), 8),
        (([-4, -2, -9],), -2),
        (([7],), 7),
    ]))
    resultats.append(verifier(module, "convertir_depuis_m", [
        ((2, "m"), 2),
        ((2, "cm"), 200),
        ((2, "km"), 0.002),
    ]))
    resultats.append(verifier(module, "coordonnees_gps", [
        (((48.8566, 2.3522),), (48.8566, 2.3522)),
    ]))
    resultats.append(verifier(module, "analyser_phrase", [
        (("abcdef ghi",), ("abcde", "f ghi", ["abcdef", "ghi"])),
    ]))
    resultats.append(verifier(module, "nettoyer_noms", [
        (("  Alice ; Bob ;Charlie  ",), ["Alice", "Bob", "Charlie"]),
        (("Un;  Deux ;Trois",), ["Un", "Deux", "Trois"]),
    ]))
    resultats.append(verifier(module, "premiere_mesure_superieure", [
        (((-2, 1, 4, 7), 5), 3),
        (((-2, 1, 4), 10), None),
    ]))

    reussis = sum(resultats)
    print(f"\nRésultat : {reussis}/{len(resultats)} exercice(s) validé(s).")
    return 0 if reussis == len(resultats) else 1


if __name__ == "__main__":
    sys.exit(main())
