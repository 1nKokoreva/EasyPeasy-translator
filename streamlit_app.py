
import streamlit as st
import time
import streamlit as st 
from transformers import pipeline

st.spinner()
with st.spinner(text='loading...'):
     time.sleep(2)

st.markdown(
    '<div style="background-color: #6e7352; padding: 10px; border-radius: 5px; text-align: center;">'
    '<h1 style="text-align: center; color: #ffffff;">'
    '<span style="color: #f64b4b;">E</span>asy'
    '<span style="color:#f64b4b;">P</span>easy'
    '</h1></div>',
    unsafe_allow_html=True
)

st.write("\n")

st.subheader('Translate texts easily and quickly from English to German:')

st.text('''1. In the first field, write the text in English that needs to be translated.
           2. Click on the 'Translate' button or press Ctrl+Enter.
           3. Review the translated text below the input field.''')

st.info('For a correct translation, make sure that the text is written correctly.')

text = st.text_area(label="Enter the text in English here")
st.markdown(
    """
    <style>
    div.stButton > button {
        background-color: #6e7352; 
        color: white; 
        border-radius: 5px; 
        font-weight: bold; 
    </style>
    """,
    unsafe_allow_html=True
)

if st.button('Translate'):
    if text.strip(): 
        try:
           
            with st.spinner("Translation in progress... Please wait."):
                # Создаем пайплайн для перевода
                pipe = pipeline("translation", model="google-t5/t5-base")

              
                result = pipe(text)
                translated_text = result[0]['translation_text']

                st.success("✅ The translation was executed successfully!")

                st.subheader("Translated Text:")
                st.write(f"> {translated_text}")
        
                st.balloons()
                
        except Exception as e:
            st.error(f"ERROR: We are sorry, some mistake has occurred. {str(e)}")
    else:
        st.warning("❗You have not entered the text to be translated in the field❗")


st.empty()
st.markdown(
    '<div style="background-color: #6e7352; padding: 3px; border-radius: 5px; text-align: center;">'
    '<h3 style="text-align: center; color: #ffffff;">s22136</h3></div>',
    unsafe_allow_html=True
)

