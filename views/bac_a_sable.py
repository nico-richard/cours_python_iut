"""Page de démonstration live : exécute du code Python saisi en direct."""

import streamlit as st
from utils import executer_code

EXEMPLE_DEFAUT = (
    "# Exemple : influence du type sur un calcul\n"
    "a = 7\n"
    "b = 2\n"
    "print('division entière :', a // b)\n"
    "print('division flottante :', a / b)\n"
)


def page_bac_a_sable() -> None:
    st.sidebar.subheader("💻 Bac à sable")
    st.title("💻 Bac à sable — démonstration live")

    code = st.text_area("Code Python", value=EXEMPLE_DEFAUT, height=250)

    if st.button("▶ Exécuter"):
        sortie, erreur = executer_code(code)
        if sortie:
            st.code(sortie, language="text")
        if erreur:
            st.error(erreur)
        if not sortie and not erreur:
            st.caption("(aucune sortie — pensez à utiliser print())")
