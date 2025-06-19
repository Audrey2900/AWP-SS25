import streamlit as st
import tempfile
import streamlit.components.v1 as components
from fpdf import FPDF
from datetime import datetime
import random
from data.char_speech_state import set_text_key
from data.zone_anchor import set_zone

set_zone("offboarding")

def generate_certificate(name: str) -> bytes:
    pdf = FPDF(orientation='L', unit='mm', format='A4')
    pdf.add_page()

    pdf.set_fill_color(255, 255, 255)
    pdf.rect(230, 12, 45, 45, style='F')
    pdf.image("static/LogoInfoGuard-Neu.png", x=230, y=12, w=45)

    pdf.set_line_width(1)
    pdf.rect(10, 10, 277, 190)

    pdf.set_font("Helvetica", 'B', 36)
    pdf.set_text_color(0, 102, 204)
    pdf.cell(0, 40, "Faktenchecker-Zertifikat", ln=True, align='C')

    pdf.set_font("Helvetica", '', 20)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(0, 10, "verliehen an", ln=True, align='C')
    pdf.set_font("Helvetica", 'B', 28)
    pdf.cell(0, 15, name, ln=True, align='C')
    pdf.set_font("Helvetica", '', 14)
    current_date = datetime.now().strftime("%d.%m.%Y")
    pdf.cell(0, 10, f"Datum: {current_date}", ln=True, align='C')

    pdf.set_font("Helvetica", '', 16)
    pdf.ln(10)
    pdf.multi_cell(0, 10,
        "für die erfolgreiche Teilnahme am interaktiven Lernprogramm\n"
        "\"Fake News & Deepfakes erkennen und bewerten\"", 
        align='C')

    cert_id = f"ZERT-{random.randint(100000,999999)}"
    pdf.ln(5)
    pdf.set_font("Helvetica", 'I', 10)
    #pdf.cell(0, 10, f"Zertifikatsnummer: {cert_id}", ln=True, align='C')

    pdf.image("static/InfoGuard_UP.png", x=85, y=115, w=120)

    pdf.ln(30)
    pdf.set_font("Helvetica", 'I', 12)
    pdf.cell(0, 10, "Unterschrift: ____________________", ln=True, align='R')

    pdf.image("static/stempel.png", x=20, y=155, w=40)
    pdf.image("static/unterschrift.png", x=200, y=170, w=50)

    return pdf.output(dest='S').encode('latin1')

def render():
    name = st.session_state.get("user_name", "Teilnehmer*in")

    # prechblasen-Button ganz oben
    st.button("", on_click=set_text_key, args=("offboarding",), key="chat12")

    # Überschrift
    st.markdown("<h1 style='text-align: center; margin-top: 30px;'>🏁 Fertig! Du hast es geschafft! 🥳</h1>", unsafe_allow_html=True)
    
    # 🎓 Info-Text zentriert
    st.markdown(f"""
        <div style="text-align: center; margin-top: 50px; margin-bottom: 30px;">
            <h3>🎓 {name}, du bist jetzt ein zertifizierter <strong>Faktenchecker</strong>!</h3>
        </div>
        <div style="text-align: center; margin-bottom: 30px;">
            <p style="font-size: 18px;">
  Dein offizielles Zertifikat wartet auf dich.<br>
  Klicke, um es herunterzuladen:<br>
  <span style="font-size: 50px;">⬇️</span>
</p>
    """, unsafe_allow_html=True)

    # Zertifikat erzeugen
    pdf_bytes = generate_certificate(name)

    # Button zentrieren mit CSS
    st.markdown("""
        <style>
        div.stDownloadButton {
            display: flex;
            justify-content: center;
        }
        </style>
    """, unsafe_allow_html=True)

    st.download_button(
        label="📥 Zertifikat herunterladen",
        data=pdf_bytes,
        file_name=f"factchecker_zertifikat_{name.replace(' ', '_')}.pdf",
        mime="application/pdf",
        key="download_button"
    )

    # Ballon-Effekt beim Klick
    st.markdown("""
    <script>
    const dlButton = parent.document.querySelector('button[data-testid="baseButton-download_button"]');
    if (dlButton) {
        dlButton.addEventListener('click', function() {
            const balloons = document.createElement('div');
            balloons.innerHTML = "🎈🎉🎈";
            balloons.style.position = "fixed";
            balloons.style.top = "20px";
            balloons.style.left = "50%";
            balloons.style.transform = "translateX(-50%)";
            balloons.style.fontSize = "3rem";
            balloons.style.zIndex = "9999";
            balloons.style.animation = "fadeout 3s ease-out forwards";
            document.body.appendChild(balloons);
            setTimeout(() => balloons.remove(), 3000);
        });
    }
    </script>
    <style>
    @keyframes fadeout {
        0% { opacity: 1; }
        100% { opacity: 0; transform: translateY(80px); }
    }
    </style>
    """, unsafe_allow_html=True)
