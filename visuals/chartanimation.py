import streamlit as st
import plotly.express as px
import pandas as pd
import streamlit.components.v1 as components

def show_category_chart_animated(df):
    st.header("3. Häufigste Fake-News-Kategorien")
    category_counts = df['category'].value_counts(normalize=True).mul(100).round(1)
    steps = 20
    data = []
    for i in range(steps + 1):
        frac = i / steps
        for cat, val in category_counts.items():
            data.append({
                "Kategorie": cat,
                "Prozent": val * frac,
                "Frame": i,
                "Text": f"{val:.1f}" if i == steps else ""
            })
    anim_df = pd.DataFrame(data)

    fig = px.bar(
        anim_df,
        x="Kategorie",
        y="Prozent",
        text="Text",        
        animation_frame="Frame",
        range_y=[0, category_counts.max() * 1.1],
        labels={'Kategorie': 'Kategorie', 'Prozent': 'Prozent'},
        template="plotly_dark"
    )
    
    fig.update_layout(
        margin=dict(l=20, r=20, t=40, b=20),
        height=345,
        width=600,
        showlegend=False,
        dragmode=False,
        paper_bgcolor='rgba(14, 17, 23, 1)',
        plot_bgcolor='rgba(14, 17, 23, 1)',
        font=dict(color='white'),
    )
    fig.update_traces(texttemplate='%{text}', textposition='outside', textangle=0, marker_color='#f7941d')

    config = {
        "displayModeBar": False,
        "displaylogo": False,
        "staticPlot": False,  
        "scrollZoom": False,
        "editable": False,
        "doubleClick": False,
    }

    plotly_html = fig.to_html(full_html=False, include_plotlyjs='cdn', auto_play=False, config=config)

    plotly_html += """
    <script>
    window.addEventListener('DOMContentLoaded', function () {
        const plot = document.querySelector('.js-plotly-plot');
        if (plot && window.Plotly) {
        Plotly.animate(plot, null, {
            frame: {duration: 2, redraw: false},
            transition: {duration: 60},
            mode: 'immediate'
        });
        }
    });
    </script>
    """

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

def show_classification_chart_animated(df):
    st.header("4. Klassifikation der Fake News")
    class_counts = df['class'].value_counts(normalize=True).mul(100).round(1)
    steps = 20
    data = []
    for i in range(steps + 1):
        frac = i / steps
        for cls, val in class_counts.items():
            data.append({
                "Klassifikation": cls,
                "Prozent": val * frac,
                "Frame": i,
                "Text": f"{val:.1f}" if i == steps else ""
            })
    anim_df = pd.DataFrame(data)

    fig = px.bar(
        anim_df,
        x="Prozent",
        y="Klassifikation",
        text="Text",
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
    )
    fig.update_traces(
        texttemplate='%{text}',
        textposition='outside',
        textangle=0,
        marker_color='#f7941d'
    )

    config = {
        "displayModeBar": False,
        "displaylogo": False,
        "staticPlot": False,
        "scrollZoom": False,
        "editable": False,
        "doubleClick": False,
    }

    plotly_html = fig.to_html(full_html=False, include_plotlyjs='cdn', auto_play=False, config=config)

    plotly_html += """
    <script>
    window.addEventListener('DOMContentLoaded', function () {
        const plot = document.querySelector('.js-plotly-plot');
        if (plot && window.Plotly) {
            Plotly.animate(plot, null, {
                frame: {duration: 15, redraw: false},
                transition: {duration: 60},
                mode: 'immediate'
            });
        }
    });
    </script>
    """

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
