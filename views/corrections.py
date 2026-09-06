"""Page affichant les corrections de la séance sélectionnée."""

from pathlib import Path

import streamlit as st

from utils import liste_corrections


def page_corrections() -> None:
    st.sidebar.subheader("✅ Corrections")
    st.title("✅ Corrections")

    corrections = liste_corrections()
    nom = st.selectbox("Séance", list(corrections.keys()))

    chemin = Path(corrections[nom])
    if chemin.exists():
        st.markdown(chemin.read_text(encoding="utf-8"))
    else:
        st.warning("Corrections non encore renseignées pour cette séance.")
