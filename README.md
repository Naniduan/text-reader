# text-reader

Text reader can convert any string of text written on an image into text.

This app uses [streamlit](https://docs.streamlit.io/)
for frontend and two models from 
[hugging face](https://huggingface.co/models) for 
backend: [trocr-base-printed](https://huggingface.co/microsoft/trocr-base-printed) and
[trocr-base-handwritten](https://huggingface.co/microsoft/trocr-base-handwritten) for
recognition of printed and handwritten text respectively.

## How to use it
### Web
Just go here: [https://naniduan-text-reader-main-4o5bni.streamlit.app/](https://naniduan-text-reader-main-4o5bni.streamlit.app/)
+ Upload an image
+ Select whether the text on the image is printed or handwritten
+ Wait for the result to appear
### Telegram bot
***still work in progress***

Use this bot: [@neuraltextreaderbot](https://t.me/neuraltextreaderbot)
+ Send it an image
+ Specify whether it has a string of printed or handwritten text
+ Wait until you get the result
### Build on your computer
You can build it as a **web app**:
+ Make sure you have a python environment
+ Download the code
+ Install required packages with ```pip install -r requirements.txt``` or
install [Pillow](https://pillow.readthedocs.io/en/stable/installation.html),
[streamlit](https://docs.streamlit.io/library/get-started/installation),
[transformers](https://github.com/huggingface/transformers#installation),
[sentencepiece](https://github.com/google/sentencepiece#installation) 
and [torch](https://pytorch.org/get-started/locally/) separately
+ Run the app with ```streamlit run main.py``` or
```python -m streamlit run main.py```
+ Wait until the models are downloaded
+ Do what the **Web** section says

Alternatively, you can build it as a **telegram bot**:
+ Then, you would also need to 
install [pyTelegramBotAPI](https://pytba.readthedocs.io/en/latest/install.html)
+ Create a ```api_token.txt``` file in the main directory and put your HTTP API
token here.
+ Run ```telegram_bot.py``` as a python file.
+ To use the bot do as the **Telegram bot** section says.