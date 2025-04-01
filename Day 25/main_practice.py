# import csv
#
# def retrieve_temps():
#     with open("weather_data.csv") as csv_file:
#         temp_list_out = []
#         temp_list = csv.reader(csv_file)
#         for element in temp_list:
#             if element[1] != "temp":
#                 temp_list_out.append(int(element[1]))
#
#     return temp_list_out
#
# print(retrieve_temps())

# import pandas as pd

#Read and average temperatures in list
# df = pd.read_csv("weather_data.csv")
# templist = df["temp"].tolist()
# temp_avg = average(templist)
# print (f"{temp_avg:.2f}")
#OR
#print(df["temp"].mean())  #<--Uses Pandas Library

#find Max value
# print(df["temp"].max())
# print(df.condition)
# print(df[df.temp == df.temp.max()])
# monday = df[df.day == "Monday"]
# temp = (monday["temp"] * 9/5) + 32
# print(temp)

# #Create a dataframe from scratch:
# data_dict = {
#     "students":["Missy", "Bo", "John"],
#     "scores":[90, 70, 60]
# }
# data = pd.DataFrame(data_dict)
# print(data)
# data.to_csv("students.csv")

import pandas as pd


cp_dict = {"color": ["black", "cinnamon", "brown"], "count": [0, 0, 0]}
cp_data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

#Returns a series that counts squirrel's by their primary color
color_counts = cp_data["Primary Fur Color"].value_counts()
print(type(color_counts))
print(color_counts)
#Output series to csv named "color_counts.csv"
color_counts.to_csv("color_counts.csv")