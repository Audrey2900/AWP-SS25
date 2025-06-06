import pathlib
import streamlit as st
from data.char_speech_state import set_text_key

def render():
    st.title("Corona und Fake News: Wie ein Virus die Wahrheit infizierte")
    st.markdown("""
Als das Coronavirus im Jahr 2020 um die Welt ging, veränderte sich unser Alltag schlagartig: Schulen wurden geschlossen, der Unterricht fand online statt, Masken wurden Pflicht, und plötzlich wusste niemand mehr so genau, was eigentlich stimmt. Doch neben dem Virus selbst verbreitete sich noch etwas anderes rasend schnell: Falschinformationen, Gerüchte und wilde Verschwörungstheorien. Fake News rund um Corona waren überall. Sie kamen über WhatsApp, TikTok, Instagram und YouTube direkt aufs Handy, also mitten in unseren Alltag.

Gerade Jugendliche sind besonders oft mit Fake News konfrontiert. Gleichzeitig fühlen sich viele unsicher, wie sie erkennen können, ob etwas wahr ist oder nicht. Fast ein Drittel der jungen Menschen in Deutschland gab an, sich nicht fit im Umgang mit Desinformation zu fühlen. Dabei ist genau das heute wichtiger denn je.

Schon früh warnte die Weltgesundheitsorganisation (WHO) vor einer **"Infodemie"**, einer Welle an falschen Nachrichten, die sich schneller verbreitet als das Virus selbst. Und tatsächlich: Studien zeigen, dass ein Großteil der Menschen während der Pandemie mit Desinformation in Kontakt kam. In Deutschland sahen **68 %** der Social-Media-Nutzer Fake News zur Corona-Pandemie. Bei Jugendlichen zwischen 14 und 24 Jahren waren es sogar **76 %**, die mindestens einmal pro Woche auf Falschnachrichten stießen.
""")

    st.markdown("""
**Das Problem:** Viele dieser Gerüchte waren nicht nur falsch, sondern gefährlich. Manche Menschen glaubten, Desinfektionsmittel zu trinken oder heißes Wasser zu inhalieren würde gegen Corona helfen.
""", unsafe_allow_html=True)

    # Ratespiel: Wie viele Menschen wurden wegen Fake News ins Krankenhaus eingeliefert?
    st.markdown("### Ratespiel: Wie viele Menschen wurden weltweit wegen gefährlicher Corona-Falschinformationen ins Krankenhaus eingeliefert?")
    st.markdown("Schätze die Zahl und bewege den Slider. Die Auflösung kommt danach!")
    guess = st.slider("Deine Schätzung:", min_value=0, max_value=10000, value=0, step=100)
    if st.button("Auflösung anzeigen"):
        st.success(f"Tatsächlich wurden weltweit etwa **6.000 Menschen** wegen gefährlicher Corona-Falschinformationen ins Krankenhaus eingeliefert.")
        st.info(f"Deine Schätzung: {guess}")
        st.progress(min(guess, 6000) / 6000)
        st.write(f"Das sind {abs(guess-6000)} Personen Unterschied zu deiner Schätzung.")
        st.markdown("<div style='height: 32px;'></div>", unsafe_allow_html=True)  # Großer Abstand

    else:
        st.info("Triff deine Schätzung und klicke auf 'Auflösung anzeigen', um die echte Zahl zu sehen.")

    st.markdown("""
**800 Menschen starben**. Andere wiederum hielten das Virus für harmlos oder gar für erfunden, was dazu führte, dass sie sich nicht mehr schützten und damit sich und andere in Gefahr brachten.

**Besonders beliebt waren Verschwörungstheorien. Die bekanntesten Verschwörungstheorien während der Coronazeit waren:**
""")

    # 2 Reihen à 3 Expander
    col1, col2, col3 = st.columns(3)
    with col1:
        with st.expander("5G-Mobilfunk verursacht COVID-19"):
            st.write("Platzhaltertext für Geschichte 1. Hier steht später die echte Geschichte.")
    with col2:
        with st.expander("Bill Gates plant, Mikrochips über Impfungen zu implantieren"):
            st.write("Platzhaltertext für Geschichte 2. Hier steht später die echte Geschichte.")
    with col3:
        with st.expander("COVID-19 ist nicht schlimmer als die Grippe"):
            st.write("Platzhaltertext für Geschichte 3. Hier steht später die echte Geschichte.")

    col4, col5, col6 = st.columns(3)
    with col4:
        with st.expander("Geheimplan: Corona als Schwindel oder Biowaffe"):
            st.write("Platzhaltertext für Geschichte 4. Hier steht später die echte Geschichte.")
    with col5:
        with st.expander("Vitamin C in Mega-Dosis heilt COVID-19"):
            st.write("Platzhaltertext für Geschichte 5. Hier steht später die echte Geschichte.")
    with col6:
        with st.expander("5G-Masten würden angeblich Corona auslösen"):
            st.write("Platzhaltertext für Geschichte 6. Hier steht später die echte Geschichte.")

    st.markdown("""
Was diese Theorien gemeinsam haben? Sie sind komplett frei erfunden. Und trotzdem glaubten Millionen Menschen daran. In den USA hielten **78 %** mindestens eine verbreitete Corona-Falschaussage für möglich oder wahr.

Aber wie konnten sich solche Falschinfos so schnell verbreiten? Die Antwort ist einfach: über Social Media und Messenger. TikTok, Instagram, YouTube, Telegram und WhatsApp sind nicht nur unsere Kommunikationskanäle, sondern auch Nachrichtenquellen. Und was sich dort gut verbreitet, ist oft das, was besonders aufregend, schockierend oder empörend ist, nicht unbedingt das, was wahr ist. Auf Telegram etwa wurden jeden Tag hunderttausende Nachrichten mit Falschbehauptungen abgerufen. YouTube-Videos wie **"Plandemic"** wurden millionenfach gesehen, bevor sie überhaupt gelöscht wurden.

Das Gefährliche daran ist, dass Fake News oft sehr überzeugend aussehen. Manche basieren auf echten Infos, die dann verdreht oder aus dem Zusammenhang gerissen wurden. Wenn ein TikTok-Video sagt, Vitamin C schützt vor Corona, klingt das vielleicht plausibel, aber es stimmt nicht.
""")

