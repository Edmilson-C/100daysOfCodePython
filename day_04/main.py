import random

print("####################################################")
print("#         Welcome Rock, Paper & Scissors Game      #")
print("####################################################\n")
print("####################################################")
print("#                 Make your choice                 #")
print("####################################################")

options = ["Rock", "Paper", "Scissors"]

user = int(input("Type 0 - Rock, 1 - Paper, 2 - Scissors:\n"))
print(options[user])

machine = random.randint(0, 2)
print(f"Computer chose {options[machine]}")

if user == machine:
    print("It's a draw")
elif (user == 0 and machine == 1) or (user == 1 and machine == 2) or (user == 2 and machine == 0):
    print("You lose")
elif (user == 0 and machine == 2) or (user == 1 and machine == 0) or (user == 2 and machine == 1):
    print("You win")

