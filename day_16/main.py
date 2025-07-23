from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

print("#######################################################")
print("#      Welcome! This is the coffee machine with OOP   #")
print("#######################################################\n")

menu = Menu()
coffeeMaker = CoffeeMaker()
moneyMachine = MoneyMachine()

while True:
    chosen_drink = input("What would you like? (espresso/latte/cappuccino) ").lower()

    if chosen_drink == "off":
        break

    if chosen_drink == "report":
        coffeeMaker.report()
        moneyMachine.report()
        continue

    found_drink = menu.find_drink(chosen_drink)

    if not found_drink:
        continue

    if not coffeeMaker.is_resource_sufficient(found_drink):
        continue

    if not moneyMachine.make_payment(found_drink.cost):
        continue

    coffeeMaker.make_coffee(found_drink)