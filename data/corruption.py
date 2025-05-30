import streamlit as st

def init_corruption_state():
    if "corruption" not in st.session_state:
        st.session_state.corruption = "0"

def update_corruption(name: str):
    st.session_state.corruption = name
