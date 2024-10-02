print("#####################################")
print("#   Welcome to the tip Calculator   #")
print("#####################################\n\n")

total = float(input("What was the total bill?\n"))
print(str(total) + " MT")

people = int(input("How many people to split the bill?\n"))
print(people)

tip = int(input("What percentage tip would you like to give? (0-50%)\n"))
print(tip)

payment = total / people + (total / 5 * (tip/100))

print(f"Each person should pay: {round(payment, 1)} MT")

# 124.54/5+(124.54/5*0.12)