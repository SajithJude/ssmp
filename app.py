import streamlit as st
import nltk
from nltk import word_tokenize
from nltk.corpus import words

nltk.download('punkt')
nltk.download('words')

def divide_syllables(word):
    vowels = "AEIOUYaeiouy"
    syllables = []
    current_syllable = ""
    for letter in word:
        if letter in vowels:
            if current_syllable:
                syllables.append(current_syllable)
            current_syllable = letter
        else:
            current_syllable += letter
    if current_syllable:
        syllables.append(current_syllable)
    return syllables

def generate_maw(words):
    sentence = " ".join(words)
    word_list = word_tokenize(sentence)
    syllables_list = [divide_syllables(word) for word in word_list]

    maws = []
    for i in range(len(syllables_list)):
        for j in range(i+1, len(syllables_list)+1):
            maw = "".join([syllables_list[k][0] for k in range(i,j)])

            if len(maw) >= 6 and len(maw) <= 20:
                maws.append(maw)
    return maws

def app():
    st.title("SMPL Memory Anchor Words Generator")

    # Text input for entering the words to memorize
    words_to_memorize = st.text_input("Enter the words to memorize, separated by commas")

    # Split the input words into a list
    if words_to_memorize:
        word_list = [word.strip() for word in words_to_memorize.split(",")]

        # Dropdown to select a word
        # selected_word = st.selectbox("Select a word to display syllables:", word_list)

        # Display syllables for the selected word when the "Show Syllables" button is clicked
        if st.button("Show Syllables"):
            syllables = divide_syllables(words_to_memorize)
            st.subheader
            st.info(f"Syllables ': {', '.join(syllables)}")

        # Generate MAWs for the input words
        maws = generate_maw(word_list)

        # Display the MAWs
        st.subheader("Memory Anchor Words:")
        for maw in maws:
            st.write(maw)
    else:
        st.write("Please enter some words to memorize.")


if __name__ == '__main__':
    app()
