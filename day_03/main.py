print("###########################################")
print("#         Welcome to Treasure Island      #")
print("###########################################\n")
print("###########################################")
print("#   Your mission is to find the treasure  #")
print("###########################################")

path = input("Choose your path L-Left or R-Right? ")
print(path)

if path.strip()[0] == "l" or path.strip()[0] == "L" :
    print("\nYou find a river on your way and on the other side there is house")
    path = input("Choose your action S-Swim or W-Wait for a boat? ")
    print(path)

    if path.strip()[0] == "w" or path.strip()[0] == "W" :
        print("\nAfter an hour of waiting a boat passes by and gives you a lift to the other side of the river.")
        print("You enter the house and the door locks automatically after you")
        path = input("You walk a bit and find three doors (as always 😅) R-Red, Y-Yellow and B-Blue. Which door do you choose? ")
        print(path)
        if path.strip()[0] == "r" or path.strip()[0] == "R":
            print("\nAfter opening the door, you accidentally hit a candle and it falls down and burns the curtains")
            print("Now everything is on fire and you a trying to get out but since the door is locked, you are trap inside and you burn to death")
            print("What a horrible way to die 💔")
        elif path.strip()[0] == "b" or path.strip()[0] == "B":
            print("\nYou chose a locked door! But since you are stubborn figure a way to open in")
            print("After getting in through the " + path + " door, you learn why it was locked, there were starving beasts and they and up eating you")
            print("What a horrible way to die 💔")
        elif path.strip()[0] == "y" or path.strip()[0] == "Y":
            print("\nYou lucky bastard! You found the treasure! Congratulations!")
            print("The exit door automatically opens and you get out of the house")
        else :
            print("\nYou won! You found the treasure!")
            print("But since you are curious, you tried to open the Blue door but was locked")
            print("You are also stubborn, so you just found a way to open it and soon after you find out why it was locked. There were starving beasts")
            print("You ran to the exit of the house but on your way to hit a candle and it falls down and burns the curtains")
            print("You managed to get to the exit door but it was locked 😬")
            print("The beasts find you and start to eat you. And then the you and the beasts notice the fire but it is already to late to run, so you all burn to death")
            print("What a horrible way to die 💔")
    else :
        print("\nYou were eaten by a crocodile and you died.")

else :
    print("\nYou feel into a hole and died.")

print("Game Over!")
