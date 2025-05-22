import streamlit.components.v1 as components
import os

_component_func = components.declare_component(
    "PictureSelector",
    path=os.path.join(os.path.dirname(__file__), "frontend")
)

def PictureSelector(height=700):
    return _component_func(height=height)
