"""Page permettant de télécharger une version imprimable (PDF) du cours."""

import re

import streamlit as st
from utils import liste_seances, liste_exercices
from pdf_export import (
    generer_pdf_complet,
    generer_pdf_exercices_seance,
    generer_pdf_seance,
)


def page_imprimer() -> None:
    st.sidebar.subheader("🖨️ Version imprimable")
    st.title("🖨️ Version imprimable")
    st.write(
        "Les PDF sont générés depuis les mêmes fichiers Markdown que le diaporama. "
        "Les compléments `:::support` y sont automatiquement intégrés."
    )

    seances = liste_seances()
    exercices = liste_exercices()
    noms_seances = list(seances.keys())

    st.subheader("Document par séance")
    nom = st.selectbox("Séance à exporter", noms_seances)
    correspondance_numero = re.match(r"Séance (\d+)", nom)
    numero = int(correspondance_numero.group(1)) if correspondance_numero else 0
    cle_exercices = f"Séance {numero}"
    chemin_exercices = exercices.get(cle_exercices)
    contenus_disponibles = ["Support de cours"]
    if chemin_exercices:
        contenus_disponibles.extend(["Fascicule de TP", "Cours + TP"])
    format_document = st.radio(
        "Contenu du document",
        contenus_disponibles,
        horizontal=True,
    )

    if st.button("Générer le document", type="primary"):
        with st.spinner("Génération du PDF..."):
            if format_document == "Fascicule de TP":
                pdf_bytes = generer_pdf_exercices_seance(
                    nom, chemin_exercices
                )
                suffixe = "tp"
            else:
                inclure_tp = format_document == "Cours + TP"
                pdf_bytes = generer_pdf_seance(
                    nom,
                    seances[nom],
                    chemin_exercices,
                    inclure_exercices=inclure_tp,
                )
                suffixe = "cours_tp" if inclure_tp else "cours"
        st.session_state["pdf_seance"] = (pdf_bytes, numero, suffixe)

    if "pdf_seance" in st.session_state:
        pdf_bytes, numero_pdf, suffixe = st.session_state["pdf_seance"]
        st.download_button(
            "📥 Télécharger le document",
            data=pdf_bytes,
            file_name=f"seance{numero_pdf}_{suffixe}.pdf",
            mime="application/pdf",
        )

    st.divider()
    st.subheader("Polycopié complet")
    inclure_tp_complet = st.checkbox("Inclure les exercices", value=True)
    if st.button("Générer le PDF complet (séance 0 + 4 séances)"):
        with st.spinner("Génération du PDF complet..."):
            pdf_bytes = generer_pdf_complet(
                seances, exercices, inclure_exercices=inclure_tp_complet
            )
        st.session_state["pdf_complet"] = pdf_bytes

    if "pdf_complet" in st.session_state:
        st.download_button(
            "📥 Télécharger le polycopié complet",
            data=st.session_state["pdf_complet"],
            file_name="cours_python_iut_complet.pdf",
            mime="application/pdf",
        )
