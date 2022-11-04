import telebot
import sqlite3
from functions import DeadDb
from config import Token
from telebot import types

bot=telebot.TeleBot(Token)
DB=DeadDb('deadline_data_base.db')



Admin=bool
UserId = 0
edit_access = 0
ObjectType = ''
DeadlineDate = ''

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

        global UserId, Admin
        if UserId == 0: UserId = message.chat.id
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
                                        #СДЕЛАТЬ АВТОУДАЛЕНИЕ СТАРЫХ ДАТ
                                        #ОБЯЗАТЕЛЬНО!!!!
            CallData = ['InProf', 'Nosyreva', 'English', 'Informatics', 'Math', 'BBC', 'Prog', 'Physics', 'PE']
            global edit_access, ObjectType, DeadlineDate

            InKeyboard = types.InlineKeyboardMarkup(row_width=2)                                    #object_id
            but1 = types.InlineKeyboardButton('ВПД', callback_data='InProf')                        #1
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
            InKeyboardType.add(but11, but12, but10)

            EndKeyboardMarkup = types.InlineKeyboardMarkup(row_width=1)
            but21 = types.InlineKeyboardButton('В начало', callback_data='ToStart')
            EndKeyboardMarkup.add(but21)

            if call.data=="Know":

                edit_access=0
                bot.edit_message_text('Выберите предмет', UserId, message_id=call.message.message_id)
                bot.edit_message_reply_markup(UserId, message_id=call.message.message_id, reply_markup=InKeyboard)

            if call.data=="Know_five":

                bot.edit_message_text(f"Ближайшие 5 дедлайнов\n"
                                      f"1. {DB.show_n_deadline(1)}\n"
                                      f"2. {DB.show_n_deadline(2)}\n"
                                      f"3. {DB.show_n_deadline(3)}\n"
                                      f"4. {DB.show_n_deadline(4)}\n"
                                      f"5. {DB.show_n_deadline(5)}\n", UserId, message_id=call.message.message_id)
                bot.edit_message_reply_markup(UserId, message_id=call.message.message_id, reply_markup=EndKeyboardMarkup )

            if call.data=="Edit":

                edit_access=1
                bot.edit_message_text('Выберите предмет', UserId, message_id=call.message.message_id)
                bot.edit_message_reply_markup(UserId, message_id=call.message.message_id, reply_markup=InKeyboard)

            if call.data == 'ToMenu':

                bot.delete_message(UserId, message_id=call.message.message_id)
                Menu(call.message)

            if call.data in CallData:
                ObjectType = call.data
                if edit_access == 1:
                    bot.edit_message_text('Д/З или Л/Р', UserId, message_id=call.message.message_id)
                    bot.edit_message_reply_markup(UserId, message_id=call.message.message_id, reply_markup=InKeyboardType)
                if edit_access == 0:
                    bot.edit_message_text(text=f"Ближайшие дедлайны\n{str(DB.object(ObjectType))[2:-3]}\nД/З: {str(DB.show_deadline(ObjectType, 0)) if str(DB.show_deadline(ObjectType, 0)) != 'None' else 'Дедлайнов нет'}\nЛ/Р: {str(DB.show_deadline(ObjectType, 1)) if str(DB.show_deadline(ObjectType, 1)) != 'None' else 'Дедлайнов нет'}", message_id=call.message.message_id, chat_id=UserId, parse_mode='HTML')
                    bot.edit_message_reply_markup(UserId, message_id=call.message.message_id, reply_markup=EndKeyboardMarkup )

            if call.data == '1' or call.data == '0':
                bot.send_message(UserId, 'Введите дату в формате дд.мм.гггг')
                @bot.message_handler(content_types=['text'])
                def make(message):
                    a = message.text
                    DeadlineDate = a[6] + a[7] + a[8] + a[9] + '-' + a[3] + a[4] + '-' + a[0] + a[1]
                    DB.make_deadline(ObjectType, int(call.data), DeadlineDate)
                    bot.edit_message_reply_markup(UserId, message_id=call.message.message_id, reply_markup=EndKeyboardMarkup )

            if call.data == "ToStart":
                Menu(message)


main()

bot.polling(long_polling_timeout=30)            #bot.polling(non_stop=True)

            #СДЕЛАТЬ ПРОВЕРКУ ВВОДА ДАТЫ НА РЕДАКТИРОВАНИИ
            #ПОЧИНИТЬ СОРТИРОВКУ В БЛИЖАЙШИХ ПЯТИ
