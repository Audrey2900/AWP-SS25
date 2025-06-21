import streamlit as st
import components.AiHarmChart.aiharmchart as HarmChart
import components.AiHarmExamples.aiharmexamples as HarmChartExamples
import components.PictureSelector as PictureSelector
import components.AiSentiment.aisentiment as AiSentiment

def render():

    HarmChart.render() 

    HarmChartExamples.render()

    AiSentiment.render()

    PictureSelector.PictureSelector() #TODO Korruptionen


# Quellen 
# https://incidentdatabase.ai/taxonomies/
# https://airtable.com/appOU03dlKuBdbmty/shrEkrIYINbrcKQ3z/tbleGYjNLn2D4Xfzs
