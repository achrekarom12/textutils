import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest
import streamlit as st
from streamlit.logger import get_logger
LOGGER = get_logger(__name__)


def run():
    st.header("Summariser")
    st.write("""
                                The act of expressing the most important facts or ideas about something or someone in a short and clear form, or a text in which these facts or ideas are expressed is summary.
                                The main types of informative summaries are: outlines, abstracts, and synopses.
                                Outlines present the plan or the “skeleton” of a written material.
                                Outlines show the order and the relation between the parts of the written material.
                                Abstracts present the major point of long piece of text or an article. Abstracts help readers to decide whether or not they want to read the longer text.
                                A synopsis is a brief overview of an article, story, book, film, or other works.
                                A synopsis is a concise, chronological description of a historical event, news event, historical event or other experiences as they develop in time
                                """)
    # Getting user input:
    st.subheader("Enter text to summarise:")
    user_input_sentence = st.text_area(" ")

    def summerize(text):
        stopwords = list(STOP_WORDS)
        nlp = spacy.load(
            "/Users/omachrekar/miniforge3/envs/work/lib/python3.10/site-packages/en_core_web_sm/en_core_web_sm-3.4.0")
        doc = nlp(text)
        tokens = [token.text for token in doc]
        word_frequencies = {}
        for word in doc:
            if word.text.lower() not in stopwords:
                if word.text.lower() not in punctuation:
                    if word.text not in word_frequencies.keys():
                        word_frequencies[word.text] = 1
                    else:
                        word_frequencies[word.text] += 1
        max_frequency = max(word_frequencies.values())

        for word in word_frequencies.keys():
            word_frequencies[word] = word_frequencies[word] / max_frequency
        sentence_tokens = [sent for sent in doc.sents]
        sentence_scores = {}
        for sent in sentence_tokens:
            for word in sent:
                if word.text.lower() in word_frequencies.keys():
                    if sent not in sentence_scores.keys():
                        sentence_scores[sent] = word_frequencies[word.text.lower()]
                    else:
                        sentence_scores[sent] += word_frequencies[word.text.lower()]

        select_length = int(len(sentence_tokens) * 0.3)
        summary = nlargest(select_length, sentence_scores, key=sentence_scores.get)
        return summary
    # user_text = """ Johannes Gutenberg (1398 – 1468) was a German goldsmith and publisher who introduced printing to Europe. His introduction of mechanical movable type printing to Europe started the Printing Revolution and is widely regarded as the most important event of the modern period. It played a key role in the scientific revolution and laid the basis for the modern knowledge-based economy and the spread of learning to the masses.
    # Gutenberg many contributions to printing are: the invention of a process for mass-producing movable type, the use of oil-based ink for printing books, adjustable molds, and the use of a wooden printing press. His truly epochal invention was the combination of these elements into a practical system that allowed the mass production of printed books and was economically viable for printers and readers alike.
    # In Renaissance Europe, the arrival of mechanical movable type printing introduced the era of mass communication which permanently altered the structure of society. The relatively unrestricted circulation of information—including revolutionary ideas—transcended borders, and captured the masses in the Reformation. The sharp increase in literacy broke the monopoly of the literate elite on education and learning and bolstered the emerging middle class."""


     # Getting user input:
    # st.subheader("Enter text to summarise:")
    # user_input_sentence = st.text_area(" ")

    summerised_text = summerize(user_input_sentence)
    print(summerised_text)
    print(type(summerised_text))
    st.subheader("Summarised text:")
    st.write(summerised_text)


if __name__ == "__main__":
    run()
