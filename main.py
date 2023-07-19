from USDfile import USD
from ILSfile import ILS

# create an object for each class
usd = USD()
ils = ILS()
# create a results list
results_list = []

print("Welcome to the currency converter")

def get_user_value():
    # user chooses conversion method
    user_choice = input("Please choose an option: \n"
                        "1. Dollars to Shekels \n"
                        "2. Shekels to Dollars \n")
    # convert USD to ILS
    if user_choice == "1":
        # ask for the user's amount
        while True:
            try:
                value_to_convert = float(input("Please enter an amount to convert "))
                if value_to_convert < 0:
                    print("Positive numbers only")
                else:
                    break
            except ValueError:
                print("Sorry, not a valid number")

        usd_result = (usd.calculate(value_to_convert))
        formatted_usd_result = f"{usd_result:.2f}"
        # save result in a list
        results_list.append(formatted_usd_result)
        # show result
        print(str(value_to_convert) + " " + "USD are" + " " + str(formatted_usd_result) + " " + "ILS")
        start_over()

    # convert ILS to USD
    elif user_choice == "2":
        # ask for the user's amount
        while True:
            try:
                value_to_convert = float(input("Please enter an amount to convert "))
                if value_to_convert < 0:
                    print("Positive numbers only")
                else:
                    break
            except ValueError:
                print("Sorry, not a valid number")
        ils_result = (ils.calculate(value_to_convert))
        formatted_ils_result = f"{ils_result:.2f}"
        # save result in a list
        results_list.append(formatted_ils_result)
        # show result
        print(str(value_to_convert) + " " + "ILS are" + " " + str(formatted_ils_result) + " " + "USD")
        start_over()

    #user made an invalid choice:
    else:
        print("Sorry, I did not understand your choice. Please choose again ")
        get_user_value()

def end_screen():
    print("Thanks for using our currency converter")
    # show results list
    for result in results_list:
        print(result)
    try:
        file = open("C:\\Users\\shiri pc\\PycharmProjects\\CurrencyConversionProject\\Results", "a", encoding="utf-8")
        file.write(result)
        file.close()
    except IOError:
        pass

def start_over():
    while True:
        start_over = input("Would you like to start over? Y/N ").upper()
        if start_over == "Y":
            main()
            break
        elif start_over == "N":
            end_screen()
            break
        # user made an invalid choice
        else:
            print("Invalid choice, please try again")

def main():
    # print("Welcome to the currency converter")
    get_user_value()

main()



