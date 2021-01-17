"""
MEMBERS

AGUARES, Maveron Tyriel V.
PADILLON, Cy Wenvir A.

DOCUMENTATION

Problem Breakdown
1. Display content on screen showing options and taking input
2. Display orders and ask for payment on checkout (allow for incomplete orders and add discount function)
3. Display receipt: contains order/s, total, change and, if applicable, discount

Additional concepts used outside class
1. List and Dictionary data types - used to store values and options
2. Format function - used to format number values to always show 2 decimal values
3. Functions (function calls and parameters) - used on repeated lines of code allowing for smaller number of lines
4. Try-except - used to catch errors instead of if statements
5. F-strings (another type of concatenation) - fastest string concatenation method
6. Exit function used to close program when close_program() is called
7. List Comprehension - way of making a list from iterables in one line
8. str.upper(), str.capitalize(), str.strip() - string manipulation methods; convert to uppercase,
    convert to sentence case, remove whitespace at start and end
9. Ternary operators - one-line if-else statements (reduces lines of code)
10. \n - escape character for new line similar to html <\br>

Sources
1. W3Schools.com
2. StackOverflow.com
3. Prior python programming experience

Usage
1. Users will be brought to the main menu.
2. If users chooses options 1-3 they will be brought to the respective option select menu (see # 6-7.)
2. Choosing option 4 in the main menu will bring users to the check out menu (see #8)
5. Choosing option 5 in the main menu ask for user input before closing the program
6. Selecting an order within the items presented will ask for the amount of the order
7. Selecting cancel will return the user to the main menu
8. The checkout menu will originally display the orders made and the total then ask if they will be paying
9. *Inputting "y or yes" (and any of the spelling changes) into the prompt will proceed to payment (see #12)
10. *Inputting "n or no" (and any of the spelling changes) into the prompt will return to the main menu
11. *Inputting anything else will ask the user to "respond accordingly" and repeat the prompt
12. Payment prompt will display the total amount input
13. *Paying an amount less than total will redisplay the payment prompt and total
14. *Inputting anything other than integers will redisplay the payment prompt
15. Successful payment (equal to or greater than total) will print receipt and ask for input before closing
Note: Items with * are in a loop and the same rules apply per loop

Features
1. Catches KeyErrors when users input anything outside the presented options (main menu and options menu)
2. Easy to add items into dictionaries making it very dynamic and portable
3. Dictionaries follow the same format so other option menus can be made making use of the same format
4. Users are guided through every procedure and fallbacks are in place for error handling in the case of missed input
5. The receipt also has a nice UI to make the Command Line Interface CLI look cleaner when the program is running
6. Clicking on file icon in explorer also works, no need to call from CLI (cmd or bash) or enter python interface

"""

divider = "--------------------------------------------------"
default_order_format = [None, None, None, format(00.00, '.2f')]
orders_dict = {"main dish": default_order_format,
               "side dish": default_order_format,
               "drink": default_order_format}


def close_program():
    input("|--------Press enter to close the program---------|")
    exit()


def check_out():
    """Function for calculating total and checking out.
        Uses the orders_dict and combo_meals dictionary
    """

    combo_meals = {"Chicken Mashed Potato Iced Tea": ["Chicken Mash Tea", format(.10, '.2f')],
                   "Steak Steamed Vegetables Root Beer": ["Steak Veg Beer", format(.15, '.2f')]
                   }

    total = format(
        float(orders_dict["main dish"][3]) + float(orders_dict["side dish"][3]) + float(orders_dict["drink"][3]),
        '.2f')

    print(divider)

    # Prints the values in the orders_dict to the receipt format
    for order in orders_dict.keys():
        if orders_dict[order][0] is not None:
            print(f'{order.capitalize()} -> {orders_dict[order][0]} -> \u20B1 {orders_dict[order][1]} x {orders_dict[order][2]} = \u20B1 {orders_dict[order][3]}')
        else:
            print(f'No {order} selected')

    if total != format(0.00, '.2f'):
        print(divider)
        print(f'TOTAL       \u20B1 {total}')

        ask_if_pay = True
        paying = False

        while ask_if_pay:

            pay = input("Proceed to payment? \n"
                        f"Type 'Y' to pay or 'N' to return to the main menu: ").upper().strip()

            if pay == 'Y' or pay == 'YES':
                paying = True
                ask_if_pay = False
            elif pay == 'N' or pay == 'NO':
                paying = False
                ask_if_pay = False
            else:
                print(f"{divider} \nPlease respond accordingly \n{divider}")

        # asks user if they will pay. Brings user back to main menu if declined proceed to payment
        if paying:

            ask_payment = True
            print(f'TOTAL       \u20B1 {total}')

            while ask_payment:
                try:
                    payment = float(input("Enter amount to be paid: ").strip())
                    ask_payment = False
                except ValueError:
                    print(f"{divider}\n Please enter the amount as a number (ie. 1000)")


            while paying:

                while payment < float(total):
                    print(f"{divider} \nInsufficient amount. Total is \u20B1 {total}. "
                          f"You are missing \u20B1 {format(float(total) - payment, '.2f')}")

                    try:
                        payment += float(input(f"Please add the missing amount: ").strip())
                    except ValueError:
                        print(f"{divider}\n Please enter the amount as a number (ie. 1000)")

                paying = False

        else:
            create_main_menu()

    else:
        print(divider)
        print('No items selected \n')
        close_program()


    change = payment - float(format(float(total), '.2f'))
    # prints a receipt
    print(f'{divider} \n'
          f'                     RECEIPT                      \n'
          f'{divider}')

    for order in orders_dict.keys():
        if orders_dict[order][0] is not None:
            print(f'{orders_dict[order][0]} -> x {orders_dict[order][2]} => \u20B1 {orders_dict[order][3]}')
        else:
            print(f'No {order} selected')

    # uses list comprehension to create a list to counter check against discount values
    str_meal = ' '.join([orders_dict[i][0] for i in orders_dict if orders_dict[i][0] is not None])

    if str_meal in combo_meals.keys():
        combo_meal = combo_meals[str_meal]
        discount = format(float(combo_meal[1]) * float(total), '.2f')
        discounted = format(float(total) - float(discount), '.2f')
        print(f'{divider} \n'
              f'{combo_meal[0]} Combo gives {"{:.0%}".format(float(combo_meal[1]))} discount \n'
              f'DISCOUNT    \u20B1 {total} X {"{:.0%}".format(float(combo_meal[1]))} = \u20B1 {discount} \n'
              f'DISCOUNTED  \u20B1 {total} -  \u20B1 {discount} = \u20B1 {discounted}')
        total = discounted

    print(f'{divider} \n'
          f'TOTAL       \u20B1 {total} \n'
          f'PAYMENT     \u20B1 {format(payment,".2f") } \n'
          f'CHANGE      \u20B1 {format(change, ".2f")} \n'
          f'{divider}')

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

main_menu_options = {"1": ["main dish", "order main dish", main_dish_options],
                     "2": ["side dish", "order side dish", side_dish_options],
                     "3": ["drink", "order drink", drink_options],
                     "4": ["check out", "checkout order", check_out],
                     "5": ["exit", "exit program", close_program]}


def create_main_menu():
    print(f'{divider} \n Welcome! Please select an option below. \n{divider}')

    for option in main_menu_options.keys():
        print(f'[{option}] {main_menu_options[option][1].capitalize()}')

    try:
        selection = main_menu_options[input(f"What would you like to do? ").strip()]
        create_option_select_menu(selection[2]) if type(selection[2]) is dict else selection[2]()

    except KeyError:
        print('Invalid selection')
        create_main_menu()




def create_option_select_menu(options_dict):
    order_type = options_dict['type']

    print(f'{divider} \n Please select a {order_type}. \n{divider}')

    for option in options_dict.keys():
        if option != 'type':
            print(f"[{option}] {options_dict[option][0]} P {options_dict[option][1]}" if options_dict[option][
                                                                              0] != 'Cancel' else f"[{option}] {options_dict[option][0]}")

    # Print "Invalid selection" if input is not in dict
    try:

        user_order = options_dict[input("What would you like to order. Press '4' to return to the main menu: ").strip()]

        if user_order[0] == 'Cancel':
            create_main_menu()
        else:
            amount = int(input(f"Enter the amount: ").strip())
            amnt_price = [amount, (float(user_order[1]) * amount)]

            orders_dict.update(dict([(order_type, tuple(user_order + amnt_price))]))

    except KeyError:
        print("Invalid Selection")
        create_option_select_menu(options_dict)

    create_main_menu()


# Code will run from here
if __name__ == "__main__":
    create_main_menu()
