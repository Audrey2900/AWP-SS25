import streamlit as st
import plotly.express as px
import pandas as pd
import streamlit.components.v1 as components

def show_category_chart_animated(df):
    st.header("3. Häufigste Fake-News-Kategorien (in %)")
    category_counts = df['category'].value_counts(normalize=True).mul(100).round(1)
    steps = 10
    data = []
    for i in range(steps + 1):
        frac = i / steps
        for cat, val in category_counts.items():
            data.append({
                "Kategorie": cat,
                "Prozent": val * frac,
                "Frame": i
            })
    anim_df = pd.DataFrame(data)

    fig = px.bar(
        anim_df,
        x="Kategorie",
        y="Prozent",
        text="Prozent",
        animation_frame="Frame",
        range_y=[0, category_counts.max() * 1.1],
        labels={'Kategorie': 'Kategorie', 'Prozent': 'Prozent'}
    )
    fig.update_layout(
        margin=dict(l=20, r=20, t=40, b=20),
        height=350,
        showlegend=False
    )
    fig.update_traces(texttemplate='%{text:.1f}', textposition='outside')

    # Automatische Animation per JavaScript
    plotly_html = fig.to_html(full_html=False, include_plotlyjs='cdn', auto_play=True)
    # auto_play=True sorgt für automatischen Start

    hide_controls_css = """
    <style>
    /* Play/Pause Button und Slider ausblenden */
    .plotly-frame-controls, .slider-container, .plotly .slider, .plotly .slider-label {display: none !important;}
    </style>
    """

    components.html(hide_controls_css + plotly_html, height=400)