#!/usr/bin/env python3

import random
import os
import json
import requests
import hangman_art

print(hangman_art.logo)

word_endpoint = "https://random-word-api.herokuapp.com/word"
response      = requests.get(word_endpoint)
chosen_word   = json.loads(response.content)[0]

# Testing code
print(f'Pssst, the solution is {chosen_word}.')

display = []
for letter in chosen_word:
    display += "_"

lives = 6

guesses = []

while "_" in display:
    guess = input("\nGuess a letter: ").lower()
    os.system("clear")
    
    if guess in guesses:
        print(f"You've already guessed {guess}.")
        print(hangman_art.stages[lives])
    elif guess in chosen_word:
        print("Correct!")
        count = 0
        for letter in chosen_word:
            if letter == guess:
                display[count] = letter
            count += 1
        print(*display, sep = " ")
    else:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        print(hangman_art.stages[lives])
        if lives == 0:
            print("You lose.")
            exit(0)
    guesses += guess
print("You Win!")
