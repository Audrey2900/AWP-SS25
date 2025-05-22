## PieChart zum zeigen, dass KI, obwohl es eigentlich rational denken sollte, auch anhand von
## Merkmalen diskriminiert (Beispielsweise wenn man KI benutzt, um sich über politische Themen
## zu informieren) (Und wenn KI diskriminiert, dann wegen eines dieser Themen)
## (Um zu zeigen, dass KI nicht perfekt ist)

import streamlit as st
import plotly.express as px

def render():
    # Daten vorbereiten, ohne none
    data = {
        "Kategorie": [
            "Ethnische Zugehörigkeit",
            "Geschlecht",
            "Nationalität/Migrationsstatus",
            "Behinderung",
            "Religion",
            "Sexuelle Orientierung/Geschlechtsidentität",
            "Finanzielle Mittel",
            "Alter",
            "Geografie",
            "Ideologie",
            "Familienstand/Schwangerschaft",
            "Sonstiges"
        ],
        "Fälle": [43, 21, 12, 11, 11, 11, 9, 8, 8, 2, 1, 1]
    }

    fig = px.pie(
        data,
        names="Kategorie",
        values="Fälle",
        title="Diskriminierung durch KI (AIID)",
        hole=0
    )

    fig.update_traces(
        textposition='outside',
        textinfo='label+percent',
        hovertemplate='%{label}<br>%{percent}',
    )

    fig.update_layout(showlegend=False)

    st.plotly_chart(fig, use_container_width=True)
