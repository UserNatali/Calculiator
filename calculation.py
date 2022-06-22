class Calculation:
    def __init__(self, message):
        self.message = message

    def tons(self, ints):
        number = ints / 1000
        return number

    def gram(self, ints):
        number = ints * 1000
        return number

    def hundredweight(self, ints):
        number = ints / 100
        return number
