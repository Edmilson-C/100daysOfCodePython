import csv
import pandas as pd

# with open("weather-data.csv") as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         if row[1].isnumeric():
#             temperatures.append(int(row[1]))
#         print(row)
#     print(temperatures)
#     data = file.readlines()

# data = pd.read_csv("weather-data.csv")
# temp_list = data["temp"].to_list()
# average_temp = data["temp"].mean() # or average_temp = sum(temp_list) / len(temp_list)
# max_temp = data["temp"].max()
# monday = data[data.day == "Monday"] # Get the row

# print(temp_list)
# print(average_temp)
# print(max_temp)
# print(data["condition"])
# print(data.condition)
# print(monday)

data = pd.read_csv("2018-Central-Park-Squirrel-Census-Squirrel-Data.csv")

gray_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
black_squirrels = len(data[data["Primary Fur Color"] == "Black"])
cinnamon_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])

data_dict = {
    "Fur Color": ["Gray", "Black", "Cinnamon"],
    "Count": [gray_squirrels, black_squirrels, cinnamon_squirrels]
}

pd.DataFrame(data_dict).to_csv("squirrel-data.csv")

print(gray_squirrels)
print(black_squirrels)
print(cinnamon_squirrels)