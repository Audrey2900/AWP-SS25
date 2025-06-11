import streamlit as st
from components.CoronaSlider6000 import coronaslider6000
from data.char_speech_state import set_text_key
from data.ui_states import set_ui_state

def render():
    def sliderauswertung():
        set_text_key("slidercorrect")

    if st.session_state.ui_state["CoronaSliderDone"] == False:
        coronaslider6000(value=0)
        st.button("Auswertung", on_click=sliderauswertung)


    if (
        st.session_state.text_key == "slidercorrect"
        and st.session_state.text_index == 1
        and not st.session_state.ui_state["CoronaSliderDone"]
    ):
        set_ui_state("CoronaSliderDone", True)
        set_ui_state("NoCorruptionCoronaSlider", True)
        st.rerun()

    #möglicherweise nicht mehr benötigt:
    #st.success("Tatsächlich: Etwa **6.000 Menschen** wurden wegen falscher Corona-Heilmittel ins Krankenhaus eingeliefert.")
    #st.info(f"Deine Schätzung: {guess}")
    #st.progress(min(guess, 6000) / 6000)