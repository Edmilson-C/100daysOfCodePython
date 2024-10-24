import random
from random import shuffle

print("#############################################")
print("#        Welcome to PyPassword Generator    #")
print("#############################################\n")


list_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
list_numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
list_symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

letters = int(input("How many letters would you like in your password?\n"))
symbols = int(input("How many symbols would you like in your password?\n"))
numbers = int(input("How many numbers would you like in your password?\n"))

password = []

for _ in range(letters):
    password.append(list_letters[random.randint(0, len(list_letters) - 1)])

for _ in range(numbers):
    password.append(list_numbers[random.randint(0, len(list_numbers) - 1)])

for _ in range(symbols):
    password.append(list_symbols[random.randint(0, len(list_symbols) - 1)])

shuffle(password)

print("You generated password is: " + ''.join(password))