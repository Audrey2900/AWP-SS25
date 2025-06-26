import streamlit as st
from data.char_speech_state import set_text_key
from data.ui_states import set_ui_state
import components.Corruption.corruption as Corruption
from components.CoronaQuizDrag import coronaquizdrag
import time
from data.zone_anchor import autojump

def render():
    st.header("Fragen: Corona & Fake News", anchor="CoronaQuiz")

    # CSS für corrupt-Stil
    st.markdown("""
    <style>
    .corrupt {
        display: inline-block;
        background: repeating-linear-gradient(
            -45deg,
            red,
            red 2px,
            black 2px,
            black 4px
        );
        background-clip: text;
        -webkit-background-clip: text;
        color: transparent;
        animation: glitch 1s infinite;
    }
    @keyframes glitch {
        0% { transform: translate(0); }
        20% { transform: translate(-1px, 1px); }
        40% { transform: translate(1px, -1px); }
        60% { transform: translate(-1px, 0px); }
        80% { transform: translate(1px, 1px); }
        100% { transform: translate(0); }
    }
    </style>
    """, unsafe_allow_html=True)

    quiz_questions = [
        {
            "question": "1. Was war eine der bekanntesten Corona-Verschwörungstheorien?",
            "options": [
                "Die Bundesregierung setzte Corona gezielt ein, um Schulden zu tilgen.",
                "Vitamin C in Mega-Dosis schützt vor Corona.",
                "Corona gibt es nur in Europa.",
                "Alle Masken sind wirkungslos."
            ],
            "answer_index": 1,
            "wrong_key": "CoronaQuiz1falsch"
        },
        {
            "question": "2. Über welche Kanäle verbreiteten sich Falschinformationen besonders schnell?",
            "options": [
                "Gedruckte Zeitungen",
                "Soziale Medien und Messenger",
                "Radio",
                "Schulbücher"
            ],
            "answer_index": 1,
            "wrong_key": "CoronaQuiz2falsch"
        },
        {
            "question": "3. Was solltest du tun, wenn dir eine Nachricht seltsam vorkommt?",
            "options": [
                "Sofort weiterleiten.",
                "Nichts tun.",
                "Kritisch hinterfragen und die Quelle prüfen.",
                "Alles glauben, was im Internet steht."
            ],
            "answer_index": 2,
            "wrong_key": "CoronaQuiz3falsch"
        },
        {
            "question": "4. Welche Kategorie von Fake News kam laut Diagramm am häufigsten vor?",
            "options": [
                "Verschwörungstheorien",
                "Antwort der US-Regierung",
                "Memes und Fehlinformationen",
                "Wirtschaft und Industrie"
            ],
            "answer_index": 1,
            "wrong_key": "CoronaQuiz4falsch"
        },
        {
            "question": "5. Wie hoch ist ungefähr der Anteil der Fake News, die im Diagramm als 'falsch' klassifiziert wurden?",
            "options": [
                "Etwa 10 Prozent",
                "Etwa 40 Prozent",
                "Etwa 80 Prozent",
                "Etwa 100 Prozent"
            ],
            "answer_index": 2,
            "wrong_key": "CoronaQuiz5falsch"
        },
        {
            "question": "6. Welche Aussage trifft laut Diagramm NICHT auf die häufigsten Fake-News-Kategorien zu?",
            "options": [
                "Memes und Fehlinformationen sind eine der Top-Kategorien.",
                "Prognosen sind die häufigste Kategorie.",
                "Verschwörungstheorien gehören zu den häufigsten Kategorien.",
                "Unterhaltung & Medien ist eine der weniger häufigen Kategorien."
            ],
            "answer_index": 1,
            "wrong_key": "CoronaQuiz6falsch"
        }
    ]

    drag_expected_set = {
        "Geheimplan: Corona als Schwindel oder Biowaffe",
        "Vitamin C in Mega-Dosis heilt COVID-19",
        "5G-Mobilfunk verursacht COVID-19"
    }

    for idx, q in enumerate(quiz_questions):
        st.markdown(f"**{q['question']}**")
        st.radio(
            label=f"Antwort zu Frage {idx+1}",
            options=q["options"],
            key=f"corona_quiz_q{idx}",
            label_visibility="collapsed"
        )
        st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)

    # Frage 7: Drag & Drop
    st.markdown("**7. Welche Verschwörungsmythen können aus den Wordclouds entnommen werden?**")
    st.markdown("_Tipp: Ziehe oder klicke die Karten, um deine Auswahl zu treffen. Klicke zum Entfernen_")
    drag_result = coronaquizdrag() or []
    st.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)

    # Frage 8: Checkbox-Stilfrage
    st.markdown("**8. Welche Faktenchecker gibt es in Deutschland?**")

    checkbox_items = {
        "Correctiv": True,
        '<span class="corrupt">[MissingText]</span>': False,
        '<span class="corrupt">huagzifebaknl</span>': False,
        '<span class="corrupt">MrTheFunny</span>': False,
        '<span class="corrupt">HHHHHHHHHHH</span>': False,
        '<span class="corrupt">49823692</span>': False,
    }

    checkbox_selections = {}
    for i, (label_text, _) in enumerate(checkbox_items.items()):
        col1, col2, col3 = st.columns([1, 3, 10])
        with col1:
            checkbox_selections[label_text] = st.checkbox("", value=False, key=f"cb_{i}")
        with col2:
            st.markdown(
                f"<div style='margin-top: 0.6rem;'>{label_text}</div>",
                unsafe_allow_html=True
            )
        with col3:
            st.markdown("")

    def auswertung():
        for idx, q in enumerate(quiz_questions):
            key = f"corona_quiz_q{idx}"
            if key not in st.session_state:
                return
            user_answer = st.session_state[key]
            if user_answer != q["options"][q["answer_index"]]:
                set_text_key(q["wrong_key"])
                return

        if not drag_expected_set.issubset(set(drag_result)):
            set_text_key("CoronaQuiz7falsch")
            return

        # "Correctiv" ist cb_0
        if not st.session_state.get("cb_0", False):
            set_text_key("CoronaQuiz8falsch")
            return

        set_text_key("transitionFactcheckers", "AnchorQuizDone")

    st.markdown("<div style='height: 50px;'></div>", unsafe_allow_html=True)
    st.button("Antworten abgeben", on_click=auswertung)

    if (
        st.session_state.text_key == "transitionFactcheckers"
        and st.session_state.text_index == 6
        and not st.session_state.ui_state["CoronaQuizDone"]
    ):
        autojump("AnchorQuizDone")
        time.sleep(1.5)
        set_ui_state("CoronaQuizDone", True)
        set_ui_state("NoCorruptionCoronaZone", True)
        st.rerun()

    if st.session_state.ui_state["NoCorruptionCoronaZone"] == False:
        Corruption.render()
