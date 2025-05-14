# streamlit run /Users/audrey/Desktop/dashboard1_2.py

import pathlib
import streamlit as st
import components.CharacterTest as CharacterTest
import streamlit.components.v1 as components
import mimetypes


def render():

    mimetypes.add_type("application/javascript", ".js")
    mimetypes.add_type("text/css", ".css")

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

    st.divider()

    # Sytled Button
    st.header("Buttons")
    st.button("I'm a blue button", key="custom-button")
    st.button("I'm a blue button", key="custom-button2")

    # Text Area with Custom Font
    st.header("Styled Text Area")
    st.text_area("Your thoughts:", key="custom-box")

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
        '<p class="custom-markdown">TEST TEST <strong>TEST TEST</strong> TEST TEST TEST</p>',
        unsafe_allow_html=True,
    )

    ########################################## CSS ###################################################

    st.divider()

    st.header("Verändere zweite Bubble")

    # fix, damit man nicht 2 mal klicken muss
    def update_bubble():
        st.session_state.bubble_text = st.session_state.new_text_jscsstest

    st.text_input(
        "Neuer Text für die Sprechblase",
        key="new_text_jscsstest",
        on_change=update_bubble,
    )

    st.divider()
    st.divider()
    st.divider()
    st.divider()
    st.divider()
    st.divider()
    st.divider()
    st.divider()
    st.divider()
    st.divider()
    st.divider()
    st.divider()
    st.divider()
    st.divider()
