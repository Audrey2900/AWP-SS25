import streamlit as st
from data.char_speech_state import set_text_key

def render():
    st.header("Willkommen bei InfoGuard – der interaktiven Lernplattform für aufmerksame Internet-Detektive.")

    st.write("")  # Pufferplatz
    st.write("")  # Noch mehr Pufferplatz
    
    # Namenseingabe
    st.markdown("#### Wie heißt du? Gib deinen Vor- und Nachnamen ein:")
    vorname = st.text_input("Vorname", key="input_vorname")
    nachname = st.text_input("Nachname", key="input_nachname")

    if vorname and nachname:
        st.session_state.user_name = f"{vorname} {nachname}"

        # Automatisch den ersten Button "drücken", wenn Namen eingegeben wurden
        if "auto_pressed_chat2" not in st.session_state:
            st.session_state.auto_pressed_chat2 = True
            set_text_key("onboarding2")
            st.session_state.text_index = 0  # Text-Index zurücksetzen
            st.rerun()  # Seite neu laden, damit der neue Text angezeigt wird

        st.button("", on_click=set_text_key, args=("onboarding2",), key="chat2")

        st.markdown("""
        ---
        #### 🧭 Überblick über die Funktionen dieser Plattform:

        💬 **Sprechblasen & Charaktere**: Lies dir aufmerksam durch, was unser Charakter dir sagt. Über die Buttons mit dem Chat-Icon kannst du jederzeit neue Hinweise abrufen.

        🎯 **Interaktive Aufgaben**: Du wirst Texte verschieben, Zahlen schätzen oder Webseiten rekonstruieren müssen – nutze deinen Verstand und deine Intuition.

        🛠️ **Defekte Zonen**: Manche Bereiche wirken kaputt oder unvollständig – genau da musst du helfen, Fake News oder Deepfakes zu entlarven.

        👁️ **Kommst du nicht weiter?** Dieser Button hilft dir dabei an die Stelle zu springen an deer du dich befinden zu dem Zeitpunkt befinden solltest.

        🏆 **Zertifikat**: Am Ende bekommst du ein persönliches Zertifikat als echter Faktenchecker.
        """)

        st.button("", on_click=set_text_key, args=("onboarding3",), key="chat3")

        if st.session_state.get("text_key") == "onboarding3":
            st.markdown("""
            ---
            ### 🔍 Was sind Fake News – und warum sind sie gefährlich?

            Fake News sehen oft aus wie echte Nachrichten – aber sie wurden absichtlich manipuliert, um dich zu täuschen.

            Sie nutzen starke Emotionen, damit du nicht hinterfragst, sondern einfach weiterleitest. Manchmal stecken persönliche Meinungen dahinter – manchmal politische Absichten oder sogar kommerzielle Ziele.

            Wer Fake News erkennt, schützt nicht nur sich selbst – sondern auch andere.

            Frage dich immer: Wer sagt das? Warum? Und kann ich das irgendwo nachprüfen?

            Gleich wirst du einige dieser Täuschungen selbst entlarven – bist du bereit?
            """)

            st.button("", on_click=set_text_key, args=("onboarding4",), key="chat4")