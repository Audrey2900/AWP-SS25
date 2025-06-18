import streamlit as st

from data.ui_states import set_ui_state

def render():

    # Testcode. TODO: Muss entfernt/angepasst werden durch richtiges Quiz. OHNE SESSION_STATE FÜR DEN RERUN!
    def auswertung():
        set_ui_state("SentimentSliderDone", True)
        st.session_state._trigger_rerun = True  # Marker setzen

    st.button("platzhalter", on_click=auswertung)

    # außerhalb der Callback-Funktion auswerten
    if st.session_state.get("_trigger_rerun"):
        st.session_state._trigger_rerun = False
        st.rerun()


# Sortieren/Ordnen per drag and drop
# ...