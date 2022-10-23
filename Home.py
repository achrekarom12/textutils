import streamlit as st
import requests
from streamlit_lottie import st_lottie
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)

# Useful links:
# https://www.webfx.com/tools/emoji-cheat-sheet/


def run():
    st.set_page_config(page_title="Text Utilities", page_icon=":computer:", layout="wide")

    # load animation asset
    def load_animation(url):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()

    # assets:
    animation_1 = load_animation("https://assets1.lottiefiles.com/private_files/lf30_ytvxrnwn.json")
    animation_2 = load_animation("https://assets1.lottiefiles.com/private_files/lf30_7th4tkji.json")
    animation_3 = load_animation("https://assets1.lottiefiles.com/private_files/lf30_y4x6f4rs.json")
    animation_4 = load_animation("https://assets3.lottiefiles.com/private_files/lf30_ysjb4sex.json")

    # Header section
    with st.container():
        st.title("Text Utilities")
        st.subheader("A simple, minimalistic web app that will help you in need!")

        st.write(
            "Want to get your text summerize? or are you searching for a paraphraser that will rearrange the sentences for you without changing its meaning? And yes grammar correction is also sometimes a big task! If you are looking for these tools then friend you have come at right place!!")

    # slide 1
    with st.container():
        st.write("---")
        left_col, right_col = st.columns(2)

        with left_col:
            st.header("Summeriser")
            # st.write("##")
            st.write("""
            The act of expressing the most important facts or ideas about something or someone in a short and clear form, or a text in which these facts or ideas are expressed is summary.
            The main types of informative summaries are: outlines, abstracts, and synopses.
            Outlines present the plan or the “skeleton” of a written material.
            Outlines show the order and the relation between the parts of the written material.
            Abstracts present the major point of long piece of text or an article. Abstracts help readers to decide whether or not they want to read the longer text.
            A synopsis is a brief overview of an article, story, book, film, or other works.
            A synopsis is a concise, chronological description of a historical event, news event, historical event or other experiences as they develop in time
            """)
            st.write("[Github :link:](https://github.com/achrekarom12/Text-Utilities/blob/main/Summerisation.ipynb)")

        with right_col:
            st_lottie(animation_1, height=300, key="animation_1")

    # slide 2
    with st.container():
        st.write("---")
        left_col, right_col = st.columns(2)

        with left_col:
            st_lottie(animation_2, height=300, key="animation_2")

        with right_col:
            st.header("Paraphrasing")
            # st.write("##")
            st.write("""
             People use the skill of paraphrasing in their everyday lives, even if they are unaware of it. When recounting an event or conversation where one cannot remember exactly what was said, he or she will recount the gist of the meaning in his or her own words. Essentially, this is paraphrasing. Simply, to paraphrase is to take information from a source and put it into one's own words. In general, paraphrases are approximately the same length as the original information, which distinguishes them from summaries, which are shorter than the original.
            """)
            st.write("[Github :link:](https://github.com/achrekarom12/Text-Utilities/blob/main/Paraphrasing.ipynb)")

    # slide 3
    with st.container():
        st.write("---")
        left_col, right_col = st.columns(2)

        with left_col:
            st.header("Grammar Correction")
            # st.write("##")
            st.write("""
                Our online grammar checker allows you to grab all the grammatical mistakes in your content in no time. This facility will enable you to ensure that your article is free from any faults and it’s completely ready to share with your colleagues, teachers, or supervisors. All the processing will be completed in a matter of seconds, and you will get reliable results without making any efforts at all. Furthermore, there is no need to proofread your content yourself, as our sentence checker is here to help you out.
            """)
            st.write("[Github :link:](https://github.com/achrekarom12/Text-Utilities/blob/main/Grammar%20Correction.ipynb)")

        with right_col:
            st_lottie(animation_3, height=300, key="animation_3")

    with st.container():
        st.write("---")
        st.header("About us")
        st.subheader("""
        "None of us, ever do great things. But we can all do small things, with great love, and together we can do something wonderful."
        """)

        col1, col2, col3 = st.columns(3)
        with col1:
            st.write(" ")

        with col2:
            st_lottie(animation_4, height=300, key="animation_4")

        with col3:
            st.write(" ")

        st.write("Our wonderful team:")
        mitali, radha, om = st.columns(3)
        with mitali:
            st.subheader("Ms. Mitali Deepaksingh Rawat")
            st.write("Roll No.: 21")
            st.write("Email ID: mitali.201433201@vcet.edu.in")
            st.write("Contact: 8452813912")
            st.write("Vidyavardhini's College of Engineering & Technology, Vasai")

        with radha:
            st.subheader("Ms. Radha Ramesh Vishwakarma")
            st.write("Roll No.: 46")
            st.write("Email ID: radha.201793201@vcet.edu.in")
            st.write("Contact: 9987701127")
            st.write("Vidyavardhini's College of Engineering & Technology, Vasai")

        with om:
            st.subheader("Mast. Om Ramesh Achrekar")
            st.write("Roll No.: 54")
            st.write("Email ID: om.201173105@vcet.edu.in")
            st.write("Contact: 9819930448")
            st.write("Vidyavardhini's College of Engineering & Technology, Vasai")


if __name__ == "__main__":
    run()

