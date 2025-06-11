import streamlit as st
import components.DragPuzzleLogic.dragpuzzlelogic as DragPuzzleLogic
from data.char_speech_state import set_text_key

def render():
    if st.session_state.ui_state["DragPuzzleDone"] == False:
            st.markdown("""
            Als das Coronavirus im Jahr 2020 um die Welt ging, veränderte sich unser Alltag schlagartig: Schulen wurden geschlossen, der Unterricht fand online statt, Masken wurden Pflicht, und plötzlich wusste niemand mehr so genau, was eigentlich stimmt. Doch neben dem Virus selbst verbreitete sich noch etwas anderes rasend schnell: <span class="falsetext">Social-Media-Nutzer</span>. Fake News rund um Corona waren überall. Sie kamen über <span class="falsetext">die Weltgesundheitsorganisation (WHO)</span> direkt aufs Handy, also mitten in unseren Alltag.

            Gerade Jugendliche sind besonders oft mit Fake News konfrontiert. Gleichzeitig fühlen sich viele unsicher, wie sie erkennen können, ob etwas wahr ist oder nicht. Fast ein Drittel der jungen Menschen in Deutschland gab an, sich nicht fit im Umgang mit Desinformation zu fühlen. Dabei ist genau das heute wichtiger denn je.

            Schon früh warnte <span class="falsetext">Jugendlichen zwischen 14 und 24 Jahren</span> vor einer Infodemie, einer Welle an falschen Nachrichten, die sich schneller verbreitet als das Virus selbst. Und tatsächlich: Studien zeigen, dass ein Großteil der Menschen während der Pandemie mit Desinformation in Kontakt kam. In Deutschland sahen **68%** der <span class="falsetext">WhatsApp, TikTok, Instagram und YouTube</span> Fake News zur Corona-Pandemie. Bei <span class="falsetext">Falschinformationen, Gerüchte und wilde Verschwörungstheorien</span> waren es sogar **76%**, die mindestens einmal pro Woche auf Falschnachrichten stießen.
            """, unsafe_allow_html=True)

            st.button("", on_click=set_text_key, args=("dragpuzzle",), key="chatcoronadragpuzzle")

            if (
                st.session_state.text_key == "dragpuzzle" and st.session_state.text_index == 4
            ) or st.session_state.ui_state["DragPuzzle"] == True:
                st.session_state.ui_state["DragPuzzle"] = True
                DragPuzzleLogic.render()

    if st.session_state.ui_state["DragPuzzleDone"] == True:
        st.markdown("""
        Als das Coronavirus im Jahr 2020 um die Welt ging, veränderte sich unser Alltag schlagartig: Schulen wurden geschlossen, der Unterricht fand online statt, Masken wurden Pflicht, und plötzlich wusste niemand mehr so genau, was eigentlich stimmt. Doch neben dem Virus selbst verbreitete sich noch etwas anderes rasend schnell: Falschinformationen, Gerüchte und wilde Verschwörungstheorien. Fake News rund um Corona waren überall. Sie kamen über WhatsApp, TikTok, Instagram und YouTube direkt aufs Handy, also mitten in unseren Alltag.

        Gerade Jugendliche sind besonders oft mit Fake News konfrontiert. Gleichzeitig fühlen sich viele unsicher, wie sie erkennen können, ob etwas wahr ist oder nicht. Fast ein Drittel der jungen Menschen in Deutschland gab an, sich nicht fit im Umgang mit Desinformation zu fühlen. Dabei ist genau das heute wichtiger denn je.

        Schon früh warnte die Weltgesundheitsorganisation (WHO) vor einer Infodemie, einer Welle an falschen Nachrichten, die sich schneller verbreitet als das Virus selbst. Und tatsächlich: Studien zeigen, dass ein Großteil der Menschen während der Pandemie mit Desinformation in Kontakt kam. In Deutschland sahen **68%** der Social-Media-Nutzer Fake News zur Corona-Pandemie. Bei Jugendlichen zwischen 14 und 24 Jahren waren es sogar **76%**, die mindestens einmal pro Woche auf Falschnachrichten stießen.
        """, unsafe_allow_html=True)

        st.button("", on_click=set_text_key, args=("coronadone",), key="chatcoronadonepuzzle")