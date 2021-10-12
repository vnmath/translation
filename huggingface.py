import streamlit as st
from transformers import pipeline

st.title('Some Hugginface Features')
st.code('''
>>>  Classify Text
>>>  Question Answering
>>>  Text Generation
>>>  Named Entity Recognition
>>>  Summarization
>>>  Translation
''')

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
