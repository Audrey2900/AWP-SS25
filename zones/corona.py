import streamlit as st
import components.CoronaExpanders.coronaexpanders as CoronaExpanders
import components.CoronaSliderLogic.coronasliderlogic as CoronaSliderLogic
import components.CoronaDragPuzzle.coronadragpuzzle as CoronaDragPuzzle
from data.char_speech_state import set_text_key

def render():
    st.title("Corona und Fake News: Wie ein Virus die Wahrheit infizierte")

    CoronaDragPuzzle.render()
    st.markdown("<div style='height: 500px;'></div>", unsafe_allow_html=True) #TODO Corruption-Effekt anstatt normaler Abstand

    st.markdown("""
    **Das Problem:** Viele dieser Gerüchte waren nicht nur falsch, sondern gefährlich.  
    Manche Menschen glaubten, Desinfektionsmittel zu trinken oder heißes Wasser zu inhalieren würde gegen Corona helfen.  
    In den ersten drei Monaten der Pandemie wurden weltweit etwa <span class="corrupt">[MissingNumber]</span> Menschen wegen solcher Falschinfos ins Krankenhaus eingeliefert.
    """, unsafe_allow_html=True)

    st.button("", on_click=set_text_key, args=("6000",), key="chatcorona6000")

    if (
        st.session_state.text_key == "6000" and st.session_state.text_index == 4
    ) or st.session_state.ui_state["CoronaSlider"]:
        st.session_state.ui_state["CoronaSlider"] = True
        CoronaSliderLogic.render()




    #TODO: Lösung. Diese wird eingefügt, sobald man die Slider-Aufgabe geschafft hat
    st.markdown("<div style='height: 500px;'></div>", unsafe_allow_html=True)
    st.markdown("""
        **Das Problem:** Viele dieser Gerüchte waren nicht nur falsch, sondern gefährlich.  
        Manche Menschen glaubten, Desinfektionsmittel zu trinken oder heißes Wasser zu inhalieren würde gegen Corona helfen.  
        In den ersten drei Monaten der Pandemie wurden weltweit etwa **6.000 Menschen** wegen solcher Falschinfos ins Krankenhaus eingeliefert.
        """, unsafe_allow_html=True)


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

