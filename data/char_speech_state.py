import streamlit as st
from data.bubble_texts import BUBBLE_TEXTS

def init_char_speech_state():
    if "bubble_text" not in st.session_state:
        st.session_state.bubble_text = "Standardtext der Blase"
    if "text_index" not in st.session_state:
        st.session_state.text_index = 0

def update_bubble():
    st.session_state.bubble_text = st.session_state.new_text

def update_text(delta: int):
    new_index = st.session_state.text_index + delta
    if 0 <= new_index < len(BUBBLE_TEXTS):
        st.session_state.text_index = new_index
