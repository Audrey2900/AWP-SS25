import time
import streamlit as st
from data.char_speech_state import set_text_key
from data.ui_states import set_ui_state
from components.FactCheckersTimeJS import factcheckerstime
from data.zone_anchor import autojump

def render():
    st.header("Fragen: Faktenchecker", anchor="FCQuiz")

    single_choice_questions = [
        {
            "question": "1. Was ist ein zentrales Merkmal seriöser Faktencheck-Redaktionen?",
            "options": [
                "Sie veröffentlichen nur ihre eigene Meinung.",
                "Sie sind Mitglied im International Fact Checking Network (IFCN) und legen ihre Quellen offen.",
                "Sie arbeiten ausschließlich für politische Parteien.",
                "Sie prüfen keine Aussagen aus sozialen Netzwerken."
            ],
            "answer_index": 1,
            "wrong_key": "FCQuiz1falsch"
        },
        {
            "question": "2. Was ist das Ziel des GADMO-Projekts?",
            "options": [
                "Falschinformationen schneller erkennen und gemeinsam bekämpfen.",
                "Mehr Werbung für Faktenchecker machen.",
                "Nur in Österreich Falschmeldungen prüfen.",
                "Falschinformationen verbreiten."
            ],
            "answer_index": 0,
            "wrong_key": "FCQuiz2falsch"
        },
        {
            "question": "3. Was ist der Unterschied zwischen Faktencheck und Zensur?",
            "options": [
                "Faktenchecks löschen alle Beiträge im Internet.",
                "Faktenchecks verbieten politische Meinungen.",
                "Faktenchecks richten sich gegen falsche Aussagen, nicht gegen Meinungen.",
                "Faktenchecks werden nur von der Regierung durchgeführt."
            ],
            "answer_index": 2,
            "wrong_key": "FCQuiz3falsch"
        }
    ]

    checkbox_options = {
        "BR24 Faktenfuchs": True,
        "TurboFinder": False,
        "PolitiFact": False,
        "AFP Faktencheck": True,
        "FactCheck.org": False,
        "ARD Faktenfinder": True,
        "Full Fact": False,
        "ABM Faktenteam": False,
        "MedienCheck": False,
        "MDR Fact Checking Team": True
    }

    expected_order = [
        "FactCheck.org",
        "PolitiFact und Full Fact",
        "CORRECTIV"
    ]

    for idx, q in enumerate(single_choice_questions):
        st.markdown(f"**{q['question']}**")
        st.radio(
            label=f"Antwort zu Frage {idx+1}",
            options=q["options"],
            key=f"factchecker_quiz_q{idx}",
            label_visibility="collapsed"
        )
        st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)

    st.markdown("**4. Welche Faktenchecker gibt es in Deutschland?**")
    for label in checkbox_options:
        st.checkbox(label, key=f"fc_checkbox_{label}")
    st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)

    st.markdown("**5. Sortiere die Faktenchecker vom ältesten zum jüngsten**")
    st.markdown("_Tipp: Ziehe oder klicke die Karten, um die Reihenfolge zu ändern._")
    order = factcheckerstime() or []
    st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)

    def auswertung():
        for idx, q in enumerate(single_choice_questions):
            key = f"factchecker_quiz_q{idx}"
            if key not in st.session_state:
                return
            user_answer = st.session_state[key]
            if user_answer != q["options"][q["answer_index"]]:
                set_text_key(q["wrong_key"])
                return

        for label, is_correct in checkbox_options.items():
            if st.session_state.get(f"fc_checkbox_{label}", False) != is_correct:
                set_text_key("FCQuiz4falsch")
                return

        if order != expected_order:
            set_text_key("FCQuiz5falsch")
            return

        set_text_key("FCQuizAlleRichtig", "AnchorFCQuizDone")

    st.button("Antworten abgeben", on_click=auswertung)

    if (
        st.session_state.text_key == "FCQuizAlleRichtig"
        and st.session_state.text_index == 1
        and not st.session_state.ui_state["FCQuizDone"]
    ):
        autojump("AnchorFCQuizDone")
        time.sleep(1.5)
        set_ui_state("FCQuizDone", True)
        set_ui_state("NoCorruptionFaktenChecker", True)
        st.rerun()
