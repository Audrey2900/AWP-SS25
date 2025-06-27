import streamlit as st
import components.CoronaExpanders.coronaexpanders as CoronaExpanders
import components.CoronaDragPuzzle.coronadragpuzzle as CoronaDragPuzzle
import components.Corruption.corruption as Corruption
import components.CoronaSlider.coronaslider as CoronaSlider
import components.CoronaMiniDashboard.minidashboard as MiniDashboard
import components.CoronaQuiz.coronaquiz as CoronaQuiz

from data.char_speech_state import set_text_key

def render():
    st.markdown('<div id="AnchorCoronaDragPuzzle"></div>', unsafe_allow_html=True)
    st.title("Corona und Fake News: Wie ein Virus die Wahrheit infizierte", anchor="CoronaTitle")
    # Puzzle
    CoronaDragPuzzle.render()
    st.markdown('<div id="AnchorSliderDone"></div>', unsafe_allow_html=True)

    if st.session_state.ui_state["NoCorruptionDragPuzzle"] == False:
       Corruption.render()

    # Slider
    CoronaSlider.render()

    if st.session_state.ui_state["NoCorruptionCoronaSlider"] == False:
        Corruption.render()

    st.markdown("""
**800 Menschen starben**. Andere wiederum hielten das Virus für harmlos oder gar für erfunden, was dazu führte, dass sie sich nicht mehr schützten und damit sich und andere in Gefahr brachten.

**Besonders beliebt waren Verschwörungstheorien. Die bekanntesten Verschwörungstheorien während der Coronazeit waren:**
""")

    CoronaExpanders.render()

    st.markdown("""
Was diese Theorien gemeinsam haben? Sie sind komplett frei erfunden. Und trotzdem glaubten Millionen Menschen daran. In den USA hielten **78 %** mindestens eine verbreitete Corona-Falschaussage für möglich oder wahr.

Aber wie konnten sich solche Falschinfos so schnell verbreiten? Die Antwort ist einfach: über Social Media und Messenger. TikTok, Instagram, YouTube, Telegram und WhatsApp sind nicht nur unsere Kommunikationskanäle, sondern auch Nachrichtenquellen. Und was sich dort gut verbreitet, ist oft das, was besonders aufregend, schockierend oder empörend ist, nicht unbedingt das, was wahr ist. Auf Telegram etwa wurden jeden Tag hunderttausende Nachrichten mit Falschbehauptungen abgerufen. YouTube-Videos wie **"Plandemic"** wurden millionenfach gesehen, bevor sie überhaupt gelöscht wurden.

Das Gefährliche daran ist, dass Fake News oft sehr überzeugend aussehen. Manche basieren auf echten Infos, die dann verdreht oder aus dem Zusammenhang gerissen wurden. Wenn ein TikTok-Video sagt, Vitamin C schützt vor Corona, klingt das vielleicht plausibel, aber es stimmt nicht.
""")
    
    st.markdown("<div style='height: 50px;'></div>", unsafe_allow_html=True)
    MiniDashboard.render()

    if st.toggle("Quellen", key="quelle"):
        st.markdown("""
        <div style="border:1px solid #ccc; border-radius:6px; padding:10px; margin-top:5px;">
        <ul>
            <li><a href='https://blog.digimind.com/de/covid-die-am-weitesten-verbreiteten-fake-news-in-den-sozialen-medien-in-deutschland' 
                    target='_blank'>Covid: Die am weitesten verbreiteten Fake News in den sozialen Medien in Deutschland</a></li>
            <li><a href='https://de.statista.com/statistik/daten/studie/1237979/umfrage/glaubwuerdigkeit-von-falschnachrichten-beim-thema-corona-pandemie/' 
                    target='_blank'>Glaubwürdigkeit von Falschnachrichten beim Thema Corona-Pandemie 2020</a></li>
            <li><a href='https://pmc.ncbi.nlm.nih.gov/articles/PMC8985560' 
                    target='_blank'>Die Ursachen des Glaubens an Verschwörungserzählungen und Empfehlungen für eine gelungene Risikokommunikation im Gesundheitswesen
                </a></li>
            <li><a href='https://www.kff.org/health-information-trust/press-release/covid-19-misinformation-is-ubiquitous-78-of-the-public-believes-or-is-unsure-about-at-least-one-false-statement-and-nearly-at-third-believe-at-least-four-of-eight-false-statements-tested/' 
                    target='_blank'>COVID-19 Misinformation is Ubiquitous: 78% of the Public Believes or is Unsure About At Least One False Statement
                </a></li>
            <li><a href='https://zenodo.org/records/3965871' target='_blank'>FakeCovid- A Multilingual Cross domain Fact Check Dataset for COVID-19</a></li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<div style='height: 50px;'></div>", unsafe_allow_html=True)
    st.markdown('<div id="AnchorQuizDone"></div>', unsafe_allow_html=True)
    st.button("", on_click=set_text_key, args=("CoronaQuiz", "CoronaQuiz"), key="chatcoronaquiz")

    if st.session_state.ui_state["CoronaQuizDone"] == False:
        if (
            st.session_state.text_key == "CoronaQuiz" and st.session_state.text_index == 3
        ) or st.session_state.ui_state["CoronaQuiz"]:
            st.session_state.ui_state["CoronaQuiz"] = True
            CoronaQuiz.render()

    if st.session_state.ui_state["NoCorruptionCoronaZone"] == False:
        Corruption.render()

    st.markdown("<div style='height: 50px;'></div>", unsafe_allow_html=True)