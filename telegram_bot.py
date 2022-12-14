import telebot
from telebot import types
from backend import model
from os import remove

f = open("api_token.txt")
api_token = f.read().split()
api_token = api_token[0]
f.close()

bot = telebot.TeleBot(api_token)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, '''Hello!\nThis bot can convert images with a string of text into text. To do this, send me a photo.''')

@bot.message_handler(content_types=['photo'])
def photo(message):
    fileID = message.photo[-1].file_id
    file_info = bot.get_file(fileID)
    downloaded_file = bot.download_file(file_info.file_path)

    with open(str(message.chat.id)+".jpg", 'wb') as new_file:
        new_file.write(downloaded_file)

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add('Printed', 'Handwritten')

    bot.send_message(message.chat.id, "Please specify whether the text is printed or handwritten",
                     reply_markup=keyboard)

@bot.message_handler(content_types=['text'])
def generate_text(message):
    if message.text == "Printed":
        try:
            bot.send_message(message.chat.id, model.get_printed_text(str(message.chat.id)+".jpg"))
            bot.send_message(message.chat.id, "You can send me another image")
            remove(str(message.chat.id)+".jpg")
        except:
            bot.send_message(message.chat.id, "It seems like I have already read you image. But you can resend it!")

    elif message.text == "Handwritten":
        try:
            bot.send_message(message.chat.id, model.get_handwritten_text(str(message.chat.id)+".jpg"))
            bot.send_message(message.chat.id, "You can send me another image")
            remove(str(message.chat.id) + ".jpg")
        except:
            bot.send_message(message.chat.id, "It seems like I have already read you image. But you can resend it!")

    else:
        bot.send_message(message.chat.id, "Please specify whether the text is printed or handwritten",
                         reply_markup=keyboard)
bot.polling(non_stop=True)
