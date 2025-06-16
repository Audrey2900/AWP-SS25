import streamlit as st
from data.bubble_texts import BUBBLE_TEXTS
from data.zone_anchor import set_zone

def init_char_speech_state():
    if "bubble_text" not in st.session_state:
        st.session_state.bubble_text = "Standardtext der Blase"
    if "text_index" not in st.session_state:
        st.session_state.text_index = 0
    if "text_key" not in st.session_state:
        st.session_state.text_key = "onboarding"  
        
def get_current_bubble_texts():
    key = st.session_state.get("text_key", "intro")
    return BUBBLE_TEXTS.get(key, ["Kein Text gefunden."])

def update_text(delta: int):
    key = st.session_state.get("text_key", "test")
    texts = BUBBLE_TEXTS.get(key, [])
    new_index = st.session_state.text_index + delta
    if 0 <= new_index < len(texts):
        st.session_state.text_index = new_index

def set_text_key(key: str, zone: str = None):
    if st.session_state.get("text_key") != key:
        st.session_state.text_key = key
    st.session_state.typewriter_refresh = st.session_state.get("typewriter_refresh", 0) + 1
    st.session_state.text_index = 0
    if zone:
        set_zone(zone)
