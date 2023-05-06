#!/usr/bin/env python3

import os
import random
import art
from game_data import data

def set_match(a, b):
    a_name           = a['name']
    a_follower_count = a['follower_count']
    a_description    = a['description']
    a_country        = a['country']

    b_name           = b['name']
    b_follower_count = b['follower_count']
    b_description    = b['description']
    b_country        = b['country']

    print(f"Compare A: {a_name}, a {a_description}, from {a_country}.")
    print(art.vs)
    print(f"Compare B: {b_name}, a {b_description}, from {b_country}.")
    return

def reset_screen():
    os.system("clear")
    print(art.logo)

def main():
    reset_screen()
    score = 0
    
    a = random.choice(data)
    b = random.choice(data)
    
    while a == b:
        b = random.choice(data)
    
    while True:
        set_match(a, b)
        answer = input("Who has more followers? Type 'A' or 'B': ").lower()
        if answer == 'a':
            answer = a['follower_count']
            if answer > b['follower_count']:
                reset_screen()
                score += 1
                print(f"You're right! Current score: {score}")
            else:
                reset_screen()
                print(f"Sorry, that's wrong. Final score: {score}")
                exit(0)
        elif answer == 'b':
            answer = b['follower_count']
            if answer > a['follower_count']:
                reset_screen()
                score += 1
                print(f"You're right! Current score: {score}")
            else:
                reset_screen()
                print(f"Sorry, that's wrong. Final score: {score}")
                exit(0)
        if a['follower_count'] < b['follower_count']:
            a = random.choice(data)
            while a == b:
                a = random.choice(data)
        else:
            b = random.choice(data)
            while a == b:
                b = random.choice(data)
    else:
        print('Invalid selection.')
        exit(1)

if __name__ == "__main__":
    main()
