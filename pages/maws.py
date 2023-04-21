import itertools
import streamlit as st
import pyphen
import nltk
from nltk.corpus import stopwords

# Download stopwords
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

# Initialize Pyphen object
dic = pyphen.Pyphen(lang='en_US')

# Function to generate syllable combinations for a word
def syllable_combinations(word):
    hyphenated_word = dic.iterate(word)
    hyp = dic.inserted(word)
    syllist = [hyp]
    for variation in hyphenated_word:
        vary = "-".join(variation)
        syllist.append(vary)
    return syllist

# Function to generate MAWs
def generate_maws(words):
    syllable_combinations_list = [
        [syllable[:4] for syllable in syllable_combinations(word)]
        for word in words
    ]
    maw_combinations = list(itertools.product(*syllable_combinations_list))
    maws = [''.join(maw) for maw in maw_combinations]
    return maws

# Define Streamlit app
def app():
    # Add a title
    st.title("Memory Anchor Words (MAWs) Generator")

    # Add a text input field for the user to enter a sentence
    sentence = st.text_input("Enter a sentence:", "")

    # Check if the user has entered a sentence
    if sentence:
        words = sentence.split()
        filtered_words = [word for word in words if word.lower() not in stop_words]
        maws = generate_maws(filtered_words)
        st.write("Suggested Memory Anchor Words:")
        for maw in maws:
            st.info(maw)

# Run the Streamlit app
if __name__ == '__main__':
    app()
