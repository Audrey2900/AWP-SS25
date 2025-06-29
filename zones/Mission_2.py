import altair as alt
import streamlit as st
import pandas as pd
from data.char_speech_state import set_text_key

def render():
    col1, col2 = st.columns([3, 1])
    with col1:
        st.title("Versteckte Hinweise im Wortchaos", anchor="mission2")
 
    st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)
    st.button("", on_click=set_text_key, args=("mission2.1",), key="chat1")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Wähle Option A", key="option_a"):
            st.session_state["chosen_option"] = "A"
        st.image("static/true.png")
    with col2:
        if st.button("Wähle Option B", key="option_b"):
            st.session_state["chosen_option"] = "B"
        st.image("static/false.png")

    st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)

    if "chosen_option" in st.session_state:
        choice = st.session_state["chosen_option"]
        st.markdown(f"**Du hast Option {choice} gewählt.**")

        # Folge-Dialog abhängig von der Auswahl
        if choice == "A":
            st.button("", on_click=set_text_key, args=("mission2_resultA",), key="chat_m2_a")
        elif choice == "B":
            st.button("", on_click=set_text_key, args=("mission2_resultB",), key="chat_m2_b")

        st.markdown("---\n## Auflösung: Was verrät uns die Sprache?")
        st.button("", on_click=set_text_key, args=("mission2.3",), key="chat3")

        # Sentiment-Diagramm
        data = pd.DataFrame({
            'Sentiment': ['sehr negativ', 'negativ', 'neutral', 'positiv', 'sehr positiv'],
            'Real News': [2, 238, 20220, 947, 10],
            'Fake News': [59, 536, 21087, 1676, 90]
        })
        df_long = data.melt(id_vars='Sentiment', var_name='Kategorie', value_name='Anzahl')
        farben = alt.Scale(domain=['Fake News', 'Real News'], range=['red', 'green'])

        chart = alt.Chart(df_long).mark_bar().encode(
            x=alt.X('Sentiment:N', sort=['sehr negativ', 'negativ', 'neutral', 'positiv', 'sehr positiv'], title="Stimmung"),
            y=alt.Y('Anzahl:Q', title="Anzahl Artikel"),
            color=alt.Color('Kategorie:N', scale=farben, legend=alt.Legend(title="Kategorie")),
            tooltip=['Kategorie', 'Sentiment', 'Anzahl'],
            xOffset='Kategorie:N'
        ).properties(width=600, height=400, title="Sentiment-Analyse: Fake News vs. Real News")

        st.altair_chart(chart, use_container_width=True)

        # Wort-Vergleich
        true_words = {
            "said": 0.071557,
            "trump": 0.043959,
            "reuters": 0.033313,
            "president": 0.026105,
            "house": 0.024856,
            "state": 0.022751,
            "government": 0.022519,
            "republican": 0.020320,
            "states": 0.020239,
            "united": 0.019446
        }
        fake_words = {
            "trump": 0.078200,
            "video": 0.032984,
            "clinton": 0.027821,
            "obama": 0.027192,
            "hillary": 0.026038,
            "people": 0.024908,
            "president": 0.023596,
            "like": 0.020506,
            "said": 0.020374,
            "donald": 0.019236
        }

        df_true = pd.DataFrame(list(true_words.items()), columns=["word", "frequency"])
        df_fake = pd.DataFrame(list(fake_words.items()), columns=["word", "frequency"])

        chart_true = alt.Chart(df_true).mark_bar(color='green').encode(
            x=alt.X('frequency:Q', title='Häufigkeit'),
            y=alt.Y('word:N', sort='-x', title='Real-News-Wörter'),
            tooltip=['word', 'frequency']
        ).properties(width=300, height=400, title="Real News")

        chart_fake = alt.Chart(df_fake).mark_bar(color='red').encode(
            x=alt.X('frequency:Q', title='Häufigkeit'),
            y=alt.Y('word:N', sort='-x', title='Fake-News-Wörter'),
            tooltip=['word', 'frequency']
        ).properties(width=300, height=400, title="Fake News")

        col1, col2 = st.columns(2)
        with col1:
            st.altair_chart(chart_true, use_container_width=True)
        with col2:
            st.altair_chart(chart_fake, use_container_width=True)

        st.button("", on_click=set_text_key, args=("mission2.4",), key="chat4")

if __name__ == "__main__":
    render()