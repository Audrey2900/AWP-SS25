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
import components.CharSpeechBubble.charspeechbubble as CharSpeechBubble
CharSpeechBubble.render()
############################## Charakter + Sprechblase ##############################

############################## Timer ##############################
import components.ResetTimer.resettimer as ResetTimer

ResetTimer.render()

############################## Timer ##############################

############################## Init Zones ##############################
from data.zone_anchor import init_zone_state
import components.Sidebar.sidebar as Sidebar

init_zone_state()
Sidebar.render()
############################## Init Zones ##############################

st.divider()

# Header
st.title("Lern-Dashboard: Fake News & Deepfakes")


## Andere Dashboards:

#import zones.jscsstest as JsCssTest
#import zones.dashboard1 as Dashboard1
import zones.anchors as Anchors
#import zones.html_to_python as HtmlToPython
import zones.zone1 as Zone1

Anchors.render()

Zone1.render()

#HtmlToPython.render()

#JsCssTest.render()

#Dashboard1.render()

