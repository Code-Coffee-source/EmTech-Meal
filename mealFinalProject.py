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

def main():
    main_options = {"1": ["Steak (P 900.00)", "900"],
                    "2": ["Salmon (P 850.00)", "850"],
                    "3": ["Chicken (P 300.00)", "300"],
                    "4": ["Cancel", "cancel()"]}

    for i in main_options.keys():
        print(f"[{i}] {main_options[i][0]}")

    return main_options[input("Which dish would you select? ").strip()][1]

def close_program():
    # closes the program
    global exit_program
    exit_program = True
    return ""

def main_menu():
    """Function for creating the main_menu for selecting main, side, dish, checkout and exit.
    Uses the main_menu_options dictionary
    """

    # dictionary containing main menu options
    # TODO: implement main(), sides(), drinks(), and checkout() functions
    main_menu_options = {"1": ["Mains", main()],
                         "2": ["Sides", "sides()"],
                         "3": ["Drinks", "drinks()"],
                         "4": ["Check-out", "checkout()"],
                         "5": ["Exit", close_program()]}

    print("Welcome! Please select an Option!")

    # prints all the options within the main_menu_options
    for i in main_menu_options.keys():
        print(f'[{i}] {main_menu_options[i][0]}')

    print("Note: One can only order one dish per each kind of food"
          "\n      and selecting a dish option overrides the selection. ")

    # Prompts the user to select an option and runs the corresponding function
    # strip() removes spaces that may have been added by the user
    return main_menu_options[input("What will you select? ").strip()][1]

def run_main_menu():
    # keeps the program running when in the main menu

    # catches KeyErrors (when selecting from values other than in the dictionary) in the main menu
    try:
        print(main_menu())
    except KeyError:
        print(f'Invalid selection! Please choose from the options provided. \n {divider} ')
        run_main_menu()


# sets exit program to false to avoid prematurely calling exit()
exit_program = False
if exit_program:
    exit()

# runs the program from the main menu
run_main_menu()
