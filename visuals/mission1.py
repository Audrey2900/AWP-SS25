import altair as alt
from matplotlib import pyplot as plt
import streamlit as st
import pandas as pd
from wordcloud import STOPWORDS, WordCloud
import plotly.express as px
import plotly.graph_objects as go

def show_country_chart(df):
    st.subheader("Fake News nach Ländern")
    
    # Ansichts-Optionen
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("🌍 Europa", key="europe_view"):
            st.session_state.globe_view = "europe"
    with col2:
        if st.button("🌎 Amerika", key="america_view"):
            st.session_state.globe_view = "america"
    with col3:
        if st.button("🌏 Asien", key="asia_view"):
            st.session_state.globe_view = "asia"
    
    # Daten vorbereiten
    country_counts = df['country'].value_counts().reset_index()
    country_counts.columns = ['Land', 'Anzahl']
    
    country_mapping = {
        'USA': 'United States',
        'UK': 'United Kingdom',
        'Brasil': 'Brazil',
    }
    country_counts['Land'] = country_counts['Land'].replace(country_mapping)
    
    # Ensure Anzahl is numeric
    country_counts['Anzahl'] = pd.to_numeric(country_counts['Anzahl'])
        
    # 3D-Weltkugel mit Farbskala je nach Anzahl
    map_fig = px.choropleth(
        country_counts,
        locations="Land",
        locationmode="country names",
        color="Anzahl",
        color_continuous_scale="Reds",
        range_color=(country_counts['Anzahl'].min(), country_counts['Anzahl'].max()),  # Uncommented to set color range
        labels={"Anzahl": "Anzahl Fake News"},
        hover_name="Land"
    )
    
    # Ansicht basierend auf Auswahl anpassen
    view = st.session_state.get("globe_view", "world")
    if view == "europe":
        rotation_lon, rotation_lat = 10, 50
    elif view == "america":
        rotation_lon, rotation_lat = -90, 20
    elif view == "asia":
        rotation_lon, rotation_lat = 100, 30
    else:
        rotation_lon, rotation_lat = 0, 0
    
    map_fig.update_geos(
        showcoastlines=True,
        projection_type="orthographic",
        showcountries=True,
        landcolor="lightgray",
        oceancolor="lightblue",
        showocean=True,
        showland=True,
        projection_rotation_lon=rotation_lon,
        projection_rotation_lat=rotation_lat
    )
    
    map_fig.update_layout(
        title="Fake News Verteilung weltweit",
        margin={"r": 0, "t": 50, "l": 0, "b": 0},
        height=250
    )
    
    st.plotly_chart(map_fig, use_container_width=True)
    
    # Optional: Zusätzliche Statistiken anzeigen
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Länder gesamt", len(country_counts))
    with col2:
        st.metric("Land mit meisten Fakes", country_counts.iloc[0]['Land'])
    with col3:
        st.metric("Höchste Anzahl", country_counts.iloc[0]['Anzahl'])

def show_monthly_chart(df):
    st.header("2. Anzahl der Fake-News pro Monat")
    df['published_date'] = pd.to_datetime(df['published_date'], errors='coerce')
    df['month'] = df['published_date'].dt.to_period('M')
    monthly_counts = df['month'].value_counts().sort_index()
    import plotly.graph_objects as go
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=monthly_counts.index.astype(str),
        y=monthly_counts.values,
        mode='lines+markers'
    ))
    fig.update_layout(
        xaxis_title="Monat",
        yaxis_title="Anzahl Fake News",
        margin=dict(l=20, r=20, t=40, b=20),
        height=350,
        dragmode=False  # Deaktiviert Ziehen/Auswählen
    )
    st.plotly_chart(
        fig,
        use_container_width=True,
        config={
            "staticPlot": False,
            "scrollZoom": False,
            "displayModeBar": False,
            "editable": False,
            "doubleClick": "reset"
        }
    )

def show_category_chart(df):
    st.header("3. Häufigste Fake-News-Kategorien (in %)")
    category_counts = df['category'].value_counts(normalize=True).mul(100).round(1)
    fig = px.bar(
        x=category_counts.index,
        y=category_counts.values,
        labels={'x': 'Kategorie', 'y': 'Prozent'},
    )
    fig.update_layout(
        margin=dict(l=20, r=20, t=40, b=20),
        height=350,
        dragmode=True  # <-- Wird alles ignoriert sobald man es animiert
    )
    st.plotly_chart(
        fig,
        use_container_width=True,
        config={
            "staticPlot": False,
            "scrollZoom": False,
            "displayModeBar": False,
            "editable": False,
            "doubleClick": "reset"
        }
    )

def show_language_chart(df):
    st.header("4. Sprachen der Artikel")
    lang_counts = df['lang'].value_counts()
    import plotly.express as px
    fig = px.bar(
        x=lang_counts.index,
        y=lang_counts.values,
        labels={'x': 'Sprache', 'y': 'Anzahl'},
    )
    fig.update_layout(
        margin=dict(l=20, r=20, t=40, b=20),
        height=350,
        dragmode=False  # Deaktiviert Ziehen/Auswählen
    )
    st.plotly_chart(
        fig,
        use_container_width=True,
        config={
            "staticPlot": False,
            "scrollZoom": False,
            "displayModeBar": False,
            "editable": False,
            "doubleClick": "reset"
        }
    )

def show_classification_chart(df):
    st.header("7. Klassifikation von Fake News")
    class_counts = df['class'].value_counts().reset_index()
    class_counts.columns = ['Klassifikation', 'Anzahl']
    import plotly.express as px
    fig = px.bar(
        class_counts,
        x='Anzahl',
        y='Klassifikation',
        orientation='h',
        text='Anzahl',
        labels={'Anzahl': 'Anzahl', 'Klassifikation': 'Klassifikation'}
    )
    fig.update_layout(
        margin=dict(l=20, r=20, t=40, b=20),
        height=360,
        dragmode=False  # Deaktiviert Ziehen/Auswählen
    )
    st.plotly_chart(
        fig,
        use_container_width=True,
        config={
            "staticPlot": False,
            "scrollZoom": False,
            "displayModeBar": False,
            "editable": False,
            "doubleClick": "reset"
        }
    )

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