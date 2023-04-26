#!/usr/bin/env python3

# Import the random module here

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random

guests_count = len(names) - 1

victim = random.randint(0, guests_count)

print(names[victim] + " is going to buy the meal today!")
