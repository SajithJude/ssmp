import streamlit as st
import pyphen

dic = pyphen.Pyphen(lang='en_US')

def split_syllables(word):
    vowels = 'aeiouy'
    splits = []
    word = word.lower()
    i = 0

    while i < len(word) - 1:
        if word[i] in vowels and word[i+1] not in vowels:
            split = word[:i+1] + '-' + word[i+1:]
            if len(split.split('-')[0]) > 2:
                splits.append(split)
        if word[i] not in vowels and word[i+1] in vowels:
            split = word[:i+1] + '-' + word[i+1:]
            if len(split.split('-')[0]) > 2:
                splits.append(split)
        i += 1

    return list(set(splits))


def app():
    st.title("Rule-based Syllables Generator")

    word = st.text_input("Enter a word:", "")
    
    if word:
        hyphenated_word = dic.inserted(word)
        
        if not dic.positions(word):
            # st.info("Default hyphenation not found. Generating alternative syllable splits:")
            syllable_splits = split_syllables(word)
            for split in syllable_splits:
                st.info(split)
        else:
            # st.info(f"Default hyphenation for the word **{word}**:")
            st.info(hyphenated_word)

if __name__ == '__main__':
    app()



#     syllables = hyphenated_word.split('-')
        
#         st.info("Syllables for the word **{}**:".format(word))
#         for index, syllable in enumerate(syllables, 1):
#             st.write(f"{index}. {syllable}")
# # 