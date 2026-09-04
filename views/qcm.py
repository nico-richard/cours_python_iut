"""Page des questionnaires de diagnostic et de révision."""

from pathlib import Path

import streamlit as st

from utils import charger_qcm, liste_qcm


def _afficher_correction(qcm: dict, reponses: list[str | None]) -> None:
    """Calcule le score et affiche une correction expliquée."""
    questions = qcm["questions"]
    questions_notees = [
        (question, reponse)
        for question, reponse in zip(questions, reponses)
        if not question.get("sondage")
    ]
    score = 0
    for question, reponse in questions_notees:
        bonne_reponse = question["choix"][question["reponse"]]
        score += reponse == bonne_reponse

    sans_reponse = sum(reponse is None for _, reponse in questions_notees)
    total_note = len(questions_notees)
    pourcentage = round(100 * score / total_note)

    if qcm.get("diagnostic"):
        st.info(
            f"Résultat indicatif : **{score}/{total_note}** ({pourcentage} %). "
            "Ce score ne compte pas dans l'évaluation."
        )
    else:
        st.success(f"Score : **{score}/{total_note}** ({pourcentage} %)")

    st.progress(score / total_note)
    if sans_reponse:
        st.warning(f"{sans_reponse} question(s) laissée(s) sans réponse.")

    st.subheader("Réponses et correction")
    for numero, (question, reponse) in enumerate(zip(questions, reponses), 1):
        if question.get("sondage"):
            with st.expander(f"ℹ️ Question {numero} — {question['question']}"):
                st.write(f"**Votre réponse :** {reponse or 'Aucune réponse'}")
                st.caption("Question de positionnement non notée.")
            continue
        bonne_reponse = question["choix"][question["reponse"]]
        correcte = reponse == bonne_reponse
        icone = "✅" if correcte else "❌"
        with st.expander(f"{icone} Question {numero} — {question['question']}"):
            if correcte:
                st.write(f"**Bonne réponse :** {bonne_reponse}")
            else:
                st.write(f"**Votre réponse :** {reponse or 'Aucune réponse'}")
                st.write(f"**Bonne réponse :** {bonne_reponse}")
            st.caption(question["explication"])


def page_qcm() -> None:
    """Affiche les cinq QCM et permet leur correction immédiate."""
    questionnaires = liste_qcm()

    st.sidebar.subheader("❓ QCM")
    nom_qcm = st.sidebar.selectbox("Questionnaire", list(questionnaires))
    qcm = charger_qcm(questionnaires[nom_qcm])
    identifiant = Path(questionnaires[nom_qcm]).stem

    st.title("❓ QCM")
    st.header(qcm["titre"])
    st.write(qcm["description"])
    nb_sondage = sum(question.get("sondage", False) for question in qcm["questions"])
    nb_notees = len(qcm["questions"]) - nb_sondage
    if nb_sondage:
        st.caption(
            f"{nb_notees} questions de connaissances et {nb_sondage} questions "
            "de positionnement non notées."
        )
    else:
        st.caption(f"{nb_notees} questions — une seule bonne réponse par question.")

    if qcm.get("diagnostic"):
        st.info(
            "Ce questionnaire sert uniquement à repérer les acquis de départ. "
            "Il n'est pas noté et ne demande aucune connaissance préalable en Python."
        )

    reponses: list[str | None] = []
    with st.form(f"formulaire_{identifiant}"):
        for numero, question in enumerate(qcm["questions"], 1):
            st.markdown(f"**{numero}. {question['question']}**")
            reponse = st.radio(
                f"Réponse à la question {numero}",
                question["choix"],
                index=None,
                key=f"{identifiant}_question_{numero}",
                label_visibility="collapsed",
            )
            reponses.append(reponse)
            if numero < len(qcm["questions"]):
                st.divider()

        corriger = st.form_submit_button("Corriger le QCM", type="primary")

    if corriger:
        _afficher_correction(qcm, reponses)
