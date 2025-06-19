import streamlit as st
from PIL import Image
import os

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

    # Bilder einmalig laden und cachen
    @st.cache_data
    def load_images():
        base_path = os.path.join(os.getcwd(), "static")
        original_ordner = os.path.join(base_path, "Original_Bilder")
        fake_ordner = os.path.join(base_path, "KI_Bilder")
        
        original_bilder = []
        fake_bilder = []
        
        # Original Bilder laden
        if os.path.exists(original_ordner):
            for f in sorted(os.listdir(original_ordner)):
                if f.lower().endswith(('.jpg', '.png', '.jpeg')):
                    original_bilder.append((os.path.join(original_ordner, f), False, f))
        
        # Fake Bilder laden
        if os.path.exists(fake_ordner):
            for f in sorted(os.listdir(fake_ordner)):
                if f.lower().endswith(('.jpg', '.png', '.jpeg')):
                    fake_bilder.append((os.path.join(fake_ordner, f), True, f))
        
        return original_bilder + fake_bilder

    # Session State einmalig initialisieren
    if "deepfake_antworten" not in st.session_state:
        st.session_state.deepfake_antworten = {}
    
    if "deepfake_abgegeben" not in st.session_state:
        st.session_state.deepfake_abgegeben = False

    # Bilder laden
    alle_bilder = load_images()
    
    if not alle_bilder:
        st.error("Keine Bilder gefunden. Überprüfe die Ordnerstruktur in 'static/Original_Bilder' und 'static/KI_Bilder'.")
        return

    # Formular für alle Antworten
    with st.form("deepfake_form"):
        st.markdown("### Bewerte die Bilder:")
        
        # Rasteranzeige
        cols = st.columns(3)  # 3 Spalten für bessere Übersicht
        
        for idx, (bildpfad, ist_fake, filename) in enumerate(alle_bilder):
            col = cols[idx % 3]
            
            with col:
                try:
                    image = Image.open(bildpfad)
                    st.image(image, caption=f"Bild {idx + 1}", use_container_width=True)
                    
                    # Radio-Button für jedes Bild
                    current_answer = st.session_state.deepfake_antworten.get(filename, "Unentschieden")
                    
                    antwort = st.radio(
                        f"Ist Bild {idx + 1} ein Deepfake?",
                        ["Unentschieden", "Ja", "Nein"],
                        index=["Unentschieden", "Ja", "Nein"].index(current_answer),
                        key=f"radio_{idx}_{filename}"
                    )
                    
                    # Antwort in Session State speichern
                    st.session_state.deepfake_antworten[filename] = antwort
                    
                except Exception as e:
                    st.error(f"Fehler beim Laden von {filename}: {str(e)}")
        
        st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)
        
        # Submit Button
        submitted = st.form_submit_button("Antworten abgeben")
        
        if submitted:
            st.session_state.deepfake_abgegeben = True
            st.rerun()

    # Auswertung anzeigen
    if st.session_state.deepfake_abgegeben:
        st.markdown("<div style='height: 40px;'></div>", unsafe_allow_html=True)
        st.markdown("### Auswertung:")
        
        richtig = 0
        falsch = 0
        nicht_beantwortet = 0
        
        # Ergebnisse in Spalten anzeigen
        result_cols = st.columns(3)
        
        for idx, (bildpfad, ist_fake, filename) in enumerate(alle_bilder):
            col = result_cols[idx % 3]
            
            with col:
                try:
                    image = Image.open(bildpfad)
                    st.image(image, caption=f"Bild {idx + 1}", use_container_width=True)
                    
                    antwort = st.session_state.deepfake_antworten.get(filename, "Unentschieden")
                    richtige_antwort = "Ja" if ist_fake else "Nein"
                    
                    st.markdown(f"**Deine Antwort:** {antwort}")
                    st.markdown(f"**Richtige Antwort:** {richtige_antwort}")
                    
                    if antwort == "Unentschieden":
                        st.warning("Keine Antwort")
                        nicht_beantwortet += 1
                    elif antwort == richtige_antwort:
                        st.success("Richtig!")
                        richtig += 1
                    else:
                        st.error("Falsch!")
                        falsch += 1
                        
                except Exception as e:
                    st.error(f"Fehler: {str(e)}")
        
        # Gesamtstatistik
        st.markdown("<div style='height: 40px;'></div>", unsafe_allow_html=True)
        st.markdown("### Gesamtergebnis:")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Richtig", richtig)
        with col2:
            st.metric("Falsch", falsch)
        with col3:
            st.metric("Nicht beantwortet", nicht_beantwortet)
        
        prozent_richtig = (richtig / len(alle_bilder)) * 100 if len(alle_bilder) > 0 else 0
        st.progress(prozent_richtig / 100)
        st.markdown(f"**Erfolgsquote: {prozent_richtig:.1f}%**")
        
        # Restart Button
        if st.button("Neu starten"):
            st.session_state.deepfake_antworten = {}
            st.session_state.deepfake_abgegeben = False
            st.rerun()

        # Fazit
        st.markdown("<div style='height: 40px;'></div>", unsafe_allow_html=True)
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


