import streamlit as st
from PIL import Image
import os
from io import BytesIO
from data.char_speech_state import set_text_key

def render():
    col1, col2 = st.columns([3, 1])
    with col1:
        st.title("Täuschend echte Bilder – oder doch nicht?", anchor="mission3")
    with col2:
        st.button("", on_click=set_text_key, args=("mission3.1",), key="chat3-1")

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

    # Bilder laden und anzeigen
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
                            target_size = (350, 250)
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

    if "deepfake_antworten" not in st.session_state:
        st.session_state.deepfake_antworten = {}
    
    if "deepfake_abgegeben" not in st.session_state:
        st.session_state.deepfake_abgegeben = False

    alle_bilder = load_and_cache_images()

    if not alle_bilder:
        st.error("Keine Bilder gefunden. Überprüfe die Ordnerstruktur in 'static/Original_Bilder' und 'static/KI_Bilder'.")
        st.stop()

    def display_images_in_rows(bilder_liste, images_per_row=3, show_results=False):
        for row_start in range(0, len(bilder_liste), images_per_row):
            row_images = bilder_liste[row_start:row_start + images_per_row]
            cols = st.columns(images_per_row)
            for col_idx, (img_bytes, ist_fake, filename) in enumerate(row_images):
                with cols[col_idx]:
                    st.image(img_bytes, use_container_width=True)
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

    if not st.session_state.deepfake_abgegeben:
        with st.form("deepfake_form"):
            st.markdown('<div style="font-size:2em; font-weight:bold;">Bewerte die Bilder:</div>', unsafe_allow_html=True)
            display_images_in_rows(alle_bilder, images_per_row=3, show_results=False)
            submitted = st.form_submit_button("Antworten abgeben", use_container_width=True)
            if submitted:
                st.session_state.deepfake_abgegeben = True
                st.rerun()

    if st.session_state.deepfake_abgegeben:
        st.markdown('<div style="font-size:2em; font-weight:bold;">Auswertung:</div>', unsafe_allow_html=True)
        display_images_in_rows(alle_bilder, images_per_row=3, show_results=True)

        richtig = falsch = nicht_beantwortet = 0
        for _, ist_fake, filename in alle_bilder:
            antwort = st.session_state.deepfake_antworten.get(filename, "Unentschieden")
            richtige_antwort = "Ja" if ist_fake else "Nein"
            if antwort == "Unentschieden":
                nicht_beantwortet += 1
            elif antwort == richtige_antwort:
                richtig += 1
            else:
                falsch += 1

        st.markdown("### Gesamtergebnis:")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Richtig", richtig)
        with col2:
            st.metric("Falsch", falsch)
        with col3:
            st.metric("Nicht beantwortet", nicht_beantwortet)

        total_images = len(alle_bilder)
        if total_images > 0:
            prozent_richtig = (richtig / total_images) * 100
            prozent_falsch = (falsch / total_images) * 100
            prozent_unbeantwortet = (nicht_beantwortet / total_images) * 100
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

        if st.button("Neu starten", use_container_width=True):
            st.session_state.deepfake_antworten = {}
            st.session_state.deepfake_abgegeben = False
            st.rerun()

        st.button("", on_click=set_text_key, args=("mission3.2",), key="chat3-2")

if __name__ == "__main__":
    render()