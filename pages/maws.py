import streamlit as st
import pyphen

# Set language fallback and initialize Pyphen object
# pyphen.language_fallback('nl_NL_variant1')
dic = pyphen.Pyphen(lang='en')

# Define Streamlit app
def app():
    # Add a title
    st.title("Rule-based maws generator")

    # Add a text input field for the user to enter a sentence
    sentence = st.text_input("Enter a sentence:", "")

    # Check if the user has entered a sentence
    if sentence:
        # Split the sentence into words
        words = sentence.split()

        for word in words:
            # Get the hyphenation pairs for the entered word
            hyphenated_word = dic.iterate(word)
            hyp = dic.inserted(word)
            syllist = [hyp]

            # Display the hyphenation variations for the current word
            st.info(f"Syllable variations for the word **{word}**:")
            st.write(hyp)
            for variation in hyphenated_word:
                vary = "-".join(variation)
                st.write(str(vary))
                syllist.append(str(vary))

            # Display the list of syllable variations for the current word
            st.write(syllist)

# Run the Streamlit app
if __name__ == '__main__':
    app()
