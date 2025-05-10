import streamlit.components.v1 as components
import os

_component_func = components.declare_component(
    "CharacterTest",
    path=os.path.join(os.path.dirname(__file__), "frontend")
)

def CharacterTest(height=150):
    return _component_func(height=height)
