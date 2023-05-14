import re
import streamlit as st

def detect_silent_vowels(word):
    silent_vowels = []
    # Check for silent 'e' at the end of words
    if len(word) > 1 and word[-1] == 'e':
        silent_vowels.append('e')

    # Check for silent 'a' in 'bread' pattern
    if 'a' in word and re.search(r'ea[^u]', word):
        silent_vowels.append('a')

    # Check for silent 'o' in 'people' pattern
    if 'o' in word and re.search(r'eo[^u]', word):
        silent_vowels.append('o')

    return silent_vowels

word = st.text_input("Enter a word: ")
silent_vowels = detect_silent_vowels(word)
if silent_vowels:
    st.write(f"The silent vowels in '{word}' are: {silent_vowels}")
else:
    st.write(f"There are no silent vowels in '{word}'")
