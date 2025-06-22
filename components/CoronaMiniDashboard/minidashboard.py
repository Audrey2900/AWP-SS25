import streamlit as st
import pathlib
import pandas as pd
from visuals.mission1 import (
    show_country_chart,
    show_classification_chart,
    show_wordcloud,
)
from components.chart_animation.chartanimation import show_category_chart_animated, show_classification_chart_animated

def load_css(file_path):
    with open(file_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def render():
    css_path = pathlib.Path("static/styles/mission1.css")
    load_css(css_path)

    st.title("📊 Mini-Dashboard: Fake News Visualisierung", anchor="zone1")

    @st.cache_data #Cachen der CSV, damit diese nicht jedes mal neu gezogen wird.
    def load_data():
        df = pd.read_csv("static/FakeCovid_July2020.csv")
        df['published_date'] = pd.to_datetime(df['published_date'], errors='coerce')
        df['month'] = df['published_date'].dt.to_period('M')
        return df

    df = load_data()

    col1, col2 = st.columns([1, 3], gap="small")

    with col1:
        with st.container(key="left-box"):
            if st.button("Länder"):
                st.session_state.selected = "countries"
            if st.button("Kategorien"):
                st.session_state.selected = "categories"
            if st.button("Klassifikationen"):
                st.session_state.selected = "classification"
            if st.button("Wordcloud"):
                st.session_state.selected = "wordcloud"

    with col2:
        with st.container(key="right-box"):
            selected = st.session_state.get("selected", "countries")
            if selected == "countries":
                show_country_chart(df)
            elif selected == "categories":
                show_category_chart_animated(df)
            elif selected == "classification":
                show_classification_chart_animated(df)
            elif selected == "wordcloud":
                col_wc1, col_wc2 = st.columns(2)
                with col_wc1:
                    lang_choice = st.selectbox("Sprache", ["", "Englisch", "Deutsch"], key="wc_lang")
                with col_wc2:
                    basis = st.selectbox("Worauf basiert die Wordcloud?", ["", "Inhalte", "Faktenchecker"], key="wc_basis")
                if basis and lang_choice:
                    basis_key = "source_title" if "Inhalte" in basis else "verifiedby"
                    lang_code = "en" if lang_choice == "Englisch" else "de"
                    show_wordcloud(df, basis=basis_key, lang=lang_code)



