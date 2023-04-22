# import streamlit as st
# import nltk
# from nltk.corpus import cmudict

# nltk.download('cmudict')

# cmu_dict = cmudict.dict()

# def is_vowel_sound(phoneme):
#     return any(char.isdigit() for char in phoneme)

# def phoneme_to_text(phoneme, word, start_idx):
#     phoneme = phoneme.lower()
#     for i in range(start_idx, len(word)):
#         if word[i] == phoneme[0]:
#             return word[start_idx:i] + word[i], i + 1
#     return word[start_idx:], len(word)

# def phonemes_to_letters(syllables, word):
#     idx = 0
#     letter_syllables = []
#     for syllable in syllables:
#         letter_syllable = ''
#         for phoneme in syllable:
#             if not phoneme[-1].isdigit():
#                 text, idx = phoneme_to_text(phoneme, word, idx)
#                 letter_syllable += text
#         letter_syllables.append(letter_syllable)
#     return '-'.join(letter_syllables)

# def split_syllables(word):
#     word = word.lower()
#     if word not in cmu_dict:
#         return []

#     phonemes = cmu_dict[word][0]
#     syllables = []
#     current_syllable = []

#     for phoneme in phonemes:
#         current_syllable.append(phoneme)
#         if is_vowel_sound(phoneme):
#             syllables.append(current_syllable)
#             current_syllable = []

#     if current_syllable:
#         syllables[1] += current_syllable

#     return phonemes_to_letters(syllables, word)




# def app():
#     st.title("Syllables Generator with CMU Pronouncing Dictionary")

#     word = st.text_input("Enter a word:", "")
    
#     if word:
#         syllables = split_syllables(word)
#         st.success(syllables)
        
#         if syllables:
#             st.info(f"Syllables for the word **{word}**:")
#             st.write("-".join(syllables))
#         else:
#             st.warning("The word was not found in the CMU Pronouncing Dictionary. Unable to split syllables.")

# if __name__ == '__main__':
#     app()
