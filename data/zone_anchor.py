import streamlit as st
from streamlit.components.v1 import html

def init_zone_state():
    if "visited_zones" not in st.session_state:
        st.session_state.visited_zones = set()
    if "current_zone" not in st.session_state:
        st.session_state.current_zone = "zone1"

def set_zone(name: str):
    if name not in st.session_state.visited_zones:
        st.session_state.current_zone = name
        st.session_state.visited_zones.add(name)

# Kann nur jeweils 1 mal je gesetzten Anchor ausgeführt werden.
# Wenn diese Funktion beim aktualisieren der Website (neue Textabschnitte) verwendet wird, sollte
# timer importiert werden und timer.sleep(1.5) eingefügt werden, bevor der Rerun das ziehen verhindert. Bsp. CoronaQuiz
def autojump(anchor_id: str):
    html(f"""
    <script>
        const target = parent.document.getElementById("{anchor_id}");
        if (target) {{
            target.scrollIntoView({{ behavior: "smooth" }});
        }}
    </script>
    """, height=0)
