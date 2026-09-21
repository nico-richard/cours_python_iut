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
        st.markdown(chemin.read_text(encoding="utf-8"))
    else:
        st.warning("Énoncé non encore renseigné pour cette évaluation.")
