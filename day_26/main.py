import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")
data_dict = {row.letter:row.code for (_, row) in data.iterrows()}

name = input("Your name?: ").upper()

print("Your name in phonetic alphabet is: ")

for letter in name: 
    print(data_dict[letter])

# print(data)
# print(data_dict)