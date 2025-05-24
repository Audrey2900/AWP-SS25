import streamlit as st

def set_zone(name: str):
    st.session_state.current_zone = name
