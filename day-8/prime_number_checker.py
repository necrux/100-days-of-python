#!/usr/bin/env python3

#Write your code below this line 👇

def prime_checker(number):
    if number == 1:
        print("It's not a prime number.")
    elif number == 2:
        print("It's a prime number.")
    elif number % 2 == 0:
        print("It's not a prime number.")
    else:
        for check in range(3, number + 1, 2):
            if number % check == 0:
                print("It's not a prime number.")
                break
            else:
                print("It's a prime number.")
                break

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
