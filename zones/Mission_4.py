import streamlit as st

def render():
    st.title("Deepfakes erkennen – Wie können wir Deepfakes erkennen und nicht auf Fakenews reinfallen")
    st.markdown("Es scheint so, als wäre die Internetseite auch komprimiert. \
    Wähle für jede Aussage die **richtige** Antwort aus und hilf mir die kaputten Texte wieder herzustellen.")

    # Fragen+ Lösungen
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

    # Speichern der Antworten
    if "mission4_antworten" not in st.session_state:
        st.session_state.mission4_antworten = [0] * len(quiz)

    # Anzeige der Fragen
    for i, eintrag in enumerate(quiz):
        auswahl = st.radio(
            eintrag["frage"], 
            eintrag["optionen"], 
            key=f"mission4_frage_{i}",
            index=st.session_state.mission4_antworten[i]
        )
        st.session_state.mission4_antworten[i] = eintrag["optionen"].index(auswahl)

    # Auswertung
    if st.button("Abgeben", key="mission4_abgeben"):
        punkte = 0
        for i, eintrag in enumerate(quiz):
            if st.session_state.mission4_antworten[i] == eintrag["lösung"]:
                punkte += 1

        st.success(f"Du hast {punkte} von {len(quiz)} Fragen richtig beantwortet!")

        if punkte == len(quiz):
            st.markdown("### Glückwunsch, du hast alle Hinweise richtig entschlüsselt!")
            st.markdown("Der Zeitungsartikel ist nun wieder vollständig lesbar:")

            st.markdown("""
            ---
            ## Deepfakes erkennen

            ### Praktische Hinweise

            - **Augen, Gesicht & Bewegungen analysieren**  
              Achte auf unnatürliche Augenbewegungen, seltenes Blinzeln oder asymmetrische Gesichter.  
              Auch ein weiches, glänzendes Hautbild oder falsche Schattenverläufe fallen auf.

            - **Stimme und Sprache prüfen**  
              Audio-Deepfakes erkennt man an monotonen oder emotionslosen Stimmen, fehlenden Pausen oder unnatürlichen Geräuschen.

            - **Kontext und Quelle kritisch hinterfragen**  
              Seriöse Medien berichten über den Inhalt? Nutze die SIFT-Methode: **Stop, Investigate source, Find coverage, Trace statement**

            - **Technische Hilfsmittel nutzen**  
              Tools wie der DeepFake‑o‑meter, Microsoft Authenticator oder FakeCatcher analysieren Deepfakes, sind aber nicht unfehlbar – **kritisches Denken bleibt entscheidend!**

            ---
            """)
        else:
            st.markdown("Du kannst es nochmal versuchen oder unten die richtigen Antworten vergleichen.")
            with st.expander("Richtige Antworten anzeigen"):
                for i, eintrag in enumerate(quiz):
                    richtige = eintrag["optionen"][eintrag["lösung"]]
                    st.markdown(f"**Frage {i+1}:** {richtige}")

# Diese Zeile wird nicht gebraucht, wenn die render() Funktion von außen
# aufgerufen wird, z.B. aus der index.py
if __name__ == "__main__":
    st.set_page_config(page_title="Deepfake erkennen", layout="centered")
    render()
