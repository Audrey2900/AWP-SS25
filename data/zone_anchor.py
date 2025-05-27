import streamlit as st

def init_zone_state():
    if "visited_zones" not in st.session_state:
        st.session_state.visited_zones = set()
    if "current_zone" not in st.session_state:
        st.session_state.current_zone = "zone1"

def set_zone(name: str):
    st.session_state.current_zone = name
    st.session_state.visited_zones.add(name)

