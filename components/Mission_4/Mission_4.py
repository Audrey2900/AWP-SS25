import time
import streamlit as st
from data.char_speech_state import set_text_key

def render():
    st.title("Fast geschafft – bring Licht ins digitale Dunkel", anchor="Mission4")

    # Intro-Dialog durch Chatbutton
    st.button("", on_click=set_text_key, args=("mission4.1", "Mission4"), key="chat4-1")

    st.markdown("<div style='height: 24px;'></div>", unsafe_allow_html=True)

    # Quizdefinition
    quiz = [
        {
            "frage": "Was ist ein typisches visuelles Merkmal eines Deepfakes?",
            "optionen": [
                "Hohe Auflösung und natürliche Beleuchtung",
                "Unnatürliche Augenbewegungen oder seltenes Blinzeln",
                "Schnelle Schnitte wie in Musikvideos"
            ],
            "lösung": 1
        },
        {
            "frage": "Was fällt bei Audio-Deepfakes oft auf?",
            "optionen": [
                "Besonders laute Geräusche im Hintergrund",
                "Unterschiedliche Lautstärke zwischen Worten",
                "Monotone oder emotionslose Stimme"
            ],
            "lösung": 2
        },
        {
            "frage": "Was gehört zur SIFT-Methode?",
            "optionen": [
                "Screenshot machen, Internet befragen, Fakten suchen, Teilen",
                "Stop, Investigate source, Find coverage, Trace statement",
                "Scannen, Identifizieren, Filtern, Teilen"
            ],
            "lösung": 1
        },
        {
            "frage": "Was gilt für technische Tools zur Deepfake-Erkennung?",
            "optionen": [
                "Sie liefern eindeutige Beweise für Echtheit",
                "Sie sind unzuverlässig und verboten",
                "Sie helfen, aber kritisches Denken ist weiterhin wichtig"
            ],
            "lösung": 2
        }
    ]

    st.markdown("<div style='height: 24px;'></div>", unsafe_allow_html=True)

    # Initialisierung der Antworten
    if "mission4_antworten" not in st.session_state:
        st.session_state.mission4_antworten = [0] * len(quiz)

    for i, eintrag in enumerate(quiz):
        auswahl = st.radio(
            eintrag["frage"], 
            eintrag["optionen"], 
            key=f"mission4_frage_{i}",
            index=st.session_state.mission4_antworten[i]
        )
        st.session_state.mission4_antworten[i] = eintrag["optionen"].index(auswahl)
        st.markdown("<div style='height: 16px;'></div>", unsafe_allow_html=True)

    if st.button("Abgeben", key="mission4_abgeben"):
        punkte = sum(
            1 for i, eintrag in enumerate(quiz)
            if st.session_state.mission4_antworten[i] == eintrag["lösung"]
        )
        st.session_state.mission4_result = punkte
        st.session_state.mission4_submitted = True
        st.rerun()

    # Ergebnis anzeigen, falls vorhanden
    if st.session_state.get("mission4_submitted"):
        punkte = st.session_state.get("mission4_result", 0)

        st.success(f"Du hast {punkte} von {len(quiz)} Fragen richtig beantwortet!")

        st.markdown("<div style='height: 16px;'></div>", unsafe_allow_html=True)

        if punkte == len(quiz):
            st.markdown("### Glückwunsch, du hast alle Hinweise richtig entschlüsselt!")
            st.markdown("Der Zeitungsartikel ist nun wieder vollständig lesbar:")
            st.markdown("<div style='height: 16px;'></div>", unsafe_allow_html=True)
        else:
            st.markdown("Du kannst es nochmal versuchen oder unten die richtigen Antworten vergleichen.")
            st.markdown("<div style='height: 8px;'></div>", unsafe_allow_html=True)
            with st.expander("Richtige Antworten anzeigen"):
                for i, eintrag in enumerate(quiz):
                    richtige = eintrag["optionen"][eintrag["lösung"]]
                    st.markdown(f"**Frage {i+1}:** {richtige}")

        if st.session_state.ui_state["NoCorruptionAiFakeNews"] == False:
            time.sleep(1.5)
            st.session_state.ui_state["NoCorruptionAiFakeNews"] = True
            st.rerun()

        st.button("", on_click=set_text_key, args=("mission4.2",), key="chat4-2")

    if (
        st.session_state.text_key == "mission4.2" and st.session_state.text_index == 2
    ) and st.session_state.ui_state["Offboarding"] == False:
        time.sleep(1.5)
        st.session_state.ui_state["Offboarding"] = True
        st.rerun()

if __name__ == "__main__":
    st.set_page_config(page_title="Deepfake erkennen", layout="centered")
    render()
