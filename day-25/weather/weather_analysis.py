#!/usr/bin/env python3
import csv
import pandas

#with open("weather_data.csv") as file:
#    data = csv.reader(file)
#    temperatures = []
#    for row in data:
#        if row[1] != "temp":
#            temperatures.append(int(row[1]))
#
#print(temperatures)

data = pandas.read_csv("weather_data.csv")

temps = data.temp.tolist()
max = data.temp.max()

print(data[data.temp == max])