import streamlit as st
import components.AiSentimentSlider.sentimentsliderlogic as AiSentimentSlider
import components.AiSentimentQuestions.aisentimentquestions as AiSentimentQuestions
from data.char_speech_state import set_text_key

def render():
    st.markdown("""
    ## Welche Wirkung Fake News anstreben
    """)

    if st.session_state.ui_state["SentimentSlider"] == False:
        st.button("", on_click=set_text_key, args=("manipulationsentiment",), key="chataisentiment1")

    if (
        st.session_state.text_key == "manipulationsentiment" and st.session_state.text_index == 4
    ) or st.session_state.ui_state["SentimentSlider"] == True:
        st.session_state.ui_state["SentimentSlider"] = True
        AiSentimentSlider.render()

    if st.session_state.ui_state["SentimentSlider"] == True and st.session_state.ui_state["SentimentSliderDone"] == False:
        AiSentimentQuestions.render()

    if st.session_state.ui_state["SentimentSliderDone"] == True:
        st.markdown("""

        Wenn man an Fake News denkt, stellt man sich oft sofort gezielte Angstmache, Hetze oder Verschwörungen vor. Und tatsächlich: Ein großer Teil der Falschmeldungen zielt darauf ab, negative Emotionen auszulösen. Sie sollen verunsichern, provozieren oder Empörung schüren. Denn was uns aufregt, teilen wir schneller. Gerade in sozialen Medien funktionieren Wut und Angst wie ein Brandbeschleuniger für Reichweite.

        Doch das ist nur eine Seite. Fake News werden nicht nur benutzt, um zu spalten oder zu attackieren. Sie dienen auch dazu, Zustimmung zu erzeugen. Manche Meldungen sollen ein Thema bewusst übertrieben positiv darstellen oder eine Person besonders glänzend dastehen lassen. In solchen Fällen geht es nicht um Zerstörung, sondern um Selbstdarstellung oder Stimmungsmache. Auch das ist Manipulation, nur freundlicher verpackt.

        Spannend ist aber vor allem der Blick auf die Falschmeldungen mit neutralem Tonfall. In der Auswertung von über 1200 FakenNews Daten hatten viele Beiträge weder eine klar negative noch eine auffällig positive Sprache. Das überrascht, denn neutrale Aussagen wirken auf den ersten Blick harmlos oder sachlich. Und genau darin liegt die Gefahr. Solche Meldungen vermitteln oft den Eindruck von Objektivität, obwohl sie gezielt verzerren oder wichtige Fakten weglassen. Sie sind leise, aber nicht weniger wirkungsvoll. Wer keine starke Emotion verspürt, hinterfragt meist auch weniger.
        """)
