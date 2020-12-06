# meal final project


""" Things needed to be implemented
    1. Main select menu (first thing you'll see)
    2. Select menu for Mains, Sides and Drink (make dictionaries)
    3. Functions for all menus (makes it easier to for each menu to interact with each other)
    4. Check out function
    5. 16-20 test cases for perfect score
    6. Try-Except catches to minimum errors
    8. Combo identification
    7. !!IMPORTANT!! optimize code for efficiency, can be done last.
    Use time or timeit modules for speed and memory_profiler for memory usage
"""


# creates a divider for better UX
divider = "--------------------------------------------------------"

# orders dictionary
orders_dict = {"Main": "",
               "Side": "",
               "Drink": ""}


def cancel():
    # returns to the main menu when called
    print(divider)
    run_main_menu()


def main():
    """Function for creating the main dish menu for selecting main dishes .
    Uses the main_options dictionary
    """

    # dictionary containing main dish options
    main_options = {"1": ["Steak", format(900.00, '.2f')],
                    "2": ["Salmon", format(850.00, '.2f')],
                    "3": ["Chicken", format(300.00, '.2f')],
                    "4": ["Cancel", cancel]}

    # prints the menu
    for i in main_options.keys():
        print(f"[{i}] {main_options[i][0]} (P {main_options[i][1]})" if i != "4" else f"[{i}] {main_options[i][0]}")

    # get selection from user (returns a list)
    selection = main_options[input("Which dish would you like? ").strip()]
    if selection[1] is cancel:
        cancel()

    # get amount from user
    amount = input("How many would you like? ")

    # Records the inputs and updates orders_dict
    main_dish = {"Main": [selection[0], selection[1], amount, format(float(selection[1])*int(amount), '.2f')]}
    orders_dict.update(main_dish)

    # returns user to main menu
    cancel()


def sides():
    """Function for creating the side dishes menu for selecting side dishes .
    Uses the sides_options dictionary
    """

    # dictionary containing side dish options
    sides_options = {"1": ["Baked Potato", format(80.00, '.2f')],
                     "2": ["Mashed Potato", format(75.00, '.2f')],
                     "3": ["Steamed Vegetables", format(50.00, '.2f')],
                     "4": ["Cancel", cancel]}

    # prints the menu
    for i in sides_options.keys():
        print(f"[{i}] {sides_options[i][0]} (P {sides_options[i][1]})" if i != "4" else f"[{i}] {sides_options[i][0]}")

    # get selection from user (returns a list)
    selection = sides_options[input("Which dish would you like? ").strip()]
    if selection[1] is cancel:
        cancel()

    # get amount from user
    amount = input("How many would you like? ")

    # Records the inputs and updates orders_dict
    sides_dish = {"Side": [selection[0], selection[1], amount, format(float(selection[1])*int(amount), '.2f')]}
    orders_dict.update(sides_dish)

    # returns user to main menu
    cancel()


def drinks():
    """Function for creating the drinks menu for selecting drinks .
    Uses the drinks_options dictionary
    """

    # dictionary containing side dish options
    drink_options = {"1": ["Iced Tea", format(55.00, '.2f')],
                     "2": ["Root Beer", format(60.00, '.2f')],
                     "3": ["Water", format(20.00, '.2f')],
                     "4": ["Cancel", cancel]}

    # prints the menu
    for i in drink_options.keys():
        print(f"[{i}] {drink_options[i][0]} (P {drink_options[i][1]})" if i != "4" else f"[{i}] {drink_options[i][0]}")

    # get selection from user (returns a list)
    selection = drink_options[input("Which drink would you like? ").strip()]
    if selection[1] is cancel:
        cancel()

    # get amount from user
    amount = input("How many would you like? ")

    # Records the inputs and updates orders_dict
    drink_select = {"Drink": [selection[0], selection[1], amount, format(float(selection[1])*int(amount), '.2f')]}
    orders_dict.update(drink_select)

    # returns user to main menu
    cancel()


def checkout():
    """Function for calculating total and checking out.
    Uses the orders_dict dictionary
    """
    total = format(float(orders_dict["Main"][3])+float(orders_dict["Side"][3])+float(orders_dict["Drink"][3]), '.2f')

    # Prints the values in the orders_dict to the checkout format
    for i in orders_dict.keys():
        print(f'{i}  - {orders_dict[i][0]} - P{orders_dict[i][1]} x {orders_dict[i][2]} = {orders_dict[i][3]}')

    print(divider)

    print(f'TOTAL       P{total}')
    payment = float(input("Enter amount to be paid: ").strip())

    # Discount triggers if Chicken-Mash-Tea combo was ordered
    if orders_dict["Main"][0] == "Chicken":
        if orders_dict["Side"][0] == "Mashed Potato":
            if orders_dict["Drink"][0] == "Iced Tea":
                print('Chicken Mash Tea Combo gives 10% discount')
                discount = format(0.10 * float(total), '.2f')
                discounted = format(float(total) - float(discount), '.2f')
                print(f'DISCOUNT    P{discount}')
                print(f'DISCOUNTED  P{discounted}')
                total = discounted

    change = payment - float(total)
    change_f = format(change, '.2f')
    print(f'CHANGE      P{change_f}')

    close_program()


def close_program():
    # closes the program when called

    # print dict (debugging only remove when finished)
    print(orders_dict)

    exit()


def main_menu():
    """Function for creating the main_menu for selecting main, side, dish, checkout and exit.
    Uses the main_menu_options dictionary
    """

    # dictionary containing main menu options
    # TODO: implement sides(), drinks(), and checkout() functions
    main_menu_options = {"1": ["Mains", main],
                         "2": ["Sides", sides],
                         "3": ["Drinks", drinks],
                         "4": ["Check-out", checkout],
                         "5": ["Exit", close_program]}

    print("Welcome! Please select an Option!")

    # prints all the options within the main_menu_options
    for i in main_menu_options.keys():
        print(f'[{i}] {main_menu_options[i][0]}')

    print("Note: One can only order one dish per each kind of food"
          "\n      and selecting a dish option overrides the selection. ")

    # Prompts the user to select an option and runs the corresponding function
    # strip() removes spaces that may have been added by the user

    main_menu_options[input("What will you select? ").strip()][1]()


def run_main_menu():
    # keeps the program running when in the main menu

    # catches KeyErrors (when selecting from values other than in the dictionary) in the main menu
    try:
        print(main_menu())
    except KeyError:
        print(f'Invalid selection! Please choose from the options provided. \n {divider} ')
        run_main_menu()


if __name__ == "__main__":
    # runs the program from the main menu
    run_main_menu()
