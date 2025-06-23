import streamlit as st

def render():
    # --- Quiz Aufgabe ---
    st.markdown("<div style='height: 50px;'></div>", unsafe_allow_html=True)
    st.subheader("Quiz: Faktenchecker")

    factchecker_quiz = [
        {
            "question": "1. Was ist ein zentrales Merkmal seriöser Faktencheck-Redaktionen?",
            "options": [
                "Sie veröffentlichen nur ihre eigene Meinung.",
                "Sie sind Mitglied im International Fact Checking Network (IFCN) und legen ihre Quellen offen.",
                "Sie arbeiten ausschließlich für politische Parteien.",
                "Sie prüfen keine Aussagen aus sozialen Netzwerken."
            ],
            "answer": 1
        },
        {
            "question": "2. Was ist das Ziel des GADMO-Projekts?",
            "options": [
                "Falschinformationen schneller erkennen und gemeinsam bekämpfen.",
                "Mehr Werbung für Faktenchecker machen.",
                "Nur in Österreich Falschmeldungen prüfen.",
                "Falschinformationen verbreiten."
            ],
            "answer": 0
        },
        {
            "question": "3. Was ist der Unterschied zwischen Faktencheck und Zensur?",
            "options": [
                "Faktenchecks richten sich gegen falsche Aussagen, nicht gegen Meinungen.",
                "Faktenchecks verbieten politische Meinungen.",
                "Faktenchecks löschen alle Beiträge im Internet.",
                "Faktenchecks werden nur von der Regierung durchgeführt."
            ],
            "answer": 0
        }
    ]

    if "factchecker_quiz_answers" not in st.session_state:
        st.session_state.factchecker_quiz_answers = [None] * len(factchecker_quiz)
    if "factchecker_quiz_submitted" not in st.session_state:
        st.session_state.factchecker_quiz_submitted = False

    with st.form("factchecker_quiz_form"):
        for idx, q in enumerate(factchecker_quiz):
            st.markdown(f"**{q['question']}**")
            st.session_state.factchecker_quiz_answers[idx] = st.radio(
                label=f"Antwort zu Frage {idx+1}",
                options=q["options"],
                index=(q["options"].index(st.session_state.factchecker_quiz_answers[idx]) if st.session_state.factchecker_quiz_answers[idx] in q["options"] else 0),
                key=f"factchecker_quiz_q{idx}",
                label_visibility="collapsed"
            )
            st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)
        submitted = st.form_submit_button("Antworten abgeben")

    if submitted:
        st.session_state.factchecker_quiz_submitted = True

    if st.session_state.factchecker_quiz_submitted:
        st.markdown("### Auswertung")
        correct = 0
        for idx, q in enumerate(factchecker_quiz):
            user_answer = st.session_state.factchecker_quiz_answers[idx]
            correct_answer = q["options"][q["answer"]]
            if user_answer == correct_answer:
                st.success(f"Frage {idx+1}: Richtig! ✅")
                correct += 1
            else:
                st.error(f"Frage {idx+1}: Falsch ❌ (Richtig wäre: **{correct_answer}**)")
        st.info(f"Du hast {correct} von {len(factchecker_quiz)} Fragen richtig beantwortet.")

        if st.button("Quiz erneut versuchen"):
            st.session_state.factchecker_quiz_answers = [None] * len(factchecker_quiz)
            st.session_state.factchecker_quiz_submitted = False
            st.experimental_rerun()