"""
Fonctions utilitaires de l'application de cours.

Ce module illustre volontairement quelques bonnes pratiques enseignées
dans le cours : fonctions documentées, lecture de fichiers avec `with`,
gestion des erreurs, typage indicatif.
"""

from pathlib import Path
import io
import re
import base64
import contextlib

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
    chemin = Path(chemin_fichier)
    if not chemin.exists():
        return ["*(Contenu à venir pour cette séance)*"]

    texte = chemin.read_text(encoding="utf-8")
    texte = corriger_espacement_listes(texte)
    texte = _integrer_images_locales(texte, chemin.parent)
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
        "Séance 1 — Machine, logiciel et bases de Python": str(base / "seance1.md"),
        "Séance 2 — Structures": str(base / "seance2.md"),
        "Séance 3 — Calcul scientifique": str(base / "seance3.md"),
        "Séance 4 — Visualisation et instrumentation": str(base / "seance4.md"),
    }


def liste_exercices() -> dict[str, str]:
    """Associe le nom affiché de chaque séance à son fichier d'exercices."""
    base = Path(__file__).parent / "data" / "exercices"
    return {
        "Séance 1": str(base / "seance1.md"),
        "Séance 2": str(base / "seance2.md"),
        "Séance 3": str(base / "seance3.md"),
        "Séance 4": str(base / "seance4.md"),
    }
