import streamlit as st
import components.OnboardingLogic.onboardinglogic as OnboardingLogic
from data.char_speech_state import set_text_key
from data.ui_states import set_ui_state

def render():
    st.markdown('<div id="OnboardingAnchor"></div>', unsafe_allow_html=True)
    OnboardingLogic.render()
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

        st.button("", on_click=set_text_key, args=("onboarding2",), key="chat_onboardin2")

        st.markdown("""
        ---
        #### 🧭 Überblick über die Funktionen dieser Plattform:

        💬 **Sprechblasen & Charaktere**: Lies dir aufmerksam durch, was unser Charakter dir sagt. Über die Buttons mit dem Chat-Icon kannst du jederzeit neue Hinweise abrufen.

        🎯 **Interaktive Aufgaben**: Du wirst Texte verschieben, Zahlen schätzen oder Webseiten rekonstruieren müssen – nutze deinen Verstand und deine Intuition.

        🛠️ **Defekte Zonen**: Manche Bereiche wirken kaputt oder unvollständig – genau da musst du helfen, Fake News oder Deepfakes zu entlarven.

        👁️ **Kommst du nicht weiter?** Dieser Button hilft dir dabei, an die Stelle zu springen, an der du dich zu diesem Zeitpunkt befinden solltest.

        🏆 **Zertifikat**: Am Ende bekommst du ein persönliches Zertifikat als echter Faktenchecker.
        """)

        st.button("", on_click=set_text_key, args=("onboarding3",), key="chat_onboardin3")

        if (
            st.session_state.get("text_key") == "onboarding3"             
            and st.session_state.text_index == 3
        ) or st.session_state.ui_state["OnboardingText"] == True:
            set_ui_state("OnboardingText", True)
            st.markdown("""
            ---
            ### 🔍 Was sind Fake News – und warum sind sie gefährlich?

            Fake News sind absichtlich erfundene oder manipulierte Informationen, die wie echte Nachrichten aussehen. Sie wollen dich täuschen – zum Beispiel, um Stimmung zu machen, Geld zu verdienen oder politische Meinungen zu beeinflussen.

            Besonders in sozialen Medien verbreiten sich solche Falschinformationen rasend schnell. Warum? Weil sie starke Gefühle auslösen – Wut, Angst oder Mitleid. Genau das sorgt dafür, dass Menschen sie teilen, ohne sie zu hinterfragen.

            Das Problem: Fake News können echten Schaden anrichten. Sie untergraben Vertrauen in die Medien, führen zu Missverständnissen – und machen es schwer, zwischen Wahrheit und Lüge zu unterscheiden.

            Deshalb ist es so wichtig, sie zu erkennen. Forschende und Entwickler arbeiten mit künstlicher Intelligenz, um Fakes automatisch zu entlarven. Aber das reicht nicht:

            Was wirklich zählt, ist dein kritisches Denken. Du bist der Filter – du entscheidest, was du glaubst und weiterverbreitest.

            Und genau das trainierst du hier – mit Sam an deiner Seite.
            """)

            st.button("", on_click=set_text_key, args=("onboarding4",), key="chat_onboarding4")
    st.stop()