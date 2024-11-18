# # with open("weather_data.csv") as weather:
# #     weather_data = weather.readlines()
# #     data = []
# #     for values in weather_data:
# #         data.append(values.strip())

# # print(data)

# # import csv

# # with open("weather_data.csv") as weather:
# #     data = csv.reader(weather)
# #     temp_data = []
# #     for row in data:
# #         if row[1] != 'temp':
# #             temp_data.append(int(row[1]))

# # print(temp_data)

# import pandas as pd

# weather = pd.read_csv("weather_data.csv")
# # temperatures = weather["temp"]
# # temp_list = weather["temp"].to_list()
# # avg = weather["temp"].sum()/weather["temp"].count()
# # # print(avg)
# # print(weather["temp"].mean())

# # print(weather.temp.max())

# # print(weather[weather.temp == weather.temp.max()])

# monday_temp = weather[weather.day == "Monday"].temp
# monday_temp_f = (monday_temp * (9/5)) + 32
# print(monday_temp_f)

# data_dict = {
#     "students": ["Amy", "James", "Katy"],
#     "scores": [75, 85, 62]
# }

# df = pd.DataFrame(data_dict)

# print(df)

# df.to_csv("data.csv")

import pandas as pd # type: ignore

data = pd.read_csv("2018_Central_Park_Squirrel_Census.csv")

fur_dict = {}

fur_dict["Fur Color"] = data["Primary Fur Color"].dropna().unique()
fur_dict["Count"] = data["Primary Fur Color"].value_counts().to_list()

df = pd.DataFrame(fur_dict)

df.to_csv("squirrel_count.csv")


