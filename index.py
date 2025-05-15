# streamlit run index.py

import streamlit as st

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
bubble_text = st.session_state.bubble_text if show_bubble else ""
if "bubble_text" not in st.session_state:
    st.session_state.bubble_text = "Standardtext der Blase"

# fix, damit man nicht 2 mal klicken muss
def update_bubble():
    st.session_state.bubble_text = st.session_state.new_text

st.text_input(
    "Neuer Text für die Sprechblase",
    key="new_text",
    on_change=update_bubble
)


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
        max-width: 280px;         /* Maximale Breite bleibt gleich */
        width: 280px;             /* Feste Breite */
        font-family: sans-serif;
        font-size: 15px;
        color: #222;
        box-shadow: 2px 2px 6px rgba(0,0,0,0.25);
        max-height: 150px;        /* Maximale Höhe */
        overflow-y: auto;         /* Nur vertikal scrollen */
        overflow-x: hidden;       /* Kein horizontaler Scrollbalken */
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


# anchors
st.header("📌 Springziel", anchor="go-here")
st.write("Hier soll hingesprungen werden!")


## Andere Dashboards:
import zones.jscsstest as JsCssTest
import zones.dashboard1 as Dashboard1
JsCssTest.render()
st.markdown('[ Springe nach oben](#go-here)', unsafe_allow_html=True)
Dashboard1.render()
