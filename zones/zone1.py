import components.CoronaMiniDashboard.minidashboard as MiniDashboard # Normale python-page
import components.PictureSelector as PictureSelector # Komponente mit __init__
import components.AiHarmChart.aiharmchart as AiHarmChart
import streamlit as st

def render():

    MiniDashboard.render()

    selection = PictureSelector.PictureSelector()
    st.write("Ausgewählt:", selection)

    st.header("AI und FakeNews - Teil")
    AiHarmChart.render()

    st.divider()
























# def render():
#     # CSV einlesen
#     df = pd.read_csv("static/FakeCovid_July2020.csv")

#     st.title("Analyse von Fake News zu COVID-19 (Juli 2020)")

#     # 1. Länderstatistik
#     st.header("1. Verteilung nach Ländern")
#     country_counts = df['country'].value_counts().head(10)
#     st.bar_chart(country_counts)

#     # 2. Veröffentlichungen über Zeit
#     st.header("2. Anzahl der Fake-News pro Monat")
#     df['published_date'] = pd.to_datetime(df['published_date'], errors='coerce')
#     df['month'] = df['published_date'].dt.to_period('M')
#     monthly_counts = df['month'].value_counts().sort_index()
#     st.line_chart(monthly_counts)

#     # 3. Kategorien
#     st.header("3. Häufigste Fake-News-Kategorien")
#     category_counts = df['category'].value_counts()
#     st.bar_chart(category_counts)

#     # 4. Sprachen
#     st.header("4. Sprachen der Artikel")
#     lang_counts = df['lang'].value_counts()
#     st.bar_chart(lang_counts)

#     # 5. Top Quellen
#     st.header("5. Häufigste Quellen (article_source)")
#     source_counts = df['article_source'].value_counts().head(10)
#     st.dataframe(source_counts)

#     # 6. Wordcloud der Inhalte
#     st.header("6. Wordcloud aus Fake-News-Inhalten")

#     if df['content_text'].dropna().empty:
#         st.warning("Kein Textinhalt vorhanden für die Wordcloud.")
#     else:
#         text = ' '.join(df['content_text'].dropna().astype(str))

#         # Wordcloud erzeugen
#         wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

#         fig, ax = plt.subplots(figsize=(12, 6))
#         ax.imshow(wordcloud, interpolation='bilinear')
#         ax.axis('off')
#         st.pyplot(fig)

