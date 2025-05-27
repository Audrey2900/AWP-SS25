import streamlit as st

def render():
    with st.sidebar:
        st.markdown("""
        <style>
        .menu-button {
            display: block;
            width: 100%;
            background-color: #f7941d;
            color: white !important;
            text-align: center;
            padding: 10px 16px;
            margin: 5px 0;
            border-radius: 6px;
            text-decoration: none !important;
            font-size: 16px;
            font-family: sans-serif;
        }
        .menu-button:hover {
            background-color: #ffa733;
        }
        </style>
        """, unsafe_allow_html=True)

        st.header("Navigation")

        if "anchors" in st.session_state.visited_zones:
            st.markdown(f'<a href="#anchors" class="menu-button">📌 Anchors</a>', unsafe_allow_html=True)

        if "zone1" in st.session_state.visited_zones:
            st.markdown(f'<a href="#zone1" class="menu-button">📊 Zone 1</a>', unsafe_allow_html=True)



