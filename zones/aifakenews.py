import streamlit as st
import components.AiHarmChart.aiharmchart as HarmChart
import components.PictureSelector as PictureSelector
import components.AiSentiment.aisentiment as AiSentiment

def render():

    HarmChart.render() 

    AiSentiment.render()

    PictureSelector.PictureSelector()


