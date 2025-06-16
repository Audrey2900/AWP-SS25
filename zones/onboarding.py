import streamlit as st
import components.OnboardingLogic.onboardinglogic as OnboardingLogic
from data.char_speech_state import set_text_key

# 💬 Onboarding-Darstellung als Funktion
def render():
    st.header("Willkommen bei InfoGuard – der interaktiven Lernplattform für aufmerksame Internet-Detektive.")

    # 1. Chat-Button zur Begrüßung
    st.button("", on_click=set_text_key, args=("onboarding",), key="chat1")

    # Namenseingabe
    st.markdown("#### Wie heißt du? Gib deinen Vor- und Nachnamen ein:")
    vorname = st.text_input("Vorname", key="input_vorname")
    nachname = st.text_input("Nachname", key="input_nachname")

    if vorname and nachname:
        st.session_state.user_name = f"{vorname} {nachname}"

        # 2. Chat zur Erklärung der Mission und Einführung
        st.button("", on_click=set_text_key, args=("onboarding2",), key="chat2")

        # Platzhalter für spätere Funktionsübersicht
        st.markdown("""
        ---
        #### 🔍 Überblick über die Funktionen dieser Plattform:
        *(Hinweis: Kommt später)*
        ---
        """)

        # 3. Abschlusssatz & Übergang zur inhaltlichen Einführung
        st.button("", on_click=set_text_key, args=("onboarding3",), key="chat3")

        # Text + Chat4 nur wenn der letzte Dialog aktiv ist
        if st.session_state.get("text_key") == "onboarding3":
            st.markdown("""
            ---
            ### 🔍 Was sind Fake News – und warum sind sie gefährlich?

            Fake News sehen oft aus wie echte Nachrichten – aber sie wurden absichtlich manipuliert, um dich zu täuschen.

            Sie nutzen starke Emotionen, damit du nicht hinterfragst, sondern einfach weiterleitest. Manchmal stecken persönliche Meinungen dahinter – manchmal politische Absichten oder sogar kommerzielle Ziele.

            Wer Fake News erkennt, schützt nicht nur sich selbst – sondern auch andere.

            👁️ Frage dich immer: Wer sagt das? Warum? Und kann ich das irgendwo nachprüfen?

            Gleich wirst du einige dieser Täuschungen selbst entlarven – bist du bereit?
            """)

            st.button("", on_click=set_text_key, args=("onboarding4",), key="chat4")

    OnboardingLogic.render()