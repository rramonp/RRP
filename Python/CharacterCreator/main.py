import _functions
import os

#VARIABLES
new_character = {}
user_option = 0

#MAIN
while True:
    try:           
        user_option = int(_functions.main_menu())
        if user_option == 5:
            print("Exiting...\n")
            break
        elif user_option == 1:
            new_character = _functions.create_character()
            continue
        elif user_option == 2:
            _functions.show_characters(_functions.total_characters)
            input("\nPress Enter to continue")
            continue
        elif user_option == 3:
            total_characters = _functions.delete_character(_functions.total_characters)
        elif user_option == 4:
            total_characters = _functions.modify_character(_functions.total_characters)
    except ValueError:
        os.system('cls')
        input("Returning to main menu...")
    
        
            
       











