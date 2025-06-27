import streamlit as st
import components.CoronaSliderLogic.coronasliderlogic as CoronasliderLogic
from data.char_speech_state import set_text_key

def render():

    if st.session_state.ui_state["CoronaSliderDone"] == False:
        st.markdown("""
        **Das Problem:** Viele dieser Gerüchte waren nicht nur falsch, sondern gefährlich.  
        Manche Menschen glaubten, Desinfektionsmittel zu trinken oder heißes Wasser zu inhalieren würde gegen Corona helfen.  
        In den ersten drei Monaten der Pandemie wurden weltweit etwa <span class="corrupt">[MissingNumber]</span> Menschen wegen solcher Falschinfos ins Krankenhaus eingeliefert.
        """, unsafe_allow_html=True)    

        st.button("", on_click=set_text_key, args=("6000", "CoronaSlider"), key="chatcorona6000")

    if st.session_state.ui_state["CoronaSliderDone"] == True:
        st.markdown("""
        **Das Problem:** Viele dieser Gerüchte waren nicht nur falsch, sondern gefährlich.  
        Manche Menschen glaubten, Desinfektionsmittel zu trinken oder heißes Wasser zu inhalieren würde gegen Corona helfen.  
        In den ersten drei Monaten der Pandemie wurden weltweit etwa **6.000 Menschen** wegen solcher Falschinfos ins Krankenhaus eingeliefert.
        """, unsafe_allow_html=True)

        if st.toggle("Quellen", key="quelleCoronaSlider"):
            st.markdown("""
            <div style="border:1px solid #ccc; border-radius:6px; padding:10px; margin-top:5px;">
            <ul>
                <li><a href='https://www.who.int/news-room/feature-stories/detail/fighting-misinformation-in-the-time-of-covid-19-one-click-at-a-time' 
                        target='_blank'>WHO: Fighting misinformation in the time of COVID-19, one click at a time</a></li>
            </ul>
            </div>
            """, unsafe_allow_html=True)

        st.button("", on_click=set_text_key, args=("coronadone",), key="donecoronalider")

    if (
        st.session_state.text_key == "6000" and st.session_state.text_index == 4
    ) or st.session_state.ui_state["CoronaSlider"]:
        st.session_state.ui_state["CoronaSlider"] = True
        CoronasliderLogic.render()