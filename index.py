# streamlit run index.py

import streamlit as st
import zones.jscsstest as JsCssTest
import zones.dashboard1 as Dashboard1

# Seiteneinstellungen
st.set_page_config(
    page_title="Lern-Dashboard: Fake News & Deepfakes",
    initial_sidebar_state="collapsed",
    layout="wide",
)

# Design-Anpassung
st.markdown(
    """
<style>
html, body, [class*="css"]  {
    background-color: #fffaf5;
    color: #333333;
    font-family: 'Segoe UI', sans-serif;
}
.stButton>button {
    background-color: #f7941d;
    color: white;
    border: none;
    border-radius: 5px;
    padding: 8px 16px;
}
.stButton>button:hover {
    background-color: #ffa733;
}
</style>
""",
    unsafe_allow_html=True,
)


import streamlit as st
from components.bubblecomp import mycomponent

value = mycomponent(my_input_value="hello there")
st.write("Received", value)


st.divider()

import streamlit as st

show_avatar = st.checkbox("Charakter anzeigen")
show_bubble = st.checkbox("Sprechblase anzeigen")

# Dynamischer Inhalt:
bubble_text = "TEST TEST TEST TEST TEST TEST" if show_bubble else ""

if show_avatar:
    st.markdown(
        f"""
    <style>
    #avatar-container {{
        position: fixed;
        bottom: 20px;
        right: 20px;
        display: flex;
        flex-direction: row;
        align-items: flex-end;
        z-index: 9999;
    }}
    #speech-bubble {{
        position: relative;
        display: {"block" if show_bubble else "none"};
        background-color: #f5f5f5;
        padding: 14px 20px;
        border-radius: 8px;
        border: 2px solid #333;
        margin-right: 40px;
        max-width: 280px;
        font-family: sans-serif;
        font-size: 15px;
        color: #222;
        box-shadow: 2px 2px 6px rgba(0,0,0,0.25);
    }}

    #speech-bubble::after {{
        content: "";
        position: absolute;
        top: 10px;
        right: -12px;
        width: 0;
        height: 0;
        border-width: 10px 0 10px 12px;
        border-style: solid;
        border-color: transparent transparent transparent #f5f5f5;
    }}

    #bubble-text {{
        user-select: none;
        pointer-events: none;
    }}
    #floating-avatar {{
        height: 160px;
    }}
    </style>

    <div id="avatar-container">
        <div id="speech-bubble">
            <div id="bubble-text">{bubble_text}</div>
        </div>
        <img id="floating-avatar" src="/app/static/PrototypeChar.png" />
    </div>
    """,
        unsafe_allow_html=True,
    )


st.divider()

# Header
st.title("Lern-Dashboard: Fake News & Deepfakes")

## Andere Dashboards:
JsCssTest.render()
Dashboard1.render()
