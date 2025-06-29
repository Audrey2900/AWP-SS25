import streamlit as st

def render():
    st.markdown("<div style='height: 100px;'></div>", unsafe_allow_html=True)
    st.markdown("""
        <style>
        html, body {
            overflow-y: hidden !important;
            padding: 0 !important;
            margin: 0 !important;
        }
        .main {
            padding-bottom: 0 !important;
            margin-bottom: 0 !important;
        }
        .block-container {
            padding-bottom: 0 !important;
            margin-bottom: 0 !important;
        }
        </style>
    """, unsafe_allow_html=True)
    st.components.v1.html("""
        <img src="https://raw.githubusercontent.com/Audrey2900/AWP-SS25/main/static/corruption.gif"
            style="
                position: relative;
                left: 50%;
                transform: translateX(-50%);
                width: 850px;
                height: auto;
                display: block;
            " />
        """,
        height=550
    )
    st.stop()