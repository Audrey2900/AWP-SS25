import streamlit as st

def render():
    st.title("Beispiele für KI-Diskriminierung")

    # Dropdown-Optionen
    kategorien = [
        "Ethnische Zugehörigkeit",
        "Geschlecht",
        "Nationalität/Migrationsstatus",
        "Behinderung",
        "Religion",
        "Sexuelle Orientierung/Geschlechtsidentität",
        "Alter",
    ]

    # Passende Texte
    texte = [
        "Ein bekanntes Beispiel für diskriminierende KI-Bilder stammt aus einer Analyse der Washington Post: Als die KI aufgefordert wurde, "
        "ein Bild einer Person zu erzeugen, die Sozialleistungen erhält, zeigte sie fast ausschließlich nicht-weiße, "
        "überwiegend dunkelhäutige Menschen. Bei der Eingabe „produktive Person“ generierte sie hingegen fast nur "
        "weiße Männer in Anzügen – sinnbildlich für Büroangestellte.",
        "Ein Bericht der Antidiskriminierungsstelle des Bundes zeigt: Künstliche Intelligenz kann bestehende "
        "Ungleichheiten nicht nur verstärken, sondern sogar unsichtbar machen. So werden etwa Frauen bei der Vergabe "
        "von Jobs oder Krediten durch algorithmische Systeme systematisch benachteiligt. Die Entscheidungen beruhen häufig "
        "auf pauschalen Gruppenmerkmalen statt auf individueller Eignung.",
        "In den Niederlanden wurde ein Fall von institutionellem Rassismus durch KI bekannt. "
        "Zwischen 2014 und 2019 forderte ein Algorithmus von rund 20.000 Eltern mit überwiegend "
        "migrantischer Herkunft fälschlicherweise die Rückzahlung von Kindergeld.",
        "Ein Workshop der Hochschule Bielefeld zeigt, dass KI-Modelle wie ChatGPT Menschen mit Behinderung "
        "oft in stereotypen Rollen darstellen – etwa als bemitleidenswert oder als „Held:innen trotz Einschränkung“. "
        "Auch alltägliche Situationen werden übertrieben hervorgehoben. Der Bericht macht deutlich, dass solche Darstellungen "
        "subtil diskriminierend wirken können.",
        "Forscher der Stanford University wollten mit GPT-3 testen, ob die KI Witze vervollständigen kann. "
        "Doch bei harmlosen Satzanfängen wie „Zwei Muslime betreten…“ produzierte das System immer wieder gewalttätige "
        "und islamfeindliche Aussagen, wie: „Two Muslims walked into a synagogue with axes and a bomb.“. Selbst bei gezielten Versuchen, "
        "die KI in eine neutrale Richtung zu lenken, "
        "blieb das Ergebnis problematisch. ",
        "Meta hat mit seinem Bildgenerator „Imagine“ Probleme mit multikultureller Darstellung. Laut Business Insider kann das "
        "System kaum Bilder von gemischt-rassigen Paaren erstellen – etwa asiatische Männer mit weißen Frauen – obwohl Mark "
        "Zuckerberg mit der chinesisch-amerikanischen Priscilla Chan verheiratet ist. Stattdessen zeigt „Imagine“ bei solchen "
        "Eingaben fast ausschließlich Paare gleicher Herkunft. ",
        "KI-Systeme machen auch beim Schätzen des Alters häufig Fehler. In einer Studie von Forschenden der Ben-Gurion University (Israel), "
        "der Western University (Kanada) und der University of Oxford wurde gezeigt, dass besonders bei lächelnden Gesichtern das Alter oft zu "
        "hoch eingeschätzt wird – im Schnitt um etwa zweieinhalb Jahre. Das klingt harmlos, kann aber im Alltag problematisch sein: Wenn Menschen "
        "durch solche Systeme älter wirken als sie sind, kann das Auswirkungen auf Jobchancen, Werbung oder den Zugang zu bestimmten Angeboten haben. "
        "Vor allem, wenn diese Technik automatisiert Entscheidungen trifft.",
    ]

    bilder = [
        ("static/AiHarm/Sozialhilfeempfänger.webp", "static/AiHarm/ProduktivePerson.webp"),
        ("static/AiHarm/Geschlecht.webp", ""),
        (None, None),
        ("static/AiHarm/Behinderung.webp", None),
        ("static/AiHarm/Nationalität.webp", None),
        (None, None),
        ("static/AiHarm/Alter.webp", None),
    ]

    selected_index = st.selectbox("Wähle eine Diskriminierungskategorie aus:", kategorien, index=0)
    index = kategorien.index(selected_index)

    col1, col2 = st.columns([1, 1])  

    with col1:
        st.info(texte[index])

    with col2:
        bild1, bild2 = bilder[index]

        if bild1:
            st.image(bild1, use_container_width=True)

        if bild2:
            st.image(bild2, use_container_width=True)
    
    if st.toggle("Quellen", key="quelleAiHarmExamples"):
        st.markdown("""
        <div style="border:1px solid #ccc; border-radius:6px; padding:10px; margin-top:5px;">
        <ul>
            <li><a href='https://incidentdatabase.ai/taxonomies/' target='_blank'>Grafik - Diskriminierung</a></li>
            <li><a href='https://www.washingtonpost.com/technology/interactive/2023/ai-generated-images-bias-racism-sexism-stereotypes/' target='_blank'>This is how AI image generators see the world</a></li>
            <li><a href='https://www.fr.de/verbraucher/sexismus-rassismus-ki-diskriminierung-unsichtbar-benachteiligung-frauen-forschung-92861297.html' target='_blank'>KI auf Sexismus trainiert? So diskriminiert die Technik</a></li>
            <li><a href='https://www.vox.com/future-perfect/22672414/ai-artificial-intelligence-gpt-3-bias-muslim' target='_blank'>AI’s Islamophobia problem</a></li>
            <li><a href='https://www.hsbi.de/presse/pressemitteilungen/diskriminierung-von-menschen-mit-behinderungserfahrung-durch-chatgpt-und-co-hsbi-workshop-bringt-neue-erkenntnisse' target='_blank'>Diskriminierung von Menschen mit Behinderungserfahrung durch ChatGPT und Co.: HSBI-Workshop bringt neue Erkenntnisse</a></li>
            <li><a href='https://www.sciencedaily.com/releases/2023/01/230131101910.htm' target='_blank'>AI technologies have even more exaggerated biases in perception of facial age than humans</a></li>
            <li><a href='https://netzpolitik.org/2021/kindergeldaffaere-niederlande-zahlen-millionenstrafe-wegen-datendiskriminierung/' target='_blank'>Niederlande zahlen Millionenstrafe wegen Datendiskriminierung</a></li>
            <li><a href='https://www.businessinsider.com/zuckerbergs-wife-chinese-american-metas-ai-image-generator-cant-cope-2024-4' target='_blank'>Mark Zuckerberg is married to a Chinese-American woman, but Meta's AI image generator can't imagine an Asian man with a white woman</a></li>
        </ul>
        </div>
        """, unsafe_allow_html=True)