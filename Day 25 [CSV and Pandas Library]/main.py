import csv
import pandas

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
#     print(temperatures)
#
# data = pandas.read_csv("weather_data.csv")
# print(data["temp"].max())
#
# # Get data in a row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
#
# # Create a dataframe from scratch
# data_dict = {
#     "students": ["Humaid", "Mahmood"],
#     "scores": [65, 52]
# }
# dataa = pandas.DataFrame(data_dict)
# # Save as csv
# dataa.to_csv("new_data.csv")


data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
data_col = data["Primary Fur Color"]
cinnamon_count = 0
grey = 0
black = 0
for data in data_col:
    if data == "Gray":
        grey += 1
    elif data == "Cinnamon":
        cinnamon_count += 1
    elif data == "Black":
        black += 1

print(cinnamon_count, grey, black)

sq_count = {
    "Fur Color": ["Grey", "Red", "Black"],
    "Count": [grey, cinnamon_count, black]
}
dataa = pandas.DataFrame(sq_count)
dataa.to_csv("Squirrel_count.csv")