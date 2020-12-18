divider = ("--------------------------------------------------")


def close_program():
	exit()

def check_out():
	print("Check out")
	
def cancel():
	create_menu(main_menu_options)


main_dish_options = {"1": ["Steak", format(900.00, '.2f')],
                    "2": ["Salmon", format(850.00, '.2f')],
                    "3": ["Chicken", format(300.00, '.2f')],
                    "4": ["Cancel", cancel]}

side_dish_options = {"1": ["Baked Potato", format(80.00, '.2f')],
                     "2": ["Mashed Potato", format(75.00, '.2f')],
                     "3": ["Steamed Vegetables", format(50.00, '.2f')],
                     "4": ["Cancel", cancel]}


drink_options = {"1": ["Iced Tea", format(55.00, '.2f')],
                     "2": ["Root Beer", format(60.00, '.2f')],
                     "3": ["Water", format(20.00, '.2f')],
                     "4": ["Cancel", cancel]}




main_menu_options = {"1": ["main dish", main_dish_options],
					 "2": ["side dish", side_dish_options],
					 "3": ["drink", drink_options],
					 "4": ["check out", check_out],
					 "5": ["exit", close_program]}



def create_main_menu(main_menu_dict = main_menu_options):

	
	print(f'{divider} \n Welcome! Please select an option below. \n {divider}')

	for i in main_menu_dict.keys():
		print(f'[{i}] {main_menu_dict[i][0].capitalize()}')

	try:
		selection = main_menu_dict[input(f"What would you option would you like? ").strip()]
	except KeyError:
		print('Invalid selection')
		create_main_menu()

	print(selection[1])

	if selection[1] is dict: 
		create_options_menu(selection[1])
	else:
		selection[1]()

def create_options_menu(options_dict):
	print(options_dict)





create_main_menu()

