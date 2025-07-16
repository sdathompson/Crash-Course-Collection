# # with open("weather_data.csv") as file:
# #     data = file.readlines()
# #     print(data)
#
# import csv
# import pandas
# import math
#
# # Python is a language used for data processing and data analysis
#
# # All this faff to read a row of data
#
# # with open("weather_data.csv") as data_file:
# #     data = csv.reader(data_file)
# #     temperatures = []
# #     for row in data:
# #         if row[1] != "temp":
# #             temperatures.append(int(row[1]))
# #     print(temperatures)
#
# data = pandas.read_csv("weather_data.csv")
# # Returns a Data-Frame (2-dimensional) object, like a table
# # a Data-Frame is like a dictionary. You're pulling out each column by the key
# # print(type(data))
# # Return a Series (1-dimensional) object, like a column
# # print(type(data['temp']))
#
# data_dict = data.to_dict()
# # print(data_dict)
#
# temp_lst = data["temp"].to_list()
# # print(f"Maximum temperature this week is going to be: {data['temp'].max()} degrees Celsius")
#
# # Getting rows in a data-frame
# # print(data[data.day == "Monday"])
#
# # The row where the temperature is at the maximum. Filter a column by a condition
# # print(data[data.temp == data.temp.max()])
#
# # Grabbing a certain cell. Get a row and use a key to grab the column again
# monday = data[data.day == "Monday"]
# # print(monday.condition)
#
# # Challenge - Get Monday's temperature in Fahrenheit
# # print((1.8 * monday.temp[0]) + 32)
#
# # Create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")
from turtledemo.nim import COLOR

import pandas

#TODO: Filter the rows with the gray, black, and cinnamon
squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur_column = squirrel_data["Primary Fur Color"]
unique_fur = list(set(fur_column.tolist()))
gray_squirrels_count = len(squirrel_data[fur_column == "Gray"])
blk_squirrels_count = len(squirrel_data[fur_column == "Black"])
red_squirrels_count = len(squirrel_data[fur_column == "Cinnamon"])

squirrel_dict = {
    "Fur Color": ["Gray", "Black", "Cinnamon"],
    "count": [gray_squirrels_count, blk_squirrels_count, red_squirrels_count]
}

data = pandas.DataFrame(squirrel_dict)
data.to_csv("fur_clr_cnt.csv")












