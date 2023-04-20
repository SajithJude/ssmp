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

def generate_maw(wordes):
    sentence = " ".join(wordes)
    word_list = word_tokenize(sentence)
    syllables_list = [divide_syllables(word) for word in word_list]

    maws = []
    syllables = []
    for i in range(len(syllables_list)):
        for j in range(i+1, len(syllables_list)+1):
            maw = "".join([syllables_list[k][0] for k in range(i,j)])

            if len(maw) >= 6 and len(maw) <= 20:
                maws.append(maw)
        
        # Add the list of syllables for the current word to the syllables list
        syllables.append(syllables_list[i])
    
    # Return both the list of MAWs and the list of syllables
    return maws, syllables

   
def app():
    st.title("Memory Anchor Words Generator")

    # Text input for entering the words to memorize
    words_to_memorize = st.text_input("Enter the words to memorize, separated by commas")

    # Generate MAWs when the "Generate MAWs" button is clicked
    if st.button("Generate MAWs"):
        if words_to_memorize:
            # Split the input words into a list
            word_list = [word.strip() for word in words_to_memorize.split(",")]

            # Generate MAWs and syllables for the input words
            maws, syllables_list = generate_maw(word_list)

            # Display the MAWs and syllables for each word
            st.write("Memory Anchor Words and Syllables:")
            for i in range(len(word_list)):
                st.write(word_list[i])
                st.write("Syllables:", syllables_list[i])
                st.write("MAWs:", [maw for maw in maws if word_list[i] in maw])
        else:
            st.write("Please enter some words to memorize.")


if __name__ == '__main__':
    app()
