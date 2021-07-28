# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#     print(temperature)
import pandas

data = pandas.read_csv("squirrel_census_data.csv")
grey_len = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_len = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_len = len(data[data["Primary Fur Color"] == "Black"])
data_dict = {
    "Fur_color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_len,cinnamon_len,black_len]
}
data = pandas.DataFrame(data_dict)
data.to_csv("new_squirrel.csv")


# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(data[data.temp == data.temp.max()])
# monday = data[data.day == "Monday"]
# print((int(monday.temp)*(9/5))+32)
# data_dict = {
#     "students": ["any", "james", "himal"],
#     "score": [76, 56, 65]
#
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")
# print(data)
