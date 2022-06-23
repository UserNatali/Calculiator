import telebot
from commands import Commands


def read_file(path):
    return open(path, 'r')


token = str(read_file('Token.txt').readline())
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def hello(message):
    bot.send_message(message.chat.id, f'Привіт, {message.from_user.first_name}. Нажміть команду /help',
                     parse_mode='html')


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id,
                     'За допомогою команд /tons, /gram, /hundredweight, ви зможете перевести кілограми '
                     'в тони, грами, центнери відповідно. Для цього наберіть команду і через пробіл'
                     ' кількість кілограм. Наприклад, /tons 5000', parse_mode='html')


@bot.message_handler(commands=['tons'])
def commands_for_tons(message):
    com = Commands()
    return com.command_tons(message, bot)


@bot.message_handler(commands=['gram'])
def commands_for_gram(message):
    com = Commands()
    return com.command_gram(message, bot)


@bot.message_handler(commands=['hundredweight'])
def commands_for_hundredweight(message):
    com = Commands()
    return com.command_hundredweight(message, bot)


bot.polling(none_stop=True)
