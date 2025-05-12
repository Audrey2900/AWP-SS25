# streamlit run /Users/audrey/Desktop/dashboard1_2.py

import pathlib
import streamlit as st
import pandas as pd
import plotly.express as px
import networkx as nx
import matplotlib.pyplot as plt
import time
import components.CharacterTest as CharacterTest
import streamlit.components.v1 as components
import mimetypes

mimetypes.add_type("application/javascript", ".js")
mimetypes.add_type("text/css", ".css")



# Seiteneinstellungen
st.set_page_config(
    page_title="Lern-Dashboard: Fake News & Deepfakes",
    initial_sidebar_state="collapsed",
    layout="wide")

# Design-Anpassung
st.markdown(
    """
<style>
html, body, [class*="css"]  {
    background-color: #fffaf5;
    color: #333333;
    font-family: 'Segoe UI', sans-serif;
}
.stButton>button {
    background-color: #f7941d;
    color: white;
    border: none;
    border-radius: 5px;
    padding: 8px 16px;
}
.stButton>button:hover {
    background-color: #ffa733;
}
</style>
""",
    unsafe_allow_html=True,
)

# Header
st.title("Lern-Dashboard: Fake News & Deepfakes")

# Per Custom Component
CharacterTest.CharacterTest()

# Per Static File Serving
with open("components/CharacterStatic/index.html", "r", encoding="utf-8") as f:
    html_code = f.read()

components.html(html_code, height=600)

########################################## CSS ###################################################
# Function to Load CSS from the 'styles' folder
def load_css(file_path):
    with open(file_path) as f:
        st.html(f"<style>{f.read()}</style>")

# Load external CSS
css_path = pathlib.Path("static/styles/global.css")
load_css(css_path)


st.title("✨ Streamlit CSS Styling Demo")
st.subheader(
    "As of Streamlit **version 1.39**, you can now set CSS classes on elements via the `key` parameter! 🎉"
)
st.code("pip install streamlit --upgrade", language="bash")
st.divider()

# Sytled Button
st.header("Buttons")
st.button("I'm a blue button", key="custom-button")
st.button("I'm a blue button", key="custom-button2")


# Text Area with Custom Font
st.header("Styled Text Area")
st.text_area("Your thoughts:", key="custom-box")
########################################## CSS ###################################################



# Sytled Button
st.header("Buttons")
st.button("I'm a green button", key="green")
st.button("Click Me!", key="pulse")

# Text Input with Custom Font and Color
st.header("Styled Text Input")
st.text_input("Some Text:", key="styledinput")


# Text Area with Custom Font
st.header("Custom Font")
st.text_area("Some Text:", key="styledtextarea")

# Radio Buttons with Custom Styles
st.header("Radio Buttons")
st.radio("Pick a choice:", ["Choice A", "Choice B", "Choice C"], key="styledradio")

# Markdown with Custom Font and Color
st.header("Markdown")
st.markdown(
    '<p class="custom-markdown">This is <strong>bold text</strong> with a custom font and color.</p>',
    unsafe_allow_html=True,
)




# --- Kapitel: Was sind Deepfakes ---
st.header("Was sind Deepfakes")
st.write("Deepfakes sind durch KI erzeugte Medieninhalte, die täuschend echt wirken.")

# --- Kapitel: Fake News ---
st.header("Fake News")
st.write("Fake News sind absichtlich verbreitete Falschinformationen.")

# Abschnitt: Weltkarte
st.subheader("Woher kommen Fake News?")
map_data = pd.DataFrame(
    {
        "Land": [
            "United States",
            "Russia",
            "China",
            "Germany",
            "Brazil",
            "India",
            "United Kingdom",
            "France",
            "Iran",
            "Turkey",
        ],
        "Anteil (%)": [35, 20, 15, 5, 4, 6, 3, 2, 7, 3],
    }
)

map_fig = px.choropleth(
    map_data,
    locations="Land",
    locationmode="country names",
    color="Anteil (%)",
    color_continuous_scale="OrRd",
    labels={"Anteil (%)": "Anteil an Fake News (%)"},
)

# Umstellung auf eine Globus-Darstellung
map_fig.update_geos(
    showcoastlines=True,
    projection_type="orthographic",
    showcountries=True,
    landcolor="lightgray",
    oceancolor="lightblue",
    showocean=True,
)

map_fig.update_layout(
    title_text="Woher kommen Fake News?", margin={"r": 0, "t": 50, "l": 0, "b": 0}
)

st.plotly_chart(map_fig, use_container_width=True)

# Abschnitt: Simulation
st.header("Simulation: Verbreitung von Fake News")
st.write("Ein animiertes Netzwerk zeigt die zeitliche Verbreitung einer Falschmeldung.")

# Graph erstellen
G = nx.balanced_tree(r=2, h=4)
pos = nx.spring_layout(G, seed=42)
steps = list(G.nodes)

# Plot vorbereiten
canvas = st.empty()

# Animation (nur einmal durchlaufen)
for i in range(1, len(steps) + 1):
    fig, ax = plt.subplots(figsize=(8, 6))
    node_colors = ["#f7941d" if n in steps[:i] else "#dddddd" for n in G.nodes]
    nx.draw(
        G,
        pos,
        with_labels=True,
        node_color=node_colors,
        edge_color="#aaaaaa",
        node_size=300,
        font_size=8,
        ax=ax,
    )
    canvas.pyplot(fig)
    time.sleep(0.2)

# --- Kapitel: Erkennung ---
st.header("Erkennung")
st.write("So kannst du Fake News und Deepfakes erkennen...")

# --- Kapitel: Beispiele ---
st.header("Beispiele")
st.write("Hier findest du einige Beispiele für manipulierte Inhalte.")

# --- Kapitel: Kennzahlen ---
st.header("Kennzahlen")
st.write("Zahlen und Statistiken zur Entwicklung von Fake News.")

st.subheader("Entwicklung von Fake News und Deepfakes")
df = pd.DataFrame(
    {
        "Jahr": [2018, 2019, 2020, 2021, 2022, 2023],
        "Fake News Fälle": [500, 1500, 3000, 5000, 7000, 9000],
        "Deepfake Fälle": [50, 120, 400, 1200, 3000, 6000],
    }
)

metric = st.radio(
    "Welche Kennzahl möchtest du sehen?", ["Fake News Fälle", "Deepfake Fälle"]
)
chart_type = st.selectbox("Darstellung wählen:", ["Linie", "Balken"])

if chart_type == "Linie":
    fig = px.line(df, x="Jahr", y=metric, title=f"{metric} pro Jahr", markers=True)
else:
    fig = px.bar(df, x="Jahr", y=metric, title=f"{metric} pro Jahr")

st.plotly_chart(fig, use_container_width=True)

st.divider()
st.subheader("Mini-Zeitstrahl: Meilensteine von Fake News")
timeline_data = {
    "2016": "Fake News beeinflussen US-Wahlkampf stark",
    "2018": "Erste Fake News Gesetzgebung in Europa",
    "2020": "Pandemie führt zu Anstieg von Verschwörungstheorien",
    "2022": "Algorithmen zur Fake News-Erkennung werden verbessert",
}
for year, event in timeline_data.items():
    st.markdown(f"**{year}**: {event}")

# --- Kapitel: Wieso sind Fake News gefährlich ---
st.header("Wieso sind Fake News gefährlich?")
st.write("Weil sie Vertrauen zerstören und die Gesellschaft spalten können.")

# --- Kapitel: Quiz ---
st.header("Quiz: Teste dein Wissen")
score = 0

q1 = st.radio(
    "1. Was ist ein typisches Zeichen für Deepfakes?",
    ["Klare Sprache", "Merkwürdige Mimik oder Blinzeln"],
)
if q1 == "Merkwürdige Mimik oder Blinzeln":
    score += 1

q2 = st.radio(
    "2. Was sollte man tun, wenn man eine reißerische Schlagzeile liest?",
    ["Gleich teilen", "Quelle prüfen und vergleichen"],
)
if q2 == "Quelle prüfen und vergleichen":
    score += 1

q3 = st.radio(
    "3. Was bedeutet 'Fake News'?",
    ["Technischer Fehler", "Bewusst verbreitete Falschmeldung"],
)
if q3 == "Bewusst verbreitete Falschmeldung":
    score += 1

if st.button("Ergebnisse anzeigen"):
    st.success(f"Du hast {score}/3 Punkten erreicht!")
    if score == 3:
        st.markdown("**Stark! Du bist ein echter News-Checker.**")
    elif score == 2:
        st.info("Fast perfekt – ein bisschen geht noch!")
    else:
        st.warning(
            "Kein Problem – scroll nochmal durch das Dashboard und versuch's erneut."
        )

# --- Kapitel: Interaktiver Bereich ---
st.header("Interaktiver Bereich")

# st.subheader("Erkennst du den Fake?")
# col1, col2 = st.columns(2)
# with col1:
#     if st.button("Bild A auswählen"):
#         st.error("Falsch! Das ist das echte Bild.")
#     st.image("/Users/audrey/Desktop/AWP/Waschbär.png", use_container_width=True)
# with col2:
#     if st.button("Bild B auswählen"):
#         st.success("Richtig! Das ist der Deepfake.")
#     st.image("/Users/audrey/Desktop/AWP/Waschbär_DF.jpg", use_container_width=True)
# st.caption("Hinweis: Nur eins der Bilder ist gefälscht — welches wohl?")

# st.subheader("Deine eigene Fake News-Schlagzeile")
# fake_headline = st.text_area(
#     "Gib eine eigene Schlagzeile ein:", "Sensation: KI übernimmt das Parlament!"
# )
# if st.button("Feedback anzeigen"):
#     st.markdown(
#         f"Diese Schlagzeile klingt {'extrem übertrieben' if '!' in fake_headline else 'relativ harmlos'}."
#     )
