import streamlit as st
import components.CoronaSliderLogic.coronasliderlogic as CoronasliderLogic
from data.char_speech_state import set_text_key

def render():

    st.markdown("### Wie viele Menschen wurden in den ersten 3 Monaten wegen gefährlicher Corona-Falschinformationen und falscher ""Heilmittel"" ins Krankenhaus eingeliefert?")    

    if st.session_state.ui_state["CoronaSliderDone"] == False:
        st.markdown("""
        **Das Problem:** Viele dieser Gerüchte waren nicht nur falsch, sondern gefährlich.  
        Manche Menschen glaubten, Desinfektionsmittel zu trinken oder heißes Wasser zu inhalieren würde gegen Corona helfen.  
        In den ersten drei Monaten der Pandemie wurden weltweit etwa <span class="corrupt">[MissingNumber]</span> Menschen wegen solcher Falschinfos ins Krankenhaus eingeliefert.
        """, unsafe_allow_html=True)    

        st.button("", on_click=set_text_key, args=("6000",), key="chatcorona6000")

    if st.session_state.ui_state["CoronaSliderDone"] == True:
        st.markdown("""
        **Das Problem:** Viele dieser Gerüchte waren nicht nur falsch, sondern gefährlich.  
        Manche Menschen glaubten, Desinfektionsmittel zu trinken oder heißes Wasser zu inhalieren würde gegen Corona helfen.  
        In den ersten drei Monaten der Pandemie wurden weltweit etwa **6.000 Menschen** wegen solcher Falschinfos ins Krankenhaus eingeliefert.
        """, unsafe_allow_html=True)

        st.button("", on_click=set_text_key, args=("coronadone",), key="chatcoronadoneslider")

    if (
        st.session_state.text_key == "6000" and st.session_state.text_index == 4
    ) or st.session_state.ui_state["CoronaSlider"]:
        st.session_state.ui_state["CoronaSlider"] = True
        CoronasliderLogic.render()