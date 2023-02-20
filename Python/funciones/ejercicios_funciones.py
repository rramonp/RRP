import os

# 1- Declare a function add_two_numbers. 
# It takes two parameters and it returns a sum.

def suma(numero1, numero2):
    sumafinal = numero1 + numero2
    return sumafinal

# print(f"Tu resultado es: {suma(10,8)}") 


#2- Area of a circle is calculated as follows: area = π x r x r. 
# Write a function that calculates area_of_circle.

def area_circle(radius_entered):
    pi = 3.141592653589793
    area = float(pi*radius_entered*radius_entered)
    area = round(area, 2)
    return area

# radius_user = float(input("Enter the radius value:"))
# area1 = area_circle(radius_user)
# print(f"The area of your circle with radius {radius_user} is {area1}")


# 3- Write a function called add_all_nums which takes arbitrary number 
# of arguments and sums all the arguments. 
# # Check if all the list items are number types. 
# If not do give a reasonable feedback.

def crear_lista_numeros():
    lista = []
    while True:
        entered_value = int(input("Add value to list[0 to quit]:"))
        if entered_value == 0:
            break
        else:
            lista.append(entered_value)
    return lista

#lista1 = crear_lista_numeros()
#listasumada = sum(lista1)
#print(f"La suma de los valores de la lista {lista1} es {listasumada}")
 
#3- Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. 
# Write a function which converts °C to °F, convert_celsius_to-fahrenheit.

def convert_celsius_to_fahrenheit(celsius):
    farenheit = (((celsius*9/5)+32))
    farenheit = round(farenheit,2)
    return farenheit

# user_value = float(input("Enter the ºC value to convert to ºF: "))
# farenheit_value = convert_celsius_to_fahrenheit(user_value)
# print(f"{user_value} ºC = {farenheit_value} ºF")


# 5- Write a function called check-season, it takes a month parameter 
# and returns the season: Autumn, Winter, Spring or Summer.

spring = ["march", "april", "may"]
summer = ["june", "july", "august"]
autumm = ["september", "october", "november"]
winter = ["december", "january", "february"]

def check_season(month):
    if month2 in spring:
        return "Spring"
    elif month2 in summer:
        return "Summer"
    elif month2 in autumm:
        return "Aurumm"
    elif month2 in winter:
        return "Winter"
    elif month2 == "e":
        return "Error"
    else:
        return "Invalid month"
           
"""while True:
    month = input("Enter a month to calculate it's season ['E' to exit] ")
    month2 = month.lower()
    season = check_season(month)
    if season == "Error":
        print("Exiting...")
        break
    if season == "Invalid month":
        print("Invalid Month, please try again")
        continue
    print(f"The month [{month}] is in the [{season}] season")
"""    

#6- Write a function called calculate_slope which return the slope 
# of a linear equation
#Porcentaje de Pendiente = Altura / Base * 100           
        
def calculate_slope(altura, longitud):
    pendiente = altura/longitud*100
    return(pendiente)

'''
os.system('cls')
print("**Vamos a calcular el porcentaje de una pendiente**")

altura = float(input("Introduce la altura: "))
altura = round(altura, 2)
longitud = float(input("Introduce la longitud de la base: "))
longitud = round(longitud, 2)

pendiente = float(calculate_slope(altura, longitud))
pendiente = round(pendiente,2)

print(f"El % de pendiente para altura: {altura}m con longitud: {longitud}m es de {pendiente}º")
'''

#7- Quadratic equation is calculated as follows: ax² + bx + c = 0. 
# Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn
          
def solve_quadratic_eqn(a,b,c,x):
    result = (a*x)** + b*x + c
    return result      
'''
os.system('cls')
while True:
    a = float(input("Enter [a] value: "))
    if a == 0:
        input("[a] cant be zero, please try again")
        continue
    else:
        break
b = float(input("Enter [b] value: ")) 
c = float(input("Enter [c] value: "))  
x = float(input("Enter [x] value: "))            
        
resultado = solve_quadratic_eqn(a,b,c,x)
print(f"({a}*{x})** + {b}*{x} + {c} = {resultado}")
'''
          
#8 - Declare a function named print_list. 
# It takes a list as a parameter and it prints out each element of the list.    

def print_list(arguments):
    mylist = []
    for a in arguments:
        mylist.append(a)
    return mylist

'''os.system('cls')
arguments = []
while True:
    user_argument = input("Enter argument to add to the list [E to exit] ")
    if user_argument == "E":
        break
    arguments.append(user_argument)
    
lista_rellenada = print_list(arguments)
for i, value in enumerate(lista_rellenada):
    print(i, value)    
'''

# 9 - Declare a function named reverse_list. 
# It takes an array as a parameter and it returns the reverse of the array (use loops).
  
def reverse_list(array):
    return list(reversed(array))

def sort_list(array):
    return list(sorted(array))

def sort_list_descending(array):
    return list(sorted(array, reverse=True))

'''
os.system('cls')
array = []
my_list2 = []
sorted_list = []
sorted_list_descending = []

while True:
    value = int(input("Enter value to add to the list [0 to exit]: "))
    if value == 0:
        break
    array.append(value)   

my_list2 = reverse_list(array)
sorted_list = sort_list(array)
sorted_list_descending = sort_list_descending(array)

print(f'\nEntered list:: {array}')                         
print(f'Reversed list: {my_list2}')
print(f'Sorted list: {sorted_list}')
print(f'Sorted list (descending): {sorted_list_descending}\n') 
'''

#10 Declare a function named capitalize_list_items. 
# It takes a list as a parameter and it returns a capitalized list of items
       
def capitalize_list_items(list_of_integers):
    capitalized_list = []
    for item in list_of_integers:
        capitalized_list.append(item.capitalize())
    return capitalized_list

'''    
os.system('cls')
entered_list = []
finished_list = []

while True:
    word = input("Enter a word, it will be converted to lower capital [0 to stop]: ")
    if word == "0":
        break
    word = word.lower()
    entered_list.append(word)

finished_list = capitalize_list_items(entered_list)
print(f'Entered list; {entered_list}')
print(f'Entered list with capitals: {finished_list}')
'''

#11 - Declare a function named add_item. It takes a list and an item parameters. 
# It returns a list with the item added at the end.        

'''def get_user_strings():
    user_strings = []
    while True:
        user_input = input("Enter a string (or 'q' to exit): ")
        if user_input == "q":
            break
        user_strings.append(user_input)
    return user_strings

def add_user_strings_to_list(all_lists, user_strings):
    all_lists.append(user_strings)
    return all_lists

all_lists = ["Batman", "Capitan America"]
user_strings = get_user_strings()
all_lists = add_user_strings_to_list(all_lists, user_strings)
print(all_lists)
'''

'''def new_user_values():
    new_user_list = []
    while True:
        entered_value = input("Enter countries to add to the animal list[q to exit]: ")
        if entered_value == 'q':
            os.system('cls')
            break
        new_user_list.append(entered_value)
    return new_user_list
        
def first_list():
    user_list = []
    while True:
        entered_value = input("Enter animals to make a list[q to exit]: ")
        if entered_value == 'q':
            os.system('cls')
            break
        user_list.append(entered_value)
    return user_list
    
def add_new_values_to_list(second_list, new_user_list):
    new_user_list.extend(second_list)
    return new_user_list
    
os.system('cls')
new_user_list = first_list()
second_list = new_user_values()
final_list = (add_new_values_to_list(second_list, new_user_list))

print("FINAL LIST:")
for a, thing in enumerate(final_list):
    print (a, thing.title())
'''     

    
animals = {
    'type': ['dog', 'cat', 'shark'], 
    'color': ['white', 'black', 'red'], 
    'gender': ['male', 'female', 'both'], 
    'age': ['1', '3', '5']
}

os.system('cls')
for key, value_list in animals.items():
    print(f"{key.title()}:")
    for position, value in enumerate(value_list):
        print(f"\t {position}-{value.title()}")



    















































   
      
    



