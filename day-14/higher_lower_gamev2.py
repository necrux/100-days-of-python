#!/usr/bin/env python3

import random
from os import system
from art import logo, vs
from game_data import data

def set_screen():
    """Clear the screen and print the game logo."""
    system("clear")
    print(logo)

def get_challenger(a):
    """Summon a challenger; ensure that it is not the same entity."""
    b = random.choice(data)
    return b

    while a == b:
        b = random.choice(data)

def set_score(score):
    score += 1
    set_screen()
    print(f"You're right! Current score: {score}")
    return score

def set_match(a, b):
    """Present the challengers."""
    a_name           = a["name"]
    a_follower_count = a["follower_count"]
    a_description    = a["description"]
    a_country        = a["country"]
    
    b_name           = b["name"]
    b_follower_count = b["follower_count"]
    b_description    = b["description"]
    b_country        = b["country"]

    print(f"Compare A: {a_name}, a {a_description}, from {a_country}.")
    print(vs)
    print(f"Compare B: {b_name}, a {b_description}, from {b_country}.")

    if a_follower_count > b_follower_count:
        return a
    else:
        return b    

def main():
    set_screen()
    
    # Get match.
    score = 0
    a = random.choice(data)
    b = get_challenger(a)
    
    # Set match.
    winner = set_match(a, b)
    
    while True:
        # Ask for answer.
        answer = input("Who has more followers? Type 'A' or 'B': ").lower()
        
        # Validate user input.
        if answer != "a" and answer != "b":
            print("Invalid selection.")
            exit(1)
        
        # Compare results; print win/lose.
        if answer == "a" and winner == a:
            score = set_score(score)
        elif answer == "b" and winner == b:
            score = set_score(score)
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            exit(0)
        
        # If user wins, set a new match with the higher challenger from the previous round in position A.
        if a != winner:
            a = b
        b = get_challenger(a)
        
        # Repeat until they lose; print final score.
        winner = set_match(a, b)

if __name__ == "__main__":
    main()
