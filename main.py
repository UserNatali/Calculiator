import telebot


def read_file(path):
    return open('Token.txt', 'r')


token = str(open('Token.txt', 'r').readline())
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['tons'])
def yourCommand(message):
    calculiator = Function(message)
    tons = calculiator.tons(message)
    bot.send_message(message.chat.id, str(tons), parse_mode='html')

@bot.message_handler(commands=['gram'])
def yourCommand(message):
    calculiator = Function(message)
    gram = calculiator.gram(message)
    bot.send_message(message.chat.id, str(gram), parse_mode='html')


class Function:
    def __init__(self, message):
        self.message = message

    def extract_arg(self, arg):
        self.arg = arg
        status = arg.split()[1:]
        list = [float(item) for item in status]
        return list

    def tons(self, message):
        ints = self.extract_arg(message.text)
        number = ints[0] / 1000
        return number

    def gram(self, message):
        ints = self.extract_arg(message.text)
        number = ints[0] * 1000
        return number


bot.polling(none_stop=True)
