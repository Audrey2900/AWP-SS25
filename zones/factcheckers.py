import streamlit as st
from data.char_speech_state import set_text_key

def render():
    st.button("key = test", on_click=set_text_key, args=("test",))
    st.button("key = FCwerprüftde", on_click=set_text_key, args=("FCwerprüftde",))
    st.button("key = FCgadmo", on_click=set_text_key, args=("FCgadmo",))
    st.button("key = FCifcn", on_click=set_text_key, args=("FCifcn",))
    st.button("key = FCdeepfakes", on_click=set_text_key, args=("FCdeepfakes",))
    st.button("key = FCzensur", on_click=set_text_key, args=("FCzensur",))
    st.button("key = FCwann", on_click=set_text_key, args=("FCwann",))
    st.button("key = FCaufgabe", on_click=set_text_key, args=("FCaufgabe",))