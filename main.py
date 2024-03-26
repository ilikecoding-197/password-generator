"""
The user interface.
"""

# Imports
from generator import generate_password, letter_groups # To generate the password
from utils import get_yes_or_no, spilt_number_into_two_halves
from threading import Thread

def get_user_options():
    """
    Gets the options the user wants for a password.
    """

    letter_group_options = []
    for letter_group_name in letter_groups.keys():
        if get_yes_or_no(f"Do {letter_group_name}?"):
            letter_group_options.append(letter_group_name)
    
    while True:
        length = input("Length? ")

        if not length.isdigit():
            print("Please enter a number.")
            continue
        
        length = int(length)
        break

    return {
        "letter_groups": letter_group_options,
        "length": length
    }
        
def main():
    """
    The user interface.
    """

    print("Welcome to Password Generator!")
    print()
    while True:
        print("Options:")
        print("1. Generate a password")
        print("2. Generate multiple.")
        print("3. Exit")

        option = input("What would you like to do?")

        if not option.isdigit():
            print("Please enter a number.")
            continue
        
        option = int(option)
        
        if not 0 < option < 4:
            print("Please enter a number between 1 and 3.")
            continue
        
        if option ==  1:
            options = get_user_options()

            print("Your password:", generate_password(options["letter_groups"], options["length"]))
        elif option == 2:
            options = get_user_options()

            while True:
                amount_of_passwords = input("Amount? ")

                if not amount_of_passwords.isdigit():
                    print("Please enter a number.")
                    continue
                
                amount_of_passwords = int(amount_of_passwords)
                break
            
            passwords = [generate_password(options["letter_groups"], options["length"]) for _ in range(amount_of_passwords)]

            print(f"Your passwords: ")

            for password in passwords:
                print(password)
        elif option == 3:
            print("Bye!")
            break


if __name__=="__main__":
    main()