import splitter as splitter
import sentencepiece
import streamlit as st
import requests
from streamlit_lottie import st_lottie
from streamlit.logger import get_logger
import torch
from transformers import PegasusForConditionalGeneration, PegasusTokenizer
from sentence_splitter import SentenceSplitter, split_text_into_sentences
LOGGER = get_logger(__name__)

model_name = 'tuner007/pegasus_paraphrase'
torch_device = 'cuda' if torch.cuda.is_available() else 'cpu'
tokenizer = PegasusTokenizer.from_pretrained(model_name)
model = PegasusForConditionalGeneration.from_pretrained(model_name).to(torch_device)


def run():
    def get_response(input_text, num_return_sequences, num_beams):
        batch = tokenizer([input_text], truncation=True, padding='longest', max_length=60, return_tensors="pt").to(
            torch_device)
        translated = model.generate(**batch, max_length=60, num_beams=num_beams,
                                    num_return_sequences=num_return_sequences,
                                    temperature=1.5)
        tgt_text = tokenizer.batch_decode(translated, skip_special_tokens=True)
        return tgt_text

    with st.container():
        st.header("Paraphraser")
        st.write("""
                         People use the skill of paraphrasing in their everyday lives, even if they are unaware of it. When recounting an event or conversation where one cannot remember exactly what was said, he or she will recount the gist of the meaning in his or her own words. Essentially, this is paraphrasing. Simply, to paraphrase is to take information from a source and put it into one's own words. In general, paraphrases are approximately the same length as the original information, which distinguishes them from summaries, which are shorter than the original.
                        """)

        # Getting user input:
        st.subheader("Enter text to paraphrase:")
        user_input_sentence = st.text_area(" ")

        # For paragraphs
        splitter = SentenceSplitter(language='en')
        sentence_list = splitter.split(user_input_sentence)

        # do a for loop to iterate through the list of sentence and paraphrase each sentence in the iterartion
        paraphrase = []

        for i in sentence_list:
            a = get_response(i, 1, 2)
            paraphrase.append(a)

        # paraphrased = get_response(user_input_sentence, 1, 3)

        def list_to_string(txt):
            # initialize an empty string
            str1 = " "

            # return string
            return str1.join(txt)

        st.subheader("Paraphrased text:")
        st.write(paraphrase)


if __name__ == "__main__":
    run()