import time
import streamlit as st
from components.CoronaSliderJS import coronasliderjs
from data.char_speech_state import set_text_key
from data.ui_states import set_ui_state
from data.zone_anchor import autojump

def render():
    def sliderauswertung():
        if value < 6000:
            if value >= 5000:
                set_text_key("sliderlowclose")
            else:
                set_text_key("sliderlow")
        elif value > 6000:
            if value <= 7000:
                set_text_key("sliderhighclose")
            else:
                set_text_key("sliderhigh")
        else:
            set_text_key("slidercorrect", "SliderDone")

    if not st.session_state.ui_state["CoronaSliderDone"]:
        st.subheader("Wie viele Menschen wurden in den ersten 3 Monaten wegen gefährlicher Corona-Falschinformationen und falscher ""Heilmittel"" ins Krankenhaus eingeliefert?",
                     anchor="CoronaSlider")
        value = coronasliderjs(value=0) or 0
        st.button("Auswertung", on_click=sliderauswertung)

    if (
        st.session_state.text_key in ["slidercorrect", "sliderlow", "sliderhigh"]
        and st.session_state.text_index == 2
        and not st.session_state.ui_state["CoronaSliderDone"]
    ):
        autojump("AnchorSliderDone")
        time.sleep(1)
        set_ui_state("CoronaSliderDone", True)
        set_ui_state("NoCorruptionCoronaSlider", True)
        st.rerun()
