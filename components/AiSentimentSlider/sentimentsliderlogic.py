import streamlit as st
import pandas as pd
from components.AiSentimentSlider import sentimentslider
from data.char_speech_state import set_text_key

@st.cache_data
def load_sentiment_counts():
    df = pd.read_csv("static/AiFakeNewsAirtable.csv")
    counts = df["target_one_sentiment"].value_counts()
    total = counts.sum()
    values = [
        int(counts.get("Positive", 0)),
        int(counts.get("Neutral", 0)),
        int(counts.get("Negative", 0)),
    ]
    percentages = [
        round(values[0] / total * 100, 1),
        round(values[1] / total * 100, 1),
        round(values[2] / total * 100, 1),
    ]
    return values, percentages

def render():
    values, percentages = load_sentiment_counts()
    sentimentslider(value=1, values=values, percentages=percentages)

    st.button("", on_click=set_text_key, args=("aisentiment",), key="chataisentiment2")
