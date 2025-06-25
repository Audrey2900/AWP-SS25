import streamlit as st

from data.char_speech_state import set_text_key
from data.ui_states import set_ui_state

def render():

    st.markdown("""
        <style>
        [class*="st-key-sentiment_radio"] label {
            margin-bottom: 15px;
        }
        </style>
    """, unsafe_allow_html=True)

    st.radio(
    "Welche Schlussfolgerung lässt sich aus den dargestellten Zahlen ziehen?",
    options=[
        "Die Mehrheit der Fake News ist positiv. Sie wird genutzt, um Menschen mit schmeichelhaften Aussagen oder Hoffnung zu beeinflussen. "
        "Solche Inhalte verbreiten sich besonders schnell in sozialen Medien. Doch nicht alle Falschmeldungen wirken freundlich. Einige sind aggressiv, andere neutral. "
        "Gerade diese scheinbar harmlosen Beiträge können besonders manipulativ sein. Wer sich emotional nicht betroffen fühlt, hinterfragt seltener. "
        "Auf diese Weise entfalten auch neutrale Fake News ihre Wirkung, leise und unauffällig.",
        "Die Mehrheit der Fake News ist negativ. Sie schürt gezielt Angst oder Wut und sorgt so für besonders schnelle Verbreitung. Positive Inhalte sind selten. "
        "Neutrale Fake News spielen hingegen keine große Rolle. Da sie keine starken Emotionen auslösen, werden sie von den meisten Menschen einfach ignoriert und haben kaum Einfluss.",
        "Die Mehrheit der Fake News ist negativ. Sie zielt darauf ab, Angst, Wut oder Empörung auszulösen. Solche Inhalte verbreiten sich besonders schnell in sozialen Medien. "
        "Doch nicht alle Falschmeldungen sind aggressiv. Einige wirken sogar positiv, andere neutral. Gerade diese scheinbar harmlosen Beiträge können besonders manipulativ sein. "
        "Wer sich emotional nicht betroffen fühlt, hinterfragt seltener. Auf diese Weise entfalten auch neutrale Fake News ihre Wirkung, leise und unauffällig.",
        "Fake News wirken nur auf Menschen, die wenig Medienkompetenz besitzen. Wer gut informiert ist, erkennt jede Falschmeldung sofort. "
        "Deshalb spielt es keine Rolle, ob sie negativ, positiv oder neutral sind. Die Wirkung hängt allein vom Bildungsgrad der Leser ab."
    ],
    key="sentiment_radio"
    )

    def auswertung():
        richtige_antwort = (
            "Die Mehrheit der Fake News ist negativ. Sie zielt darauf ab, Angst, Wut oder Empörung auszulösen. "
            "Solche Inhalte verbreiten sich besonders schnell in sozialen Medien. Doch nicht alle Falschmeldungen "
            "sind aggressiv. Einige wirken sogar positiv, andere neutral. Gerade diese scheinbar harmlosen Beiträge "
            "können besonders manipulativ sein. Wer sich emotional nicht betroffen fühlt, hinterfragt seltener. "
            "Auf diese Weise entfalten auch neutrale Fake News ihre Wirkung, leise und unauffällig."
        )

        if st.session_state.get("sentiment_radio") == richtige_antwort:
            set_text_key("SentimentSliderCorrect")
        else:
            set_text_key("SentimentSliderFalse")


    st.button("Antworten übertragen", on_click=auswertung)

    if (
        st.session_state.text_key == "SentimentSliderCorrect"
        and st.session_state.text_index == 1
        and not st.session_state.ui_state["SentimentSliderDone"]
    ):
        set_ui_state("SentimentSliderDone", True)
        set_ui_state("NoCorruptionSentimentSlider", True)
        st.rerun()

