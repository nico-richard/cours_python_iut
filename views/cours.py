"""Page "Cours" : diaporama de projection et support de lecture d'une séance."""

import re

import streamlit as st
import streamlit.components.v1 as components
from utils import charger_document, charger_slides, liste_seances

CSS_DIAPORAMA = """
<style>
[data-testid="stMain"] [data-testid="stMarkdownContainer"] h1 { font-size: 2.8rem !important; }
[data-testid="stMain"] [data-testid="stMarkdownContainer"] h2 { font-size: 2.15rem !important; }
[data-testid="stMain"] [data-testid="stMarkdownContainer"] h3 { font-size: 1.7rem !important; }
[data-testid="stMain"] [data-testid="stMarkdownContainer"] p,
[data-testid="stMain"] [data-testid="stMarkdownContainer"] li {
    font-size: 1.42rem !important;
    line-height: 1.5 !important;
}
[data-testid="stMain"] [data-testid="stMarkdownContainer"] code {
    font-size: 1.15rem !important;
}
[data-testid="stMain"] [data-testid="stMarkdownContainer"] pre code {
    font-size: 1.15rem !important;
    line-height: 1.4 !important;
}
[data-testid="stMain"] [data-testid="stMarkdownContainer"] th,
[data-testid="stMain"] [data-testid="stMarkdownContainer"] td {
    font-size: 1.15rem !important;
    line-height: 1.35 !important;
}
[data-testid="stMain"] div.stButton > button {
    min-height: 2.1rem !important;
    padding: 0.15rem 0.45rem !important;
}
[data-testid="stMain"] div.stButton > button p {
    font-size: 1.05rem !important;
    line-height: 1.1 !important;
}
[data-testid="stMain"] [data-testid="stProgress"] p {
    font-size: 0.85rem !important;
    line-height: 1.1 !important;
    margin-bottom: 0.15rem !important;
}
[data-testid="stMain"] hr {
    margin: 0.25rem 0 0.75rem !important;
}
[data-testid="stMainBlockContainer"] {
    max-width: 1200px;
    padding-top: 4rem;
}
</style>
"""

CSS_DIAGRAMMES = """
<style>
.diagram-wrapper {
    width: 100%;
    overflow-x: auto;
    margin: 1.2rem 0;
}
table.diagram-flow {
    width: 100%;
    border-collapse: separate;
    border-spacing: 0.7rem;
    table-layout: fixed;
}
table.diagram-flow td.diagram-node {
    border: 2px solid #2a6f9e !important;
    border-radius: 10px;
    background: #eef5fb;
    color: #17324d;
    padding: 0.85rem 1rem;
    text-align: center;
    vertical-align: middle;
    font-weight: 600;
}
table.diagram-flow td.diagram-arrow {
    border: none !important;
    background: transparent;
    width: 2rem;
    padding: 0;
    text-align: center;
    vertical-align: middle;
    color: #2a6f9e;
    font-size: 1.6rem;
    font-weight: 700;
}
table.diagram-flow-vertical {
    width: min(100%, 650px);
    margin: 0 auto;
}
table.diagram-flow-vertical td.diagram-arrow-vertical {
    width: auto;
    height: 1.8rem;
}
</style>
"""


def _changer_slide(pas: int, nb_slides: int) -> None:
    """Déplace l'index courant avant le nouveau rendu de la page."""
    index = st.session_state.get("index_slide", 0)
    st.session_state["index_slide"] = max(0, min(index + pas, nb_slides - 1))


def _activer_navigation_clavier() -> None:
    """Associe les flèches gauche et droite aux boutons de navigation."""
    components.html(
        """
        <script>
        (() => {
            const host = window.parent;
            const handlerName = "__coursPythonSlideKeyboardHandler";

            if (host[handlerName]) {
                host.removeEventListener("keydown", host[handlerName]);
            }

            const handler = (event) => {
                if (event.key !== "ArrowLeft" && event.key !== "ArrowRight") return;

                const target = event.target;
                const tag = target && target.tagName ? target.tagName.toLowerCase() : "";
                const isEditable = target && (
                    target.isContentEditable || tag === "input" || tag === "textarea" || tag === "select"
                );
                if (isEditable) return;

                const label = event.key === "ArrowLeft" ? "←" : "→";
                const button = Array.from(host.document.querySelectorAll("button")).find(
                    (item) => item.innerText.trim() === label
                );

                if (button && !button.disabled) {
                    event.preventDefault();
                    button.click();
                }
            };

            host[handlerName] = handler;
            host.addEventListener("keydown", handler);
        })();
        </script>
        """,
        height=0,
    )


def _afficher_diaporama(chemin_seance: str) -> None:
    """Affiche une seule diapositive avec la navigation de projection."""
    slides = charger_slides(chemin_seance)
    nb_slides = len(slides)
    index = min(st.session_state.get("index_slide", 0), nb_slides - 1)
    st.session_state["index_slide"] = index

    col_prec, col_progression, col_suiv = st.columns([0.7, 8, 0.7], gap="small")
    col_prec.button(
        "←",
        key="diapo_precedente",
        help="Diapositive précédente — flèche gauche",
        disabled=index == 0,
        use_container_width=True,
        on_click=_changer_slide,
        args=(-1, nb_slides),
    )
    col_progression.progress(
        (index + 1) / nb_slides,
        text=f"Diapo {index + 1}/{nb_slides}",
    )
    col_suiv.button(
        "→",
        key="diapo_suivante",
        help="Diapositive suivante — flèche droite",
        disabled=index == nb_slides - 1,
        use_container_width=True,
        on_click=_changer_slide,
        args=(1, nb_slides),
    )

    st.divider()
    st.markdown(slides[index], unsafe_allow_html=True)
    _activer_navigation_clavier()


def _afficher_lecture(chemin_seance: str) -> None:
    """Affiche le cours complet, compléments étudiants inclus."""
    document = charger_document(chemin_seance, inclure_support=True)
    sections = [bloc.strip() for bloc in document.split("\n---\n") if bloc.strip()]

    with st.expander("Sommaire de la séance"):
        for numero, section in enumerate(sections, start=1):
            titre = re.search(r"(?m)^#{1,3}\s+(.+)$", section)
            if titre:
                st.write(f"{numero}. {titre.group(1)}")

    for numero, section in enumerate(sections):
        if numero:
            st.divider()
        st.markdown(section, unsafe_allow_html=True)


def page_cours() -> None:
    st.markdown(CSS_DIAGRAMMES, unsafe_allow_html=True)
    st.sidebar.subheader("📘 Cours")
    seances = liste_seances()
    nom_seance = st.sidebar.selectbox("Séance", list(seances.keys()))
    mode_affichage = st.sidebar.radio(
        "Affichage",
        ["Diaporama", "Lecture"],
        horizontal=True,
        help="Diaporama masque les compléments étudiants ; Lecture affiche le cours complet.",
    )

    # Réinitialise l'index de diapositive quand on change de séance
    if st.session_state.get("seance_courante") != nom_seance:
        st.session_state["seance_courante"] = nom_seance
        st.session_state["index_slide"] = 0

    if mode_affichage == "Diaporama":
        st.markdown(CSS_DIAPORAMA, unsafe_allow_html=True)

    if mode_affichage == "Diaporama":
        _afficher_diaporama(seances[nom_seance])
    else:
        _afficher_lecture(seances[nom_seance])
