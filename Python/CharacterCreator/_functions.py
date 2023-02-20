import os
total_characters = []

def main_menu():
    os.system('cls')
    print("""***** CHARACTER MENU *****\n
    1- Create new character
    2- Show characters
    3- Delete character
    4- Modify character
    5- Exit""")
    option = input("\n---> ")
    return option

def create_character():
    os.system('cls')
    new_character = {
        'Name': 'None',
        'Profession': 'None',
        'Race': 'None'
    }
    print("***** CHARACTER CREATION *****\n")
    while True:
        value = input("Enter name: ")  
        new_character['Name'] = value
        value = input("Enter profession: ")  
        new_character['Profession'] = value
        value = input("Enter race: ")   
        new_character['Race'] = value
        print("\nCharacter created (Press Enter to continue)")
        input()
        total_characters.append(new_character)
        return new_character

def show_characters(total_character):
    os.system('cls')
    print("***** CURRENT CHARACTERS *****\n")
    for position, a in enumerate(total_character):
        print(f"Position:{position}")
        print(f"Name:{a['Name']}")
        print(f"Profession:{a['Profession']}")
        print(f"Race:{a['Race']}\n")   

def delete_character(character_name):
    while True:
        os.system('cls')
        show_characters(character_name)
        character_to_delete = int(input("Which [position] you want to delete? ['E' to return]:  "))
        try: 
            del character_name[character_to_delete]
        except IndexError:
            os.system('cls')
            input("This character does not exist, please try again...\n")
           
def modify_character(character_name):
    while True:
        os.system('cls')
        show_characters(character_name)
        character_to_modify = int(input("Which [position] you want to modify? ['E' to return]:  "))
        try: 
            while True:
                os.system('cls')
                print("***** MODIFY CHARACTER *****\n")
                print(total_characters[character_to_modify])
                print("\n1- Name")
                print("2- Profession")
                print("3- Race")
                print("4- Choose a different character")
                modify_option = int(input("\nWhich value you want to modify ['Q' to Exit]: "))
                try: 
                    if modify_option == 1:
                        new_value = input("\nEnter new name: ")
                        total_characters[character_to_modify]['Name'] = new_value
                        continue
                    if modify_option == 2:
                        new_value = input("\nEnter new profession: ")
                        total_characters[character_to_modify]['Profession'] = new_value
                        continue
                    if modify_option == 3:
                        new_value = input("\nEnter new race: ")
                        total_characters[character_to_modify]['Race'] = new_value
                        continue
                    if modify_option == 4:
                        break
                except ValueError:
                    os.system('cls')
                    input("Returning to main menu...")
        except IndexError:
            os.system('cls')
            input("This character does not exist, please try again...\n")
    
