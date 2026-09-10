"""
Génération de versions imprimables (PDF) des séances de cours.

Convertit le Markdown du cours et des exercices en HTML mis en forme, puis
en PDF via xhtml2pdf (pure Python, sans dépendance système).
"""

from pathlib import Path
import io
import re
import markdown
from xhtml2pdf import pisa

from utils import (
    _integrer_images_locales,
    corriger_espacement_listes,
    traiter_blocs_pedagogiques,
    traiter_diagrammes,
)

CSS_IMPRESSION = """
<style>
    @page {
        size: A4;
        margin: 2cm;
        @frame footer_frame {
            -pdf-frame-content: footer_content;
            bottom: 1cm; margin-left: 2cm; margin-right: 2cm; height: 1cm;
        }
    }
    body { font-family: Helvetica, Arial, sans-serif; font-size: 10.5pt; line-height: 1.4; color: #1a1a1a; }
    h1 { font-size: 20pt; color: #1e3a5f; border-bottom: 2px solid #1e3a5f; padding-bottom: 6px; }
    h2 { font-size: 15pt; color: #1e3a5f; margin-top: 18px; -pdf-keep-with-next: true; }
    h3 { font-size: 12.5pt; color: #2a4d75; margin-top: 14px; -pdf-keep-with-next: true; }
    p, li { text-align: justify; }
    code {
        font-family: Courier, monospace; background-color: #f0f0f0;
        padding: 1px 4px; font-size: 9.5pt; color: #333;
    }
    pre {
        font-family: Courier, monospace; background-color: #f5f5f5;
        border: 0.5px solid #ccc; padding: 8px; font-size: 9pt;
        line-height: 1.3; white-space: pre-wrap; -pdf-keep-with-next: true;
    }
    pre code { background-color: transparent; padding: 0; }
    blockquote {
        margin: 10px 0; padding: 8px 12px; background-color: #eef5fb;
        border-left: 4px solid #2a6f9e; color: #1f3444;
    }
    blockquote p { margin: 3px 0; text-align: left; }
    .diagram-wrapper { width: 100%; margin: 12px 0; }
    table.diagram-flow { width: 100%; border-spacing: 6px; }
    table.diagram-flow td.diagram-node {
        border: 1.5px solid #2a6f9e; background-color: #eef5fb;
        color: #17324d; padding: 8px; text-align: center; font-weight: bold;
    }
    table.diagram-flow td.diagram-arrow {
        border: none; width: 18px; padding: 2px; text-align: center;
        vertical-align: middle; color: #2a6f9e; font-weight: bold;
    }
    .diagram-wrapper-vertical-pdf { width: 100%; margin: 12px 0; }
    table.diagram-step-vertical-pdf {
        width: 70%; margin-left: 15%; border-spacing: 0;
        -pdf-keep-with-next: true;
    }
    table.diagram-step-vertical-pdf td.diagram-node-vertical-pdf {
        width: 100%; padding: 8px; border: 1.5px solid #2a6f9e;
        background-color: #eef5fb; color: #17324d;
        text-align: center; font-weight: bold;
    }
    table.diagram-step-vertical-pdf td.diagram-arrow-vertical-pdf {
        width: 100%; border: none;
        height: 12px; margin: 0; padding: 0; line-height: 10px;
        color: #2a6f9e; text-align: center; font-weight: bold;
    }
    hr { border: none; border-top: 1px solid #ccc; margin: 14px 0; }
    img { max-width: 90%; margin: 8px 0; }
    .page-break { page-break-before: always; }
    .titre-page { text-align: center; margin-top: 30%; }
    .titre-page h1 { border: none; font-size: 26pt; }
    .titre-page p { text-align: center; font-size: 13pt; color: #555; }
</style>
"""


def _markdown_vers_html(chemin_fichier: Path) -> str:
    """Charge un fichier .md, intègre ses images locales, et le convertit en HTML."""
    if not chemin_fichier.exists():
        return "<p><em>(Contenu non disponible)</em></p>"
    texte = chemin_fichier.read_text(encoding="utf-8")
    texte = traiter_blocs_pedagogiques(texte, inclure_support=True)
    texte = traiter_diagrammes(texte, mode_impression=True)
    texte = corriger_espacement_listes(texte)
    # Les séparateurs de diapositives structurent l'écran mais ne doivent pas
    # devenir une succession de traits horizontaux dans le polycopié.
    texte = re.sub(r"(?m)^---\s*$", "", texte)
    texte = _integrer_images_locales(texte, chemin_fichier.parent)
    html = markdown.markdown(texte, extensions=["fenced_code", "tables"])

    # xhtml2pdf ne respecte pas toujours ``white-space: pre-wrap`` et peut
    # fusionner toutes les lignes d'un bloc <pre>. Des balises <br /> rendent
    # les retours à la ligne explicites, sans modifier le code affiché.
    def preserver_sauts_ligne_code(match: re.Match) -> str:
        ouverture, contenu, fermeture = match.groups()
        lignes = contenu.rstrip("\n").split("\n")
        for index, ligne in enumerate(lignes):
            indentation = len(ligne) - len(ligne.lstrip(" \t"))
            espaces = (
                ligne[:indentation]
                .replace("\t", "&nbsp;" * 4)
                .replace(" ", "&nbsp;")
            )
            lignes[index] = espaces + ligne[indentation:]
        contenu = "<br />\n".join(lignes)
        return f"{ouverture}{contenu}{fermeture}"

    return re.sub(
        r'(<pre><code(?:\s+class="[^"]*")?>)(.*?)(</code></pre>)',
        preserver_sauts_ligne_code,
        html,
        flags=re.DOTALL,
    )


def _produire_pdf(html_complet: str) -> bytes:
    """Convertit le HTML en PDF et signale explicitement tout échec d'export."""
    sortie = io.BytesIO()
    resultat = pisa.CreatePDF(src=html_complet, dest=sortie, encoding="utf-8")
    if resultat.err:
        raise RuntimeError(
            f"La génération du PDF a échoué avec {resultat.err} erreur(s)."
        )
    donnees = sortie.getvalue()
    if not donnees.startswith(b"%PDF-"):
        raise RuntimeError("La génération n'a pas produit un fichier PDF valide.")
    return donnees


def generer_pdf_seance(
    titre_seance: str,
    chemin_cours: str,
    chemin_exercices: str | None,
    inclure_exercices: bool = True,
) -> bytes:
    """Assemble le cours et les exercices d'une séance en un PDF imprimable.

    Args:
        titre_seance: titre affiché en page de garde (ex: "Séance 1 — ...").
        chemin_cours: chemin du fichier Markdown des diapositives de cours.
        chemin_exercices: chemin du fichier Markdown des exercices, ou ``None``
            lorsqu'une séance ne possède pas de travaux pratiques.

    Returns:
        Le contenu binaire du PDF généré.
    """
    html_cours = _markdown_vers_html(Path(chemin_cours))
    bloc_exercices = ""
    if inclure_exercices and chemin_exercices:
        html_exercices = _markdown_vers_html(Path(chemin_exercices))
        bloc_exercices = f"""
        <div class="page-break"></div>
        {html_exercices}
        """

    html_complet = f"""
    <html><head>{CSS_IMPRESSION}</head><body>
        <div class="titre-page">
            <h1>{titre_seance}</h1>
            <p>Introduction à la programmation Python — IUT 1re année</p>
        </div>
        <div class="page-break"></div>
        {html_cours}
        {bloc_exercices}
        <div id="footer_content" style="text-align:center; font-size:8pt; color:#888;">
            {titre_seance} — page <pdf:pagenumber>
        </div>
    </body></html>
    """
    return _produire_pdf(html_complet)


def generer_pdf_exercices_seance(titre_seance: str, chemin_exercices: str) -> bytes:
    """Génère un fascicule de TP indépendant pour une séance."""
    html_exercices = _markdown_vers_html(Path(chemin_exercices))
    html_complet = f"""
    <html><head>{CSS_IMPRESSION}</head><body>
        <div class="titre-page">
            <h1>Travaux pratiques</h1>
            <p>{titre_seance}</p>
        </div>
        <div class="page-break"></div>
        {html_exercices}
        <div id="footer_content" style="text-align:center; font-size:8pt; color:#888;">
            Travaux pratiques — {titre_seance} — page <pdf:pagenumber>
        </div>
    </body></html>
    """
    return _produire_pdf(html_complet)


def generer_pdf_complet(
    seances: dict[str, str],
    exercices: dict[str, str],
    inclure_exercices: bool = True,
) -> bytes:
    """Assemble toutes les séances (cours + exercices) en un seul PDF (polycopié complet).

    Args:
        seances: dict {nom_affiché: chemin_fichier_cours} (voir utils.liste_seances).
        exercices: dict {"Séance N": chemin_fichier_exercices} (voir utils.liste_exercices).

    Returns:
        Le contenu binaire du PDF généré.
    """
    blocs = []
    for titre, chemin_cours in seances.items():
        html_cours = _markdown_vers_html(Path(chemin_cours))
        correspondance_numero = re.match(r"Séance (\d+)", titre)
        numero = correspondance_numero.group(1) if correspondance_numero else ""
        chemin_exercices = exercices.get(f"Séance {numero}")
        html_exercices = (
            _markdown_vers_html(Path(chemin_exercices)) if chemin_exercices else ""
        )
        bloc_exercices = ""
        if inclure_exercices and html_exercices:
            bloc_exercices = (
                '<div class="page-break"></div>'
                f"{html_exercices}"
            )
        saut = '<div class="page-break"></div>'
        blocs.append(f"""
            {saut}
            {html_cours}
            {bloc_exercices}
        """)

    html_complet = f"""
    <html><head>{CSS_IMPRESSION}</head><body>
        <div class="titre-page">
            <h1>Introduction à la programmation Python</h1>
            <p>Support de cours complet — IUT 1re année</p>
        </div>
        {''.join(blocs)}
        <div id="footer_content" style="text-align:center; font-size:8pt; color:#888;">
            Introduction à la programmation Python — IUT 1re année — page <pdf:pagenumber>
        </div>
    </body></html>
    """

    return _produire_pdf(html_complet)
