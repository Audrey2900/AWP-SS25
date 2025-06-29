# DOKUMENTATION: FAKE NEWS VISUALISIERUNG & AUFKLÄRUNG

## Inhaltsverzeichnis

1. Projektübersicht und Ziel des Projekts
2. Fachliche Komponenten
3. Technische Komponenten
4. Installation und Setup  
4.1 !WICHTIG! Code-Anpassung für Streamlit Cloud und lokales Deployment (Bildpfade)
5. Code-Logik und zentrale Funktionen
5.1 Datenmodell und -verarbeitung
5.2 Wichtige Funktionen
5.3 Praktische Anwendung & Spezialfunktionen
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
- **Update Juni 2025**: Optimiertes Layout mit gleichmäßig verteilten Buttons über die gesamte Container-Höhe

#### Animierte Diagramme

- **Funktionalität**: Automatisch ablaufende Balkendiagramme zur Veranschaulichung von Trends
- **Nutzen**: Dynamische Darstellung von Datenentwicklungen und Verhältnissen
- **Besonderheit**: HTML/CSS/JS-Integration für flüssige Animationen
- **Update Juni 2025**: Verbesserte Performance mit optimierten Timing-Parametern (60ms pro Frame) für flüssigere Animationen

#### Bildauswahl- und Kombinationsspiel (PictureSelector)

- **Funktionalität**: Interaktive Kombination von Personen und Fake-News-Schlagzeilen
- **Nutzen**: Spielerische Auseinandersetzung mit absurden Falschmeldungen
- **Update Juni 2025**: Bilder werden jetzt aus dem Ordner `pictureGeneration` geladen mit einheitlicher Bildgröße

#### Aufklappbare Info-Boxen (CoronaExpanders)

- **Funktionalität**: Übersicht und detaillierte Erläuterung bekannter Corona-Verschwörungstheorien
- **Nutzen**: Kompakte Aufbereitung von Fakten zu verbreiteten Falschinformationen

#### 3D-Weltkarte

- **Funktionalität**: Interaktive Darstellung der globalen Fake-News-Verteilung
- **Nutzen**: Geografische Einordnung und Schwerpunktanalyse
- **Technologie**: Plotly-3D-Globe mit Länderdaten
- **Update Juni 2025**: Größere Darstellung (400px Höhe) und verbessertes dunkles Theme für konsistente Darstellung

#### Statistische Metriken

- **Funktionalität**: Anzeige von Kennzahlen wie Anzahl der Länder, häufigste Fake-News-Kategorien etc.
- **Nutzen**: Schneller Überblick über die wichtigsten Daten auf einen Blick

#### Interaktive Quiz-Komponenten (Neu)

- **Funktionalität**: Interaktive Wissenstests zu Corona-Fake-News und Faktencheckern
- **Nutzen**: Spielerische Wissensüberprüfung mit sofortigem Feedback
- **Besonderheit**: Automatische Auswertung und Anzeige der korrekten Antworten

#### Deepfake-Erkennung (Mission 3) (Neu)

- **Funktionalität**: Interaktive Übung zur Unterscheidung echter und KI-generierter Bilder
- **Nutzen**: Sensibilisierung für KI-generierte Inhalte
- **Besonderheit**: Bilder werden auf einheitliche Größe (350x250px) gebracht für konsistente Darstellung

#### Faktenchecker-Bereich (Neu)

- **Funktionalität**: Informationen über Arbeit und Geschichte von Faktencheckern
- **Nutzen**: Aufklärung über wichtige Instanzen der Fake-News-Bekämpfung
- **Besonderheit**: Integriertes Quiz zur Überprüfung des Verständnisses

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
- **Wissen testen**: Beantwortung von Quiz-Fragen mit direktem Feedback (Neu)
- **Bilderkennung**: Unterscheidung echter und KI-generierter Bilder (Neu)

## Technische Komponenten

### Systemarchitektur

Das Projekt folgt einer modularen Struktur mit klar getrennten Komponenten:

```
AWP-SS25/
├── app.py                    # Haupt-Einstiegspunkt der Anwendung
├── static/                   # Statische Dateien
│   ├── FakeCovid_July2020.csv # Hauptdatensatz
│   ├── styles/               # CSS-Dateien
│   ├── pictureGeneration/    # Bilder für den PictureSelector (Neu)
│   ├── Original_Bilder/      # Echte Bilder für Deepfake-Erkennung (Neu)
│   └── KI_Bilder/            # KI-generierte Bilder für Vergleich (Neu)
├── visuals/                  # Visualisierungskomponenten
│   └── mission1.py           # Grundlegende Visualisierungsfunktionen
├── components/               # Wiederverwendbare UI-Komponenten
│   ├── CoronaMiniDashboard/  # Dashboard-Komponente
│   ├── CoronaExpanders/      # Expander-Komponente
│   ├── CoronaQuiz/           # Quiz-Komponente (Neu)
│   ├── chart_animation/      # Animierte Charts
│   └── PictureSelector/      # Bild-Auswahl-Komponente
└── zones/                    # Inhaltsbereiche der Anwendung
    ├── corona.py             # Corona-spezifische Inhalte
    ├── Mission_3.py          # Deepfake-Erkennungsaufgabe (Neu)
    └── factcheckers.py       # Bereich zu Faktencheckern (Neu)
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
- **Update Juni 2025**: Konsistentes dunkles Theme (`template="plotly_dark"`) und erweiterte Größenoptionen

#### minidashboard.py

- **Funktionalität**: Steuert das Hauptdashboard, Navigation und Auswahl der Visualisierungen
- **Besonderheiten**:
  - Verwendet Streamlit Session State für persistente Auswahlzustände
  - Zweispaltiges Layout mit Navigationsbutttons links, Visualisierungen rechts
  - Integriert alle Visualisierungsfunktionen aus mission1.py
- **Datenverarbeitung**: Lädt CSV-Daten mit Caching für Performanzoptimierung
- **Update Juni 2025**: Optimiertes Button-Layout mit CSS für gleichmäßige vertikale Verteilung

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
- **Update Juni 2025**: Performance-Optimierung mit verbesserten Timing-Parametern:
  - `frame_duration` auf 60ms reduziert
  - `transition_duration` auf 30ms reduziert
  - Animation bleibt flüssig, läuft aber schneller ab

#### corona.py

- **Funktionalität**: Hauptseite für Corona-Fake-News mit Text und integrierten Komponenten
- **Inhalte**: Erläuternde Texte zu Fake News während der Pandemie
- **Integration**: Bindet CoronaExpanders und andere Komponenten ein
- **Update Juni 2025**: Integration des neuen Corona-Quiz und verbesserter Visualisierungen

#### Mission_3.py (Neu)

- **Funktionalität**: Deepfake-Erkennungsaufgabe
- **Besonderheiten**:
  - Lädt Bilder aus zwei Ordnern (echt/KI-generiert)
  - Verarbeitet Bilder zu einheitlicher Größe (350x250px)
  - Implementiert ein Bewertungssystem für Nutzerantworten
  - Dynamische Fortschrittsanzeige der Ergebnisse

#### factcheckers.py (Neu)

- **Funktionalität**: Informationsseite zu Faktencheckern
- **Inhalte**: Geschichte, Arbeit und Bedeutung von Faktencheckern
- **Besonderheiten**: Integration eines Wissensquiz mit automatischer Auswertung

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

## Code-Logik und zentrale Funktionen

### 5.1 Datenmodell und -verarbeitung

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
- **Bildverarbeitung (Neu)**:
  - Standardisierung von Bildgrößen und -formaten
  - Zentrale Ausrichtung für konsistentes Layout

### Bibliotheken und Dependencies

- **Streamlit (v1.27+)**: UI-Framework für die gesamte Webanwendung
  - Verwendet für interaktive Elemente, Layouts und Komponenten
- **Plotly (v5.18+)**: Erstellung interaktiver und animierter Diagramme
  - 3D-Globus, Balkendiagramme, Zeitreihen
- **Pandas (v2.0+)**: Datenverarbeitung und -analyse
  - Dataframe-Operationen, Gruppierung, Aggregation, Zeitreihenanalyse
- **Streamlit Components v1**: Integration eigener HTML/JS/CSS-Komponenten
  - Verwendet für PictureSelector und animierte Diagramme
- **Pillow (v10.0+)**: Bildverarbeitung für standardisierte Bildgrößen (Neu)

## 5.2 Wichtige Funktionen

### `data/bubble_texts.py`

In dieser Datei ist das gesamte **Skript des Charakters** als Dictionary `BUBBLE_TEXTS` gespeichert.  
Die Texte sind in thematische Blöcke unterteilt, z. B. `"onboarding"`, `"test"`, `"onboarding2"`.  
Jeder Block enthält eine Liste von Strings, die nacheinander in der Sprechblase angezeigt werden.

---

### `data/char_speech_state.py`

#### `init_char_speech_state()`

Initialisiert die relevanten Streamlit-Zustände für die Sprechblase:

- `bubble_text`: ein optionaler Starttext
- `text_index`: Position innerhalb des aktuellen Textblocks
- `text_key`: aktueller Textblock-Schlüssel (z. B. `"onboarding"`)

#### `set_text_key(key: str, zone: str = None)`

Wechselt zu einem anderen Textblock. Zusätzlich:

- wird `text_index` auf `0` zurückgesetzt
- `typewriter_refresh` erhöht (für die Animation)
- bei Übergabe eines `zone`-Namens wird `set_zone(...)` aufgerufen

---

### `data/zone_anchor.py`

#### `init_zone_state()`

Initialisiert die Zustände zur Bereichssteuerung:

- `visited_zones`: Menge aller besuchten Zonen
- `current_zone`: aktuell aktive Zone

#### `set_zone(name: str)`

Aktualisiert `current_zone` und fügt die Zone zu `visited_zones` hinzu – nur, wenn sie noch nicht besucht wurde. Dadurch kann das Sprungziel vom Auge-Button angepasst werden

#### `autojump(anchor_id: str)`

Scrollt per JavaScript automatisch zu einem HTML-Element mit der entsprechenden `id`.  
> Hinweis: Bei sofortigem Triggern nach einem Zonenwechsel sollte `time.sleep(1.5)` verwendet werden, um ein Überspringen durch das Neuladen (Rerun) zu verhindern.

> Hinweis: Verlässlich, solange das Sprungziel sich zwischen dem Aufruf verändert hat. Streamlit blockiert manchmal diesen Funktionsaufruf, wenn das Sprungziel sich nicht verändert hat.

---

### `data/ui_states.py`

#### `init_ui_state()`

Legt im `st.session_state` das Dictionary `ui_state` an, in dem für alle definierten UI-Komponenten der Zustand (`True`/`False`) gespeichert wird.  
Die enthaltenen Schlüssel betreffen z. B.:

- abgeschlossene Aufgaben (`CoronaQuizDone`)
- sichtbare UI-Elemente (`CoronaSlider`)
- aktivierte Corruption-Effekte (`NoCorruptionDragPuzzle`)

#### `set_ui_state(key: str, value: bool)`

Ändert gezielt den Status eines UI-Elements oder -Effekts.

> Damit lässt sich zentral steuern, welche Komponenten sichtbar oder deaktiviert werden. Beispielsweise wird dadurch gesteuert wann der Corruption-Gif zu sehen ist.

## 5.3 Praktische Anwendung & Spezialfunktionen

### Korruptionsanzeige aktivieren/deaktivieren

**Korruption anzeigen (z. B. wenn Aufgabe noch nicht gelöst):**

```python
if st.session_state.ui_state["NoCorruptionCoronaSlider"] == False:
    Corruption.render()
```

**Korruption ausblenden (nach erfolgreicher Lösung):**

```python
if (
    st.session_state.text_key == "slidercorrect"
    and st.session_state.text_index == 1
    and not st.session_state.ui_state["CoronaSliderDone"]
):
    set_ui_state("CoronaSliderDone", True)
    set_ui_state("NoCorruptionCoronaSlider", True)
    st.rerun()
```

>Hinweis: Der st.rerun() sorgt dafür, dass nach dem Setzen der Zustände sofort neu geladen wird und der Korruptionseffekt verschwindet.

---

### Sprungziele für den „Auge“-Button setzen

#### Voraussetzung

In einem Streamlit-Element (z. B. `st.title`) einen `anchor` setzen:

```python
st.title("Faktencheck", anchor="factcheckers")
oder in einer Markdown:
st.markdown('<div id="factcheckers"></div>', unsafe_allow_html=True)
```

#### Ziel per Code setzen

```python
set_zone("factcheckers")
```

#### Ziel über Button in der Sprechblase setzen

```python
st.button("", on_click=set_text_key, args=("FCwerprüftde", "factcheckers"), key="chat_fc")
```

- Erstes Argument = Schlüssel aus `bubble_texts` (Welcher Text aus dem Dictionary soll gezeigt werden)
- Zweites Argument = Sprungziel-Anchor

---

### Charaktertext gezielt anzeigen

Text muss in `data/bubble_texts.py` enthalten sein:

```python
"FCwerprüftde": [
    "Wer überprüft eigentlich Fakten im Netz?..."
]
```

Dann mit Button aufrufen:

```python
st.button("", on_click=set_text_key, args=("FCwerprüftde", "factcheckers"), key="chat_fc")
```

Durch den Ersten Parameter wird bei einem Klick der Text angepasst zu "FCwerprüftde"

---

### Sichtbarkeit und Fortschritt per `ui_state` steuern

In `data/ui_states.py` neue Keys ergänzen:

```python
_UI_KEYS = [
    "DragPuzzle",
    "DragPuzzleDone",
    "NoCorruptionDragPuzzle",
    "NoCorruptionCoronaSlider"
]
```

**Zustände ändern:**

```python
set_ui_state("DragPuzzle", True)
set_ui_state("DragPuzzleDone", True)
```

**Verwendung im Code:**

```python
if (
    st.session_state.text_key == "dragpuzzle"
    and st.session_state.text_index == 4
) or st.session_state.ui_state["DragPuzzle"]:
    st.session_state.ui_state["DragPuzzle"] = True
    DragPuzzleLogic.render()
```

>st.session_state.text_key == "dragpuzzle" prüft, ob gerade der richtige Textabschnitt aktiv ist.

>st.session_state.text_index == 4 prüft, ob der aktuelle Satz in der Sprechblase dem Punkt entspricht, an dem das Puzzle starten soll.

>or st.session_state.ui_state["DragPuzzle"] stellt sicher, dass das Puzzle auch nach einem st.rerun() weiterhin angezeigt wird. Ebenfalls wird verhindert, dass diese Komponente in Zukunft erneut angezeigt wird, wenn man auf denselben button klickt.

---

### Eigene Zone lokal testen

1. Datei `index.py` öffnen  
2. Unten Abschnitt `## Andere Dashboards:` finden  
3. Alles darunter auskommentieren (inkl. `render()`)

4. Stattdessen eigene Komponente laden:

```python
import zones.Corona as Corona
Corona.render()
```

> Voraussetzung: Die Ziel-Datei enthält eine `def render():`-Funktion.

---

### Hinweis zu Korruption und Tests

Wenn eine Zone korrupt ist, werden Inhalte blockiert.  
Durch die Option von oben "Korruption ausblenden" kann man dies lösen und die Korruption ausblenden, falls man eine Aufgabe richtig löst.

---

### Glitch- und FakeText-Effekte im Text

Einfügen in `st.markdown(...)`:

```html
<span class="corrupt">[MissingNumber]</span>
<span class="falsetext">DeinFalscherText</span>
```

**Eigene CSS-Effekte:**  
In `index.py` im `<style>`-Block ganz oben ergänzen – unbedingt **eindeutige Klassennamen** verwenden.

---

### Automatisch scrollen beim Zonenwechsel
>
>Wenn Streamlit dynamisch die Website erweitern, bspw. entfernen der Corruption und hinzufügen einer neuen Zone, dann wird die Position des Users nicht automatisch angepasst.
Somit wird der User mitten in der Zone positioniert sein, nachdem die Seitenanpassungen durch sind.
Deshalb bietet sich die autojump-Funktion an.

```python
from data.zone_anchor import autojump
import time

time.sleep(1.5)
autojump("factcheckers")
```

**Voraussetzung:**

```python
st.title("Faktencheck", anchor="factcheckers")
```

 Wichtig:

- `time.sleep(1.5)` ist nötig, da Streamlit sonst sofort neu rendert
- Scroll funktioniert nur, bzw. meistens nur, wenn sich das Sprungziel, zwischen den Aufrufen der Funktion, verändert hat

---

### Quellenangaben einfügen

```python
if st.toggle("Quellen", key="quelle_slider"):
    st.markdown("""
    <div style="border:1px solid #ccc; border-radius:6px; padding:10px; margin-top:5px;">
        <ul>
            <li><a href='https://example.com/a' target='_blank'>Studie A</a></li>
            <li><a href='https://example.com/b' target='_blank'>Studie B</a></li>
            <li><a href='https://example.com/c' target='_blank'>Artikel C</a></li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
```

**Hinweis:**  
Der Key des Toggles sollte mit `"quelle"` beginnen, damit das Styling korrekt greift.

---

### Buttons im Chat-Stil verwenden

```python
st.button("", on_click=set_text_key, args=("FCwerprüftde", "factcheckers"), key="chat_fc")
```

**Achtung:**  

- Button-Key muss **einzigartig** sein (z. B. `"chat_fc"`, `"chat_drag"`)  
- Keine zwei Buttons dürfen den gleichen Key haben – sonst reagiert Streamlit nicht mehr korrekt

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

Die Anwendung ist dann unter <http://localhost:8501> erreichbar.

---

## Deployment auf Streamlit Cloud

Um den Code auf **Streamlit Cloud** laufen zu lassen, muss das Repository auf **GitHub öffentlich** sein.  
Außerdem **muss eine Kleinigkeit im Code angepasst werden**, sodass `PrototypeChar2.gif` und `PrototypeChar_still.png` korrekt angezeigt werden.

**Hintergrund:**  
Streamlit Cloud erlaubt **kein direktes Fileserving aus dem `/static/`-Ordner**, sodass JS nicht auf lokale Bilder zugreifen kann.

## Code-Anpassung für Streamlit Cloud (Bildpfade)

### Anpassung in `components/CharSpeechBubble/charspeechbubble.py`

Folgenden Code:

```html
<img id="floating-avatar" src="app/static/PrototypeChar2.gif" />
```

```js
avatar.src = "app/static/PrototypeChar2.gif";
avatar.src = "app/static/PrototypeChar_still.png";
```

ändern zu:

```html
<img id="floating-avatar" src="https://raw.githubusercontent.com/Audrey2900/AWP-SS25/main/static/PrototypeChar2.gif" />
```

```js
avatar.src = "https://raw.githubusercontent.com/Audrey2900/AWP-SS25/main/static/PrototypeChar2.gif";
avatar.src = "https://raw.githubusercontent.com/Audrey2900/AWP-SS25/main/static/PrototypeChar_still.png";
```

### Anpassung in `components/Corruption/corruption.py`

Folgenden Code:

```html
<img src="app/static/corruption.gif"
```

ändern zu:

```html
<img src="https://raw.githubusercontent.com/Audrey2900/AWP-SS25/main/static/corruption.gif"
```

> **Wichtig:** Statt `Audrey2900/AWP-SS25` muss der eigene GitHub-Repo-Pfad verwendet werden. Der Restliche Pfad kann so bleiben.

## Kein Deployment in der Cloud

Wenn **kein Deployment in der Cloud** erfolgt, sondern die App lokal ausgeführt wird, kann weiterhin folgendes verwendet werden:

```
"app/static/(NameVomBild,Gif)"
```

## Komponenten-Details

### Animierte Diagramme

Die animierten Diagramme in `chartanimation.py` verwenden HTML/JS-Injection mit Plotly, um automatisch startende Animationen zu erzeugen. Seit Juni 2025 mit optimierten Timing-Parametern:

```python
fig.layout.updatemenus[0].buttons[0].args[1]["frame"]["duration"] = 60   # 60ms pro Frame
fig.layout.updatemenus[0].buttons[0].args[1]["transition"]["duration"] = 30  # 30ms Übergang
```

### PictureSelector

Der PictureSelector bietet ein spielerisches Element, bei dem Nutzer:innen Personen und Aktionen kombinieren können:

1. Frontend in HTML/CSS/JS
2. Integration in Streamlit via IFrame oder Components
3. Angepasstes Styling mit dunklem Hintergrund und hellen Akzenten

### Neue Quiz-Komponenten

Die interaktiven Quizze zu Corona und Faktencheckern bieten:

1. Multiple-Choice-Fragen mit direktem Feedback
2. Auswertung der Antworten mit farblicher Markierung
3. Möglichkeit zum Wiederholen des Quiz

### Deepfake-Erkennungsaufgabe

Die Mission 3 zur Deepfake-Erkennung bietet:

1. Bildverarbeitung für einheitliche Größen:

```python
img = img.convert("RGB")
img.thumbnail(target_size, Image.LANCZOS)
background = Image.new("RGB", target_size, (14, 17, 23))
offset = ((target_size[0] - img.width) // 2, (target_size[1] - img.height) // 2)
background.paste(img, offset)
```

2. Bewertungssystem für richtige und falsche Antworten
3. Fortschrittsanzeige mit farblichen Indikatoren

## Herausforderungen und Lösungen

### 1. Automatische Animation in Streamlit

**Herausforderung**: Streamlit bietet keine native Unterstützung für automatisch startende Plotly-Animationen.

**Lösung**: Nutzung von HTML-Injection mit `components.html()` und angepasstem JavaScript/CSS, um Steuerelemente auszublenden und Auto-Play zu erzwingen.

### 2. Dark Mode mit konsistentem Design

**Herausforderung**: Streamlit-Komponenten und eigene HTML-Elemente im einheitlichen Dark Mode darstellen.

**Lösung**: Globales Theme in config.toml und manuelle CSS-Anpassungen für Custom Components.

**Update Juni 2025**: Konsistente Anwendung des dunklen Themes auch für Plotly-Visualisierungen mit `template="plotly_dark"` und angepassten Farbparametern.

### 3. Responsive Layout für verschiedene Bildschirmgrößen

**Herausforderung**: Konsistente Darstellung auf verschiedenen Geräten.

**Lösung**: Relative Einheiten (%, vh) und Flexbox-Layout für bessere Anpassungsfähigkeit.

### 4. Einheitliche Bildgrößen für konsistente Darstellung (Neu)

**Herausforderung**: Bilder mit unterschiedlichen Größen und Seitenverhältnissen führen zu unruhigem Layout.

**Lösung**: Bildverarbeitung mit Pillow, um alle Bilder auf einheitliche Größe zu bringen und zentriert darzustellen.

### 5. Performance-Optimierung für animierte Visualisierungen (Neu)

**Herausforderung**: Animationen waren zu langsam oder liefen nicht flüssig genug.

**Lösung**: Optimierung der Timing-Parameter für Frame-Dauer und Übergänge, Reduzierung unnötiger Neuzeichnungen mit `redraw: False`.

## Erweiterungsmöglichkeiten

...

## Anhang und Referenzen

### Nützliche Ressourcen

- [Streamlit Dokumentation](https://docs.streamlit.io/)
- [Plotly Python Dokumentation](https://plotly.com/python/)
- [Pandas Dokumentation](https://pandas.pydata.org/docs/)
- [Pillow Dokumentation](https://pillow.readthedocs.io/) (Neu)

### Projekthistorie und Meilensteine

- **April 2025**: Projektstart, Konzeption
- **Juni 2025**: Entwicklung der Kernkomponenten
- **11. Juni 2025**: Erste Dokumentation
- **24. Juni 2025**: Erweiterung um Quiz-Komponenten, Performance-Optimierungen und Deepfake-Erkennung
- **Juli 2025**: Fertigstellung sowie Kundenübernahme

---

**Stand:** 24. Juni 2025  
**Autor:** Luca Breisinger
