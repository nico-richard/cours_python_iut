"""
Point d'entrée de l'outil de cours.

Lancement : streamlit run app.py
"""

import streamlit as st
from views.cours import page_cours
from views.bac_a_sable import page_bac_a_sable
from views.exercices import page_exercices
from views.imprimer import page_imprimer

st.set_page_config(page_title="Python IUT - Cours", page_icon="🐍", layout="wide")

pages = [
    st.Page(page_cours, title="Cours", icon="📘", default=True),
    st.Page(page_bac_a_sable, title="Bac à sable", icon="💻"),
    st.Page(page_exercices, title="Exercices", icon="📝"),
    st.Page(page_imprimer, title="Version imprimable", icon="🖨️"),
]

navigation = st.navigation(pages, position="sidebar")
navigation.run()
