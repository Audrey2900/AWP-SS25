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


