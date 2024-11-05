from string import ascii_lowercase

def encode(message, shift_number):
    encoded_message = ""

    for i in range(len(message)):
        if message[i] == " ":
            encoded_message += " "
            continue

        index = ascii_lowercase.find(message[i])

        if index == -1:
            encoded_message += message[i]
        else:
            position = index + shift_number
            if position > len(ascii_lowercase):
                position -= len(ascii_lowercase)

            encoded_message += ascii_lowercase[position]

    return encoded_message

def decode(message, shift_number):
    decoded_message = ""

    for i in range(len(message)):
        if message[i] == " ":
            decoded_message += " "
            continue

        index = ascii_lowercase.find(message[i])

        if index == -1:
            decoded_message += message[i]
        else:
            decoded_message += ascii_lowercase[index - shift_number]

    return decoded_message