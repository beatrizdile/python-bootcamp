# with open("weather_data.csv") as weather_file:
#     data = weather_file.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1].isdigit():
#             temperatures.append(row[1])
#
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
data_dict = data.to_dict()
data_list = data["temp"].to_list()

# average = sum(data_list) / len(data_list)
# print(average)

# get average in the row
print(data["temp"].mean())

# get the highest number in the row
print(data["temp"].max())

# get data in columns
print(data["condition"])
print(data.condition)

# get data in row
print(data[data.day == "Wednesday"])
print(data[data.temp == data.temp.max()])

# get a data from a row
max_temp = data[data.temp == data.temp.max()]
print(max_temp.day)

#convert celsius to fahrenheit
# print(max_temp)
# in_fahrenheit = (max_temp.temp * 9/5) + 32
# print(in_fahrenheit)

# Create a dataframe from scratch
data_dictionary = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

create_dataframe = pandas.DataFrame(data_dictionary)
create_dataframe.to_csv("new_data.csv")
