import os
import streamlit.components.v1 as components

deepfakefinder = components.declare_component(
    "deepfakefinder",
    path=os.path.dirname(__file__)
)