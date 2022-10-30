import telebot
from config import Token
from telebot import types
bot=telebot.TeleBot(Token)

Admin=bool
UserId=int
def Error(message):
    global UserId
    bot.send_message(UserId, "Клавиатурой бота пользуйся, дебил!")

def main():

    @bot.message_handler(commands=['start'])
    def Hello(message):
        global UserId
        UserId = message.chat.id
        ReKeyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        ReKeyboard.add('Начать')
        bot.send_message(UserId, f'Привет, {UserId},через меня ты можешь узнать свои ближайшие дедлайны', reply_markup=ReKeyboard)
    @bot.message_handler(regexp='Начать')
    def Menu(message):
        bot.send_message(UserId, "Ну что ж, приступим!", reply_markup=types.ReplyKeyboardRemove())

        Admin=False
        if (UserId==545762112):
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
            but10 = types.InlineKeyboardButton('В начало', callback_data='ToMenu')
            InKeyboard.add(but1, but2, but3, but4, but5, but6, but7, but8, but9, but10)

            if call.data=="Know":
                bot.edit_message_text('Выберите предмет', UserId, message_id=call.message.message_id, reply_markup=InKeyboard)

                @bot.callback_query_handler(func=lambda call: True)
                def Subject():
                    if call.data =='InProf': bot.send_message(UserId, "leeee")
                    if call.data == 'Nosyreva': ''
                    if call.data == 'English': ''
                    if call.data == 'Informatics': ''
                    if call.data == 'Math': ''
                    if call.data == 'BBC': ''
                    if call.data == 'Prog': ''
                    if call.data == 'Physics': ''
                    if call.data == 'PE': ''
                    if call.data == 'ToMenu':
                        bot.delete_message(UserId, message_id=call.message.message_id)
                        Menu(call.message)
            elif call.data=="Edit": ''


main()

bot.polling(none_stop=True)