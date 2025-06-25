import streamlit as st
import components.AiHarmChart.aiharmchart as HarmChart
import components.AiHarmExamples.aiharmexamples as HarmChartExamples
import components.Corruption.corruption as Corruption
import components.PictureSelector as PictureSelector
import components.AiSentiment.aisentiment as AiSentiment
import components.DeepfakeFinderLogic.deepfakefinderlogic as DeepfakeFinderLogic
from data.ui_states import set_ui_state
import components.DeepfakeFinderLogic.deepfakefinderlogic as d


def render():

    #HarmChart.render() 

    #HarmChartExamples.render()

    #AiSentiment.render()

    PictureSelector.PictureSelector() #TODO Korruptionen

    #st.markdown("<div style='height: 100px;'></div>", unsafe_allow_html=True)

    #st.button("Platzhalter für Schlussaufgabe", on_click=set_ui_state, args=("NoCorruptionAiFakeNews", True))

    #if st.session_state.ui_state["NoCorruptionAiFakeNews"] == False:
        #Corruption.render()

    #DeepfakeFinderLogic.render()

# Quellen 
# https://incidentdatabase.ai/taxonomies/
# https://airtable.com/appOU03dlKuBdbmty/shrEkrIYINbrcKQ3z/tbleGYjNLn2D4Xfzs