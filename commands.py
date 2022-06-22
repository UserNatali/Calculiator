import telebot
from class_Calculation import Calculation


def read_file(path):
    return open(path, 'r')


token = str(read_file('Token.txt').readline())
bot = telebot.TeleBot(token)


class Commands:
    def extract_arg(self, message):
        global list
        arg = message.text
        status = arg.split()[1:]
        list = [float(item) for item in status]
        return list[0]

    def command_tons(self, message):
        calculiator = Calculation(message)
        try:
            ints = self.extract_arg(message)
            tons = calculiator.tons(ints)
            bot.send_message(message.chat.id, str(tons), parse_mode='html')
        except ValueError:
            bot.send_message(message.chat.id, 'Неправильно ввели число', parse_mode='html')
        except TypeError:
            bot.send_message(message.chat.id, 'Неправильно ввели число', parse_mode='html')

    def command_gram(self, message):
        calculiator = Calculation(message)
        try:
            ints = self.extract_arg(message)
            gram = calculiator.gram(ints)
            bot.send_message(message.chat.id, str(gram), parse_mode='html')
        except ValueError:
            bot.send_message(message.chat.id, 'Неправильно ввели число', parse_mode='html')
        except TypeError:
            bot.send_message(message.chat.id, 'Неправильно ввели число', parse_mode='html')

    def command_hundredweight(self, message):
        calculiator = Calculation(message)
        try:
            ints = self.extract_arg(message)
            hundredweight = calculiator.hundredweight(ints)
            bot.send_message(message.chat.id, str(hundredweight), parse_mode='html')
        except ValueError:
            bot.send_message(message.chat.id, 'Неправильно ввели число', parse_mode='html')
        except TypeError:
            bot.send_message(message.chat.id, 'Неправильно ввели число', parse_mode='html')
