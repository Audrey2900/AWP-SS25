import streamlit as st

# Anker setzen
st.markdown('<div id="zone1"></div>', unsafe_allow_html=True)
st.title("📊 Mini-Dashboard: Fake News Visualisierung")

# Abstand erzeugen
st.markdown("<div style='height:1500px'></div>", unsafe_allow_html=True)
st.write("Noch weiter unten…")

# Fixierter Button
st.markdown(f"""
<a href="#zone1">
    <button style="
        background-color: #f7941d;
        color: white;
        border: none;
        border-radius: 8px;
        padding: 8px 16px;
        font-size: 16px;
        cursor: pointer;
    ">👁️ Springen</button>
</a>

""", unsafe_allow_html=True)


st.markdown('[Springe nach oben](#zone1)', unsafe_allow_html=True)
