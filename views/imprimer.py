"""Page permettant de télécharger une version imprimable (PDF) du cours."""

import streamlit as st
from utils import liste_seances, liste_exercices
from pdf_export import generer_pdf_seance, generer_pdf_complet


def page_imprimer() -> None:
    st.sidebar.subheader("🖨️ Version imprimable")
    st.title("🖨️ Version imprimable")
    st.write(
        "Génère un PDF (cours + exercices) à partir du contenu actuel des séances, "
        "à distribuer aux étudiants ou à imprimer."
    )

    seances = liste_seances()
    exercices = liste_exercices()
    noms_seances = list(seances.keys())

    st.subheader("Par séance")
    for nom in noms_seances:
        numero = noms_seances.index(nom) + 1
        col_nom, col_bouton = st.columns([3, 1])
        col_nom.write(nom)
        cle_exercices = f"Séance {numero}"
        if col_bouton.button("Générer", key=f"gen_{numero}"):
            with st.spinner("Génération du PDF..."):
                pdf_bytes = generer_pdf_seance(
                    nom, seances[nom], exercices[cle_exercices]
                )
            st.session_state[f"pdf_{numero}"] = pdf_bytes

        if f"pdf_{numero}" in st.session_state:
            col_bouton.download_button(
                "📥 Télécharger",
                data=st.session_state[f"pdf_{numero}"],
                file_name=f"seance{numero}_python_iut.pdf",
                mime="application/pdf",
                key=f"dl_{numero}",
            )

    st.divider()
    st.subheader("Polycopié complet")
    if st.button("Générer le PDF complet (4 séances)"):
        with st.spinner("Génération du PDF complet..."):
            pdf_bytes = generer_pdf_complet(seances, exercices)
        st.session_state["pdf_complet"] = pdf_bytes

    if "pdf_complet" in st.session_state:
        st.download_button(
            "📥 Télécharger le polycopié complet",
            data=st.session_state["pdf_complet"],
            file_name="cours_python_iut_complet.pdf",
            mime="application/pdf",
        )
