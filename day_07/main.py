from random import randint

print("#########################################")
print("#      Welcome to the Pyhangman game    #")
print("#########################################\n")

words_list = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

chosen_word = words_list[randint(0, len(words_list) -1)]

lives = 6
blanks_filled = 0
users_results = ["_"] * len(chosen_word)

print("Guess the day of the week")
print(f"Lives: {lives}")
print("_ " * len(chosen_word))

while lives > 0 and blanks_filled < len(chosen_word):
    users_choice = input("\nChoose a letter: ")[0]

    if users_choice not in chosen_word:
        lives -= 1
        print("Wrong choice")
        print(f"Lives: {lives}")
    else:
        for i in range(len(chosen_word)):
            if users_choice == chosen_word[i]:
                users_results[i] = users_choice
                blanks_filled += 1

    print('  '.join(users_results))

if lives == 0:
    print("You lost!")
else:
    print("You won!")








# while users_choice.strip().casefold() != chosen_letter.strip().casefold():
#     users_choice = input("Guess the letter: ")
#
#     if users_choice.strip().casefold() != chosen_letter.strip().casefold():
#         print("Wrong letter")
#     else:
#         print("Right letter")
#         print(chosen_word)
#         print(chosen_letter)