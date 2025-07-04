import streamlit as st
import components.AiHarmChart.aiharmchart as HarmChart
import components.AiHarmExamples.aiharmexamples as HarmChartExamples
import components.Corruption.corruption as Corruption
import components.PictureSelector as PictureSelector
import components.AiSentiment.aisentiment as AiSentiment
import components.DeepfakeFinderLogic.deepfakefinderlogic as DeepfakeFinderLogic
import components.Mission_2.Mission_2 as Mission2
import components.Mission_3.Mission_3 as Mission3
import components.Mission_4.Mission_4 as Mission4
from data.char_speech_state import set_text_key

def render():
    
    st.title("Künstliche Intelligenz und Fake News - wie hängt das zusammen?")

    st.markdown("""
    Künstliche Intelligenz (KI) wird heute in vielen Bereichen eingesetzt, zum Beispiel bei automatischen Übersetzungen, Chatbots oder Bilderkennungen. Sie verarbeitet große Mengen an Daten und erkennt Muster. Genau das macht sie auch anfällig für Fehler, vor allem dann, wenn sie mit einseitigen oder falschen Informationen trainiert wurde.

    Wenn im Netz viele Falschmeldungen vorkommen, übernimmt die KI diese Inhalte, ohne sie zu hinterfragen. Sie verbreitet sie weiter, oft in scheinbar sachlicher Form. So kann KI ungewollt zur Verbreitung von Fake News beitragen, obwohl sie eigentlich neutral wirken soll.
    """)

    st.markdown('<div id="KiDiskriminierung"></div>', unsafe_allow_html=True)
    st.markdown("<div style='height: 50px;'></div>", unsafe_allow_html=True)

    st.markdown("""
    ### Warum KI nicht immer fair ist

    Künstliche Intelligenz basiert auf Daten. Wenn diese Daten Vorurteile enthalten, übernimmt die KI diese Muster und wiederholt sie. Studien zeigen, dass viele KI-Modelle Menschen unterschiedlich behandeln, je nach Aussehen, Geschlecht oder Herkunft.

    Gesichtserkennungsprogramme zum Beispiel erkennen weiße Männer deutlich besser als Schwarze Frauen. Bildgeneratoren zeigen bei Begriffen wie „Chef“ fast ausschließlich Männer. Auch in Texten werden Klischees übernommen, wenn sie häufig genug im Trainingsmaterial vorkamen.

    In einer bereinigten Grafik werden reale Beispiele gezeigt, bei denen KI diskriminierend oder einseitig gearbeitet hat. Dabei wurde das Feld „none“ entfernt, um gezielt sichtbar zu machen, wie KI Entscheidungen treffen würde, wenn sie tatsächlich nach bestimmten Mustern bevorzugt oder benachteiligt.

    """)

    HarmChart.render() 

    HarmChartExamples.render()

    st.markdown("<div style='height: 50px;'></div>", unsafe_allow_html=True)

    AiSentiment.render()

    if st.session_state.ui_state["NoCorruptionSentimentSlider"] == False:
        Corruption.render()

    if st.toggle("Quellen", key="quelleAiSentiment"):
        st.markdown("""
        <div style="border:1px solid #ccc; border-radius:6px; padding:10px; margin-top:5px;">
        <ul>
            <li><a href='https://airtable.com/appOU03dlKuBdbmty/shrEkrIYINbrcKQ3z/tbleGYjNLn2D4Xfzs' target='_blank'>Datensatz</a></li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<div style='height: 50px;'></div>", unsafe_allow_html=True)

    Mission2.render()

    if st.session_state.ui_state["NoCorruptionMission2"] == False:
        Corruption.render()

    st.markdown("<div style='height: 50px;'></div>", unsafe_allow_html=True)

    st.markdown("""
    ### Was Deepfakes gefährlich macht

    Deepfakes sind Videos oder Audiodateien, die mithilfe von KI gefälscht wurden. Personen sagen oder tun dort Dinge, die sie nie gesagt oder getan haben. Die Fälschungen sehen oft täuschend echt aus.

    Diese Technik kann gezielt eingesetzt werden, um Personen zu schädigen oder politische Botschaften zu manipulieren. Wer solche Inhalte sieht, erkennt häufig nicht auf den ersten Blick, dass es sich um Fälschungen handelt. Genau das macht Deepfakes so gefährlich im Zusammenhang mit Fake News.
    """)

    st.markdown("<div style='height: 50px;'></div>", unsafe_allow_html=True)

    DeepfakeFinderLogic.render()

    Mission3.render()

    if st.session_state.ui_state["NoCorruptionMission3"] == False:
        Corruption.render()

    st.markdown("<div style='height: 50px;'></div>", unsafe_allow_html=True)

    st.button("", on_click=set_text_key, args=("AiPictureSelector",), key="chatAiPictureSelector")
    PictureSelector.PictureSelector()
    st.button("", on_click=set_text_key, args=("AiBradolini",), key="chatBradolini")

    st.markdown("<div style='height: 50px;'></div>", unsafe_allow_html=True)

    st.markdown("""
    ### Warum Falschinformationen so schwer zu stoppen sind

    Falschinformationen verbreiten sich oft sehr schnell, vor allem in sozialen Netzwerken. Sie sind leicht formuliert, emotional und lassen sich gut weiterleiten. Richtigstellungen dagegen sind aufwendig. Es braucht Quellen, Belege und Erklärungen, die nachvollziehbar sind.

    Dieses Problem wird mit dem sogenannten Bradolinis Gesetz beschrieben:

    > Es kostet zehnmal mehr Aufwand, eine Falschinformation zu widerlegen, als sie zu produzieren.

    Deshalb ist es wichtig, Inhalte kritisch zu hinterfragen, bevor sie geteilt werden. Wer besser versteht, wie Fake News und KI funktionieren, kann gezielter damit umgehen.
    """)

    Mission4.render()

    if st.session_state.ui_state["NoCorruptionAiFakeNews"] == False:
        Corruption.render()

    st.markdown("<div style='height: 50px;'></div>", unsafe_allow_html=True)