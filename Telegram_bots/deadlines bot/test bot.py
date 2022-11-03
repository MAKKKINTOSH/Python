import telebot
import sqlite3
import datetime
from config import Token
from telebot import types

bot=telebot.TeleBot(Token)
DB=sqlite3.connect('deadline_data_base.db')

Admin=bool
UserId=int
edit_access = 0

def  objects(CallData, edit_acces): ''


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

        InKeyboard=types.InlineKeyboardMarkup(row_width=3)
        but1 = types.InlineKeyboardButton("ближайшие дедлайны", callback_data='Know')
        but2 = types.InlineKeyboardButton("Ближайшие 5 дедлайнов", callback_data='Know_five')
        but3 = types.InlineKeyboardButton("Редактировать", callback_data='Edit')
        InKeyboard.add(but1, but2)
        if (Admin==True): InKeyboard.add(but3)

        bot.send_message(UserId, f"Что вы хотите сделать\nadmin={Admin}\nid={UserId}", reply_markup=InKeyboard)

        @bot.callback_query_handler(func=lambda call:True)
        def Choise(call):

            CallData = ['InProf', 'Nosyreva', 'English', 'Informatics', 'Math', 'BBC', 'Prog', 'Physics', 'PE']

            global edit_access

            InKeyboard = types.InlineKeyboardMarkup(row_width=2)                                    #object_id
            but1 = types.InlineKeyboardButton('ВПД', callback_data='InProf')                  #1
            but2 = types.InlineKeyboardButton('Дискретная математика', callback_data='Nosyreva')    #2
            but3 = types.InlineKeyboardButton('Иностранный язык', callback_data='English')          #3
            but4 = types.InlineKeyboardButton('Информатика', callback_data='Informatics')           #4
            but5 = types.InlineKeyboardButton('Математика', callback_data='Math')                   #5
            but6 = types.InlineKeyboardButton('ОДК', callback_data='BBC')                           #6
            but7 = types.InlineKeyboardButton('Программирование', callback_data='Prog')             #7
            but8 = types.InlineKeyboardButton('Физика', callback_data='Physics')                    #8
            but9 = types.InlineKeyboardButton('Физкультура', callback_data='PE')                    #9
            but10 = types.InlineKeyboardButton('В меню', callback_data='ToMenu')
            InKeyboard.add(but1, but2, but3, but4, but5, but6, but7, but8, but9, but10)

            InKeyboardType = types.InlineKeyboardMarkup(row_width=3)
            but11 = types.InlineKeyboardButton('Д/З', callback_data='0')
            but12 = types.InlineKeyboardButton('Л/Р', callback_data='1')
            InKeyboardType.add(but11, but12)

            if call.data=="Know":

                edit_access=0
                bot.edit_message_text('Выберите предмет', UserId, message_id=call.message.message_id)
                bot.edit_message_reply_markup(UserId, message_id=call.message.message_id, reply_markup=InKeyboard)

            if call.data=="Know_five":

                bot.answer_callback_query(call.id, text="еще не готово", show_alert=True)

            if call.data=="Edit":

                edit_access=1
                bot.edit_message_text('Выберите предмет', UserId, message_id=call.message.message_id)
                bot.edit_message_reply_markup(UserId, message_id=call.message.message_id, reply_markup=InKeyboard)

            if call.data == 'ToMenu':

                bot.delete_message(UserId, message_id=call.message.message_id)
                Menu(call.message)

            if call.data in CallData:
                if edit_access == 1:
                    bot.edit_message_text('Д/З или Л/Р')
                    bot.edit_message_reply_markup(UserId, message_id=call.message.message_id, reply_markup=InKeyboardType)
                if edit_access == 0:
                    bot.answer_callback_query(UserId, text="not ready", show_alert=True)






main()

bot.polling(long_polling_timeout=30)            #bot.polling(non_stop=True)