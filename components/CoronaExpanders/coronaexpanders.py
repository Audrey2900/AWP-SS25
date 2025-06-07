import streamlit as st

def render():
    col1, col2, col3 = st.columns(3)
    with col1:
        with st.expander("5G-Mobilfunk verursacht COVID-19"):
            st.write("Platzhaltertext für Geschichte 1. Hier steht später die echte Geschichte.")
    with col2:
        with st.expander("Bill Gates plant, Mikrochips über Impfungen zu implantieren"):
            st.write("Platzhaltertext für Geschichte 2. Hier steht später die echte Geschichte.")
    with col3:
        with st.expander("COVID-19 ist nicht schlimmer als die Grippe"):
            st.write("Platzhaltertext für Geschichte 3. Hier steht später die echte Geschichte.")

    col4, col5, col6 = st.columns(3)
    with col4:
        with st.expander("Geheimplan: Corona als Schwindel oder Biowaffe"):
            st.write("Platzhaltertext für Geschichte 4. Hier steht später die echte Geschichte.")
    with col5:
        with st.expander("Vitamin C in Mega-Dosis heilt COVID-19"):
            st.write("Platzhaltertext für Geschichte 5. Hier steht später die echte Geschichte.")
    with col6:
        with st.expander("5G-Masten würden angeblich Corona auslösen"):
            st.write("Platzhaltertext für Geschichte 6. Hier steht später die echte Geschichte.")