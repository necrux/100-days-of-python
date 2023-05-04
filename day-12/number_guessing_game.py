#!/usr/bin/env python3
# Ideas to add.
#  Store the guess in 2 dicts (higher and lower guesses) and allow the player to view their guess at any time.
#  Let the player choose to play a new game after.

from random import choice
from art import logo

def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

    if difficulty == "hard":
        lives = 5
    else:
        lives = 10
    return lives
    
def main():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    lives  = set_difficulty()
    number = choice(range(1, 101)) 
    
    while True:
        print(f"You have {lives} attempts remaining to guess the number.")
        if lives == 0:
            print("Game Over.")
            break
        else:
            guess = int(input("Make a guess: "))
        if guess > number:
            print("Too high.")
            if lives != 1:
                print("Guess again.")
        elif guess < number:
            print("Too low.")
            if lives != 1:
                print("Guess again.")
        else:
            print("Correct! You win!")
            break
        lives -= 1

if __name__ == "__main__":
    main()
