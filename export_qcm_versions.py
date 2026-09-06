"""Exporte les grilles Verificator depuis les versions de projection figées.

Usage : python export_qcm_versions.py chemin/vers/verificator/qcm_keys.json
"""
import argparse
import json
from pathlib import Path


def exporter(destination: Path) -> None:
    source = Path(__file__).parent / "data" / "qcm_versions.json"
    catalogue = json.loads(source.read_text(encoding="utf-8"))
    grilles = {
        identifiant: {
            "titre": qcm["titre"],
            **{
                version: [
                    None if question.get("sondage") else "ABCD"[question["reponse"]]
                    for question in qcm[version]
                ]
                for version in ("A", "B")
            },
        }
        for identifiant, qcm in catalogue.items()
    }
    destination.write_text(json.dumps(grilles, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("destination", type=Path)
    exporter(parser.parse_args().destination)
