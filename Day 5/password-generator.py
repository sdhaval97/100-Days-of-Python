# Creating a password generator

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

# Asking the users for number of characters in their password
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = ""

# Creating loops to fetch random characters from each type (letters, symbols, and numbers)
letter_count = 0
for i in range(len(letters)):
    if letter_count < nr_letters:
        rand_index = random.randrange(len(letters))
        password += letters[rand_index]
        letter_count += 1

symbol_count = 0
for i in range(len(symbols)):
    if symbol_count < nr_symbols:
        rand_index = random.randrange(len(symbols))
        password += symbols[rand_index]
        symbol_count += 1

number_count = 0
for i in range(len(numbers)):
    if number_count < nr_numbers:
        rand_index = random.randrange(len(numbers))
        password += numbers[rand_index]
        number_count += 1

print(password)





