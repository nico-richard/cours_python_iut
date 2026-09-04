"""
Fonctions utilitaires de l'application de cours.

Ce module illustre volontairement quelques bonnes pratiques enseignées
dans le cours : fonctions documentées, lecture de fichiers avec `with`,
gestion des erreurs, typage indicatif.
"""

from pathlib import Path
import json
import io
import re
import base64
import contextlib
import html
import random

_TYPES_MIME = {
    ".png": "image/png",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".gif": "image/gif",
    ".svg": "image/svg+xml",
    ".webp": "image/webp",
}

_MOTIF_IMAGE_MARKDOWN = re.compile(r"!\[([^\]]*)\]\(([^)\s]+)\)")
_MOTIF_DEBUT_LISTE = re.compile(r"^(\s*)([-*+]\s+|\d+\.\s+)")
_MOTIF_BLOC_PEDAGOGIQUE = re.compile(
    r"(?ms)^:::(support|attention|retenir)[ \t]*\r?\n(.*?)^:::[ \t]*$"
)
_MOTIF_DIAGRAMME = re.compile(
    r"(?ms)^:::diagram(?:[ \t]+(vertical))?[ \t]*\r?\n(.*?)^:::[ \t]*$"
)

_LIBELLES_BLOCS = {
    "support": "📖 Complément pour le support étudiant",
    "attention": "⚠️ Attention",
    "retenir": "✅ À retenir",
}


def corriger_espacement_listes(texte: str) -> str:
    """Insère une ligne vide avant une liste Markdown si elle en manque.

    En Markdown standard (CommonMark, utilisé par Streamlit et par le
    convertisseur PDF), une liste doit être précédée d'une ligne vide pour
    être reconnue comme telle — sinon elle fusionne avec le paragraphe qui
    précède. Cette fonction corrige automatiquement l'oubli.
    """
    lignes = texte.split("\n")
    resultat: list[str] = []
    for ligne in lignes:
        est_liste = bool(_MOTIF_DEBUT_LISTE.match(ligne))
        if est_liste and resultat:
            precedente = resultat[-1]
            precedente_est_liste = bool(_MOTIF_DEBUT_LISTE.match(precedente))
            if precedente.strip() != "" and not precedente_est_liste:
                resultat.append("")
        resultat.append(ligne)
    return "\n".join(resultat)


def traiter_blocs_pedagogiques(texte: str, inclure_support: bool = True) -> str:
    """Convertit les blocs pédagogiques en Markdown standard.

    Syntaxe reconnue::

        :::support
        Explication destinée au polycopié et au mode Lecture.
        :::

    ``support`` est masqué en mode projection. Les blocs ``attention`` et
    ``retenir`` restent visibles dans tous les modes. Le résultat utilise une
    citation Markdown, comprise à la fois par Streamlit et l'export PDF.
    """

    def remplacer(match: re.Match) -> str:
        nature, contenu = match.group(1), match.group(2).strip()
        if nature == "support" and not inclure_support:
            return ""
        if nature == "support":
            lignes = []
        else:
            lignes = [f"> **{_LIBELLES_BLOCS[nature]}**", ">"]
        lignes.extend(f"> {ligne}" if ligne else ">" for ligne in contenu.splitlines())
        return "\n".join(lignes)

    return _MOTIF_BLOC_PEDAGOGIQUE.sub(remplacer, texte)


def _formater_noeud_diagramme(texte: str) -> str:
    """Échappe un libellé de diagramme et conserve un formatage inline minimal."""
    texte = html.escape(texte.strip())
    texte = re.sub(r"`([^`]+)`", r"<code>\1</code>", texte)
    texte = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", texte)
    return texte


def traiter_diagrammes(texte: str, mode_impression: bool = False) -> str:
    """Transforme un bloc ``:::diagram`` en diagramme HTML accessible.

    Chaque ligne non vide devient un bloc encadré. Par défaut les blocs sont
    disposés horizontalement ; ``:::diagram vertical`` produit une chaîne
    verticale adaptée aux séquences longues. Le mode impression utilise des
    blocs indépendants et des flèches ASCII, mieux pris en charge par xhtml2pdf.
    """

    def remplacer(match: re.Match) -> str:
        vertical = bool(match.group(1))
        noeuds = [
            _formater_noeud_diagramme(ligne)
            for ligne in match.group(2).splitlines()
            if ligne.strip()
        ]
        if not noeuds:
            return ""

        if vertical and mode_impression:
            etapes = []
            for index, noeud in enumerate(noeuds):
                ligne_fleche = (
                    '<tr><td class="diagram-arrow-vertical-pdf">v</td></tr>'
                    if index > 0
                    else ""
                )
                etapes.append(
                    '<table class="diagram-step-vertical-pdf" role="presentation">'
                    f"{ligne_fleche}"
                    f'<tr><td class="diagram-node-vertical-pdf">{noeud}</td></tr>'
                    "</table>"
                )
            return (
                '\n\n<div class="diagram-wrapper diagram-wrapper-vertical-pdf">'
                f"{''.join(etapes)}</div>\n\n"
            )

        if vertical:
            lignes = []
            for index, noeud in enumerate(noeuds):
                if index:
                    lignes.append(
                        '<tr><td class="diagram-arrow diagram-arrow-vertical">↓</td></tr>'
                    )
                lignes.append(f'<tr><td class="diagram-node">{noeud}</td></tr>')
            contenu = "".join(lignes)
            classe = "diagram-flow diagram-flow-vertical"
        else:
            cellules = []
            for index, noeud in enumerate(noeuds):
                if index:
                    fleche = "-&gt;" if mode_impression else "→"
                    cellules.append(f'<td class="diagram-arrow">{fleche}</td>')
                cellules.append(f'<td class="diagram-node">{noeud}</td>')
            contenu = f"<tr>{''.join(cellules)}</tr>"
            classe = "diagram-flow"

        return (
            '\n\n<div class="diagram-wrapper">'
            f'<table class="{classe}" role="presentation">{contenu}</table>'
            "</div>\n\n"
        )

    return _MOTIF_DIAGRAMME.sub(remplacer, texte)


def _en_data_uri(chemin_image: Path) -> str | None:
    """Encode une image locale en data URI base64, ou None si introuvable."""
    if not chemin_image.exists():
        return None
    mime = _TYPES_MIME.get(chemin_image.suffix.lower(), "application/octet-stream")
    donnees = base64.b64encode(chemin_image.read_bytes()).decode("utf-8")
    return f"data:{mime};base64,{donnees}"


def _integrer_images_locales(texte_markdown: str, dossier_base: Path) -> str:
    """Remplace les images locales référencées en Markdown (ex: `images/x.png`)
    par des data URI base64.

    st.markdown() convertit le Markdown en HTML affiché par le navigateur :
    un chemin relatif y est interprété comme une URL web, pas comme un fichier
    sur le disque. On intègre donc directement le contenu de l'image dans le
    HTML pour qu'elle s'affiche, sans dépendre d'un serveur de fichiers statiques.
    Les URLs distantes (http/https) et les data URI existants sont laissés tels quels.
    """

    def remplacer(match: re.Match) -> str:
        alt, chemin = match.group(1), match.group(2)
        if chemin.startswith(("http://", "https://", "data:")):
            return match.group(0)
        chemin_complet = (dossier_base / chemin).resolve()
        data_uri = _en_data_uri(chemin_complet)
        if data_uri is None:
            return f"*(image introuvable : {chemin})*"
        return f"![{alt}]({data_uri})"

    return _MOTIF_IMAGE_MARKDOWN.sub(remplacer, texte_markdown)


def charger_document(chemin_fichier: str, inclure_support: bool = True) -> str:
    """Charge et prépare un document Markdown pour son affichage."""
    chemin = Path(chemin_fichier)
    if not chemin.exists():
        return "*(Contenu à venir pour cette séance)*"

    texte = chemin.read_text(encoding="utf-8")
    texte = traiter_blocs_pedagogiques(texte, inclure_support=inclure_support)
    texte = traiter_diagrammes(texte)
    texte = corriger_espacement_listes(texte)
    return _integrer_images_locales(texte, chemin.parent)


def charger_slides(chemin_fichier: str) -> list[str]:
    """Charge un fichier Markdown et le découpe en diapositives.

    Les diapositives sont séparées par une ligne contenant uniquement '---'.
    Les images référencées avec un chemin relatif (ex: `images/photo.png`)
    sont résolues par rapport au dossier du fichier Markdown, puis intégrées
    en base64 pour s'afficher correctement.

    Args:
        chemin_fichier: chemin vers le fichier .md de la séance.

    Returns:
        Liste des diapositives (chaque élément = texte Markdown d'une slide).
    """
    texte = charger_document(chemin_fichier, inclure_support=False)
    diapositives = [bloc.strip() for bloc in texte.split("\n---\n") if bloc.strip()]
    return diapositives


def executer_code(code: str) -> tuple[str, str]:
    """Exécute un extrait de code Python et capture sa sortie.

    Utilisé par le "bac à sable" pour faire des démonstrations live en cours.
    Usage strictement local/pédagogique : ne pas exposer sur internet.

    Args:
        code: code Python à exécuter.

    Returns:
        Un tuple (sortie_standard, message_erreur). message_erreur est vide
        si l'exécution s'est déroulée sans exception.
    """
    sortie = io.StringIO()
    erreur = ""
    try:
        with contextlib.redirect_stdout(sortie):
            exec(code, {"__builtins__": __builtins__})
    except Exception as e:
        erreur = f"{type(e).__name__} : {e}"
    return sortie.getvalue(), erreur


def liste_seances() -> dict[str, str]:
    """Associe le nom affiché de chaque séance à son fichier de contenu."""
    base = Path(__file__).parent / "data" / "sessions"
    return {
        "Séance 0 — Présentation du cours": str(base / "seance0.md"),
        "Séance 1 — Premiers programmes Python": str(base / "seance1.md"),
        "Séance 2 — Organiser et répéter les traitements": str(base / "seance2.md"),
        "Séance 3 — Exploiter des données scientifiques": str(base / "seance3.md"),
        "Séance 4 — Visualiser et acquérir des mesures": str(base / "seance4.md"),
    }


def liste_exercices() -> dict[str, str]:
    """Associe le nom affiché de chaque séance à son fichier d'exercices."""
    base = Path(__file__).parent / "data" / "exercices"
    return {
        "Séance 0 — Installation et premiers essais": str(base / "seance0.md"),
        "Séance 1": str(base / "seance1.md"),
        "Séance 2": str(base / "seance2.md"),
        "Séance 3": str(base / "seance3.md"),
        "Séance 4": str(base / "seance4.md"),
    }


def liste_qcm() -> dict[str, str]:
    """Associe chaque questionnaire à son fichier JSON."""
    base = Path(__file__).parent / "data" / "qcm"
    return {
        "Séance 1 — Premiers programmes": str(base / "seance1.json"),
        "Séance 2 — Fonctions, objets et boucles": str(base / "seance2.json"),
        "Séance 3 — Fichiers et NumPy": str(base / "seance3.json"),
        "Séance 4 — Visualisation et instrumentation": str(base / "seance4.json"),
    }


def charger_qcm(chemin_fichier: str) -> dict:
    """Charge un QCM et mélange ses choix de façon stable."""
    chemin = Path(chemin_fichier)
    with chemin.open(encoding="utf-8") as fichier:
        qcm = json.load(fichier)

    for question in qcm["questions"]:
        # Les questions de positionnement n'ont pas de bonne réponse et leur
        # échelle ordonnée doit rester dans l'ordre défini dans le fichier.
        if question.get("sondage"):
            continue
        bonne_reponse = question["choix"][question["reponse"]]
        generateur = random.Random(f"{qcm['titre']}|{question['question']}")
        generateur.shuffle(question["choix"])
        question["reponse"] = question["choix"].index(bonne_reponse)

    return qcm
