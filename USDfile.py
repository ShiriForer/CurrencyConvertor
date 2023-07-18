class USD:
    #set value for 1 usd
    def get_value(self):
        return 3.52
    #multiply the value of 1 USD by the user's amount
    def calculate(self, user_input):
        return user_input * self.get_value()