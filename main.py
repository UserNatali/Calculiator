import telebot

def read_file(file):
    return open('Token.txt', 'r')
bot = telebot.Telebot(Token)

@bot.message_handler(commands=['website'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Посетить вебсайт", url="https://itproger.com"))
    bot.send_message(message.chat.id, 'Перейдите на сайт', reply_markup=markup)
