import streamlit as st
from data.bubble_texts import BUBBLE_TEXTS

def init_char_speech_state():
    if "bubble_text" not in st.session_state:
        st.session_state.bubble_text = "Standardtext der Blase"
    if "text_index" not in st.session_state:
        st.session_state.text_index = 0
    if "text_key" not in st.session_state:
        st.session_state.text_key = "test"   # TODO: Muss nach dem Testen in Onboarding gestellt werden

def get_current_bubble_texts():
    key = st.session_state.get("text_key", "intro")
    return BUBBLE_TEXTS.get(key, ["Kein Text gefunden."])

def update_text(delta: int):
    key = st.session_state.get("text_key", "test")
    texts = BUBBLE_TEXTS.get(key, [])
    new_index = st.session_state.text_index + delta
    if 0 <= new_index < len(texts):
        st.session_state.text_index = new_index

def set_text_key(key: str):
    st.session_state.text_key = key
    st.session_state.text_index = 0
