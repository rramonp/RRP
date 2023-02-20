characters = [
    {'Name': 'Elsa', 'Class': 'Rogue', 'Race': 'Gnome'}, 
    {'Name': 'Rafael', 'Class': 'Hunter', 'Race': 'Human'}
    ]

def show_characters(total_character):
    print("Current characters\n")
    for position,a in enumerate(total_character):
        print(f"Position:{position+1}")
        print(f"Name:{a['Name']}")
        print(f"Class:{a['Class']}")
        print(f"Human:{a['Race']}\n")

show_characters(characters)