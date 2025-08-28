from random import shuffle, randint, choice
from string import ascii_letters, digits

list_symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

letters = randint(8, 10)
symbols = randint(2, 4)
numbers = randint(2, 4)

def generate_password():
    generated_password = ""
    password = ([choice(ascii_letters) for _ in range(letters)] + [choice(digits) for _ in range(numbers)] +
                [choice(list_symbols) for _ in range(symbols)])

    shuffle(password)

    for letter in password:
        generated_password += letter

    return generated_password
