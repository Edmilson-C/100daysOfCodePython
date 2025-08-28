from random import shuffle, randint
from string import ascii_letters, digits

list_symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

letters = randint(8, 10)
symbols = randint(2, 4)
numbers = randint(2, 4)

def generate_password():
    password = []
    generated_password = ""

    for _ in range(letters):
        password.append(ascii_letters[randint(0, len(ascii_letters) - 1)])

    for _ in range(numbers):
        password.append(digits[randint(0, len(digits) - 1)])

    for _ in range(symbols):
        password.append(list_symbols[randint(0, len(list_symbols) - 1)])

    shuffle(password)

    for letter in password:
        generated_password += letter

    return generated_password
