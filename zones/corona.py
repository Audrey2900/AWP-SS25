import streamlit as st
import components.CoronaExpanders.coronaexpanders as CoronaExpanders
import components.CoronaSliderLogic.coronasliderlogic as CoronaSliderLogic
from data.char_speech_state import set_text_key

def render():
    st.title("Corona und Fake News: Wie ein Virus die Wahrheit infizierte")
    st.markdown("""
    Als das Coronavirus im Jahr 2020 um die Welt ging, veränderte sich unser Alltag schlagartig: Schulen wurden geschlossen, der Unterricht fand online statt, Masken wurden Pflicht, und plötzlich wusste niemand mehr so genau, was eigentlich stimmt. Doch neben dem Virus selbst verbreitete sich noch etwas anderes rasend schnell: Falschinformationen, Gerüchte und wilde Verschwörungstheorien. Fake News rund um Corona waren überall. Sie kamen über WhatsApp, TikTok, Instagram und YouTube direkt aufs Handy, also mitten in unseren Alltag.

    Gerade Jugendliche sind besonders oft mit Fake News konfrontiert. Gleichzeitig fühlen sich viele unsicher, wie sie erkennen können, ob etwas wahr ist oder nicht. Fast ein Drittel der jungen Menschen in Deutschland gab an, sich nicht fit im Umgang mit Desinformation zu fühlen. Dabei ist genau das heute wichtiger denn je.

    Schon früh warnte die Weltgesundheitsorganisation (WHO) vor einer **"Infodemie"**, einer Welle an falschen Nachrichten, die sich schneller verbreitet als das Virus selbst. Und tatsächlich: Studien zeigen, dass ein Großteil der Menschen während der Pandemie mit Desinformation in Kontakt kam. In Deutschland sahen **68 %** der Social-Media-Nutzer Fake News zur Corona-Pandemie. Bei Jugendlichen zwischen 14 und 24 Jahren waren es sogar **76 %**, die mindestens einmal pro Woche auf Falschnachrichten stießen.
    """)

    st.markdown("""
    **Das Problem:** Viele dieser Gerüchte waren nicht nur falsch, sondern gefährlich.  
    Manche Menschen glaubten, Desinfektionsmittel zu trinken oder heißes Wasser zu inhalieren würde gegen Corona helfen.  
    In den ersten drei Monaten der Pandemie wurden weltweit etwa <span class="corrupt">[MissingNumber]</span> Menschen wegen solcher Falschinfos ins Krankenhaus eingeliefert.
    """, unsafe_allow_html=True)

    st.button("", on_click=set_text_key, args=("6000",), key="chatcorona6000")

    if st.session_state.text_key == "6000" and st.session_state.text_index == 4:
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

