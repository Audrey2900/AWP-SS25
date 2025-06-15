import streamlit as st
from streamlit.components.v1 import html
import json
from data.char_speech_state import get_current_bubble_texts, init_char_speech_state, update_text
from data.bubble_texts import BUBBLE_TEXTS

def render():
    init_char_speech_state()

    show_avatar = st.checkbox("Charakter anzeigen + Sprechblase anzeigen")

    current_texts = get_current_bubble_texts()
    bubble_text = current_texts[st.session_state.text_index]

    col1, col2 = st.columns(2)
    with col1:
        st.button("← Zurück", on_click=update_text, args=(-1,), disabled=st.session_state.text_index == 0)
    with col2:
        st.button("Weiter →", on_click=update_text, args=(+1,), disabled=st.session_state.text_index == len(BUBBLE_TEXTS) - 1)

    if show_avatar:
        st.button("hidden_next", key="hidden_next_button", on_click=update_text, args=(+1,))

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
            position: relative;
            background-color: #f5f5f5;
            padding: 14px 20px;
            border-radius: 8px;
            border: 2px solid #333;
            max-width: 320px;
            width: 320px;
            font-family: sans-serif;
            font-size: 15px;
            color: #222;
            box-shadow: 2px 2px 6px rgba(0,0,0,0.25);
            max-height: 150px;
            overflow: hidden;
        }}
        #bubble-text {{
            max-height: 125px;
            overflow-y: auto;
            margin-right: 50px;     
            width: calc(100% - 30px);            
            scrollbar-width: thin;
            scrollbar-color: #bbb transparent;
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
        #js-next-button {{
            position: absolute;
            bottom: 3px; 
            right: 6px;
            width: 44px;
            height: 44px;
            background-color: #f5f5f5;
            border: none;
            border-radius: 8px;
            font-size: 26px;  
            font-weight: bold;
            text-decoration: none;
            color: #666;
            cursor: pointer;
            z-index: 10;
            display: flex;
            align-items: center;
            justify-content: center;
            pointer-events: auto;
        }}
        #js-next-button:hover {{
            background-color: #e6e6e6;
        }}
        .st-key-hidden_next_button {{
            opacity: 0;
            pointer-events: none;
            position: fixed;
            top: 0;
            left: 0;
            z-index: -1
        }}

        @keyframes blink {{
        0%   {{ opacity: 1; }}
        50%  {{ opacity: 0.5; }}
        100% {{ opacity: 1; }}
        }}

        .blinking {{
        animation: blink 1.2s infinite;
        }}
        </style>

        <div id="avatar-container">
            <img id="floating-avatar" src="/app/static/PrototypeChar2.gif" />
            <div id="speech-bubble">
                <div id="bubble-text"></div>
                <a id="js-next-button" href="#">➤</a>
            </div>
            <a href="#{st.session_state.get("current_zone", "")}" id="eye-button">👁️</a>
        </div>
        """, unsafe_allow_html=True)
        

        html(f"""
        <script id="typewriter-{st.session_state.get("typewriter_refresh", 0)}">
        const text = {json.dumps(bubble_text)};
        const target = parent.document.getElementById("bubble-text");
        const trigger = parent.document.getElementById("js-next-button");
        const hiddenbutton = parent.document.querySelector('.st-key-hidden_next_button button');
        const avatar = parent.document.getElementById("floating-avatar");

        const maxIndex = {len(current_texts) - 1};
        const currentIndex = {st.session_state.text_index};

        if (trigger) {{
            trigger.style.display = "none";
        }}

        // Start GIF Animation
        if (avatar) {{
            avatar.src = "/app/static/PrototypeChar2.gif"; // Start Animation
        }}

        // Typewriter-Effekt
        if (target) {{
            target.innerHTML = "";
            let i = 0;
            function typeWriter() {{
                if (i < text.length) {{
                    let delay = 40;
                    const char = text.charAt(i);
                    if (char === "." || char === "?" || char === "!") {{
                        delay = 600;
                    }}
                    target.innerHTML += char;
                    target.scrollTop = target.scrollHeight;
                    i++;
                    setTimeout(typeWriter, delay);
                }} else {{
                    if (trigger && currentIndex < maxIndex) {{
                        trigger.style.display = "flex";
                        trigger.classList.add("blinking");
                    }}
                    // Pause/Stop GIF Animation
                    if (avatar) {{
                        avatar.src = "/app/static/PrototypeChar_still.png"; // Replace with static image
                    }}
                }}
            }}
            typeWriter();
        }}

        setTimeout(() => {{
            if (trigger && currentIndex < maxIndex) {{
                const style = window.getComputedStyle(trigger);
                if (style.display === "none") {{
                    trigger.style.display = "flex";
                    trigger.classList.add("blinking");
                }}
            }}
        }}, 10000);

        // Klick-Handler
        if (trigger && hiddenbutton) {{
            trigger.addEventListener("pointerup", (e) => {{
                e.preventDefault();
                hiddenbutton.click();
            }}, {{ passive: false }});

        }}
        </script>
        """, height=0)