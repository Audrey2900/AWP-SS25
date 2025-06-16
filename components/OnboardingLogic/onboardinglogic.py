import streamlit as st
from data.ui_states import set_ui_state

def render():
    if (
            st.session_state.text_key == "onboarding4"
            and st.session_state.text_index == 0
            and not st.session_state.ui_state["OnboardingDone"]
        ):
            set_ui_state("OnboardingDone", True)
            st.rerun()

    #TODO: Später das hier benutzen, um die späteren Teile der Website nach dem Onboarding zu zeigen
    # Momentan ist es so, dass sofort alles angezeigt wird. 