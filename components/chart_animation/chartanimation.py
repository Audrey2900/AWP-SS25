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
        labels={'Kategorie': 'Kategorie', 'Prozent': 'Prozent'},
        # Dunkles Theme
        template="plotly_dark"
    )
    
    fig.update_layout(
        margin=dict(l=20, r=20, t=40, b=20),
        height=345,
        width=600,
        showlegend=False,
        dragmode=False,
    )
    fig.update_traces(texttemplate='%{text:.1f}', textposition='outside')

    config = {
        "displayModeBar": False,
        "displaylogo": False,
        "staticPlot": False,  
        "scrollZoom": False,
        "editable": False,
        "doubleClick": False,
    }

    # Automatische Animation per JavaScript
    plotly_html = fig.to_html(full_html=False, include_plotlyjs='cdn', auto_play=True, config=config)
    # auto_play=True sorgt für automatischen Start

    hide_controls_css = """
        <style>
        /* Dark theme für den Container */
        .js-plotly-plot {
            background-color: #0e1117 !important;
        }
        
        /* Animation Controls ausblenden */
        .plotly .menulayer,
        g.updatemenu-container,
        g.updatemenu-header-group,
        g.updatemenu-button,
        g.updatemenu-dropdown-button-group,
        g.slider-container {
            display: none !important;
        }
        </style>
    """

    components.html(hide_controls_css + plotly_html, height=400)

def show_classification_chart_animated(df):
    st.header("4. Klassifikation der Fake News (in %)")
    
    # Gleiche Datenverarbeitung wie in show_classification_chart
    class_counts = df['class'].value_counts(normalize=True).mul(100).round(1)
    
    steps = 10 
    data = []
    for i in range(steps + 1):
        frac = i / steps
        for cls, val in class_counts.items():
            data.append({
                "Klassifikation": cls,
                "Prozent": val * frac,
                "Frame": i
            })
    anim_df = pd.DataFrame(data)

    fig = px.bar(
        anim_df,
        x="Prozent",
        y="Klassifikation",
        text="Prozent",
        animation_frame="Frame",
        orientation='h',  
        range_x=[0, class_counts.max() * 1.1],
        labels={'Klassifikation': 'Klassifikation', 'Prozent': 'Prozent'},
        template="plotly_dark"
    )
    
    fig.update_layout(
        margin=dict(l=20, r=20, t=40, b=20),
        height=360, 
        width=600,
        showlegend=False,
        dragmode=False,
        paper_bgcolor='rgba(14, 17, 23, 1)',
        plot_bgcolor='rgba(14, 17, 23, 1)',
        font=dict(color='white'),
        transition={'duration': 150, 'easing': 'cubic-in-out'}
    )
    
    fig.update_traces(
        texttemplate='%{text:.1f}', 
        textposition='outside',
        marker_color='#f7941d'
    )
    
    # Animation Settings
    fig.layout.updatemenus[0].buttons[0].args[1]["frame"]["duration"] = 150
    fig.layout.updatemenus[0].buttons[0].args[1]["transition"]["duration"] = 100

    config = {
        "displayModeBar": False,
        "displaylogo": False,
        "staticPlot": False,  
        "scrollZoom": False,
        "editable": False,
        "doubleClick": False,
    }

    plotly_html = fig.to_html(full_html=False, include_plotlyjs='cdn', auto_play=True, config=config)

    hide_controls_css = """
        <style>
        .js-plotly-plot {
            background-color: #0e1117 !important;
        }
        
        .plotly .menulayer,
        g.updatemenu-container,
        g.updatemenu-header-group,
        g.updatemenu-button,
        g.updatemenu-dropdown-button-group,
        g.slider-container {
            display: none !important;
        }
        </style>
    """

    components.html(hide_controls_css + plotly_html, height=400)