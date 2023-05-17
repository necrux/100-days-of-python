#!/usr/bin/env python3
import pandas

CENSUS = '2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv'

data = pandas.read_csv(CENSUS)

gray = 0
red = 0
black = 0

for fur in data["Primary Fur Color"]:
    if fur == "Gray":
        gray += 1
    elif fur == "Cinnamon":
        red += 1
    elif fur == "Black":
        black += 1

squirrel_colors = {
    "Fur Color": ["Gray", "Red", "Black"],
    "Count": [gray, red, black],
}

data = pandas.DataFrame(squirrel_colors)
print(data)
data.to_csv("squirrel_colors.csv")