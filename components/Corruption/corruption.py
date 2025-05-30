import streamlit as st

def render():
    #möglicherweise die gesamte Logik für das Erscheinen des Gifs in dieser Datei betreiben
    if st.session_state.corruption == "onboarding":    #Beispielhaft mal falls state = onboarding
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
            <img src="/app/static/corruption.gif"
                style="
                    position: relative;
                    left: 50%;
                    transform: translateX(-50%);
                    width: 1700px;
                    height: auto;
                    display: block;
                " />
            """,
            height=800
        )
        st.stop()