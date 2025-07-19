from menu import MENU

print("####################")
print("#      Welcome!    #")
print("####################\n")

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0.0

def report():
    for resource in resources:
       print(f"{resource.capitalize()}: {resources[resource]}ml")
    print(f"Money: ${money}")

while True:
    chosen_drink = input("What would you like? (espresso/latte/cappuccino) ").lower()

    if chosen_drink == "off":
        break

    if chosen_drink == "report":
        report()
        continue

    if chosen_drink != "espresso" and chosen_drink != "latte" and chosen_drink != "cappuccino":
        print("Wrong drink")
        continue

    ingredients = MENU[chosen_drink]["ingredients"]
    cost = MENU[chosen_drink]["cost"]

    if chosen_drink != "espresso" and  ingredients["milk"] > resources["milk"]:
        print("There is not enough milk")
        continue

    if ingredients["water"] > resources["water"]:
        print("There is not enough water")
        continue

    if ingredients["coffee"] > resources["coffee"]:
        print("There is not enough coffee")
        continue

    print("Insert the coins")
    quarters = int(input("How many quarters? "))
    if quarters == "off":
        break

    if quarters == "report":
        report()
        continue

    dimes = int(input("How many dimes? "))
    if dimes == "off":
        break

    if dimes == "report":
        report()
        continue

    nickles = int(input("How many nickles? "))
    if nickles == "off":
        break

    if nickles == "report":
        report()
        continue

    pennies = int(input("How many pennies? "))
    if pennies == "off":
        break

    if pennies == "report":
        report()
        continue

    amount = (quarters * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies * 0.01)

    change = round((amount - cost), 2)

    if change < 0:
        print("That's not enough money")
        continue

    if chosen_drink != "espresso":
        resources["milk"] -= ingredients["milk"]

    resources["water"] -= ingredients["water"]
    resources["coffee"] -= ingredients["coffee"]
    money += cost

    print(f"Your change is {change}")



