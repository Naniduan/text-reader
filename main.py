import streamlit as st

from PIL import Image
import requests
from backend import model

def __main():
    st.write("Choose an image file with a line of text:")
    image_file = st.file_uploader("Choose an image")
    text_type = st.radio(
        "To start, please specify whether the text is printed or handwritten.",
        ("printed", "handwritten"))
    start = st.button('start')

    if start:
        if text_type == "printed":
            st.write(model.get_printed_text(image_file))
        else:
            st.write(model.get_handwritten_text(image_file))

if __name__ == '__main__':
    __main()