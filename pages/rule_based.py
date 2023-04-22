import streamlit as st
import pyphen

# Set language fallback and initialize Pyphen object
# pyphen.language_fallback('nl_NL_variant1')
dic = pyphen.Pyphen(lang='en_US')

# Define Streamlit app
def app():
    # Add a title
    st.title("Rule based Syllables generator")

    # Add a text input field for the user to enter a word
    word = st.text_input("Enter a word:", "")
    syllist = []
    # Check if the user has entered a word
    num= st.number_input("width",step=1)
    if word:
        # Get the hyphenation pairs for the entered word
        hyphenated_word = dic.inserted(word)
        syllables = hyphenated_word.split('-')
        
        st.info("Syllables for the word **{}**:".format(word))
        for index, syllable in enumerate(syllables, 1):
            st.write(f"{index}. {syllable}")

        hyp  = dic.inserted(word)
        syllist.append(hyp)
        st.info(hyp)
        # st.success(dic.positions(word))
        st.success(dic.wrap(word,num,hyphen='-'))

       

# Run the Streamlit app
if __name__ == '__main__':
    app()
