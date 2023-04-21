import streamlit as st
import pyphen

# Set language fallback and initialize Pyphen object
pyphen.language_fallback('nl_NL_variant1')
dic = pyphen.Pyphen(lang='en')

# Define Streamlit app
def app():
    # Add a title
    st.title("Rule based Syllables generator")

    # Add a text input field for the user to enter a word
    word = st.text_input("Enter a word:", "")

    # Check if the user has entered a word
    if word:
        # Get the hyphenation pairs for the entered word
        hyphenated_word = dic.iterate(word)
        hyp  = dic.inserted(word)
        # Display the hyphenation variations
        # st.info("Syllable variations for the word **{}**:".format(word))
        st.write(hyp)
        for variation in hyphenated_word:
            vary = "-".join(variation)
            st.write(str(vary))
            # st.write(type(variation))

# Run the Streamlit app
if __name__ == '__main__':
    app()
