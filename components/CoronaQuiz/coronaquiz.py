import streamlit as st
import components.Corruption.corruption as Corruption

def render():

    # --- Quiz Aufgabe ---
    st.subheader("Quiz: Fake News & Corona")
    quiz_questions = [
        {
            "question": "1. Was war eine der bekanntesten Corona-Verschwörungstheorien?",
            "options": [
                "Das Virus wurde absichtlich in einem Labor gezüchtet.",
                "Vitamin C schützt sicher vor Corona.",
                "Corona gibt es nur in Europa.",
                "Alle Masken sind wirkungslos."
            ],
            "answer": 0
        },
        {
            "question": "2. Über welche Kanäle verbreiteten sich Falschinformationen besonders schnell?",
            "options": [
                "Gedruckte Zeitungen",
                "Soziale Medien und Messenger",
                "Radio",
                "Schulbücher"
            ],
            "answer": 1
        },
        {
            "question": "3. Was ist ein typisches Merkmal von Fake News?",
            "options": [
                "Sie sind immer schwer zu verstehen.",
                "Sie wirken oft sehr überzeugend und emotional.",
                "Sie enthalten viele wissenschaftliche Quellen.",
                "Sie werden nur von offiziellen Stellen verbreitet."
            ],
            "answer": 1
        },
        {
            "question": "4. Was solltest du tun, wenn dir eine Nachricht seltsam vorkommt?",
            "options": [
                "Sofort weiterleiten.",
                "Nichts tun.",
                "Kritisch hinterfragen und die Quelle prüfen.",
                "Alles glauben, was im Internet steht."
            ],
            "answer": 2
        },
        {
            "question": "5. Welche Kategorie von Fake News kam laut Diagramm am häufigsten vor?",
            "options": [
                "Verschwörungstheorien",
                "Antwort der US-Regierung",
                "Memes und Fehlinformationen",
                "Wirtschaft und Industrie"
            ],
            "answer": 1  
        },
        {
            "question": "6. Wie hoch ist ungefähr der Anteil der Fake News, die im Diagramm als 'falsch' klassifiziert wurden?",
            "options": [
                "Etwa 10 Prozent",
                "Etwa 40 Prozent",
                "Etwa 80 Prozent",
                "Etwa 100 Prozent"
            ],
            "answer": 2  
        },
        {
            "question": "7. Welche Aussage trifft laut Diagramm NICHT auf die häufigsten Fake-News-Kategorien zu?",
            "options": [
                "Memes und Fehlinformationen sind eine der Top-Kategorien.",
                "Prognosen sind die häufigste Kategorie.",
                "Verschwörungstheorien gehören zu den häufigsten Kategorien.",
                "Unterhaltung & Medien ist eine der weniger häufigen Kategorien."
            ],
            "answer": 1  
        }
    ]

    if "corona_quiz_answers" not in st.session_state:
        st.session_state.corona_quiz_answers = [None] * len(quiz_questions)
    if "corona_quiz_submitted" not in st.session_state:
        st.session_state.corona_quiz_submitted = False

    with st.form("corona_quiz_form"):
        for idx, q in enumerate(quiz_questions):
            st.markdown(f"**{q['question']}**")
            st.session_state.corona_quiz_answers[idx] = st.radio(
                label=f"Antwort zu Frage {idx+1}",
                options=q["options"],
                index=(q["options"].index(st.session_state.corona_quiz_answers[idx]) if st.session_state.corona_quiz_answers[idx] in q["options"] else 0),
                key=f"corona_quiz_q{idx}",
                label_visibility="collapsed"
            )
            st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)
        submitted = st.form_submit_button("Antworten abgeben")

    if submitted:
        st.session_state.corona_quiz_submitted = True

    if st.session_state.corona_quiz_submitted:
        st.markdown("### Auswertung")
        correct = 0
        for idx, q in enumerate(quiz_questions):
            user_answer = st.session_state.corona_quiz_answers[idx]
            correct_answer = q["options"][q["answer"]]
            if user_answer == correct_answer:
                st.success(f"Frage {idx+1}: Richtig!")
                correct += 1
            else:
                st.error(f"Frage {idx+1}: Falsch (Richtig wäre: **{correct_answer}**)")
        st.info(f"Du hast {correct} von {len(quiz_questions)} Fragen richtig beantwortet.")

        if st.button("Quiz erneut versuchen"):
            st.session_state.corona_quiz_answers = [None] * len(quiz_questions)
            st.session_state.corona_quiz_submitted = False
            st.experimental_rerun()

    if st.session_state.ui_state["NoCorruptionCoronaZone"] == False:
        Corruption.render()