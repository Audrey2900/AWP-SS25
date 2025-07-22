import streamlit as st
import zones.onboarding as Onboarding
import zones.offboarding as Offboarding
import zones.corona as Corona
import zones.factcheckers as FactCheckers
import zones.aifakenews as AiFakeNews

def render():     

    if "active_page" not in st.session_state:
        st.session_state.active_page = "onboarding"

    page = st.session_state.active_page

    if page == "onboarding":
        Onboarding.render()

    elif page == "offboarding":
        Offboarding.render()

    elif page == "corona":
        Corona.render()

    elif page == "factcheckers":
        FactCheckers.render()

    elif page == "aifakenews":
        AiFakeNews.render()
