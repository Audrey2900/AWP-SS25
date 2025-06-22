import streamlit as st
from PIL import Image
import os
from io import BytesIO

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

    # Custom CSS für einheitliche Bildgrößen, Layout und farbige Progress Bars
    st.markdown("""
    <style>
    .image-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        margin-bottom: 20px;
        min-height: 450px;
    }
    .fixed-image {
        width: 100%;
        height: 250px;
        object-fit: cover;
        border-radius: 8px;
        border: 2px solid #ddd;
        margin-bottom: 10px;
    }
    .image-row {
        display: flex;
        gap: 15px;
        margin-bottom: 30px;
        align-items: flex-start;
    }
    .image-item {
        flex: 1;
        min-height: 500px;
        padding: 10px;
        border: 1px solid #e0e0e0;
        border-radius: 10px;
        background-color: rgba(255, 255, 255, 0.05);
        display: flex;
        flex-direction: column;
    }
    .radio-container {
        min-height: 120px;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }
    
    /* Custom Progress Bar Styles */
    .progress-bar-container {
        width: 100%;
        height: 25px;
        background-color: #e0e0e0;
        border-radius: 12px;
        overflow: hidden;
        margin: 10px 0;
        position: relative;
    }
    
    .progress-segment {
        height: 100%;
        float: left;
        transition: width 0.5s ease;
    }
    
    .progress-correct {
        background-color: #28a745;
    }
    
    .progress-wrong {
        background-color: #dc3545;
    }
    
    .progress-unanswered {
        background-color: #6c757d;
    }
    
    .progress-legend {
        display: flex;
        justify-content: space-between;
        margin-top: 5px;
        font-size: 0.9em;
    }
    
    .legend-item {
        display: flex;
        align-items: center;
        gap: 5px;
    }
    
    .legend-color {
        width: 15px;
        height: 15px;
        border-radius: 3px;
    }
    
    /* Form Submit Button Styling */
    .stFormSubmitButton > button {
        background-color: #f7941d !important;
        border-color: #f7941d !important;
        color: white !important;
    }
    
    .stFormSubmitButton > button:hover {
        background-color: #e6831a !important;
        border-color: #e6831a !important;
    }
    
    .stFormSubmitButton > button:focus {
        background-color: #f7941d !important;
        border-color: #f7941d !important;
        box-shadow: 0 0 0 0.2rem rgba(247, 148, 29, 0.25) !important;
    }
    </style>
    """, unsafe_allow_html=True)

    # Bilder einmalig laden, verkleinern und als Bytes cachen
    @st.cache_data
    def load_and_cache_images():
        base_path = os.path.join(os.getcwd(), "static")
        original_ordner = os.path.join(base_path, "Original_Bilder")
        fake_ordner = os.path.join(base_path, "KI_Bilder")

        def process_folder(folder, is_fake):
            images = []
            if os.path.exists(folder):
                for f in sorted(os.listdir(folder)):
                    if f.lower().endswith(('.jpg', '.png', '.jpeg')):
                        path = os.path.join(folder, f)
                        try:
                            img = Image.open(path)
                            target_size = (350, 250)  # Breite, Höhe

                            # Bild auf Zielgröße einpassen 
                            img = img.convert("RGB")
                            img.thumbnail(target_size, Image.LANCZOS)
                            background = Image.new("RGB", target_size, (14, 17, 23))
                            offset = ((target_size[0] - img.width) // 2, (target_size[1] - img.height) // 2)
                            background.paste(img, offset)
                            buf = BytesIO()
                            background.save(buf, format="JPEG", quality=85)
                            images.append((buf.getvalue(), is_fake, f))
                        except Exception as e:
                            st.error(f"Fehler beim Laden von {f}: {e}")
            return images

        originals = process_folder(original_ordner, False)
        fakes = process_folder(fake_ordner, True)
        return originals + fakes

    # Session State einmalig initialisieren
    if "deepfake_antworten" not in st.session_state:
        st.session_state.deepfake_antworten = {}
    
    if "deepfake_abgegeben" not in st.session_state:
        st.session_state.deepfake_abgegeben = False

    # Bilder laden (jetzt als Bytes)
    alle_bilder = load_and_cache_images()
    
    if not alle_bilder:
        st.error("Keine Bilder gefunden. Überprüfe die Ordnerstruktur in 'static/Original_Bilder' und 'static/KI_Bilder'.")
        st.stop()

    # Hilfsfunktion für Bildanzeige in Reihen
    def display_images_in_rows(bilder_liste, images_per_row=3, show_results=False):
        for row_start in range(0, len(bilder_liste), images_per_row):
            row_images = bilder_liste[row_start:row_start + images_per_row]
            cols = st.columns(images_per_row)
            # Bilder anzeigen
            for col_idx, (img_bytes, ist_fake, filename) in enumerate(row_images):
                with cols[col_idx]:
                    st.image(img_bytes, use_container_width=True)
            # Radio/Ergebnis auf gleicher Höhe
            cols2 = st.columns(images_per_row)
            for col_idx, (img_bytes, ist_fake, filename) in enumerate(row_images):
                with cols2[col_idx]:
                    with st.container():
                        if not show_results:
                            current_answer = st.session_state.deepfake_antworten.get(filename, "Unentschieden")
                            antwort = st.radio(
                                f"Ist dies ein Deepfake?",
                                ["Unentschieden", "Ja", "Nein"],
                                index=["Unentschieden", "Ja", "Nein"].index(current_answer),
                                key=f"radio_{row_start + col_idx}_{filename}"
                            )
                            st.session_state.deepfake_antworten[filename] = antwort
                        else:
                            antwort = st.session_state.deepfake_antworten.get(filename, "Unentschieden")
                            richtige_antwort = "Ja" if ist_fake else "Nein"
                            st.markdown(f"**Deine Antwort:** {antwort}")
                            st.markdown(f"**Richtige Antwort:** {richtige_antwort}")
                            if antwort == "Unentschieden":
                                st.warning("Keine Antwort")
                            elif antwort == richtige_antwort:
                                st.success("Richtig!")
                            else:
                                st.error("Falsch!")
                st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)
        st.markdown("<div style='height: 30px;'></div>", unsafe_allow_html=True)

    # Formular für alle Antworten (nur wenn noch nicht abgegeben)
    if not st.session_state.deepfake_abgegeben:
        with st.form("deepfake_form"):
            st.markdown('<div style="font-size:2em; font-weight:bold;">Bewerte die Bilder:</div>', unsafe_allow_html=True)
            
            # Bilder in Reihen anzeigen
            display_images_in_rows(alle_bilder, images_per_row=3, show_results=False)
            
            st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)
            
            # Submit Button
            submitted = st.form_submit_button("Antworten abgeben", use_container_width=True)
            
            if submitted:
                st.session_state.deepfake_abgegeben = True
                st.rerun()

    # Auswertung anzeigen
    if st.session_state.deepfake_abgegeben:
        st.markdown("<div style='height: 40px;'></div>", unsafe_allow_html=True)
        st.markdown('<div style="font-size:2em; font-weight:bold;">Auswertung:</div>', unsafe_allow_html=True)
        
        # Bilder mit Ergebnissen in Reihen anzeigen
        display_images_in_rows(alle_bilder, images_per_row=3, show_results=True)
        
        # Gesamtstatistik berechnen
        richtig = 0
        falsch = 0
        nicht_beantwortet = 0
        
        for bildpfad, ist_fake, filename in alle_bilder:
            antwort = st.session_state.deepfake_antworten.get(filename, "Unentschieden")
            richtige_antwort = "Ja" if ist_fake else "Nein"
            
            if antwort == "Unentschieden":
                nicht_beantwortet += 1
            elif antwort == richtige_antwort:
                richtig += 1
            else:
                falsch += 1
        
        # Gesamtstatistik anzeigen
        st.markdown("<div style='height: 40px;'></div>", unsafe_allow_html=True)
        st.markdown("### Gesamtergebnis:")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Richtig", richtig)
        with col2:
            st.metric("Falsch", falsch)
        with col3:
            st.metric("Nicht beantwortet", nicht_beantwortet)
        
        # Custom Progress Bar mit Farben
        total_images = len(alle_bilder)
        if total_images > 0:
            prozent_richtig = (richtig / total_images) * 100
            prozent_falsch = (falsch / total_images) * 100
            prozent_unbeantwortet = (nicht_beantwortet / total_images) * 100
            
            # Custom HTML Progress Bar
            progress_html = f"""
            <div class="progress-bar-container">
                <div class="progress-segment progress-correct" style="width: {prozent_richtig}%;"></div>
                <div class="progress-segment progress-wrong" style="width: {prozent_falsch}%;"></div>
                <div class="progress-segment progress-unanswered" style="width: {prozent_unbeantwortet}%;"></div>
            </div>
            <div class="progress-legend">
                <div class="legend-item">
                    <div class="legend-color progress-correct"></div>
                    <span>Richtig ({richtig}/{total_images})</span>
                </div>
                <div class="legend-item">
                    <div class="legend-color progress-wrong"></div>
                    <span>Falsch ({falsch}/{total_images})</span>
                </div>
                <div class="legend-item">
                    <div class="legend-color progress-unanswered"></div>
                    <span>Unbeantwortet ({nicht_beantwortet}/{total_images})</span>
                </div>
            </div>
            """
            
            st.markdown(f"<div style='font-size: 1.5em; font-weight: margin-top: 10px;'>{progress_html}</div>", unsafe_allow_html=True)
            st.markdown(f"<div style='font-size: 2em;'>Erfolgsquote: {prozent_richtig:.1f}%</div>", unsafe_allow_html=True)
        
        # Restart Button
        if st.button("Neu starten", use_container_width=True):
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

        Wenn dir etwas seltsam vorkommt: **Frag nach, schau genau hin – und vertraue deinem Bauchgefühl.**  
        Ein kritischer Blick ist der beste Schutz gegen Deepfakes.
        
        ---""")

if __name__ == "__main__":
    render()


