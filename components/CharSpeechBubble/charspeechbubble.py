import streamlit as st
from streamlit.components.v1 import html
import json

def render():
    from data.bubble_texts import BUBBLE_TEXTS

    show_avatar = st.checkbox("Charakter anzeigen")
    show_bubble = st.checkbox("Sprechblase anzeigen")

    if "bubble_text" not in st.session_state:
        st.session_state.bubble_text = "Standardtext der Blase"

    def update_bubble():
        st.session_state.bubble_text = st.session_state.new_text

    st.text_input(
        "Neuer Text für die Sprechblase",
        key="new_text",
        on_change=update_bubble
    )

    if "text_index" not in st.session_state:
        st.session_state.text_index = 0

    def next_text():
        if st.session_state.text_index < len(BUBBLE_TEXTS) - 1:
            st.session_state.text_index += 1

    def prev_text():
        if st.session_state.text_index > 0:
            st.session_state.text_index -= 1

    col1, col2 = st.columns(2)
    with col1:
        st.button("← Zurück", on_click=prev_text, disabled=st.session_state.text_index == 0)
    with col2:
        st.button("Weiter →", on_click=next_text, disabled=st.session_state.text_index == len(BUBBLE_TEXTS) - 1)

    bubble_text = BUBBLE_TEXTS[st.session_state.text_index]

    if show_avatar and show_bubble:
        st.markdown(f"""
        <style>
        #avatar-container {{
            position: fixed;
            bottom: 20px;
            left: 20px;
            display: flex;
            flex-direction: row;
            align-items: flex-end;
            z-index: 9999;
            gap: 10px;
        }}
        #speech-bubble {{
            background-color: #f5f5f5;
            padding: 14px 20px;
            border-radius: 8px;
            border: 2px solid #333;
            max-width: 280px;
            width: 280px;
            font-family: sans-serif;
            font-size: 15px;
            color: #222;
            box-shadow: 2px 2px 6px rgba(0,0,0,0.25);
            max-height: 150px;
            overflow-y: auto;
            overflow-x: hidden;
        }}
        #bubble-text {{
            user-select: none;
            pointer-events: none;
        }}
        #floating-avatar {{
            height: 160px;
        }}
        #eye-button {{
            width: 50px;
            height: 50px;
            background-color: #f7941d;
            color: white;
            border: none;
            border-radius: 8px;
            font-size: 24px;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow: 2px 2px 6px rgba(0,0,0,0.25);
            text-decoration: none;
        }}
        #eye-button:hover {{
            background-color: #ffa733;
        }}
        </style>

        <div id="avatar-container">
            <img id="floating-avatar" src="/app/static/PrototypeChar.png" />
            <div id="speech-bubble">
                <div id="bubble-text"></div>
            </div>
            <a href="#{st.session_state.get("current_zone", "")}" id="eye-button">👁️</a>
        </div>
        """, unsafe_allow_html=True)

        text_js = json.dumps(bubble_text)
        html(f"""
        <script>
        const text = {text_js};
        const target = parent.document.getElementById("bubble-text");
        if (target) {{
            target.innerHTML = "";
            let i = 0;
            function typeWriter() {{
                if (i < text.length) {{
                    target.innerHTML += text.charAt(i);
                    i++;
                    setTimeout(typeWriter, 40);
                }}
            }}
            typeWriter();
        }}
        </script>
        """, height=0)
