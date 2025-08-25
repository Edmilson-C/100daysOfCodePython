from random import randint
import pandas as pd

# List comprehension - [<variable || an action> for <condition> if <condition>]
num_range = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
double_num = [n * 2 for n in num_range]
even_numbers = [n for n in num_range if n % 2 == 0]

print(double_num)
print(even_numbers)

# Dictionary comprehension - {<key>:<value> for <condition> if <condition>}
names = ["Edmilson", "Ethan", "Nicole"]
names_scores = {name:randint(1, 20) for name in names}
names_situation = {name:"Passou" for (name, score) in names_scores.items() if score >= 10}

print(names_scores)
print(names_situation)

# Pandas Interation
aux_data = {
    "names": [name for (name, _) in names_scores.items()],
    "scores": [score for (_, score) in names_scores.items()]
}
names_data = pd.DataFrame(aux_data)
print(names_data)

for (index, row) in names_data.iterrows():
    print(index, row)