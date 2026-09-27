"""Page de projection des énoncés d'examen."""

from pathlib import Path

import streamlit as st

from utils import liste_examens


CSS_EXAMEN = """
<style>
[data-testid="stMain"] [data-testid="stMarkdownContainer"] h1 {
    font-size: 2.6rem !important;
}
[data-testid="stMain"] [data-testid="stMarkdownContainer"] h2 {
    font-size: 1.8rem !important;
}
[data-testid="stMain"] [data-testid="stMarkdownContainer"] p,
[data-testid="stMain"] [data-testid="stMarkdownContainer"] li {
    font-size: 1.25rem !important;
    line-height: 1.45 !important;
}
[data-testid="stMain"] [data-testid="stMarkdownContainer"] code {
    font-size: 1.05rem !important;
}
[data-testid="stMainBlockContainer"] {
    max-width: 1200px;
    padding-top: 3rem;
}
[data-testid="stMain"] [data-testid="stHorizontalBlock"] > [data-testid="stColumn"]:first-child {
    border-right: 2px solid rgba(128, 128, 128, 0.35);
    padding-right: 2rem;
}
</style>
"""


def page_examen() -> None:
    """Affiche l'énoncé sélectionné avec une mise en page adaptée au tableau."""
    st.markdown(CSS_EXAMEN, unsafe_allow_html=True)
    st.sidebar.subheader("🎓 Examen")

    examens = liste_examens()
    nom = st.sidebar.selectbox("Évaluation", list(examens))
    chemin = Path(examens[nom])

    if chemin.exists():
        contenu = chemin.read_text(encoding="utf-8")
        sections = contenu.split("<!-- colonne -->")
        if len(sections) == 3:
            st.markdown(sections[0])
            colonne_gauche, colonne_droite = st.columns(2, gap="large")
            with colonne_gauche:
                st.markdown(sections[1])
            with colonne_droite:
                st.markdown(sections[2])
        else:
            st.markdown(contenu)
    else:
        st.warning("Énoncé non encore renseigné pour cette évaluation.")
