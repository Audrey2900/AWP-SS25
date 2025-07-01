import streamlit as st
import components.FactCheckersGraph.factcheckersgraph as FactCheckersGraph
import components.FactCheckersQuiz.factcheckersquiz as FactCheckersQuiz
import components.Corruption.corruption as Corruption
from data.char_speech_state import set_text_key
import pathlib

def render():
    col1, col2 = st.columns([3, 1])
    with col1:
        st.title("Faktenchecker in Deutschland – Wer prüft die Wahrheit?", anchor="factcheckers")
        st.markdown("""
        Falschinformationen verbreiten sich im Netz oft schneller als echte Nachrichten. Besonders in Krisenzeiten – wie während der Corona-Pandemie – reicht ein viraler Post, und schon glauben tausende Menschen an erfundene Fakten. Doch wer zieht die Notbremse?  
        **Die Antwort lautet: Faktenchecker.**
        """)
        
    with col2:
        img_path = pathlib.Path(__file__).parent / "factcheckers_pic" / "factcheckersintro.webp"
        st.image(str(img_path), use_container_width=True)    
    

    st.markdown("""
### Was genau machen Faktenchecker?

Faktenchecker sind spezialisierte Journalistinnen und Journalisten, die sich ausschließlich damit beschäftigen, Informationen auf ihren Wahrheitsgehalt zu überprüfen. Sie schauen sich Aussagen an, die öffentlich verbreitet wurden, zum Beispiel in sozialen Netzwerken, Pressemitteilungen oder Interviews, und prüfen, ob diese Aussagen durch überprüfbare Quellen belegt werden können. Dabei geht es nicht um persönliche Meinungen oder politische Haltungen, sondern um konkrete Behauptungen, die entweder richtig oder falsch sind.

Die Arbeitsweise von Faktencheck-Teams ist dabei sehr methodisch. Zuerst wird geprüft, woher eine Aussage stammt, in welchem Zusammenhang sie gemacht wurde und ob sie möglicherweise aus dem Kontext gerissen wurde. Anschließend werden öffentlich zugängliche Datenbanken, wissenschaftliche Studien oder offizielle Stellungnahmen herangezogen. Am Ende steht eine nachvollziehbare Bewertung, bei der erklärt wird, warum eine Aussage stimmt, teilweise richtig oder komplett falsch ist.
""")
    
    st.markdown("<div style='height: 50px;'></div>", unsafe_allow_html=True)

    st.markdown("""
### Wer prüft in Deutschland?

In Deutschland gibt es mehrere professionelle Teams, die regelmäßig Faktenchecks veröffentlichen. Manche arbeiten unabhängig, andere sind Teil großer Nachrichtenagenturen oder öffentlich-rechtlicher Sender. Besonders bekannt ist die Redaktion von **CORRECTIV**. Sie arbeitet gemeinnützig und unabhängig. Das bedeutet, sie finanziert sich über Spenden und nimmt keine Werbung oder Einfluss von außen an.

Auch **AFP Faktencheck Deutschland**, also die deutsche Redaktion der internationalen Nachrichtenagentur Agence France Presse, betreibt ein eigenes Faktencheck-Team.  
Die **Deutsche Presseagentur (dpa)** hat ebenfalls ein spezialisiertes Team aufgebaut, das Falschbehauptungen überprüft. Zusätzlich engagieren sich auch einige öffentlich-rechtliche Sender im Faktencheck: **ARD Faktenfinder**, **BR24 Faktenfuchs**, **MDR Fact Checking Team** und auch **DW Fact Check** von der Deutschen Welle.

Einige dieser Redaktionen arbeiten inzwischen eng zusammen, zum Beispiel im Projekt **GADMO**.
""")
    
    st.button("", on_click=set_text_key, args=("FCwerprüftde", "factcheckers"), key="chat")

    st.markdown("<div style='height: 50px;'></div>", unsafe_allow_html=True)

    st.markdown("""
### Was ist GADMO?

**GADMO** steht für *German Austrian Digital Media Observatory*. Es ist ein Projekt, bei dem mehrere Faktencheck-Teams, Forschungseinrichtungen und Medien gemeinsam gegen Desinformation arbeiten. Ziel ist es, Falschinformationen schneller zu erkennen, besser zu analysieren und wirksam dagegen vorzugehen.

Zum Netzwerk gehören unter anderem CORRECTIV, AFP Deutschland, die dpa, der Bayerische Rundfunk sowie Universitäten wie die TU Dortmund. Auch Partner aus Österreich sind beteiligt. Gemeinsam tauschen sie sich aus, teilen ihre Recherchen und entwickeln Werkzeuge, mit denen sich Falschmeldungen frühzeitig entdecken lassen.

Ein Vorteil von GADMO ist, dass Redaktionen nicht doppelt an derselben Sache arbeiten müssen. Wenn etwa eine Falschmeldung gleichzeitig in mehreren Ländern kursiert, können die Beteiligten ihre Erkenntnisse direkt abstimmen.
""")
    
    st.button("", on_click=set_text_key, args=("FCgadmo",), key="chat2")

    st.markdown("<div style='height: 50px;'></div>", unsafe_allow_html=True)

    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown("""
        ### Wie erkenne ich seriöse Faktenchecker?

        Im Internet gibt es viele, die sich als Faktenchecker bezeichnen. Manche meinen es ernst, andere verbreiten unter diesem Namen ihre eigene Meinung oder politische Agenda. Deshalb ist es wichtig zu wissen, woran man seriöse Faktencheck-Redaktionen erkennen kann.

        Allgemein gibt es über 400 seriöse Fact-Checking-Projekte, jedoch ist ein gutes Zeichen die 
        Mitgliedschaft im **International Fact Checking Network (IFCN)**. Das ist ein weltweites Netzwerk, das Mindeststandards für journalistisches Arbeiten im Faktencheck festgelegt hat.

        Wer Mitglied im IFCN ist, verpflichtet sich unter anderem zu:
        - Unparteilichkeit und Transparenz  
        - Offenlegung der Quellen  
        - Nachvollziehbaren Arbeitsprozessen  
        - Korrektur eigener Fehler

        👉 [Zur Liste der IFCN-Mitglieder](https://ifcncodeofprinciples.poynter.org/signatories)

        Zertifiziert sind über 150 Faktenchecker – darunter auch CORRECTIV, AFP Deutschland, dpa und Deutsche Welle. 
                    
    
        """)

    with col2:
        img_path2 = pathlib.Path(__file__).parent / "factcheckers_pic" / "400FactCheckingTeams.webp"
        st.image(str(img_path2), use_container_width=True)
    
    st.button("", on_click=set_text_key, args=("FCifcn",), key="chat3")

    img_path3 = pathlib.Path(__file__).parent / "factcheckers_pic" / "IFCNcerts.png"
    st.image(str(img_path3), use_container_width=True)

    FactCheckersGraph.render()

    st.markdown("<div style='height: 50px;'></div>", unsafe_allow_html=True)

    st.markdown("""
### Faktenchecker und Deepfakes

Auch bei gefälschten Videos kommen Faktenchecker zum Einsatz. Sie analysieren Aufnahmen, bei denen der Verdacht besteht, dass sie manipuliert wurden. Dafür verwenden sie forensische Werkzeuge, mit denen sich z. B. Bildartefakte, Schattenverläufe oder Tonspuren untersuchen lassen.

Trotzdem: Je besser die Technik, desto schwerer die Erkennung. Deswegen ist Aufklärung so wichtig – also zu wissen, dass es solche Fälschungen überhaupt gibt und wie sie aussehen können.
""")
    
    st.button("", on_click=set_text_key, args=("FCdeepfakes",), key="chat4")

    st.markdown("<div style='height: 50px;'></div>", unsafe_allow_html=True)

    st.markdown("""
### Faktencheck ≠ Zensur

Manche werfen Faktencheck-Redaktionen vor, sie würden Meinungen verbieten oder die Meinungsfreiheit einschränken. Doch das ist falsch. Faktenchecks richten sich nicht gegen persönliche Haltungen, sondern gegen falsche Aussagen, die als Fakten dargestellt werden.

Ob man eine politische Maßnahme gut oder schlecht findet, bleibt jedem selbst überlassen. Aber ob eine Organisation wie die WHO tatsächlich gesagt hat, dass Cola gegen ein Virus hilft, ist überprüfbar. Und genau an dieser Stelle setzen Faktenchecks an.

> Die Bundesregierung formuliert es so:  
> *„Faktencheck-Redaktionen widerlegen falsche Informationen und helfen so, die öffentliche Debatte auf eine verlässliche Grundlage zu stellen.“*
""")
    
    st.button("", on_click=set_text_key, args=("FCzensur",), key="chat5")

    st.markdown("<div style='height: 50px;'></div>", unsafe_allow_html=True)

    st.markdown("""
### Seit wann gibt es eigentlich Faktenchecker?

Die Idee, Behauptungen auf ihren Wahrheitsgehalt zu überprüfen, ist nicht neu. Schon früher wurden Aussagen von Politikerinnen und Politikern oder Beiträge in Zeitungen kritisch hinterfragt. Was wir heute unter professionellem Faktencheck verstehen, entwickelte sich aber erst in den letzten zwanzig Jahren.

Eine der ersten bekannten Plattformen war **FactCheck.org** aus den USA (2003). Kurz danach entstanden **PolitiFact** und **Full Fact** in Großbritannien.

In Deutschland wurde das Thema ab dem Jahr **2016** präsenter. Vor allem durch den US-Wahlkampf und das Brexit-Votum gerieten digitale Falschinformationen stärker in den Fokus. **CORRECTIV** startete in dieser Zeit als erstes unabhängiges Faktencheck-Team und gehört bis heute zu den zentralen Anlaufstellen im deutschsprachigen Raum.
""")
    if st.toggle("Quellen", key="quelleFactCheckers"):
        st.markdown("""
        <div style="border:1px solid #ccc; border-radius:6px; padding:10px; margin-top:5px;">
        <ul>
            <li><a href='https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Informationen-und-Empfehlungen/Kuenstliche-Intelligenz/Deepfakes/deepfakes_node.html#doc1009562bodyText6' target='_blank'>Deepfakes - Gefahren und Gegenmaßnahmen</a></li>
            <li><a href='https://www.bundesregierung.de/breg-de/aktuelles/desinformation-erkennen-1750146' target='_blank'>Woran Sie Desinformation erkennen können</a></li>
            <li><a href='https://www.bundesregierung.de/breg-de/service/archiv-bundesregierung/die-arbeit-der-faktenchecker-2081802' target='_blank'>Die Arbeit der Faktenchecker</a></li>
            <li><a href='https://euvsdisinfo.eu/de/' target='_blank'>https://euvsdisinfo.eu/de/</a></li>
            <li><a href='https://ifcncodeofprinciples.poynter.org/' target='_blank'>https://ifcncodeofprinciples.poynter.org/</a></li>
            <li><a href='https://gadmo.eu/' target='_blank'>https://gadmo.eu/</a></li>
            <li><a href='https://en.wikipedia.org/wiki/FactCheck.org' target='_blank'>https://en.wikipedia.org/wiki/FactCheck.org</a></li>
            <li><a href='https://de.wikipedia.org/wiki/Correctiv' target='_blank'>https://de.wikipedia.org/wiki/Correctiv</a></li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

    st.button("", on_click=set_text_key, args=("FCwann",), key="chat6")

    st.markdown("<div style='height: 50px;'></div>", unsafe_allow_html=True)
    st.markdown('<div id="AnchorFCQuizDone"></div>', unsafe_allow_html=True)

    if st.session_state.ui_state["FCQuizDone"] == False:
        st.button("", on_click=set_text_key, args=("FCaufgabe", "FCQuiz"), key="chat7")
        if (
            st.session_state.text_key == "FCaufgabe" and st.session_state.text_index == 3
        ) or st.session_state.ui_state["FCQuiz"]:
            st.session_state.ui_state["FCQuiz"] = True
            FactCheckersQuiz.render()

    if st.session_state.ui_state["NoCorruptionFaktenChecker"] == False:
        Corruption.render()