from calculation import Calculation
class Commands:
    def extract_arg(self, message):
        global list
        arg = message.text
        status = arg.split()[1:]
        list = [float(item) for item in status]
        return list[0]

    def send_message(self, message, bot):
        bot.send_message(message.chat.id, 'Неправильно ввели число', parse_mode='html')

    def command_tons(self, message, bot):
        calculiator = Calculation(message)
        try:
            ints = self.extract_arg(message)
            tons = calculiator.tons(ints)
            bot.send_message(message.chat.id, str(tons), parse_mode='html')
        except ValueError:
            self.send_message(message, bot)
        except TypeError:
            self.send_message(message, bot)

    def command_gram(self, message, bot):
        calculiator = Calculation(message)
        try:
            ints = self.extract_arg(message)
            gram = calculiator.gram(ints)
            bot.send_message(message.chat.id, str(gram), parse_mode='html')
        except ValueError:
            self.send_message(message, bot)
        except TypeError:
            self.send_message(message, bot)

    def command_hundredweight(self, message, bot):
        calculiator = Calculation(message)
        try:
            ints = self.extract_arg(message)
            hundredweight = calculiator.hundredweight(ints)
            bot.send_message(message.chat.id, str(hundredweight), parse_mode='html')
        except ValueError:
            self.send_message(message, bot)
        except TypeError:
            self.send_message(message, bot)
