import streamlit as st

def render():
    col1, col2, col3 = st.columns(3)
    with col1:
        with st.expander("**5G-Mobilfunk verursacht COVID-19**"):
            st.write("Eine absurde Behauptung machte 2020 die Runde: 5G-Mobilfunkstrahlen würden das Coronavirus übertragen oder das Immunsystem schwächen. Die Theorie verbreitete sich rasant über soziale Medien, vor allem in Großbritannien und den USA – mit teils drastischen Folgen: Mobilfunkmasten wurden angezündet, Techniker bedroht. Wissenschaftlich ist die Aussage völlig unbegründet – Viren werden durch Tröpfchen, nicht durch Funkwellen übertragen. Trotzdem hielt sich der Mythos hartnäckig und heizte Ängste weiter an.")
    with col2:
        with st.expander("**Bill Gates plant, Mikrochips über Impfungen zu implantieren**"):
            st.write("Bill Gates wurde zur Zielscheibe vieler Corona-Verschwörungen. Eine besonders verbreitete Lüge: Er wolle durch Impfstoffe Ortungs-Chips implantieren. Obwohl völlig haltlos, glaubten in den USA 44 % der Republikaner daran. Auch in Deutschland verbreiteten Blogs Falschbehauptungen über Patente und angebliche Pandemie-Pläne von Gates.")
    with col3:
        with st.expander("**COVID-19 ist nicht schlimmer als die Grippe**"):
            st.write("Viele Falschmeldungen stellten COVID-19 als harmlos dar. Die verbreitete Aussage, Corona sei „wie eine normale Grippe“, wurde millionenfach geteilt, oft zur Ablehnung von Maßnahmen wie Masken oder Lockdowns. Wissenschaftlich ist das falsch: Vor den Impfstoffen hatte COVID-19 deutlich höhere Sterbe- und Hospitalisierungsraten. Dennoch hielten laut einer Umfrage 60 % der 14–24-Jährigen 2020 Corona nicht für gefährlicher als Grippe – ein weitverbreiteter Irrglaube.")

    col4, col5, col6 = st.columns(3)
    with col4:
        with st.expander("**Geheimplan: Corona als Schwindel oder Biowaffe**"):
            st.write("Zwei widersprüchliche Theorien verbreiteten sich gleichzeitig: Corona sei entweder ein erfundener Schwindel („Plandemie“) oder absichtlich im Labor erschaffen. Laut einer deutschen Studie 2021 hielten 15 % Corona für erfunden, 11 % für eine Biowaffe – und 9 % glaubten beidem. Solche Mythen untergraben Vertrauen in Staat und Wissenschaft und verstärken Ängste und Wut.")
    with col5:
        with st.expander("**Vitamin C in Mega-Dosis heilt COVID-19**"):
            st.write("Neben drastischen Mitteln wie Bleichmittel kursierten auch scheinbar harmlose Ratschläge: Mega-Dosen von Vitamin C oder D sollten vor oder gegen COVID helfen – teils intravenös. Bis heute gibt es keine Belege für einen medizinischen Nutzen. Solche Empfehlungen wiegten Menschen in falscher Sicherheit und schadeten eher.")