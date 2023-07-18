class ILS:
    #set value for 1 ILS
    def get_value(self):
        return 0.28
    #multiply the value of 1 ILS by the user's dollars amount
    def calculate(self, user_input):
        return user_input * self.get_value()