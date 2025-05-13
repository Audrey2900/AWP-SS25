import os
import streamlit.components.v1 as components
mycomponent = components.declare_component(
    "bubblecomp",
    path=os.path.dirname(__file__)
)