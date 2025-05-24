import streamlit as st

from data.zone_anchor import set_zone

def render(): 
    # anchors
    st.button("Springziel zu AnchorsTest", on_click=set_zone, args=("anchors",))

    st.header("📌 Springziel", anchor="anchors")
    st.write("Hier soll hingesprungen werden!")

    st.divider()
    st.divider()
    st.divider()

    st.markdown(f'[ Springe nach oben](#{st.session_state.current_zone})', unsafe_allow_html=True)

    st.markdown(f"""
        <style>
        #fixed-jump {{
            position: fixed;
            bottom: 20px;
            right: 20px;
            z-index: 9999;
        }}
        #fixed-jump button {{
            background-color: #f7941d;
            color: white;
            border: none;
            border-radius: 8px;
            padding: 10px 16px;
            font-size: 16px;
            cursor: pointer;
            box-shadow: 2px 2px 6px rgba(0,0,0,0.2);
        }}
        #fixed-jump button:hover {{
            background-color: #ffa733;
        }}
        </style>

        <div id="fixed-jump">
            <a href="#{st.session_state.current_zone}">
                <button>👁️ Springen</button>
            </a>
        </div>
    """, unsafe_allow_html=True)
