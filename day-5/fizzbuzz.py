#!/usr/bin/env python3
#Write your code below this row 👇

for number in range(1, 101):
    three = False
    five  = False

    if number % 3 == 0:
        three = True
    if number % 5 == 0:
        five = True

    if three and five:
        print("FizzBuzz")
    elif three:
        print("Fizz")
    elif five:
        print("Buzz")
    else:
        print(number)
