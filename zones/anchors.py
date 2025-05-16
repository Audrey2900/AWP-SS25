import streamlit as st

def render(): 
    # anchors
    st.header("📌 Springziel", anchor="go-here")
    st.write("Hier soll hingesprungen werden!")

    st.divider()
    st.divider()
    st.divider()

    st.markdown('[ Springe nach oben](#go-here)', unsafe_allow_html=True)
