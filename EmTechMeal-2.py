divider = "--------------------------------------------------"
default_orders = [None, None, None, format(00.00, '.2f')]
orders_dict = {"main dish": default_orders,
               "side dish": default_orders,
               "drink": default_orders}


def close_program():
    exit()


def check_out():
    """Function for calculating total and checking out.
        Uses the orders_dict and combo_meals dictionary
        """

    combo_meals = {"Chicken Mashed Potato Iced Tea": ["Chicken Mash Tea", format(.10, '.2f')],
                   "Steak Steamed Vegetables Root Beer": ["Steak Veg Beer", format(.15, '.2f')]
                   }

    total = format(float(orders_dict["main dish"][3]) + float(orders_dict["side dish"][3]) + float(orders_dict["drink"][3]),
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


def cancel():
    create_main_menu()


main_dish_options = {"1": ["Steak", format(900.00, '.2f')],
                     "2": ["Salmon", format(850.00, '.2f')],
                     "3": ["Chicken", format(300.00, '.2f')],
                     "4": ["Cancel", cancel],
                     "type": "main dish"}

side_dish_options = {"1": ["Baked Potato", format(80.00, '.2f')],
                     "2": ["Mashed Potato", format(75.00, '.2f')],
                     "3": ["Steamed Vegetables", format(50.00, '.2f')],
                     "4": ["Cancel", cancel],
                     "type": "side dish"}

drink_options = {"1": ["Iced Tea", format(55.00, '.2f')],
                 "2": ["Root Beer", format(60.00, '.2f')],
                 "3": ["Water", format(20.00, '.2f')],
                 "4": ["Cancel", cancel],
                 "type": "drink"}

main_menu_options = {"1": ["main dish", main_dish_options],
                     "2": ["side dish", side_dish_options],
                     "3": ["drink", drink_options],
                     "4": ["check out", check_out],
                     "5": ["exit", close_program]}


def create_main_menu():
    print(f'{divider} \n Welcome! Please select an option below. \n {divider}')

    for i in main_menu_options.keys():
        print(f'[{i}] {main_menu_options[i][0].capitalize()}')

    try:
        selection = main_menu_options[input(f"What would you option would you like? ").strip()]

    except KeyError:
        print('Invalid selection')
        create_main_menu()

    create_options_menu(selection[1]) if type(selection[1]) is dict else selection[1]()


def create_options_menu(options_dict):
    add_to_order = lambda x: orders_dict.update(dict([(order_type, x)]))

    order_type = options_dict['type']

    print(f'{divider} \n Please select a {order_type}. \n {divider}')

    for i in options_dict.keys():
        if i != 'type':
            print(f"[{i}] {options_dict[i][0]} P {options_dict[i][1]}" if options_dict[i][
                                                                              0] != 'Cancel' else f"[{i}] {options_dict[i][0]}")

    user_order = options_dict[input("What would you like to order. Press '4' to return to the main menu: ").strip()]
    amount = int(input(f"Enter the amount: ").strip())

    if user_order[0] != 'Cancel':
        amnt_price = [amount, (float(user_order[1]) * amount)]

        add_to_order(tuple(user_order + amnt_price))

    create_main_menu()


create_main_menu()

print(orders_dict)
