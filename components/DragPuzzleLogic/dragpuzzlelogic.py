from components.DragPuzzle import dragpuzzle
import streamlit as st
from data.char_speech_state import set_text_key
from data.ui_states import set_ui_state

def render():
    result = dragpuzzle(height=450)

    korrekte_antworten = [
        "Falschinformationen, Gerüchte und wilde Verschwörungstheorien",
        "WhatsApp, TikTok, Instagram und YouTube",
        "die Weltgesundheitsorganisation (WHO)",
        "Social-Media-Nutzer",
        "Jugendlichen zwischen 14 und 24 Jahren",
    ]

    def auswertung():
        if result == korrekte_antworten:
            set_text_key("dragpuzzlecorrect")
        else:
            set_text_key("dragpuzzlefalse")

    st.button("Antworten übertragen", on_click=auswertung)

    if (
        st.session_state.text_key == "dragpuzzlecorrect"
        and st.session_state.text_index == 2
        and not st.session_state.ui_state["DragPuzzleDone"]
    ):
        set_ui_state("DragPuzzleDone", True)
        set_ui_state("DragPuzzleDone", True)
        st.rerun()