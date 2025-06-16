import streamlit as st
import pandas as pd
import plotly.graph_objects as go

@st.cache_data
def load_ifcn_data():
    df = pd.read_csv("static/ifcn_checker.csv", sep=";", encoding="utf-8")
    df["Verified"] = df["Verified"].str.extract(r"(\d{1,2}\.\d{1,2}\.\d{4})")[0]
    df["Verified"] = pd.to_datetime(df["Verified"], format="%d.%m.%Y", errors="coerce")
    df = df.dropna(subset=["Verified", "Country", "Name"])
    df["Country"] = df["Country"].str.replace("from ", "", regex=False).str.strip()
    return df

def render():
    df = load_ifcn_data()
    df["Verified_orig"] = df["Verified"].dt.strftime("%d.%m.%Y")
    df["dup_count"] = df.groupby(["Verified", "Country"]).cumcount()
    df["Verified_shifted"] = df["Verified"] + pd.to_timedelta(df["dup_count"] * 7, unit="d")
    df["opacity"] = 1 - df["dup_count"] * 0.3
    df["opacity"] = df["opacity"].clip(lower=0.3)
    df["Country"] = df["Country"].astype(str)

    country_order = sorted(df["Country"].unique().tolist())

    fig = go.Figure()

    for country in country_order:
        sub = df[df["Country"] == country]
        fig.add_trace(go.Scatter(
            x=sub["Verified_shifted"],
            y=sub["Country"],
            mode="markers",
            name=country,
            marker=dict(size=20, opacity=sub["opacity"]),
            text=sub["Name"],
            hovertemplate="<b>%{text}</b><br>Land: %{y}<br>Datum: %{x|%d.%m.%Y}<extra></extra>"
        ))

    fig.update_layout(
        title="IFCN-zertifizierte Faktencheck-Organisationen weltweit",
        height=max(1750, 15 * len(country_order)),
        width=1200,
        xaxis_title="Verifizierungsdatum",
        yaxis_title=None,
        margin=dict(l=20, r=20, t=30, b=0),
        showlegend=False,
        dragmode=False,
        xaxis=dict(fixedrange=True),
        yaxis=dict(
            fixedrange=True,
            categoryorder="array",
            categoryarray=country_order,
            domain=[0.05, 1.0],
        ),
    )

    st.plotly_chart(fig, use_container_width=False, config={"displayModeBar": False})
