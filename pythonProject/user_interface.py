import os


def simulation_main_menu():  # TODO attach to simulation
    """Main menu prompting user to choose an option"""
    validate_user_selection = (False, None)
    while validate_user_selection[0] is False:
        print("\t\t-Simulation menu-")
        print("\tPress -1- to run Sweepstakes")
        print("\tPress -2- to Add Sweesptakes")
        print("\t\tPress -3- to terminate simulation")
        user_input = try_parse_int(input())
        validate_user_selection = validate_main_menu(user_input)
    return validate_user_selection[1]


def assign_contestant_info():
    contestant_dictionary = {}
    print(f'Please enter your first name.')
    userinput = input()
    contestant_dictionary["firstname"] = userinput
    print(f'Please enter your last name.')
    userinput = input()
    contestant_dictionary["lastname"] = userinput
    print("Please enter your email address.")
    userinput = input()
    contestant_dictionary["email"] = userinput
    return contestant_dictionary


def menu_2():
    validate_user_selection = (False, None)
    while validate_user_selection[0] is False:
        print("\t\t-Simulation menu-")
        print("\tPress -1- to Add contestant")
        print("\tPress -2- to choose winner")
        print("\t\tPress -3- to terminate simulation")
        user_input = try_parse_int(input())
        validate_user_selection = validate_main_menu(user_input)
    return validate_user_selection[1]


def choose_manager_type():
    validate_user_selection = (False, None)
    while validate_user_selection[0] is False:
        print("\t\t-Simulation menu-")
        print("\tPress -1- for Stack")
        print("\tPress -2- for Queue")
        print("\t\tPress -3- to terminate simulation")
        user_input = try_parse_int(input())
        validate_user_selection = validate_main_menu(user_input)
        return validate_user_selection[1]



def validate_main_menu(user_input):
    """Validation function that checks if 'user_input' argument is an int 1-4. No errors."""
    switcher = {
        1: (True, 1),
        2: (True, 2),
        3: (True, 3)
    }
    return switcher.get(user_input, (False, None))


def output_text(text):
    """User input method that will print to console any string passed in as an argument"""
    print(text)


def clear_console():
    """Used for clearing out the console. No errors."""
    os.system('cls' if os.name == 'nt' else "clear")


def continue_prompt(text):
    """Validates a 'y' or 'yes' string and returns a True value. No errors."""
    switcher = {
        "y": True,
        "yes": True
    }
    user_input = input(text).lower()
    return switcher.get(user_input, False)


def try_parse_int(value):
    """Attempts to parse a string into an integer, returns 0 if unable to parse. No errors."""
    try:
        return int(value)
    except ValueError:
        return 0
