import re
import streamlit as st


def detect_silent_vowels(word):
    silent_vowels = []

    # Silent 'e' at the end of words
    if len(word) > 1 and word[-1] == 'e':
        silent_vowels.append('e')

    # Silent 'a' in 'bread' pattern or 'each' pattern or 'aisle' pattern or 'boar' pattern
    if 'a' in word and (re.search(r'ea[^u]', word) or re.search(r'aisle', word) or re.search(r'oa[^u]', word)):
        silent_vowels.append('a')

    # Silent 'o' in 'people' pattern or 'country' pattern
    if 'o' in word and (re.search(r'eo[^u]', word) or re.search(r'ou[^u]', word)):
        silent_vowels.append('o')

    # Silent 'i' in 'business' pattern or 'cushion' pattern
    if 'i' in word and (re.search(r'business', word) or re.search(r'io[^u]', word)):
        silent_vowels.append('i')

    # Silent 'u' in 'guess' pattern or 'guide' pattern
    if 'u' in word and (re.search(r'gue[^u]', word) or re.search(r'gui[^u]', word)):
        silent_vowels.append('u')

    return silent_vowels

word = st.text_input("Enter a word: ")
silent_vowels = detect_silent_vowels(word)
if silent_vowels:
    st.write(f"The silent vowels in '{word}' are: {silent_vowels}")
else:
    st.write(f"There are no silent vowels in '{word}'")
