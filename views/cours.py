"""Page "Cours" : diapositives d'une séance, avec un mode d'affichage
grand format pensé pour la projection en salle ("mode Tableau")."""

import re

import streamlit as st
from utils import charger_document, charger_slides, liste_seances

CSS_MODE_TABLEAU = """
<style>
[data-testid="stMarkdownContainer"] h1 { font-size: 3.2rem !important; }
[data-testid="stMarkdownContainer"] h2 { font-size: 2.5rem !important; }
[data-testid="stMarkdownContainer"] h3 { font-size: 2.1rem !important; }
[data-testid="stMarkdownContainer"] p,
[data-testid="stMarkdownContainer"] li {
    font-size: 1.7rem !important;
    line-height: 1.7 !important;
}
[data-testid="stMarkdownContainer"] code {
    font-size: 1.35rem !important;
}
[data-testid="stMarkdownContainer"] pre code {
    font-size: 1.35rem !important;
    line-height: 1.5 !important;
}
div.stButton > button {
    font-size: 1.6rem !important;
    padding: 0.6rem 1.6rem !important;
}
.block-container {
    max-width: 1100px;
    padding-top: 2rem;
}
</style>
"""


def _afficher_diaporama(chemin_seance: str) -> None:
    """Affiche une seule diapositive avec la navigation de projection."""
    slides = charger_slides(chemin_seance)
    nb_slides = len(slides)
    index = min(st.session_state.get("index_slide", 0), nb_slides - 1)

    st.progress((index + 1) / nb_slides)

    col_prec, col_compteur, col_suiv = st.columns([1, 1, 1])
    if col_prec.button("◀ Précédent", use_container_width=True) and index > 0:
        index -= 1
    col_compteur.markdown(
        f"<p style='text-align:center; padding-top:0.5rem;'>Diapo {index + 1}/{nb_slides}</p>",
        unsafe_allow_html=True,
    )
    if col_suiv.button("Suivant ▶", use_container_width=True) and index < nb_slides - 1:
        index += 1

    st.session_state["index_slide"] = index
    st.divider()
    st.markdown(slides[index])


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
        st.markdown(section)


def page_cours() -> None:
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

    mode_tableau = False
    if mode_affichage == "Diaporama":
        mode_tableau = st.sidebar.toggle(
            "🖥️ Mode Tableau (grand affichage)",
            value=st.session_state.get("mode_tableau", False),
            help="Agrandit le texte pour une lecture confortable en fond de salle.",
        )
    st.session_state["mode_tableau"] = mode_tableau
    if mode_tableau:
        st.markdown(CSS_MODE_TABLEAU, unsafe_allow_html=True)

    if mode_affichage == "Diaporama":
        _afficher_diaporama(seances[nom_seance])
    else:
        _afficher_lecture(seances[nom_seance])
