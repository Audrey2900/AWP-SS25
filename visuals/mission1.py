import altair as alt
from matplotlib import pyplot as plt
import streamlit as st
import pandas as pd
from wordcloud import STOPWORDS, WordCloud

def show_country_chart(df):
    st.header("1. Verteilung nach Ländern")
    country_counts = df['country'].value_counts().head(10)
    st.bar_chart(country_counts, use_container_width=True)

def show_monthly_chart(df):
    st.header("2. Anzahl der Fake-News pro Monat")
    df['published_date'] = pd.to_datetime(df['published_date'], errors='coerce')
    df['month'] = df['published_date'].dt.to_period('M')
    monthly_counts = df['month'].value_counts().sort_index()
    st.line_chart(monthly_counts, use_container_width=True)

def show_category_chart(df):
    st.header("3. Häufigste Fake-News-Kategorien (in %)")
    category_counts = df['category'].value_counts(normalize=True).mul(100).round(1)
    st.bar_chart(category_counts, use_container_width=True)

def show_language_chart(df):
    st.header("4. Sprachen der Artikel")
    lang_counts = df['lang'].value_counts()
    st.bar_chart(lang_counts, use_container_width=True)

def show_classification_chart(df):
    st.header("7. Klassifikation von Fake News")
    class_counts = df['class'].value_counts().reset_index()
    class_counts.columns = ['Klassifikation', 'Anzahl']

    chart = alt.Chart(class_counts).mark_bar().encode(
        x=alt.X('Anzahl:Q', title='Anzahl'),
        y=alt.Y('Klassifikation:N', sort='-x', title=None)
    ).properties(
        width='container',
        height=360
    )

    st.altair_chart(chart, use_container_width=True)

def show_wordcloud(df, basis, lang):
    st.header("Wordcloud")

    if basis == "source_title":
        texts = df[df['lang'] == lang]['source_title'].dropna().astype(str)
    elif basis == "verifiedby":
        texts = df[df['lang'] == lang]['verifiedby'].dropna().astype(str)
    else:
        st.warning("Ungültige Datenbasis.")
        return

    text = " ".join(texts.tolist())

    if lang == "de":
        stopwords = set(STOPWORDS).union({
            "dass", "die", "der", "und", "mit", "ist", "ein", "eine", "im", "den",
            "des", "für", "auf", "sich", "nicht", "wie", "auch", "es", "das", "zu", "von", "am"
        })
    else:
        stopwords = set(STOPWORDS)

    wordcloud = WordCloud(
        width=800,
        height=300,
        background_color='white',
        stopwords=stopwords,
        max_words=100,
        colormap='viridis'
    ).generate(text)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis("off")
    st.pyplot(fig)



## Weitere Beispiele:
# Top Faktenchecker (muss erstmals überprüft werden) (vielleicht auch mit Dropdown für Land)
# 