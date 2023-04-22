import streamlit as st
import nltk
from nltk.corpus import cmudict

nltk.download('cmudict')

cmu_dict = cmudict.dict()

def is_vowel_sound(phoneme):
    return any(char.isdigit() for char in phoneme)

def phonemes_to_letters(syllables, word):
    word = word.lower()
    word_idx = 0
    letter_syllables = []

    for syllable in syllables:
        letter_syllable = ''
        for phoneme in syllable:
            phoneme_letters = phoneme.lower()
            while word_idx < len(word) and phoneme_letters:
                current_letter = word[word_idx]
                if current_letter == phoneme_letters[0]:
                    letter_syllable += current_letter
                    phoneme_letters = phoneme_letters[1:]
                word_idx += 1
        letter_syllables.append(letter_syllable)

    return '-'.join(letter_syllables)

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

    return phonemes_to_letters(syllables, word)



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
