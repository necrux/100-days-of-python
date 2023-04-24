#!/usr/bin/env python3

# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

two_digit_number     = str(two_digit_number)
first_digit          = two_digit_number[0]
second_digit         = two_digit_number[1]
two_digit_number_sum = int(first_digit) + int(second_digit)

print(first_digit + " + " + second_digit + " = " + str(two_digit_number_sum))
