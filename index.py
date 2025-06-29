# streamlit run index.py
import pathlib
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
div[data-testid="stMainBlockContainer"] {
    max-width: 900px;
    margin: 0 auto;
    padding-left: 1rem;
    padding-right: 1rem;
}
.element-container:has(.stMarkdown) {
    max-width: 900px;
    margin-left: auto;
    margin-right: auto;
}
[class*="st-key-quelle"] label > div:first-child {
    display: none !important;
}
[class*="st-key-quelle"] label {
    cursor: pointer !important;
}
[class*="st-key-quelle"] [data-testid="stMarkdownContainer"] {
    color: #1a73e8 !important;
}
.corrupt {
    display: inline-block;
    background: repeating-linear-gradient(
        -45deg,
        red,
        red 2px,
        black 2px,
        black 4px
    );
    background-clip: text;
    -webkit-background-clip: text;
    color: transparent;
    animation: glitch 1s infinite;
}
@keyframes glitch {
    0% { transform: translate(0); }
    20% { transform: translate(-1px, 1px); }
    40% { transform: translate(1px, -1px); }
    60% { transform: translate(-1px, -2px); }
    80% { transform: translate(1px, 2px); }
    100% { transform: translate(0); }
}
@keyframes subtle-glitch {
  0%   { transform: translate(0px, 0px); opacity: 0.9; }
  25%  { transform: translate(0.3px, -0.3px); opacity: 0.88; }
  50%  { transform: translate(-0.3px, 0.3px); opacity: 0.91; }
  75%  { transform: translate(0.2px, 0px); opacity: 0.89; }
  100% { transform: translate(0px, 0px); opacity: 0.9; }
}
.falsetext {
    color: #d67474;
    font-style: italic;
    text-decoration: underline dashed;
    text-decoration-color: #ff1a1a;
    text-underline-offset: 2px;
    opacity: 0.9;
    animation: subtle-glitch 1.6s infinite ease-in-out;
    display: inline-block;
    transition: all 0.3s ease;
}
.falsetext:hover {
    color: #ff6666;
    text-shadow: 0 0 2px rgba(255, 100, 100, 0.4);
    cursor: help;
}
</style>
""",
    unsafe_allow_html=True,
)

def load_css(file_path):
        with open(file_path) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

css_path = pathlib.Path("static/styles/global.css")
load_css(css_path)


st.divider()

############################## Charakter + Sprechblase ##############################
import components.CharSpeechBubble.charspeechbubble as CharSpeechBubble
CharSpeechBubble.render()
############################## Charakter + Sprechblase ##############################

############################## Timer ##############################
import components.ResetTimer.resettimer as ResetTimer

ResetTimer.render()
############################## Timer ##############################

############################## Init Zones ##############################
from data.zone_anchor import autojump, init_zone_state
from data.ui_states import init_ui_state

init_zone_state()
init_ui_state()
############################## Init Zones ##############################

st.divider()

# Header
st.title("Lern-Dashboard: Fake News & Deepfakes")


## Andere Dashboards:

import zones.factcheckers as FactCheckers
import zones.corona as Corona
import zones.aifakenews as AiFakeNews
import zones.onboarding as Onboarding
import zones.offboarding as Offboarding
import zones.Mission_2 as mission2
import zones.Mission_3 as Mission3
import zones.Mission_4 as Mission4

#Onboarding.render()

Corona.render()

#FactCheckers.render()

#AiFakeNews.render()

#Offboarding.render()

#mission2.render()

#Mission3.render()

#Mission4.render()

# Anchors erstellen:
#        st.markdown('<div id="SliderDone"></div>', unsafe_allow_html=True)
