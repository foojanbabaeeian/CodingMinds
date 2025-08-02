import streamlit as st

"""
# Hello World, Streamlit!

This is a website to demonstrate Streamlit's API.
You can stop looking at this now.

Please.
"""

st.write("This is some text made using Python.")

adjective = st.text_input("Type in an adjective")
noun = st.text_input("Type in a noun")
verb = st.text_input("Type in a verb in past tense")

st.write("I just gave a " + noun + " twenty " + adjective + " dollars and he " + verb + " me!")

pressed = st.button("Press me!")
if pressed:
    st.write("Why did you do that?")