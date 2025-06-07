import streamlit as st
from components.CoronaSlider6000 import coronaslider6000

def render():
    st.markdown("### Wie viele Menschen wurden in den ersten 3 Monaten wegen gefährlicher Corona-Falschinformationen und falscher ""Heilmittel"" ins Krankenhaus eingeliefert?")

    guess = coronaslider6000(value=0)

    if st.button("Auflösung anzeigen"):
        st.success("Tatsächlich: Etwa **6.000 Menschen** wurden wegen falscher Corona-Heilmittel ins Krankenhaus eingeliefert.")
        st.info(f"Deine Schätzung: {guess}")
        st.progress(min(guess, 6000) / 6000)
