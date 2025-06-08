import streamlit.components.v1 as components
import os

dragpuzzle = components.declare_component(
    "dragpuzzle",
    path=os.path.dirname(__file__)
)
