"""Page affichant les exercices de la séance sélectionnée."""

import streamlit as st
from pathlib import Path
from utils import liste_exercices


def page_exercices() -> None:
    st.sidebar.subheader("📝 Exercices")
    st.title("📝 Exercices")

    exercices = liste_exercices()
    nom = st.selectbox("Séance", list(exercices.keys()))

    chemin = Path(exercices[nom])
    if chemin.exists():
        st.markdown(chemin.read_text(encoding="utf-8"))
    else:
        st.warning("Exercices non encore renseignés pour cette séance.")
