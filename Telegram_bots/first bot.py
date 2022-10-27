import telebot
from telebot import types
token='5500352575:AAHq_bKD3MVfNSwJCjuH02_IjHnKSBaIqGE'
bot=telebot.TeleBot(token)

def er(message):
    bot.send_message(message.chat.id, "Встроенной клавиатурой пользуйся, дебил!")


@bot.message_handler(commands=['start'])
def kuz(message):
    basedKeyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1=types.KeyboardButton("Да")
    basedKeyboard.add(but1)
    bot.send_sticker(message.chat.id,open('E:/stickers/welcome_1.webp', 'rb'))
    bot.send_message(message.chat.id, "Welcome to the club, buddy!", reply_markup=basedKeyboard)
    bot.send_sticker(message.chat.id,open('E:/stickers/welcome_2.webp', 'rb'))

@bot.message_handler(content_types=['text'])

def slaves(message):
    basedKeyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton("yeas")
    but2 = types.KeyboardButton("yeas of course")
    basedKeyboard.add(but1, but2)
    if (message.text == "fucking slave"):
        bot.send_message(message.chat.id, "lets go to the dungeon, honey", reply_markup=basedKeyboard)
    elif (message.text == "Semen"):
        bot.send_message(message.chat.id, "fisting?", reply_markup=basedKeyboard)
    else:
        er(message)




bot.polling(none_stop=True)