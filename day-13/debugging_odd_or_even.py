#!/usr/bin/env python3

number = int(input("Which number do you want to check?"))

# There was only 1 = sign, meaning that it was assigning the value rather than comparing.  
if number % 2 == 0:
  print("This is an even number.")
else:
  print("This is an odd number.")
