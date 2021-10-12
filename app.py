import streamlit as st
from transformers import pipeline

st.title('Translation from English to French')

option = st.selectbox(
    "Select an Option",
    [
        "Translation to French",
    ],
)

if option == "Translation to French":
    translator = pipeline("translation_en_to_fr")
    text = st.text_area(label="Enter text")
    if st.button("Translate"):
        translation = translator(text)
        st.write(translation)
