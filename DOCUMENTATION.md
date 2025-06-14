## Inhaltsverzeichnis
1. Projektübersicht und Ziel des Projekts
2. Fachliche Komponenten
3. Technische Komponenten
4. Installation und Setup
5. Datenmodell und -verarbeitung
6. Komponenten-Details
7. Herausforderungen und Lösungen
8. Erweiterungsmöglichkeiten
9. Anhang und Referenzen

## Projektübersicht und Ziel des Projekts

Das Projekt "Fake News Visualisierung & Aufklärung" ist eine interaktive Webanwendung, die mit Streamlit und Python entwickelt wurde. Es bietet verschiedene interaktive Elemente zur Aufklärung über Desinformation. Die Anwendung dient Bildungszwecken und soll Nutzer:innen für die Problematik von Fake News sensibilisieren.

### Hauptfunktionen

#### Interaktives Dashboard
- **Funktionalität**: Filtermöglichkeiten nach Ländern, Monaten, Kategorien, Sprachen, Klassifikationen und Wordcloud
- **Nutzen**: Ermöglicht die gezielte Analyse von Fake-News-Daten nach verschiedenen Kriterien
- **Umsetzung**: Streamlit-Buttons und Seitenleiste mit Session-State zur Filterung

#### Animierte Diagramme
- **Funktionalität**: Automatisch ablaufende Balkendiagramme zur Veranschaulichung von Trends
- **Nutzen**: Dynamische Darstellung von Datenentwicklungen und Verhältnissen
- **Besonderheit**: HTML/CSS/JS-Integration für flüssige Animationen

#### Bildauswahl- und Kombinationsspiel (PictureSelector)
- **Funktionalität**: Interaktive Kombination von Personen und Fake-News-Schlagzeilen
- **Nutzen**: Spielerische Auseinandersetzung mit absurden Falschmeldungen

#### Aufklappbare Info-Boxen (CoronaExpanders)
- **Funktionalität**: Übersicht und detaillierte Erläuterung bekannter Corona-Verschwörungstheorien
- **Nutzen**: Kompakte Aufbereitung von Fakten zu verbreiteten Falschinformationen

#### 3D-Weltkarte
- **Funktionalität**: Interaktive Darstellung der globalen Fake-News-Verteilung
- **Nutzen**: Geografische Einordnung und Schwerpunktanalyse
- **Technologie**: Plotly-3D-Globe mit Länderdaten

#### Statistische Metriken
- **Funktionalität**: Anzeige von Kennzahlen wie Anzahl der Länder, häufigste Fake-News-Kategorien etc.
- **Nutzen**: Schneller Überblick über die wichtigsten Daten auf einen Blick

### Datenquellen
- **FakeCovid_July2020.csv**: Hauptdatensatz mit Fake-News-Artikeln
  - Enthält Informationen zu Kategorien, Ländern, Sprachen, Veröffentlichungsdatum, Quellen, Faktencheckern und weiteren Attributen
  - Umfasst mehrere tausend Einträge aus dem Zeitraum der frühen Corona-Pandemie
  - Struktur: ID, Titel, Text, Quelle, Land, Sprache, Kategorie, Veröffentlichungsdatum, Faktencheck-Status

### Nutzerinteraktionen
- **Daten filtern**: Auswahl verschiedener Ansichten im Dashboard durch Button-Navigation
- **Visualisierungen erkunden**: Interaktion mit Diagrammen durch Hover, Zoom und Filterung
- **Spielerische Elemente**: Kombination von Bildern und Texten im PictureSelector
- **Informationen abrufen**: Auf- und Zuklappen von Expander-Elementen zu Verschwörungstheorien
- **Geografische Exploration**: Drehen und Zoomen der 3D-Weltkarte

## Technische Komponenten

### Systemarchitektur

Das Projekt folgt einer modularen Struktur mit klar getrennten Komponenten:

```
AWP-SS25/
├── app.py                    # Haupt-Einstiegspunkt der Anwendung
├── static/                   # Statische Dateien
│   ├── FakeCovid_July2020.csv # Hauptdatensatz
│   └── styles/               # CSS-Dateien
├── visuals/                  # Visualisierungskomponenten
│   └── mission1.py           # Grundlegende Visualisierungsfunktionen
├── components/               # Wiederverwendbare UI-Komponenten
│   ├── CoronaMiniDashboard/  # Dashboard-Komponente
│   ├── CoronaExpanders/      # Expander-Komponente
│   ├── chart_animation/      # Animierte Charts
│   └── PictureSelector/      # Bild-Auswahl-Komponente
└── zones/                    # Inhaltsbereiche der Anwendung
    └── corona.py             # Corona-spezifische Inhalte
usw.
```

### Backend (Python)

#### mission1.py
- **Funktionalität**: Enthält alle grundlegenden Visualisierungsfunktionen
- **Wichtige Funktionen**:
  - `show_country_chart(df)`: Erstellt 3D-Weltkugel mit Fake-News-Verteilung
  - `show_monthly_chart(df)`: Zeitlicher Verlauf der Fake-News
  - `show_category_chart(df)`: Balkendiagramm der Fake-News-Kategorien
  - `show_language_chart(df)`: Sprachenverteilung der Fake-News
  - `show_classification_chart(df)`: Klassifikation nach Arten von Fake-News
- **Technologie**: Hauptsächlich Plotly für interaktive Visualisierungen

#### minidashboard.py
- **Funktionalität**: Steuert das Hauptdashboard, Navigation und Auswahl der Visualisierungen
- **Besonderheiten**:
  - Verwendet Streamlit Session State für persistente Auswahlzustände
  - Zweispaltiges Layout mit Navigationsbutttons links, Visualisierungen rechts
  - Integriert alle Visualisierungsfunktionen aus mission1.py
- **Datenverarbeitung**: Lädt CSV-Daten mit Caching für Performanzoptimierung

#### coronaexpanders.py
- **Funktionalität**: Stellt die Info-Expander zu Verschwörungstheorien bereit
- **Inhalte**: Informationen zu gängigen Corona-Mythen wie:
  - 5G-Mobilfunk und COVID-19
  - Bill Gates und Impf-Mikrochips
  - COVID-19 vs. Grippe-Vergleiche
  - Corona als Biowaffe/Schwindel
  - Vitamin C als angebliches Heilmittel
- **Design**: Formatierte Expander mit angepasstem CSS für bessere Lesbarkeit

#### chartanimation.py
- **Funktionalität**: Erweiterte Visualisierungskomponente für animierte Diagramme
- **Besonderheiten**:
  - Nutzt Streamlit Components und HTML-Injection zur Animation
  - Auto-Play-Funktion für automatischen Start der Animationen
  - Angepasstes CSS zum Ausblenden von Steuerungselementen
  - Optimierte Frame-Raten für flüssige Darstellung

#### corona.py
- **Funktionalität**: Hauptseite für Corona-Fake-News mit Text und integrierten Komponenten
- **Inhalte**: Erläuternde Texte zu Fake News während der Pandemie
- **Integration**: Bindet CoronaExpanders und andere Komponenten ein

### Frontend (CSS/JS)

#### styles.css
- **Funktionalität**: Styling für das Bildauswahlspiel
- **Design-Elemente**:
  - Dunkles Farbschema als Hintergrund
  - Helle Ränder für Kontrast
  - Responsive Layout mit flexiblen Komponenten
  - Einheitliche Bildgrößen und -abstände
  - Weiße Textfarben für bessere Lesbarkeit
- **Besonderheiten**: Angepasstes Styling für Bilderrahmen, Auswahleffekte und Anzeige der kombinierten Elemente

#### config.toml
- **Funktionalität**: Globale Streamlit-Konfiguration
- **Einstellungen**:
  - Dark Mode als Basis-Theme
  - Minimale Toolbar
  - Versteckte obere Leiste
  - Aktiviertes statisches Serving

### Datenmodell und -verarbeitung

#### FakeCovid_July2020.csv
- **Struktur**: Tabellendaten mit mehreren Spalten:
  - `published_date`: Datum der Veröffentlichung
  - `country`: Ursprungsland der Fake News
  - `lang`: Sprache des Artikels
  - `category`: Thematische Kategorie (z.B. Politik, Gesundheit)
  - `class`: Klassifikation der Fake News (z.B. Falschinformation, Verschwörungstheorie)
  - weitere Felder mit Details zu Quellen, Faktencheckern etc.

#### Datenverarbeitung
- **Vorverarbeitung**:
  - Datumsumwandlung mit Pandas für zeitliche Analysen
  - Gruppierung und Aggregation für verschiedene Visualisierungen
  - Normalisierung für prozentuale Darstellungen
- **Caching**:
  - Nutzung von `@st.cache_data` für schnelles Nachladen
  - Vermeidung wiederholter CSV-Verarbeitung

### Bibliotheken und Dependencies

- **Streamlit (v1.27+)**: UI-Framework für die gesamte Webanwendung
  - Verwendet für interaktive Elemente, Layouts und Komponenten
- **Plotly (v5.18+)**: Erstellung interaktiver und animierter Diagramme
  - 3D-Globus, Balkendiagramme, Zeitreihen
- **Pandas (v2.0+)**: Datenverarbeitung und -analyse
  - Dataframe-Operationen, Gruppierung, Aggregation, Zeitreihenanalyse
- **Streamlit Components v1**: Integration eigener HTML/JS/CSS-Komponenten
  - Verwendet für PictureSelector und animierte Diagramme

## Installation und Setup siehe auch README.md

### Voraussetzungen
- Python 3.10 oder höher
- pip (Paketmanager)
- Git (optional, für Projekt-Klonen)

### Installation
1. Repository klonen oder als ZIP herunterladen
2. Virtuelle Umgebung erstellen (empfohlen):
   ```
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   source .venv/bin/activate  # Unix/Mac
   ```
3. Dependencies installieren:
   ```
   pip install -r requirements.txt
   ```

### Ausführung
```
streamlit run app.py
```
Die Anwendung ist dann unter http://localhost:8501 erreichbar.

## Komponenten-Details

### Animierte Diagramme

Die animierten Diagramme in `chartanimation.py` verwenden HTML/JS-Injection mit Plotly, um automatisch startende Animationen zu erzeugen:

### PictureSelector

Der PictureSelector bietet ein spielerisches Element, bei dem Nutzer:innen Personen und Aktionen kombinieren können:

1. Frontend in HTML/CSS/JS
2. Integration in Streamlit via IFrame oder Components
3. Angepasstes Styling mit dunklem Hintergrund und hellen Akzenten

## Herausforderungen und Lösungen

### 1. Automatische Animation in Streamlit

**Herausforderung**: Streamlit bietet keine native Unterstützung für automatisch startende Plotly-Animationen.

**Lösung**: Nutzung von HTML-Injection mit `components.html()` und angepasstem JavaScript/CSS, um Steuerelemente auszublenden und Auto-Play zu erzwingen.

### 2. Dark Mode mit konsistentem Design

**Herausforderung**: Streamlit-Komponenten und eigene HTML-Elemente im einheitlichen Dark Mode darstellen.

**Lösung**: Globales Theme in config.toml und manuelle CSS-Anpassungen für Custom Components.

### 3. Responsive Layout für verschiedene Bildschirmgrößen

**Herausforderung**: Konsistente Darstellung auf verschiedenen Geräten.

**Lösung**: Relative Einheiten (%, vh) und Flexbox-Layout für bessere Anpassungsfähigkeit.

## Erweiterungsmöglichkeiten

...

## Anhang und Referenzen

### Nützliche Ressourcen
- [Streamlit Dokumentation](https://docs.streamlit.io/)
- [Plotly Python Dokumentation](https://plotly.com/python/)
- [Pandas Dokumentation](https://pandas.pydata.org/docs/)

### Projekthistorie und Meilensteine
- **April 2025**: Projektstart, Konzeption
- **Juni 2025**: Entwicklung der Kernkomponenten
- **Juli 2025**: Fertigstellung sowie Kundenübernahme
- **11. Juni 2025**: Dokumentation 

---

**Stand:** 11. Juni 2025  
**Autor:** Luca Breisinger