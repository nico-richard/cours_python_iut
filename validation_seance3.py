"""Validation locale : python validation_seance3.py s3_ex1.py calculer_distance.

Sans argument, valide les dix fonctions d'un fichier seance3.py voisin.
Outil enseignant/local : les soumissions doivent être des fichiers de confiance.
"""

import importlib.util
import subprocess
import sys
from pathlib import Path

from data.validation.seance3 import EXERCICES_SEANCE3


def verifier_fichier(chemin, nom=None):
    exercices = [e for e in EXERCICES_SEANCE3 if nom is None or e.function_name == nom]
    if not exercices:
        print(f"Fonction inconnue : {nom}")
        return 1
    spec = importlib.util.spec_from_file_location("seance3_etudiant", chemin)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    reussis = 0
    for exercice in exercices:
        resultats = exercice.test_module(module)
        valide = all(cas["passed"] for cas in resultats)
        reussis += valide
        print(f"[{'OK' if valide else 'ÉCHEC'}] {exercice.function_name}")
        for cas in resultats:
            if not cas["passed"]:
                print(f"  {cas['name']} : {cas['message']}")
    print(f"Résultat : {reussis}/{len(exercices)} exercice(s) validé(s).")
    return 0 if reussis == len(exercices) else 1


def main():
    arguments = sys.argv[1:]
    if arguments and arguments[0] == "--executer":
        try:
            nom = arguments[2] if len(arguments) > 2 else None
            return verifier_fichier(Path(arguments[1]), nom)
        except Exception as erreur:
            print(f"Erreur de chargement : {type(erreur).__name__}: {erreur}")
            return 1
    chemin = Path(arguments[0]) if arguments else Path(__file__).with_name("seance3.py")
    if not chemin.is_file():
        print(f"Fichier introuvable : {chemin}")
        return 1
    commande = [
        sys.executable,
        str(Path(__file__).resolve()),
        "--executer",
        str(chemin.resolve()),
    ]
    if len(arguments) > 1:
        commande.append(arguments[1])
    try:
        return subprocess.run(
            commande,
            timeout=5,
            stdin=subprocess.DEVNULL,
        ).returncode
    except subprocess.TimeoutExpired:
        print("Délai dépassé (5 s) : vérifier que le programme peut se terminer.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
