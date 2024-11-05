from utils import encode
from utils import decode

print("####################################")
print("#      Welcome to Caesar Cipher    #")
print("####################################\n")


condition = "yes"

while condition.lower() == "yes" or condition.lower() == "y":
    mode = input("\nType \"encode\" to encrypt or type \"decode\" to decrypt: ")

    message = input("Type your message: ")

    shift_number = int(input("Type the shift number: "))

    if mode == "encode":
        result = encode(message.lower(), shift_number)
    else:
        result = decode(shift_number = shift_number, message = message.lower())

    print(f"Here is the {mode} result {result}")

    condition = input("Do you want to continue? (Yes/No): ")