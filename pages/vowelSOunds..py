import streamlit as st
import nltk
from nltk.corpus import cmudict

nltk.download('cmudict')

cmu_dict = cmudict.dict()

def is_vowel_sound(phoneme):
    return any(char.isdigit() for char in phoneme)

def phonemes_to_letters(syllables):
    letters = ''
    for syllable in syllables:
        for phoneme in syllable:
            if phoneme[-1].isdigit():
                letters += phoneme[:-1].lower()
            else:
                letters += phoneme.lower()
        letters += '-'
    return letters[:-1]

def split_syllables(word):
    word = word.lower()
    if word not in cmu_dict:
        return []

    phonemes = cmu_dict[word][0]
    syllables = []
    current_syllable = []

    for phoneme in phonemes:
        current_syllable.append(phoneme)
        if is_vowel_sound(phoneme):
            syllables.append(current_syllable)
            current_syllable = []

    if current_syllable:
        syllables[-1] += current_syllable

    return phonemes_to_letters(syllables)


def app():
    st.title("Syllables Generator with CMU Pronouncing Dictionary")

    word = st.text_input("Enter a word:", "")
    
    if word:
        syllables = split_syllables(word)
        
        if syllables:
            st.info(f"Syllables for the word **{word}**:")
            st.write("-".join(syllables))
        else:
            st.warning("The word was not found in the CMU Pronouncing Dictionary. Unable to split syllables.")

if __name__ == '__main__':
    app()
