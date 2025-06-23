import streamlit as st
import components.CoronaExpanders.coronaexpanders as CoronaExpanders
import components.CoronaDragPuzzle.coronadragpuzzle as CoronaDragPuzzle
import components.Corruption.corruption as Corruption
import components.CoronaSlider.coronaslider as CoronaSlider
import components.CoronaMiniDashboard.minidashboard as MiniDashboard
from data.ui_states import set_ui_state

def render():
#     st.title("Corona und Fake News: Wie ein Virus die Wahrheit infizierte")

#     # Puzzle
#     CoronaDragPuzzle.render()

#     if st.session_state.ui_state["NoCorruptionDragPuzzle"] == False:
#        Corruption.render()

#     # Slider
#     CoronaSlider.render()

#     if st.session_state.ui_state["NoCorruptionCoronaSlider"] == False:
#         Corruption.render()

#     st.markdown("""
# **800 Menschen starben**. Andere wiederum hielten das Virus für harmlos oder gar für erfunden, was dazu führte, dass sie sich nicht mehr schützten und damit sich und andere in Gefahr brachten.

# **Besonders beliebt waren Verschwörungstheorien. Die bekanntesten Verschwörungstheorien während der Coronazeit waren:**
# """)

#     CoronaExpanders.render()

    st.markdown("""
Was diese Theorien gemeinsam haben? Sie sind komplett frei erfunden. Und trotzdem glaubten Millionen Menschen daran. In den USA hielten **78 %** mindestens eine verbreitete Corona-Falschaussage für möglich oder wahr.

Aber wie konnten sich solche Falschinfos so schnell verbreiten? Die Antwort ist einfach: über Social Media und Messenger. TikTok, Instagram, YouTube, Telegram und WhatsApp sind nicht nur unsere Kommunikationskanäle, sondern auch Nachrichtenquellen. Und was sich dort gut verbreitet, ist oft das, was besonders aufregend, schockierend oder empörend ist, nicht unbedingt das, was wahr ist. Auf Telegram etwa wurden jeden Tag hunderttausende Nachrichten mit Falschbehauptungen abgerufen. YouTube-Videos wie **"Plandemic"** wurden millionenfach gesehen, bevor sie überhaupt gelöscht wurden.

Das Gefährliche daran ist, dass Fake News oft sehr überzeugend aussehen. Manche basieren auf echten Infos, die dann verdreht oder aus dem Zusammenhang gerissen wurden. Wenn ein TikTok-Video sagt, Vitamin C schützt vor Corona, klingt das vielleicht plausibel, aber es stimmt nicht.
""")
    
    st.markdown("<div style='height: 50px;'></div>", unsafe_allow_html=True)
    
    MiniDashboard.render()

    # Platzhalter für Aufgabe
    st.markdown("<div style='height: 0px;'></div>", unsafe_allow_html=True)

    st.button("Zum Quiz", on_click=set_ui_state, args=("NoCorruptionCoronaZone", True))

    if st.session_state.ui_state["NoCorruptionCoronaZone"] == False:
        Corruption.render()


    st.markdown("<div style='height: 0px;'></div>", unsafe_allow_html=True)

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

# Quellen:
#https://www.stiftungen.org/aktuelles/news-aus-stiftungen/detail/studie-zu-desinformation-von-jungen-menschen-in-der-coronakrise-4986.html
#https://www.bitkom.org/Presse/Presseinformation/Mehr-als-50-Millionen-Deutsche-nutzen-soziale-Medien
#https://www.who.int/news-room/feature-stories/detail/fighting-misinformation-in-the-time-of-covid-19-one-click-at-a-time
#https://blog.digimind.com/de/covid-die-am-weitesten-verbreiteten-fake-news-in-den-sozialen-medien-in-deutschland
#https://de.statista.com/statistik/daten/studie/1237979/umfrage/glaubwuerdigkeit-von-falschnachrichten-beim-thema-corona-pandemie
#https://pmc.ncbi.nlm.nih.gov/articles/PMC8985560
#https://www.kff.org/health-information-trust/press-release/covid-19-misinformation-is-ubiquitous-78-of-the-public-believes-or-is-unsure-about-at-least-one-false-statement-and-nearly-at-third-believe-at-least-four-of-eight-false-statements-tested