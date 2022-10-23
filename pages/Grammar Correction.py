import streamlit as st
import requests
from streamlit_lottie import st_lottie
from streamlit.logger import get_logger
from happytransformer import HappyTextToText, TTSettings
LOGGER = get_logger(__name__)

happy_tt = HappyTextToText("T5", "achrekarom/grammar_correction")
args = TTSettings(num_beams=5, min_length=1)


def run():
    st.header("Grammar Correction")
    st.write("""
                Our online grammar checker allows you to grab all the grammatical mistakes in your content in no time. This facility will enable you to ensure that your article is free from any faults and it’s completely ready to share with your colleagues, teachers, or supervisors. All the processing will be completed in a matter of seconds, and you will get reliable results without making any efforts at all. Furthermore, there is no need to proofread your content yourself, as our sentence checker is here to help you out.
                """)

    # Getting user input:
    st.subheader("Enter text to check:")
    user_input_sentence = st.text_area(" ")

    # Add the prefix "grammar: " before each input
    result = happy_tt.generate_text("grammar: "+user_input_sentence, args=args)

    st.subheader("Corrected text:")
    st.write(" "+result.text)
    # print(result.text)


if __name__ == "__main__":
    run()