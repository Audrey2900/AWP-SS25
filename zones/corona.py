import streamlit as st
import components.CoronaExpanders.coronaexpanders as CoronaExpanders
import components.CoronaDragPuzzle.coronadragpuzzle as CoronaDragPuzzle
import components.Corruption.corruption as Corruption
import components.CoronaSlider.coronaslider as CoronaSlider
import components.CoronaMiniDashboard.minidashboard as MiniDashboard

def render():
    st.title("Corona und Fake News: Wie ein Virus die Wahrheit infizierte")

    # Puzzle
    #CoronaDragPuzzle.render()

    #if st.session_state.ui_state["NoCorruptionDragPuzzle"] == False:
       # Corruption.render()

    # Slider
    #CoronaSlider.render()

    #if st.session_state.ui_state["NoCorruptionCoronaSlider"] == False:
        #Corruption.render()

    st.markdown("""
**800 Menschen starben**. Andere wiederum hielten das Virus für harmlos oder gar für erfunden, was dazu führte, dass sie sich nicht mehr schützten und damit sich und andere in Gefahr brachten.

**Besonders beliebt waren Verschwörungstheorien. Die bekanntesten Verschwörungstheorien während der Coronazeit waren:**
""")

    #CoronaExpanders.render()

    st.markdown("""
Was diese Theorien gemeinsam haben? Sie sind komplett frei erfunden. Und trotzdem glaubten Millionen Menschen daran. In den USA hielten **78 %** mindestens eine verbreitete Corona-Falschaussage für möglich oder wahr.

Aber wie konnten sich solche Falschinfos so schnell verbreiten? Die Antwort ist einfach: über Social Media und Messenger. TikTok, Instagram, YouTube, Telegram und WhatsApp sind nicht nur unsere Kommunikationskanäle, sondern auch Nachrichtenquellen. Und was sich dort gut verbreitet, ist oft das, was besonders aufregend, schockierend oder empörend ist, nicht unbedingt das, was wahr ist. Auf Telegram etwa wurden jeden Tag hunderttausende Nachrichten mit Falschbehauptungen abgerufen. YouTube-Videos wie **"Plandemic"** wurden millionenfach gesehen, bevor sie überhaupt gelöscht wurden.

Das Gefährliche daran ist, dass Fake News oft sehr überzeugend aussehen. Manche basieren auf echten Infos, die dann verdreht oder aus dem Zusammenhang gerissen wurden. Wenn ein TikTok-Video sagt, Vitamin C schützt vor Corona, klingt das vielleicht plausibel, aber es stimmt nicht.
""")
    
    MiniDashboard.render()



# Quellen:
#https://www.stiftungen.org/aktuelles/news-aus-stiftungen/detail/studie-zu-desinformation-von-jungen-menschen-in-der-coronakrise-4986.html
#https://www.bitkom.org/Presse/Presseinformation/Mehr-als-50-Millionen-Deutsche-nutzen-soziale-Medien
#https://www.who.int/news-room/feature-stories/detail/fighting-misinformation-in-the-time-of-covid-19-one-click-at-a-time
#https://blog.digimind.com/de/covid-die-am-weitesten-verbreiteten-fake-news-in-den-sozialen-medien-in-deutschland
#https://de.statista.com/statistik/daten/studie/1237979/umfrage/glaubwuerdigkeit-von-falschnachrichten-beim-thema-corona-pandemie
#https://pmc.ncbi.nlm.nih.gov/articles/PMC8985560
#https://www.kff.org/health-information-trust/press-release/covid-19-misinformation-is-ubiquitous-78-of-the-public-believes-or-is-unsure-about-at-least-one-false-statement-and-nearly-at-third-believe-at-least-four-of-eight-false-statements-tested
#https://zenodo.org/records/3965871