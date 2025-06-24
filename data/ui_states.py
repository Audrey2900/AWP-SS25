import streamlit as st

# Simplere Variante. 
_UI_KEYS = [
    "OnboardingDone",
    "DragPuzzle",
    "DragPuzzleDone",
    "CoronaSlider",
    "CoronaSliderDone",
    "SentimentSlider",
    "SentimentSliderDone",
    "CoronaQuiz",
    "CoronaQuizDone",
    "FCQuiz",
    "FCQuizDone",

    



    # Corruptions:
    "NoCorruptionDragPuzzle",
    "NoCorruptionCoronaSlider",
    "NoCorruptionCoronaZone",
    "NoCorruptionFaktenChecker",
    "NoCorruptionAiFakeNews",
]

def init_ui_state():
    if "ui_state" not in st.session_state:
        st.session_state.ui_state = {key: False for key in _UI_KEYS}

def set_ui_state(key: str, value: bool):
    st.session_state.ui_state[key] = value


# komplexere Variante. Könnte in Zukunft nützlich sein. 

# _UI_KEYS = [
#     "corona_slider",
# ]

# def init_ui_state():
#     if "ui_state" not in st.session_state:
#         st.session_state.ui_state = {
#             key: {"visible": False, "locked": False}
#             for key in _UI_KEYS
#         }

# Nutzung:  Man kann Die UI-Komponenten locken, bzw. nicht mehr anzeigen lassen, falls locked auf true gesetzt wird.
# Damit können wir verhindern, dass die gelösten Komponenten nach Benutzung wieder erscheinen.
# if (
#     st.session_state.text_key == "6000"
#     and st.session_state.text_index == 4
#     and not st.session_state.ui_state["corona_slider"]["locked"]
# ):
#     st.session_state.ui_state["corona_slider"]["visible"] = True
#     st.session_state.ui_state["corona_slider"]["locked"] = True

# # anzeigen
# if st.session_state.ui_state["corona_slider"]["visible"]:
#     CoronaSliderLogic.render()
