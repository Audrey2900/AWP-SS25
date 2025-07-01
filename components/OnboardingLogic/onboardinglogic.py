import time
import streamlit as st
from data.ui_states import set_ui_state
from data.zone_anchor import autojump

def render():
    if (
            st.session_state.text_key == "onboarding4"
            and st.session_state.text_index == 0
            and not st.session_state.ui_state["OnboardingDone"]
        ):
            autojump("OnboardingAnchor")
            time.sleep(1.5)
            set_ui_state("OnboardingDone", True)
            st.rerun()