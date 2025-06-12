import os
import streamlit.components.v1 as components

coronasliderjs = components.declare_component(
    "coronasliderjs",
    path=os.path.dirname(__file__)
)
