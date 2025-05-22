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


st.divider()

############################## Charakter + Sprechblase ##############################
from data.bubble_texts import BUBBLE_TEXTS

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

# Initialisiere den Textindex im Session State
if "text_index" not in st.session_state:
    st.session_state.text_index = 0

# Callback-Funktionen für die Buttons
def next_text():
    if st.session_state.text_index < len(BUBBLE_TEXTS) - 1:
        st.session_state.text_index += 1

def prev_text():
    if st.session_state.text_index > 0:
        st.session_state.text_index -= 1

# Anzeige des aktuellen Textes basierend auf dem Index
bubble_text = BUBBLE_TEXTS[st.session_state.text_index]

# Buttons mit Callbacks
col1, col2 = st.columns(2)
with col1:
    st.button("← Zurück", on_click=prev_text, disabled=st.session_state.text_index == 0)
with col2:
    st.button("Weiter →", on_click=next_text, disabled=st.session_state.text_index == len(BUBBLE_TEXTS) - 1)


if show_avatar:
    st.markdown(
        f"""
    <style>
    #avatar-container {{
        position: fixed;
        bottom: 20px;
        left: 20px;              
        display: flex;
        flex-direction: row-reverse;  
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
        margin-left: 40px;        
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

    #speech-bubble::after {{
        content: "";
        position: absolute;
        top: 10px;
        left: -12px;             
        width: 0;
        height: 0;
        border-width: 10px 12px 10px 0;  
        border-style: solid;
        border-color: transparent #f5f5f5 transparent transparent;  
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

############################## Timer ##############################
import components.ResetTimer.resettimer as ResetTimer

ResetTimer.render()

############################## Timer ##############################

############################## Charakter + Sprechblase ##############################

st.divider()

# Header
st.title("Lern-Dashboard: Fake News & Deepfakes")


## Andere Dashboards:

#import zones.jscsstest as JsCssTest
#import zones.dashboard1 as Dashboard1
#import zones.anchors as Anchors
#import zones.html_to_python as HtmlToPython
import zones.zone1 as Zone1

Zone1.render()

#HtmlToPython.render()

#Anchors.render()

#JsCssTest.render()

#Dashboard1.render()