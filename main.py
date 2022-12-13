import streamlit as st

<<<<<<< HEAD
from PIL import Image
import requests
from backend import model

def __main():
    st.write("Choose an image file with a line of text:")
    image_file = st.file_uploader("Choose an image")
    st.write("To start, please specify whether the text is printed or handwritten.")
    printed = st.button("printed")
    handwritten = st.button("handwritten")

    if printed:
        st.write(model.get_printed_text(image_file))
    if handwritten:
        st.write(model.get_handwritten_text(image_file))

if __name__ == '__main__':
    __main()
=======
st.title('Work in progress')
>>>>>>> 2dbef0f (Create main.py)
