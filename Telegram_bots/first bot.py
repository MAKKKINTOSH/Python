import telebot
import sqlite3
import datetime
from config import Token
from telebot import types
bot=telebot.TeleBot(Token)

Admin=bool
UserId=int
def Error(message):
    global UserId
    bot.send_message(UserId, "Клавиатурой бота пользуйся, дебил!")

def deadlines(object):


def main():

    @bot.message_handler(commands=['start'])
    def Hello(message):
        global UserId
        UserId = message.chat.id
        ReKeyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        ReKeyboard.add('Запуск')
        bot.send_message(UserId, f'Привет, {UserId},через меня ты можешь узнать свои ближайшие дедлайны', reply_markup=ReKeyboard)
    @bot.message_handler(regexp='Запуск')
    def Menu(message):


        Admin=False
        if UserId==545762112 or UserId==958029367:
            Admin=True

        InKeyboard=types.InlineKeyboardMarkup(row_width=2)
        but1 = types.InlineKeyboardButton("Узнать ближайшие дедлайны", callback_data='Know')
        but2 = types.InlineKeyboardButton("Редактировать", callback_data='Edit')
        InKeyboard.add(but1)
        if (Admin==True): InKeyboard.add(but2)

        bot.send_message(UserId, f"Что вы хотите сделать\nadmin={Admin}\nid={UserId}", reply_markup=InKeyboard)

        @bot.callback_query_handler(func=lambda call:True)
        def Choise(call):

            InKeyboard = types.InlineKeyboardMarkup(row_width=2)
            but1 = types.InlineKeyboardButton('Кононенко', callback_data='InProf')
            but2 = types.InlineKeyboardButton('Дискретная математика', callback_data='Nosyreva')
            but3 = types.InlineKeyboardButton('Иностранный язык', callback_data='English')
            but4 = types.InlineKeyboardButton('Информатика', callback_data='Informatics')
            but5 = types.InlineKeyboardButton('Математика', callback_data='Math')
            but6 = types.InlineKeyboardButton('ОДК', callback_data='BBC')
            but7 = types.InlineKeyboardButton('Программирование', callback_data='Prog')
            but8 = types.InlineKeyboardButton('Физика', callback_data='Physics')
            but9 = types.InlineKeyboardButton('Физкультура', callback_data='PE')
            but10 = types.InlineKeyboardButton('В меню', callback_data='ToMenu')
            InKeyboard.add(but1, but2, but3, but4, but5, but6, but7, but8, but9, but10)

            if call.data=="Know":

                bot.edit_message_text('Выберите предмет', UserId, message_id=call.message.message_id)
                bot.edit_message_reply_markup(UserId, message_id=call.message.message_id, reply_markup=InKeyboard)

            if call.data=="Edit":

                bot.edit_message_text('Выберите предмет', UserId, message_id=call.message.message_id)
                bot.edit_message_reply_markup(UserId, message_id=call.message.message_id, reply_markup=InKeyboard)

            if call.data =='InProf':
                bot.answer_callback_query(call.id, text="еще не готово", show_alert=False)
                bot.send_message(UserId, call)

            if call.data == 'Nosyreva': bot.answer_callback_query(call.id, text="еще не готово", show_alert=False)

            if call.data == 'English': bot.answer_callback_query(call.id, text="еще не готово", show_alert=False)

            if call.data == 'Informatics': bot.answer_callback_query(call.id, text="еще не готово", show_alert=False)

            if call.data == 'Math': bot.answer_callback_query(call.id, text="еще не готово", show_alert=False)

            if call.data == 'BBC': bot.answer_callback_query(call.id, text="еще не готово", show_alert=False)

            if call.data == 'Prog': bot.answer_callback_query(call.id, text="еще не готово", show_alert=False)

            if call.data == 'Physics': bot.answer_callback_query(call.id, text="еще не готово", show_alert=False)

            if call.data == 'PE': bot.answer_callback_query(call.id, text="еще не готово", show_alert=False)

            if call.data == 'ToMenu':

                bot.delete_message(UserId, message_id=call.message.message_id)
                Menu(call.message)



main()

bot.polling(non_stop=True)     #bot.polling(long_polling_timeout=30)