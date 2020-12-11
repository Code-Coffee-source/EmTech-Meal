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
default_orders = [None, None, None, format(00.00, '.2f')]

# orders dictionary
orders_dict = {"Main": default_orders,
               "Side": default_orders,
               "Drink": default_orders}


def cancel():
    # returns to the main menu when called
    print(divider)
    main_menu()


def close_program():
    # closes the program when called
    exit()


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
    print(f'{divider} \n Select a main dish \n {divider}')
    for i in main_options.keys():
        print(f"[{i}] {main_options[i][0]} (P {main_options[i][1]})" if i != "4" else f"[{i}] {main_options[i][0]}")

    # get selection from user and update the value of Main under orders_dict
    try:
        selection = main_options[input("Which drink would you like? ").strip()]
        if selection[1] is cancel:
            cancel()

        # get amount from user
        amount = input("How many would you like? ")

        # Records the inputs and updates orders_dict
        main_select = {
            "Main": [selection[0], selection[1], amount, format(float(selection[1]) * int(amount), '.2f')]}
        orders_dict.update(main_select)

        # returns user to main menu
        cancel()

    except KeyError:
        print(f'Invalid selection! Please choose from the options provided. \n {divider} ')
        main()


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
    print(f'{divider} \n Select a side dish \n {divider}')
    for i in sides_options.keys():
        print(f"[{i}] {sides_options[i][0]} (P {sides_options[i][1]})" if i != "4" else f"[{i}] {sides_options[i][0]}")

    # get selection from user and update the value of Main under orders_dict
    try:
        selection = sides_options[input("Which drink would you like? ").strip()]
        if selection[1] is cancel:
            cancel()

        # get amount from user
        amount = input("How many would you like? ")

        # Records the inputs and updates orders_dict
        sides_select = {
            "Side": [selection[0], selection[1], amount, format(float(selection[1]) * int(amount), '.2f')]}
        orders_dict.update(sides_select)

        # returns user to main menu
        cancel()

    except KeyError:
        print(f'Invalid selection! Please choose from the options provided. \n {divider} ')
        sides()


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
    print(f'{divider} \n Select a drink \n {divider}')
    for i in drink_options.keys():
        print(f"[{i}] {drink_options[i][0]} (P {drink_options[i][1]})" if i != "4" else f"[{i}] {drink_options[i][0]}")

    # get selection from user and update the value of Main under orders_dict
    try:
        selection = drink_options[input("Which drink would you like? ").strip()]
        if selection[1] is cancel:
            cancel()

        # get amount from user
        amount = input("How many would you like? ")

        # Records the inputs and updates orders_dict
        drink_select = {
            "Drink": [selection[0], selection[1], amount, format(float(selection[1]) * int(amount), '.2f')]}
        orders_dict.update(drink_select)

        # returns user to main menu
        cancel()

    except KeyError:
        print(f'Invalid selection! Please choose from the options provided. \n {divider} ')
        drinks()




def checkout():
    """Function for calculating total and checking out.
    Uses the orders_dict and combo_meals dictionary
    """

    combo_meals = {"Chicken Mashed Potato Iced Tea": ["Chicken Mash Tea", format(.10, '.2f')],
                   "Steak Steamed Vegetables Root Beer": ["Steak Veg Beer", format(.15, '.2f')]
                   }

    total = format(float(orders_dict["Main"][3]) + float(orders_dict["Side"][3]) + float(orders_dict["Drink"][3]),
                   '.2f')

    # Prints the values in the orders_dict to the checkout format
    for i in orders_dict.keys():
        if orders_dict[i][0] is not None:
            print(f'{i}  - {orders_dict[i][0]} - P{orders_dict[i][1]} x {orders_dict[i][2]} = {orders_dict[i][3]}')
        else:
            print(f' No {i} selected')

    if total != format(0.00, '.2f'):
        print(divider)
        print(f'TOTAL       P{total}')
        payment = float(input("Enter amount to be paid: ").strip())
    else:
        print(divider)
        print('No items selected \n'
              'Closing program...')
        close_program()


    meal_list = []

    for i in orders_dict:
        meal_list.append(orders_dict[i][0])

    try:
        str_meal = ' '.join(meal_list)

        if str_meal in combo_meals.keys():
            combo_meal = combo_meals[str_meal]
            discount = format(float(combo_meal[1]) * float(total), '.2f')
            discounted = format(float(total) - float(discount), '.2f')
            print(f'{combo_meal[0]} Combo gives {"{:.0%}".format(float(combo_meal[1]))} discount \n'
                  f'DISCOUNT    P{discount} \n'
                  f'DISCOUNTED  P{discounted}')
            total = discounted

    except TypeError:
        pass

    # Checks for possible combo meals and apply discount

    change = payment - float(total)
    change_f = format(change, '.2f')
    print(f'CHANGE      P{change_f}')

    close_program()


def main_menu():
    """Function for creating the main_menu for selecting main, side, dish, checkout and exit.
    Uses the main_menu_options dictionary
    """

    # dictionary containing main menu options
    main_menu_options = {"1": ["Mains", main],
                         "2": ["Sides", sides],
                         "3": ["Drinks", drinks],
                         "4": ["Check-out", checkout],
                         "5": ["Exit", close_program]}

    print("Welcome! Please select an Option!")

    # prints all the options within the main_menu_options
    try:
        for i in main_menu_options.keys():
            print(f'[{i}] {main_menu_options[i][0]}')
    except KeyError:
        print(f'Invalid selection! Please choose from the options provided. \n {divider} ')

    print("Note: One can only order one dish per each kind of food"
          "\n      and selecting a dish option overrides the selection. ")

    # Prompts the user to select an option and runs the corresponding function
    # strip() removes spaces that may have been added by the user

    main_menu_options[input("What will you select? ").strip()][1]()


if __name__ == "__main__":
    # runs the program from the main menu
    main_menu()
