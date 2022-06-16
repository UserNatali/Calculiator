import telebot
from telebot import types

def read_file(path):
    return open('Token.txt', 'r')


token = str(open('Token.txt', 'r').readline())
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привіт, <b>{message.from_user.first_name} <u>{message.from_user.last_name} </u></b>, введіть кількість кілограм'
    bot.send_message(message.chat.id, mess, parse_mode='html')

@bot.message_handler(content_types=['text'])
def send_tona(message):
     mess = float(message.text) * 1000
     return bot.send_message(message.chat.id, str(mess), parse_mode='html')


@bot.message_handler(commands=['convert'])
def convert(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)

    tona = types.KeyboardButton('Перевести в тони')
    #gramm = types.KeyboardButton('Перевести в грами')
    markup.add(tona)
    mess = float(message.text) * 1000
    bot.send_message(message.chat.id, str(mess), reply_markup=markup)

# @bot.message_handler(commands=['convert'])
# def convert(message.text, message.chat.id, answer})





bot.polling(none_stop=True)
