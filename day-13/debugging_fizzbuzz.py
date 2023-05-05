#!/usr/bin/env python3

for number in range(1, 101):
  # Was using an or instead of an and.
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  # Was using if instead of elif.
  elif number % 3 == 0:
    print("Fizz")
  # Was using if instead of elif.
  elif number % 5 == 0:
    print("Buzz")
  else:
    # Was printing with [ ] around the number.
    print(number)
