def get_name_and_surname():
    name = input("Enter your name: ")
    surname = input("Enter your surname: ")
    return name, surname

# Call the function and store the result in two variables
first_name, last_name = get_name_and_surname()

# Print the result
print("Your name is:", first_name, last_name)
