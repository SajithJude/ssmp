# import streamlit as st

# def split_syllables(word):
#     vowels = 'aeiouy'
#     splits = []
#     word = word.lower()
#     i = 0

#     while i < len(word) - 1:
#         if word[i] in vowels and word[i+1] not in vowels:
#             splits.append(word[:i+1] + '-' + word[i+1:])
#         if word[i] not in vowels and word[i+1] in vowels:
#             splits.append(word[:i+1] + '-' + word[i+1:])
#         i += 1

#     return list(set(splits))

# def app():
#     st.title("Alternative Syllable Splits")

#     word = st.text_input("Enter a word:", "")
    
#     if word:
#         syllable_splits = split_syllables(word)
        
#         st.info(f"Syllable variations for the word **{word}**:")
#         for split in syllable_splits:
#             st.write(split)

# if __name__ == '__main__':
#     app()
