#!/usr/bin/env python3

# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

age     = int(age)
top_age = 90

years_remaining = top_age - age

days_in_year   = 365
weeks_in_year  = 52
months_in_year = 12

days   = round(years_remaining * days_in_year)
weeks  = round(years_remaining * weeks_in_year)
months = round(years_remaining * months_in_year)

print(f"You have {days} days, {weeks} weeks, and {months} months left.")
