import streamlit as st
from components.DeepfakeFinder import deepfakefinder

def render():

    st.markdown("""
        ### So erkennst du Deepfakes

        Deepfakes wirken oft täuschend echt. Doch bei genauem Hinsehen lassen sich typische Hinweise entdecken, die auf eine Fälschung hinweisen.

        **Ein Klick auf das Bild aktiviert die Lupe**, die verdächtige Stellen farblich markiert.  
        
        Das zugehörige Erkennungsmerkmal kann auch direkt unter dem Bild eingeblendet werden.

        """)
    
    deepfakefinder()
    
    st.markdown("""
    **Zusätzlicher Tipp:**  
    Prüfe, woher das Bild oder Video stammt. Fehlende Metadaten oder unbekannte Quellen können ein Warnsignal sein.

    Bei Video- oder Audio-Deepfakes lohnt sich ein genauer Blick auf bestimmte Merkmale:

    **Augen, Gesicht und Bewegungen analysieren:**  
    Unnatürliche Augenbewegungen, seltenes Blinzeln oder asymmetrische Gesichter können Hinweise auf eine Manipulation sein.  
    Auch auffällig glatte Haut, falsche Schattenverläufe oder unrealistische Lichtreflexe sollten stutzig machen.

    **Stimme und Sprache prüfen:**  
    Audio-Deepfakes erkennt man häufig an monotonen oder emotionslosen Stimmen, fehlenden Pausen oder unnatürlichen Übergängen im Klang.

    **Kontext und Quelle kritisch hinterfragen:**  
    Wird das Material auch von seriösen Quellen berichtet? Nutze die SIFT-Methode: Stop – Investigate the source – Find other coverage – Trace the original context.

    **Technische Hilfsmittel nutzen:**  
    Werkzeuge wie der Deepfake-o-meter, Microsoft Authenticator oder FakeCatcher können Hinweise liefern, sind aber nicht unfehlbar. Kritisches Denken bleibt entscheidend.

    **Wenn dir etwas seltsam vorkommt:**
    Frag nach, schau genau hin – und vertraue deinem Bauchgefühl. 
    Ein kritischer Blick ist der beste Schutz gegen Deepfakes.
    """)