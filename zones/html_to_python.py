import streamlit as st
from components.htmltopython import htmltopython

def render():
    value = htmltopython(my_input_value="hello there")
    st.write("Received", value)