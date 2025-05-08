# Setup

Package Manager herunterladen:
pip install uv

In Powershell: cd "Pfad zum Projekt"

(
Optional: uv venv
Warum venv? => Erstellt eine virtuelle Umgebung. In dieser werden die Packages heruntergeladen.
Packages können durch das venv in der virtuellen Umgebung heruntergeladen werden und werden nicht global installiert.
=> Keine Konflikte mit anderen Python-Projekten
Im Pfad ausführen:  .\.venv\Scripts\Activate
)

Packages herunterladen mit: uv sync

Nachdem alle Packages heruntergeladen wurden: streamlit run "dashboard1 2.py"

## Venv

Wenn man uv venv benutzt hat, dann sollte man immer mit dem Befehl .\.venv\Scripts\Activate die Umgebung aktivieren.
Deaktivieren geht durch den Befehl: deactivate

## Optionaler Formatter

Ein empfohlener formatter für Python ist "Black".
Man kann entweder in der pyproject.toml diese zeile in die dependencies einfügen:
"black>=23.0"

oder man installiert es direkt global mit pip install black.
Wenn man VSCode verwendet kann man eine Extension für Black installieren.
