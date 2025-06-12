import streamlit as st
from data.char_speech_state import set_text_key

def render():
    col1, col2 = st.columns([3, 1])
    with col1:
        st.title("Faktenchecker in Deutschland – Wer prüft die Wahrheit?", anchor="factcheckers")
        st.markdown("""
        Falschinformationen verbreiten sich im Netz oft schneller als echte Nachrichten. Besonders in Krisenzeiten – wie während der Corona-Pandemie – reicht ein viraler Post, und schon glauben tausende Menschen an erfundene Fakten. Doch wer zieht die Notbremse?  
        **Die Antwort lautet: Faktenchecker.**
        """)
        
    with col2:
        st.markdown("""
            <img src="/app/static/factcheckersintro.webp"
            alt="400 Faktenchecker visualisiert"
            style="width: 100%; border-radius: 8px;" />""", 
        unsafe_allow_html=True)    
    

    st.markdown("""
### Was genau machen Faktenchecker?

Faktenchecker sind spezialisierte Journalistinnen und Journalisten, die sich ausschließlich damit beschäftigen, Informationen auf ihren Wahrheitsgehalt zu überprüfen. Sie schauen sich Aussagen an, die öffentlich verbreitet wurden, zum Beispiel in sozialen Netzwerken, Pressemitteilungen oder Interviews, und prüfen, ob diese Aussagen durch überprüfbare Quellen belegt werden können. Dabei geht es nicht um persönliche Meinungen oder politische Haltungen, sondern um konkrete Behauptungen, die entweder richtig oder falsch sind.

Die Arbeitsweise von Faktencheck-Teams ist dabei sehr methodisch. Zuerst wird geprüft, woher eine Aussage stammt, in welchem Zusammenhang sie gemacht wurde und ob sie möglicherweise aus dem Kontext gerissen wurde. Anschließend werden öffentlich zugängliche Datenbanken, wissenschaftliche Studien oder offizielle Stellungnahmen herangezogen. Am Ende steht eine nachvollziehbare Bewertung, bei der erklärt wird, warum eine Aussage stimmt, teilweise richtig oder komplett falsch ist.
""")
    
    st.markdown("<div style='height: 100px;'></div>", unsafe_allow_html=True)

    st.markdown("""
### Wer prüft in Deutschland?

In Deutschland gibt es mehrere professionelle Teams, die regelmäßig Faktenchecks veröffentlichen. Manche arbeiten unabhängig, andere sind Teil großer Nachrichtenagenturen oder öffentlich-rechtlicher Sender. Besonders bekannt ist die Redaktion von **CORRECTIV**. Sie arbeitet gemeinnützig und unabhängig. Das bedeutet, sie finanziert sich über Spenden und nimmt keine Werbung oder Einfluss von außen an.

Auch **AFP Deutschland**, also die deutsche Redaktion der internationalen Nachrichtenagentur Agence France Presse, betreibt ein eigenes Faktencheck-Team.  
Die **Deutsche Presseagentur (dpa)** hat ebenfalls ein spezialisiertes Team aufgebaut, das Falschbehauptungen überprüft. Zusätzlich engagieren sich auch einige öffentlich-rechtliche Sender im Faktencheck: **ARD Faktenfinder**, **BR24 Faktenfuchs**, **MDR Fact Checking Team** und auch **DW Fact Check** von der Deutschen Welle.

Einige dieser Redaktionen arbeiten inzwischen eng zusammen, zum Beispiel im Projekt **GADMO**.
""")
    
    st.button("", on_click=set_text_key, args=("FCwerprüftde", "factcheckers"), key="chat")

    st.markdown("<div style='height: 100px;'></div>", unsafe_allow_html=True)

    st.markdown("""
### Was ist GADMO?

**GADMO** steht für *German Austrian Digital Media Observatory*. Es ist ein Projekt, bei dem mehrere Faktencheck-Teams, Forschungseinrichtungen und Medien gemeinsam gegen Desinformation arbeiten. Ziel ist es, Falschinformationen schneller zu erkennen, besser zu analysieren und wirksam dagegen vorzugehen.

Zum Netzwerk gehören unter anderem CORRECTIV, AFP Deutschland, die dpa, der Bayerische Rundfunk sowie Universitäten wie die TU Dortmund. Auch Partner aus Österreich sind beteiligt. Gemeinsam tauschen sie sich aus, teilen ihre Recherchen und entwickeln Werkzeuge, mit denen sich Falschmeldungen frühzeitig entdecken lassen.

Ein Vorteil von GADMO ist, dass Redaktionen nicht doppelt an derselben Sache arbeiten müssen. Wenn etwa eine Falschmeldung gleichzeitig in mehreren Ländern kursiert, können die Beteiligten ihre Erkenntnisse direkt abstimmen.
""")
    
    st.button("", on_click=set_text_key, args=("FCgadmo",), key="chat2")

    st.markdown("<div style='height: 100px;'></div>", unsafe_allow_html=True)

    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown("""
        ### Wie erkenne ich seriöse Faktenchecker?

        Im Internet gibt es viele, die sich als Faktenchecker bezeichnen. Manche meinen es ernst, andere verbreiten unter diesem Namen ihre eigene Meinung oder politische Agenda. Deshalb ist es wichtig zu wissen, woran man seriöse Faktencheck-Redaktionen erkennen kann.

        Ein gutes Zeichen ist die Mitgliedschaft im **International Fact Checking Network (IFCN)**. Das ist ein weltweites Netzwerk, das Mindeststandards für journalistisches Arbeiten im Faktencheck festgelegt hat.

        Wer Mitglied im IFCN ist, verpflichtet sich unter anderem zu:
        - Unparteilichkeit und Transparenz  
        - Offenlegung der Quellen  
        - Nachvollziehbaren Arbeitsprozessen  
        - Korrektur eigener Fehler

        👉 [Zur Liste der IFCN-Mitglieder](https://ifcncodeofprinciples.poynter.org/signatories)

        Zertifiziert sind über 400 Faktenchecker – darunter auch CORRECTIV, AFP Deutschland, dpa und Deutsche Welle.
        """)

    with col2:
        st.markdown("""
    	    <img src="/app/static/400factcheckingteams.webp"
            alt="400 Faktenchecker visualisiert"
            style="margin-top: 80px; width: 100%; border-radius: 8px;" />""", 
        unsafe_allow_html=True)

    st.components.v1.html("""
        <div style="text-align: center;">
            <img src="/app/static/IFCNcerts.png" style="border-radius: 8px; width: 800px; height: auto; display: block; margin: 20px auto 0 auto;;" />
        </div>
    """, height=360)

    
    st.button("", on_click=set_text_key, args=("FCifcn",), key="chat3")

    st.markdown("<div style='height: 100px;'></div>", unsafe_allow_html=True)

    st.markdown("""
### Faktenchecker und Deepfakes

Auch bei gefälschten Videos kommen Faktenchecker zum Einsatz. Sie analysieren Aufnahmen, bei denen der Verdacht besteht, dass sie manipuliert wurden. Dafür verwenden sie forensische Werkzeuge, mit denen sich z. B. Bildartefakte, Schat4tenverläufe oder Tonspuren untersuchen lassen.

Trotzdem: Je besser die Technik, desto schwerer die Erkennung. Deswegen ist Aufklärung so wichtig – also zu wissen, dass es solche Fälschungen überhaupt gibt und wie sie aussehen können.
""")
    
    st.button("", on_click=set_text_key, args=("FCdeepfakes",), key="chat4")

    st.markdown("<div style='height: 100px;'></div>", unsafe_allow_html=True)

    st.markdown("""
### Faktencheck ≠ Zensur

Manche werfen Faktencheck-Redaktionen vor, sie würden Meinungen verbieten oder die Meinungsfreiheit einschränken. Doch das ist falsch. Faktenchecks richten sich nicht gegen persönliche Haltungen, sondern gegen falsche Aussagen, die als Fakten dargestellt werden.

Ob man eine politische Maßnahme gut oder schlecht findet, bleibt jedem selbst überlassen. Aber ob eine Organisation wie die WHO tatsächlich gesagt hat, dass Cola gegen ein Virus hilft, ist überprüfbar. Und genau an dieser Stelle setzen Faktenchecks an.

> Die Bundesregierung formuliert es so:  
> *„Faktencheck-Redaktionen widerlegen falsche Informationen und helfen so, die öffentliche Debatte auf eine verlässliche Grundlage zu stellen.“*
""")
    
    st.button("", on_click=set_text_key, args=("FCzensur",), key="chat5")

    st.markdown("<div style='height: 100px;'></div>", unsafe_allow_html=True)

    st.markdown("""
### Seit wann gibt es eigentlich Faktenchecker?

Die Idee, Behauptungen auf ihren Wahrheitsgehalt zu überprüfen, ist nicht neu. Schon früher wurden Aussagen von Politikerinnen und Politikern oder Beiträge in Zeitungen kritisch hinterfragt. Was wir heute unter professionellem Faktencheck verstehen, entwickelte sich aber erst in den letzten zwanzig Jahren.

Eine der ersten bekannten Plattformen war **FactCheck.org** aus den USA (2003). Kurz danach entstanden **PolitiFact** und **Full Fact** in Großbritannien.

In Deutschland wurde das Thema ab dem Jahr **2016** präsenter. Vor allem durch den US-Wahlkampf und das Brexit-Votum gerieten digitale Falschinformationen stärker in den Fokus. **CORRECTIV** startete in dieser Zeit als erstes unabhängiges Faktencheck-Team und gehört bis heute zu den zentralen Anlaufstellen im deutschsprachigen Raum.
""")
    
    st.button("", on_click=set_text_key, args=("FCwann",), key="chat6")

    st.button("", on_click=set_text_key, args=("FCaufgabe",), key="chat7")