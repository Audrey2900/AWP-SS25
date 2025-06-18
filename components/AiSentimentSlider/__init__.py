import os
import streamlit.components.v1 as components

sentimentslider = components.declare_component(
    "sentimentslider",
    path=os.path.dirname(__file__)
)
