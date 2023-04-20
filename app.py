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
    for i in range(len(syllables_list)):
        for j in range(i+1, len(syllables_list)+1):
            maw = "".join([syllables_list[k][0] for k in range(i,j)])

            if len(maw) >= 6 and len(maw) <= 20:
                maws.append(maw)
    return maws, syllables_list
   
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

            # Create a dropdown with the list of words
            selected_word = st.selectbox("Select a word:", word_list)

            # Find the index of the selected word in the word list
            index = word_list.index(selected_word)

            # Display the syllables for the selected word
            st.write("Syllables:", syllables_list[index])

            # Display the MAWs that contain the selected word
            selected_word_maws = [maw for maw in maws if selected_word in maw]
            st.write("Memory Anchor Words:")
            if len(selected_word_maws) > 0:
                for maw in selected_word_maws:
                    st.write(maw)
            else:
                st.write("No Memory Anchor Words found for this word.")
        else:
            st.write("Please enter some words to memorize.")



if __name__ == '__main__':
    app()
