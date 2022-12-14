# Text reader

Text reader can convert any string of text written on an image into text.

This app uses [streamlit](https://docs.streamlit.io/)
for frontend and two models from 
[hugging face](https://huggingface.co/models) for 
backend: [trocr-base-printed](https://huggingface.co/microsoft/trocr-base-printed) and
[trocr-base-handwritten](https://huggingface.co/microsoft/trocr-base-handwritten) for
recognition of printed and handwritten text respectively.

## How to use it
### Web
Just go here: [https://naniduan-text-reader-main-5sfmm3.streamlit.app/](https://naniduan-text-reader-main-5sfmm3.streamlit.app/)
+ Upload an image
+ Select whether the text on the image is printed or handwritten
+ Wait for the result to appear
### Telegram bot
*Work in progress*
### Build on your computer
+ Make sure you have a python environment
+ Download the code
+ Install required packages with ```pip install -r requirements.txt``` or
install [Pillow](https://pillow.readthedocs.io/en/stable/installation.html),
[streamlit](https://docs.streamlit.io/library/get-started/installation),
[transformers](https://github.com/huggingface/transformers) 
and [torch](https://pytorch.org/get-started/locally/) separately
+ Run the app with ```streamlit run main.py``` or
```python -m streamlit run main.py```
+ Wait until the models are downloaded
+ Do what the **Web** section says