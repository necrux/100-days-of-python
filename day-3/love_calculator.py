#!/usr/bin/env python3

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

combined_string = (name1 + name2).lower()

count1 = 0
count2 = 0

count1 += combined_string.count("t")
count1 += combined_string.count("r")
count1 += combined_string.count("u")
count1 += combined_string.count("e")

count2 += combined_string.count("l")
count2 += combined_string.count("o")
count2 += combined_string.count("v")
count2 += combined_string.count("e")

score = int(str(count1) + str(count2))

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")
