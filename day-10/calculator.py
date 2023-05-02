#!/usr/bin/env python3
from art import logo

print(logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {'+': add,
              '-': subtract,
              '*': multiply,
              '/': divide,
             }

def calculator():
    num1 = float(input("What's the first number?: "))
    calc = 'y'
    
    while calc == 'y':
        for key in operations:
            print(key)
        operation = input("Pick an operation: ")
        num2      = float(input("What's the next number?: "))
        
        calc_func = operations[operation]
        answer    = calc_func(num1, num2)
        
        print(f'{num1} {operation} {num2} = {answer}')
        calc = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
    calculator()

calculator()
