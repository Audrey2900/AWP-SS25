import streamlit as st
from components.DeepfakeFinder import deepfakefinder

def render():

    st.markdown("""
        ### So erkennst du Deepfakes

        Deepfakes können täuschend echt wirken – doch mit etwas Übung und einem wachsamen Blick lassen sich viele Hinweise entdecken.
        In der Folgenden Grafik können einige Erkennungsmerkmale interaktiv gesucht werden.
        Klicke auf das Bild, um die Lupe zu verwenden, welche Hinweise farblich markiert.
        Das Erkennungsmerkmal kann ebenfalls direkt unten aufgelöst werden.
        
        """)
    
    deepfakefinder()
    
    st.markdown("""

        **Zusätzlicher Tipp:**  
        Prüfe, woher das Bild oder Video stammt. Fehlende Metadaten oder unbekannte Quellen können ein Warnsignal sein.

        Wenn dir etwas seltsam vorkommt: **Frag nach, schau genau hin – und vertraue deinem Bauchgefühl.**  
        Ein kritischer Blick ist der beste Schutz gegen Deepfakes.
        
        ---""")