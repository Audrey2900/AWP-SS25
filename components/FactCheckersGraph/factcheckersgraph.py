import streamlit as st
import pandas as pd

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
    df["Verifiziert am"] = df["Verified"].dt.strftime("%d.%m.%Y")
    df["Organisation"] = df["Name"]
    country_order = sorted(df["Country"].astype(str).unique().tolist())

    st.markdown("IFCN-zertifizierte Faktencheck-Organisationen weltweit")
    
    selected_country = st.selectbox(
        "Land auswählen",
        country_order,
        index=country_order.index("Germany") if "Germany" in country_order else 0
    )

    filtered = df[df["Country"] == selected_country][["Organisation", "Verifiziert am"]].sort_values("Verifiziert am")

    st.markdown("""
        <style>
            [data-testid="stElementToolbarButtonContainer"] {
                display: none !important;
            }
        </style>
    """, unsafe_allow_html=True)

    # CSS zum Ausblenden der UI-Elemente (Fullscreen, Download, Spaltenauswahl)
    st.markdown("""
        <style>
            [data-testid="stDataFrameFullscreenButton"],
            [data-testid="stDataFrameDownloadButton"],
            [data-testid="stDataFrameViewDropdown"] {
                display: none !important;
            }
        </style>
    """, unsafe_allow_html=True)

    st.dataframe(filtered, use_container_width=True, hide_index=True)
