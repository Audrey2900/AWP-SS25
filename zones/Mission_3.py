import streamlit as st
from PIL import Image
import os

# Ordnerpfade
base_path = os.path.join(os.getcwd(), "static")
original_ordner = os.path.join(base_path, "Original_Bilder")
fake_ordner = os.path.join(base_path, "KI_Bilder")

def render():
    col1, col2 = st.columns([3, 1])
    with col1:
        st.title("Mission 3: Deepfake-Erkennung", anchor="mission3")
        st.markdown("""
        In dieser Mission lernst du, echte Bilder von KI-generierten Deepfakes zu unterscheiden.  
        Bewerte für jedes Bild, ob du es für **einen Fake** hältst oder nicht.  
        **Schau dir die Bilder genau an und markiere die Deepfakes.**
        """)
    with col2:
        st.markdown("""
            <img src="/app/static/deepfake_icon.png"
            alt="Deepfake Icon"
            style="width: 100%; border-radius: 8px;" />""",
        unsafe_allow_html=True)

    st.markdown("<div style='height: 40px;'></div>", unsafe_allow_html=True)

    st.markdown("""
    ### Was sind Deepfakes?

    **Deepfakes** sind täuschend echte Bilder, Videos oder Audios, die mit Hilfe von künstlicher Intelligenz erstellt oder verändert wurden.  
    Sie können reale Personen scheinbar Dinge sagen oder tun lassen, die sie nie gesagt oder getan haben.  
    Besonders bekannt sind Deepfake-Gesichter – sie wirken echt, sind aber computergeneriert oder manipuliert.
    """)

    st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)

    # Bilder laden
    original_bilder = [(os.path.join(original_ordner, f), False) for f in sorted(os.listdir(original_ordner)) if f.lower().endswith(('.jpg', '.png'))]
    fake_bilder = [(os.path.join(fake_ordner, f), True) for f in sorted(os.listdir(fake_ordner)) if f.lower().endswith(('.jpg', '.png'))]

    # Feste Reihenfolge
    alle_bilder = original_bilder + fake_bilder

    # Session State initialisieren
    if "antworten" not in st.session_state:
        st.session_state.antworten = {}

    if "abgegeben" not in st.session_state:
        st.session_state.abgegeben = False

    # Rasteranzeige
    cols = st.columns(4)
    for idx, (bildpfad, ist_fake) in enumerate(alle_bilder):
        col = cols[idx % 4]
        with col:
            image = Image.open(bildpfad)
            st.image(image, use_container_width=True)

            name = os.path.basename(bildpfad)

            if not st.session_state.abgegeben:
                antwort = st.radio(
                    "Deepfake?",
                    ["Unentschieden", "Ja", "Nein"],
                    index=0,
                    key=f"radio_{idx}"
                )
                st.session_state.antworten[bildpfad] = antwort
            else:
                antwort = st.session_state.antworten.get(bildpfad, "Unentschieden")

                st.markdown(f"**Deine Antwort:** `{antwort}`")

                richtige_antwort = "Ja" if ist_fake else "Nein"
                st.markdown(f"**Richtige Antwort:** `{richtige_antwort}`")

                if antwort == "Unentschieden":
                    st.warning("Keine Antwort gegeben.")
                elif antwort == richtige_antwort:
                    st.success("Richtig erkannt!")
                else:
                    st.error("Falsch eingeschätzt.")

    # Abgabe-Button
    st.markdown("<div style='height: 40px;'></div>", unsafe_allow_html=True)
    
    if not st.session_state.abgegeben:
        if st.button("Antworten abgeben"):
            st.session_state.abgegeben = True
            st.rerun()

    # Gesamtauswertung
    if st.session_state.abgegeben:
        richtig = 0
        falsch = 0
        nicht_beantwortet = 0

        for bildpfad, ist_fake in alle_bilder:
            antwort = st.session_state.antworten.get(bildpfad, "Unentschieden")
            richtige_antwort = "Ja" if ist_fake else "Nein"

            if antwort == "Unentschieden":
                nicht_beantwortet += 1
            elif antwort == richtige_antwort:
                richtig += 1
            else:
                falsch += 1

        st.markdown("<div style='height: 40px;'></div>", unsafe_allow_html=True)
        
        st.markdown("### Gesamtauswertung")
        st.info(f"""
    **Richtige Einschätzungen:** {richtig}  
    **Falsche Einschätzungen:** {falsch}  
    **Unbeantwortet:** {nicht_beantwortet}
    """)

        if st.button("Neu starten"):
            del st.session_state.antworten
            del st.session_state.abgegeben
            st.rerun()

        st.markdown("""
        ### Fazit: So erkennst du Deepfakes

        Deepfakes können täuschend echt wirken – doch mit etwas Übung und einem wachsamen Blick lassen sich viele Hinweise entdecken.

        **Achte besonders auf:**
        - *Unnatürliche Augenbewegungen* oder seltener Lidschlag  
        - *Verwaschene Übergänge* zwischen Gesicht, Haaren oder Hintergrund  
        - *Asymmetrien* bei Zähnen, Ohren oder Händen  
        - *Steife Bewegungen* und unnatürlich wirkende Mimik  
        - *Unstimmige Details* im Hintergrund (z.B. schiefe Möbel, verschwommene Objekte)  

        **Zusätzlicher Tipp:**  
        Prüfe, woher das Bild oder Video stammt. Fehlende Metadaten oder unbekannte Quellen können ein Warnsignal sein.

        ---

        Wenn dir etwas seltsam vorkommt: **Frag nach, schau genau hin – und vertraue deinem Bauchgefühl.**  
        Ein kritischer Blick ist der beste Schutz gegen Deepfakes.
        """)

if __name__ == "__main__":
    render()


